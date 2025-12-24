---
layout: default
title: Benchmarking the Legal Reasoning of LLMs in Arabic Islamic Inheritance Cases
---

# Benchmarking the Legal Reasoning of LLMs in Arabic Islamic Inheritance Cases

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.15796" class="toolbar-btn" target="_blank">📄 arXiv: 2508.15796v1</a>
  <a href="https://arxiv.org/pdf/2508.15796.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.15796v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.15796v1', 'Benchmarking the Legal Reasoning of LLMs in Arabic Islamic Inheritance Cases')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Nouar AlDahoul, Yasir Zaki

**分类**: cs.CL, cs.AI, cs.CY, cs.LG

**发布日期**: 2025-08-13

**备注**: 5 pages, 3 figures

---

## 💡 一句话要点

**利用LLMs提升阿拉伯伊斯兰继承案件的法律推理能力**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `法律推理` `大型语言模型` `伊斯兰继承法` `自动化计算` `多模型融合`

## 📋 核心要点

1. 现有手动计算伊斯兰继承份额的方法复杂且容易出错，缺乏高效的自动化工具。
2. 本研究提出利用大型语言模型（LLMs）来自动化法律推理，特别是在伊斯兰继承法的应用上。
3. 实验结果表明，采用多数投票策略的模型在准确率上达到了92.7%，显著优于其他模型。

## 📝 摘要（中文）

伊斯兰继承领域对穆斯林至关重要，以确保继承人之间的公平分配。然而，手动计算在多种情况下的继承份额既复杂又耗时，且容易出错。近期大型语言模型（LLMs）的进展引发了对其在复杂法律推理任务中潜力的关注。本研究评估了最先进的LLMs在解释和应用伊斯兰继承法方面的推理能力。我们利用阿拉伯NLP QIAS 2025挑战中提出的数据集，评估了多种基础和微调模型在准确识别继承人、计算份额及其推理的合理性方面的表现。分析结果显示，采用三种基础模型（Gemini Flash 2.5、Gemini Pro 2.5和GPT o3）的多数投票解决方案在所有难度级别上均优于其他模型，准确率高达92.7%，并在QIAS 2025挑战的任务1中获得第三名。

## 🔬 方法详解

**问题定义**：本研究旨在解决伊斯兰继承法中手动计算继承份额的复杂性和低效性。现有方法在处理多种场景时容易出错，缺乏自动化支持。

**核心思路**：论文提出利用大型语言模型（LLMs）来自动化法律推理过程，特别是通过结合多个基础模型的输出，以提高推理的准确性和可靠性。

**技术框架**：整体架构包括数据集构建、模型选择与训练、推理过程及结果评估。主要模块包括数据预处理、模型训练、推理逻辑及结果整合。

**关键创新**：最重要的技术创新在于采用多数投票机制结合多个LLMs的输出，显著提升了推理的准确性，与传统单一模型方法相比，具有更强的鲁棒性和准确性。

**关键设计**：在模型选择上，使用了Gemini Flash 2.5、Gemini Pro 2.5和GPT o3三种基础模型，采用了适当的损失函数和参数设置，以确保模型在推理过程中的一致性和准确性。通过微调模型以适应特定的法律场景，进一步提升了性能。

## 📊 实验亮点

实验结果显示，采用多数投票的模型在所有难度级别上均表现优异，准确率高达92.7%。这一结果不仅超越了其他基线模型，还在QIAS 2025挑战的任务1中获得了第三名，展示了该方法在法律推理任务中的有效性。

## 🎯 应用场景

该研究的成果可广泛应用于法律咨询、教育和自动化文书生成等领域，尤其是在伊斯兰法相关的法律事务中。通过提高法律推理的效率和准确性，能够为法律从业者和普通民众提供更为便捷的服务，未来可能推动法律技术的进一步发展。

## 📄 摘要（原文）

> Islamic inheritance domain holds significant importance for Muslims to ensure fair distribution of shares between heirs. Manual calculation of shares under numerous scenarios is complex, time-consuming, and error-prone. Recent advancements in Large Language Models (LLMs) have sparked interest in their potential to assist with complex legal reasoning tasks. This study evaluates the reasoning capabilities of state-of-the-art LLMs to interpret and apply Islamic inheritance laws. We utilized the dataset proposed in the ArabicNLP QIAS 2025 challenge, which includes inheritance case scenarios given in Arabic and derived from Islamic legal sources. Various base and fine-tuned models, are assessed on their ability to accurately identify heirs, compute shares, and justify their reasoning in alignment with Islamic legal principles. Our analysis reveals that the proposed majority voting solution, leveraging three base models (Gemini Flash 2.5, Gemini Pro 2.5, and GPT o3), outperforms all other models that we utilized across every difficulty level. It achieves up to 92.7% accuracy and secures the third place overall in Task 1 of the Qias 2025 challenge.

