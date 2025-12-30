---
layout: default
title: Automated river gauge plate reading using a hybrid object detection and generative AI framework in the Limpopo River Basin
---

# Automated river gauge plate reading using a hybrid object detection and generative AI framework in the Limpopo River Basin

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.23454" class="toolbar-btn" target="_blank">📄 arXiv: 2512.23454v1</a>
  <a href="https://arxiv.org/pdf/2512.23454.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.23454v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.23454v1', 'Automated river gauge plate reading using a hybrid object detection and generative AI framework in the Limpopo River Basin')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Kayathri Vigneswaran, Hugo Retief, Jai Clifford Holmes, Mariangel Garcia Andarcia, Hansaka Tennakoon

**分类**: cs.CV

**发布日期**: 2025-12-29

**备注**: 11 pages, 14 figures, 4 tables

---

## 💡 一句话要点

**提出混合AI框架，用于利姆波波河流域自动读取水位标尺**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `水位监测` `河流标尺` `计算机视觉` `YOLOv8` `多模态学习` `大型语言模型` `水资源管理`

## 📋 核心要点

1. 传统人工测量水位存在误差和环境限制，难以满足洪水预报和水资源管理的需求。
2. 提出结合视觉水线检测、YOLOv8姿态估计和大型多模态语言模型的混合框架，实现自动水位标尺读取。
3. 实验表明，该方法在水线检测和刻度估计方面表现出色，结合几何元数据显著提升了LLM的预测精度。

## 📝 摘要（中文）

本文提出了一种混合框架，该框架集成了基于视觉的水线检测、YOLOv8姿态尺度提取以及大型多模态语言模型（GPT 4o和Gemini 2.0 Flash），用于自动读取河流标尺。该方法包括图像预处理、标注、水线检测、刻度间隙估计和数值读取提取等阶段。实验表明，水线检测实现了94.24%的高精度和83.64%的F1分数，而刻度间隙检测为后续的读数提取提供了精确的几何校准。结合刻度间隙元数据显著提高了LLM的预测性能，其中Gemini Stage 2在最佳图像条件下实现了最高的准确率，平均绝对误差为5.43厘米，均方根误差为8.58厘米，R平方为0.84。结果表明，LLM对图像质量敏感，图像质量下降会导致更高的误差，并强调了将几何元数据与多模态人工智能相结合以实现稳健的水位估计的重要性。总的来说，该方法为自动水文监测提供了一种可扩展、高效且可靠的解决方案，展示了实时河流标尺数字化和改进水资源管理的潜力。

## 🔬 方法详解

**问题定义**：论文旨在解决传统人工测量河流标尺水位存在的误差大、效率低以及难以实时监测的问题。现有方法依赖人工读数，易受主观因素和环境条件的影响，无法满足现代水资源管理和防洪预警的需求。

**核心思路**：论文的核心思路是将计算机视觉技术与大型多模态语言模型相结合，利用视觉技术提取水位标尺的几何信息，然后利用LLM进行数值识别和水位估计。通过融合视觉信息和语言模型的推理能力，提高水位读取的准确性和鲁棒性。

**技术框架**：该框架包含以下主要阶段：1) 图像预处理：对采集的河流标尺图像进行去噪、增强等处理，提高图像质量。2) 水线检测：利用计算机视觉算法检测图像中的水线位置。3) 刻度间隙估计：使用YOLOv8提取标尺的姿态和尺度信息，估计刻度之间的间隙大小。4) 数值读取提取：将水线位置和刻度间隙信息输入到大型多模态语言模型（GPT 4o或Gemini 2.0 Flash）中，由LLM识别标尺上的数值并估计水位。

**关键创新**：该论文的关键创新在于将计算机视觉技术与大型多模态语言模型相结合，实现自动化的河流标尺水位读取。通过引入刻度间隙的几何元数据，显著提高了LLM的预测性能。此外，该方法还探索了不同LLM在水位读取任务中的表现，并分析了图像质量对LLM性能的影响。

**关键设计**：水线检测采用图像处理算法，例如边缘检测和霍夫变换。刻度间隙估计使用YOLOv8进行目标检测和姿态估计。大型多模态语言模型使用GPT 4o和Gemini 2.0 Flash，通过提示工程（prompt engineering）引导LLM进行数值识别和水位估计。损失函数主要考虑水位估计的均方误差和绝对误差。

## 📊 实验亮点

实验结果表明，水线检测精度达到94.24%，F1分数为83.64%。在最佳图像条件下，结合刻度间隙元数据后，Gemini Stage 2的平均绝对误差为5.43厘米，均方根误差为8.58厘米，R平方为0.84。实验还验证了图像质量对LLM性能的影响，表明高质量图像对于准确的水位估计至关重要。

## 🎯 应用场景

该研究成果可应用于水文监测、水资源管理、防洪预警等领域。通过自动化河流标尺水位读取，可以提高监测效率和数据质量，为水资源决策提供更准确的依据。该技术还可扩展到其他类型的仪表读数自动化，具有广泛的应用前景。

## 📄 摘要（原文）

> Accurate and continuous monitoring of river water levels is essential for flood forecasting, water resource management, and ecological protection. Traditional hydrological observation methods are often limited by manual measurement errors and environmental constraints. This study presents a hybrid framework integrating vision based waterline detection, YOLOv8 pose scale extraction, and large multimodal language models (GPT 4o and Gemini 2.0 Flash) for automated river gauge plate reading. The methodology involves sequential stages of image preprocessing, annotation, waterline detection, scale gap estimation, and numeric reading extraction. Experiments demonstrate that waterline detection achieved high precision of 94.24 percent and an F1 score of 83.64 percent, while scale gap detection provided accurate geometric calibration for subsequent reading extraction. Incorporating scale gap metadata substantially improved the predictive performance of LLMs, with Gemini Stage 2 achieving the highest accuracy, with a mean absolute error of 5.43 cm, root mean square error of 8.58 cm, and R squared of 0.84 under optimal image conditions. Results highlight the sensitivity of LLMs to image quality, with degraded images producing higher errors, and underscore the importance of combining geometric metadata with multimodal artificial intelligence for robust water level estimation. Overall, the proposed approach offers a scalable, efficient, and reliable solution for automated hydrological monitoring, demonstrating potential for real time river gauge digitization and improved water resource management.

