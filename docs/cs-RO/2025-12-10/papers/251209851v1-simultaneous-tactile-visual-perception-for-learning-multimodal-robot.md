---
layout: default
title: Simultaneous Tactile-Visual Perception for Learning Multimodal Robot Manipulation
---

# Simultaneous Tactile-Visual Perception for Learning Multimodal Robot Manipulation

<div class="paper-toolbar">
  <div class="toolbar-left">
    <a href="https://arxiv.org/abs/2512.09851" target="_blank" class="toolbar-btn">arXiv: 2512.09851v1</a>
    <a href="https://arxiv.org/pdf/2512.09851.pdf" target="_blank" class="toolbar-btn">PDF</a>
  </div>
  <div class="toolbar-right">
    <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.09851v1" 
            onclick="toggleFavorite(this, '2512.09851v1', 'Simultaneous Tactile-Visual Perception for Learning Multimodal Robot Manipulation')" title="收藏">
      ☆ 收藏
    </button>
    <button class="toolbar-btn share-btn" onclick="copyLink()" title="复制链接">
      🔗 分享
    </button>
  </div>
</div>


**作者**: Yuyang Li, Yinghan Chen, Zihang Zhao, Puhao Li, Tengyu Liu, Siyuan Huang, Yixin Zhu

**分类**: cs.RO, cs.CV

**发布日期**: 2025-12-10

---

## 💡 一句话要点

**提出TacThru-UMI，结合新型触觉视觉传感器与Transformer扩散策略，提升机器人操作精度。**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `机器人操作` `触觉感知` `视觉感知` `多模态融合` `模仿学习`

## 📋 核心要点

1. 现有透皮视觉传感器缺乏同步多模态感知能力，触觉跟踪的可靠性不足，限制了机器人操作的精度。
2. TacThru-UMI结合新型STS传感器TacThru和Transformer扩散策略，实现同步触觉视觉感知和精确操作。
3. 实验表明，TacThru-UMI在多个真实操作任务中显著优于传统方法，平均成功率提升至85.5%。

## 📝 摘要（中文）

机器人操作需要丰富的多模态感知和有效的学习框架来处理复杂的现实世界任务。透皮视觉（STS）传感器结合了触觉和视觉感知，提供了有前景的传感能力，而现代模仿学习为策略获取提供了强大的工具。然而，现有的STS设计缺乏同步多模态感知，并且存在不可靠的触觉跟踪问题。此外，将这些丰富的多模态信号集成到基于学习的操作流程中仍然是一个公开的挑战。我们介绍了TacThru，一种能够实现同步视觉感知和鲁棒触觉信号提取的STS传感器，以及TacThru-UMI，一种利用这些多模态信号进行操作的模仿学习框架。我们的传感器具有完全透明的弹性体、持久照明、新型关键线标记和高效跟踪，而我们的学习系统通过基于Transformer的扩散策略集成这些信号。在五个具有挑战性的现实世界任务中的实验表明，TacThru-UMI实现了平均85.5%的成功率，显著优于交替触觉视觉（66.3%）和仅视觉（55.4%）的基线。该系统在关键场景中表现出色，包括薄而软物体的接触检测以及需要多模态协调的精确操作。这项工作表明，将同步多模态感知与现代学习框架相结合，可以实现更精确、更具适应性的机器人操作。

## 🔬 方法详解

**问题定义**：论文旨在解决机器人操作中，由于传感器感知能力不足和学习框架无法有效融合多模态信息，导致操作精度和适应性受限的问题。现有方法，如交替使用触觉和视觉信息，或仅依赖视觉信息，无法充分利用触觉提供的接触信息，尤其是在处理薄、软物体或需要精细操作的场景下，表现不佳。

**核心思路**：论文的核心思路是设计一种新型的透皮视觉（STS）传感器TacThru，能够同时提供高质量的视觉和触觉信息，并通过一个基于Transformer的扩散策略TacThru-UMI，将这些多模态信息有效地融合到机器人操作的学习过程中。通过同步感知和多模态融合，提高机器人对环境的理解和操作的精度。

**技术框架**：TacThru-UMI的整体框架包含两个主要部分：TacThru传感器和Transformer扩散策略。TacThru传感器负责采集同步的视觉和触觉信息，包括通过透明弹性体获取的视觉图像和通过关键线标记跟踪得到的触觉信息。这些信息被输入到Transformer扩散策略中，该策略学习从多模态数据到机器人动作的映射。整个流程包括数据采集、传感器信号处理、策略学习和机器人控制等阶段。

**关键创新**：论文的关键创新在于TacThru传感器的设计和TacThru-UMI学习框架的构建。TacThru传感器通过完全透明的弹性体、持久照明和新型关键线标记，实现了同步、鲁棒的视觉和触觉感知。TacThru-UMI学习框架则利用Transformer的强大建模能力，有效地融合了视觉和触觉信息，从而提高了机器人操作的精度和适应性。与现有方法的本质区别在于，TacThru-UMI能够同时利用视觉和触觉信息进行决策，而不是交替使用或仅依赖视觉信息。

**关键设计**：TacThru传感器采用完全透明的弹性体，以减少视觉遮挡。关键线标记被设计成易于跟踪和区分的形状，并使用高效的跟踪算法进行处理。Transformer扩散策略使用Transformer编码器来提取视觉和触觉特征，并使用扩散模型来生成机器人动作。损失函数包括模仿学习损失和正则化项，以提高策略的泛化能力。具体的网络结构和参数设置在论文中有详细描述。

## 📊 实验亮点

实验结果表明，TacThru-UMI在五个具有挑战性的现实世界任务中，平均成功率达到85.5%，显著优于交替触觉视觉（66.3%）和仅视觉（55.4%）的基线方法。尤其是在处理薄而软的物体以及需要精确操作的场景中，TacThru-UMI表现出明显的优势，证明了同步多模态感知和学习框架的有效性。

## 🎯 应用场景

该研究成果可应用于各种需要精细操作和环境感知的机器人任务中，例如医疗手术机器人、精密装配机器人、以及在复杂环境中进行操作的机器人。通过提供更精确的感知和更智能的控制，该技术有望提高机器人操作的效率和安全性，并扩展机器人的应用范围。

## 📄 摘要（原文）

> Robotic manipulation requires both rich multimodal perception and effective learning frameworks to handle complex real-world tasks. See-through-skin (STS) sensors, which combine tactile and visual perception, offer promising sensing capabilities, while modern imitation learning provides powerful tools for policy acquisition. However, existing STS designs lack simultaneous multimodal perception and suffer from unreliable tactile tracking. Furthermore, integrating these rich multimodal signals into learning-based manipulation pipelines remains an open challenge. We introduce TacThru, an STS sensor enabling simultaneous visual perception and robust tactile signal extraction, and TacThru-UMI, an imitation learning framework that leverages these multimodal signals for manipulation. Our sensor features a fully transparent elastomer, persistent illumination, novel keyline markers, and efficient tracking, while our learning system integrates these signals through a Transformer-based Diffusion Policy. Experiments on five challenging real-world tasks show that TacThru-UMI achieves an average success rate of 85.5%, significantly outperforming the baselines of alternating tactile-visual (66.3%) and vision-only (55.4%). The system excels in critical scenarios, including contact detection with thin and soft objects and precision manipulation requiring multimodal coordination. This work demonstrates that combining simultaneous multimodal perception with modern learning frameworks enables more precise, adaptable robotic manipulation.

