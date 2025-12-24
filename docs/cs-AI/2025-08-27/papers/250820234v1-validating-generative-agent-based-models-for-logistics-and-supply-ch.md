---
layout: default
title: Validating Generative Agent-Based Models for Logistics and Supply Chain Management Research
---

# Validating Generative Agent-Based Models for Logistics and Supply Chain Management Research

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.20234" class="toolbar-btn" target="_blank">📄 arXiv: 2508.20234v1</a>
  <a href="https://arxiv.org/pdf/2508.20234.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.20234v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.20234v1', 'Validating Generative Agent-Based Models for Logistics and Supply Chain Management Research')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Vincent E. Castillo

**分类**: cs.MA, cs.AI, cs.CY

**发布日期**: 2025-08-27

**备注**: A version of this work is also available on SSRN (https://ssrn.com/abstract=5407742 or http://dx.doi.org/10.2139/ssrn.5407742). This preprint is distributed under the CC BY-NC-SA 4.0 License

---

## 💡 一句话要点

**验证生成代理基础模型以提升物流与供应链管理研究的有效性**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `生成代理基础模型` `大型语言模型` `物流管理` `供应链管理` `人类行为模拟` `决策过程验证` `实验设计` `结构方程模型`

## 📋 核心要点

1. 现有的代理基础模型在模拟人类行为时缺乏真实感，难以反映复杂的决策过程。
2. 本研究提出通过生成代理基础模型结合大型语言模型，进行人类行为的模拟与验证。
3. 实验结果显示，GABMs能够有效模拟人类行为，但在决策过程上存在显著差异，需进行双重验证。

## 📝 摘要（中文）

生成代理基础模型（GABMs）结合大型语言模型（LLMs）为物流与供应链管理（LSCM）研究提供了新的实证潜力，能够真实模拟复杂的人类行为。与传统的代理基础模型不同，GABMs通过自然语言推理生成类人响应，从而为LSCM现象的涌现提供了新的视角。然而，LLMs作为人类行为的代理在LSCM模拟中的有效性尚不明确。本研究通过控制实验评估LLM与人类行为的等效性，考察了食品配送场景中的客户与工作人员的双边互动。研究结果表明，GABMs能够有效模拟LSCM中的人类行为，但出现了等效性与过程的悖论。尽管某些LLMs在表面上与人类表现出等效性，但结构方程模型（SEM）显示某些LLMs的决策过程与人类参与者存在差异。这些发现表明，GABMs在经过适当验证后，可能成为LSCM研究的有效方法工具。

## 🔬 方法详解

**问题定义**：本研究旨在解决生成代理基础模型（GABMs）在物流与供应链管理（LSCM）研究中作为人类行为代理的有效性问题。现有的代理基础模型无法真实反映人类复杂的决策过程，导致模拟结果的可靠性不足。

**核心思路**：本研究的核心思路是通过对比实验评估大型语言模型（LLMs）与人类行为的等效性，探索GABMs在LSCM中的应用潜力。通过设计控制实验，考察客户与工作人员在食品配送场景中的互动，验证GABMs的有效性。

**技术框架**：整体研究框架包括两个主要模块：首先是人类等效性测试，通过与957名人类参与者的对比，评估LLMs的表现；其次是决策过程验证，使用结构方程模型（SEM）分析LLMs的决策过程与人类的差异。

**关键创新**：本研究的关键创新在于提出了双重验证框架，既考察了LLMs在表面行为上的等效性，又深入分析了其决策过程的结构性差异。这一方法与传统的单一等效性测试形成鲜明对比。

**关键设计**：实验设计中采用了调节中介设计，确保了对比的有效性。使用了两侧单一检验（TOST）方法进行等效性检验，并结合结构方程模型（SEM）分析决策过程，确保了结果的科学性与可靠性。

## 📊 实验亮点

实验结果表明，某些大型语言模型在表面行为上与人类表现出等效性，但在决策过程上存在显著差异。具体而言，部分LLMs的决策过程与人类参与者的真实决策过程不符，提示需要进行更深入的验证。

## 🎯 应用场景

该研究的潜在应用领域包括物流与供应链管理的决策支持系统、智能配送系统以及人机交互界面设计。通过验证GABMs的有效性，研究为相关领域提供了新的方法论支持，未来可能推动更智能化的供应链管理实践。

## 📄 摘要（原文）

> Generative Agent-Based Models (GABMs) powered by large language models (LLMs) offer promising potential for empirical logistics and supply chain management (LSCM) research by enabling realistic simulation of complex human behaviors. Unlike traditional agent-based models, GABMs generate human-like responses through natural language reasoning, which creates potential for new perspectives on emergent LSCM phenomena. However, the validity of LLMs as proxies for human behavior in LSCM simulations is unknown. This study evaluates LLM equivalence of human behavior through a controlled experiment examining dyadic customer-worker engagements in food delivery scenarios. I test six state-of-the-art LLMs against 957 human participants (477 dyads) using a moderated mediation design. This study reveals a need to validate GABMs on two levels: (1) human equivalence testing, and (2) decision process validation. Results reveal GABMs can effectively simulate human behaviors in LSCM; however, an equivalence-versus-process paradox emerges. While a series of Two One-Sided Tests (TOST) for equivalence reveals some LLMs demonstrate surface-level equivalence to humans, structural equation modeling (SEM) reveals artificial decision processes not present in human participants for some LLMs. These findings show GABMs as a potentially viable methodological instrument in LSCM with proper validation checks. The dual-validation framework also provides LSCM researchers with a guide to rigorous GABM development. For practitioners, this study offers evidence-based assessment for LLM selection for operational tasks.

