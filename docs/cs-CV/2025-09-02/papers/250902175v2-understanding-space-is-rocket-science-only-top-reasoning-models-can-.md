---
layout: default
title: Understanding Space Is Rocket Science -- Only Top Reasoning Models Can Solve Spatial Understanding Tasks
---

# Understanding Space Is Rocket Science -- Only Top Reasoning Models Can Solve Spatial Understanding Tasks

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.02175" class="toolbar-btn" target="_blank">📄 arXiv: 2509.02175v2</a>
  <a href="https://arxiv.org/pdf/2509.02175.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.02175v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.02175v2', 'Understanding Space Is Rocket Science -- Only Top Reasoning Models Can Solve Spatial Understanding Tasks')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Nils Hoehing, Mayug Maniparambil, Ellen Rushe, Noel E. O'Connor, Anthony Ventresque

**分类**: cs.CV, cs.AI, cs.CL, cs.LG

**发布日期**: 2025-09-02 (更新: 2025-09-04)

**🔗 代码/项目**: [GITHUB](https://github.com/nilshoehing/rocketscience)

---

## 💡 一句话要点

**提出RocketScience基准，揭示现有VLM在空间关系理解上的不足**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `空间关系理解` `视觉语言模型` `VLM` `基准数据集` `RocketScience` `空间推理` `物体定位` `解耦分析`

## 📋 核心要点

1. 现有视觉语言模型（VLM）在空间关系理解方面存在明显不足，难以处理涉及相对位置和物体顺序的任务。
2. 提出RocketScience基准，包含真实图像-文本对，专注于考察VLM的空间推理能力，特别是相对空间关系和物体顺序。
3. 实验表明，现有VLM在RocketScience上表现不佳，而推理模型表现出更高的性能，空间推理是性能瓶颈。

## 📝 摘要（中文）

本文提出了RocketScience，一个开源的对比视觉语言模型（VLM）基准，用于测试空间关系理解能力。该基准包含全新的真实世界图像-文本对，主要考察相对空间理解和物体顺序。实验验证表明，RocketScience对人类来说非常简单，但对当前一代VLM来说却极具挑战。结果显示，开源和前沿商业VLM在空间关系理解方面存在显著不足，而推理模型表现出令人惊讶的高性能。此外，我们进行了解耦分析，以区分思维链模型中物体定位和空间推理的贡献，发现该基准的性能瓶颈在于空间推理能力，而非物体定位能力。我们以CC-BY-4.0许可证发布数据集，并在https://github.com/nilshoehing/rocketscience提供评估代码。

## 🔬 方法详解

**问题定义**：论文旨在解决视觉语言模型（VLM）在理解图像中物体之间的空间关系方面的不足。现有的VLM在处理需要理解相对位置（例如“A在B的左边”）和物体顺序的任务时表现不佳，这限制了它们在需要空间推理的应用中的能力。

**核心思路**：论文的核心思路是创建一个专门用于测试VLM空间关系理解能力的基准数据集RocketScience。该数据集的设计原则是：对人类来说非常简单，但对当前的VLM来说具有挑战性。通过对比VLM和推理模型在RocketScience上的表现，来揭示VLM在空间推理方面的局限性。

**技术框架**：RocketScience基准包含真实世界的图像-文本对，这些图像-文本对主要关注相对空间理解和物体顺序。论文还进行了解耦分析，以区分物体定位和空间推理在思维链模型中的贡献。具体流程包括：1）构建RocketScience数据集；2）在RocketScience上评估各种VLM和推理模型；3）进行解耦分析，评估物体定位和空间推理对模型性能的影响。

**关键创新**：RocketScience基准的主要创新在于其专注于测试VLM的空间关系理解能力，并且数据集的设计使得它对人类来说很简单，但对VLM来说却具有挑战性。此外，论文还通过解耦分析，深入研究了物体定位和空间推理对模型性能的影响，揭示了空间推理是当前VLM的瓶颈。

**关键设计**：RocketScience数据集包含大量的图像-文本对，这些图像-文本对涵盖了各种不同的空间关系和物体顺序。数据集的标注质量很高，并且经过了人工验证。解耦分析通过修改思维链模型，分别评估物体定位和空间推理对模型性能的影响。具体的参数设置和网络结构细节未在摘要中详细说明，需要查阅论文全文。

## 📊 实验亮点

实验结果表明，现有的开源和商业VLM在RocketScience基准上表现出显著的空间关系理解不足。令人惊讶的是，推理模型在该基准上表现出更高的性能。解耦分析表明，空间推理能力是当前VLM在该基准上的性能瓶颈，而非物体定位能力。具体的性能数据和提升幅度需要在论文全文中查找。

## 🎯 应用场景

该研究成果可应用于机器人导航、自动驾驶、图像检索、视觉问答等领域。通过提高VLM的空间关系理解能力，可以使机器更好地理解周围环境，从而实现更智能的交互和决策。未来的研究可以集中在开发更强大的空间推理模型，并将其集成到VLM中。

## 📄 摘要（原文）

> We propose RocketScience, an open-source contrastive VLM benchmark that tests for spatial relation understanding. It is comprised of entirely new real-world image-text pairs covering mostly relative spatial understanding and the order of objects. The benchmark is designed to be very easy for humans and hard for the current generation of VLMs, and this is empirically verified. Our results show a striking lack of spatial relation understanding in open source and frontier commercial VLMs and a surprisingly high performance of reasoning models. Additionally, we perform a disentanglement analysis to separate the contributions of object localization and spatial reasoning in chain-of-thought-based models and find that the performance on the benchmark is bottlenecked by spatial reasoning and not object localization capabilities. We release the dataset with a CC-BY-4.0 license and make the evaluation code available at: https://github.com/nilshoehing/rocketscience

