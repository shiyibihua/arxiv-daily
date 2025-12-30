---
layout: default
title: Eliciting Behaviors in Multi-Turn Conversations
---

# Eliciting Behaviors in Multi-Turn Conversations

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.23701" class="toolbar-btn" target="_blank">📄 arXiv: 2512.23701v1</a>
  <a href="https://arxiv.org/pdf/2512.23701.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.23701v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.23701v1', 'Eliciting Behaviors in Multi-Turn Conversations')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jing Huang, Shujian Zhang, Lun Wang, Andrew Hard, Rajiv Mathews, John Lambert

**分类**: cs.CL, cs.LG

**发布日期**: 2025-12-29

---

## 💡 一句话要点

**提出多轮对话行为引导方法以提升评估效果**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多轮对话` `行为引导` `自然语言处理` `动态评估` `大型语言模型`

## 📋 核心要点

1. 现有方法主要集中在单轮对话，缺乏对多轮对话中复杂行为的有效引导与评估。
2. 论文提出了一种新的多轮对话行为引导框架，整合了单轮与多轮的引导方法，提升了模型的交互能力。
3. 实验结果显示，在线方法在多个任务中成功率显著高于传统静态方法，展示了动态评估的潜力。

## 📝 摘要（中文）

识别大型语言模型在对话环境中的特定复杂行为对于其评估至关重要。尽管已有研究提出了诱导特定行为的自然语言提示技术，但主要集中在单轮对话中。本研究探讨了多轮对话中的行为引导，首先提供了一个分析框架，将现有方法分为三类：仅使用先前知识的方法、离线交互的方法和在线交互的方法。我们引入了一种在线方法的多轮通用形式，统一了单轮和多轮引导。通过自动生成多轮测试用例评估这三类方法，分析了查询预算与成功率之间的权衡，发现在线方法在三个任务中平均成功率达到了45/19/77%，而现有基准的静态方法几乎未能发现失败案例。我们的研究强调了行为引导方法在多轮对话评估中的新应用，以及社区向动态基准发展的必要性。

## 🔬 方法详解

**问题定义**：本研究旨在解决现有方法在多轮对话中无法有效引导复杂行为的问题。现有方法多集中于单轮对话，导致对多轮交互的评估不足。

**核心思路**：论文提出了一种多轮对话的行为引导方法，通过分析现有方法的不足，设计了一个统一的框架，能够同时处理单轮和多轮的行为引导。

**技术框架**：整体架构包括三个主要模块：基于先前知识的引导、离线交互引导和在线交互引导。通过这些模块的组合，形成了一个灵活的多轮对话行为引导系统。

**关键创新**：最重要的创新在于引入了在线交互的方法，能够在多轮对话中动态调整引导策略，与静态方法相比，显著提高了行为发现的成功率。

**关键设计**：在参数设置上，研究对查询预算进行了优化，确保在有限的交互次数内最大化成功率。损失函数和网络结构经过精心设计，以适应多轮对话的复杂性。具体细节包括对输入的动态调整和反馈机制的实现。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.23701v1/figs/benchmark_saturation.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.23701v1/x1.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.23701v1/x2.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

实验结果表明，在线方法在三个任务中的平均成功率分别为45%、19%和77%，显著高于现有静态方法的表现，展示了动态评估在多轮对话中的有效性和必要性。

## 🎯 应用场景

该研究的潜在应用领域包括智能客服、虚拟助手和教育领域等多轮对话系统。通过提升对话系统的行为引导能力，可以显著改善用户体验和系统的交互质量，未来可能推动更智能的对话系统发展。

## 📄 摘要（原文）

> Identifying specific and often complex behaviors from large language models (LLMs) in conversational settings is crucial for their evaluation. Recent work proposes novel techniques to find natural language prompts that induce specific behaviors from a target model, yet they are mainly studied in single-turn settings. In this work, we study behavior elicitation in the context of multi-turn conversations. We first offer an analytical framework that categorizes existing methods into three families based on their interactions with the target model: those that use only prior knowledge, those that use offline interactions, and those that learn from online interactions. We then introduce a generalized multi-turn formulation of the online method, unifying single-turn and multi-turn elicitation. We evaluate all three families of methods on automatically generating multi-turn test cases. We investigate the efficiency of these approaches by analyzing the trade-off between the query budget, i.e., the number of interactions with the target model, and the success rate, i.e., the discovery rate of behavior-eliciting inputs. We find that online methods can achieve an average success rate of 45/19/77% with just a few thousand queries over three tasks where static methods from existing multi-turn conversation benchmarks find few or even no failure cases. Our work highlights a novel application of behavior elicitation methods in multi-turn conversation evaluation and the need for the community to move towards dynamic benchmarks.

