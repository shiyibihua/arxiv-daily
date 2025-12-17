---
layout: default
title: InfiniBench: Infinite Benchmarking for Visual Spatial Reasoning with Customizable Scene Complexity
---

# InfiniBench: Infinite Benchmarking for Visual Spatial Reasoning with Customizable Scene Complexity

<div class="paper-toolbar">
  <div class="toolbar-left">
    <a href="https://arxiv.org/abs/2511.18200" target="_blank" class="toolbar-btn">arXiv: 2511.18200v2</a>
    <a href="https://arxiv.org/pdf/2511.18200.pdf" target="_blank" class="toolbar-btn">PDF</a>
  </div>
  <div class="toolbar-right">
    <button class="toolbar-btn favorite-btn" data-arxiv-id="2511.18200v2" 
            onclick="toggleFavorite(this, '2511.18200v2', 'InfiniBench: Infinite Benchmarking for Visual Spatial Reasoning with Customizable Scene Complexity')" title="收藏">
      ☆ 收藏
    </button>
    <button class="toolbar-btn share-btn" onclick="copyLink()" title="复制链接">
      🔗 分享
    </button>
  </div>
</div>


**作者**: Haoming Wang, Qiyao Xue, Wei Gao

**分类**: cs.CV

**发布日期**: 2025-11-22 (更新: 2025-12-05)

---

## 💡 一句话要点

**InfiniBench：提出可定制场景复杂度的无限视觉空间推理评测基准。**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)**

**关键词**: `视觉语言模型` `空间推理` `3D场景生成` `基准测试` `场景复杂度` `LLM代理` `集群布局优化`

## 📋 核心要点

1. 现有视觉空间推理评测基准缺乏多样性和可定制性，难以充分评估VLM在复杂场景下的能力。
2. InfiniBench通过LLM驱动的代理、集群布局优化和任务感知相机轨迹优化，生成无限且可控的3D场景。
3. 实验证明InfiniBench在场景保真度和物理合理性上优于现有方法，并可用于多种空间推理任务。

## 📝 摘要（中文）

现代视觉语言模型(VLM)需要具备处理各种场景复杂度的空间推理能力，但由于缺乏多样、可扩展且完全可定制的基准，评估这些能力非常困难。现有基准在场景复杂度上的定制性有限，无法在不同的空间条件下隔离和分析特定的VLM失效模式。为了解决这个问题，本文提出了InfiniBench，一个全自动、可定制且用户友好的基准生成器，可以合成理论上无限种具有参数化控制场景复杂度的3D场景。InfiniBench独特地将自然语言的场景描述转换为具有复杂且物理上合理的3D布局的逼真视频。这通过三个关键创新实现：1) 基于LLM的代理框架，迭代地从场景描述中细化程序化场景约束；2) 灵活的基于集群的布局优化器，生成以前程序化方法难以处理的密集和杂乱的场景；3) 任务感知的相机轨迹优化方法，将场景渲染成具有完整对象覆盖的视频作为VLM输入。实验表明，InfiniBench在提示保真度和物理合理性方面优于最先进的程序化和基于LLM的3D生成方法，尤其是在高复杂度场景中。我们进一步展示了InfiniBench的用处，通过为代表性的空间推理任务（包括测量、透视和时空跟踪）生成基准。

## 🔬 方法详解

**问题定义**：现有视觉语言模型（VLM）在空间推理能力评估方面面临挑战，主要原因是缺乏能够生成多样化、可扩展且可定制复杂场景的基准。现有基准的场景复杂度定制性不足，难以隔离和分析VLM在特定空间条件下的失效模式。这限制了对VLM空间推理能力的深入理解和改进。

**核心思路**：InfiniBench的核心思路是构建一个全自动的基准生成器，该生成器能够根据自然语言描述，生成具有复杂且物理上合理的3D场景。通过参数化控制场景复杂度，InfiniBench可以创建理论上无限种不同的场景，从而为VLM的空间推理能力提供更全面和细致的评估。这种设计允许研究人员针对特定的空间推理任务和VLM失效模式，定制相应的评测基准。

**技术框架**：InfiniBench的技术框架主要包含三个模块：1) 基于LLM的代理框架：该模块负责将自然语言的场景描述转换为程序化的场景约束，并进行迭代优化。2) 基于集群的布局优化器：该模块用于生成密集和杂乱的3D场景布局，克服了传统程序化方法在处理高复杂度场景时的局限性。3) 任务感知的相机轨迹优化：该模块根据特定的空间推理任务，优化相机轨迹，确保生成的视频能够充分覆盖场景中的所有对象。

**关键创新**：InfiniBench的关键创新在于其全自动、可定制的场景生成能力，以及在高复杂度场景下的表现。与现有的程序化和基于LLM的3D生成方法相比，InfiniBench在提示保真度和物理合理性方面具有显著优势。此外，InfiniBench的集群布局优化器和任务感知相机轨迹优化方法，使其能够生成更复杂、更逼真且更适合VLM空间推理能力评估的场景。

**关键设计**：在基于LLM的代理框架中，使用了迭代细化的方法来优化场景约束，确保生成的场景与自然语言描述一致。集群布局优化器采用了基于物理的模拟方法，以生成密集且物理上合理的场景布局。任务感知的相机轨迹优化则使用了强化学习方法，以最大化场景中对象的覆盖率。

## 📊 实验亮点

InfiniBench在提示保真度和物理合理性方面优于最先进的程序化和基于LLM的3D生成方法，尤其是在高复杂度场景中。实验结果表明，InfiniBench能够生成更逼真、更复杂的3D场景，为VLM的空间推理能力评估提供更可靠的基准。通过为测量、透视和时空跟踪等代表性空间推理任务生成基准，展示了InfiniBench的实用性。

## 🎯 应用场景

InfiniBench可广泛应用于视觉语言模型的空间推理能力评估、模型训练数据生成、以及机器人导航和场景理解等领域。它能够帮助研究人员更深入地理解VLM的优势和不足，并推动VLM在实际应用中的发展。此外，该基准生成器还可以用于生成各种虚拟环境，用于训练和评估机器人的感知和决策能力。

## 📄 摘要（原文）

> Modern vision-language models (VLMs) are expected to have abilities of spatial reasoning with diverse scene complexities, but evaluating such abilities is difficult due to the lack of benchmarks that are not only diverse and scalable but also fully customizable. Existing benchmarks offer limited customizability over the scene complexity and are incapable of isolating and analyzing specific VLM failure modes under distinct spatial conditions. To address this gap, instead of individually presenting benchmarks for different scene complexities, in this paper we present InfiniBench, a fully automated, customizable and user-friendly benchmark generator that can synthesize a theoretically infinite variety of 3D scenes with parameterized control on scene complexity. InfiniBench uniquely translates scene descriptions in natural language into photo-realistic videos with complex and physically plausible 3D layouts. This is achieved through three key innovations: 1) a LLM-based agentic framework that iteratively refines procedural scene constraints from scene descriptions; 2) a flexible cluster-based layout optimizer that generates dense and cluttered scenes previously intractable for procedural methods; and 3) a task-aware camera trajectory optimization method that renders scenes into videos with full object coverage as VLM input. Experiments demonstrate that InfiniBench outperforms state-of-the-art procedural and LLM-based 3D generation methods in prompt fidelity and physical plausibility, especially in high-complexity scenarios. We further showcased the usefulness of InfiniBench, by generating benchmarks for representative spatial reasoning tasks including measurement, perspective-taking and spatiotemporal tracking.

