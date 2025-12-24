---
layout: default
title: Adversarial Attacks and Defenses on Graph-aware Large Language Models (LLMs)
---

# Adversarial Attacks and Defenses on Graph-aware Large Language Models (LLMs)

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.04894" class="toolbar-btn" target="_blank">📄 arXiv: 2508.04894v1</a>
  <a href="https://arxiv.org/pdf/2508.04894.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.04894v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.04894v1', 'Adversarial Attacks and Defenses on Graph-aware Large Language Models (LLMs)')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Iyiola E. Olatunji, Franziska Boenisch, Jing Xu, Adam Dziedzic

**分类**: cs.CR, cs.AI, cs.SI

**发布日期**: 2025-08-06

---

## 💡 一句话要点

**提出针对图感知大语言模型的对抗攻击与防御方法**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `对抗攻击` `大语言模型` `图神经网络` `鲁棒性` `防御框架` `节点分类` `特征修正`

## 📋 核心要点

1. 现有的图感知大语言模型在面对对抗攻击时的脆弱性尚未被充分研究，尤其是在节点分类任务中。
2. 本文提出了一种新的防御框架GALGUARD，结合了特征修正和GNN防御策略，以增强模型的鲁棒性。
3. 实验结果表明，LLAGA在节点序列模板下更易受到攻击，而GRAPHPROMPTER则展现出更高的抗攻击能力。

## 📝 摘要（中文）

随着大语言模型（LLMs）与图结构数据的结合日益增多，尤其在节点分类等任务中，LLMs的鲁棒性对抗攻击的研究尚未深入。本文首次探讨了图感知LLMs的脆弱性，利用现有针对图模型的对抗攻击方法，包括训练时的中毒攻击和测试时的规避攻击，分析了LLAGA和GRAPHPROMPTER两种代表性模型。研究发现，LLAGA的节点序列模板增加了其脆弱性，而GRAPHPROMPTER的GNN编码器表现出更强的鲁棒性。最后，提出了一个名为GALGUARD的端到端防御框架，结合了LLM特征修正模块和适应性GNN防御，以抵御结构性攻击。

## 🔬 方法详解

**问题定义**：本文旨在解决图感知大语言模型在对抗攻击下的脆弱性问题，现有方法未能有效应对训练时和测试时的攻击。

**核心思路**：通过利用现有的对抗攻击方法，分析图感知LLMs的脆弱性，并提出GALGUARD防御框架，以增强其鲁棒性。

**技术框架**：研究首先对LLAGA和GRAPHPROMPTER进行系统分析，识别其在对抗攻击下的弱点，然后设计GALGUARD框架，结合特征修正和GNN防御模块。

**关键创新**：本文的主要创新在于首次系统性地分析了图感知LLMs的对抗攻击脆弱性，并提出了针对性的防御策略，显著提升了模型的抗攻击能力。

**关键设计**：在GALGUARD中，特征修正模块用于减轻特征级别的扰动，而GNN防御模块则针对结构性攻击进行保护，确保整体防御效果的提升。

## 📊 实验亮点

实验结果显示，LLAGA在节点序列模板下的攻击成功率显著提高，而GRAPHPROMPTER则展现出更强的抗攻击能力。GALGUARD框架有效降低了对抗攻击的影响，提升了模型的整体鲁棒性，展示了防御策略的有效性。

## 🎯 应用场景

该研究在图感知大语言模型的安全性和鲁棒性方面具有重要的应用价值，尤其适用于金融、社交网络分析和生物信息学等领域，能够有效防止潜在的对抗攻击，提升模型在实际应用中的可靠性。

## 📄 摘要（原文）

> Large Language Models (LLMs) are increasingly integrated with graph-structured data for tasks like node classification, a domain traditionally dominated by Graph Neural Networks (GNNs). While this integration leverages rich relational information to improve task performance, their robustness against adversarial attacks remains unexplored. We take the first step to explore the vulnerabilities of graph-aware LLMs by leveraging existing adversarial attack methods tailored for graph-based models, including those for poisoning (training-time attacks) and evasion (test-time attacks), on two representative models, LLAGA (Chen et al. 2024) and GRAPHPROMPTER (Liu et al. 2024). Additionally, we discover a new attack surface for LLAGA where an attacker can inject malicious nodes as placeholders into the node sequence template to severely degrade its performance. Our systematic analysis reveals that certain design choices in graph encoding can enhance attack success, with specific findings that: (1) the node sequence template in LLAGA increases its vulnerability; (2) the GNN encoder used in GRAPHPROMPTER demonstrates greater robustness; and (3) both approaches remain susceptible to imperceptible feature perturbation attacks. Finally, we propose an end-to-end defense framework GALGUARD, that combines an LLM-based feature correction module to mitigate feature-level perturbations and adapted GNN defenses to protect against structural attacks.

