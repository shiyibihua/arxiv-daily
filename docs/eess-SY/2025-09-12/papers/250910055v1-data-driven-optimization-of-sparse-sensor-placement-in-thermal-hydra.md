---
layout: default
title: Data-driven optimization of sparse sensor placement in thermal hydraulic experiments
---

# Data-driven optimization of sparse sensor placement in thermal hydraulic experiments

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.10055" class="toolbar-btn" target="_blank">📄 arXiv: 2509.10055v1</a>
  <a href="https://arxiv.org/pdf/2509.10055.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.10055v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.10055v1', 'Data-driven optimization of sparse sensor placement in thermal hydraulic experiments')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Xicheng Wang, Yun. Feng, Dmitry Grishchenko, Pavel Kudinov, Ruifeng Tian, Sichao Tan

**分类**: eess.SY

**发布日期**: 2025-09-12

---

## 💡 一句话要点

**提出数据驱动的稀疏传感器优化部署框架，用于热工水力实验。**

🎯 **匹配领域**: **支柱六：视频提取与匹配 (Video Extraction)**

**关键词**: `热工水力实验` `传感器优化` `数据驱动` `灵敏度分析` `POD降维` `QR分解` `传感器部署`

## 📋 核心要点

1. 热工水力实验中传感器稀疏分布导致数据覆盖有限，传感器空间配置是实验设计的关键挑战。
2. 该论文提出一种数据驱动框架，通过灵敏度分析、POD降维和QR分解优化传感器位置。
3. 该框架在铅铋共晶回路实验中验证，结果表明该方法能有效提升传感器对参数变化的敏感性，并实现精确的全场重建。

## 📝 摘要（中文）

热工水力(TH)实验为传热传质的物理现象提供了宝贵的见解，并为代码开发、校准和验证提供了合格的数据。然而，测量通常是从稀疏分布的传感器收集的，对感兴趣的区域和现象的覆盖有限。在测试前的设计阶段，确定这些传感器的空间配置至关重要且具有挑战性。本文开发了一个数据驱动的框架，用于优化热工水力实验中的传感器位置，包括(i)用于构建数据集的灵敏度分析，(ii)用于降维的Proper Orthogonal Decomposition (POD)，以及(iii)带有列主元的QR分解，用于确定空间约束下的最佳传感器配置。该框架在一个TALL-3D铅铋共晶(LBE)回路中进行的测试中得到了验证。在这种情况下，诸如粒子图像测速(PIV)等光学技术的应用是不切实际的。因此，动量和能量传递的量化严重依赖于热电偶(TCs)的读数。测试部分之前已经配备了许多热电偶，这些热电偶是通过结合模拟结果和专家判断的手动过程确定的。所提出的框架提供了一种系统和自动化的传感器放置方法。由此产生的热电偶对不确定输入参数的变化表现出高灵敏度，并能够在保持对测量噪声的鲁棒性的同时实现精确的全场重建。

## 🔬 方法详解

**问题定义**：热工水力实验中，传感器数量有限且分布稀疏，如何优化传感器位置，以最大程度地获取实验信息，并准确重建整个流场的状态？传统方法依赖于专家经验和仿真结果，效率低且难以保证最优性。

**核心思路**：利用实验数据，通过灵敏度分析确定关键区域，然后使用降维技术提取主要特征，最后通过优化算法选择最具代表性的传感器位置。核心在于将传感器部署问题转化为一个数据驱动的优化问题，从而实现自动化和高效的传感器配置。

**技术框架**：该框架包含三个主要阶段：1) **灵敏度分析**：通过改变输入参数，分析各位置传感器读数的变化，构建数据集。2) **降维**：使用Proper Orthogonal Decomposition (POD)对数据集进行降维，提取主要模态，减少计算复杂度。3) **传感器优化**：使用带有列主元的QR分解，在空间约束下选择最佳传感器配置，保证所选传感器能够最大程度地捕捉流场的主要特征。

**关键创新**：该方法将数据驱动的优化方法引入到热工水力实验的传感器部署中，摆脱了对专家经验的依赖，实现了传感器配置的自动化和优化。与传统方法相比，该方法能够更有效地利用实验数据，选择对输入参数变化更敏感的传感器位置，从而提高实验数据的质量和信息量。

**关键设计**：灵敏度分析的具体方法未知，需要根据具体实验场景选择合适的灵敏度指标。POD降维中，需要确定保留的模态数量，以平衡计算精度和计算效率。QR分解中，需要考虑空间约束，例如传感器之间的最小距离，以保证传感器部署的合理性。此外，测量噪声对传感器选择的影响也需要考虑，框架需要具备一定的鲁棒性。

## 📊 实验亮点

该论文在TALL-3D铅铋共晶回路中验证了所提出的框架。结果表明，该方法选择的传感器对输入参数变化具有高灵敏度，并且能够实现精确的全场重建，同时保持对测量噪声的鲁棒性。虽然论文中没有给出具体的性能数据和对比基线，但强调了该方法能够提供一种系统和自动化的传感器放置方法，优于传统的手动方法。

## 🎯 应用场景

该研究成果可应用于各种热工水力实验的传感器优化部署，例如核反应堆热工水力实验、冷却系统设计、换热器性能测试等。通过优化传感器配置，可以提高实验数据的质量和信息量，降低实验成本，并为相关设备的研发和优化提供更可靠的数据支持。该方法也可能推广到其他类型的实验，例如化学反应器、生物反应器等。

## 📄 摘要（原文）

> Thermal-Hydraulic (TH) experiments provide valuable insight into the physics of heat and mass transfer and qualified data for code development, calibration and validation. However, measurements are typically collected from sparsely distributed sensors, offering limited coverage over the domain of interest and phenomena of interest. Determination of the spatial configuration of these sensors is crucial and challenging during the pre-test design stage. This paper develops a data-driven framework for optimizing sensor placement in TH experiments, including (i) a sensitivity analysis to construct datasets, (ii) Proper Orthogonal Decomposition (POD) for dimensionality reduction, and (iii) QR factorization with column pivoting to determine optimal sensor configuration under spatial constraints. The framework is demonstrated on a test conducted in the TALL-3D Lead-bismuth eutectic (LBE) loop. In this case, the utilization of optical techniques, such as Particle Image Velocimetry (PIV), are impractical. Thereby the quantification of momentum and energy transport relies heavily on readings from Thermocouples (TCs). The test section was previously instrumented with many TCs determined through a manual process combining simulation results with expert judgement. The proposed framework provides a systematic and automated approach for sensor placement. The resulting TCs exhibit high sensitivity to the variation of uncertain input parameters and enable accurate full field reconstruction while maintaining robustness against measurement noise.

