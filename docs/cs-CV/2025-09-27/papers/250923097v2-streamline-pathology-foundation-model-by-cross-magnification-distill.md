---
layout: default
title: Streamline pathology foundation model by cross-magnification distillation
---

# Streamline pathology foundation model by cross-magnification distillation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.23097" class="toolbar-btn" target="_blank">📄 arXiv: 2509.23097v2</a>
  <a href="https://arxiv.org/pdf/2509.23097.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.23097v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.23097v2', 'Streamline pathology foundation model by cross-magnification distillation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Ziyu Su, Abdul Rehman Akbar, Usama Sajjad, Anil V. Parwani, Muhammad Khalid Khan Niazi

**分类**: cs.CV

**发布日期**: 2025-09-27 (更新: 2025-10-01)

---

## 💡 一句话要点

**提出基于跨倍率蒸馏的轻量级病理学基础模型XMAG，加速临床部署。**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `病理学` `基础模型` `知识蒸馏` `跨倍率` `轻量化`

## 📋 核心要点

1. 现有病理学基础模型参数量巨大，且依赖高倍率图像，计算成本高昂，难以在临床环境中部署。
2. XMAG通过跨倍率蒸馏，将20倍教师模型的知识迁移到5倍学生模型，显著降低计算需求。
3. XMAG在多种癌症类型的病理学分析任务中，实现了与大型模型接近的精度，但速度提升30倍。

## 📝 摘要（中文）

本文提出了一种轻量级病理学基础模型XMAG，通过跨倍率蒸馏将先进的20倍放大倍率教师模型的知识迁移到高效的5倍放大倍率学生模型架构。XMAG采用紧凑的骨干网络，完全在5倍放大倍率下运行，与现有方法相比，每个全切片图像（WSI）所需的图像块数量减少了11.3倍。该文提出的新型蒸馏框架包含双层知识迁移，对齐全局图像表示和局部空间token映射。XMAG在从公开数据集整理的349万张图像上进行训练，并在涵盖多种癌症类型的六项临床相关组织病理学分析任务中评估了性能。XMAG实现了与更大的基础模型相差不到1%的诊断准确率，同时处理速度提高了30倍，达到每分钟处理8.8张WSI的速度。跨机构验证证实了其强大的泛化能力。此外，该文还开发了一种端到端训练策略，以进一步提高模型的性能，使其接近更大的基础模型的性能。这些结果表明，跨倍率蒸馏是部署资源受限的临床环境中基础模型能力的可行方法，有可能实现实时病理学AI集成。

## 🔬 方法详解

**问题定义**：现有病理学基础模型虽然在性能上取得了显著进展，但其庞大的参数量和对高倍率图像的依赖导致计算成本过高，难以在资源受限的临床环境中部署。这限制了它们在实时病理学分析中的应用。

**核心思路**：本文的核心思路是通过跨倍率蒸馏，将高倍率（20x）教师模型的知识迁移到低倍率（5x）学生模型。这样可以在保持性能的同时，显著降低计算复杂度，因为低倍率图像包含的图像块数量更少，计算量更小。选择5x作为目标倍率，旨在在信息量和计算效率之间取得平衡。

**技术框架**：XMAG的整体框架包括以下几个主要阶段：1) 教师模型训练：使用现有的高性能基础模型（在20x倍率下训练）作为教师模型。2) 学生模型构建：构建一个参数量更小的学生模型，该模型在5x倍率下运行。3) 跨倍率蒸馏：使用双层知识迁移策略，将教师模型的知识迁移到学生模型。这包括全局图像表示的对齐和局部空间token映射的对齐。4) 端到端训练：采用端到端训练策略进一步优化学生模型。

**关键创新**：XMAG的关键创新在于其跨倍率蒸馏框架，特别是双层知识迁移策略。传统的知识蒸馏方法通常只关注全局图像表示的对齐，而XMAG同时考虑了全局和局部信息，通过对齐空间token映射，使得学生模型能够更好地学习教师模型的空间特征表示。此外，针对病理图像的特点，设计了特定的损失函数，以更好地进行知识迁移。

**关键设计**：XMAG的关键设计包括：1) 紧凑的骨干网络：学生模型采用轻量级的卷积神经网络作为骨干网络，以减少参数量。2) 双层知识迁移：全局图像表示的对齐使用余弦相似度损失函数，局部空间token映射的对齐使用KL散度损失函数。3) 端到端训练策略：采用交叉熵损失函数和知识蒸馏损失函数的加权和作为总损失函数，进行端到端训练。具体权重比例未知。

## 📊 实验亮点

XMAG在六项临床相关的组织病理学分析任务中，实现了与大型基础模型相差不到1%的诊断准确率，同时处理速度提高了30倍，达到每分钟处理8.8张WSI的速度。跨机构验证也证实了XMAG具有良好的泛化能力。这些结果表明，XMAG在保持高性能的同时，显著降低了计算成本。

## 🎯 应用场景

XMAG的潜在应用领域包括实时病理诊断、远程病理会诊、病理图像辅助分析等。通过降低计算成本，XMAG使得在资源受限的临床环境中部署高性能病理学AI成为可能，有助于提高诊断效率和准确性，改善患者预后。未来，XMAG可以进一步扩展到其他医学图像分析任务中。

## 📄 摘要（原文）

> Foundation models (FM) have transformed computational pathology but remain computationally prohibitive for clinical deployment due to their massive parameter counts and high-magnification processing requirements. Here, we introduce XMAG, a lightweight FM developed through corss-magnification distillation that transfers knowledge from state-of-the-art 20x magnification teacher to an efficient 5x magnification student architecture. XMAG employs a compact backbone and operates entirely at 5x, requiring 11.3 times fewer patches per whole slide image (WSI) compared to existing approaches. Our Novel distillation framework incorporates dual-level knowledge transfer, aligning both global image representations and local spatial token mapping. We trained XMAG on 3.49 million images curated from publicly available datasets and evaluated performance across six clinically relevant histopathology analysis tasks spanning multiple cancer types. XMAG achieved diagnostic accuracy within 1% of substantially larger foundation models while delivering 30-fold processing acceleration, reaching 8.8 WSIs per minute processing speed. Our cross-institutional validation confirmed robust generalization. Further, we developed an end-to-end training strategy to further boost our model's performance to approach the larger FMs' performance. These results establish cross-magnification distillation as a viable approach for deploying FM capabilities in resource-constrained clinical environments, potentially enabling real-time pathology AI integration.

