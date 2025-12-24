---
layout: default
title: Edge-Based Multimodal Sensor Data Fusion with Vision Language Models (VLMs) for Real-time Autonomous Vehicle Accident Avoidance
---

# Edge-Based Multimodal Sensor Data Fusion with Vision Language Models (VLMs) for Real-time Autonomous Vehicle Accident Avoidance

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.01057" class="toolbar-btn" target="_blank">📄 arXiv: 2508.01057v2</a>
  <a href="https://arxiv.org/pdf/2508.01057.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.01057v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.01057v2', 'Edge-Based Multimodal Sensor Data Fusion with Vision Language Models (VLMs) for Real-time Autonomous Vehicle Accident Avoidance')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Fengze Yang, Bo Yu, Yang Zhou, Xuewen Luo, Zhengzhong Tu, Chenxi Liu

**分类**: cs.AI, cs.RO

**发布日期**: 2025-08-01 (更新: 2025-08-12)

**备注**: 24 pages, 6 tables, 7 figures

---

## 💡 一句话要点

**提出REACT框架以解决自动驾驶实时碰撞避免问题**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `自动驾驶` `多模态融合` `视觉语言模型` `实时推理` `轨迹优化` `边缘计算` `交通安全`

## 📋 核心要点

1. 现有自动驾驶方法在复杂交通环境中难以实现有效的多模态数据融合与实时推理，导致碰撞风险增加。
2. 本文提出REACT框架，通过集成基础设施警报与车载传感器数据，利用轻量级视觉语言模型进行轨迹优化。
3. REACT在DeepAccident基准上表现出色，碰撞率降低77%，视频全景质量达到48.2%，推理延迟仅为0.57秒。

## 📝 摘要（中文）

自动驾驶系统仅依赖车载传感器可能无法探测远处或障碍物，导致可避免的碰撞。现有的基于变换器的车联网（V2X）方法在多模态融合和推理方面存在不足，或在复杂的高维交通条件下难以满足实时性能要求。本文提出了一种基于轻量级视觉语言模型（VLM）的实时边缘自主副驾驶轨迹规划器（REACT），该框架集成了基础设施提供的危险警报与车载传感器数据，通过视觉嵌入捕捉周围交通动态和车辆意图，利用上下文推理生成优化的安全轨迹。REACT在DeepAccident基准上评估，取得了77%的碰撞率降低和0.57秒的推理延迟，验证了轻量级VLM在边缘平台上实现实时协同规划的有效性。

## 🔬 方法详解

**问题定义**：本文旨在解决自动驾驶系统在复杂交通环境中对远处障碍物探测不足的问题，现有方法在多模态数据融合和实时推理方面存在显著不足。

**核心思路**：REACT框架通过结合基础设施提供的危险警报与车载传感器数据，利用轻量级视觉语言模型（VLM）进行上下文推理和轨迹优化，以提高安全性和实时性。

**技术框架**：REACT的整体架构包括数据采集模块、视觉嵌入生成模块、上下文推理模块和轨迹优化模块，确保在边缘设备上高效运行。

**关键创新**：REACT的主要创新在于采用了残差轨迹融合（RTF）设计和专门的边缘适应策略，显著降低了模型复杂性并提升了推理效率。

**关键设计**：在模型设计中，采用了轻量级的网络结构，优化了损失函数以平衡安全性与效率，同时通过边缘适应策略确保模型在实时环境中的有效性。

## 📊 实验亮点

REACT在DeepAccident基准测试中表现优异，达到了77%的碰撞率降低，视频全景质量（VPQ）为48.2%，推理延迟仅为0.57秒，显示出其在实时自动驾驶应用中的强大性能。

## 🎯 应用场景

该研究的潜在应用领域包括自动驾驶车辆的实时碰撞避免系统、智能交通管理和车联网（V2X）系统。通过提高交通安全性和响应速度，REACT框架能够显著降低交通事故发生率，具有重要的实际价值和社会影响。

## 📄 摘要（原文）

> Autonomous driving (AD) systems relying solely on onboard sensors may fail to detect distant or obstacle hazards, potentially causing preventable collisions; however, existing transformer-based Vehicle-to-Everything (V2X) approaches, which mitigate AD sensing limitations, either lack effective multimodal fusion and reasoning or struggle to meet real-time performance requirements under complex, high-dimensional traffic conditions. This paper proposes the Real-time Edge-based Autonomous Co-pilot Trajectory planner (REACT), a V2X-integrated trajectory optimization framework for AD based on a fine-tuned lightweight Vision-Language Model (VLM). REACT integrates infrastructure-provided hazard alerts with onboard sensor data, capturing intricate surrounding traffic dynamics and vehicle intents through visual embeddings, interpreting precise numerical data from symbolic inputs, and employing contextual reasoning to generate optimized, safety-oriented trajectories. To ensure robust real-time deployment on edge devices, REACT innovatively employs Residual Trajectory Fusion (RTF) design and specialized edge-adaptation strategies to reduce model complexity and improve inference efficiency. Evaluated on the DeepAccident benchmark, REACT achieves state-of-the-art performance, a 77% collision rate reduction, a 48.2% Video Panoptic Quality (VPQ), and a 0.57-second inference latency on the Jetson AGX Orin. Ablation studies validate the contribution of each input, module, and edge adaptation strategy. These results highlight the effectiveness of lightweight VLMs in enabling real-time cooperative planning on edge platforms and underscore the potential of language-guided contextual reasoning for improving traffic safety and responsiveness.

