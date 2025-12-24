---
layout: default
title: Holistic Evaluation of Multimodal LLMs on Spatial Intelligence
---

# Holistic Evaluation of Multimodal LLMs on Spatial Intelligence

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.13142" class="toolbar-btn" target="_blank">📄 arXiv: 2508.13142v4</a>
  <a href="https://arxiv.org/pdf/2508.13142.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.13142v4" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.13142v4', 'Holistic Evaluation of Multimodal LLMs on Spatial Intelligence')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zhongang Cai, Yubo Wang, Qingping Sun, Ruisi Wang, Chenyang Gu, Wanqi Yin, Zhiqian Lin, Zhitao Yang, Chen Wei, Oscar Qian, Hui En Pang, Xuanke Shi, Kewang Deng, Xiaoyang Han, Zukai Chen, Jiaqi Li, Xiangyu Fan, Hanming Deng, Lewei Lu, Bo Li, Ziwei Liu, Quan Wang, Dahua Lin, Lei Yang

**分类**: cs.CV, cs.CL, cs.LG, cs.MM, cs.RO

**发布日期**: 2025-08-18 (更新: 2025-11-27)

**备注**: Codebase: https://github.com/EvolvingLMMs-Lab/EASI/; Leaderboard: https://huggingface.co/spaces/lmms-lab-si/EASI-Leaderboard

---

## 💡 一句话要点

**提出EASI以全面评估多模态LLMs在空间智能上的表现**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `空间智能` `多模态模型` `评估框架` `人工智能` `模型比较` `任务分类` `开源代码` `社区合作`

## 📋 核心要点

1. 现有多模态模型在空间理解和推理方面存在显著不足，限制了其在实际应用中的有效性。
2. 提出EASI框架，系统整合空间任务基准，提供标准化接口和协议，便于对多模态模型进行全面评估。
3. 实验证明，GPT-5在空间智能任务中表现优异，但仍未达到人类水平，且在复杂任务中模型能力不足的现象明显。

## 📝 摘要（中文）

多模态模型近年来取得了显著进展，但在空间理解和推理方面仍存在明显局限，这一能力是人工通用智能在物理世界中的基础。随着GPT-5的发布，本文及时评估了当前领先模型（如GPT、Gemini等）在空间智能（SI）方面的表现。我们提出了EASI，一个全面的空间任务评估框架，整合了现有基准和新创建的任务，支持对最先进模型的系统评估。研究表明，尽管GPT-5在SI方面表现出色，但在广泛的SI任务中仍显著低于人类表现。此外，SI任务暴露出模型能力的不足，尤其是在面对最具挑战性的任务时，专有模型未能展现出明显优势。我们还进行了定性评估，发现许多直观的场景对当前多模态模型构成挑战。EASI是一个持续的社区努力，已开源代码库并建立了EASI排行榜，以促进对SI的集体进展。

## 🔬 方法详解

**问题定义**：本文旨在解决多模态模型在空间智能（SI）任务中的评估问题。现有方法缺乏统一的评估框架，导致模型性能难以比较和分析。

**核心思路**：EASI框架通过构建全面的空间任务分类法，整合现有基准和新任务，提供系统化的评估方案，旨在提升对多模态模型的理解和比较。

**技术框架**：EASI框架包括任务分类、评估标准、数据集整合和模型评估四个主要模块。通过标准化的接口和协议，用户可以方便地配置和运行多个基准测试。

**关键创新**：EASI的核心创新在于其全面的任务分类和整合能力，使得不同模型在空间智能任务上的表现可以进行系统性比较，填补了现有评估方法的空白。

**关键设计**：EASI采用标准化的评估协议，设计了多样化的空间任务，并通过开源代码库提供可复现的实验环境，确保评估过程的透明性和可重复性。具体参数设置和损失函数设计在文中详细说明。

## 📊 实验亮点

实验结果显示，GPT-5在空间智能任务中表现出前所未有的强度，但在广泛的SI任务中仍显著低于人类表现。研究还发现，SI任务揭示了模型能力的更大缺陷，尤其是在面对最具挑战性的任务时，专有模型未能展现出明显优势。

## 🎯 应用场景

该研究的潜在应用领域包括机器人导航、自动驾驶、增强现实等，需要高水平空间理解和推理能力的场景。EASI框架的建立将推动多模态模型在这些领域的应用，提升其智能水平和实用性。

## 📄 摘要（原文）

> Multimodal models have achieved remarkable progress in recent years. Nevertheless, they continue to exhibit notable limitations in spatial understanding and reasoning, the very capability that anchors artificial general intelligence in the physical world. With the recent release of GPT-5, allegedly the most powerful AI model to date, it is timely to examine where the leading models (GPT, Gemini, Grok, Seed, Qwen, and Intern) stand on the path toward spatial intelligence (SI). We thus propose EASI for holistic Evaluation of multimodAl LLMs on Spatial Intelligence. EASI conceptualizes a comprehensive taxonomy of spatial tasks that unifies existing benchmarks and a growing collection of newly curated ones, enabling systematic evaluation of state-of-the-art models. In this report, we conduct the study across eight key benchmarks, at a cost exceeding ten billion total tokens. Our empirical study then reveals that (1) GPT-5 demonstrates unprecedented strength in SI, yet (2) still falls short of human performance significantly across a broad spectrum of SI-tasks. Moreover, we (3) show that SI-tasks expose greater model capability deficiency than non-SI tasks, to the extent that (4) proprietary models do not exhibit a decisive advantage when facing the most difficult ones. In addition, we conduct a qualitative evaluation across a diverse set of scenarios that are intuitive for humans, yet fail the most advanced multimodal models. EASI is an ongoing community effort: we have open-sourced the EASI codebase that provides a one-stop and reproducible solution with standardized interfaces, integrated protocols and prompts that significantly reduce the friction of configuring and running multiple benchmarks; we have also launched an accompanying EASI leaderboard to provide a continually updated snapshot of model performance across the full SI spectrum, accelerating collective progress toward robust SI.

