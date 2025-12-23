---
layout: default
title: Object-level Self-Distillation for Vision Pretraining
---

# Object-level Self-Distillation for Vision Pretraining

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.05409" class="toolbar-btn" target="_blank">📄 arXiv: 2506.05409v1</a>
  <a href="https://arxiv.org/pdf/2506.05409.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.05409v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.05409v1', 'Object-level Self-Distillation for Vision Pretraining')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Çağlar Hızlı, Çağatay Yıldız, Pekka Marttinen

**分类**: cs.CV, cs.LG

**发布日期**: 2025-06-04

---

## 💡 一句话要点

**提出对象级自蒸馏方法以解决图像级自蒸馏局限性**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `对象级自蒸馏` `视觉预训练` `图像处理` `深度学习` `计算机视觉`

## 📋 核心要点

1. 现有视觉预训练方法假设每张图像仅包含一个对象，导致在多对象图像和复杂场景数据集上的表现不佳。
2. 本文提出对象级自蒸馏（ODIS）方法，通过聚焦于单个对象而非整张图像，提升自蒸馏的有效性。
3. ODIS方法在ImageNet1k上使用ViT-Large模型实现了82.6%的k-NN准确率，显著提升了视觉表示能力。

## 📝 摘要（中文）

现有的视觉预训练方法依赖于从以对象为中心的数据集（如ImageNet）进行图像级自蒸馏，隐含假设每张图像只包含一个对象。然而，这一假设并不总是成立，许多ImageNet图像实际上包含多个对象。此外，这限制了方法在更复杂的场景中心数据集上的扩展能力。为了解决这些挑战，本文提出了对象级自蒸馏（ODIS）方法，将自蒸馏的粒度从整张图像转移到单个对象。通过对象感知裁剪和掩码注意力，ODIS能够隔离对象特定区域，引导变换器关注语义上有意义的内容，从而将噪声较大的场景级任务转化为更简单的对象级子任务。实验结果表明，该方法在图像和补丁级别均提升了视觉表示能力。

## 🔬 方法详解

**问题定义**：现有的视觉预训练方法通常假设每张图像只包含一个对象，这在多对象图像中并不成立，限制了模型的表现和扩展性。

**核心思路**：本文提出的对象级自蒸馏（ODIS）方法，通过将自蒸馏的关注点从整张图像转移到单个对象，解决了这一假设带来的局限性。该方法通过对象感知裁剪和掩码注意力，帮助模型更好地理解和处理图像中的语义信息。

**技术框架**：ODIS的整体架构包括对象感知裁剪模块和掩码注意力机制。首先，通过裁剪技术提取对象特定区域，然后利用掩码注意力引导变换器关注这些区域，最终将复杂的场景级任务分解为简单的对象级子任务。

**关键创新**：ODIS的主要创新在于将自蒸馏的粒度从图像级别转向对象级别，这一转变使得模型能够更有效地学习和提取对象特征，克服了传统方法的局限。

**关键设计**：在设计中，ODIS使用了对象感知裁剪技术来精确定位对象区域，并通过掩码注意力机制来增强模型对这些区域的关注。此外，损失函数的设计也考虑了对象级别的特征提取，以确保模型能够有效学习。

## 📊 实验亮点

在实验中，ODIS方法在ImageNet1k数据集上使用ViT-Large模型达到了82.6%的k-NN准确率，相较于传统图像级自蒸馏方法，显著提升了视觉表示能力，展示了其在复杂场景处理中的有效性。

## 🎯 应用场景

该研究的潜在应用领域包括计算机视觉中的物体识别、场景理解和自动驾驶等。通过提升模型在复杂场景中的表现，ODIS方法能够为实际应用提供更强的视觉理解能力，推动智能系统的进一步发展。

## 📄 摘要（原文）

> State-of-the-art vision pretraining methods rely on image-level self-distillation from object-centric datasets such as ImageNet, implicitly assuming each image contains a single object. This assumption does not always hold: many ImageNet images already contain multiple objects. Further, it limits scalability to scene-centric datasets that better mirror real-world complexity. We address these challenges by introducing Object-level Self-DIStillation (ODIS), a pretraining approach that shifts the self-distillation granularity from whole images to individual objects. Using object-aware cropping and masked attention, ODIS isolates object-specific regions, guiding the transformer toward semantically meaningful content and transforming a noisy, scene-level task into simpler object-level sub-tasks. We show that this approach improves visual representations both at the image and patch levels. Using masks at inference time, our method achieves an impressive $82.6\%$ $k$-NN accuracy on ImageNet1k with ViT-Large.

