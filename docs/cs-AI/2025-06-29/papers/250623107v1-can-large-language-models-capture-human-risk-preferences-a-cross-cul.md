---
layout: default
title: Can Large Language Models Capture Human Risk Preferences? A Cross-Cultural Study
---

# Can Large Language Models Capture Human Risk Preferences? A Cross-Cultural Study

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.23107" class="toolbar-btn" target="_blank">📄 arXiv: 2506.23107v1</a>
  <a href="https://arxiv.org/pdf/2506.23107.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.23107v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.23107v1', 'Can Large Language Models Capture Human Risk Preferences? A Cross-Cultural Study')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Bing Song, Jianing Liu, Sisi Jian, Chenyang Wu, Vinayak Dixit

**分类**: cs.AI

**发布日期**: 2025-06-29

**备注**: 20 pages, 1 figure

---

## 💡 一句话要点

**研究大型语言模型在模拟人类风险偏好中的有效性**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `风险偏好` `决策模拟` `跨文化研究` `CRRA框架`

## 📋 核心要点

1. 现有大型语言模型在模拟复杂决策行为时存在可靠性不足的问题，尤其是在风险决策场景中。
2. 本研究通过对比模型生成的决策与人类反应，探讨LLMs在风险偏好模拟中的表现，采用CRRA框架进行分析。
3. 实验结果表明，模型表现出更强的风险厌恶倾向，且o1-mini模型的决策与人类更为一致，提示语言影响模型性能。

## 📝 摘要（中文）

大型语言模型（LLMs）在对话系统、自动内容创作和特定领域咨询任务中取得了显著进展。然而，随着其应用的增加，关于其在复杂决策行为模拟中的可靠性问题逐渐显现。本研究探讨了LLMs在模拟风险决策场景中的能力。通过对悉尼、达卡、香港和南京参与者的抽样调查数据进行分析，比较了模型生成的决策与实际人类反应。结果显示，两种模型表现出比人类参与者更为风险厌恶的行为，其中o1-mini模型与观察到的人类决策更为一致。此外，来自南京和香港的多语言数据分析表明，中文模型预测与实际反应的偏差大于英文，提示提示语言可能影响模拟性能。这些发现突显了LLMs在复制人类风险行为方面的潜力与当前局限性，尤其是在语言和文化背景下。

## 🔬 方法详解

**问题定义**：本研究旨在解决大型语言模型在模拟人类风险偏好时的可靠性问题。现有方法在复杂决策行为的模拟上存在不足，尤其是在不同文化和语言背景下的表现不一致。

**核心思路**：论文通过对比模型生成的决策与实际人类反应，评估LLMs在风险决策场景中的能力，采用CRRA框架分析风险偏好。

**技术框架**：研究设计包括数据收集、模型输入、决策生成和结果分析四个主要模块。数据来自不同文化背景的参与者，模型输入包括人口统计信息。

**关键创新**：本研究的创新点在于首次系统性地比较了不同语言模型在模拟人类风险偏好时的表现，揭示了语言对模型预测的影响。

**关键设计**：使用了两种不同的LLMs（ChatGPT 4o和ChatGPT o1-mini），并在模型输入中考虑了参与者的文化背景和语言，采用CRRA框架进行风险偏好分析。

## 📊 实验亮点

实验结果显示，LLMs在模拟风险决策时表现出更强的风险厌恶倾向，o1-mini模型的决策与人类反应更为一致。此外，中文模型的预测与实际反应的偏差大于英文，提示语言可能显著影响模型性能。

## 🎯 应用场景

该研究的潜在应用领域包括金融决策支持、市场营销策略设计以及跨文化交流中的决策模拟。通过更好地理解LLMs在风险决策中的表现，可以提升其在实际应用中的可靠性和有效性，推动智能决策系统的发展。

## 📄 摘要（原文）

> Large language models (LLMs) have made significant strides, extending their applications to dialogue systems, automated content creation, and domain-specific advisory tasks. However, as their use grows, concerns have emerged regarding their reliability in simulating complex decision-making behavior, such as risky decision-making, where a single choice can lead to multiple outcomes. This study investigates the ability of LLMs to simulate risky decision-making scenarios. We compare model-generated decisions with actual human responses in a series of lottery-based tasks, using transportation stated preference survey data from participants in Sydney, Dhaka, Hong Kong, and Nanjing. Demographic inputs were provided to two LLMs -- ChatGPT 4o and ChatGPT o1-mini -- which were tasked with predicting individual choices. Risk preferences were analyzed using the Constant Relative Risk Aversion (CRRA) framework. Results show that both models exhibit more risk-averse behavior than human participants, with o1-mini aligning more closely with observed human decisions. Further analysis of multilingual data from Nanjing and Hong Kong indicates that model predictions in Chinese deviate more from actual responses compared to English, suggesting that prompt language may influence simulation performance. These findings highlight both the promise and the current limitations of LLMs in replicating human-like risk behavior, particularly in linguistic and cultural settings.

