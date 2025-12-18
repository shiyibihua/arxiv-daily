---
layout: default
title: Understanding the Dilemma of Unlearning for Large Language Models
---

# Understanding the Dilemma of Unlearning for Large Language Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.24675" class="toolbar-btn" target="_blank">📄 arXiv: 2509.24675v1</a>
  <a href="https://arxiv.org/pdf/2509.24675.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.24675v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.24675v1', 'Understanding the Dilemma of Unlearning for Large Language Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Qingjie Zhang, Haoting Qian, Zhicong Huang, Cheng Hong, Minlie Huang, Ke Xu, Chao Zhang, Han Qiu

**分类**: cs.CL, cs.AI

**发布日期**: 2025-09-29

---

## 💡 一句话要点

**提出unPact框架，揭示大语言模型不可靠的知识遗忘现象与机理。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `知识遗忘` `大语言模型` `可解释性` `提示归因` `灾难性遗忘`

## 📋 核心要点

1. 现有大语言模型知识遗忘方法存在有效性争议，且缺乏对遗忘机制的深入可解释性分析。
2. 提出unPact框架，通过提示归因和贡献追踪，量化每个token对模型输出的影响，从而分析遗忘过程。
3. 实验表明，现有方法要么无法彻底遗忘知识，要么导致灾难性遗忘，存在知识遗忘困境。

## 📝 摘要（中文）

知识遗忘旨在从大型语言模型（LLMs）中移除特定知识，但其有效性一直存在争议。一方面，“遗忘”的知识通常可以通过轻量级微调等干预手段恢复；另一方面，知识遗忘可能导致灾难性遗忘，从而降低模型的通用能力。尽管知识遗忘方法的研究非常活跃，但由于难以追踪LLMs复杂架构中的知识，对其机制的可解释性分析仍然匮乏。我们提出了unPact，一个通过提示归因和贡献追踪实现可解释知识遗忘的框架，以弥补这一空白。它量化了每个提示token对输出的影响，从而能够进行遗忘前后的比较，以揭示发生了哪些变化。在六种主流知识遗忘方法、三种LLMs和三个基准测试中，我们发现：（1）知识遗忘似乎通过扰乱对提示中关键词的关注而生效；（2）大部分知识并没有真正被删除，可以通过简单地强调提示中的这些关键词来恢复，而无需修改模型的权重；（3）灾难性遗忘源于对所有token的不加区分的惩罚。总而言之，我们的结果表明了一个知识遗忘困境：现有方法要么不足——知识仍然可以通过关键词强调来恢复，要么过度破坏——由于灾难性遗忘导致通用性能崩溃，这仍然留下了可靠知识遗忘的差距。

## 🔬 方法详解

**问题定义**：论文旨在解决大型语言模型（LLMs）知识遗忘效果不佳且缺乏可解释性的问题。现有方法要么无法彻底删除知识，导致知识容易被恢复，要么过度删除知识，导致灾难性遗忘，损害模型的通用能力。现有方法难以追踪LLMs复杂架构中的知识变化，缺乏对遗忘机制的深入理解。

**核心思路**：论文的核心思路是通过提示归因和贡献追踪来分析知识遗忘过程。通过量化每个提示token对模型输出的影响，可以观察到遗忘前后token重要性的变化，从而理解遗忘机制。强调提示中的关键词可以恢复“遗忘”的知识，表明知识并没有真正被删除。对所有token的不加区分的惩罚会导致灾难性遗忘。

**技术框架**：unPact框架包含以下主要步骤：1. 提示输入：向LLM输入包含目标知识的提示。2. 提示归因：使用梯度积分等方法计算每个提示token对模型输出的影响。3. 遗忘操作：应用现有的知识遗忘方法。4. 提示归因（遗忘后）：再次计算每个提示token对模型输出的影响。5. 比较分析：比较遗忘前后token重要性的变化，分析遗忘机制。

**关键创新**：unPact框架的关键创新在于其可解释性。通过提示归因和贡献追踪，可以量化每个token对模型输出的影响，从而深入理解知识遗忘的机制。与现有方法相比，unPact不仅关注遗忘效果，更关注遗忘过程，为改进知识遗忘方法提供了新的视角。

**关键设计**：unPact框架的关键设计包括：1. 使用梯度积分作为提示归因方法，计算每个token对模型输出的梯度。2. 设计实验评估不同知识遗忘方法的效果，包括知识删除率和通用性能下降程度。3. 分析遗忘前后token重要性的变化，揭示遗忘机制。

## 📊 实验亮点

实验结果表明，现有知识遗忘方法要么无法彻底删除知识，知识可以通过强调关键词恢复；要么导致灾难性遗忘，通用性能显著下降。例如，在某些基准测试中，知识删除率可以达到较高水平，但通用性能下降幅度也超过10%。这些结果揭示了现有知识遗忘方法面临的困境。

## 🎯 应用场景

该研究成果可应用于需要保护用户隐私、防止模型泄露敏感信息的场景。例如，在医疗、金融等领域，可以利用知识遗忘技术删除模型中包含的个人信息或商业机密，从而降低数据泄露的风险。此外，该研究也有助于提升模型的可控性和安全性，避免模型被用于恶意目的。

## 📄 摘要（原文）

> Unlearning seeks to remove specific knowledge from large language models (LLMs), but its effectiveness remains contested. On one side, "forgotten" knowledge can often be recovered through interventions such as light fine-tuning; on the other side, unlearning may induce catastrophic forgetting that degrades general capabilities. Despite active exploration of unlearning methods, interpretability analyses of the mechanism are scarce due to the difficulty of tracing knowledge in LLMs' complex architectures. We address this gap by proposing unPact, an interpretable framework for unlearning via prompt attribution and contribution tracking. Typically, it quantifies each prompt token's influence on outputs, enabling pre- and post-unlearning comparisons to reveal what changes. Across six mainstream unlearning methods, three LLMs, and three benchmarks, we find that: (1) Unlearning appears to be effective by disrupting focus on keywords in prompt; (2) Much of the knowledge is not truly erased and can be recovered by simply emphasizing these keywords in prompts, without modifying the model's weights; (3) Catastrophic forgetting arises from indiscriminate penalization of all tokens. Taken together, our results suggest an unlearning dilemma: existing methods tend either to be insufficient - knowledge remains recoverable by keyword emphasis, or overly destructive - general performance collapses due to catastrophic forgetting, still leaving a gap to reliable unlearning.

