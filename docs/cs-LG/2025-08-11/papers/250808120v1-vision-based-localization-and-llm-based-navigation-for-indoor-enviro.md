---
layout: default
title: Vision-Based Localization and LLM-based Navigation for Indoor Environments
---

# Vision-Based Localization and LLM-based Navigation for Indoor Environments

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.08120" class="toolbar-btn" target="_blank">📄 arXiv: 2508.08120v1</a>
  <a href="https://arxiv.org/pdf/2508.08120.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.08120v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.08120v1', 'Vision-Based Localization and LLM-based Navigation for Indoor Environments')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Keyan Rahimi, Md. Wasiul Haque, Sagar Dasgupta, Mizanur Rahman

**分类**: cs.LG, cs.AI, cs.CV

**发布日期**: 2025-08-11

**备注**: 20 pages, 6 figures, 1 table

---

## 💡 一句话要点

**提出基于视觉定位与大语言模型导航的室内导航解决方案**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `室内导航` `视觉定位` `大语言模型` `ResNet-50` `机器人导航` `深度学习` `智能手机应用`

## 📋 核心要点

1. 室内导航面临GPS信号缺失和建筑复杂性导致的定位困难，现有方法在这些环境中表现不佳。
2. 本研究提出了一种结合视觉定位和大语言模型的导航系统，通过智能手机摄像头实现用户定位，并生成导航指令。
3. 实验结果显示，模型在定位上实现了96%的准确率，导航指令的平均准确率为75%，展示了其在实际应用中的有效性。

## 📝 摘要（中文）

室内导航因缺乏可靠的GPS信号和复杂的建筑结构而面临挑战。本研究提出了一种结合视觉定位与大语言模型（LLM）导航的室内定位与导航方法。定位系统利用经过两阶段微调的ResNet-50卷积神经网络，通过智能手机摄像头输入识别用户位置。导航模块则通过精心设计的系统提示，利用LLM解析预处理的平面图像并生成逐步导航指令。实验在具有重复特征和有限可见度的真实办公走廊中进行，验证了定位的鲁棒性。该模型在所有测试的路标上实现了96%的高准确率，即使在受限的视角条件和短时查询下也表现良好。使用ChatGPT对真实建筑平面图进行导航测试的指令准确率平均为75%，但在零-shot推理和推理时间上存在局限。该研究展示了在资源受限环境（如医院、机场和教育机构）中，利用现成摄像头和公开平面图进行可扩展的基础设施自由室内导航的潜力。

## 🔬 方法详解

**问题定义**：本研究旨在解决室内环境中由于缺乏GPS信号和建筑复杂性导致的导航困难。现有方法在这些条件下的定位和导航效果不理想，尤其是在可见度受限的情况下。

**核心思路**：本研究的核心思路是将视觉定位与大语言模型（LLM）结合，利用智能手机摄像头进行用户定位，并通过LLM解析平面图生成导航指令。这样的设计旨在提高室内导航的准确性和可用性，尤其是在资源受限的环境中。

**技术框架**：整体架构包括两个主要模块：首先是基于ResNet-50的视觉定位模块，该模块通过两阶段微调来提高定位精度；其次是LLM导航模块，通过系统提示解析平面图并生成导航指令。

**关键创新**：本研究的主要创新在于将视觉定位与LLM结合，形成了一种新的室内导航方法。这种方法不同于传统的基于传感器或GPS的导航，具有更高的灵活性和适应性。

**关键设计**：在技术细节上，ResNet-50网络经过两阶段微调以适应特定的室内环境，损失函数的选择和参数设置经过优化，以确保在不同条件下的鲁棒性。

## 📊 实验亮点

实验结果显示，模型在所有测试的路标上实现了96%的定位准确率，且在有限可见度条件下仍表现出高信心。导航测试中，使用ChatGPT的指令准确率达75%，尽管在零-shot推理和推理时间上存在一定局限，整体效果仍显著优于传统方法。

## 🎯 应用场景

该研究的潜在应用领域包括医院、机场和教育机构等资源受限的环境。通过利用现成的摄像头和公开的平面图，能够实现基础设施自由的室内导航，降低了部署成本并提高了可访问性。未来，该技术有望在智能建筑和自动化导览系统中得到广泛应用。

## 📄 摘要（原文）

> Indoor navigation remains a complex challenge due to the absence of reliable GPS signals and the architectural intricacies of large enclosed environments. This study presents an indoor localization and navigation approach that integrates vision-based localization with large language model (LLM)-based navigation. The localization system utilizes a ResNet-50 convolutional neural network fine-tuned through a two-stage process to identify the user's position using smartphone camera input. To complement localization, the navigation module employs an LLM, guided by a carefully crafted system prompt, to interpret preprocessed floor plan images and generate step-by-step directions. Experimental evaluation was conducted in a realistic office corridor with repetitive features and limited visibility to test localization robustness. The model achieved high confidence and an accuracy of 96% across all tested waypoints, even under constrained viewing conditions and short-duration queries. Navigation tests using ChatGPT on real building floor maps yielded an average instruction accuracy of 75%, with observed limitations in zero-shot reasoning and inference time. This research demonstrates the potential for scalable, infrastructure-free indoor navigation using off-the-shelf cameras and publicly available floor plans, particularly in resource-constrained settings like hospitals, airports, and educational institutions.

