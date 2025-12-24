---
layout: default
title: Mitigating Jailbreaks with Intent-Aware LLMs
---

# Mitigating Jailbreaks with Intent-Aware LLMs

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.12072" class="toolbar-btn" target="_blank">📄 arXiv: 2508.12072v2</a>
  <a href="https://arxiv.org/pdf/2508.12072.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.12072v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.12072v2', 'Mitigating Jailbreaks with Intent-Aware LLMs')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Wei Jie Yeo, Ranjan Satapathy, Erik Cambria

**分类**: cs.CR, cs.CL

**发布日期**: 2025-08-16 (更新: 2025-08-23)

**🔗 代码/项目**: [GITHUB](https://github.com/wj210/Intent_Jailbreak)

---

## 💡 一句话要点

**提出Intent-FT以解决大语言模型的越狱攻击问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大语言模型` `越狱攻击` `意图推断` `模型微调` `鲁棒性增强`

## 📋 核心要点

1. 现有大语言模型在安全性方面仍然脆弱，容易受到越狱攻击，导致安全性与性能之间的矛盾。
2. 本文提出的Intent-FT方法通过微调模型，使其能够在响应指令前推断潜在意图，从而增强模型的鲁棒性。
3. 实验结果显示，Intent-FT在所有评估的攻击类别中均有效降低了攻击成功率，且模型的通用能力得以保留。

## 📝 摘要（中文）

尽管经过广泛的安全调优，大语言模型（LLMs）仍然容易受到通过对抗性指令构造的越狱攻击，反映出安全性与任务性能之间的持续权衡。本文提出了一种简单且轻量的微调方法Intent-FT，明确训练LLMs在响应之前推断指令的潜在意图。通过在针对性的对抗性指令集上进行微调，Intent-FT使LLMs能够将意图推断推广到未见的攻击，从而显著提高其鲁棒性。我们全面评估了开放源代码和专有模型下的参数性和非参数性攻击，考虑了攻击的有害性、效用、过度拒绝和对白盒威胁的影响。实验证明，Intent-FT始终有效缓解所有评估的攻击类别，没有单一攻击的成功率超过50%，而现有防御方法仅部分有效。重要的是，我们的方法保留了模型的通用能力，并减少了对包含表面有害关键词的良性指令的过度拒绝。

## 🔬 方法详解

**问题定义**：本文旨在解决大语言模型在面对对抗性指令时的越狱攻击问题。现有方法在防御这些攻击时效果有限，无法有效降低攻击成功率。

**核心思路**：论文提出的Intent-FT方法通过微调模型，使其在响应指令之前能够推断出指令的潜在意图。这种设计可以帮助模型更好地理解指令，从而提高其对越狱攻击的抵抗力。

**技术框架**：整体架构包括数据准备、模型微调和评估三个主要阶段。在数据准备阶段，收集针对性的对抗性指令；在微调阶段，使用这些指令对模型进行训练；最后在评估阶段，测试模型在不同攻击下的表现。

**关键创新**：最重要的技术创新在于通过意图推断来增强模型的鲁棒性，与现有方法相比，Intent-FT能够有效降低攻击成功率，并且在未见攻击上也表现出良好的泛化能力。

**关键设计**：在微调过程中，采用了特定的损失函数来优化意图推断的准确性，同时保持模型的通用能力。此外，模型的参数设置经过精心调整，以确保在不同类型的攻击下均能保持良好的性能。

## 📊 实验亮点

实验结果表明，使用Intent-FT微调后的模型在所有评估的攻击类别中均未出现单一攻击成功率超过50%的情况，相较于现有防御方法，表现出显著的提升。具体而言，模型在面对不同类型的攻击时，鲁棒性得到了全面增强，且对良性指令的拒绝率显著降低。

## 🎯 应用场景

该研究的潜在应用领域包括安全性要求高的对话系统、自动问答系统以及任何依赖大语言模型的应用场景。通过增强模型对越狱攻击的抵抗力，可以提升用户的信任度和系统的安全性，未来可能在商业和社会应用中产生深远影响。

## 📄 摘要（原文）

> Despite extensive safety-tuning, large language models (LLMs) remain vulnerable to jailbreak attacks via adversarially crafted instructions, reflecting a persistent trade-off between safety and task performance. In this work, we propose Intent-FT, a simple and lightweight fine-tuning approach that explicitly trains LLMs to infer the underlying intent of an instruction before responding. By fine-tuning on a targeted set of adversarial instructions, Intent-FT enables LLMs to generalize intent deduction to unseen attacks, thereby substantially improving their robustness. We comprehensively evaluate both parametric and non-parametric attacks across open-source and proprietary models, considering harmfulness from attacks, utility, over-refusal, and impact against white-box threats. Empirically, Intent-FT consistently mitigates all evaluated attack categories, with no single attack exceeding a 50\% success rate -- whereas existing defenses remain only partially effective. Importantly, our method preserves the model's general capabilities and reduces excessive refusals on benign instructions containing superficially harmful keywords. Furthermore, models trained with Intent-FT accurately identify hidden harmful intent in adversarial attacks, and these learned intentions can be effectively transferred to enhance vanilla model defenses. We publicly release our code at https://github.com/wj210/Intent_Jailbreak.

