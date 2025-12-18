---
layout: default
title: Vehicle-to-Infrastructure Collaborative Spatial Perception via Multimodal Large Language Models
---

# Vehicle-to-Infrastructure Collaborative Spatial Perception via Multimodal Large Language Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.03837" class="toolbar-btn" target="_blank">📄 arXiv: 2509.03837v1</a>
  <a href="https://arxiv.org/pdf/2509.03837.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.03837v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.03837v1', 'Vehicle-to-Infrastructure Collaborative Spatial Perception via Multimodal Large Language Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Kimia Ehsani, Walid Saad

**分类**: cs.LG, cs.IT

**发布日期**: 2025-09-04

**备注**: Accepted at IEEE GLOBECOM 2025

---

## 💡 一句话要点

**提出基于BEV注入的多模态大语言模型，提升V2I通信链路质量预测精度。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `车路协同` `多模态大语言模型` `鸟瞰图` `链路质量预测` `空间感知`

## 📋 核心要点

1. 现有V2I通信链路质量预测方法难以有效利用车辆传感器数据，且大语言模型缺乏空间理解能力。
2. 提出一种BEV注入框架，融合相邻车辆感知数据构建环境鸟瞰图，为MLLM提供空间上下文信息。
3. 实验表明，该框架在各种V2I链路预测任务中均有显著提升，尤其在恶劣天气下表现出更强的鲁棒性。

## 📝 摘要（中文）

精确预测通信链路质量指标对于车路协同（V2I）系统至关重要，它能实现平滑切换、高效波束管理和可靠的低延迟通信。现代车辆传感器数据的日益普及促使人们使用多模态大语言模型（MLLM），因为它们具有跨任务适应性和推理能力。然而，MLLM 本身缺乏三维空间理解。为了克服这个限制，本文提出了一种轻量级的、即插即用的鸟瞰图（BEV）注入连接器。在该框架中，通过收集相邻车辆的感知数据来构建环境的 BEV。然后，将此 BEV 表示与自车输入融合，从而为大语言模型提供空间上下文。为了支持真实的多模态学习，开发了一个结合 CARLA 模拟器和基于 MATLAB 的射线追踪的联合仿真环境，以生成各种场景下的 RGB、LiDAR、GPS 和无线信号数据。指令和真实响应以编程方式从射线追踪输出中提取。在三个 V2I 链路预测任务（视距（LoS）与非视距（NLoS）分类、链路可用性和阻塞预测）上进行了广泛的实验。仿真结果表明，所提出的 BEV 注入框架始终提高了所有任务的性能。结果表明，与仅使用自车的基线相比，所提出的方法将准确率指标的宏平均值提高了高达 13.9%。结果还表明，在具有挑战性的雨天和夜间条件下，这种性能提升高达 32.7%，证实了该框架在不利环境中的鲁棒性。

## 🔬 方法详解

**问题定义**：论文旨在解决V2I通信中准确预测链路质量的问题，现有方法难以有效利用车辆传感器数据，且大语言模型（LLM）本身缺乏对三维空间信息的理解，导致预测精度受限。尤其是在复杂环境和恶劣天气条件下，预测性能会显著下降。

**核心思路**：论文的核心思路是通过构建环境的鸟瞰图（BEV），为大语言模型提供丰富的空间上下文信息。通过融合自车和周围车辆的感知数据，生成BEV表示，从而弥补LLM在空间理解方面的不足。这种方法能够使LLM更好地理解车辆周围的环境，从而更准确地预测链路质量。

**技术框架**：整体框架包含以下几个主要模块：1) 数据采集：通过CARLA模拟器和MATLAB射线追踪联合仿真环境，生成RGB、LiDAR、GPS和无线信号数据。2) BEV构建：利用相邻车辆的感知数据构建环境的鸟瞰图。3) 多模态融合：将BEV表示与自车输入融合，形成包含空间信息的输入。4) MLLM预测：将融合后的数据输入多模态大语言模型，进行链路质量预测。5) 评估：根据射线追踪输出提取的ground truth，评估预测结果。

**关键创新**：该论文的关键创新在于提出了一个轻量级的、即插即用的BEV注入连接器，能够有效地将空间信息融入到大语言模型中。与传统的直接使用LLM进行预测的方法相比，该方法能够显著提高预测精度，尤其是在恶劣天气条件下。此外，联合仿真环境的构建也为多模态学习提供了realistic的数据支持。

**关键设计**：BEV的构建方式是关键设计之一，论文中具体如何构建BEV，以及如何进行多模态融合的细节未详细描述。损失函数的设计也未提及。网络结构方面，采用了MLLM，但具体模型选择和参数设置未知。

## 📊 实验亮点

实验结果表明，所提出的BEV注入框架在视距/非视距分类、链路可用性和阻塞预测等V2I链路预测任务中均取得了显著提升。与仅使用自车的基线相比，准确率指标的宏平均值提高了高达13.9%。在雨天和夜间等恶劣条件下，性能提升高达32.7%，验证了该框架的鲁棒性。

## 🎯 应用场景

该研究成果可应用于智能交通系统、自动驾驶、车路协同等领域。通过提升V2I通信链路质量预测的准确性，可以优化资源分配、提高通信效率、降低延迟，从而改善用户体验，并为自动驾驶车辆提供更可靠的环境感知。

## 📄 摘要（原文）

> Accurate prediction of communication link quality metrics is essential for vehicle-to-infrastructure (V2I) systems, enabling smooth handovers, efficient beam management, and reliable low-latency communication. The increasing availability of sensor data from modern vehicles motivates the use of multimodal large language models (MLLMs) because of their adaptability across tasks and reasoning capabilities. However, MLLMs inherently lack three-dimensional spatial understanding. To overcome this limitation, a lightweight, plug-and-play bird's-eye view (BEV) injection connector is proposed. In this framework, a BEV of the environment is constructed by collecting sensing data from neighboring vehicles. This BEV representation is then fused with the ego vehicle's input to provide spatial context for the large language model. To support realistic multimodal learning, a co-simulation environment combining CARLA simulator and MATLAB-based ray tracing is developed to generate RGB, LiDAR, GPS, and wireless signal data across varied scenarios. Instructions and ground-truth responses are programmatically extracted from the ray-tracing outputs. Extensive experiments are conducted across three V2I link prediction tasks: line-of-sight (LoS) versus non-line-of-sight (NLoS) classification, link availability, and blockage prediction. Simulation results show that the proposed BEV injection framework consistently improved performance across all tasks. The results indicate that, compared to an ego-only baseline, the proposed approach improves the macro-average of the accuracy metrics by up to 13.9%. The results also show that this performance gain increases by up to 32.7% under challenging rainy and nighttime conditions, confirming the robustness of the framework in adverse settings.

