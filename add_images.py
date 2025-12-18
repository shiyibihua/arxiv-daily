#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
为已有的 AI 分析结果补充图片

用法:
    python add_images.py data/2025-09/ai_summary.json           # 为指定文件补充图片
    python add_images.py data/2025-09                           # 为指定目录下的 ai_summary.json 补充图片
    python add_images.py data/2025-09 --max-images 5            # 每篇论文最多提取5张图片
    python add_images.py data/2025-09 --concurrency 10          # 使用10个并发
    python add_images.py data/2025-09 --skip-existing           # 跳过已有图片的论文
"""

import argparse
import json
import os
import sys

from utils.image_extractor import batch_extract_images


def main():
    parser = argparse.ArgumentParser(description="为已有的 AI 分析结果补充图片")
    parser.add_argument("path", type=str,
                       help="ai_summary.json 文件路径或包含该文件的目录")
    parser.add_argument("--max-images", type=int, default=3,
                       help="每篇论文最多提取图片数 (默认: 3)")
    parser.add_argument("--concurrency", type=int, default=5,
                       help="并发数 (默认: 5)")
    parser.add_argument("--skip-existing", action="store_true",
                       help="跳过已有图片的论文")
    
    args = parser.parse_args()
    
    # 确定文件路径
    if os.path.isdir(args.path):
        json_path = os.path.join(args.path, "ai_summary.json")
    else:
        json_path = args.path
    
    if not os.path.exists(json_path):
        print(f"❌ 文件不存在: {json_path}")
        sys.exit(1)
    
    # 加载数据
    print(f"📂 加载: {json_path}")
    with open(json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    papers = data.get("papers", [])
    if not papers:
        print("❌ 没有找到论文数据")
        sys.exit(1)
    
    print(f"[INFO] 共 {len(papers)} 篇论文")
    
    # 筛选需要处理的论文
    if args.skip_existing:
        papers_to_process = [p for p in papers if not p.get("figures")]
        print(f"[INFO] 跳过已有图片的论文，剩余 {len(papers_to_process)} 篇需要处理")
    else:
        papers_to_process = papers
    
    if not papers_to_process:
        print("✅ 所有论文都已有图片，无需处理")
        return
    
    # 提取图片
    print(f"\n🖼️ 正在提取论文图片...")
    print(f"[INFO] 并发数: {args.concurrency}, 每篇最多: {args.max_images} 张")
    
    image_results = batch_extract_images(
        papers=papers_to_process,
        max_images_per_paper=args.max_images,
        concurrency=args.concurrency
    )
    
    # 将图片信息合并到结果中
    # 创建 arxiv_id -> paper 的映射
    paper_map = {p.get("arxiv_id", ""): p for p in papers}
    
    updated_count = 0
    for arxiv_id, figures in image_results.items():
        if arxiv_id in paper_map:
            paper_map[arxiv_id]["figures"] = figures
            updated_count += 1
    
    img_count = sum(len(v) for v in image_results.values())
    print(f"[OK] 提取图片: {img_count} 张 (来自 {len(image_results)} 篇论文)")
    
    # 保存结果
    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
    print(f"[OK] 已保存: {json_path}")
    
    # 统计
    papers_with_figures = sum(1 for p in papers if p.get("figures"))
    print(f"\n✅ 完成！")
    print(f"   📄 总论文数: {len(papers)}")
    print(f"   🖼️ 有图片的论文: {papers_with_figures}")
    print(f"   📷 本次新增: {updated_count} 篇论文的图片")


if __name__ == '__main__':
    main()

