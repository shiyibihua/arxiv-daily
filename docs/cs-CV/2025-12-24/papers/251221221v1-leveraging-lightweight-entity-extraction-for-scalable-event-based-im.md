---
layout: default
title: Leveraging Lightweight Entity Extraction for Scalable Event-Based Image Retrieval
---

# Leveraging Lightweight Entity Extraction for Scalable Event-Based Image Retrieval

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.21221" class="toolbar-btn" target="_blank">📄 arXiv: 2512.21221v1</a>
  <a href="https://arxiv.org/pdf/2512.21221.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.21221v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.21221v1', 'Leveraging Lightweight Entity Extraction for Scalable Event-Based Image Retrieval')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Dao Sy Duy Minh, Huynh Trung Kiet, Nguyen Lam Phu Quy, Phu-Hoa Pham, Tran Chi Nguyen

**分类**: cs.CV, cs.AI

**发布日期**: 2025-12-24

**备注**: System description paper for EVENTA Grand Challenge Track 2 at ACM Multimedia 2025 (MM '25). Ranked 4th place. 6 pages, 1 figure, 2 tables

**🔗 代码/项目**: [GITHUB](https://github.com/PhamPhuHoa-23/Event-Based-Image-Retrieval)

---

## 💡 一句话要点

**提出基于事件中心实体提取的两阶段图像检索方法，提升复杂场景下的检索精度。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `图像检索` `事件提取` `多模态学习` `BEiT-3` `BM25` `视觉语言模型` `自然语言处理`

## 📋 核心要点

1. 真实场景图像-文本检索面临模糊查询、语言变异性和可扩展性挑战。
2. 利用事件中心实体提取，结合BM25过滤和BEiT-3重排序，提升检索效率和精度。
3. 在OpenEvents v1数据集上，该方法mAP达到0.559，显著优于现有方法。

## 📝 摘要（中文）

本文提出了一种轻量级的两阶段图像检索流程，旨在利用事件中心实体提取来整合真实场景字幕中的时间和上下文信息。第一阶段，该流程使用基于BM25的显著实体进行高效的候选过滤。第二阶段，应用BEiT-3模型来捕捉深层的多模态语义并对结果进行重排序。在OpenEvents v1基准测试中，该方法实现了0.559的平均精度均值（mAP），显著优于先前的基线方法。实验结果表明，在复杂的真实场景中，将事件引导的过滤与长文本视觉-语言建模相结合，能够实现准确而高效的图像检索。

## 🔬 方法详解

**问题定义**：论文旨在解决真实场景下图像-文本检索的难题，现有方法难以有效处理复杂、模糊的自然语言描述，并且缺乏对事件上下文信息的充分利用，导致检索精度不高，尤其是在大规模数据集上。

**核心思路**：论文的核心思路是利用事件相关的实体信息作为桥梁，将图像和文本联系起来。通过提取文本描述中的关键实体，并将其作为检索的线索，可以有效地过滤掉不相关的图像，从而提高检索效率和精度。同时，利用预训练的BEiT-3模型来学习图像和文本的深层语义表示，进一步提升检索性能。

**技术框架**：该方法采用两阶段检索框架。第一阶段是候选过滤阶段，使用BM25算法基于提取的实体信息对图像进行初步筛选，快速缩小检索范围。第二阶段是重排序阶段，使用BEiT-3模型对候选图像进行多模态语义分析，并根据图像和文本的相似度对结果进行重排序，最终返回最相关的图像。

**关键创新**：该方法最重要的创新点在于将事件中心实体提取与视觉-语言模型相结合，充分利用了事件的上下文信息，从而提高了检索的准确性和效率。此外，两阶段检索框架的设计也使得该方法能够在大规模数据集上进行高效检索。

**关键设计**：在第一阶段，使用轻量级的实体提取方法，保证了检索的效率。BM25算法被用于快速计算文本和图像描述之间的相似度。在第二阶段，BEiT-3模型被用于学习图像和文本的深层语义表示，并使用余弦相似度来衡量图像和文本之间的相似度。具体的参数设置和网络结构细节在论文中未详细说明，属于未知信息。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.21221v1/Images_pipeline.png" alt="fig_0" loading="lazy">
</figure>
</div>

## 📊 实验亮点

该方法在OpenEvents v1基准测试中取得了显著的成果，平均精度均值（mAP）达到了0.559，大幅超越了现有的基线方法。这表明该方法在处理复杂、真实的图像-文本检索任务时具有很强的竞争力，验证了事件引导过滤与长文本视觉-语言建模结合的有效性。

## 🎯 应用场景

该研究成果可应用于搜索引擎、媒体内容管理、数字内容归档等领域。通过更准确地理解图像内容和用户查询意图，可以提升搜索结果的相关性，改善用户体验。未来，该方法有望应用于智能监控、自动驾驶等需要理解场景事件的领域。

## 📄 摘要（原文）

> Retrieving images from natural language descriptions is a core task at the intersection of computer vision and natural language processing, with wide-ranging applications in search engines, media archiving, and digital content management. However, real-world image-text retrieval remains challenging due to vague or context-dependent queries, linguistic variability, and the need for scalable solutions. In this work, we propose a lightweight two-stage retrieval pipeline that leverages event-centric entity extraction to incorporate temporal and contextual signals from real-world captions. The first stage performs efficient candidate filtering using BM25 based on salient entities, while the second stage applies BEiT-3 models to capture deep multimodal semantics and rerank the results. Evaluated on the OpenEvents v1 benchmark, our method achieves a mean average precision of 0.559, substantially outperforming prior baselines. These results highlight the effectiveness of combining event-guided filtering with long-text vision-language modeling for accurate and efficient retrieval in complex, real-world scenarios. Our code is available at https://github.com/PhamPhuHoa-23/Event-Based-Image-Retrieval

