---
layout: default
title: "The Dawn of Agentic EDA: A Survey of Autonomous Digital Chip Design"
---

# The Dawn of Agentic EDA: A Survey of Autonomous Digital Chip Design

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.23189" class="toolbar-btn" target="_blank">📄 arXiv: 2512.23189v1</a>
  <a href="https://arxiv.org/pdf/2512.23189.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.23189v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.23189v1', 'The Dawn of Agentic EDA: A Survey of Autonomous Digital Chip Design')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zelin Zang, Yuhang Song, Bingo Wing-Kuen Ling, Aili Wang, Fuji Yang

**分类**: eess.SY

**发布日期**: 2025-12-29

---

## 💡 一句话要点

**提出Agentic EDA框架，实现数字芯片设计的自主化，加速AI原生设计流程。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `Agentic EDA` `自主芯片设计` `AI原生设计` `生成式AI` `多模态基础模型` `RTL代码生成` `物理设计`

## 📋 核心要点

1. 传统EDA工具难以应对日益复杂的芯片设计需求，AI辅助设计虽有进展，但仍依赖人工干预，效率受限。
2. 论文提出Agentic EDA框架，利用生成式AI和Agentic AI，构建自主化的芯片设计流程，实现跨阶段的智能优化。
3. 通过案例研究验证了Agentic EDA框架的可行性，展示了其在微架构定义、RTL代码生成和物理设计等方面的潜力。

## 📝 摘要（中文）

本综述全面概述了生成式AI和Agentic AI在数字电子设计自动化（EDA）领域的集成。首先回顾了从传统计算机辅助设计（CAD）到AI辅助EDA（AI4EDA），再到新兴的AI原生和Agentic设计范式的演变。详细介绍了这些范式在数字芯片设计流程中的应用，包括基于多模态基础模型的Agentic认知架构的构建、前端RTL代码生成和智能验证，以及后端物理设计中的算法创新和工具编排。通过综合案例研究验证了这些方法，展示了从微架构定义到GDSII的实际可行性。特别强调了跨阶段反馈循环的潜力，其中Agent利用后端PPA指标自主优化前端逻辑。此外，本综述深入探讨了对安全性的双重影响，包括新型对抗风险、自动漏洞修复和隐私保护基础设施。最后，批判性地总结了当前与幻觉、数据稀缺和黑盒工具相关的挑战，并概述了未来L4自主芯片设计的发展趋势。最终，这项工作旨在定义Agentic EDA这一新兴领域，并为从AI辅助工具到完全自主的设计工程师的过渡提供战略路线图。

## 🔬 方法详解

**问题定义**：当前数字芯片设计面临日益增长的复杂性和上市时间压力。传统的EDA工具虽然提供了自动化功能，但仍然需要大量的人工干预和专家知识。AI辅助EDA（AI4EDA）在一定程度上提高了效率，但仍然依赖于预定义的算法和有限的优化策略。现有的方法难以实现跨阶段的自主优化和快速迭代，导致设计周期长、成本高。

**核心思路**：本论文的核心思路是引入Agentic AI，构建一个自主的芯片设计Agent，使其能够像人类工程师一样，理解设计目标、探索设计空间、并根据反馈进行优化。通过将芯片设计的各个阶段（如RTL代码生成、验证、物理设计）建模为Agent，并赋予其自主决策和学习能力，实现端到端的自动化设计流程。

**技术框架**：Agentic EDA框架包含以下主要模块：1) 基于多模态基础模型的认知架构，用于理解设计规范和目标；2) 前端RTL代码生成Agent，负责根据规范生成可验证的RTL代码；3) 智能验证Agent，用于自动检测和修复设计缺陷；4) 后端物理设计Agent，负责布局、布线和优化PPA指标。这些Agent通过跨阶段的反馈循环进行协作，例如，后端Agent将PPA指标反馈给前端Agent，用于优化RTL代码。

**关键创新**：本论文的关键创新在于将Agentic AI引入到数字芯片设计领域，提出了一个完整的Agentic EDA框架。与传统的AI4EDA方法相比，Agentic EDA具有更强的自主性和适应性，能够实现跨阶段的智能优化和快速迭代。此外，论文还强调了跨阶段反馈循环的重要性，通过将后端PPA指标反馈给前端Agent，实现了全局优化。

**关键设计**：在Agentic EDA框架中，关键的设计包括：1) 多模态基础模型的选择和训练，用于理解设计规范和目标；2) Agent之间的通信协议和协作机制，确保Agent能够有效地协同工作；3) 奖励函数的设计，用于指导Agent的学习和优化；4) 知识库的构建，用于存储和共享设计经验和知识。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.23189v1/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.23189v1/x2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.23189v1/x3.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

论文通过案例研究验证了Agentic EDA框架的可行性，展示了其在微架构定义、RTL代码生成和物理设计等方面的潜力。虽然具体的性能数据和提升幅度未在摘要中明确给出，但强调了从微架构定义到GDSII的实际可行性，以及通过后端PPA指标自主优化前端逻辑的能力，暗示了在设计效率和芯片性能上的显著提升。

## 🎯 应用场景

Agentic EDA框架可应用于各种数字芯片设计场景，包括CPU、GPU、AI芯片等。它能够显著缩短设计周期、降低设计成本，并提高芯片的性能和功耗。此外，Agentic EDA还有助于解决芯片设计人才短缺的问题，使非专业人士也能参与到芯片设计中来。未来，Agentic EDA有望成为芯片设计的主流范式，推动芯片产业的快速发展。

## 📄 摘要（原文）

> This survey provides a comprehensive overview of the integration of Generative AI and Agentic AI within the field of Digital Electronic Design Automation (EDA). The paper first reviews the paradigmatic evolution from traditional Computer-Aided Design (CAD) to AI-assisted EDA (AI4EDA), and finally to the emerging AI-Native and Agentic design paradigms. We detail the application of these paradigms across the digital chip design flow, including the construction of agentic cognitive architectures based on multimodal foundation models, frontend RTL code generation and intelligent verification, and backend physical design featuring algorithmic innovations and tool orchestration. We validate these methodologies through integrated case studies, demonstrating practical viability from microarchitecture definition to GDSII. Special emphasis is placed on the potential for cross-stage feedback loops where agents utilize backend PPA metrics to autonomously refine frontend logic. Furthermore, this survey delves into the dual-faceted impact on security, covering novel adversarial risks, automated vulnerability repair, and privacy-preserving infrastructure. Finally, the paper critically summarizes current challenges related to hallucinations, data scarcity, and black-box tools, and outlines future trends towards L4 autonomous chip design. Ultimately, this work aims to define the emerging field of Agentic EDA and provide a strategic roadmap for the transition from AI-assisted tools to fully autonomous design engineers.

