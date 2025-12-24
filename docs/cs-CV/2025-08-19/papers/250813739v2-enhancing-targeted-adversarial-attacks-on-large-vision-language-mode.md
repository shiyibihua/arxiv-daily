---
layout: default
title: Enhancing Targeted Adversarial Attacks on Large Vision-Language Models via Intermediate Projector
---

# Enhancing Targeted Adversarial Attacks on Large Vision-Language Models via Intermediate Projector

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.13739" class="toolbar-btn" target="_blank">📄 arXiv: 2508.13739v2</a>
  <a href="https://arxiv.org/pdf/2508.13739.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.13739v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.13739v2', 'Enhancing Targeted Adversarial Attacks on Large Vision-Language Models via Intermediate Projector')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yiming Cao, Yanjie Li, Kaisheng Liang, Bin Xiao

**分类**: cs.CV

**发布日期**: 2025-08-19 (更新: 2025-09-24)

---

## 💡 一句话要点

**提出中间投影器以增强针对大型视觉-语言模型的对抗攻击**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `对抗攻击` `视觉-语言模型` `细粒度攻击` `查询变换器` `模型安全性` `多模态对齐` `黑箱攻击`

## 📋 核心要点

1. 现有方法主要集中于全局相似性，难以实现细粒度的隐蔽攻击，无法有效针对特定目标进行修改。
2. 本文提出了中间投影器引导攻击（IPGA）框架，利用查询变换器增强攻击的细粒度和有效性，同时提高攻击的可转移性。
3. 实验结果显示，IPGA在全局针对性攻击中显著优于基线方法，而结合残差查询对齐模块的IPGA-R在细粒度攻击中表现更佳。

## 📝 摘要（中文）

随着大型视觉-语言模型（VLMs）的广泛应用，安全性问题日益凸显，尤其是针对黑箱模型的有针对性对抗攻击。现有方法主要关注编码器级别的全局相似性，缺乏细粒度的攻击能力。为了解决这些问题，本文提出了一种新的黑箱针对性攻击框架，利用了投影器的优势，特别是通过查询变换器（Q-Former）将全局图像嵌入转化为细粒度查询输出，从而增强攻击的有效性和细粒度。实验结果表明，所提出的方法在全局针对性攻击和细粒度攻击中均显著优于基线方法。

## 🔬 方法详解

**问题定义**：本文旨在解决现有针对大型视觉-语言模型的对抗攻击方法在细粒度攻击中的不足，现有方法往往无法有效针对特定目标进行修改，且缺乏对投影器的利用。

**核心思路**：提出中间投影器引导攻击（IPGA）框架，通过查询变换器将全局图像嵌入转化为细粒度查询输出，从而增强攻击的有效性和细粒度。

**技术框架**：整体架构包括两个主要模块：首先是Q-Former模块，将全局图像嵌入转化为细粒度查询输出；其次是残差查询对齐模块（RQA），用于在细粒度攻击中保持与目标无关的内容。

**关键创新**：最重要的技术创新在于利用投影器作为语义桥梁，增强了攻击的细粒度和有效性，尤其是在针对特定目标的修改上，与现有方法相比具有本质区别。

**关键设计**：在设计中，采用了未针对特定大型语言模型（LLM）进行微调的预训练Q-Former，以提高攻击的可转移性，同时在RQA模块中引入约束，以保持与目标无关的查询输出。

## 📊 实验亮点

实验结果表明，IPGA在全局针对性攻击中显著优于基线方法，成功率提升幅度达到XX%。结合RQA模块的IPGA-R在细粒度攻击中表现更佳，成功率和与目标无关内容的保留率均显著高于基线方法，展示了良好的转移能力。

## 🎯 应用场景

该研究的潜在应用领域包括安全性测试、模型鲁棒性评估以及对抗样本生成等。通过增强对抗攻击的有效性和细粒度，能够更好地评估大型视觉-语言模型在实际应用中的安全性，进而推动相关领域的研究与发展。

## 📄 摘要（原文）

> The growing deployment of Large Vision-Language Models (VLMs) raises safety concerns, as adversaries may exploit model vulnerabilities to induce harmful outputs, with targeted black-box adversarial attacks posing a particularly severe threat. However, existing methods primarily maximize encoder-level global similarity, which lacks the granularity for stealthy and practical fine-grained attacks, where only specific target should be altered (e.g., modifying a car while preserving its background). Moreover, they largely neglect the projector, a key semantic bridge in VLMs for multimodal alignment. To address these limitations, we propose a novel black-box targeted attack framework that leverages the projector. Specifically, we utilize the widely adopted Querying Transformer (Q-Former) which transforms global image embeddings into fine-grained query outputs, to enhance attack effectiveness and granularity. For standard global targeted attack scenarios, we propose the Intermediate Projector Guided Attack (IPGA), which aligns Q-Former fine-grained query outputs with the target to enhance attack strength and exploits the intermediate pretrained Q-Former that is not fine-tuned for any specific Large Language Model (LLM) to improve attack transferability. For fine-grained attack scenarios, we augment IPGA with the Residual Query Alignment (RQA) module, which preserves unrelated content by constraining non-target query outputs to enhance attack granularity. Extensive experiments demonstrate that IPGA significantly outperforms baselines in global targeted attacks, and IPGA with RQA (IPGA-R) attains superior success rates and unrelated content preservation over baselines in fine-grained attacks. Our method also transfers effectively to commercial VLMs such as Google Gemini and OpenAI GPT.

