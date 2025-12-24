---
layout: default
title: The Computational Complexity of Satisfiability in State Space Models
---

# The Computational Complexity of Satisfiability in State Space Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.18162" class="toolbar-btn" target="_blank">📄 arXiv: 2508.18162v1</a>
  <a href="https://arxiv.org/pdf/2508.18162.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.18162v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.18162v1', 'The Computational Complexity of Satisfiability in State Space Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Eric Alsmann, Martin Lange

**分类**: cs.LO, cs.AI, cs.CC, cs.LG

**发布日期**: 2025-08-25

**备注**: Accepted at ECAI 25

---

## 💡 一句话要点

**分析状态空间模型中可满足性问题的计算复杂性**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `状态空间模型` `可满足性问题` `计算复杂性` `形式推理` `模型验证` `量化SSM`

## 📋 核心要点

1. 核心问题：状态空间模型中的可满足性问题在一般情况下是不可判定的，给理论推理带来挑战。
2. 方法要点：通过识别特定限制条件，论文使得可满足性问题在某些情况下变为可判定，并给出了复杂性界限。
3. 实验或效果：研究结果表明，在特定条件下，ssmSAT的复杂性可归类为NP完全或PSPACE完全，提供了理论基础。

## 📝 摘要（中文）

本文分析了状态空间模型（SSM）中可满足性问题ssmSAT的复杂性，该问题询问输入序列是否能使模型达到接受配置。研究发现，ssmSAT在一般情况下是不可判定的，反映了SSM的计算能力。基于实际应用，本文识别了两个自然限制条件，使得ssmSAT变为可判定，并建立了相应的复杂性界限。首先，对于具有有限上下文长度的SSM，当输入长度以单一进制给出时，ssmSAT是NP完全的；而当输入长度以二进制给出时，ssmSAT则是NEXPTIME（且PSPACE-硬）。其次，对于在固定宽度算术下运行的量化SSM，ssmSAT在不同位宽编码下分别是PSPACE完全或EXPSPACE。本文的结果为SSM的形式推理建立了首个复杂性景观，并突出了SSM基础语言模型验证的基本限制与机遇。

## 🔬 方法详解

**问题定义**：本文旨在解决状态空间模型（SSM）中的可满足性问题ssmSAT的复杂性，现有方法在一般情况下无法判定该问题的可满足性，限制了其应用。

**核心思路**：论文通过识别具有有限上下文长度和量化SSM的特定条件，使得ssmSAT在这些条件下变为可判定，进而分析其复杂性。

**技术框架**：研究首先定义了ssmSAT问题，然后在不同的上下文长度和位宽条件下，分析其复杂性，最后给出相应的复杂性界限。

**关键创新**：本文的主要创新在于首次为SSM的可满足性问题建立了复杂性景观，明确了在特定条件下的可判定性和复杂性分类。

**关键设计**：研究中对上下文长度的限制和量化SSM的位宽进行了详细分析，提出了在不同输入长度表示下的复杂性界限，确保了理论分析的严谨性。

## 📊 实验亮点

研究结果显示，在有限上下文长度的情况下，ssmSAT在输入长度为单一进制时为NP完全，而在二进制时为NEXPTIME，且在量化SSM中，复杂性可达到PSPACE完全或EXPSPACE。这些结果为SSM的形式推理提供了重要的理论支持。

## 🎯 应用场景

该研究的潜在应用领域包括自然语言处理、自动化推理和模型验证等。通过明确状态空间模型的可满足性问题的复杂性，研究为开发更高效的验证工具提供了理论基础，推动了基于SSM的语言模型的实际应用与发展。

## 📄 摘要（原文）

> We analyse the complexity of the satisfiability problem ssmSAT for State Space Models (SSM), which asks whether an input sequence can lead the model to an accepting configuration. We find that ssmSAT is undecidable in general, reflecting the computational power of SSM. Motivated by practical settings, we identify two natural restrictions under which ssmSAT becomes decidable and establish corresponding complexity bounds. First, for SSM with bounded context length, ssmSAT is NP-complete when the input length is given in unary and in NEXPTIME (and PSPACE-hard) when the input length is given in binary. Second, for quantised SSM operating over fixed-width arithmetic, ssmSAT is PSPACE-complete resp. in EXPSPACE depending on the bit-width encoding. While these results hold for diagonal gated SSM we also establish complexity bounds for time-invariant SSM. Our results establish a first complexity landscape for formal reasoning in SSM and highlight fundamental limits and opportunities for the verification of SSM-based language models.

