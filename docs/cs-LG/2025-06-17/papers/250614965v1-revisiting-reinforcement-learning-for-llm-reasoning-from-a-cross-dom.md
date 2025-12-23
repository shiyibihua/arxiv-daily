---
layout: default
title: Revisiting Reinforcement Learning for LLM Reasoning from A Cross-Domain Perspective
---

# Revisiting Reinforcement Learning for LLM Reasoning from A Cross-Domain Perspective

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.14965" class="toolbar-btn" target="_blank">📄 arXiv: 2506.14965v1</a>
  <a href="https://arxiv.org/pdf/2506.14965.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.14965v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.14965v1', 'Revisiting Reinforcement Learning for LLM Reasoning from A Cross-Domain Perspective')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zhoujun Cheng, Shibo Hao, Tianyang Liu, Fan Zhou, Yutao Xie, Feng Yao, Yuexin Bian, Yonghao Zhuang, Nilabjo Dey, Yuheng Zha, Yi Gu, Kun Zhou, Yuqi Wang, Yuan Li, Richard Fan, Jianshu She, Chengqian Gao, Abulhair Saparov, Haonan Li, Taylor W. Killian, Mikhail Yurochkin, Zhengzhong Liu, Eric P. Xing, Zhiting Hu

**分类**: cs.LG, cs.AI, cs.CL

**发布日期**: 2025-06-17

**备注**: 38 pages, 9 figures. Under review

**🔗 代码/项目**: [GITHUB](https://github.com/LLM360/Reasoning360)

---

## 💡 一句话要点

**提出Guru以解决大语言模型推理中的奖励信号不足问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `强化学习` `大语言模型` `推理能力` `跨领域训练` `语料库设计` `模型评估` `复杂任务`

## 📋 核心要点

1. 现有的强化学习方法在大语言模型推理中主要集中于数学和代码，缺乏对其他推理领域的有效支持。
2. 本文提出Guru语料库，通过设计领域特定的奖励信号，提供了一个可靠且可扩展的RL训练基础。
3. 实验结果显示，Guru-7B和Guru-32B模型在多项任务中表现优异，显著提升了基线模型的性能。

## 📝 摘要（中文）

强化学习（RL）已成为提升大语言模型（LLM）推理能力的有前景的方法，然而现有研究主要集中在数学和代码领域，限制了其在更广泛推理领域的应用理解。本文引入Guru，一个包含92K可验证示例的RL推理语料库，涵盖数学、代码、科学、逻辑、仿真和表格六个推理领域。通过系统性地回顾RL在LLM推理中的既有发现，观察到不同领域间的显著差异。研究表明，RL不仅能从预训练模型中提取知识，还能促进真实技能的获取。最后，提出的Guru-7B和Guru-32B模型在17项任务评估中超越最佳基线，分别提升7.9%和6.7%。

## 🔬 方法详解

**问题定义**：本文旨在解决大语言模型推理中缺乏可靠和可扩展的强化学习奖励信号的问题。现有方法主要集中于数学和代码，未能有效覆盖其他推理领域。

**核心思路**：论文提出Guru语料库，包含92K个可验证示例，涵盖六个推理领域，通过领域特定的奖励设计和去重过滤，确保训练的可靠性和有效性。

**技术框架**：整体架构包括数据收集、奖励设计、模型训练和评估四个主要模块。数据收集阶段构建多领域的推理示例，奖励设计阶段针对每个领域制定特定的奖励信号，模型训练阶段使用强化学习算法进行训练，评估阶段则通过17项任务进行性能验证。

**关键创新**：最重要的创新在于提出了Guru语料库，系统性地解决了不同推理领域间的奖励信号不足问题，展示了跨领域训练的有效性。

**关键设计**：在模型训练中，采用了特定的损失函数和网络结构，确保模型能够有效学习到各领域的推理技能，同时对复杂任务的表现进行了优化。具体参数设置和网络结构细节在论文中有详细描述。

## 📊 实验亮点

实验结果显示，Guru-7B和Guru-32B模型在17项任务评估中分别超越最佳基线7.9%和6.7%。这些模型在复杂任务上的表现尤为突出，显著提升了基础模型的Pass@k性能，尤其是在预训练数据中较少出现的任务上。

## 🎯 应用场景

该研究的潜在应用领域包括教育、科学研究、编程辅助等，能够为复杂推理任务提供更强大的支持。通过提升大语言模型的推理能力，未来可能在自动化决策、智能问答等领域产生深远影响。

## 📄 摘要（原文）

> Reinforcement learning (RL) has emerged as a promising approach to improve large language model (LLM) reasoning, yet most open efforts focus narrowly on math and code, limiting our understanding of its broader applicability to general reasoning. A key challenge lies in the lack of reliable, scalable RL reward signals across diverse reasoning domains. We introduce Guru, a curated RL reasoning corpus of 92K verifiable examples spanning six reasoning domains--Math, Code, Science, Logic, Simulation, and Tabular--each built through domain-specific reward design, deduplication, and filtering to ensure reliability and effectiveness for RL training. Based on Guru, we systematically revisit established findings in RL for LLM reasoning and observe significant variation across domains. For example, while prior work suggests that RL primarily elicits existing knowledge from pretrained models, our results reveal a more nuanced pattern: domains frequently seen during pretraining (Math, Code, Science) easily benefit from cross-domain RL training, while domains with limited pretraining exposure (Logic, Simulation, and Tabular) require in-domain training to achieve meaningful performance gains, suggesting that RL is likely to facilitate genuine skill acquisition. Finally, we present Guru-7B and Guru-32B, two models that achieve state-of-the-art performance among open models RL-trained with publicly available data, outperforming best baselines by 7.9% and 6.7% on our 17-task evaluation suite across six reasoning domains. We also show that our models effectively improve the Pass@k performance of their base models, particularly on complex tasks less likely to appear in pretraining data. We release data, models, training and evaluation code to facilitate general-purpose reasoning at: https://github.com/LLM360/Reasoning360

