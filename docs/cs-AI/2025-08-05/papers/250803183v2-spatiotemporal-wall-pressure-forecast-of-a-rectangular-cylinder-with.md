---
layout: default
title: Spatiotemporal wall pressure forecast of a rectangular cylinder with physics-aware DeepU-Fourier neural network
---

# Spatiotemporal wall pressure forecast of a rectangular cylinder with physics-aware DeepU-Fourier neural network

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.03183" class="toolbar-btn" target="_blank">📄 arXiv: 2508.03183v2</a>
  <a href="https://arxiv.org/pdf/2508.03183.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.03183v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.03183v2', 'Spatiotemporal wall pressure forecast of a rectangular cylinder with physics-aware DeepU-Fourier neural network')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Junle Liu, Chang Liu, Yanyu Ke, Wenliang Chen, Kihing Shum, Tim K. T. Tse, Gang Hu

**分类**: physics.flu-dyn, cs.AI, cs.CE

**发布日期**: 2025-08-05 (更新: 2025-12-07)

**DOI**: [10.1063/5.0298947](https://doi.org/10.1063/5.0298947)

---

## 💡 一句话要点

**提出DeepUFNet以解决矩形圆柱体壁面压力预测问题**

🎯 **匹配领域**: **支柱八：物理动画 (Physics-based Animation)**

**关键词**: `深度学习` `流体力学` `壁面压力` `时空预测` `物理感知` `傅里叶神经网络` `UNet` `模型泛化`

## 📋 核心要点

1. 现有深度学习框架通常只能预测单一快照，缺乏对时空壁面压力的全面预测能力。
2. 本文提出的DeepUFNet模型结合了UNet和傅里叶神经网络，并引入物理高频损失控制以提升预测性能。
3. 实验结果显示，DeepUFNet在预测矩形圆柱体的壁面压力时具有高准确性，并在不同侧比的圆柱体上展现了良好的泛化能力。

## 📝 摘要（中文）

壁面压力在理解流体引起的力和结构响应中具有重要意义。尽管已有研究探讨了深度学习技术在预测平均压力系数和波动压力系数方面的潜力，但现有框架通常仅限于使用完整空间信息预测单一快照。为此，本文提出了一种物理感知的DeepU-Fourier神经网络（DeepUFNet）模型，旨在预测流过矩形圆柱体的时空壁面压力。该模型结合了UNet结构和傅里叶神经网络，并在训练阶段嵌入物理高频损失控制，以优化模型性能。实验结果表明，DeepUFNet在矩形圆柱体的时空壁面压力预测中表现出高准确性，并在未见案例中也展现了良好的泛化能力。

## 🔬 方法详解

**问题定义**：本文旨在解决流过矩形圆柱体的时空壁面压力预测问题。现有方法多局限于单一快照的预测，无法充分利用时空信息，导致预测精度不足。

**核心思路**：提出DeepUFNet模型，结合UNet结构和傅里叶神经网络，通过嵌入物理高频损失控制，优化模型在时空壁面压力预测中的表现。这种设计旨在提高模型对高频波动的捕捉能力。

**技术框架**：DeepUFNet的整体架构包括数据输入模块、UNet特征提取模块、傅里叶变换模块和损失计算模块。模型通过训练数据学习时空壁面压力的特征，并通过高频损失控制优化预测结果。

**关键创新**：DeepUFNet的主要创新在于将物理高频损失控制嵌入模型训练中，显著提升了对高阶频率波动和壁面压力方差的预测能力。这一设计与传统方法的本质区别在于其物理感知的特性。

**关键设计**：模型中设置了高频损失控制系数b，以增强对高频波动的预测能力。此外，采用了UNet和傅里叶神经网络的结合，确保了模型在处理复杂流动时的有效性。损失函数设计也考虑了物理特性，以提高模型的准确性。

## 📊 实验亮点

实验结果表明，DeepUFNet在矩形圆柱体的时空壁面压力预测中达到了高准确性，与实验数据的统计信息和物理解释一致。特别是，通过引入物理高频损失控制，模型在高阶频率波动和壁面压力方差的预测上显著提升，展现出良好的泛化能力，适用于不同侧比的圆柱体。

## 🎯 应用场景

该研究的潜在应用领域包括航空航天、建筑工程和流体动力学等领域，能够为流体力学相关的设计和优化提供重要的预测工具。通过准确预测壁面压力，工程师可以更好地理解和设计结构，以应对流体引起的力和响应，提升安全性和效率。

## 📄 摘要（原文）

> The wall pressure is of great importance in understanding the forces and structural responses induced by fluid. Recent works have investigated the potential of deep learning techniques in predicting mean pressure coefficients and fluctuating pressure coefficients, but most of existing deep learning frameworks are limited to predicting a single snapshot using full spatial information. To forecast spatiotemporal wall pressure of flow past a rectangular cylinder, this study develops a physics-aware DeepU-Fourier neural Network (DeepUFNet) deep learning model. DeepUFNet comprises the UNet structure and the Fourier neural network, with physical high-frequency loss control embedded in the model training stage to optimize model performance. Wind tunnel testing was performed to collect wall pressures on two-dimensional rectangular cylinders using high-frequency pressure scanning, thereby constructing a database for DeepUFNet training and testing. The DeepUFNet model is found capable of forecasting spatiotemporal wall pressure information with high accuracy on the rectangular cylinder with side ratio 1.5. The comparison between forecast results and experimental data presents agreement in statistical information and physical interpretation. It is also found that embedding a physical high-frequency loss control coefficient b in the DeepUFNet model can significantly improve model performance in forecasting spatiotemporal wall pressure information, particularly, high-order frequency fluctuation and wall pressure variance. Furthermore, the DeepUFNet extrapolation capability is tested with sparse spatial information input, and the model presents a satisfactory extrapolation ability. Last, the DeepUFNet is tested for generalization in unseen cases, rectangular cylinders with side ratio 4 and 3.75, and the model presents satisfactory generalization ability.

