---
layout: default
title: MobileWorldBench: Towards Semantic World Modeling For Mobile Agents
---

# MobileWorldBench: Towards Semantic World Modeling For Mobile Agents

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.14014" class="toolbar-btn" target="_blank">📄 arXiv: 2512.14014v1</a>
  <a href="https://arxiv.org/pdf/2512.14014.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.14014v1" onclick="toggleFavorite(this, '2512.14014v1', 'MobileWorldBench: Towards Semantic World Modeling For Mobile Agents')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Shufan Li, Konstantinos Kallidromitis, Akash Gokul, Yusuke Kato, Kazuki Kozuka, Aditya Grover

**分类**: cs.AI

**发布日期**: 2025-12-16

**备注**: 21 pages, 13 figures

**🔗 代码/项目**: [GITHUB](https://github.com/jacklishufan/MobileWorld)

---

## 💡 一句话要点

**提出MobileWorldBench，用于评估移动Agent的语义世界建模能力**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `世界模型` `视觉-语言模型` `移动Agent` `GUI自动化` `语义建模`

## 📋 核心要点

1. 现有像素空间世界模型在GUI环境中预测复杂视觉元素面临挑战，限制了其在移动Agent中的应用。
2. 论文提出使用自然语言描述状态转换的语义世界模型，利用视觉-语言模型（VLM）进行世界建模。
3. 实验表明，集成了VLM世界模型的规划框架能够提高移动Agent的任务成功率，验证了语义世界模型的有效性。

## 📝 摘要（中文）

世界模型在提升具身智能体的任务表现方面展现出巨大潜力。然而，现有工作主要集中于像素空间的世界模型，在GUI环境中面临实际限制，因为预测未来状态中复杂的视觉元素通常很困难。本文探索了一种针对GUI智能体的世界建模替代方案，其中状态转换用自然语言描述，而不是预测原始像素。首先，我们引入MobileWorldBench，一个评估视觉-语言模型（VLM）作为移动GUI智能体世界模型能力的基准。其次，我们发布MobileWorld，一个包含140万样本的大规模数据集，显著提升了VLM的世界建模能力。最后，我们提出了一个将VLM世界模型集成到移动智能体规划框架中的新框架，证明了语义世界模型可以通过提高任务成功率直接使移动智能体受益。代码和数据集可在https://github.com/jacklishufan/MobileWorld 获取。

## 🔬 方法详解

**问题定义**：现有基于像素空间的世界模型难以准确预测GUI环境中复杂视觉元素的变化，导致移动Agent在GUI任务中表现不佳。痛点在于像素级别的预测对于理解GUI元素的语义信息和状态转换关系存在困难。

**核心思路**：论文的核心思路是利用视觉-语言模型（VLM）将GUI状态转换为自然语言描述，并预测状态转换的语义变化。通过自然语言描述，模型可以更好地理解GUI元素的语义信息，从而更准确地预测未来状态。

**技术框架**：整体框架包含三个主要部分：1）使用VLM将GUI状态编码为自然语言描述；2）利用编码后的自然语言描述构建世界模型，预测未来状态的语义变化；3）将世界模型集成到移动Agent的规划框架中，指导Agent执行任务。

**关键创新**：关键创新在于使用自然语言作为世界模型的中间表示，避免了直接预测像素的困难。这种语义世界模型能够更好地捕捉GUI元素的语义信息和状态转换关系，从而提高移动Agent的任务成功率。

**关键设计**：MobileWorld数据集包含140万个样本，用于训练和评估VLM的世界建模能力。论文还设计了一种新的规划框架，将VLM世界模型集成到移动Agent中。具体的VLM模型选择和训练细节以及规划算法的具体实现细节在论文中有详细描述。

## 📊 实验亮点

论文提出的MobileWorldBench基准和MobileWorld数据集显著提升了VLM的世界建模能力。实验结果表明，集成了VLM世界模型的规划框架能够显著提高移动Agent的任务成功率，具体提升幅度在论文中有详细数据展示，证明了语义世界模型的有效性。

## 🎯 应用场景

该研究成果可应用于开发更智能的移动Agent，例如自动化测试、智能助手和自动化办公等领域。通过理解GUI元素的语义信息和预测状态转换，Agent可以更有效地完成各种GUI任务，提高工作效率和用户体验。未来，该方法还可以扩展到其他类型的具身智能体和环境。

## 📄 摘要（原文）

> World models have shown great utility in improving the task performance of embodied agents. While prior work largely focuses on pixel-space world models, these approaches face practical limitations in GUI settings, where predicting complex visual elements in future states is often difficult. In this work, we explore an alternative formulation of world modeling for GUI agents, where state transitions are described in natural language rather than predicting raw pixels. First, we introduce MobileWorldBench, a benchmark that evaluates the ability of vision-language models (VLMs) to function as world models for mobile GUI agents. Second, we release MobileWorld, a large-scale dataset consisting of 1.4M samples, that significantly improves the world modeling capabilities of VLMs. Finally, we propose a novel framework that integrates VLM world models into the planning framework of mobile agents, demonstrating that semantic world models can directly benefit mobile agents by improving task success rates. The code and dataset is available at https://github.com/jacklishufan/MobileWorld

