---
layout: default
title: Sparse-LaViDa: Sparse Multimodal Discrete Diffusion Language Models
---

# Sparse-LaViDa: Sparse Multimodal Discrete Diffusion Language Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.14008" class="toolbar-btn" target="_blank">📄 arXiv: 2512.14008v1</a>
  <a href="https://arxiv.org/pdf/2512.14008.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.14008v1" onclick="toggleFavorite(this, '2512.14008v1', 'Sparse-LaViDa: Sparse Multimodal Discrete Diffusion Language Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Shufan Li, Jiuxiang Gu, Kangning Liu, Zhe Lin, Zijun Wei, Aditya Grover, Jason Kuen

**分类**: cs.CV

**发布日期**: 2025-12-16

**备注**: 18 pages (12 pages for the main paper and 6 pages for the appendix), 9 figures

---

## 💡 一句话要点

**Sparse-LaViDa：通过稀疏化采样加速多模态离散扩散语言模型推理。**

🎯 **匹配领域**: **支柱四：生成式动作 (Generative Motion)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多模态扩散模型` `稀疏采样` `推理加速` `文本到图像生成` `图像编辑`

## 📋 核心要点

1. MDM推理速度受限于重复处理冗余掩码token，效率有待提升。
2. Sparse-LaViDa动态截断不必要的掩码token，并用register token保持生成质量。
3. 通过专门设计的attention mask，确保训练和推理过程的一致性，加速效果显著。

## 📝 摘要（中文）

本文提出了一种名为Sparse-LaViDa的新建模框架，旨在加速Masked Discrete Diffusion Models (MDMs)的推理过程。MDMs在图像理解、生成和编辑等多种多模态任务中表现出色，但由于需要在每个采样步骤中重复处理冗余的掩码token，其推理速度仍有优化空间。Sparse-LaViDa通过在每个推理步骤中动态截断不必要的掩码token来加速MDM采样。为了保持生成质量，引入了专门的register token作为截断token的紧凑表示。此外，为了确保训练和推理之间的一致性，设计了一种专门的attention mask，在训练期间忠实地匹配截断采样过程。基于最先进的统一MDM LaViDa-O，Sparse-LaViDa在文本到图像生成、图像编辑和数学推理等多种任务中实现了高达2倍的加速，同时保持了生成质量。

## 🔬 方法详解

**问题定义**：现有Masked Discrete Diffusion Models (MDMs)在多模态任务中表现出色，但推理速度较慢，主要原因是需要在每个采样步骤中重复处理大量的掩码token。这些冗余的计算消耗了大量的计算资源，限制了MDMs在实际应用中的效率。

**核心思路**：Sparse-LaViDa的核心思路是在推理过程中动态地截断不必要的掩码token，从而减少计算量，加速采样过程。为了弥补截断token可能造成的生成质量损失，引入了register token作为截断token的紧凑表示，以保留关键信息。通过这种稀疏化的方式，可以在保证生成质量的前提下，显著提升推理速度。

**技术框架**：Sparse-LaViDa建立在LaViDa-O模型之上，其整体框架仍然是扩散模型。主要改进在于采样阶段。在每个采样步骤中，模型首先评估各个掩码token的重要性，然后根据重要性得分截断一部分token。被截断的token的信息被聚合到register token中。然后，模型基于剩余的token和register token进行下一步的采样。

**关键创新**：Sparse-LaViDa的关键创新在于动态稀疏化采样和register token的设计。动态稀疏化采样允许模型自适应地减少计算量，而register token则保证了在稀疏化过程中信息的有效保留。此外，专门设计的attention mask确保了训练和推理过程的一致性，避免了因训练和推理差异导致的性能下降。

**关键设计**：register token的数量是一个关键参数，需要根据具体任务进行调整。attention mask的设计需要精确匹配截断采样过程，以保证训练的有效性。损失函数方面，Sparse-LaViDa沿用了LaViDa-O的损失函数，但可能需要根据稀疏化程度进行调整。

## 📊 实验亮点

实验结果表明，Sparse-LaViDa在多种任务上实现了显著的加速效果，最高可达2倍，同时保持了与LaViDa-O相当的生成质量。在文本到图像生成任务中，Sparse-LaViDa在加速的同时，FID指标没有明显下降。在图像编辑和数学推理任务中，Sparse-LaViDa也表现出了类似的性能提升。

## 🎯 应用场景

Sparse-LaViDa可应用于各种多模态任务，如文本到图像生成、图像编辑、视觉推理等。其加速推理的特性使其更适合对实时性要求较高的应用场景，例如在线图像编辑、智能客服等。该研究有助于推动多模态扩散模型在实际应用中的普及。

## 📄 摘要（原文）

> Masked Discrete Diffusion Models (MDMs) have achieved strong performance across a wide range of multimodal tasks, including image understanding, generation, and editing. However, their inference speed remains suboptimal due to the need to repeatedly process redundant masked tokens at every sampling step. In this work, we propose Sparse-LaViDa, a novel modeling framework that dynamically truncates unnecessary masked tokens at each inference step to accelerate MDM sampling. To preserve generation quality, we introduce specialized register tokens that serve as compact representations for the truncated tokens. Furthermore, to ensure consistency between training and inference, we design a specialized attention mask that faithfully matches the truncated sampling procedure during training. Built upon the state-of-the-art unified MDM LaViDa-O, Sparse-LaViDa achieves up to a 2x speedup across diverse tasks including text-to-image generation, image editing, and mathematical reasoning, while maintaining generation quality.

