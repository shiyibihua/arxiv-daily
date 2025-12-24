---
layout: default
title: Autonomous Navigation of Cloud-Controlled Quadcopters in Confined Spaces Using Multi-Modal Perception and LLM-Driven High Semantic Reasoning
---

# Autonomous Navigation of Cloud-Controlled Quadcopters in Confined Spaces Using Multi-Modal Perception and LLM-Driven High Semantic Reasoning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.07885" class="toolbar-btn" target="_blank">📄 arXiv: 2508.07885v1</a>
  <a href="https://arxiv.org/pdf/2508.07885.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.07885v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.07885v1', 'Autonomous Navigation of Cloud-Controlled Quadcopters in Confined Spaces Using Multi-Modal Perception and LLM-Driven High Semantic Reasoning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Shoaib Ahmmad, Zubayer Ahmed Aditto, Md Mehrab Hossain, Noushin Yeasmin, Shorower Hossain

**分类**: cs.RO, cs.AI, cs.CV, eess.SY

**发布日期**: 2025-08-11

---

## 💡 一句话要点

**提出云控制四旋翼自主导航系统以解决GPS缺失环境中的导航问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱三：空间感知与语义 (Perception & Semantics)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `自主导航` `四旋翼无人机` `多模态感知` `云计算` `深度学习` `安全包` `室内环境` `语义推理`

## 📋 核心要点

1. 现有的无人机导航方法在GPS缺失的室内环境中面临挑战，尤其是在狭小空间中的导航精度和安全性。
2. 本文提出了一种基于云计算的多模态感知系统，结合YOLOv11、深度估计和LLM进行高语义推理，以实现自主导航。
3. 实验结果显示，该系统在物体检测和深度估计方面表现优异，且在多次试验中安全包违规次数极少，系统延迟低于1秒。

## 📝 摘要（中文）

本文介绍了一种先进的AI驱动感知系统，用于在GPS缺失的室内环境中实现四旋翼自主导航。该框架利用云计算卸载计算密集型任务，并结合定制设计的印刷电路板（PCB）以高效获取传感器数据，从而在狭小空间中实现稳健导航。系统集成了YOLOv11进行物体检测、Depth Anything V2进行单目深度估计、配备飞行时间（ToF）传感器和惯性测量单元（IMU）的PCB，以及基于云的大型语言模型（LLM）进行上下文感知决策。通过校准的传感器偏移量强制执行的虚拟安全包确保了碰撞避免，同时多线程架构实现了低延迟处理。实验结果表明，在室内测试平台上，物体检测的平均精度（mAP50）达到0.6，深度估计的平均绝对误差（MAE）为7.2厘米，在42次试验中仅发生16次安全包违规，系统的端到端延迟低于1秒。该云支持的高智能框架作为辅助感知和导航系统，补充了GPS缺失的狭小空间中的无人机自主性。

## 🔬 方法详解

**问题定义**：本文旨在解决在GPS缺失的室内环境中，四旋翼无人机的自主导航问题。现有方法在狭小空间中导航时，往往面临感知精度不足和碰撞风险高的挑战。

**核心思路**：论文提出的解决方案是利用云计算和多模态感知技术，结合深度学习模型和传感器数据，增强无人机的环境感知能力和决策能力。通过将计算密集型任务卸载到云端，提升了系统的实时性和智能性。

**技术框架**：整体架构包括多个模块：首先，使用YOLOv11进行物体检测，接着通过Depth Anything V2进行深度估计，利用PCB收集传感器数据，最后通过云端的LLM进行上下文感知决策。系统还实现了虚拟安全包以确保安全导航。

**关键创新**：最重要的技术创新在于将云计算与多模态感知相结合，利用LLM进行高层次的语义推理，从而显著提升了无人机在复杂环境中的自主导航能力。与传统方法相比，该方法在处理复杂场景时表现出更高的灵活性和安全性。

**关键设计**：系统设计中，PCB集成了ToF传感器和IMU，以提高数据采集的效率和准确性。采用的损失函数和网络结构经过精心调整，以优化物体检测和深度估计的性能。

## 📊 实验亮点

实验结果显示，物体检测的平均精度（mAP50）达到0.6，深度估计的平均绝对误差（MAE）为7.2厘米。在42次试验中，仅发生16次安全包违规，且系统的端到端延迟低于1秒，展示了该系统在复杂环境中的优越性能。

## 🎯 应用场景

该研究的潜在应用领域包括室内无人机配送、搜索与救援、以及工业自动化等场景。通过提高无人机在复杂环境中的自主导航能力，能够显著提升其在实际应用中的安全性和效率，未来可能推动无人机技术的广泛应用。

## 📄 摘要（原文）

> This paper introduces an advanced AI-driven perception system for autonomous quadcopter navigation in GPS-denied indoor environments. The proposed framework leverages cloud computing to offload computationally intensive tasks and incorporates a custom-designed printed circuit board (PCB) for efficient sensor data acquisition, enabling robust navigation in confined spaces. The system integrates YOLOv11 for object detection, Depth Anything V2 for monocular depth estimation, a PCB equipped with Time-of-Flight (ToF) sensors and an Inertial Measurement Unit (IMU), and a cloud-based Large Language Model (LLM) for context-aware decision-making. A virtual safety envelope, enforced by calibrated sensor offsets, ensures collision avoidance, while a multithreaded architecture achieves low-latency processing. Enhanced spatial awareness is facilitated by 3D bounding box estimation with Kalman filtering. Experimental results in an indoor testbed demonstrate strong performance, with object detection achieving a mean Average Precision (mAP50) of 0.6, depth estimation Mean Absolute Error (MAE) of 7.2 cm, only 16 safety envelope breaches across 42 trials over approximately 11 minutes, and end-to-end system latency below 1 second. This cloud-supported, high-intelligence framework serves as an auxiliary perception and navigation system, complementing state-of-the-art drone autonomy for GPS-denied confined spaces.

