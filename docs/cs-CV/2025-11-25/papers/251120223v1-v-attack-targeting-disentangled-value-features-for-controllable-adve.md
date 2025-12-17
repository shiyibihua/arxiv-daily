---
layout: default
title: V-Attack: Targeting Disentangled Value Features for Controllable Adversarial Attacks on LVLMs
---

# V-Attack: Targeting Disentangled Value Features for Controllable Adversarial Attacks on LVLMs

<div class="paper-toolbar">
  <div class="toolbar-left">
    <a href="https://arxiv.org/abs/2511.20223" target="_blank" class="toolbar-btn">arXiv: 2511.20223v1</a>
    <a href="https://arxiv.org/pdf/2511.20223.pdf" target="_blank" class="toolbar-btn">PDF</a>
  </div>
  <div class="toolbar-right">
    <button class="toolbar-btn favorite-btn" data-arxiv-id="2511.20223v1" 
            onclick="toggleFavorite(this, '2511.20223v1', 'V-Attack: Targeting Disentangled Value Features for Controllable Adversarial Attacks on LVLMs')" title="收藏">
      ☆ 收藏
    </button>
    <button class="toolbar-btn share-btn" onclick="copyLink()" title="复制链接">
      🔗 分享
    </button>
  </div>
</div>


**作者**: Sen Nie, Jie Zhang, Jianxin Yan, Shiguang Shan, Xilin Chen

**分类**: cs.CV

**发布日期**: 2025-11-25

**备注**: 21 pages

**🔗 代码/项目**: [GITHUB](https://github.com/Summu77/V-Attack)

---

## 💡 一句话要点

**V-Attack通过操控解耦的Value特征，实现对LVLM的可控对抗攻击。**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)**

**关键词**: `对抗攻击` `大型视觉语言模型` `语义操纵` `Value特征` `可控攻击`

## 📋 核心要点

1. 现有对抗攻击方法难以精确控制LVLM中特定概念的语义操纵，主要原因是patch-token表示中的语义纠缠。
2. V-Attack通过操控Transformer注意力模块中的Value特征，抑制全局上下文干扰，实现对局部语义信息的精确控制。
3. 实验表明，V-Attack在多种LVLM上显著提升了攻击成功率，平均提升36%，揭示了LVLM的潜在安全风险。

## 📝 摘要（中文）

对抗攻击已从扰乱特定任务模型的预测演变为操纵大型视觉语言模型(LVLM)中的图像语义。然而，现有方法在可控性方面存在困难，无法精确地操纵图像中特定概念的语义。这种局限性归因于对抗攻击通常作用的patch-token表示中的语义纠缠：视觉编码器中自注意力机制聚合的全局上下文主导了单个patch特征，使其成为精确局部语义操纵的不可靠句柄。我们的系统研究揭示了一个关键见解：Transformer注意力模块中计算的value特征(V)是更精确的操纵句柄。我们证明V抑制了全局上下文通道，使其能够保留高熵、解耦的局部语义信息。基于此，我们提出了一种用于精确局部语义攻击的新方法V-Attack。V-Attack以value特征为目标，并引入两个核心组件：(1)自Value增强模块，用于提炼V的内在语义丰富性；(2)文本引导的Value操纵模块，利用文本提示来定位源概念并将其优化为目标概念。通过绕过纠缠的patch特征，V-Attack实现了高效的语义控制。在包括LLaVA、InternVL、DeepseekVL和GPT-4o在内的各种LVLM上的大量实验表明，V-Attack的攻击成功率比最先进的方法平均提高了36%，暴露了现代视觉语言理解中的关键漏洞。我们的代码和数据可在https://github.com/Summu77/V-Attack获取。

## 🔬 方法详解

**问题定义**：现有针对大型视觉语言模型（LVLM）的对抗攻击方法，难以实现对图像中特定概念语义的精确控制。现有方法通常直接攻击patch-token表示，但由于自注意力机制引入的全局上下文信息，导致patch特征语义纠缠，难以进行局部语义操纵。

**核心思路**：论文的核心思路是利用Transformer注意力模块中的Value特征（V）作为攻击目标。Value特征相比于patch特征，能够更好地抑制全局上下文信息，保留更纯粹、解耦的局部语义信息。通过精确操纵Value特征，可以实现对图像语义的精细控制。

**技术框架**：V-Attack的整体框架包含两个主要模块：自Value增强模块和文本引导的Value操纵模块。首先，自Value增强模块用于提升Value特征的语义丰富性。然后，文本引导的Value操纵模块利用文本提示定位源概念，并将其优化为目标概念。整个过程绕过了语义纠缠的patch特征，直接作用于Value特征。

**关键创新**：V-Attack的关键创新在于发现了Value特征在LVLM中具有解耦的局部语义信息，并将其作为对抗攻击的有效目标。与直接攻击patch特征的方法相比，V-Attack能够更精确地控制图像语义，实现更有效的对抗攻击。

**关键设计**：自Value增强模块的具体实现细节未知，但其目标是增强Value特征的语义表达能力。文本引导的Value操纵模块利用文本提示来指导Value特征的优化方向，损失函数的设计需要保证优化后的Value特征能够使LVLM将源概念识别为目标概念。具体的损失函数形式和优化算法细节未知。

## 📊 实验亮点

V-Attack在包括LLaVA、InternVL、DeepseekVL和GPT-4o在内的多种LVLM上进行了广泛的实验，结果表明V-Attack的攻击成功率比现有最先进的方法平均提高了36%。这一显著的提升表明V-Attack能够更有效地攻击LVLM，揭示了其在视觉语义理解方面的脆弱性。

## 🎯 应用场景

V-Attack的研究成果可应用于评估和提升LVLM的鲁棒性和安全性。通过对抗攻击，可以发现LVLM在视觉语义理解方面的潜在漏洞，并有针对性地进行防御。此外，该技术还可以用于生成对抗样本，用于训练更鲁棒的LVLM模型，提高其在真实世界应用中的可靠性。

## 📄 摘要（原文）

> Adversarial attacks have evolved from simply disrupting predictions on conventional task-specific models to the more complex goal of manipulating image semantics on Large Vision-Language Models (LVLMs). However, existing methods struggle with controllability and fail to precisely manipulate the semantics of specific concepts in the image. We attribute this limitation to semantic entanglement in the patch-token representations on which adversarial attacks typically operate: global context aggregated by self-attention in the vision encoder dominates individual patch features, making them unreliable handles for precise local semantic manipulation. Our systematic investigation reveals a key insight: value features (V) computed within the transformer attention block serve as much more precise handles for manipulation. We show that V suppresses global-context channels, allowing it to retain high-entropy, disentangled local semantic information. Building on this discovery, we propose V-Attack, a novel method designed for precise local semantic attacks. V-Attack targets the value features and introduces two core components: (1) a Self-Value Enhancement module to refine V's intrinsic semantic richness, and (2) a Text-Guided Value Manipulation module that leverages text prompts to locate source concept and optimize it toward a target concept. By bypassing the entangled patch features, V-Attack achieves highly effective semantic control. Extensive experiments across diverse LVLMs, including LLaVA, InternVL, DeepseekVL and GPT-4o, show that V-Attack improves the attack success rate by an average of 36% over state-of-the-art methods, exposing critical vulnerabilities in modern visual-language understanding. Our code and data are available https://github.com/Summu77/V-Attack.

