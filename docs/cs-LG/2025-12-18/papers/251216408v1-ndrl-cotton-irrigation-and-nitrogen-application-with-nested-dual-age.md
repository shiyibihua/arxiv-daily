---
layout: default
title: NDRL: Cotton Irrigation and Nitrogen Application with Nested Dual-Agent Reinforcement Learning
---

# NDRL: Cotton Irrigation and Nitrogen Application with Nested Dual-Agent Reinforcement Learning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.16408" class="toolbar-btn" target="_blank">📄 arXiv: 2512.16408v1</a>
  <a href="https://arxiv.org/pdf/2512.16408.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.16408v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.16408v1', 'NDRL: Cotton Irrigation and Nitrogen Application with Nested Dual-Agent Reinforcement Learning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Ruifeng Xu, Liang He

**分类**: cs.LG, cs.MA

**发布日期**: 2025-12-18

**备注**: Accepted by ICONIP 2025

---

## 💡 一句话要点

**提出嵌套双智能体强化学习NDRL，优化棉花灌溉施氮，提升产量和资源利用率。**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `强化学习` `农业灌溉` `氮肥施用` `双智能体` `精准农业`

## 📋 核心要点

1. 现有方法在作物生长期间难以优化水氮组合，导致产量提升有限，且难以量化轻微胁迫信号。
2. NDRL通过嵌套双智能体结构，父智能体进行宏观决策，子智能体基于胁迫因子动态优化每日策略。
3. 实验结果表明，NDRL相较于最佳基线，产量提升4.7%，灌溉用水生产率提升5.1%-5.6%，氮素偏生产率提升1.0%-6.3%。

## 📝 摘要（中文）

本文提出了一种嵌套双智能体强化学习(NDRL)方法，旨在解决作物生长过程中水氮组合优化的高复杂性和产量优化结果不佳的问题，以及量化轻微胁迫信号的困难和反馈延迟的问题，从而提高水氮动态调节的精确性和资源利用效率。NDRL中的父智能体基于预测的累积产量效益识别有前景的宏观灌溉和施肥行动，减少无效探索，同时保持目标与产量之间的一致性。子智能体的奖励函数结合了量化的水分胁迫因子(WSF)和氮素胁迫因子(NSF)，并使用混合概率分布来动态优化每日策略，从而提高产量和资源效率。使用2023年和2024年的田间试验数据校准和验证了农业技术转移决策支持系统(DSSAT)，以模拟真实世界条件并与NDRL交互。实验结果表明，与最佳基线相比，2023年和2024年的模拟产量均提高了4.7%，灌溉用水生产率分别提高了5.6%和5.1%，氮素偏生产率分别提高了6.3%和1.0%。该方法推动了棉花灌溉和氮肥施用的发展，为解决农业资源管理中的复杂性和精确性问题以及可持续农业发展提供了新思路。

## 🔬 方法详解

**问题定义**：论文旨在解决棉花种植过程中，如何精确控制灌溉和施氮量，以最大化产量并提高资源利用率的问题。现有方法的痛点在于难以在复杂的水氮组合中找到最优解，且对作物轻微胁迫的感知不精确，导致资源浪费和产量损失。

**核心思路**：论文的核心思路是利用嵌套的双智能体强化学习框架，将宏观决策（长期产量目标）和微观调控（每日水氮策略）相结合。父智能体负责根据预测的累积产量效益选择有前景的宏观行动，减少无效探索；子智能体则根据量化的水分和氮素胁迫因子，动态优化每日策略，从而实现产量和资源效率的双重提升。

**技术框架**：NDRL的整体架构包含两个智能体：父智能体和子智能体。父智能体基于DSSAT模拟的长期产量预测，选择宏观的水氮管理策略。子智能体则在父智能体设定的宏观策略下，根据每日的WSF和NSF，利用混合概率分布动态调整每日的灌溉和施氮量。DSSAT作为环境模拟器，提供作物生长状态和产量反馈。

**关键创新**：NDRL的关键创新在于嵌套的双智能体结构和基于胁迫因子的奖励函数设计。双智能体结构实现了宏观目标和微观调控的有效结合，克服了传统单智能体强化学习在复杂环境中的探索难题。基于WSF和NSF的奖励函数能够更精确地反映作物的水氮需求，从而指导子智能体做出更合理的决策。

**关键设计**：子智能体使用混合概率分布来选择每日的灌溉和施氮量，这种设计允许智能体在探索和利用之间进行平衡。WSF和NSF的计算方式需要根据具体的作物生理模型和环境条件进行调整。父智能体的奖励函数设计需要充分考虑长期产量目标和资源利用率之间的权衡。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16408v1/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16408v1/x3.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16408v1/x4.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

实验结果表明，NDRL在模拟环境下显著提升了棉花产量和资源利用率。与最佳基线相比，2023年和2024年的模拟产量均提高了4.7%，灌溉用水生产率分别提高了5.6%和5.1%，氮素偏生产率分别提高了6.3%和1.0%。这些数据表明，NDRL能够有效地优化水氮管理策略，实现产量和资源效率的双重提升。

## 🎯 应用场景

该研究成果可应用于精准农业领域，为棉花等作物的灌溉和施氮管理提供决策支持。通过NDRL，可以实现水肥资源的优化配置，提高作物产量和资源利用率，降低农业生产成本，并促进农业可持续发展。该方法也可推广到其他作物和农业场景，具有广阔的应用前景。

## 📄 摘要（原文）

> Effective irrigation and nitrogen fertilization have a significant impact on crop yield. However, existing research faces two limitations: (1) the high complexity of optimizing water-nitrogen combinations during crop growth and poor yield optimization results; and (2) the difficulty in quantifying mild stress signals and the delayed feedback, which results in less precise dynamic regulation of water and nitrogen and lower resource utilization efficiency. To address these issues, we propose a Nested Dual-Agent Reinforcement Learning (NDRL) method. The parent agent in NDRL identifies promising macroscopic irrigation and fertilization actions based on projected cumulative yield benefits, reducing ineffective explorationwhile maintaining alignment between objectives and yield. The child agent's reward function incorporates quantified Water Stress Factor (WSF) and Nitrogen Stress Factor (NSF), and uses a mixed probability distribution to dynamically optimize daily strategies, thereby enhancing both yield and resource efficiency. We used field experiment data from 2023 and 2024 to calibrate and validate the Decision Support System for Agrotechnology Transfer (DSSAT) to simulate real-world conditions and interact with NDRL. Experimental results demonstrate that, compared to the best baseline, the simulated yield increased by 4.7% in both 2023 and 2024, the irrigation water productivity increased by 5.6% and 5.1% respectively, and the nitrogen partial factor productivity increased by 6.3% and 1.0% respectively. Our method advances the development of cotton irrigation and nitrogen fertilization, providing new ideas for addressing the complexity and precision issues in agricultural resource management and for sustainable agricultural development.

