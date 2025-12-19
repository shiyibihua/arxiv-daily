---
layout: default
title: Causal-Tune: Mining Causal Factors from Vision Foundation Models for Domain Generalized Semantic Segmentation
---

# Causal-Tune: Mining Causal Factors from Vision Foundation Models for Domain Generalized Semantic Segmentation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.16567" class="toolbar-btn" target="_blank">📄 arXiv: 2512.16567v1</a>
  <a href="https://arxiv.org/pdf/2512.16567.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.16567v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.16567v1', 'Causal-Tune: Mining Causal Factors from Vision Foundation Models for Domain Generalized Semantic Segmentation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yin Zhang, Yongqiang Zhang, Yaoyue Zheng, Bogdan Raducanu, Dan Liu

**分类**: cs.CV

**发布日期**: 2025-12-18

**备注**: Accepted by AAAI 2026

---

## 💡 一句话要点

**Causal-Tune：挖掘视觉基础模型中的因果因子，用于领域泛化语义分割**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `领域泛化` `语义分割` `视觉基础模型` `因果推断` `离散余弦变换` `频率分析` `特征解耦`

## 📋 核心要点

1. 现有领域泛化语义分割方法忽略了预训练视觉基础模型中存在的伪影，这些伪影会降低模型性能。
2. Causal-Tune通过分析特征频谱，分离并提取因果因素，抑制非因果因素，从而提升模型的泛化能力。
3. 实验表明，Causal-Tune在各种跨域任务中表现出色，尤其在恶劣天气条件下，显著提高了语义分割的精度。

## 📝 摘要（中文）

本文提出了一种新颖的领域泛化语义分割（DGSS）方法，旨在解决视觉基础模型（VFM）中存在的伪影问题。这些伪影与非因果因素相关，通常存在于VFM频谱的低频和高频分量中，阻碍了VFM的有效利用并降低了DGSS的性能。受因果机制的启发，本文显式地研究了VFM特征中的因果和非因果因素，并提出了一种简单而有效的方法来识别和分离它们，从而实现更鲁棒的领域泛化。具体而言，本文提出了Causal-Tune，一种新的微调策略，旨在从VFM的特征中提取因果因素并抑制非因果因素。该方法首先使用离散余弦变换（DCT）提取每层特征的频谱，然后应用高斯带通滤波器将频谱分离为因果和非因果分量。为了进一步细化因果分量，引入了一组在频域中运行的因果感知可学习token，同时丢弃非因果分量。最后，细化后的特征通过逆DCT转换回空间域，并传递到下一层。在各种跨域任务上进行的大量实验证明了Causal-Tune的有效性。尤其是在恶劣天气条件下，该方法表现出优异的性能，在雪地条件下比基线提高了+4.8% mIoU。

## 🔬 方法详解

**问题定义**：领域泛化语义分割（DGSS）旨在使模型在未见过的目标领域上也能保持良好的分割性能。现有的方法通常通过训练轻量级适配器或优化中间特征来实现，但忽略了预训练视觉基础模型（VFM）中存在的伪影，这些伪影与非因果因素相关，阻碍了VFM的有效利用，导致DGSS性能下降。

**核心思路**：本文的核心思路是基于因果机制，认为VFM中存在的伪影与非因果因素相关，这些因素通常存在于VFM频谱的低频和高频分量中。通过识别和分离这些因果和非因果因素，可以提取更鲁棒的特征表示，从而提升DGSS的性能。

**技术框架**：Causal-Tune的整体框架包括以下几个主要步骤：1. 使用离散余弦变换（DCT）提取每层特征的频谱。2. 应用高斯带通滤波器将频谱分离为因果和非因果分量。3. 引入一组因果感知可学习token，在频域中细化因果分量，并丢弃非因果分量。4. 通过逆DCT将细化后的特征转换回空间域，并传递到下一层。

**关键创新**：本文最重要的技术创新点在于显式地考虑了VFM特征中的因果和非因果因素，并提出了一种简单而有效的方法来识别和分离它们。与现有方法不同，Causal-Tune不是简单地训练适配器或优化特征，而是从因果关系的角度出发，挖掘VFM中更本质的特征表示。

**关键设计**：Causal-Tune的关键设计包括：1. 使用DCT将特征转换到频域，以便分析其频谱特性。2. 设计高斯带通滤波器，用于分离因果和非因果分量。滤波器的参数（例如中心频率和带宽）需要根据具体任务进行调整。3. 引入因果感知可学习token，用于在频域中细化因果分量。这些token可以通过反向传播进行训练，以更好地适应不同的领域和任务。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16567v1/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16567v1/x2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16567v1/x3.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

Causal-Tune在多个跨域语义分割任务上取得了显著的性能提升。特别是在雪地条件下，Causal-Tune相比基线方法提高了4.8%的mIoU。实验结果表明，Causal-Tune能够有效地提取因果因素并抑制非因果因素，从而提高模型在未见过的目标领域上的泛化能力。

## 🎯 应用场景

Causal-Tune在自动驾驶、遥感图像分析、医学图像诊断等领域具有广泛的应用前景。通过提高模型在不同环境和条件下的泛化能力，可以显著提升这些应用系统的鲁棒性和可靠性。例如，在自动驾驶中，Causal-Tune可以帮助车辆在恶劣天气条件下更准确地识别道路和障碍物，从而提高驾驶安全性。

## 📄 摘要（原文）

> Fine-tuning Vision Foundation Models (VFMs) with a small number of parameters has shown remarkable performance in Domain Generalized Semantic Segmentation (DGSS). Most existing works either train lightweight adapters or refine intermediate features to achieve better generalization on unseen domains. However, they both overlook the fact that long-term pre-trained VFMs often exhibit artifacts, which hinder the utilization of valuable representations and ultimately degrade DGSS performance. Inspired by causal mechanisms, we observe that these artifacts are associated with non-causal factors, which usually reside in the low- and high-frequency components of the VFM spectrum. In this paper, we explicitly examine the causal and non-causal factors of features within VFMs for DGSS, and propose a simple yet effective method to identify and disentangle them, enabling more robust domain generalization. Specifically, we propose Causal-Tune, a novel fine-tuning strategy designed to extract causal factors and suppress non-causal ones from the features of VFMs. First, we extract the frequency spectrum of features from each layer using the Discrete Cosine Transform (DCT). A Gaussian band-pass filter is then applied to separate the spectrum into causal and non-causal components. To further refine the causal components, we introduce a set of causal-aware learnable tokens that operate in the frequency domain, while the non-causal components are discarded. Finally, refined features are transformed back into the spatial domain via inverse DCT and passed to the next layer. Extensive experiments conducted on various cross-domain tasks demonstrate the effectiveness of Causal-Tune. In particular, our method achieves superior performance under adverse weather conditions, improving +4.8% mIoU over the baseline in snow conditions.

