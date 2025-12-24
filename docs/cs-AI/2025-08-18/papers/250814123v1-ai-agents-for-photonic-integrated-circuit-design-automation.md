---
layout: default
title: AI Agents for Photonic Integrated Circuit Design Automation
---

# AI Agents for Photonic Integrated Circuit Design Automation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.14123" class="toolbar-btn" target="_blank">📄 arXiv: 2508.14123v1</a>
  <a href="https://arxiv.org/pdf/2508.14123.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.14123v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.14123v1', 'AI Agents for Photonic Integrated Circuit Design Automation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Ankita Sharma, YuQi Fu, Vahid Ansari, Rishabh Iyer, Fiona Kuang, Kashish Mistry, Raisa Islam Aishy, Sara Ahmad, Joaquin Matres, Dirk R. Englund, Joyce K. S. Poon

**分类**: cs.AR, cs.AI, physics.app-ph, physics.optics

**发布日期**: 2025-08-18

---

## 💡 一句话要点

**提出PhIDO框架以实现光子集成电路设计自动化**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `光子集成电路` `设计自动化` `自然语言处理` `多智能体系统` `大型语言模型` `布局掩模文件` `机器人自动化`

## 📋 核心要点

1. 现有光子集成电路设计方法效率低下，难以快速响应复杂的设计请求。
2. 论文提出的PhIDO框架利用多智能体系统，将自然语言设计请求转化为具体的布局文件，提升设计自动化水平。
3. 实验结果显示，单设备设计成功率达到91%，而对于小型设计，部分模型的成功率可达57%，显著提高了设计效率。

## 📝 摘要（中文）

本文提出了光子智能设计与优化（PhIDO）框架，该框架能够将自然语言的光子集成电路（PIC）设计请求转换为布局掩模文件。通过对102个设计描述的测试，比较了7种推理大型语言模型在PhIDO中的表现。单设备设计的成功率高达91%。对于组件数量不超过15的设计查询，o1、Gemini-2.5-pro和Claude Opus 4的端到端通过率约为57%，其中Gemini-2.5-pro在输出令牌数量和成本上表现最佳。未来的工作将集中在标准化知识表示、扩展数据集、增强验证和机器人自动化等方面。

## 🔬 方法详解

**问题定义**：本文旨在解决光子集成电路设计中的自动化问题，现有方法在处理复杂设计请求时效率低下，难以满足快速响应的需求。

**核心思路**：PhIDO框架通过多智能体系统，将自然语言描述转化为具体的设计文件，利用大型语言模型进行推理和生成，旨在提高设计的自动化和准确性。

**技术框架**：PhIDO框架包括多个模块，首先接收自然语言输入，然后通过推理模型进行解析，最后生成布局掩模文件。整个流程涉及设计请求的理解、模型推理和文件生成三个主要阶段。

**关键创新**：最重要的创新在于将自然语言处理与光子集成电路设计结合，利用大型语言模型进行高效推理，显著提升了设计的自动化水平。与传统方法相比，PhIDO框架能够更好地处理复杂的设计请求。

**关键设计**：在模型选择上，论文比较了7种大型语言模型，重点关注输出令牌数量和成本，选择了性能最佳的模型进行设计生成。

## 📊 实验亮点

实验结果显示，单设备设计的成功率高达91%。在组件数量不超过15的设计查询中，o1、Gemini-2.5-pro和Claude Opus 4的端到端通过率约为57%。其中，Gemini-2.5-pro在输出令牌数量和成本方面表现最佳，展示了其在设计自动化中的优势。

## 🎯 应用场景

该研究的潜在应用领域包括光子集成电路的设计与制造，尤其是在快速原型开发和定制化设计方面。PhIDO框架的实现将大幅提升设计效率，降低人力成本，推动光子技术在通信、传感和计算等领域的应用。未来，随着技术的成熟，可能会实现更广泛的自动化设计流程。

## 📄 摘要（原文）

> We present Photonics Intelligent Design and Optimization (PhIDO), a multi-agent framework that converts natural-language photonic integrated circuit (PIC) design requests into layout mask files. We compare 7 reasoning large language models for PhIDO using a testbench of 102 design descriptions that ranged from single devices to 112-component PICs. The success rate for single-device designs was up to 91%. For design queries with less than or equal to 15 components, o1, Gemini-2.5-pro, and Claude Opus 4 achieved the highest end-to-end pass@5 success rates of approximately 57%, with Gemini-2.5-pro requiring the fewest output tokens and lowest cost. The next steps toward autonomous PIC development include standardized knowledge representations, expanded datasets, extended verification, and robotic automation.

