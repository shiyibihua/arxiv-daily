---
layout: default
title: MambaEye: A Size-Agnostic Visual Encoder with Causal Sequential Processing
---

# MambaEye: A Size-Agnostic Visual Encoder with Causal Sequential Processing

<div class="paper-toolbar">
  <div class="toolbar-left">
    <a href="https://arxiv.org/abs/2511.19963" target="_blank" class="toolbar-btn">arXiv: 2511.19963v1</a>
    <a href="https://arxiv.org/pdf/2511.19963.pdf" target="_blank" class="toolbar-btn">PDF</a>
  </div>
  <div class="toolbar-right">
    <button class="toolbar-btn favorite-btn" data-arxiv-id="2511.19963v1" 
            onclick="toggleFavorite(this, '2511.19963v1', 'MambaEye: A Size-Agnostic Visual Encoder with Causal Sequential Processing')" title="收藏">
      ☆ 收藏
    </button>
    <button class="toolbar-btn share-btn" onclick="copyLink()" title="复制链接">
      🔗 分享
    </button>
  </div>
</div>


**作者**: Changho Choi, Minho Kim, Jinkyu Kim

**分类**: cs.CV, cs.AI

**发布日期**: 2025-11-25

**备注**: Code will be released in github

---

## 💡 一句话要点

**MambaEye：基于因果序列处理的尺寸无关视觉编码器**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `视觉编码器` `Mamba` `状态空间模型` `因果序列处理` `尺寸无关` `相对移动嵌入` `高分辨率图像` `图像分类`

## 📋 核心要点

1. 现有视觉编码器难以实现输入尺寸无关性，限制了其在不同分辨率图像上的应用。
2. MambaEye利用单向Mamba2骨干网络和相对移动嵌入，实现因果序列处理和对任意分辨率的适应性。
3. 实验表明，MambaEye在ImageNet-1K分类任务中，高分辨率图像上表现出强大的性能，且保持线性复杂度。

## 📝 摘要（中文）

本文提出了一种新颖的因果序列编码器MambaEye，旨在解决视觉编码器对输入尺寸的依赖问题，这是人类视觉的一个基本特征但长期未被解决。MambaEye利用低复杂度和基于因果过程的纯Mamba2骨干网络。与以往基于Mamba的双向视觉编码器不同，MambaEye采用严格的单向方法，保留了状态空间模型的固有因果性，使其能够在输入序列的任何点生成预测。核心创新是相对移动嵌入，它编码了连续图像块之间的空间位移，为平移不变性提供了强大的归纳偏置，并使模型能够适应任意图像分辨率和扫描模式。此外，引入了一种受扩散启发的损失函数，提供密集的、逐步的监督，训练模型在收集更多视觉证据时建立置信度。实验表明，MambaEye在各种图像分辨率下表现出强大的性能，尤其是在ImageNet-1K分类任务中，分辨率高达$1536^2$时。同时，相对于图像块的数量，保持了线性的时间和内存复杂度。

## 🔬 方法详解

**问题定义**：现有视觉编码器通常对输入图像的尺寸有严格要求，无法像人类视觉一样灵活处理任意分辨率的图像。这限制了它们在实际应用中的泛化能力，尤其是在高分辨率图像处理方面，计算复杂度会显著增加。

**核心思路**：MambaEye的核心思路是利用单向的Mamba2架构，结合相对移动嵌入，实现对图像块序列的因果建模。通过这种方式，模型可以逐步积累视觉信息，并在任意时刻生成预测，从而摆脱对固定输入尺寸的依赖。

**技术框架**：MambaEye的整体框架包括以下几个主要步骤：1) 将输入图像分割成图像块序列；2) 使用相对移动嵌入编码图像块之间的空间关系；3) 将编码后的序列输入到单向Mamba2骨干网络中进行特征提取；4) 使用分类头基于提取的特征进行预测。关键在于Mamba2的单向性和相对移动嵌入的空间信息编码。

**关键创新**：MambaEye的关键创新在于以下两点：一是采用了单向的Mamba2架构，保留了状态空间模型的因果性，使其能够进行序列化的视觉信息处理；二是引入了相对移动嵌入，有效地编码了图像块之间的空间关系，为平移不变性提供了强大的归纳偏置，并使模型能够适应任意图像分辨率和扫描模式。

**关键设计**：MambaEye的关键设计包括：1) 使用相对移动嵌入来编码图像块之间的空间位移，具体实现方式未知；2) 采用受扩散启发的损失函数，提供密集的、逐步的监督，训练模型在收集更多视觉证据时建立置信度，损失函数的具体形式未知；3) Mamba2骨干网络的具体参数设置未知。

## 📊 实验亮点

MambaEye在ImageNet-1K分类任务中，尤其是在高分辨率（如$1536^2$）图像上表现出强大的性能。相较于传统的视觉编码器，MambaEye在高分辨率图像处理方面具有显著优势，同时保持了线性的时间和内存复杂度。具体的性能数据和对比基线未在摘要中明确给出，需要查阅论文全文。

## 🎯 应用场景

MambaEye具有广泛的应用前景，例如在高分辨率图像识别、医学图像分析、遥感图像处理等领域。其尺寸无关的特性使其能够灵活应用于各种场景，降低了对输入图像尺寸的限制，提升了模型的泛化能力。未来，MambaEye有望成为一种通用的视觉编码器，为各种视觉任务提供强大的支持。

## 📄 摘要（原文）

> Despite decades of progress, a truly input-size agnostic visual encoder-a fundamental characteristic of human vision-has remained elusive. We address this limitation by proposing \textbf{MambaEye}, a novel, causal sequential encoder that leverages the low complexity and causal-process based pure Mamba2 backbone. Unlike previous Mamba-based vision encoders that often employ bidirectional processing, our strictly unidirectional approach preserves the inherent causality of State Space Models, enabling the model to generate a prediction at any point in its input sequence. A core innovation is our use of relative move embedding, which encodes the spatial shift between consecutive patches, providing a strong inductive bias for translation invariance and making the model inherently adaptable to arbitrary image resolutions and scanning patterns. To achieve this, we introduce a novel diffusion-inspired loss function that provides dense, step-wise supervision, training the model to build confidence as it gathers more visual evidence. We demonstrate that MambaEye exhibits robust performance across a wide range of image resolutions, especially at higher resolutions such as $1536^2$ on the ImageNet-1K classification task. This feat is achieved while maintaining linear time and memory complexity relative to the number of patches.

