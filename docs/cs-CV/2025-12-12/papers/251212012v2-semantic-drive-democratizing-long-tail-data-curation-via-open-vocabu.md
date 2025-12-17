---
layout: default
title: Semantic-Drive: Democratizing Long-Tail Data Curation via Open-Vocabulary Grounding and Neuro-Symbolic VLM Consensus
---

# Semantic-Drive: Democratizing Long-Tail Data Curation via Open-Vocabulary Grounding and Neuro-Symbolic VLM Consensus

<div class="paper-toolbar">
  <div class="toolbar-left">
    <a href="https://arxiv.org/abs/2512.12012" target="_blank" class="toolbar-btn">arXiv: 2512.12012v2</a>
    <a href="https://arxiv.org/pdf/2512.12012.pdf" target="_blank" class="toolbar-btn">PDF</a>
  </div>
  <div class="toolbar-right">
    <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.12012v2" 
            onclick="toggleFavorite(this, '2512.12012v2', 'Semantic-Drive: Democratizing Long-Tail Data Curation via Open-Vocabulary Grounding and Neuro-Symbolic VLM Consensus')" title="收藏">
      ☆ 收藏
    </button>
    <button class="toolbar-btn share-btn" onclick="copyLink()" title="复制链接">
      🔗 分享
    </button>
  </div>
</div>


**作者**: Antonio Guillen-Perez

**分类**: cs.CV, cs.AI, cs.CL, cs.RO

**发布日期**: 2025-12-12 (更新: 2025-12-16)

---

## 💡 一句话要点

**Semantic-Drive：通过开放词汇 grounding 和神经符号 VLM 共识实现长尾数据挖掘**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)**

**关键词**: `自动驾驶` `长尾数据挖掘` `开放词汇检测` `视觉语言模型` `神经符号推理` `数据标注` `事件识别`

## 📋 核心要点

1. 自动驾驶长尾数据稀缺，人工标注成本高昂，现有元数据搜索精度不足，云端VLM方案存在隐私问题。
2. Semantic-Drive 采用本地优先的神经符号框架，通过开放词汇检测和神经符号 VLM 共识进行语义数据挖掘。
3. 实验表明，Semantic-Drive 在 nuScenes 数据集上实现了更高的召回率，并显著降低了风险评估误差，且可在消费级硬件上运行。

## 📝 摘要（中文）

自动驾驶车辆（AVs）的发展受到“长尾”训练数据稀缺的限制。虽然车队收集了大量的视频日志，但识别罕见的安全关键事件（例如，不稳定的乱穿马路、施工改道）仍然是一个手动且成本高昂的过程。现有的解决方案依赖于粗略的元数据搜索（缺乏精度）或基于云的 VLM（侵犯隐私且昂贵）。我们引入了 Semantic-Drive，这是一个用于语义数据挖掘的本地优先的神经符号框架。我们的方法将感知解耦为两个阶段：（1）通过实时开放词汇检测器（YOLOE）进行符号 grounding 以锚定注意力，以及（2）通过推理 VLM 进行认知分析，执行取证场景分析。为了减轻幻觉，我们实施了一种“系统 2”推理时对齐策略，利用多模型“Judge-Scout”共识机制。在 nuScenes 数据集上针对 Waymo Open Dataset (WOD-E2E) 分类法进行基准测试，Semantic-Drive 实现了 0.966 的召回率（CLIP 为 0.475），并且与最佳单 scout 模型相比，风险评估误差降低了 40%。该系统完全在消费级硬件（NVIDIA RTX 3090）上运行，为云提供了一种保护隐私的替代方案。

## 🔬 方法详解

**问题定义**：论文旨在解决自动驾驶领域中长尾数据难以获取和标注的问题。现有方法，如基于粗略元数据的搜索，精度较低，无法有效识别罕见但关键的安全事件。而依赖云端视觉语言模型（VLM）的方案，则面临隐私泄露和高昂计算成本的挑战。

**核心思路**：论文的核心思路是将感知过程解耦为符号 grounding 和认知分析两个阶段。首先利用开放词汇检测器（YOLOE）在视频中定位潜在目标，然后使用推理 VLM 对场景进行分析，判断是否为目标事件。通过这种方式，可以更精确地识别长尾数据，并降低对人工标注的依赖。

**技术框架**：Semantic-Drive 框架包含以下主要模块：1) **开放词汇检测器 (YOLOE)**：用于检测视频帧中的各种物体，提供 grounding 信息。2) **推理 VLM**：对检测到的物体和场景进行分析，判断是否符合目标事件的语义描述。3) **Judge-Scout 共识机制**：采用多个 VLM 模型进行推理，通过共识机制减少幻觉，提高判断的准确性。

**关键创新**：该论文的关键创新在于将神经符号方法应用于自动驾驶长尾数据的挖掘。通过结合开放词汇检测和神经符号 VLM 共识，实现了更精确、更高效的事件识别。与现有方法相比，该方法无需预定义类别，能够识别更广泛的长尾事件，并且可以在本地运行，保护用户隐私。

**关键设计**：论文采用 YOLOE 作为开放词汇检测器，因为它具有实时性和较高的检测精度。在 VLM 部分，采用了多模型“Judge-Scout”共识机制，通过多个模型的投票来减少幻觉。具体实现细节和参数设置在论文中未详细说明，属于未知信息。

## 📊 实验亮点

Semantic-Drive 在 nuScenes 数据集上进行了评估，并与基于 CLIP 的方法进行了比较。实验结果表明，Semantic-Drive 实现了 0.966 的召回率，远高于 CLIP 的 0.475。此外，与最佳单 scout 模型相比，Semantic-Drive 的风险评估误差降低了 40%。该系统完全在消费级硬件（NVIDIA RTX 3090）上运行，验证了其在本地部署的可行性。

## 🎯 应用场景

Semantic-Drive 可应用于自动驾驶车辆的训练数据挖掘，帮助快速识别和标注罕见的安全关键事件，提升自动驾驶系统的安全性和可靠性。此外，该方法还可扩展到其他视频监控和分析领域，例如智能交通、安防监控等，具有广泛的应用前景。

## 📄 摘要（原文）

> The development of robust Autonomous Vehicles (AVs) is bottlenecked by the scarcity of "Long-Tail" training data. While fleets collect petabytes of video logs, identifying rare safety-critical events (e.g., erratic jaywalking, construction diversions) remains a manual, cost-prohibitive process. Existing solutions rely on coarse metadata search, which lacks precision, or cloud-based VLMs, which are privacy-invasive and expensive. We introduce Semantic-Drive, a local-first, neuro-symbolic framework for semantic data mining. Our approach decouples perception into two stages: (1) Symbolic Grounding via a real-time open-vocabulary detector (YOLOE) to anchor attention, and (2) Cognitive Analysis via a Reasoning VLM that performs forensic scene analysis. To mitigate hallucination, we implement a "System 2" inference-time alignment strategy, utilizing a multi-model "Judge-Scout" consensus mechanism. Benchmarked on the nuScenes dataset against the Waymo Open Dataset (WOD-E2E) taxonomy, Semantic-Drive achieves a Recall of 0.966 (vs. 0.475 for CLIP) and reduces Risk Assessment Error by 40% ccompared to the best single scout models. The system runs entirely on consumer hardware (NVIDIA RTX 3090), offering a privacy-preserving alternative to the cloud.

