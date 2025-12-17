---
layout: default
title: HanDyVQA: A Video QA Benchmark for Fine-Grained Hand-Object Interaction Dynamics
---

# HanDyVQA: A Video QA Benchmark for Fine-Grained Hand-Object Interaction Dynamics

<div class="paper-toolbar">
  <div class="toolbar-left">
    <a href="https://arxiv.org/abs/2512.00885" target="_blank" class="toolbar-btn">arXiv: 2512.00885v1</a>
    <a href="https://arxiv.org/pdf/2512.00885.pdf" target="_blank" class="toolbar-btn">PDF</a>
  </div>
  <div class="toolbar-right">
    <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.00885v1" 
            onclick="toggleFavorite(this, '2512.00885v1', 'HanDyVQA: A Video QA Benchmark for Fine-Grained Hand-Object Interaction Dynamics')" title="收藏">
      ☆ 收藏
    </button>
    <button class="toolbar-btn share-btn" onclick="copyLink()" title="复制链接">
      🔗 分享
    </button>
  </div>
</div>


**作者**: Masatoshi Tateno, Gido Kato, Hirokatsu Kataoka, Yoichi Sato, Takuma Yagi

**分类**: cs.CV

**发布日期**: 2025-11-30

**备注**: Project page: https://masatate.github.io/HanDyVQA-project-page/

---

## 💡 一句话要点

**HanDyVQA：一个用于细粒度手-物交互动态的视频问答基准**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱五：交互与反应 (Interaction & Reaction)**

**关键词**: `视频问答` `手-物交互` `细粒度理解` `视频理解` `HOI` `时空推理` `部件级别理解`

## 📋 核心要点

1. 现有HOI基准缺乏细粒度的时空推理能力，难以捕捉手-物交互中的动态过程。
2. HanDyVQA基准通过六种问题类型和物体部件分割掩码，全面评估HOI的操作和效果。
3. 实验表明，现有视频基础模型在HanDyVQA上表现不佳，表明HOI动态理解仍具挑战。

## 📝 摘要（中文）

手-物交互(HOI)本质上涉及动态过程，其中人类操作会对物体产生独特的时空影响。然而，现有的语义HOI基准要么侧重于操作，要么侧重于粗略层面的结果影响，缺乏捕获HOI底层动态的细粒度时空推理。我们推出了HanDyVQA，这是一个细粒度的视频问答基准，全面涵盖了HOI的操作和效果两方面。HanDyVQA包含六种互补的问题类型（动作、过程、物体、位置、状态变化和物体部件），总计11.1K个多项选择QA对。收集的QA对能够识别操作风格、手/物体的运动以及部件级别的状态变化。HanDyVQA还包括10.3K个物体和物体部件的分割掩码，从而能够评估视频物体分割中物体/部件级别的推理。我们在我们的基准上评估了最新的视频基础模型，发现即使是性能最佳的模型Gemini-2.5-Pro也仅达到73%的平均准确率，远低于人类的表现（97%）。进一步的分析表明，空间关系、运动和部件级别的几何理解仍然存在挑战。我们还发现，将显式的HOI相关线索集成到视觉特征中可以提高性能，这为开发未来具有更深入HOI动态理解的模型提供了见解。

## 🔬 方法详解

**问题定义**：现有HOI视频理解方法主要关注粗粒度的操作或结果，缺乏对细粒度时空动态的建模能力。这导致模型难以理解手部动作如何影响物体状态，以及物体部件之间的交互关系。现有基准无法充分评估模型在这些方面的能力。

**核心思路**：HanDyVQA的核心思路是构建一个包含细粒度标注的视频问答数据集，涵盖手-物交互的各个方面，包括动作、过程、物体、位置、状态变化和物体部件。通过设计不同类型的问题，迫使模型进行更深入的时空推理和部件级别的理解。

**技术框架**：HanDyVQA数据集包含11.1K个多项选择QA对和10.3K个物体和物体部件的分割掩码。问题类型包括：Action (动作)、Process (过程)、Objects (物体)、Location (位置)、State Change (状态变化)和Object Parts (物体部件)。分割掩码用于评估模型在物体和部件级别的分割能力。数据集的构建过程包括视频收集、问题生成、答案标注和分割掩码标注。

**关键创新**：HanDyVQA的关键创新在于其细粒度的标注和全面的问题类型设计。与现有HOI基准相比，HanDyVQA更关注手部动作对物体状态的影响，以及物体部件之间的交互关系。此外，数据集还提供了物体和部件的分割掩码，从而能够评估模型在物体和部件级别的理解能力。

**关键设计**：数据集中的问题设计旨在涵盖HOI的各个方面，包括动作类型、操作过程、涉及的物体、物体的位置、状态变化以及物体部件。分割掩码的标注采用了人工标注的方式，保证了标注的准确性。评估指标包括平均准确率和分割指标（如IoU）。

## 📊 实验亮点

在HanDyVQA基准上，即使是性能最佳的视频基础模型Gemini-2.5-Pro也仅达到73%的平均准确率，远低于人类的表现（97%）。这表明现有模型在细粒度手-物交互理解方面仍存在很大的提升空间。研究还发现，将显式的HOI相关线索集成到视觉特征中可以提高性能，这为未来的模型设计提供了重要的指导。

## 🎯 应用场景

HanDyVQA可用于训练和评估视频理解模型在手-物交互方面的能力，促进智能机器人、人机交互、虚拟现实等领域的发展。例如，可以应用于机器人操作任务，使机器人能够更好地理解人类的指令并执行复杂的任务。此外，该基准还可以用于开发更智能的视频监控系统，能够识别异常行为并及时发出警报。

## 📄 摘要（原文）

> Hand-object interaction (HOI) inherently involves dynamics where human manipulations produce distinct spatio-temporal effects on objects. However, existing semantic HOI benchmarks focused either on manipulation or on the resulting effects at a coarse level, lacking fine-grained spatio-temporal reasoning to capture the underlying dynamics in HOI. We introduce HanDyVQA, a fine-grained video question-answering benchmark that comprehensively covers both the manipulation and effect aspects of HOI. HanDyVQA comprises six complementary question types (Action, Process, Objects, Location, State Change, and Object Parts), totalling 11.1K multiple-choice QA pairs. Collected QA pairs recognizing manipulation styles, hand/object motions, and part-level state changes. HanDyVQA also includes 10.3K segmentation masks for Objects and Object Parts questions, enabling the evaluation of object/part-level reasoning in video object segmentation. We evaluated recent video foundation models on our benchmark and found that even the best-performing model, Gemini-2.5-Pro, reached only 73% average accuracy, which is far from human performance (97%). Further analysis shows the remaining challenges in spatial relationship, motion, and part-level geometric understanding. We also found that integrating explicit HOI-related cues into visual features improves performance, offering insights for developing future models with a deeper understanding of HOI dynamics.

