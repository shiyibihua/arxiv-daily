---
layout: default
title: Reinforcement Learning with Rubric Anchors
---

# Reinforcement Learning with Rubric Anchors

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.12790" class="toolbar-btn" target="_blank">📄 arXiv: 2508.12790v1</a>
  <a href="https://arxiv.org/pdf/2508.12790.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.12790v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.12790v1', 'Reinforcement Learning with Rubric Anchors')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zenan Huang, Yihong Zhuang, Guoshan Lu, Zeyu Qin, Haokai Xu, Tianyu Zhao, Ru Peng, Jiaqi Hu, Zhanming Shen, Xiaomeng Hu, Xijun Gu, Peiyi Tu, Jiaxin Liu, Wenyu Chen, Yuzhuo Fu, Zhiting Fan, Yanmei Gu, Yuanyuan Wang, Zhengkai Yang, Jianguo Li, Junbo Zhao

**分类**: cs.AI, cs.CL, cs.LG

**发布日期**: 2025-08-18

**备注**: technical report

---

## 💡 一句话要点

**提出基于评分标准的强化学习以解决开放任务的评估问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `强化学习` `评分标准` `大型语言模型` `自动评分` `开放任务` `模型训练` `人机交互`

## 📋 核心要点

1. 现有的RLVR方法主要依赖于可验证的奖励信号，限制了其在开放任务中的应用。
2. 本文通过引入基于评分标准的奖励，构建了一个包含超过10,000个评分标准的系统，以支持主观输出的自动评分。
3. 实验结果显示，Qwen-30B-A3B模型在开放任务基准上提升了5.2%，超越了671B的DeepSeek-V3模型，且保持了推理能力。

## 📝 摘要（中文）

可验证奖励的强化学习（RLVR）已成为增强大型语言模型（LLMs）的强大范式，但其主要局限于具有自动可检查结果的领域。为此，本文通过引入基于评分标准的奖励，扩展了RLVR的应用范围，构建了迄今为止最大的评分标准奖励系统，包含超过10,000个评分标准。我们提出的Qwen-30B-A3B模型在开放任务基准上取得了显著提升，尤其是在文科领域，且在保持一般性和推理能力的同时，提供了更细致的风格控制。我们分享了评分标准构建和训练的关键经验，并讨论了局限性和未来的发布计划。

## 🔬 方法详解

**问题定义**：本文旨在解决现有RLVR方法在开放任务中无法有效评估主观输出的问题，现有方法依赖于自动可检查的结果，限制了其应用范围。

**核心思路**：通过引入基于评分标准的奖励机制，构建一个结构化且可解释的评分系统，以支持对主观输出的自动化评估，从而扩展RLVR的应用场景。

**技术框架**：整体架构包括评分标准的设计、数据选择、模型训练等多个阶段，重点在于如何将评分标准有效整合到强化学习过程中。

**关键创新**：构建了迄今为止最大的评分标准奖励系统，包含来自人类、LLMs及其混合的评分标准，显著提升了模型在开放任务中的表现。

**关键设计**：在模型训练中，采用了特定的损失函数和网络结构，以确保评分标准的有效性和模型的响应风格控制。

## 📊 实验亮点

实验结果表明，Qwen-30B-A3B模型在开放任务基准上提升了5.2%，尤其在文科领域表现突出，超越了671B的DeepSeek-V3模型2.4%。该方法还提供了更细致的风格控制，减少了“AI式”语调，使输出更具人类表达特征。

## 🎯 应用场景

该研究的潜在应用领域包括教育、内容生成和人机交互等，能够为主观性较强的任务提供更为可靠的自动评分机制，提升用户体验和模型的实用性。未来，该方法可能在更多开放任务中得到应用，推动人工智能在复杂场景中的发展。

## 📄 摘要（原文）

> Reinforcement Learning from Verifiable Rewards (RLVR) has emerged as a powerful paradigm for enhancing Large Language Models (LLMs), exemplified by the success of OpenAI's o-series. In RLVR, rewards are derived from verifiable signals-such as passing unit tests in code generation or matching correct answers in mathematical reasoning. While effective, this requirement largely confines RLVR to domains with automatically checkable outcomes. To overcome this, we extend the RLVR paradigm to open-ended tasks by integrating rubric-based rewards, where carefully designed rubrics serve as structured, model-interpretable criteria for automatic scoring of subjective outputs. We construct, to our knowledge, the largest rubric reward system to date, with over 10,000 rubrics from humans, LLMs, or a hybrid human-LLM collaboration. Implementing rubric-based RL is challenging; we tackle these issues with a clear framework and present an open-sourced Qwen-30B-A3B model with notable gains: 1) With only 5K+ samples, our system improves by +5.2% on open-ended benchmarks (especially humanities), outperforming a 671B DeepSeek-V3 model by +2.4%, while preserving general and reasoning abilities. 2) Our method provides fine-grained stylistic control, using rubrics as anchors to mitigate the "AI-like" tone and produce more human-like, expressive responses. We share key lessons in rubric construction, data selection, and training, and discuss limitations and future releases.

