"""
从 arXiv 官方 HTML 版本提取论文图片
优先使用 arxiv.org/html/（更新快），回退到 ar5iv
使用同步请求，避免 asyncio 事件循环冲突
"""
import re
import requests
from concurrent.futures import ThreadPoolExecutor, as_completed
from typing import List, Dict, Optional
from tqdm import tqdm


# arXiv 官方 HTML 版本（首选，更新更快）
ARXIV_HTML_BASE = "https://arxiv.org/html/"
# ar5iv 备选（某些旧论文可能只有这个）
AR5IV_BASE = "https://ar5iv.labs.arxiv.org/html/"

# 请求超时
TIMEOUT = 30


def fetch_html(url: str) -> Optional[str]:
    """获取 HTML 内容（同步）"""
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Referer': 'https://arxiv.org/',
    }
    try:
        resp = requests.get(url, headers=headers, timeout=TIMEOUT)
        if resp.status_code == 200:
            return resp.text
        return None
    except Exception as e:
        return None


def extract_arxiv_id(arxiv_id: str) -> str:
    """提取纯净的 arXiv ID (去掉版本号)"""
    # 2512.14689v1 -> 2512.14689
    match = re.match(r'(\d+\.\d+)', arxiv_id)
    return match.group(1) if match else arxiv_id.split('v')[0]


def ensure_version(arxiv_id: str) -> str:
    """确保 arXiv ID 包含版本号（默认 v1）"""
    # 如果已有版本号，直接返回
    if re.search(r'v\d+$', arxiv_id):
        return arxiv_id
    # 否则添加 v1
    return f"{arxiv_id}v1"


def parse_images_from_html(html: str, arxiv_id: str, base_url: str = None) -> List[Dict]:
    """
    从 arXiv HTML 中解析图片
    返回: [{"url": "...", "caption": "...", "figure_id": "figure1"}, ...]
    
    Args:
        html: HTML 内容
        arxiv_id: arXiv ID
        base_url: 图片的基础 URL（如 https://arxiv.org/html/2512.14689v1/）
    """
    images = []
    seen_urls = set()
    
    # 默认使用 arXiv 官方 HTML
    if base_url is None:
        base_url = f"{ARXIV_HTML_BASE}{arxiv_id}/"
    
    # 过滤词（跳过网站图标等）
    skip_keywords = ['icon', 'logo', 'badge', 'button', 'social', 'static/browse', 'cornell', 'arxiv-logo', 'data:image']
    
    def should_skip(src):
        src_lower = src.lower()
        return any(kw in src_lower for kw in skip_keywords)
    
    def build_url(img_src):
        if img_src.startswith('http'):
            return img_src
        elif img_src.startswith('data:'):
            return None  # 跳过 data URI
        elif img_src.startswith('/'):
            # 绝对路径，提取域名
            from urllib.parse import urlparse
            parsed = urlparse(base_url)
            return f"{parsed.scheme}://{parsed.netloc}{img_src}"
        else:
            # 相对路径
            return f"{base_url.rstrip('/')}/{img_src}"
    
    # 方法1: 匹配 figure 标签中的图片
    figure_pattern = re.compile(
        r'<figure[^>]*(?:id=["\']([^"\']*)["\'])?[^>]*>.*?'
        r'<img[^>]*src=["\']([^"\']+)["\'][^>]*>.*?'
        r'(?:<figcaption[^>]*>(.*?)</figcaption>)?.*?</figure>',
        re.DOTALL | re.IGNORECASE
    )
    
    for match in figure_pattern.finditer(html):
        fig_id = match.group(1) or f"fig_{len(images)}"
        img_src = match.group(2)
        caption = match.group(3) or ""
        
        if should_skip(img_src):
            continue
        
        # 清理 caption 中的 HTML 标签
        caption = re.sub(r'<[^>]+>', '', caption).strip()
        caption = ' '.join(caption.split())[:200]
        
        img_url = build_url(img_src)
        
        if img_url not in seen_urls:
            images.append({
                "url": img_url,
                "caption": caption,
                "figure_id": fig_id
            })
            seen_urls.add(img_url)
    
    # 方法2: 直接匹配 assets 目录中的图片（ar5iv 常用格式）
    asset_pattern = re.compile(
        r'<img[^>]*src=["\']([^"\']*(?:/assets/|/x\d+)[^"\']*\.(png|jpg|jpeg|gif))["\']',
        re.IGNORECASE
    )
    
    for match in asset_pattern.finditer(html):
        img_src = match.group(1)
        if should_skip(img_src):
            continue
        
        img_url = build_url(img_src)
        
        if img_url not in seen_urls:
            images.append({
                "url": img_url,
                "caption": "",
                "figure_id": f"img_{len(images)}"
            })
            seen_urls.add(img_url)
    
    # 方法3: 匹配其他主要图片（png/jpg）
    if len(images) < 3:
        general_pattern = re.compile(
            r'<img[^>]*src=["\']([^"\']+\.(png|jpg|jpeg))["\']',
            re.IGNORECASE
        )
        
        for match in general_pattern.finditer(html):
            img_src = match.group(1)
            if should_skip(img_src):
                continue
            
            img_url = build_url(img_src)
            
            if img_url not in seen_urls:
                images.append({
                    "url": img_url,
                    "caption": "",
                    "figure_id": f"img_{len(images)}"
                })
                seen_urls.add(img_url)
    
    return images


def extract_paper_images(arxiv_id: str, max_images: int = 5) -> List[Dict]:
    """
    提取单篇论文的图片（同步）
    优先使用 arxiv.org/html/（官方，更新快），失败则回退到 ar5iv
    
    Args:
        arxiv_id: arXiv ID (如 2512.14689 或 2512.14689v1)
        max_images: 最多提取几张图片
    
    Returns:
        图片列表 [{"url": "...", "caption": "...", "figure_id": "..."}, ...]
    """
    clean_id = extract_arxiv_id(arxiv_id)
    full_id = ensure_version(arxiv_id)  # 确保有版本号
    
    # 优先尝试 arXiv 官方 HTML 版本（需要完整版本号）
    html_url = f"{ARXIV_HTML_BASE}{full_id}"
    base_url = f"{ARXIV_HTML_BASE}{full_id}/"
    html = fetch_html(html_url)
    
    # 如果官方版本失败，回退到 ar5iv
    if not html:
        html_url = f"{AR5IV_BASE}{clean_id}"
        base_url = f"{AR5IV_BASE}{clean_id}/"
        html = fetch_html(html_url)
    
    if not html:
        return []
    
    images = parse_images_from_html(html, arxiv_id, base_url)
    
    # 过滤掉 None URL
    images = [img for img in images if img.get("url")]
    
    # 优先选择有 caption 的图片
    images_with_caption = [img for img in images if img["caption"]]
    images_without_caption = [img for img in images if not img["caption"]]
    sorted_images = images_with_caption + images_without_caption
    
    return sorted_images[:max_images]


def batch_extract_images(
    papers: List[Dict],
    max_images_per_paper: int = 3,
    concurrency: int = 5,
    show_progress: bool = True
) -> Dict[str, List[Dict]]:
    """
    批量提取多篇论文的图片（使用线程池，同步方式）
    
    Args:
        papers: 论文列表，每个需要有 arxiv_id 字段
        max_images_per_paper: 每篇论文最多提取几张图片
        concurrency: 并发数
        show_progress: 是否显示进度条
    
    Returns:
        {arxiv_id: [图片列表], ...}
    """
    results = {}
    
    # 过滤出有 arxiv_id 的论文
    valid_papers = [p for p in papers if p.get("arxiv_id")]
    
    if not valid_papers:
        return results
    
    def extract_one(paper):
        arxiv_id = paper.get("arxiv_id", "")
        images = extract_paper_images(arxiv_id, max_images_per_paper)
        return arxiv_id, images
    
    with ThreadPoolExecutor(max_workers=concurrency) as executor:
        futures = {executor.submit(extract_one, p): p for p in valid_papers}
        
        iterator = as_completed(futures)
        if show_progress:
            iterator = tqdm(iterator, total=len(futures), desc="提取图片", unit="篇")
        
        for future in iterator:
            try:
                arxiv_id, images = future.result()
                if arxiv_id:
                    results[arxiv_id] = images
            except Exception as e:
                pass  # 静默忽略单篇论文的错误
    
    return results


# 测试函数
def test_extract():
    """测试图片提取"""
    test_id = "2512.14689"
    print(f"测试提取: {test_id}")
    images = extract_paper_images(test_id)
    print(f"找到 {len(images)} 张图片:")
    for img in images:
        print(f"  - {img['figure_id']}: {img['url'][:60]}...")
        if img['caption']:
            print(f"    Caption: {img['caption'][:80]}...")
    return images


if __name__ == "__main__":
    test_extract()
