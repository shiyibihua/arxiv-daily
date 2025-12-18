---
layout: default
title: Towards a Neurosymbolic Reasoning System Grounded in Schematic Representations
---

# Towards a Neurosymbolic Reasoning System Grounded in Schematic Representations

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.03644" class="toolbar-btn" target="_blank">📄 arXiv: 2509.03644v1</a>
  <a href="https://arxiv.org/pdf/2509.03644.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.03644v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.03644v1', 'Towards a Neurosymbolic Reasoning System Grounded in Schematic Representations')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: François Olivier, Zied Bouraoui

**分类**: cs.AI, cs.CL

**发布日期**: 2025-09-03

**备注**: To appear in Proceedings of Machine Learning Research, 19th Conference on Neurosymbolic Learning and Reasoning, 2025

---

## 💡 一句话要点

**提出Embodied-LM，通过具身图式表征增强神经符号推理能力**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `神经符号推理` `具身认知` `图像图式` `大型语言模型` `解答集编程`

## 📋 核心要点

1. 大型语言模型在逻辑推理方面存在不足，缺乏人类拥有的稳健心智表征。
2. Embodied-LM通过图像图式将理解和逻辑推理建立在具身认知结构之上。
3. 实验证明，该系统能有效引导LLMs进行逻辑推理，并提升可解释性。

## 📝 摘要（中文）

尽管自然语言理解取得了显著进展，但大型语言模型（LLMs）在执行逻辑推理时仍然容易出错，通常缺乏类似人类的、稳健的心智表征。我们介绍了一个原型神经符号系统Embodied-LM，它将理解和逻辑推理建立在基于图像图式的图式表征之上——图像图式是从感觉运动经验中获得的、构成人类认知的重复模式。我们的系统在解答集编程（Answer Set Programming）中，利用声明式空间推理来实现这些认知结构的空间基础。通过对逻辑演绎问题的评估，我们证明了可以引导LLMs通过具身认知结构来解释场景，这些结构可以被形式化为可执行程序，并且由此产生的表征支持有效的、具有增强可解释性的逻辑推理。虽然我们目前的实现侧重于空间原语，但它为整合更复杂和动态的表征奠定了计算基础。

## 🔬 方法详解

**问题定义**：现有的大型语言模型在进行逻辑推理时，常常表现出不尽如人意的地方。它们缺乏像人类一样基于经验的、稳健的心智模型，导致在理解和推理复杂场景时容易出错。现有的方法难以将语言与实际的物理世界联系起来，缺乏具身认知的能力。

**核心思路**：本文的核心思路是利用图像图式（Image Schemas）作为LLM进行逻辑推理的桥梁。图像图式是从感觉运动经验中提取的重复模式，能够有效地组织和结构化人类的认知。通过将语言描述的场景映射到图像图式，并利用这些图式进行推理，可以提升LLM的逻辑推理能力和可解释性。

**技术框架**：Embodied-LM系统的整体框架包含以下几个主要模块：1) 场景理解模块：利用LLM解析自然语言描述的场景，提取关键的空间关系和对象信息。2) 图式激活模块：根据场景信息，激活相应的图像图式。3) 空间推理模块：使用解答集编程（Answer Set Programming, ASP）对激活的图式进行形式化表示，并进行声明式空间推理。4) 结果输出模块：将推理结果以自然语言的形式呈现。

**关键创新**：该论文的关键创新在于将具身认知理论中的图像图式引入到神经符号推理系统中。通过将LLM与ASP相结合，实现了从自然语言到可执行程序的转换，从而提升了逻辑推理的可靠性和可解释性。与传统的符号推理系统相比，Embodied-LM能够更好地处理不确定性和模糊性。

**关键设计**：在空间推理模块中，论文使用ASP来表示和推理图像图式。ASP是一种声明式编程范式，允许用户描述问题的约束条件，而无需指定具体的求解过程。论文定义了一系列ASP规则，用于表示常见的空间关系（如“在…之上”、“在…之间”等）和推理规则。此外，论文还设计了一种机制，用于将LLM提取的场景信息转换为ASP的事实，从而实现LLM与ASP的无缝集成。

## 📊 实验亮点

论文通过在逻辑演绎问题上的评估，证明了Embodied-LM能够有效地引导LLMs通过具身认知结构来解释场景，并将这些结构形式化为可执行程序。实验结果表明，该系统能够提升逻辑推理的准确性和可解释性，为神经符号推理的研究提供了一个新的方向。

## 🎯 应用场景

该研究成果可应用于智能机器人、人机交互、自然语言理解等领域。例如，可以帮助机器人更好地理解人类指令，并在复杂环境中进行导航和操作。此外，该系统还可以用于构建更智能的对话系统，使其能够进行更深入的推理和理解。

## 📄 摘要（原文）

> Despite significant progress in natural language understanding, Large Language Models (LLMs) remain error-prone when performing logical reasoning, often lacking the robust mental representations that enable human-like comprehension. We introduce a prototype neurosymbolic system, Embodied-LM, that grounds understanding and logical reasoning in schematic representations based on image schemas-recurring patterns derived from sensorimotor experience that structure human cognition. Our system operationalizes the spatial foundations of these cognitive structures using declarative spatial reasoning within Answer Set Programming. Through evaluation on logical deduction problems, we demonstrate that LLMs can be guided to interpret scenarios through embodied cognitive structures, that these structures can be formalized as executable programs, and that the resulting representations support effective logical reasoning with enhanced interpretability. While our current implementation focuses on spatial primitives, it establishes the computational foundation for incorporating more complex and dynamic representations.

