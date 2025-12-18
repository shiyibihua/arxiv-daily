---
layout: default
title: LLM Agents for Knowledge Discovery in Atomic Layer Processing
---

# LLM Agents for Knowledge Discovery in Atomic Layer Processing

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.26201" class="toolbar-btn" target="_blank">📄 arXiv: 2509.26201v1</a>
  <a href="https://arxiv.org/pdf/2509.26201.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.26201v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.26201v1', 'LLM Agents for Knowledge Discovery in Atomic Layer Processing')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Andreas Werbrouck, Marshall B. Lindsay, Matthew Maschmann, Matthias J. Young

**分类**: cs.AI, cond-mat.mes-hall, cond-mat.mtrl-sci

**发布日期**: 2025-09-30

**备注**: Accepted submission to the AI4MAT workshop@NEURIPS 2025. As submitted, except author names added

---

## 💡 一句话要点

**利用LLM Agent在原子层处理中进行知识发现**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `LLM Agent` `知识发现` `原子层处理` `材料科学` `LangGraph` `自主学习`

## 📋 核心要点

1. 现有材料科学研究中，知识发现依赖人工经验，效率低且易受主观因素影响。
2. 利用LLM Agent自主探索和验证关于系统行为的陈述，实现自动化知识发现。
3. 实验证明LLM Agent能在原子层处理模拟中发现化学相互作用，无需人工干预。

## 📝 摘要（中文）

大型语言模型（LLM）近年来备受关注。最近，有人提出将其用作独立推理的Agent。本文旨在测试此类Agent在材料科学中进行知识发现的潜力。我们重新利用LangGraph的工具功能，为Agent提供一个黑盒函数进行查询。与过程优化或执行特定的用户定义任务不同，知识发现包括自由探索系统，提出和验证关于黑盒行为的陈述，其唯一目标是生成和验证可推广的陈述。我们通过一个儿童游戏来证明这种方法的概念，展示了试错和坚持在知识发现中的作用，以及结果的强路径依赖性。然后，我们应用相同的策略来表明，LLM Agent可以在先进的原子层处理反应器模拟中探索、发现和利用各种化学相互作用，而无需明确的指令，仅使用有意限制的探测能力。

## 🔬 方法详解

**问题定义**：论文旨在解决材料科学领域中知识发现效率低下的问题。传统的知识发现方法依赖于研究人员的经验和直觉，需要大量的人工实验和分析，效率低下且容易受到主观因素的影响。此外，对于复杂的材料系统，人工难以全面探索所有可能的参数组合和相互作用。

**核心思路**：论文的核心思路是利用LLM Agent的推理和探索能力，使其能够自主地探索材料系统，并从中发现新的知识。Agent通过与一个黑盒函数（即材料系统的模拟器）进行交互，提出假设并验证这些假设，从而逐步构建对系统的理解。这种方法类似于人类科学家进行实验的过程，但可以自动化地进行，从而大大提高知识发现的效率。

**技术框架**：论文使用LangGraph框架来构建LLM Agent。Agent的主要组成部分包括：1) 知识库：用于存储Agent已经发现的知识；2) 探索策略：用于决定Agent下一步要探索的参数组合；3) 假设生成器：用于根据已有的知识生成新的假设；4) 验证模块：用于通过与黑盒函数交互来验证假设。整个流程是一个循环迭代的过程，Agent不断地探索、学习和改进其对系统的理解。

**关键创新**：论文的关键创新在于将LLM Agent应用于材料科学领域的知识发现。与传统的机器学习方法不同，LLM Agent不仅可以学习数据中的模式，还可以进行推理和生成新的假设。这使得Agent能够发现隐藏在数据中的深层知识，而这些知识是传统方法难以发现的。此外，Agent的自主探索能力使其能够适应不同的材料系统，而无需人工进行大量的参数调整。

**关键设计**：论文中一个关键的设计是Agent与黑盒函数之间的交互方式。Agent通过提出问题并接收黑盒函数的回答来获取信息。为了限制Agent的探索范围，论文有意限制了Agent的探测能力。例如，Agent只能测量某些特定的物理量，而不能直接观察系统的内部状态。这种限制迫使Agent进行更深入的推理，从而发现更重要的知识。

## 📊 实验亮点

论文通过儿童游戏和原子层处理模拟实验验证了LLM Agent在知识发现方面的潜力。在原子层处理模拟中，Agent能够在有限的探测能力下，自主发现并利用各种化学相互作用，无需人工干预。这表明LLM Agent具有强大的自主学习和知识发现能力，能够有效地解决材料科学领域中的复杂问题。

## 🎯 应用场景

该研究成果可应用于新材料设计、工艺优化、故障诊断等领域。通过自动化知识发现，加速新材料的研发进程，降低研发成本。在原子层处理等复杂工艺中，可用于优化工艺参数，提高产品质量和良率。此外，该方法还可用于分析实验数据，发现潜在的故障原因，提高生产效率。

## 📄 摘要（原文）

> Large Language Models (LLMs) have garnered significant attention for several years now. Recently, their use as independently reasoning agents has been proposed. In this work, we test the potential of such agents for knowledge discovery in materials science. We repurpose LangGraph's tool functionality to supply agents with a black box function to interrogate. In contrast to process optimization or performing specific, user-defined tasks, knowledge discovery consists of freely exploring the system, posing and verifying statements about the behavior of this black box, with the sole objective of generating and verifying generalizable statements. We provide proof of concept for this approach through a children's parlor game, demonstrating the role of trial-and-error and persistence in knowledge discovery, and the strong path-dependence of results. We then apply the same strategy to show that LLM agents can explore, discover, and exploit diverse chemical interactions in an advanced Atomic Layer Processing reactor simulation using intentionally limited probe capabilities without explicit instructions.

