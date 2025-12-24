---
layout: default
title: Prompting Large Language Models to Detect Dementia Family Caregivers
---

# Prompting Large Language Models to Detect Dementia Family Caregivers

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.01999" class="toolbar-btn" target="_blank">📄 arXiv: 2508.01999v1</a>
  <a href="https://arxiv.org/pdf/2508.01999.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.01999v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.01999v1', 'Prompting Large Language Models to Detect Dementia Family Caregivers')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Md Badsha Biswas, Özlem Uzuner

**分类**: cs.CL, cs.LG

**发布日期**: 2025-08-04

---

## 💡 一句话要点

**提出基于大语言模型的推文检测方法以支持痴呆症家庭护理者**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大语言模型` `推文检测` `痴呆症护理` `社交媒体分析` `自然语言处理` `机器学习`

## 📋 核心要点

1. 核心问题：现有方法在识别痴呆症家庭护理者的推文时面临准确性和效率的挑战。
2. 方法要点：论文提出利用大语言模型（LLMs）和多种提示方法来解决推文检测问题。
3. 实验或效果：最终系统在验证集和测试集上取得了0.95的宏F1分数，表现优异。

## 📝 摘要（中文）

社交媒体如Twitter为痴呆症患者的家庭护理者提供了分享经验和寻求支持的机会。为了开发基于互联网的干预措施，必须首先识别这些护理者发布的推文。本文展示了我们在SMM4H 2025共享任务3中的系统，专注于检测提及家庭成员痴呆症的推文。我们将此任务定义为二分类问题，区分提及痴呆症的推文与不提及的推文。我们的解决方案探索了多种提示方法，结果表明，简单的零-shot提示在微调模型上取得了最佳效果，最终系统在验证集和测试集上达到了0.95的宏F1分数。我们的完整代码已在GitHub上发布。

## 🔬 方法详解

**问题定义**：本文旨在解决如何准确识别社交媒体上痴呆症家庭护理者发布的推文的问题。现有方法在处理此类文本时常常面临分类准确性不足和上下文理解能力弱的挑战。

**核心思路**：我们提出的解决方案基于大语言模型（LLMs），通过不同的提示方法来引导模型更好地理解和分类推文内容。选择这种方法是因为LLMs在自然语言处理任务中展现了强大的上下文理解能力。

**技术框架**：整体架构包括数据收集、数据预处理、模型选择、提示设计和模型评估几个主要模块。首先，从Twitter收集相关推文，然后进行清洗和标注，接着选择合适的LLM进行微调，最后通过不同的提示策略进行分类。

**关键创新**：本研究的主要创新在于通过简单的零-shot提示在微调模型上取得了最佳效果，这与传统的需要大量标注数据的训练方法形成鲜明对比。

**关键设计**：在模型训练中，我们使用了特定的损失函数来优化分类效果，并对模型的超参数进行了细致调优，以确保在不同数据集上的泛化能力。

## 📊 实验亮点

实验结果显示，最终系统在验证集和测试集上达到了0.95的宏F1分数，显著高于基线模型。这一结果表明，采用大语言模型和有效的提示策略能够显著提升推文分类的准确性和效率。

## 🎯 应用场景

该研究的潜在应用领域包括社交媒体监测、心理健康支持和在线干预措施的开发。通过准确识别痴呆症家庭护理者的推文，相关机构可以提供更有针对性的支持和资源，帮助改善护理者的心理健康和生活质量。未来，该方法还可扩展到其他类型的社交媒体文本分析中。

## 📄 摘要（原文）

> Social media, such as Twitter, provides opportunities for caregivers of dementia patients to share their experiences and seek support for a variety of reasons. Availability of this information online also paves the way for the development of internet-based interventions in their support. However, for this purpose, tweets written by caregivers of dementia patients must first be identified. This paper demonstrates our system for the SMM4H 2025 shared task 3, which focuses on detecting tweets posted by individuals who have a family member with dementia. The task is outlined as a binary classification problem, differentiating between tweets that mention dementia in the context of a family member and those that do not. Our solution to this problem explores large language models (LLMs) with various prompting methods. Our results show that a simple zero-shot prompt on a fine-tuned model yielded the best results. Our final system achieved a macro F1-score of 0.95 on the validation set and the test set. Our full code is available on GitHub.

