---
layout: default
title: Multi-source Multimodal Progressive Domain Adaption for Audio-Visual Deception Detection
---

# Multi-source Multimodal Progressive Domain Adaption for Audio-Visual Deception Detection

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.12842" class="toolbar-btn" target="_blank">📄 arXiv: 2508.12842v1</a>
  <a href="https://arxiv.org/pdf/2508.12842.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.12842v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.12842v1', 'Multi-source Multimodal Progressive Domain Adaption for Audio-Visual Deception Detection')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Ronghao Lin, Sijie Mai, Ying Zeng, Qiaolin He, Aolin Xiong, Haifeng Hu

**分类**: cs.CV, cs.MM

**发布日期**: 2025-08-18

**备注**: Accepted at ACM MM 2025 SVC Workshop

**🔗 代码/项目**: [GITHUB](https://github.com/RH-Lin/MMPDA)

---

## 💡 一句话要点

**提出多源多模态渐进领域适应框架以解决音视频欺骗检测问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多模态学习` `领域适应` `欺骗检测` `音视频分析` `深度学习`

## 📋 核心要点

1. 现有方法在处理源域与目标域之间的领域转移时存在显著挑战，导致音视频欺骗检测效果不佳。
2. 论文提出的多源多模态渐进领域适应框架通过逐步对齐源域与目标域的特征和决策层，解决了领域转移问题。
3. 实验结果显示，所提方法在准确率和F1分数上均优于其他参赛团队，验证了其有效性和优越性。

## 📝 摘要（中文）

本文提出了在第一届细微视觉计算研讨会的多模态欺骗检测挑战赛中获胜的方法。针对源域与目标域之间的领域转移问题，我们提出了一种多源多模态渐进领域适应（MMPDA）框架，旨在将来自不同源域的音视频知识迁移到目标域。通过逐步在特征和决策层面对齐源域与目标域，我们的方法有效地弥合了不同多模态数据集之间的领域差异。大量实验表明，我们的方法在比赛第二阶段中取得了60.43%的准确率和56.99%的F1分数，超越了第一名团队5.59%的F1分数和第三名团队6.75%的准确率。我们的代码可在https://github.com/RH-Lin/MMPDA获取。

## 🔬 方法详解

**问题定义**：本研究旨在解决音视频欺骗检测中的领域转移问题，现有方法在不同源域与目标域之间的知识迁移效果不佳，导致检测性能下降。

**核心思路**：我们提出的多源多模态渐进领域适应框架通过逐步对齐源域与目标域的特征和决策层，旨在有效迁移音视频知识，减少领域间的差异。

**技术框架**：该框架包括多个模块，首先通过特征提取模块获取源域和目标域的音视频特征，然后在对齐模块中逐步对齐这些特征，最后通过决策模块进行分类。

**关键创新**：本研究的创新点在于提出了渐进式对齐策略，能够在特征和决策层面上有效减少领域转移的影响，这与传统的单一对齐方法有本质区别。

**关键设计**：在模型设计中，我们采用了多源输入和逐步对齐的损失函数，确保模型在训练过程中能够有效学习到不同源域的特征，同时优化了网络结构以提高性能。

## 📊 实验亮点

实验结果显示，所提方法在比赛第二阶段中取得了60.43%的准确率和56.99%的F1分数，分别超越第一名团队5.59%的F1分数和第三名团队6.75%的准确率，验证了其在多模态欺骗检测中的有效性。

## 🎯 应用场景

该研究在音视频欺骗检测领域具有广泛的应用潜力，能够帮助提升安全监控、在线会议和社交媒体平台中的欺诈检测能力。未来，该方法还可扩展到其他多模态学习任务中，推动相关领域的发展。

## 📄 摘要（原文）

> This paper presents the winning approach for the 1st MultiModal Deception Detection (MMDD) Challenge at the 1st Workshop on Subtle Visual Computing (SVC). Aiming at the domain shift issue across source and target domains, we propose a Multi-source Multimodal Progressive Domain Adaptation (MMPDA) framework that transfers the audio-visual knowledge from diverse source domains to the target domain. By gradually aligning source and the target domain at both feature and decision levels, our method bridges domain shifts across diverse multimodal datasets. Extensive experiments demonstrate the effectiveness of our approach securing Top-2 place. Our approach reaches 60.43% on accuracy and 56.99\% on F1-score on competition stage 2, surpassing the 1st place team by 5.59% on F1-score and the 3rd place teams by 6.75% on accuracy. Our code is available at https://github.com/RH-Lin/MMPDA.

