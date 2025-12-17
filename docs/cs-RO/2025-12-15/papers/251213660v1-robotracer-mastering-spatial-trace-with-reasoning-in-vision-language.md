---
layout: default
title: RoboTracer: Mastering Spatial Trace with Reasoning in Vision-Language Models for Robotics
---

# RoboTracer: Mastering Spatial Trace with Reasoning in Vision-Language Models for Robotics

<div class="paper-toolbar">
  <div class="toolbar-left">
    <a href="https://arxiv.org/abs/2512.13660" target="_blank" class="toolbar-btn">arXiv: 2512.13660v1</a>
    <a href="https://arxiv.org/pdf/2512.13660.pdf" target="_blank" class="toolbar-btn">PDF</a>
  </div>
  <div class="toolbar-right">
    <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.13660v1" 
            onclick="toggleFavorite(this, '2512.13660v1', 'RoboTracer: Mastering Spatial Trace with Reasoning in Vision-Language Models for Robotics')" title="收藏">
      ☆ 收藏
    </button>
    <button class="toolbar-btn share-btn" onclick="copyLink()" title="复制链接">
      🔗 分享
    </button>
  </div>
</div>


**作者**: Enshen Zhou, Cheng Chi, Yibo Li, Jingkun An, Jiayuan Zhang, Shanyu Rong, Yi Han, Yuheng Ji, Mengzhen Liu, Pengwei Wang, Zhongyuan Wang, Lu Sheng, Shanghang Zhang

**分类**: cs.RO, cs.CV

**发布日期**: 2025-12-15

**备注**: Project page: https://zhoues.github.io/RoboTracer

---

## 💡 一句话要点

**RoboTracer：利用视觉-语言模型推理实现机器人空间轨迹追踪**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)**

**关键词**: `机器人` `视觉-语言模型` `空间推理` `轨迹追踪` `强化学习` `3D感知` `度量学习`

## 📋 核心要点

1. 现有机器人空间轨迹追踪方法难以进行多步骤度量推理，且缺乏对复杂空间指代和真实世界度量测量的能力。
2. RoboTracer通过通用空间编码器和回归监督解码器，以及度量敏感的过程奖励强化微调，提升了空间理解和推理能力。
3. 实验表明，RoboTracer在空间理解、测量和指代方面优于基线，并在TraceSpatial-Bench上大幅超越现有SOTA模型。

## 📝 摘要（中文）

本文提出RoboTracer，一个3D感知的视觉-语言模型，旨在提升机器人空间轨迹追踪能力。该模型通过通用空间编码器和回归监督解码器实现3D空间指代和测量，从而增强监督微调（SFT）期间的尺度感知。此外，RoboTracer通过强化微调（RFT）和度量敏感的过程奖励，提升多步度量推理能力，监督关键的中间感知线索，以准确生成空间轨迹。为了支持SFT和RFT训练，本文构建了TraceSpatial，一个包含3000万QA对的大规模数据集，覆盖室外/室内/桌面场景，并支持复杂的推理过程（最多9步）。同时，提出了TraceSpatial-Bench，一个用于评估空间轨迹追踪的基准。实验结果表明，RoboTracer在空间理解、测量和指代方面超越了基线模型，平均成功率为79.1%，并在TraceSpatial-Bench上取得了SOTA性能，超越Gemini-2.5-Pro 36%的准确率。RoboTracer可以与各种控制策略集成，在杂乱的真实场景中执行各种机器人（UR5、G1人形机器人）上的长时程动态任务。

## 🔬 方法详解

**问题定义**：论文旨在解决机器人空间轨迹追踪问题，即让机器人在复杂环境中根据指令进行精确的空间定位和移动。现有方法的痛点在于难以处理多步骤的度量推理，无法准确理解复杂的空间指代，并且缺乏对真实世界尺度信息的感知能力，导致轨迹追踪的精度和鲁棒性不足。

**核心思路**：论文的核心思路是构建一个3D感知的视觉-语言模型RoboTracer，该模型能够同时进行3D空间指代和测量，并通过强化学习的方式提升多步度量推理能力。通过监督微调（SFT）增强尺度感知，并通过强化微调（RFT）监督中间感知线索，从而更准确地生成空间轨迹。

**技术框架**：RoboTracer的整体框架包含以下几个主要模块：1) 通用空间编码器：用于提取场景的3D空间特征；2) 回归监督解码器：用于进行3D空间指代和测量，并增强尺度感知；3) 强化微调模块：使用度量敏感的过程奖励，提升多步度量推理能力。整个流程是，首先通过视觉输入和语言指令，利用空间编码器和解码器进行初步的空间理解和测量，然后通过强化学习不断优化模型的推理能力，最终生成精确的空间轨迹。

**关键创新**：最重要的技术创新点在于将3D空间感知和度量推理能力融入到视觉-语言模型中，并利用强化学习进行优化。与现有方法相比，RoboTracer能够更准确地理解空间关系，进行精确的度量测量，并进行多步骤的推理，从而实现更鲁棒和精确的空间轨迹追踪。

**关键设计**：在SFT阶段，使用回归损失监督解码器的输出，使其能够准确预测3D空间坐标和距离。在RFT阶段，设计了度量敏感的过程奖励，奖励模型在每一步推理中产生的中间感知线索的准确性，例如，中间步骤的定位精度。此外，还构建了大规模数据集TraceSpatial，用于支持SFT和RFT的训练。

## 📊 实验亮点

RoboTracer在TraceSpatial-Bench上取得了显著的性能提升，超越Gemini-2.5-Pro 36%的准确率。在空间理解、测量和指代方面，RoboTracer也优于其他基线模型，平均成功率达到79.1%。此外，RoboTracer能够与多种机器人平台（UR5、G1人形机器人）集成，并在真实的、杂乱的环境中执行长时程动态任务，验证了其在实际应用中的可行性和有效性。

## 🎯 应用场景

RoboTracer在机器人导航、智能制造、自动驾驶、家庭服务等领域具有广泛的应用前景。它可以使机器人在复杂环境中更准确地执行任务，例如，在仓库中进行货物拣选和搬运，在家庭环境中进行清洁和整理，在自动驾驶中进行路径规划和避障。该研究的实际价值在于提升了机器人的自主性和智能化水平，未来有望推动机器人技术在各个领域的普及和应用。

## 📄 摘要（原文）

> Spatial tracing, as a fundamental embodied interaction ability for robots, is inherently challenging as it requires multi-step metric-grounded reasoning compounded with complex spatial referring and real-world metric measurement. However, existing methods struggle with this compositional task. To this end, we propose RoboTracer, a 3D-aware VLM that first achieves both 3D spatial referring and measuring via a universal spatial encoder and a regression-supervised decoder to enhance scale awareness during supervised fine-tuning (SFT). Moreover, RoboTracer advances multi-step metric-grounded reasoning via reinforcement fine-tuning (RFT) with metric-sensitive process rewards, supervising key intermediate perceptual cues to accurately generate spatial traces. To support SFT and RFT training, we introduce TraceSpatial, a large-scale dataset of 30M QA pairs, spanning outdoor/indoor/tabletop scenes and supporting complex reasoning processes (up to 9 steps). We further present TraceSpatial-Bench, a challenging benchmark filling the gap to evaluate spatial tracing. Experimental results show that RoboTracer surpasses baselines in spatial understanding, measuring, and referring, with an average success rate of 79.1%, and also achieves SOTA performance on TraceSpatial-Bench by a large margin, exceeding Gemini-2.5-Pro by 36% accuracy. Notably, RoboTracer can be integrated with various control policies to execute long-horizon, dynamic tasks across diverse robots (UR5, G1 humanoid) in cluttered real-world scenes.

