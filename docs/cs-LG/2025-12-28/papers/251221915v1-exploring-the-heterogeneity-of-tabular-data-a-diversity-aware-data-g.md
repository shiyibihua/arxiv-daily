---
layout: default
title: "Exploring the Heterogeneity of Tabular Data: A Diversity-aware Data Generator via LLMs"
---

# Exploring the Heterogeneity of Tabular Data: A Diversity-aware Data Generator via LLMs

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.21915" class="toolbar-btn" target="_blank">📄 arXiv: 2512.21915v1</a>
  <a href="https://arxiv.org/pdf/2512.21915.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.21915v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.21915v1', 'Exploring the Heterogeneity of Tabular Data: A Diversity-aware Data Generator via LLMs')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yafeng Tang, Xiaoou Ding, Jianzhuo Du, Zishuo Yan, Zhuang Ma, Zheng Liang, Zekai Qian, Hongzhi Wang

**分类**: cs.LG, cs.DB

**发布日期**: 2025-12-26

**备注**: This manuscript has been submitted to IEEE Transactions on Knowledge and Data Engineering (TKDE) for peer review

**🔗 代码/项目**: [GITHUB](https://github.com/windblow32/DATE)

---

## 💡 一句话要点

**提出DATE框架，利用LLM生成多样性表格数据，提升小样本学习性能。**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `表格数据生成` `异构数据` `大型语言模型` `多臂老虎机` `数据增强`

## 📋 核心要点

1. 现实表格数据异构性强，现有生成模型难以兼顾多样性与质量，导致生成数据效果不佳。
2. DATE框架通过数据划分、LLM生成和多臂老虎机采样，实现高质量、多样性的表格数据生成。
3. 实验表明，DATE在表格分类和回归任务上显著优于现有方法，错误率平均降低23.75%。

## 📝 摘要（中文）

表格数据生成对于实现稳健的机器学习应用至关重要，这些应用需要大规模、高质量的数据。现有方法利用生成模型学习原始数据分布。然而，现实世界的数据本质上是异构的，具有不同的分布，这使得获得一个通用的良好模型来生成多样化数据具有挑战性。为了解决这个限制，我们引入了多样性感知表格数据生成器(DATE)，该框架(i)通过有效地将原始异构数据划分为多个不同的子集，为上下文学习准备高质量和分布不同的示例；(ii)利用大型语言模型(LLM)，以决策树推理作为反馈，探索划分分布的多样性，为每个子集生成高质量的标记数据。然而，大量生成的数据固有地涉及多样性和质量之间的权衡。为了整合这个问题，现有的解决方案贪婪地选择验证效果最佳的数据。然而，我们证明了在异构设置中的选择不具备贪婪选择的性质，并设计了一种基于多臂老虎机的抽样算法，该算法平衡了生成数据的多样性和质量。在表格分类和回归基准上的大量实验表明，DATE始终优于最先进的基于GAN和基于LLM的方法。平均而言，DATE仅用100个生成数据就实现了23.75%的错误率降低。经验表明，DATE生成的数据可以提高直接偏好优化(DPO)的准确性，并增强LLM在目标数据上的推理能力。代码可在https://github.com/windblow32/DATE获得。

## 🔬 方法详解

**问题定义**：现有表格数据生成方法难以处理真实世界数据的异构性，即数据分布的多样性。简单地使用单一模型学习所有数据会导致模型无法捕捉到各个子分布的特征，从而生成质量不高且缺乏多样性的数据。现有方法在平衡生成数据的多样性和质量时，通常采用贪婪选择策略，但在异构数据场景下，这种策略并非最优。

**核心思路**：DATE框架的核心思路是将异构数据划分为多个同质性更高的子集，然后利用大型语言模型（LLM）为每个子集生成数据。为了平衡生成数据的多样性和质量，DATE采用了一种基于多臂老虎机的采样算法，自适应地选择不同子集生成的数据。

**技术框架**：DATE框架包含三个主要阶段：1) **数据划分**：将原始异构数据划分为多个分布不同的子集，为后续的LLM生成提供更具针对性的数据基础。2) **LLM数据生成**：利用LLM，以决策树推理作为反馈，探索划分分布的多样性，为每个子集生成高质量的标记数据。3) **多臂老虎机采样**：设计了一种基于多臂老虎机的抽样算法，平衡生成数据的多样性和质量。

**关键创新**：DATE的关键创新在于：1) 提出了一个多样性感知的表格数据生成框架，能够有效处理异构数据。2) 利用LLM结合决策树推理生成高质量的表格数据。3) 设计了一种基于多臂老虎机的采样算法，解决了异构数据场景下贪婪选择策略的局限性，实现了多样性和质量的平衡。

**关键设计**：数据划分阶段，采用了合适的划分算法（具体算法未知）将数据划分为多个子集。LLM数据生成阶段，使用了决策树推理作为反馈，指导LLM生成更符合子集分布的数据。多臂老虎机采样阶段，设计了合适的奖励函数，用于评估每个子集生成数据的质量和多样性，并根据奖励值调整采样概率。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.21915v1/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.21915v1/x2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.21915v1/x3.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

实验结果表明，DATE在表格分类和回归任务上显著优于现有的基于GAN和基于LLM的方法。在仅使用100个生成数据的情况下，DATE的错误率平均降低了23.75%。此外，DATE生成的数据还可以提高直接偏好优化(DPO)的准确性，并增强LLM在目标数据上的推理能力。

## 🎯 应用场景

DATE框架生成的表格数据可用于增强机器学习模型的训练数据，尤其是在数据量不足或数据分布不平衡的情况下。该方法可以应用于金融风控、医疗诊断、市场营销等领域，提升模型在这些领域的泛化能力和鲁棒性。此外，DATE还可以用于生成合成数据，保护用户隐私。

## 📄 摘要（原文）

> Tabular data generation has become increasingly essential for enabling robust machine learning applications, which require large-scale, high-quality data. Existing solutions leverage generative models to learn original data distributions. However, real-world data are naturally heterogeneous with diverse distributions, making it challenging to obtain a universally good model for diverse data generation. To address this limitation, we introduce Diversity-Aware Tabular data gEnerator (DATE), a framework that (i) prepares high-quality and distributionally distinct examples for in-context learning by effectively partitioning the original heterogeneous data into multiple diverse subsets; (ii) harnesses Large Language Models (LLMs) to explore the diversity of the partitioned distribution with decision tree reasoning as feedback, generating high-quality labeled data for each subset. However, the massive generated data inherently involves a trade-off between diversity and quality. To integrate this issue, existing solutions greedily select the validation-best data. However, we prove that the selection in heterogeneous settings does not possess the greedy-choice property, and design a Multi-Arm Bandit-based sampling algorithm that balances the diversity and quality of generated data. Extensive experiments on tabular classification and regression benchmarks demonstrate that DATE consistently outperforms state-of-the-art GAN-based and LLM-based methods. On average, DATE achieves a 23.75% reduction in error rate with just 100 generated data. Empirically, we demonstrate that data generated by DATE can improve the accuracy of Direct Preference Optimization (DPO) and enhance the reasoning capability of LLMs on the target data. Code is available at https://github.com/windblow32/DATE.

