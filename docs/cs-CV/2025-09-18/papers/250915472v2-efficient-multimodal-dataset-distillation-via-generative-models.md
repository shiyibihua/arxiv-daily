---
layout: default
title: Efficient Multimodal Dataset Distillation via Generative Models
---

# Efficient Multimodal Dataset Distillation via Generative Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.15472" class="toolbar-btn" target="_blank">📄 arXiv: 2509.15472v2</a>
  <a href="https://arxiv.org/pdf/2509.15472.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.15472v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.15472v2', 'Efficient Multimodal Dataset Distillation via Generative Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zhenghao Zhao, Haoxuan Wang, Junyi Wu, Yuzhang Shang, Gaowen Liu, Yan Yan

**分类**: cs.CV

**发布日期**: 2025-09-18 (更新: 2025-09-25)

---

## 💡 一句话要点

**提出EDGE方法以解决多模态数据集蒸馏效率问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多模态数据集` `数据集蒸馏` `生成模型` `对比损失` `样本多样性` `图像-文本检索` `高效算法`

## 📋 核心要点

1. 现有的多模态数据集蒸馏方法受到Matching Training Trajectories算法的限制，导致计算资源需求高且处理时间长。
2. 本文提出EDGE方法，通过双向对比损失和多样性损失的结合，解决生成图像与文本描述之间的相关性和样本多样性问题。
3. 在Flickr30K、COCO和CC3M数据集上的实验结果显示，EDGE方法在性能和效率上均优于现有方法，速度提升显著。

## 📝 摘要（中文）

数据集蒸馏旨在从大规模数据集中合成小型数据集，使得在其上训练的模型能够在原始数据集上表现良好。随着大型语言模型和多模态大型语言模型的兴起，多模态数据集，尤其是图像-文本数据集的重要性显著增加。然而，现有的多模态数据集蒸馏方法受到Matching Training Trajectories算法的限制，显著增加了计算资源需求，蒸馏过程可能需要数天时间。本文提出了一种名为EDGE的生成蒸馏方法，旨在实现高效的多模态数据集蒸馏。我们识别出使用生成模型蒸馏多模态数据集的两个关键挑战：生成图像与文本描述之间缺乏相关性，以及生成样本之间缺乏多样性。为了解决这些问题，我们提出了一种新颖的生成模型训练工作流程，结合了双向对比损失和多样性损失。此外，我们还提出了一种文本合成策略，以进一步提高文本到图像检索的性能。我们的实验在Flickr30K、COCO和CC3M数据集上进行，结果表明该方法在性能和效率上优于现有方法，速度比最先进的方法快18倍。

## 🔬 方法详解

**问题定义**：本文旨在解决多模态数据集蒸馏中的效率问题，现有方法在计算资源和时间上存在显著瓶颈，尤其是Matching Training Trajectories算法的使用使得蒸馏过程极为缓慢。

**核心思路**：EDGE方法通过引入双向对比损失和多样性损失，旨在提高生成图像与文本之间的相关性，并增加生成样本的多样性，从而提升蒸馏效率和效果。

**技术框架**：整体架构包括生成模型的训练流程，首先通过双向对比损失优化生成图像与文本的匹配度，然后通过多样性损失确保生成样本的多样性，最后结合文本合成策略提升文本到图像的检索性能。

**关键创新**：最重要的技术创新在于提出了双向对比损失和多样性损失的结合使用，这在现有方法中尚未见到，显著提升了生成样本的质量和多样性。

**关键设计**：在损失函数设计上，双向对比损失用于增强图像与文本的相关性，而多样性损失则确保生成样本的多样性。此外，文本合成策略的引入进一步增强了文本信息的利用，提升了检索性能。

## 📊 实验亮点

实验结果表明，EDGE方法在Flickr30K、COCO和CC3M数据集上表现优异，速度比最先进的方法快18倍，且在性能上也有显著提升，展示了其在多模态数据集蒸馏中的有效性和高效性。

## 🎯 应用场景

该研究的潜在应用领域包括图像-文本检索、自动标注和多模态学习等。通过提高多模态数据集的蒸馏效率，能够在资源受限的环境中快速生成高质量的数据集，推动相关领域的研究与应用发展，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> Dataset distillation aims to synthesize a small dataset from a large dataset, enabling the model trained on it to perform well on the original dataset. With the blooming of large language models and multimodal large language models, the importance of multimodal datasets, particularly image-text datasets, has grown significantly. However, existing multimodal dataset distillation methods are constrained by the Matching Training Trajectories algorithm, which significantly increases the computing resource requirement, and takes days to process the distillation. In this work, we introduce EDGE, a generative distillation method for efficient multimodal dataset distillation. Specifically, we identify two key challenges of distilling multimodal datasets with generative models: 1) The lack of correlation between generated images and captions. 2) The lack of diversity among generated samples. To address the aforementioned issues, we propose a novel generative model training workflow with a bi-directional contrastive loss and a diversity loss. Furthermore, we propose a caption synthesis strategy to further improve text-to-image retrieval performance by introducing more text information. Our method is evaluated on Flickr30K, COCO, and CC3M datasets, demonstrating superior performance and efficiency compared to existing approaches. Notably, our method achieves results 18x faster than the state-of-the-art method.

