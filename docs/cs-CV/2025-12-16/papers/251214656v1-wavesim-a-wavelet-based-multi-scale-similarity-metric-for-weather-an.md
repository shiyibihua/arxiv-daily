---
layout: default
title: WaveSim: A Wavelet-based Multi-scale Similarity Metric for Weather and Climate Fields
---

# WaveSim: A Wavelet-based Multi-scale Similarity Metric for Weather and Climate Fields

**arXiv**: [2512.14656v1](https://arxiv.org/abs/2512.14656) | [PDF](https://arxiv.org/pdf/2512.14656.pdf)

**作者**: Gabriele Accarino, Viviana Acquaviva, Sara Shamekh, Duncan Watson-Parris, David Lawrence

**分类**: physics.ao-ph, cs.CV, physics.data-an

**发布日期**: 2025-12-16

**🔗 代码/项目**: [GITHUB](https://github.com/gabrieleaccarino/wavesim)

---

## 💡 一句话要点

**WaveSim：一种基于小波变换的多尺度相似性度量，用于评估天气和气候场**

🎯 **匹配领域**: **物理动画 (Physics-based Animation)**

**关键词**: `小波变换` `相似性度量` `气候模型评估` `多尺度分析` `空间场` `地球系统模型` `模式识别`

## 📋 核心要点

1. 传统逐点度量方法无法将天气和气候模型中的误差归因于特定的物理尺度或模式，限制了模型诊断和改进。
2. WaveSim利用小波变换将空间场分解为多尺度分量，并从幅度、位移和结构三个正交维度评估相似性。
3. 实验表明，WaveSim能有效评估合成数据和地球系统模型中气候变率的相似性，并提供可解释的诊断信息。

## 📝 摘要（中文）

本文提出了一种名为WaveSim的多尺度相似性度量方法，用于评估天气和气候应用中的空间场。WaveSim利用小波变换将输入场分解为特定尺度的小波系数。该度量通过将从这些系数中导出的三个正交分量相乘构建：幅度（Magnitude），量化系数能量分布的相似性，即场的强度；位移（Displacement），通过比较归一化能量分布的质心来捕获空间位移；以及结构（Structure），评估独立于位置和幅度的模式组织。每个分量产生一个尺度特定的相似性得分，范围从0（无相似性）到1（完全相似性），然后跨尺度组合以产生整体相似性度量。我们首先使用合成测试用例评估WaveSim，应用受控的空间和时间扰动来系统地评估其灵敏度和预期行为。然后，我们展示了其在地球系统模型中气候变率关键模式的物理相关案例研究中的适用性。传统的逐点度量缺乏将误差归因于物理尺度或不同相似性模式的机制。通过在小波域中操作并沿独立轴分解信号，WaveSim绕过了这些限制，并提供了一个可解释且具有诊断意义的框架，用于评估复杂场中的相似性。此外，WaveSim框架允许用户强调特定尺度或分量，并适用于用户特定的模型互比较、模型评估以及预测系统的校准和训练。我们提供了一个PyTorch-ready的WaveSim实现，以及所有评估脚本，地址为：https://github.com/gabrieleaccarino/wavesim。

## 🔬 方法详解

**问题定义**：天气和气候模型评估中，传统逐点度量方法无法有效捕捉空间场的整体相似性，尤其是在存在空间位移和尺度差异的情况下。这些方法难以将模型误差归因于特定的物理过程或尺度，阻碍了模型的诊断和改进。

**核心思路**：WaveSim的核心思路是利用小波变换将空间场分解到不同的尺度上，然后在小波域中评估相似性。通过将相似性分解为幅度、位移和结构三个正交分量，WaveSim能够更全面地捕捉空间场的相似性，并提供更具诊断意义的信息。这种多尺度分析方法能够有效处理空间位移和尺度差异带来的挑战。

**技术框架**：WaveSim的整体框架包括以下几个主要步骤：1) 对输入场进行小波变换，得到不同尺度的小波系数；2) 计算每个尺度上的幅度分量，量化能量分布的相似性；3) 计算每个尺度上的位移分量，通过比较归一化能量分布的质心来捕获空间位移；4) 计算每个尺度上的结构分量，评估独立于位置和幅度的模式组织；5) 将每个尺度上的三个分量进行组合，得到尺度特定的相似性得分；6) 将不同尺度的相似性得分进行加权平均，得到最终的整体相似性度量。

**关键创新**：WaveSim最重要的技术创新在于其多尺度分解和正交分量分析。通过小波变换，WaveSim能够将空间场分解到不同的尺度上，从而更好地捕捉不同尺度的特征。通过将相似性分解为幅度、位移和结构三个正交分量，WaveSim能够更全面地评估空间场的相似性，并提供更具诊断意义的信息。与传统的逐点度量方法相比，WaveSim能够有效处理空间位移和尺度差异带来的挑战。

**关键设计**：WaveSim的关键设计包括：1) 小波基函数的选择，需要根据具体应用场景进行选择；2) 尺度分解的层数，需要根据输入场的特征进行调整；3) 幅度、位移和结构三个分量的计算方法，需要保证其正交性和可解释性；4) 不同尺度相似性得分的加权方式，可以根据用户需求进行调整，以强调特定尺度或分量。

## 📊 实验亮点

WaveSim在合成数据实验中表现出良好的灵敏度和预期行为，能够有效捕捉空间和时间扰动。在地球系统模型评估中，WaveSim成功应用于气候变率关键模式的案例研究，验证了其在实际应用中的有效性。与传统逐点度量相比，WaveSim能够提供更丰富和可解释的诊断信息。

## 🎯 应用场景

WaveSim可应用于天气和气候模型的评估、模型间的比较、以及预测系统的校准和训练。通过提供可解释的相似性度量，WaveSim能够帮助研究人员更好地理解模型误差的来源，并改进模型性能。此外，该方法还可用于评估不同气候模式对未来气候变化的预测结果，为决策者提供科学依据。

## 📄 摘要（原文）

> We introduce WaveSim, a multi-scale similarity metric for the evaluation of spatial fields in weather and climate applications. WaveSim exploits wavelet transforms to decompose input fields into scale-specific wavelet coefficients. The metric is built by multiplying three orthogonal components derived from these coefficients: Magnitude, which quantifies similarities in the energy distribution of the coefficients, i.e., the intensity of the field; Displacement, which captures spatial shift by comparing the centers of mass of normalized energy distributions; and Structure, which assesses pattern organization independent of location and amplitude. Each component yields a scale-specific similarity score ranging from 0 (no similarity) to 1 (perfect similarity), which are then combined across scales to produce an overall similarity measure. We first evaluate WaveSim using synthetic test cases, applying controlled spatial and temporal perturbations to systematically assess its sensitivity and expected behavior. We then demonstrate its applicability to physically relevant case studies of key modes of climate variability in Earth System Models. Traditional point-wise metrics lack a mechanism for attributing errors to physical scales or modes of dissimilarity. By operating in the wavelet domain and decomposing the signal along independent axes, WaveSim bypasses these limitations and provides an interpretable and diagnostically rich framework for assessing similarity in complex fields. Additionally, the WaveSim framework allows users to place emphasis on a specific scale or component, and lends itself to user-specific model intercomparison, model evaluation, and calibration and training of forecasting systems. We provide a PyTorch-ready implementation of WaveSim, along with all evaluation scripts, at: https://github.com/gabrieleaccarino/wavesim.

