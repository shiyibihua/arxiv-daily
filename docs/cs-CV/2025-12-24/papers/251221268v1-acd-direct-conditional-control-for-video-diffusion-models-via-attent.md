---
layout: default
title: "ACD: Direct Conditional Control for Video Diffusion Models via Attention Supervision"
---

# ACD: Direct Conditional Control for Video Diffusion Models via Attention Supervision

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.21268" class="toolbar-btn" target="_blank">📄 arXiv: 2512.21268v1</a>
  <a href="https://arxiv.org/pdf/2512.21268.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.21268v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.21268v1', 'ACD: Direct Conditional Control for Video Diffusion Models via Attention Supervision')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Weiqi Li, Zehao Zhang, Liang Lin, Guangrun Wang

**分类**: cs.CV

**发布日期**: 2025-12-24

---

## 💡 一句话要点

**ACD：通过注意力监督实现视频扩散模型中的直接条件控制**

🎯 **匹配领域**: **支柱四：生成式动作 (Generative Motion)**

**关键词**: `视频生成` `扩散模型` `条件控制` `注意力机制` `ControlNet` `3D感知` `对象布局` `注意力监督`

## 📋 核心要点

1. 现有视频生成方法在条件控制方面存在不足，难以精确对齐条件信号，导致可控性受限。
2. ACD通过注意力监督，直接将模型的注意力图与外部控制信号对齐，从而实现更强的条件控制能力。
3. 实验表明，ACD在保证视频质量和时间连贯性的同时，显著提升了与条件输入的对齐程度。

## 📝 摘要（中文）

可控性是视频合成中的一项基本要求，其中与条件信号的精确对齐至关重要。现有的无分类器引导方法通常通过对数据和条件的联合分布进行建模来间接实现条件控制，这通常导致对指定条件的有限可控性。基于分类器的引导通过外部分类器强制执行条件，但模型可能会利用这种机制来提高分类器分数，而没有真正满足预期的条件，从而导致对抗性伪影和有限的有效可控性。在本文中，我们提出了一种新颖的注意力条件扩散（ACD）框架，用于通过注意力监督在视频扩散模型中进行直接条件控制。通过将模型的注意力图与外部控制信号对齐，ACD实现了更好的可控性。为了支持这一点，我们引入了一种稀疏的3D感知对象布局作为一种有效的条件信号，以及一个专用的布局ControlNet和一个用于可扩展布局集成的自动注释管道。在基准视频生成数据集上的大量实验表明，ACD在保持时间连贯性和视觉保真度的同时，提供了与条件输入的卓越对齐，从而为条件视频合成建立了一种有效的范例。

## 🔬 方法详解

**问题定义**：现有视频扩散模型在条件控制方面存在挑战。无分类器引导方法可控性有限，而基于分类器的引导方法容易产生对抗性伪影，无法真正满足条件要求。因此，需要一种更直接、更有效的条件控制方法。

**核心思路**：ACD的核心思路是通过注意力监督，直接将视频扩散模型的注意力图与外部控制信号对齐。通过这种方式，模型能够更准确地理解和响应条件信号，从而实现更强的可控性。这种直接对齐避免了现有方法中存在的间接建模和对抗性问题。

**技术框架**：ACD框架主要包含以下几个模块：1) 视频扩散模型：作为生成视频的基础模型。2) 布局ControlNet：用于处理稀疏的3D感知对象布局，并将其融入到扩散模型的生成过程中。3) 注意力监督模块：通过损失函数，促使扩散模型的注意力图与外部控制信号（例如，对象布局）对齐。4) 自动标注管道：用于生成大规模的训练数据，支持布局ControlNet的训练。

**关键创新**：ACD的关键创新在于通过注意力监督实现直接条件控制。与现有方法相比，ACD避免了对数据和条件的联合分布进行建模，而是直接将模型的注意力与条件信号对齐，从而实现了更强的可控性和更好的生成质量。此外，引入的稀疏3D感知对象布局和自动标注管道也为ACD的有效实施提供了支持。

**关键设计**：ACD的关键设计包括：1) 稀疏3D感知对象布局：使用3D bounding box表示场景中的对象，提供更精确的空间信息。2) 布局ControlNet：一个专门的网络，用于将布局信息融入到扩散模型的生成过程中。3) 注意力损失函数：用于衡量模型注意力图与目标布局之间的差异，并促使模型进行学习。具体的损失函数形式未知，需要在论文中查找。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.21268v1/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.21268v1/x2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.21268v1/x3.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

实验结果表明，ACD在多个基准视频生成数据集上取得了显著的性能提升。与现有方法相比，ACD能够生成与条件输入更精确对齐的视频，同时保持了良好的时间连贯性和视觉保真度。具体的性能数据需要在论文中查找，例如FID分数、用户满意度调查等。

## 🎯 应用场景

ACD可应用于各种条件视频生成任务，例如：根据用户指定的对象布局生成视频、根据文本描述生成视频场景、以及根据其他模态的信号（如音频）生成视频。该技术在游戏开发、电影制作、虚拟现实等领域具有广泛的应用前景，可以显著提升视频内容的创作效率和质量。

## 📄 摘要（原文）

> Controllability is a fundamental requirement in video synthesis, where accurate alignment with conditioning signals is essential. Existing classifier-free guidance methods typically achieve conditioning indirectly by modeling the joint distribution of data and conditions, which often results in limited controllability over the specified conditions. Classifier-based guidance enforces conditions through an external classifier, but the model may exploit this mechanism to raise the classifier score without genuinely satisfying the intended condition, resulting in adversarial artifacts and limited effective controllability. In this paper, we propose Attention-Conditional Diffusion (ACD), a novel framework for direct conditional control in video diffusion models via attention supervision. By aligning the model's attention maps with external control signals, ACD achieves better controllability. To support this, we introduce a sparse 3D-aware object layout as an efficient conditioning signal, along with a dedicated Layout ControlNet and an automated annotation pipeline for scalable layout integration. Extensive experiments on benchmark video generation datasets demonstrate that ACD delivers superior alignment with conditioning inputs while preserving temporal coherence and visual fidelity, establishing an effective paradigm for conditional video synthesis.

