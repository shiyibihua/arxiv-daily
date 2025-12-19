---
layout: default
title: PhysBrain: Human Egocentric Data as a Bridge from Vision Language Models to Physical Intelligence
---

# PhysBrain: Human Egocentric Data as a Bridge from Vision Language Models to Physical Intelligence

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.16793" class="toolbar-btn" target="_blank">📄 arXiv: 2512.16793v1</a>
  <a href="https://arxiv.org/pdf/2512.16793.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.16793v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.16793v1', 'PhysBrain: Human Egocentric Data as a Bridge from Vision Language Models to Physical Intelligence')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Xiaopeng Lin, Shijie Lian, Bin Yu, Ruoqi Yang, Changti Wu, Yuzhuo Miao, Yurun Jin, Yukun Shi, Cong Huang, Bojun Cheng, Kai Chen

**分类**: cs.RO

**发布日期**: 2025-12-18

**备注**: 17 pages, 4 figures

---

## 💡 一句话要点

**提出Egocentric2Embodiment以解决机器人物理智能问题**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱六：视频提取与匹配 (Video Extraction)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `物理智能` `自我中心感知` `视觉问答` `数据集构建` `机器人控制` `长时间规划` `模型训练`

## 📋 核心要点

1. 现有的视觉语言模型主要依赖第三人称数据，导致人形机器人在自我中心感知下的推理能力不足。
2. 论文提出了Egocentric2Embodiment翻译管道，将第一人称视频转化为结构化的VQA监督，解决了数据收集的高成本和多样性不足问题。
3. PhysBrain在E2E-3M数据集上训练后，展现出更强的自我中心理解能力，成功率达到53.9%，有效实现了人类自我中心监督向机器人控制的迁移。

## 📝 摘要（中文）

机器人通用化依赖于物理智能，即在自我中心感知和行动下推理状态变化、接触丰富的交互和长时间规划的能力。然而，大多数视觉语言模型（VLMs）主要在第三人称数据上训练，导致人形机器人面临视角不匹配的问题。本文提出了Egocentric2Embodiment翻译管道，将第一人称视频转化为多层次、基于模式的视觉问答（VQA）监督，构建了大规模的Egocentric2Embodiment数据集（E2E-3M）。通过在该数据集上训练，获得了一个自我中心感知的具身智能系统PhysBrain，显著提升了其自我中心理解能力，尤其在EgoThink上的规划表现。该系统为机器人控制提供了更高效的样本利用率和成功率。

## 🔬 方法详解

**问题定义**：本文旨在解决机器人在自我中心感知下的物理智能问题，现有方法主要依赖第三人称数据，导致视角不匹配和推理能力不足。

**核心思路**：提出Egocentric2Embodiment翻译管道，将第一人称视频转化为多层次的VQA监督，以实现更可靠的具身训练监督。

**技术框架**：该方法包括数据收集、视频处理、监督生成和模型训练四个主要阶段，利用丰富的自我中心视频数据构建E2E-3M数据集。

**关键创新**：最重要的创新在于将原始自我中心视频转化为结构化的监督信息，确保了证据的基础和时间的一致性，与传统方法相比，显著提升了数据的有效性和可用性。

**关键设计**：在设计中，采用了多层次的模式驱动方法，结合特定的损失函数和网络结构，确保生成的监督信息具有高质量和一致性。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16793v1/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16793v1/fig/data_pipeline.jpg" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16793v1/fig/data_sum.jpg" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

在实验中，PhysBrain在EgoThink任务上的表现显著提升，成功率达到53.9%。与基线模型相比，展现出更高的样本利用效率和更强的自我中心理解能力，验证了人类自我中心监督向机器人控制的有效迁移。

## 🎯 应用场景

该研究的潜在应用领域包括机器人控制、智能家居和人机交互等。通过提升机器人在自我中心感知下的理解能力，PhysBrain能够更好地执行复杂的任务，具有广泛的实际价值和未来影响。

## 📄 摘要（原文）

> Robotic generalization relies on physical intelligence: the ability to reason about state changes, contact-rich interactions, and long-horizon planning under egocentric perception and action. However, most VLMs are trained primarily on third-person data, creating a fundamental viewpoint mismatch for humanoid robots. Scaling robot egocentric data collection remains impractical due to high cost and limited diversity, whereas large-scale human egocentric videos offer a scalable alternative that naturally capture rich interaction context and causal structure. The key challenge is to convert raw egocentric videos into structured and reliable embodiment training supervision. Accordingly, we propose an Egocentric2Embodiment translation pipeline that transforms first-person videos into multi-level, schema-driven VQA supervision with enforced evidence grounding and temporal consistency, enabling the construction of the Egocentric2Embodiment dataset (E2E-3M) at scale. An egocentric-aware embodied brain, termed PhysBrain, is obtained by training on the E2E-3M dataset. PhysBrain exhibits substantially improved egocentric understanding, particularly for planning on EgoThink. It provides an egocentric-aware initialization that enables more sample-efficient VLA fine-tuning and higher SimplerEnv success rates (53.9\%), demonstrating effective transfer from human egocentric supervision to downstream robot control.

