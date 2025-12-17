---
layout: default
title: Towards Transferable Defense Against Malicious Image Edits
---

# Towards Transferable Defense Against Malicious Image Edits

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.14341" class="toolbar-btn" target="_blank">📄 arXiv: 2512.14341v1</a>
  <a href="https://arxiv.org/pdf/2512.14341.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.14341v1" onclick="toggleFavorite(this, '2512.14341v1', 'Towards Transferable Defense Against Malicious Image Edits')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jie Zhang, Shuai Dong, Shiguang Shan, Xilin Chen

**分类**: cs.CV, cs.AI, cs.CY, cs.LG

**发布日期**: 2025-12-16

**备注**: 14 pages, 5 figures

---

## 💡 一句话要点

**提出TDAE框架，增强图像对恶意编辑的防御迁移能力**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)**

**关键词**: `恶意图像编辑防御` `可迁移性` `对抗攻击` `扩散模型` `双模态学习`

## 📋 核心要点

1. 现有防御方法在跨不同扩散模型进行恶意编辑防御时，迁移能力不足，鲁棒性较差。
2. TDAE框架通过图像和文本的协同优化，增强图像对恶意编辑的免疫力，提高跨模型迁移性。
3. 实验结果表明，TDAE在模型内和跨模型评估中，均能有效减轻恶意编辑，达到最佳性能。

## 📝 摘要（中文）

现有方法在对抗基于扩散模型的图像编辑系统中恶意操作时，通过在输入图像中加入不易察觉的扰动，展现出了一定的潜力。然而，这些方法在跨模型评估中迁移性有限。为了解决这个问题，我们提出了可迁移的恶意图像编辑防御（TDAE），这是一种新颖的双模态框架，通过协调图像-文本优化来增强图像对恶意编辑的免疫力。具体来说，在视觉防御层面，我们引入了FlatGrad防御机制（FDM），它将梯度正则化纳入对抗目标中。通过显式地引导扰动朝向平坦最小值，FDM增强了对未见过的编辑模型的免疫鲁棒性。对于文本增强保护，我们提出了一种名为动态提示防御（DPD）的对抗优化范式，它定期细化文本嵌入，以使免疫图像的编辑结果与原始图像的编辑结果对齐，然后使用优化的嵌入更新图像。通过对各种嵌入进行迭代对抗更新，DPD强制生成免疫图像，以寻求更广泛的免疫增强特征，从而实现跨模型可迁移性。大量的实验结果表明，我们的TDAE在减轻模型内和跨模型评估中的恶意编辑方面取得了最先进的性能。

## 🔬 方法详解

**问题定义**：论文旨在解决现有方法在对抗基于扩散模型的恶意图像编辑时，防御能力在不同模型间迁移性差的问题。现有的防御方法通常针对特定模型进行优化，导致在面对未知的恶意编辑模型时，防御效果显著下降。

**核心思路**：论文的核心思路是通过图像和文本的双模态协同优化，增强图像的免疫力，使其对各种恶意编辑具有更强的鲁棒性和迁移性。通过在视觉层面寻找平坦最小值和在文本层面动态调整提示词，使得防御策略更加通用。

**技术框架**：TDAE框架包含两个主要模块：FlatGrad防御机制（FDM）和动态提示防御（DPD）。FDM在视觉层面通过梯度正则化增强图像的鲁棒性，DPD在文本层面通过对抗优化提示词，使免疫图像的编辑结果与原始图像对齐。这两个模块协同工作，共同提升防御效果。

**关键创新**：论文的关键创新在于提出了一个双模态的防御框架，将图像和文本信息结合起来进行防御。FDM通过寻找平坦最小值来提高鲁棒性，DPD通过动态调整提示词来增强迁移性。这种双管齐下的方法能够有效地应对各种恶意编辑。

**关键设计**：FDM的关键设计在于梯度正则化项，通过最小化梯度的范数，引导扰动朝向平坦最小值。DPD的关键设计在于对抗优化提示词，通过迭代更新文本嵌入，使免疫图像的编辑结果与原始图像对齐。损失函数的设计也至关重要，需要平衡防御效果和图像质量。

## 📊 实验亮点

实验结果表明，TDAE在减轻恶意编辑方面取得了最先进的性能。具体来说，TDAE在模型内和跨模型评估中均优于现有方法，能够有效地防御各种恶意编辑攻击。论文提供了详细的实验数据，证明了TDAE的有效性和优越性。

## 🎯 应用场景

该研究成果可应用于保护图像内容免受恶意篡改，例如在社交媒体、新闻媒体等领域，防止虚假信息的传播。此外，该技术还可以应用于数字水印、版权保护等领域，提高图像内容的安全性。未来，该技术有望进一步发展，应用于更广泛的图像安全领域。

## 📄 摘要（原文）

> Recent approaches employing imperceptible perturbations in input images have demonstrated promising potential to counter malicious manipulations in diffusion-based image editing systems. However, existing methods suffer from limited transferability in cross-model evaluations. To address this, we propose Transferable Defense Against Malicious Image Edits (TDAE), a novel bimodal framework that enhances image immunity against malicious edits through coordinated image-text optimization. Specifically, at the visual defense level, we introduce FlatGrad Defense Mechanism (FDM), which incorporates gradient regularization into the adversarial objective. By explicitly steering the perturbations toward flat minima, FDM amplifies immune robustness against unseen editing models. For textual enhancement protection, we propose an adversarial optimization paradigm named Dynamic Prompt Defense (DPD), which periodically refines text embeddings to align the editing outcomes of immunized images with those of the original images, then updates the images under optimized embeddings. Through iterative adversarial updates to diverse embeddings, DPD enforces the generation of immunized images that seek a broader set of immunity-enhancing features, thereby achieving cross-model transferability. Extensive experimental results demonstrate that our TDAE achieves state-of-the-art performance in mitigating malicious edits under both intra- and cross-model evaluations.

