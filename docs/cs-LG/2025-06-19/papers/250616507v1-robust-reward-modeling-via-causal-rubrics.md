---
layout: default
title: Robust Reward Modeling via Causal Rubrics
---

# Robust Reward Modeling via Causal Rubrics

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.16507" class="toolbar-btn" target="_blank">📄 arXiv: 2506.16507v1</a>
  <a href="https://arxiv.org/pdf/2506.16507.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.16507v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.16507v1', 'Robust Reward Modeling via Causal Rubrics')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Pragya Srivastava, Harman Singh, Rahul Madhavan, Gandharv Patil, Sravanti Addepalli, Arun Suggala, Rengarajan Aravamudhan, Soumya Sharma, Anirban Laha, Aravindan Raghuveer, Karthikeyan Shanmugam, Doina Precup

**分类**: cs.LG

**发布日期**: 2025-06-19

---

## 💡 一句话要点

**提出Crome框架以解决奖励模型中的奖励黑客问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `奖励模型` `因果建模` `人类反馈` `大型语言模型` `鲁棒性` `深度学习` `模型对齐`

## 📋 核心要点

1. 现有奖励模型容易受到奖励黑客的影响，导致模型依赖表面特征而非真正的因果因素。
2. Crome框架通过因果增强和中性增强技术，旨在提高模型对因果属性的敏感性和对虚假属性的鲁棒性。
3. 实验结果表明，Crome在多个基准测试中显著优于标准基线，平均准确率提升达5.4%。

## 📝 摘要（中文）

奖励模型（RMs）是通过人类反馈对大型语言模型（LLMs）进行对齐的基础，但它们常常受到奖励黑客的影响。现有模型容易依赖表面或虚假的属性，如响应长度或格式，误将这些从训练数据中学习到的相关性视为质量的真正因果驱动因素。为此，本文提出了Crome（因果鲁棒奖励建模），一个基于明确因果模型的新框架，旨在减轻奖励黑客现象。Crome在训练过程中采用了合成的目标增强技术，包括因果增强和中性增强，显著提升了在RewardBench上的表现，平均准确率提高了5.4%。

## 🔬 方法详解

**问题定义**：本文旨在解决奖励模型在对齐大型语言模型时面临的奖励黑客问题。现有方法往往无法有效区分因果属性与虚假属性，导致模型表现脆弱。

**核心思路**：Crome框架通过引入因果增强和中性增强，分别强化模型对因果属性的敏感性和对虚假属性的鲁棒性。通过这种设计，模型能够更好地识别和利用真正的因果驱动因素。

**技术框架**：Crome的整体架构包括两个主要模块：因果增强模块和中性增强模块。因果增强模块生成在特定因果属性上有差异的样本对，而中性增强模块则生成在虚假属性上有差异的样本对。

**关键创新**：Crome的主要创新在于其合成目标增强技术，能够在没有虚假因素知识的情况下，通过查询一个oracle LLM生成增强样本。这一方法与传统的奖励模型训练方法有本质区别。

**关键设计**：在训练过程中，Crome采用了特定的损失函数来优化模型对因果属性的敏感性，同时确保模型对虚假属性的鲁棒性。具体的参数设置和网络结构细节在实验部分进行了详细描述。

## 📊 实验亮点

Crome在多个基准测试中表现出色，尤其是在RewardBench上，平均准确率提高了5.4%。在特定类别中，Crome的提升幅度达到13.2%和7.2%。这些结果表明Crome在应对奖励黑客方面的有效性和鲁棒性。

## 🎯 应用场景

Crome框架在对齐大型语言模型方面具有广泛的应用潜力，尤其是在需要高质量人类反馈的任务中，如对话系统和内容生成。通过提高奖励模型的鲁棒性，Crome能够帮助开发更可靠的AI系统，减少因奖励黑客导致的偏差，从而提升用户体验和安全性。

## 📄 摘要（原文）

> Reward models (RMs) are fundamental to aligning Large Language Models (LLMs) via human feedback, yet they often suffer from reward hacking. They tend to latch on to superficial or spurious attributes, such as response length or formatting, mistaking these cues learned from correlations in training data for the true causal drivers of quality (e.g., factuality, relevance). This occurs because standard training objectives struggle to disentangle these factors, leading to brittle RMs and misaligned policies. We introduce Crome (Causally Robust Reward Modeling), a novel framework grounded in an explicit causal model designed to mitigate reward hacking. Crome employs the following synthetic targeted augmentations during training: (1) Causal Augmentations, which are pairs that differ along specific causal attributes, to enforce sensitivity along each causal attribute individually, and (2) Neutral Augmentations, which are tie-label pairs varying primarily in spurious attributes, to enforce invariance along spurious attributes. Notably, our augmentations are produced without any knowledge of spurious factors, via answer interventions only along causal rubrics, that are identified by querying an oracle LLM. Empirically, Crome significantly outperforms standard baselines on RewardBench, improving average accuracy by up to 5.4% and achieving gains of up to 13.2% and 7.2% in specific categories. The robustness of Crome is further testified by the consistent gains obtained in a Best-of-N inference setting across increasing N, across various benchmarks, including the popular RewardBench (covering chat, chat-hard, safety, and reasoning tasks), the safety-focused WildGuardTest, and the reasoning-specific GSM8k.

