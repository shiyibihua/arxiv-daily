---
layout: default
title: Scaling Laws for Energy Efficiency of Local LLMs
---

# Scaling Laws for Energy Efficiency of Local LLMs

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.16531" class="toolbar-btn" target="_blank">📄 arXiv: 2512.16531v1</a>
  <a href="https://arxiv.org/pdf/2512.16531.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.16531v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.16531v1', 'Scaling Laws for Energy Efficiency of Local LLMs')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Ander Alvarez, Alessandro Genuardi, Nilotpal Sinha, Antonio Tiene, Samuel Mugel, Román Orús

**分类**: cs.AI

**发布日期**: 2025-12-18

---

## 💡 一句话要点

**针对本地LLM，揭示CPU能效缩放规律，并提出量子启发压缩优化方案。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `本地LLM` `CPU推理` `能效优化` `缩放规律` `量子启发压缩`

## 📋 核心要点

1. 现有方法在CPU上部署本地LLM时，缺乏对计算和能耗缩放规律的系统研究，难以优化。
2. 论文通过在主流CPU上进行基准测试，揭示了LLM和VLM在CPU上的计算负载缩放规律。
3. 实验表明，量子启发压缩能显著降低CPU和内存使用，并降低能耗，同时保持或提升语义精度。

## 📝 摘要（中文）

在边缘设备上部署本地大型语言模型和视觉语言模型需要在精度、计算和能源预算之间取得平衡。尽管图形处理器在现代人工智能部署中占据主导地位，但大多数消费级硬件（包括笔记本电脑、台式机、工业控制器和嵌入式系统）依赖于中央处理器。本文系统地对两种广泛用于本地推理的中央处理器进行了基准测试：MacBook Pro M2（主流笔记本电脑级部署）和 Raspberry Pi 5（受限的低功耗嵌入式环境）。通过统一的方法，即连续采样处理器和内存使用情况以及曲线下面积积分，我们描述了语言模型的计算负载如何随输入文本长度缩放，以及视觉语言模型的计算负载如何随图像分辨率缩放。我们发现了两个经验缩放规律：(1) 语言模型推理的计算成本与token长度近似线性缩放；(2) 视觉语言模型表现出由预处理驱动的“分辨率膝点”，即计算量在内部分辨率上限之上保持不变，而在其之下急剧下降。此外，量子启发压缩可将处理器和内存使用量降低高达71.9%，并将能耗降低高达62%，同时保持或提高语义准确性。这些结果系统地量化了多模态中央处理器在本地语言和视觉语言工作负载中的缩放规律，并确定了模型压缩和输入分辨率预处理是可持续边缘推理的有效且低成本的手段。

## 🔬 方法详解

**问题定义**：论文旨在解决在CPU上部署本地大型语言模型（LLM）和视觉语言模型（VLM）时，缺乏对计算资源和能耗需求缩放规律的理解的问题。现有方法主要针对GPU进行优化，忽略了大量依赖CPU的边缘设备，导致在这些设备上部署LLM/VLM时效率低下，难以满足资源约束。

**核心思路**：论文的核心思路是通过系统性的基准测试，量化LLM和VLM在不同CPU平台上的计算负载与输入数据规模（token长度、图像分辨率）之间的关系，从而揭示其缩放规律。此外，探索模型压缩技术，降低资源占用，提升能效。

**技术框架**：论文采用的整体框架包括：
1.  选择代表性的CPU平台：MacBook Pro M2 (笔记本电脑级) 和 Raspberry Pi 5 (嵌入式系统级)。
2.  选择LLM和VLM模型进行测试。
3.  设计统一的基准测试方法：连续采样CPU和内存使用情况，并计算曲线下面积。
4.  分析计算负载与输入数据规模之间的关系，发现缩放规律。
5.  应用量子启发压缩技术，降低模型大小和计算复杂度。

**关键创新**：论文的关键创新在于：
1.  首次系统性地研究了LLM和VLM在CPU上的计算负载缩放规律，填补了该领域的空白。
2.  发现了视觉语言模型中由预处理驱动的“分辨率膝点”现象。
3.  验证了量子启发压缩技术在降低CPU资源占用和能耗方面的有效性。

**关键设计**：
1.  基准测试方法：采用连续采样CPU和内存使用情况，通过曲线下面积积分来量化计算负载。
2.  量子启发压缩：具体压缩算法未知，但强调其在降低模型大小和计算复杂度方面的作用。
3.  实验设计：针对不同模型和平台，设计合理的输入数据规模范围，确保结果的可靠性。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16531v1/figures/updated/llm_mac_cpu_auc.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16531v1/figures/updated/llm_rpi_cpu_auc.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16531v1/figures/updated/vlm_mac_cpu_auc.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

实验结果表明，语言模型推理的计算成本与token长度近似线性缩放；视觉语言模型存在“分辨率膝点”现象。量子启发压缩可将处理器和内存使用量降低高达71.9%，并将能耗降低高达62%，同时保持或提高语义准确性。这些数据突出了模型压缩在边缘设备上的重要性。

## 🎯 应用场景

该研究成果可应用于各种边缘设备上的本地LLM/VLM部署，例如智能家居设备、工业控制器、移动机器人等。通过理解计算负载的缩放规律，可以更好地进行资源分配和模型优化，实现更高效、更节能的本地AI应用。此外，模型压缩技术可以进一步降低部署成本，扩大应用范围。

## 📄 摘要（原文）

> Deploying local large language models and vision-language models on edge devices requires balancing accuracy with constrained computational and energy budgets. Although graphics processors dominate modern artificial-intelligence deployment, most consumer hardware--including laptops, desktops, industrial controllers, and embedded systems--relies on central processing units. Despite this, the computational laws governing central-processing-unit-only inference for local language and vision-language workloads remain largely unexplored. We systematically benchmark large language and vision-language models on two representative central-processing-unit tiers widely used for local inference: a MacBook Pro M2, reflecting mainstream laptop-class deployment, and a Raspberry Pi 5, representing constrained, low-power embedded settings. Using a unified methodology based on continuous sampling of processor and memory usage together with area-under-curve integration, we characterize how computational load scales with input text length for language models and with image resolution for vision-language models. We uncover two empirical scaling laws: (1) computational cost for language-model inference scales approximately linearly with token length; and (2) vision-language models exhibit a preprocessing-driven "resolution knee", where compute remains constant above an internal resolution clamp and decreases sharply below it. Beyond these laws, we show that quantum-inspired compression reduces processor and memory usage by up to 71.9% and energy consumption by up to 62%, while preserving or improving semantic accuracy. These results provide a systematic quantification of multimodal central-processing-unit-only scaling for local language and vision-language workloads, and they identify model compression and input-resolution preprocessing as effective, low-cost levers for sustainable edge inference.

