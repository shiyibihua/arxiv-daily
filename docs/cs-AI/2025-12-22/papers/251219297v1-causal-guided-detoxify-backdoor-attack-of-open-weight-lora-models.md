---
layout: default
title: Causal-Guided Detoxify Backdoor Attack of Open-Weight LoRA Models
---

# Causal-Guided Detoxify Backdoor Attack of Open-Weight LoRA Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.19297" class="toolbar-btn" target="_blank">📄 arXiv: 2512.19297v1</a>
  <a href="https://arxiv.org/pdf/2512.19297.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.19297v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.19297v1', 'Causal-Guided Detoxify Backdoor Attack of Open-Weight LoRA Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Linzhi Chen, Yang Sun, Hongru Wei, Yuqi Chen

**分类**: cs.CR, cs.AI

**发布日期**: 2025-12-22

**备注**: NDSS 2026

---

## 💡 一句话要点

**提出CBA：一种因果引导的LoRA模型解毒后门攻击方法**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `后门攻击` `LoRA模型` `因果引导` `解毒策略` `大型语言模型` `安全漏洞` `对抗防御`

## 📋 核心要点

1. 现有LoRA后门攻击方法依赖不可访问的训练数据，忽略LoRA结构特性，且误触发率高，隐蔽性差。
2. CBA通过覆盖引导的数据生成和因果引导的解毒策略，在无需原始数据的情况下实现高隐蔽性后门攻击。
3. 实验表明，CBA在保持高攻击成功率的同时，显著降低了误触发率，并增强了对现有防御的抵抗力。

## 📝 摘要（中文）

低秩适应(LoRA)已成为微调大型语言模型(LLM)的有效方法，并在开源社区中得到广泛应用。然而，通过Hugging Face等平台分散传播LoRA适配器引入了新的安全漏洞：恶意适配器可以很容易地传播并逃避传统的监督机制。尽管存在这些风险，但针对基于LoRA的微调的后门攻击仍然相对未被探索。现有的后门攻击策略不适合这种设置，因为它们通常依赖于无法访问的训练数据，未能考虑到LoRA特有的结构属性，或者遭受高误触发率(FTR)，从而损害了它们的隐蔽性。为了解决这些挑战，我们提出了一种因果引导的解毒后门攻击(CBA)，这是一种专门为开放权重LoRA模型设计的新的后门攻击框架。CBA在无需访问原始训练数据的情况下运行，并通过两个关键创新实现高隐蔽性：(1)一个覆盖引导的数据生成管道，通过行为探索合成任务对齐的输入，以及(2)一个因果引导的解毒策略，通过保留任务关键神经元来合并中毒和干净的适配器。与先前的方法不同，CBA通过基于因果影响的权重分配，实现了对攻击强度的训练后控制，从而消除了重复训练的需要。在六个LoRA模型上进行评估，CBA实现了高攻击成功率，同时与基线方法相比，降低了50-70%的FTR。此外，它还展示了对最先进的后门防御的增强抵抗力，突出了其隐蔽性和鲁棒性。

## 🔬 方法详解

**问题定义**：现有针对LoRA模型的后门攻击方法存在诸多问题。首先，许多方法需要访问原始训练数据，这在实际场景中通常是不可行的。其次，这些方法未能充分利用LoRA的结构特性，导致攻击效果不佳。此外，现有方法的误触发率（FTR）较高，容易被检测到，从而降低了攻击的隐蔽性。因此，需要一种能够在无需访问原始数据的情况下，利用LoRA结构特性，并具有低误触发率的后门攻击方法。

**核心思路**：CBA的核心思路是通过行为探索生成任务对齐的输入，并利用因果关系指导中毒和干净适配器的合并，从而实现高隐蔽性和可控的后门攻击。具体来说，CBA首先通过覆盖引导的数据生成管道，合成能够触发目标行为的输入。然后，利用因果引导的解毒策略，选择性地保留任务关键神经元，将中毒适配器和干净适配器合并，从而在保持模型性能的同时，植入后门。

**技术框架**：CBA框架主要包含两个阶段：(1)覆盖引导的数据生成阶段：该阶段通过探索模型的行为空间，生成能够有效触发目标行为的输入数据。具体来说，该阶段使用一种基于覆盖率的策略，选择能够最大程度覆盖模型内部状态的输入，从而提高生成数据的有效性。(2)因果引导的解毒阶段：该阶段利用因果关系指导中毒适配器和干净适配器的合并。具体来说，该阶段首先识别对任务性能至关重要的神经元，然后选择性地保留这些神经元，从而在植入后门的同时，保持模型的性能。

**关键创新**：CBA的关键创新在于其因果引导的解毒策略。与现有方法不同，CBA不是简单地将中毒适配器和干净适配器合并，而是利用因果关系选择性地保留任务关键神经元。这种策略能够有效地降低误触发率，并提高攻击的隐蔽性。此外，CBA还实现了对攻击强度的训练后控制，无需重复训练即可调整攻击效果。

**关键设计**：在覆盖引导的数据生成阶段，CBA使用了一种基于神经元覆盖率的策略，选择能够最大程度覆盖模型内部神经元的输入。在因果引导的解毒阶段，CBA使用了一种基于因果影响的权重分配方法，根据神经元对任务性能的影响程度，分配不同的权重。此外，CBA还设计了一种损失函数，用于平衡攻击成功率和模型性能。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.19297v1/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.19297v1/x2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.19297v1/x3.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

CBA在六个LoRA模型上进行了评估，实验结果表明，CBA能够实现高攻击成功率，同时将误触发率(FTR)降低50-70%，显著优于基线方法。此外，CBA还展示了对最先进的后门防御的增强抵抗力，证明了其隐蔽性和鲁棒性。这些结果表明，CBA是一种有效的LoRA模型后门攻击方法。

## 🎯 应用场景

CBA的研究成果可应用于评估和增强LoRA模型的安全性，尤其是在开源社区中广泛共享的LoRA适配器。该方法能够帮助开发者识别潜在的后门攻击风险，并开发更有效的防御机制。此外，CBA的思路也可以推广到其他类型的模型和攻击场景，为提升人工智能系统的整体安全性做出贡献。

## 📄 摘要（原文）

> Low-Rank Adaptation (LoRA) has emerged as an efficient method for fine-tuning large language models (LLMs) and is widely adopted within the open-source community. However, the decentralized dissemination of LoRA adapters through platforms such as Hugging Face introduces novel security vulnerabilities: malicious adapters can be easily distributed and evade conventional oversight mechanisms. Despite these risks, backdoor attacks targeting LoRA-based fine-tuning remain relatively underexplored. Existing backdoor attack strategies are ill-suited to this setting, as they often rely on inaccessible training data, fail to account for the structural properties unique to LoRA, or suffer from high false trigger rates (FTR), thereby compromising their stealth. To address these challenges, we propose Causal-Guided Detoxify Backdoor Attack (CBA), a novel backdoor attack framework specifically designed for open-weight LoRA models. CBA operates without access to original training data and achieves high stealth through two key innovations: (1) a coverage-guided data generation pipeline that synthesizes task-aligned inputs via behavioral exploration, and (2) a causal-guided detoxification strategy that merges poisoned and clean adapters by preserving task-critical neurons. Unlike prior approaches, CBA enables post-training control over attack intensity through causal influence-based weight allocation, eliminating the need for repeated retraining. Evaluated across six LoRA models, CBA achieves high attack success rates while reducing FTR by 50-70\% compared to baseline methods. Furthermore, it demonstrates enhanced resistance to state-of-the-art backdoor defenses, highlighting its stealth and robustness.

