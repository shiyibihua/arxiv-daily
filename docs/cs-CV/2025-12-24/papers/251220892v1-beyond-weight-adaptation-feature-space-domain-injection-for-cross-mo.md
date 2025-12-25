---
layout: default
title: "Beyond Weight Adaptation: Feature-Space Domain Injection for Cross-Modal Ship Re-Identification"
---

# Beyond Weight Adaptation: Feature-Space Domain Injection for Cross-Modal Ship Re-Identification

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.20892" class="toolbar-btn" target="_blank">📄 arXiv: 2512.20892v1</a>
  <a href="https://arxiv.org/pdf/2512.20892.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.20892v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.20892v1', 'Beyond Weight Adaptation: Feature-Space Domain Injection for Cross-Modal Ship Re-Identification')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Tingfeng Xian, Wenlve Zhou, Zhiheng Zhou, Zhelin Li

**分类**: cs.CV

**发布日期**: 2025-12-24

**🔗 代码/项目**: [GITHUB](https://github.com/TingfengXian/DRI)

---

## 💡 一句话要点

**提出领域表示注入方法以解决跨模态船舶再识别问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `跨模态再识别` `领域表示注入` `视觉基础模型` `参数高效微调` `海洋目标跟踪`

## 📋 核心要点

1. 现有的跨模态船舶再识别方法依赖于大规模配对数据集，导致模态对齐效果不佳。
2. 本文提出领域表示注入（DRI）策略，通过特征空间优化而非权重空间，提升跨模态再识别性能。
3. 在HOSS-ReID数据集上，DRI方法以最少的可训练参数实现了SOTA性能，显著提升了识别精度。

## 📝 摘要（中文）

跨模态船舶再识别（CMS Re-ID）对全天候海洋目标跟踪至关重要，但面临显著的模态差异挑战。现有主流解决方案通常依赖于显式模态对齐策略，然而这种方法严重依赖于构建大规模配对数据集进行预训练。为了解决这一问题，基于柏拉图表征假设，本文探讨了视觉基础模型（VFM）在弥合模态差距方面的潜力。我们提出了一种新颖的参数高效微调策略，称为领域表示注入（DRI），通过保持VFM完全冻结，设计轻量级可学习的偏移编码器，从原始输入中提取丰富的模态和身份属性的领域特征。实验结果表明，该方法在HOSS-ReID数据集上实现了57.9%和60.5%的mAP，参数量仅为1.54M和7.05M。

## 🔬 方法详解

**问题定义**：本文旨在解决跨模态船舶再识别中的模态差异问题。现有方法通常依赖于大规模配对数据集进行预训练，导致在小型模型上的性能不佳。

**核心思路**：我们提出领域表示注入（DRI）策略，转向特征空间的优化，通过冻结VFM来保留通用知识，同时提取领域特定的表示。

**技术框架**：整体架构包括一个偏移编码器和一个调制器。偏移编码器从原始输入中提取领域特征，调制器根据中间特征的上下文信息进行自适应转换，最后通过加法融合将这些表示注入到中间层。

**关键创新**：DRI方法的核心创新在于通过特征空间的动态重塑来适应下游任务，而不改变VFM的预训练权重。这一方法显著提升了模型在跨模态任务中的表现。

**关键设计**：我们设计了轻量级的偏移编码器和调制器，采用了特定的损失函数来优化领域特征的提取与融合，确保了模型的高效性与准确性。通过精简的参数设置，DRI方法在保持性能的同时降低了计算复杂度。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.20892v1/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.20892v1/x2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.20892v1/x3.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

实验结果显示，DRI方法在HOSS-ReID数据集上取得了57.9%和60.5%的mAP，分别使用了1.54M和7.05M的参数，显著优于现有的基线方法，展示了其在参数效率和识别精度上的优势。

## 🎯 应用场景

该研究在海洋监测、船舶识别和智能交通等领域具有广泛的应用潜力。通过提高跨模态再识别的准确性，能够有效支持全天候的海洋目标跟踪，提升海洋安全和管理效率。未来，该方法还可扩展至其他多模态识别任务，推动相关技术的发展。

## 📄 摘要（原文）

> Cross-Modality Ship Re-Identification (CMS Re-ID) is critical for achieving all-day and all-weather maritime target tracking, yet it is fundamentally challenged by significant modality discrepancies. Mainstream solutions typically rely on explicit modality alignment strategies; however, this paradigm heavily depends on constructing large-scale paired datasets for pre-training. To address this, grounded in the Platonic Representation Hypothesis, we explore the potential of Vision Foundation Models (VFMs) in bridging modality gaps. Recognizing the suboptimal performance of existing generic Parameter-Efficient Fine-Tuning (PEFT) methods that operate within the weight space, particularly on limited-capacity models, we shift the optimization perspective to the feature space and propose a novel PEFT strategy termed Domain Representation Injection (DRI). Specifically, while keeping the VFM fully frozen to maximize the preservation of general knowledge, we design a lightweight, learnable Offset Encoder to extract domain-specific representations rich in modality and identity attributes from raw inputs. Guided by the contextual information of intermediate features at different layers, a Modulator adaptively transforms these representations. Subsequently, they are injected into the intermediate layers via additive fusion, dynamically reshaping the feature distribution to adapt to the downstream task without altering the VFM's pre-trained weights. Extensive experimental results demonstrate the superiority of our method, achieving State-of-the-Art (SOTA) performance with minimal trainable parameters. For instance, on the HOSS-ReID dataset, we attain 57.9\% and 60.5\% mAP using only 1.54M and 7.05M parameters, respectively. The code is available at https://github.com/TingfengXian/DRI.

