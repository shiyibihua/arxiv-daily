---
layout: default
title: GeoVista: Web-Augmented Agentic Visual Reasoning for Geolocalization
---

# GeoVista: Web-Augmented Agentic Visual Reasoning for Geolocalization

**arXiv**: [2511.15705v1](https://arxiv.org/abs/2511.15705) | [PDF](https://arxiv.org/pdf/2511.15705.pdf)

**作者**: Yikun Wang, Zuyan Liu, Ziyi Wang, Pengfei Liu, Han Hu, Yongming Rao

**分类**: cs.CV

**发布日期**: 2025-11-19

---

## 💡 一句话要点

**提出GeoVista，一个基于Web增强的Agentic视觉推理模型，用于地理定位任务。**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱二：RL算法与架构 (RL & Architecture)** **支柱三：空间感知 (Perception & SLAM)**

**关键词**: `Agentic模型` `视觉推理` `地理定位` `Web增强` `强化学习`

## 📋 核心要点

1. 现有Agentic视觉推理主要集中于图像操作工具，缺乏面向通用任务的模型，地理定位任务需要细致的视觉理解和Web搜索。
2. GeoVista模型通过集成图像缩放和Web搜索工具，在推理过程中动态获取信息，提升地理定位的准确性。
3. GeoVista在GeoBench基准测试中表现出色，超越了其他开源模型，并能与部分闭源模型相媲美。

## 📝 摘要（中文）

本文针对通用Agentic模型在地理定位任务中的不足，提出了GeoVista模型。该模型集成了图像缩放和Web搜索工具，能够在推理循环中无缝调用，从而实现更精确的地理定位。为了评估Agentic模型在此任务中的能力，作者构建了GeoBench基准数据集，包含全球范围内的照片、全景图以及不同城市的卫星图像。GeoVista的训练流程包括冷启动监督微调（SFT）阶段，用于学习推理模式和工具使用先验，以及强化学习（RL）阶段，以进一步提升推理能力。实验结果表明，GeoVista在地理定位任务上显著优于其他开源Agentic模型，并在大多数指标上达到了与Gemini-2.5-flash和GPT-5等闭源模型相当的性能。

## 🔬 方法详解

**问题定义**：现有的Agentic视觉推理模型主要关注图像处理任务，缺乏解决通用任务的能力。地理定位任务需要模型具备细致的视觉理解能力，并能通过外部知识（如Web搜索）来验证或修正假设。现有的地理定位基准数据集难以满足深度Agentic推理对高分辨率图像和定位挑战的需求。

**核心思路**：GeoVista的核心思路是将工具调用无缝集成到Agentic模型的推理循环中。通过引入图像缩放工具和Web搜索工具，模型可以在推理过程中动态地放大感兴趣区域，并检索相关的Web信息，从而提升地理定位的准确性。这种设计模拟了人类在进行地理定位时的思考过程，即观察图像细节、查阅地图或相关资料。

**技术框架**：GeoVista的整体架构包含一个Agentic模型，该模型可以调用图像缩放工具和Web搜索工具。训练流程分为两个阶段：首先是冷启动监督微调（SFT）阶段，使用标注数据训练模型学习推理模式和工具使用先验知识；然后是强化学习（RL）阶段，使用分层奖励函数进一步提升模型的推理能力。分层奖励函数利用多层次的地理信息，例如国家、城市、地标等，来指导模型的学习。

**关键创新**：GeoVista的关键创新在于将工具调用与Agentic模型的推理过程紧密结合，形成一个闭环的推理系统。与传统的Agentic模型相比，GeoVista能够主动地利用外部信息来辅助推理，从而提升了模型的泛化能力和鲁棒性。此外，GeoBench数据集的构建也为Agentic模型在地理定位任务上的研究提供了新的基准。

**关键设计**：在SFT阶段，使用了标注数据来训练模型，学习工具的使用方式和推理模式。在RL阶段，采用了分层奖励函数，根据模型预测的地理位置与真实位置的接近程度，给予不同层次的奖励。图像缩放工具和Web搜索工具的具体实现细节未在论文中详细描述，但可以推测图像缩放工具可能基于图像处理算法，Web搜索工具可能调用现有的搜索引擎API。

## 📊 实验亮点

GeoVista在GeoBench基准测试中取得了显著的成果，大幅超越了其他开源Agentic模型。在某些指标上，GeoVista的性能甚至可以与Gemini-2.5-flash和GPT-5等闭源模型相媲美。这些实验结果表明，GeoVista在地理定位任务上具有很强的竞争力。

## 🎯 应用场景

GeoVista具有广泛的应用前景，例如智能旅游、自动驾驶、灾害救援、城市规划等。该模型可以帮助用户快速定位图像或视频的拍摄地点，为相关应用提供地理信息支持。未来，GeoVista可以进一步扩展到其他需要视觉推理和外部知识的任务中，例如目标检测、图像描述等。

## 📄 摘要（原文）

> Current research on agentic visual reasoning enables deep multimodal understanding but primarily focuses on image manipulation tools, leaving a gap toward more general-purpose agentic models. In this work, we revisit the geolocalization task, which requires not only nuanced visual grounding but also web search to confirm or refine hypotheses during reasoning. Since existing geolocalization benchmarks fail to meet the need for high-resolution imagery and the localization challenge for deep agentic reasoning, we curate GeoBench, a benchmark that includes photos and panoramas from around the world, along with a subset of satellite images of different cities to rigorously evaluate the geolocalization ability of agentic models. We also propose GeoVista, an agentic model that seamlessly integrates tool invocation within the reasoning loop, including an image-zoom-in tool to magnify regions of interest and a web-search tool to retrieve related web information. We develop a complete training pipeline for it, including a cold-start supervised fine-tuning (SFT) stage to learn reasoning patterns and tool-use priors, followed by a reinforcement learning (RL) stage to further enhance reasoning ability. We adopt a hierarchical reward to leverage multi-level geographical information and improve overall geolocalization performance. Experimental results show that GeoVista surpasses other open-source agentic models on the geolocalization task greatly and achieves performance comparable to closed-source models such as Gemini-2.5-flash and GPT-5 on most metrics.

