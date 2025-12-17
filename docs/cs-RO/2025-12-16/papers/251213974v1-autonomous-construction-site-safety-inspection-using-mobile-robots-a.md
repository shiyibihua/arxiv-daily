---
layout: default
title: Autonomous Construction-Site Safety Inspection Using Mobile Robots: A Multilayer VLM-LLM Pipeline
---

# Autonomous Construction-Site Safety Inspection Using Mobile Robots: A Multilayer VLM-LLM Pipeline

<div class="paper-toolbar">
  <div class="toolbar-left">
    <a href="https://arxiv.org/abs/2512.13974" target="_blank" class="toolbar-btn">arXiv: 2512.13974v1</a>
    <a href="https://arxiv.org/pdf/2512.13974.pdf" target="_blank" class="toolbar-btn">PDF</a>
  </div>
  <div class="toolbar-right">
    <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.13974v1" 
            onclick="toggleFavorite(this, '2512.13974v1', 'Autonomous Construction-Site Safety Inspection Using Mobile Robots: A Multilayer VLM-LLM Pipeline')" title="收藏">
      ☆ 收藏
    </button>
    <button class="toolbar-btn share-btn" onclick="copyLink()" title="复制链接">
      🔗 分享
    </button>
  </div>
</div>


**作者**: Hossein Naderi, Alireza Shojaei, Philip Agee, Kereshmeh Afsari, Abiola Akanmu

**分类**: cs.RO

**发布日期**: 2025-12-16

---

## 💡 一句话要点

**提出基于多层VLM-LLM流水线的移动机器人自主建筑工地安全巡检方案**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱三：空间感知 (Perception & SLAM)**

**关键词**: `建筑工地安全` `移动机器人` `自主巡检` `视觉语言模型` `大型语言模型` `多模态融合` `SLAM导航`

## 📋 核心要点

1. 现有建筑工地安全检查主要依赖人工，自动化方法依赖于特定任务数据集，难以适应快速变化的环境。
2. 论文提出多层VLM-LLM框架，利用移动机器人自主导航，结合视觉语言模型和大型语言模型自动生成安全巡检报告。
3. 实验结果表明，该方法在模拟建筑工地场景中，与现有闭源模型相比，具有较高的召回率和有竞争力的精确率。

## 📝 摘要（中文）

本文提出了一种利用移动机器人进行自主建筑工地安全巡检的多层框架。现有方法主要依赖于特定任务数据集，难以适应快速变化的建筑环境，且机器人现场巡检仍依赖人工遥操作和手动报告，劳动强度大。该框架结合了机器人技术和人工智能，通过SLAM和自主导航实现可重复覆盖和目标重访。在AI方面，基于视觉语言模型（VLM）的层生成场景描述，检索组件根据OSHA和现场策略进行信息定位，另一个VLM层基于规则评估安全状况，最后，大型语言模型（LLM）层根据之前的输出生成安全报告。该框架通过概念验证实现进行了验证，并在模拟常见危险的实验室环境中进行了评估。结果表明，与最先进的闭源模型相比，该方法具有较高的召回率和有竞争力的精确率。该论文贡献了一个透明、可推广的流水线，通过暴露每一层的中间结果并将人纳入循环，超越了黑盒模型。这项工作为未来在建筑环境内外扩展到其他任务和设置奠定了基础。

## 🔬 方法详解

**问题定义**：论文旨在解决建筑工地安全巡检自动化程度低，依赖人工和特定任务数据集的问题。现有方法难以适应快速变化的建筑环境，且机器人巡检仍需人工遥操作和手动报告，效率低下，成本高昂。

**核心思路**：论文的核心思路是利用移动机器人进行自主导航，并结合视觉语言模型（VLM）和大型语言模型（LLM）自动分析场景，评估安全状况，并生成巡检报告。通过VLM理解场景，LLM进行推理和报告生成，从而实现端到端的自动化安全巡检。

**技术框架**：该框架包含机器人和AI两个主要模块。机器人模块负责SLAM和自主导航，实现对建筑工地的可重复覆盖和目标重访。AI模块是一个多层流水线，包括：1) VLM层：生成场景描述；2) 检索组件：根据OSHA和现场策略进行信息检索；3) VLM层：基于规则评估安全状况；4) LLM层：生成安全报告。各层之间通过中间结果传递信息，实现透明化和可解释性。

**关键创新**：该论文的关键创新在于将VLM和LLM结合，构建了一个多层流水线，实现了建筑工地安全巡检的自动化。与传统的黑盒模型相比，该方法具有更高的透明度和可解释性，并且可以通过人工干预进行调整和优化。此外，该方法不依赖于特定任务数据集，具有更好的泛化能力。

**关键设计**：论文中VLM和LLM的具体选择和配置未详细说明，检索组件的实现方式也未明确。但整体框架的设计思路清晰，通过多层模块化设计，实现了复杂任务的分解和协同。未来的研究可以进一步探索不同VLM和LLM的选择，以及更高效的检索算法。

## 📊 实验亮点

该论文在模拟建筑工地场景中进行了实验验证，结果表明，与最先进的闭源模型相比，该方法具有较高的召回率和有竞争力的精确率。这表明该方法在建筑工地安全巡检方面具有一定的优势和潜力。具体的性能数据和提升幅度未在摘要中详细给出。

## 🎯 应用场景

该研究成果可应用于建筑工地安全巡检，降低人工成本，提高巡检效率和准确性。此外，该方法还可以扩展到其他需要自动化场景理解和报告生成的领域，如智能安防、环境监测、灾害救援等，具有广泛的应用前景。

## 📄 摘要（原文）

> Construction safety inspection remains mostly manual, and automated approaches still rely on task-specific datasets that are hard to maintain in fast-changing construction environments due to frequent retraining. Meanwhile, field inspection with robots still depends on human teleoperation and manual reporting, which are labor-intensive. This paper aims to connect what a robot sees during autonomous navigation to the safety rules that are common in construction sites, automatically generating a safety inspection report. To this end, we proposed a multi-layer framework with two main modules: robotics and AI. On the robotics side, SLAM and autonomous navigation provide repeatable coverage and targeted revisits via waypoints. On AI side, a Vision Language Model (VLM)-based layer produces scene descriptions; a retrieval component powered grounds those descriptions in OSHA and site policies; Another VLM-based layer assesses the safety situation based on rules; and finally Large Language Model (LLM) layer generates safety reports based on previous outputs. The framework is validated with a proof-of-concept implementation and evaluated in a lab environment that simulates common hazards across three scenarios. Results show high recall with competitive precision compared to state-of-the-art closed-source models. This paper contributes a transparent, generalizable pipeline that moves beyond black-box models by exposing intermediate artifacts from each layer and keeping the human in the loop. This work provides a foundation for future extensions to additional tasks and settings within and beyond construction context.

