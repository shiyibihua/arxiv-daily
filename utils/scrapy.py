from typing import List, Tuple, Dict, Optional
from datetime import datetime, timedelta, timezone
from zoneinfo import ZoneInfo
import re
import json
import arxiv
import requests
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor, as_completed
from tqdm import tqdm

US_EASTERN = ZoneInfo("US/Eastern")

def load_tags(tags_file: str) -> List[str]:
    with open(tags_file, 'r', encoding='utf-8') as f:
        tags = json.load(f)
    return tags['tags']


def load_interests(interests_file: str) -> Dict:
    """加载用户感兴趣的领域配置"""
    try:
        with open(interests_file, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        return None


def match_interests(paper: Dict, interests_config: Dict) -> Dict:
    """
    检查论文是否匹配用户感兴趣的领域
    返回匹配信息：匹配的领域列表和相关性分数
    """
    if not interests_config:
        return {"matched_interests": [], "relevance_score": 0}
    
    interests = interests_config.get("interests", [])
    filter_mode = interests_config.get("filter_mode", "any")  # "any" 或 "all"
    
    title = paper.get("title", "").lower()
    summary = paper.get("summary", "").lower()
    text = f"{title} {summary}"
    
    matched = []
    total_score = 0
    
    for interest in interests:
        if not interest.get("enabled", True):
            continue
        
        name = interest.get("name", "")
        keywords = interest.get("keywords", [])
        
        # 检查是否匹配任一关键词
        match_count = 0
        matched_keywords = []
        for kw in keywords:
            if kw.lower() in text:
                match_count += 1
                matched_keywords.append(kw)
        
        if match_count > 0:
            matched.append({
                "name": name,
                "matched_keywords": matched_keywords,
                "score": match_count
            })
            total_score += match_count
    
    return {
        "matched_interests": matched,
        "relevance_score": total_score
    }


def filter_by_interests(papers: List[Dict], interests_file: str = "interests.json") -> List[Dict]:
    """根据用户兴趣筛选论文"""
    interests_config = load_interests(interests_file)
    
    if not interests_config:
        print("[INFO] 未找到 interests.json，跳过兴趣筛选")
        return papers
    
    min_score = interests_config.get("min_relevance_score", 1)
    
    filtered = []
    for paper in papers:
        match_info = match_interests(paper, interests_config)
        paper["matched_interests"] = match_info["matched_interests"]
        paper["relevance_score"] = match_info["relevance_score"]
        
        if match_info["relevance_score"] >= min_score:
            filtered.append(paper)
    
    # 按相关性分数排序
    filtered.sort(key=lambda x: x.get("relevance_score", 0), reverse=True)
    
    print(f"[INFO] 兴趣筛选: {len(papers)} → {len(filtered)} 篇论文")
    
    # 显示匹配统计
    interest_counts = {}
    for p in filtered:
        for m in p.get("matched_interests", []):
            name = m["name"]
            interest_counts[name] = interest_counts.get(name, 0) + 1
    
    if interest_counts:
        print("[INFO] 各领域匹配数量:")
        for name, count in sorted(interest_counts.items(), key=lambda x: -x[1]):
            print(f"       {name}: {count} 篇")
    
    return filtered

def get_UTC_range() -> Tuple[str, str, str]:
    fmt = "%Y%m%d%H%M"
    
    now_utc = datetime.now(timezone.utc)
    now_et = now_utc.astimezone(US_EASTERN)
    today_et = now_et.date()
    t2000_et = datetime(today_et.year, today_et.month, today_et.day, 20, 0, 0, tzinfo=US_EASTERN)
    
    if now_et < t2000_et:
        end_et = t2000_et - timedelta(days=1, minutes=1)
    else:
        end_et = t2000_et
    if end_et.weekday() in (4, 5):  # Friday or Saturday
        end_et -= timedelta(days=end_et.weekday() - 3, minutes=1)  # Move to Thursday
    
    if end_et.weekday() == 6:
        start_et = end_et - timedelta(days=3, minutes=-1)
    else:
        start_et = end_et - timedelta(days=1, minutes=-1)
    
    return (start_et.astimezone(timezone.utc).strftime(fmt),
            end_et.astimezone(timezone.utc).strftime(fmt),
            end_et.strftime("%Y-%m-%d"))


def extract_code_links(text: str) -> List[Dict[str, str]]:
    """从文本中提取代码仓库链接（GitHub, GitLab, Hugging Face 等）"""
    patterns = [
        # GitHub
        (r'https?://github\.com/[\w\-\.]+/[\w\-\.]+(?:/[\w\-\.]*)?', 'github'),
        # GitLab
        (r'https?://gitlab\.com/[\w\-\.]+/[\w\-\.]+(?:/[\w\-\.]*)?', 'gitlab'),
        # Hugging Face
        (r'https?://huggingface\.co/[\w\-\.]+(?:/[\w\-\.]+)?', 'huggingface'),
        # 项目主页（常见模式）
        (r'https?://[\w\-\.]+\.github\.io/[\w\-\.]+/?', 'project_page'),
    ]
    
    links = []
    seen = set()
    for pattern, link_type in patterns:
        matches = re.findall(pattern, text, re.IGNORECASE)
        for url in matches:
            # 清理 URL（移除末尾的标点）
            url = re.sub(r'[.,;:!?)}\]]+$', '', url)
            if url not in seen:
                seen.add(url)
                links.append({"url": url, "type": link_type})
    return links


def fetch_arxiv_thumbnail(arxiv_id: str, timeout: int = 10) -> Optional[str]:
    """
    从 arXiv 页面抓取论文预览缩略图
    返回图片 URL 或 None
    """
    base_id = arxiv_id.split('v')[0]
    abs_url = f"https://arxiv.org/abs/{base_id}"
    
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (compatible; ArxivDailyBot/1.0)'
        }
        resp = requests.get(abs_url, headers=headers, timeout=timeout)
        if resp.status_code != 200:
            return None
        
        soup = BeautifulSoup(resp.text, 'html.parser')
        
        # 方式1: 查找 og:image meta 标签
        og_image = soup.find('meta', property='og:image')
        if og_image and og_image.get('content'):
            return og_image['content']
        
        # 方式2: 查找论文缩略图 (通常在 arXiv 页面的特定位置)
        # arXiv 使用 https://arxiv.org/html/{id}/extracted/figure1.png 格式
        # 或者 https://static.arxiv.org/static/browse/0.3.4/images/...
        
        # 查找页面中的第一张相关图片
        for img in soup.find_all('img'):
            src = img.get('src', '')
            # 排除图标和装饰图片
            if any(x in src.lower() for x in ['icon', 'logo', 'button', 'arrow', 'social']):
                continue
            # 找到有意义的图片
            if 'arxiv' in src or src.startswith('/'):
                if src.startswith('/'):
                    src = f"https://arxiv.org{src}"
                return src
        
        return None
    except Exception:
        return None


def fetch_thumbnails_batch(papers: List[Dict], max_workers: int = 10) -> List[Dict]:
    """批量抓取论文缩略图"""
    print(f"[INFO] 正在抓取 {len(papers)} 篇论文的预览图...")
    
    def fetch_one(paper: Dict) -> Tuple[str, Optional[str]]:
        arxiv_id = paper.get('arxiv_id', '')
        thumb = fetch_arxiv_thumbnail(arxiv_id)
        return arxiv_id, thumb
    
    thumbnails = {}
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = {executor.submit(fetch_one, p): p for p in papers}
        for future in tqdm(as_completed(futures), total=len(futures), desc="抓取缩略图"):
            arxiv_id, thumb = future.result()
            if thumb:
                thumbnails[arxiv_id] = thumb
    
    # 更新论文数据
    for paper in papers:
        arxiv_id = paper.get('arxiv_id', '')
        if arxiv_id in thumbnails:
            paper['thumbnail'] = thumbnails[arxiv_id]
    
    print(f"[INFO] 成功获取 {len(thumbnails)}/{len(papers)} 篇论文的预览图")
    return papers


def _result_to_minimal(r: arxiv.Result) -> Dict:
    arxiv_id = r.get_short_id() if hasattr(r, "get_short_id") else r.entry_id.split("/abs/")[-1]
    authors = [a.name for a in r.authors] if r.authors else []
    
    # 获取分类信息
    categories = list(r.categories) if r.categories else []
    primary_category = r.primary_category if hasattr(r, "primary_category") and r.primary_category else (categories[0] if categories else "")
    
    # 获取更多元数据
    summary = (r.summary or "").strip()
    
    # 提取代码链接
    code_links = extract_code_links(summary)
    
    # 发布和更新日期
    published = r.published.strftime("%Y-%m-%d") if r.published else ""
    updated = r.updated.strftime("%Y-%m-%d") if r.updated else ""
    
    # 评论信息（通常包含页数、会议等）
    comment = (r.comment or "").strip() if hasattr(r, 'comment') and r.comment else ""
    
    # DOI 和期刊引用
    doi = r.doi if hasattr(r, 'doi') and r.doi else ""
    journal_ref = (r.journal_ref or "").strip() if hasattr(r, 'journal_ref') and r.journal_ref else ""
    
    # PDF URL
    pdf_url = r.pdf_url if hasattr(r, 'pdf_url') else f"https://arxiv.org/pdf/{arxiv_id.split('v')[0]}.pdf"
    
    return {
        "title": (r.title or "").strip().replace("\n", " "),
        "authors": authors,
        "arxiv_id": arxiv_id,
        "summary": summary,
        "categories": categories,
        "primary_category": primary_category,
        "published": published,
        "updated": updated,
        "comment": comment,
        "doi": doi,
        "journal_ref": journal_ref,
        "pdf_url": pdf_url,
        "code_links": code_links,
    }


def query_arxiv(tags: List[str], time_range: Tuple[str, str], max_results: int = 500, fetch_thumbnails: bool = False) -> Dict:
    start, end = time_range
    tag_clause = " OR ".join(f"cat:{t}" for t in tags)
    query = f"({tag_clause}) AND submittedDate:[{start} TO {end}]"

    client = arxiv.Client(page_size=200, delay_seconds=1.0, num_retries=3)

    search = arxiv.Search(
        query=query,
        max_results=max_results,
        sort_by=arxiv.SortCriterion.SubmittedDate,
        sort_order=arxiv.SortOrder.Descending,
    )

    seen = set()
    papers = []
    print(f"[INFO] 正在从 arXiv 抓取论文...")
    for r in tqdm(client.results(search), desc="抓取论文", unit="paper"):
        item = _result_to_minimal(r)
        if item["arxiv_id"] in seen:
            continue
        seen.add(item["arxiv_id"])
        papers.append(item)
    
    # 可选：批量抓取缩略图
    if fetch_thumbnails and papers:
        papers = fetch_thumbnails_batch(papers)
    
    return {"count": len(papers), "papers": papers}


def get_today_arxiv(tags: List[str], max_results: int = 500, fetch_thumbnails: bool = False) -> Tuple[Dict, str]:
    start, end, label_date = get_UTC_range()
    return query_arxiv(tags, (start, end), max_results=max_results, fetch_thumbnails=fetch_thumbnails), label_date


if __name__ == "__main__":
    tags = load_tags('../tags.json')
    result, label_date = get_today_arxiv(tags, fetch_thumbnails=True)
    print(f'Tags: {tags}')
    print(f"Date: {label_date}, Found {result['count']} papers")
    
    # 显示一些示例
    if result['papers']:
        p = result['papers'][0]
        print(f"\n示例论文:")
        print(f"  标题: {p['title'][:60]}...")
        print(f"  发布: {p['published']}")
        print(f"  代码: {p['code_links']}")
        print(f"  缩略图: {p.get('thumbnail', 'N/A')}")
