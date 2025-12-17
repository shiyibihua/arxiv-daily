---
layout: default
title: DinoLizer: Learning from the Best for Generative Inpainting Localization
---

# DinoLizer: Learning from the Best for Generative Inpainting Localization

**arXiv**: [2511.20722v1](https://arxiv.org/abs/2511.20722) | [PDF](https://arxiv.org/pdf/2511.20722.pdf)

**作者**: Minh Thong Doi, Jan Butora, Vincent Itier, Jérémie Boulanger, Patrick Bas

**分类**: cs.CV, cs.AI

**发布日期**: 2025-11-25

---

## 💡 一句话要点

**DinoLizer：利用DINOv2学习生成式图像修复篡改区域的定位**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱三：空间感知 (Perception & SLAM)**

**关键词**: `图像篡改检测` `生成式图像修复` `DINOv2` `Vision Transformer` `自监督学习`

## 📋 核心要点

1. 现有篡改检测方法难以有效定位生成式图像修复中的篡改区域，尤其是在语义一致性较强的情况下。
2. DinoLizer利用预训练的DINOv2模型，通过微调线性分类头，专注于检测语义层面的篡改，忽略非语义编辑。
3. 实验表明，DinoLizer在多个数据集上显著优于现有方法，尤其是在后处理操作后，IoU提升高达12%。

## 📝 摘要（中文）

本文提出DinoLizer，一个基于DINOv2的模型，用于定位生成式图像修复中被篡改的区域。该方法基于一个预训练的DINOv2模型，该模型在B-Free数据集上训练以检测合成图像。我们在Vision Transformer的patch嵌入之上添加一个线性分类头，以$14	imes 14$的patch分辨率预测篡改。该分类头被训练为关注语义上被改变的区域，将非语义编辑视为原始内容的一部分。由于ViT只接受固定大小的输入，我们使用滑动窗口策略来聚合更大图像上的预测；对生成的heatmap进行后处理，以细化估计的二值篡改mask。实验结果表明，DinoLizer在从不同生成模型导出的各种修复数据集上，超越了最先进的局部篡改检测器。它对常见的后处理操作（如调整大小、添加噪声和JPEG（双重）压缩）保持鲁棒性。平均而言，DinoLizer实现了比次优模型高12%的交并比（IoU），后处理后增益更大。我们使用现成的DINOv2进行的实验证明了Vision Transformer在该任务中的强大表征能力。最后，将DINOv2及其后继者DINOv3在deepfake定位中进行比较的广泛消融研究证实了DinoLizer的优越性。代码将在论文被接受后公开。

## 🔬 方法详解

**问题定义**：论文旨在解决生成式图像修复后，如何精确定位被篡改区域的问题。现有方法在面对语义一致性较强的修复图像时，难以区分真实内容和生成内容，导致定位精度下降。

**核心思路**：核心思路是利用预训练的DINOv2模型强大的视觉表征能力，并在此基础上训练一个分类器，专注于检测图像中语义层面的变化。通过忽略非语义编辑，模型可以更准确地识别出被篡改的区域。

**技术框架**：DinoLizer的技术框架主要包括以下几个阶段：1) 使用在B-Free数据集上预训练的DINOv2模型提取图像特征；2) 在Vision Transformer的patch嵌入之上添加一个线性分类头；3) 使用滑动窗口策略处理大尺寸图像，生成heatmap；4) 对heatmap进行后处理，得到最终的二值篡改mask。

**关键创新**：关键创新在于利用DINOv2的自监督学习能力，使其能够学习到图像的深层语义信息。通过微调线性分类头，模型能够专注于检测语义层面的篡改，从而提高定位精度。此外，滑动窗口策略和后处理步骤也进一步提升了模型的性能。

**关键设计**：DinoLizer的关键设计包括：1) 使用DINOv2作为特征提取器；2) 在ViT的patch嵌入上添加线性分类头，以$14	imes 14$的patch分辨率进行预测；3) 使用滑动窗口策略处理大尺寸图像；4) 通过后处理步骤（未知具体细节）细化篡改mask。

## 📊 实验亮点

DinoLizer在多个生成式图像修复数据集上取得了显著的性能提升，平均IoU比次优模型高12%，并且在经过常见的后处理操作（如缩放、噪声添加、JPEG压缩）后，仍然保持了较好的鲁棒性。消融实验表明，DINOv2优于其后继者DINOv3在deepfake定位任务上的表现。

## 🎯 应用场景

DinoLizer可应用于数字取证、图像版权保护、新闻真实性验证等领域。通过自动检测图像中的篡改区域，可以帮助识别伪造图像，维护网络信息安全，并为司法鉴定提供技术支持。未来，该技术有望集成到图像编辑软件中，辅助用户识别潜在的篡改风险。

## 📄 摘要（原文）

> We introduce DinoLizer, a DINOv2-based model for localizing manipulated regions in generative inpainting. Our method builds on a DINOv2 model pretrained to detect synthetic images on the B-Free dataset. We add a linear classification head on top of the Vision Transformer's patch embeddings to predict manipulations at a $14\times 14$ patch resolution. The head is trained to focus on semantically altered regions, treating non-semantic edits as part of the original content. Because the ViT accepts only fixed-size inputs, we use a sliding-window strategy to aggregate predictions over larger images; the resulting heatmaps are post-processed to refine the estimated binary manipulation masks. Empirical results show that DinoLizer surpasses state-of-the-art local manipulation detectors on a range of inpainting datasets derived from different generative models. It remains robust to common post-processing operations such as resizing, noise addition, and JPEG (double) compression. On average, DinoLizer achieves a 12\% higher Intersection-over-Union (IoU) than the next best model, with even greater gains after post-processing. Our experiments with off-the-shelf DINOv2 demonstrate the strong representational power of Vision Transformers for this task. Finally, extensive ablation studies comparing DINOv2 and its successor, DINOv3, in deepfake localization confirm DinoLizer's superiority. The code will be publicly available upon acceptance of the paper.

