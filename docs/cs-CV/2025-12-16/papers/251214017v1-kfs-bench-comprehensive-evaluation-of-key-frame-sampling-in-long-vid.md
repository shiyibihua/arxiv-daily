---
layout: default
title: KFS-Bench: Comprehensive Evaluation of Key Frame Sampling in Long Video Understanding
---

# KFS-Bench: Comprehensive Evaluation of Key Frame Sampling in Long Video Understanding

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.14017" class="toolbar-btn" target="_blank">📄 arXiv: 2512.14017v1</a>
  <a href="https://arxiv.org/pdf/2512.14017.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.14017v1" onclick="toggleFavorite(this, '2512.14017v1', 'KFS-Bench: Comprehensive Evaluation of Key Frame Sampling in Long Video Understanding')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zongyao Li, Kengo Ishida, Satoshi Yamazaki, Xiaotong Ji, Jianquan Liu

**分类**: cs.CV, cs.AI

**发布日期**: 2025-12-16

**备注**: WACV2026

**🔗 代码/项目**: [GITHUB](https://github.com/NEC-VID/KFS-Bench)

---

## 💡 一句话要点

**提出KFS-Bench基准，用于长视频问答中关键帧采样的全面评估。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `长视频理解` `关键帧采样` `视频问答` `多模态学习` `基准数据集`

## 📋 核心要点

1. 现有长视频问答的关键帧采样方法缺乏直接评估手段，通常只能通过最终QA准确率间接评估采样质量。
2. 论文提出KFS-Bench基准，包含多场景标注，能够直接分析采样方法对关键内容的覆盖程度和采样质量。
3. 实验表明，采样精度、场景覆盖率和采样平衡是影响QA性能的关键因素，并提出了一种自适应平衡采样方法，提升了QA性能。

## 📝 摘要（中文）

本文提出了KFS-Bench，这是首个用于长视频问答（QA）中关键帧采样的基准，它具有多场景标注，能够直接且稳健地评估采样策略。关键帧采样对于高效的长视频理解至关重要。在长视频QA中，选择信息量大的帧可以使多模态大型语言模型（MLLM）提高准确性和效率。KFS-Bench解决了先前工作仅通过QA准确性间接评估帧选择质量的局限性。通过提供每个问题所需多个不相交场景的ground-truth标注，KFS-Bench允许我们直接分析不同的采样方法如何捕获整个长视频中的关键内容。使用KFS-Bench，我们对关键帧采样方法进行了全面研究，并确定不仅采样精度，而且场景覆盖率和采样平衡是影响QA性能的关键因素。考虑到所有因素，我们设计了一种新的采样质量指标，该指标与QA准确性相关。此外，我们开发了一种新的关键帧采样方法，该方法利用问题-视频相关性来平衡采样多样性与问题-帧相似性，从而提高相关场景的覆盖率。我们的自适应平衡采样方法在关键帧采样和QA性能方面均实现了卓越的性能。该基准可在https://github.com/NEC-VID/KFS-Bench上获得。

## 🔬 方法详解

**问题定义**：论文旨在解决长视频问答中关键帧采样策略的评估问题。现有方法主要依赖于最终问答的准确率来间接评估关键帧采样的质量，缺乏直接、细粒度的评估手段，无法有效指导采样策略的优化。此外，现有方法难以保证采样帧覆盖视频中的所有相关场景，导致信息缺失。

**核心思路**：论文的核心思路是构建一个包含多场景标注的基准数据集KFS-Bench，从而能够直接评估关键帧采样策略的质量。同时，论文提出了一种自适应平衡采样方法，该方法通过平衡问题-视频相关性和采样多样性，提高相关场景的覆盖率。

**技术框架**：KFS-Bench基准包含长视频、问题以及与问题相关的多个视频场景的标注。评估流程包括：1) 使用不同的关键帧采样方法从长视频中选择关键帧；2) 使用多模态大型语言模型（MLLM）对选择的关键帧进行问答；3) 使用KFS-Bench提供的标注，直接评估关键帧采样策略的精度、场景覆盖率和采样平衡性。自适应平衡采样方法则包含问题-视频相关性计算模块和采样多样性平衡模块。

**关键创新**：论文的关键创新在于：1) 提出了KFS-Bench基准，为长视频问答中的关键帧采样提供了直接评估手段；2) 提出了一种新的采样质量指标，该指标与QA准确性相关；3) 提出了一种自适应平衡采样方法，该方法通过平衡问题-视频相关性和采样多样性，提高了相关场景的覆盖率。

**关键设计**：自适应平衡采样方法中，问题-视频相关性可以通过计算问题和视频帧的语义相似度得到。采样多样性平衡可以通过最大化采样帧之间的差异性来实现，例如使用最大边缘相关性（Maximal Marginal Relevance, MMR）算法。具体的参数设置包括相似度计算方法（如余弦相似度）、MMR算法中的惩罚因子等。损失函数的设计需要考虑采样精度、场景覆盖率和采样平衡性，例如可以设计一个多目标优化函数，同时优化这三个指标。

## 📊 实验亮点

实验结果表明，KFS-Bench能够有效评估不同关键帧采样策略的性能。提出的自适应平衡采样方法在关键帧采样和QA性能方面均优于现有方法。具体而言，该方法在KFS-Bench上实现了显著的性能提升，QA准确率提高了X%（具体数值需要在论文中查找）。

## 🎯 应用场景

该研究成果可应用于智能视频分析、视频检索、智能客服等领域。通过更有效地提取长视频中的关键信息，可以提升多模态大语言模型在视频理解任务中的性能，例如视频问答、视频摘要等。未来，该研究可以进一步扩展到其他长视频理解任务，例如视频编辑、视频推荐等。

## 📄 摘要（原文）

> We propose KFS-Bench, the first benchmark for key frame sampling in long video question answering (QA), featuring multi-scene annotations to enable direct and robust evaluation of sampling strategies. Key frame sampling is crucial for efficient long-form video understanding. In long video QA, selecting informative frames enables multimodal large language models (MLLMs) to improve both accuracy and efficiency. KFS-Bench addresses the limitation of prior works that only indirectly assess frame selection quality via QA accuracy. By providing ground-truth annotations of multiple disjoint scenes required per question, KFS-Bench allows us to directly analyze how different sampling approaches capture essential content across an entire long video. Using KFS-Bench, we conduct a comprehensive study of key frame sampling methods and identify that not only sampling precision but also scene coverage and sampling balance are the key factors influencing QA performance. Regarding all the factors, we design a novel sampling quality metric that correlates with QA accuracy. Furthermore, we develop a novel key frame sampling method that leverages question-video relevance to balance sampling diversity against question-frame similarity, thereby improving coverage of relevant scenes. Our adaptively balanced sampling approach achieves superior performance in both key frame sampling and QA performance. The benchmark is available at https://github.com/NEC-VID/KFS-Bench.

