---
layout: default
title: Debiasing Online Preference Learning via Preference Feature Preservation
---

# Debiasing Online Preference Learning via Preference Feature Preservation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.11098" class="toolbar-btn" target="_blank">📄 arXiv: 2506.11098v1</a>
  <a href="https://arxiv.org/pdf/2506.11098.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.11098v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.11098v1', 'Debiasing Online Preference Learning via Preference Feature Preservation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Dongyoung Kim, Jinsung Yoon, Jinwoo Shin, Jaehyung Kim

**分类**: cs.LG, cs.AI

**发布日期**: 2025-06-06

**备注**: 20 page, 20 figures

---

## 💡 一句话要点

**提出偏好特征保留框架以解决在线偏好学习中的偏见问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `偏好学习` `在线学习` `特征提取` `模型公平性` `人机交互`

## 📋 核心要点

1. 现有的偏好学习方法在简化人类偏好时，可能导致模型响应偏向于某些特征，造成偏见。
2. 本文提出的PFP框架通过保留人类偏好特征的分布，增强了在线偏好学习过程中的信号利用。
3. 实验结果显示，PFP在标准基准测试中显著提升了模型的性能，成功减轻了偏见问题。

## 📝 摘要（中文）

近年来，针对大型语言模型（LLMs）的偏好学习框架通过二元成对比较和标量奖励简化了人类偏好。这种简化可能导致LLMs的响应偏向于主要偏好的特征，并在在线偏好学习的迭代过程中加剧。为了解决这些挑战，本文提出了一种新颖的框架，称为PFP（偏好特征保留）。PFP的核心思想是保持人类偏好特征的分布，并在在线偏好学习过程中利用这些丰富的信号。具体而言，PFP首先从离线成对人类偏好数据中提取偏好特征，并训练特征分类器。然后，利用训练好的分类器和分布保留优化，PFP在在线学习过程中为新的输入指令映射适当的偏好特征。最后，PFP通过将偏好特征纳入系统提示，使用现有的偏好学习方法训练LLM，使其能够明确处理各种人类偏好。实验表明，PFP成功减轻了在线学习中偏好特征的偏见，并在标准基准测试中相较于以往的偏好学习方法取得了更优的性能。

## 🔬 方法详解

**问题定义**：本文旨在解决现有偏好学习方法中由于简化人类偏好而导致的偏见问题。现有方法在在线学习过程中容易使模型偏向于某些特征，影响其多样性和准确性。

**核心思路**：PFP框架的核心思路是通过提取和保留人类偏好特征的分布，确保模型在学习过程中能够充分利用这些特征信号，从而减轻偏见。

**技术框架**：PFP的整体架构包括三个主要模块：首先，从离线成对人类偏好数据中提取偏好特征并训练特征分类器；其次，利用训练好的分类器和分布保留优化为新输入指令映射适当的偏好特征；最后，将这些偏好特征融入系统提示中，训练LLM以处理多样化的人类偏好。

**关键创新**：PFP的主要创新在于其分布保留优化方法，使得模型能够在在线学习过程中保持对偏好特征的敏感性，避免了传统方法中偏见的加剧。

**关键设计**：在设计中，PFP使用了特征分类器来提取偏好特征，并采用了特定的损失函数来优化分布保留，确保模型在训练过程中能够有效地处理各种人类偏好。具体的网络结构和参数设置在实验部分进行了详细描述。

## 📊 实验亮点

实验结果表明，PFP在标准基准测试中相较于传统偏好学习方法提升了模型性能，具体表现为在多个评估指标上均取得了显著改善，减轻了偏见的影响，验证了其有效性和优越性。

## 🎯 应用场景

该研究的潜在应用领域包括个性化推荐系统、用户偏好分析和人机交互等。通过减轻偏见，PFP框架能够提升模型的公平性和准确性，进而在商业和社会应用中产生积极影响。未来，PFP的理念和方法可以扩展到其他机器学习领域，促进更广泛的应用。

## 📄 摘要（原文）

> Recent preference learning frameworks for large language models (LLMs) simplify human preferences with binary pairwise comparisons and scalar rewards. This simplification could make LLMs' responses biased to mostly preferred features, and would be exacerbated during the iterations of online preference learning steps. To address these challenges, we propose a novel framework coined PFP (Preference Feature Preservation). The key idea of PFP is maintaining the distribution of human preference features and utilizing such rich signals throughout the online preference learning process. Specifically, PFP first extract preference features from offline pairwise human preference data and trains a feature classifier. Then, using trained classifier and the distribution preserving optimization, PFP maps appropriate preference features for a new input instruction during online learning. Lastly, PFP trains LLM using the existing preference learning method, by incorporating the preference feature into system prompts and enabling LLM to explicitly handle various human preferences. Our experiments demonstrate that PFP successfully mitigates the bias in preference features during online learning, and hence achieves superior performance compared to previous preference learning methods on standard benchmarks to evaluate LLM alignment.

