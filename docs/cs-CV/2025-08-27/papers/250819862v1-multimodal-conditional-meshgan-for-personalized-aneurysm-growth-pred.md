---
layout: default
title: Multimodal Conditional MeshGAN for Personalized Aneurysm Growth Prediction
---

# Multimodal Conditional MeshGAN for Personalized Aneurysm Growth Prediction

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.19862" class="toolbar-btn" target="_blank">📄 arXiv: 2508.19862v1</a>
  <a href="https://arxiv.org/pdf/2508.19862.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.19862v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.19862v1', 'Multimodal Conditional MeshGAN for Personalized Aneurysm Growth Prediction')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Long Chen, Ashiv Patel, Mengyun Qiao, Mohammad Yousuf Salmasi, Salah A. Hammouche, Vasilis Stavrinides, Jasleen Nagi, Soodeh Kalaie, Xiao Yun Xu, Wenjia Bai, Declan P. O'Regan

**分类**: cs.CV, cs.LG

**发布日期**: 2025-08-27

**🔗 代码/项目**: [GITHUB](https://github.com/ImperialCollegeLondon/MCMeshGAN)

---

## 💡 一句话要点

**提出MCMeshGAN以解决个性化动脉瘤生长预测问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `动脉瘤预测` `生成对抗网络` `多模态学习` `图卷积网络` `个性化医疗` `医疗影像分析` `三维建模`

## 📋 核心要点

1. 个性化动脉瘤生长预测面临建模细微局部变形和全局解剖变化的挑战，现有方法难以满足临床需求。
2. MCMeshGAN通过双分支架构结合局部KNN卷积网络和全局图卷积网络，提升了对复杂三维几何体的建模能力。
3. 实验结果显示，MCMeshGAN在几何准确性和直径估计上显著优于现有基线，展示了其临床应用潜力。

## 📝 摘要（中文）

个性化、准确的主动脉动脉瘤进展预测对于及时干预至关重要，但由于需要建模复杂三维几何体中的细微局部变形和全局解剖变化，这一任务仍然具有挑战性。我们提出了MCMeshGAN，这是首个用于三维动脉瘤生长预测的多模态条件网格生成对抗网络。MCMeshGAN引入了双分支架构，结合了一种新颖的基于KNN的局部卷积网络（KCN）以保留细致的几何细节，以及一种全局图卷积网络（GCN）以捕捉长距离结构上下文，克服了深度GCN的过平滑限制。我们还创建了TAAMesh，这是一个新的纵向胸主动脉动脉瘤网格数据集，包含来自208名患者的590个多模态记录（CT扫描、3D网格和临床数据）。大量实验表明，MCMeshGAN在几何精度和临床重要的直径估计方面始终优于现有的基线方法。

## 🔬 方法详解

**问题定义**：本论文旨在解决个性化动脉瘤生长预测中的建模挑战，现有方法在处理复杂三维几何体时，难以有效捕捉细微的局部变形和全局结构变化。

**核心思路**：MCMeshGAN的核心思路是通过双分支架构，结合局部KNN卷积网络（KCN）和全局图卷积网络（GCN），以同时保留细致的几何特征和长距离的结构上下文，从而提高预测的准确性。

**技术框架**：MCMeshGAN的整体架构包括两个主要模块：局部分支使用KCN来处理细节，全球分支使用GCN来捕捉全局结构信息。此外，条件分支用于编码临床属性（如年龄和性别）及目标时间间隔，以生成符合解剖学的时间控制预测。

**关键创新**：MCMeshGAN的关键创新在于其双分支架构设计，尤其是KCN与GCN的结合，克服了传统深度GCN的过平滑问题，能够更好地处理复杂的三维结构。

**关键设计**：在网络设计上，MCMeshGAN采用了特定的损失函数以平衡几何精度与临床相关性，同时在参数设置上进行了优化，以确保模型的稳定性和预测的准确性。

## 📊 实验亮点

实验结果表明，MCMeshGAN在几何准确性和临床重要的直径估计方面，均显著优于现有的基线方法，具体性能提升幅度达到XX%（具体数据未知），展示了其在临床应用中的潜力和价值。

## 🎯 应用场景

该研究的潜在应用领域包括医疗影像分析和个性化医疗，尤其是在主动脉动脉瘤的监测和治疗规划中。通过提供准确的生长预测，MCMeshGAN能够帮助医生制定更有效的干预策略，提升患者的治疗效果。未来，该框架有望扩展到其他类型的生物医学建模和疾病进展预测中。

## 📄 摘要（原文）

> Personalized, accurate prediction of aortic aneurysm progression is essential for timely intervention but remains challenging due to the need to model both subtle local deformations and global anatomical changes within complex 3D geometries. We propose MCMeshGAN, the first multimodal conditional mesh-to-mesh generative adversarial network for 3D aneurysm growth prediction. MCMeshGAN introduces a dual-branch architecture combining a novel local KNN-based convolutional network (KCN) to preserve fine-grained geometric details and a global graph convolutional network (GCN) to capture long-range structural context, overcoming the over-smoothing limitations of deep GCNs. A dedicated condition branch encodes clinical attributes (age, sex) and the target time interval to generate anatomically plausible, temporally controlled predictions, enabling retrospective and prospective modeling. We curated TAAMesh, a new longitudinal thoracic aortic aneurysm mesh dataset consisting of 590 multimodal records (CT scans, 3D meshes, and clinical data) from 208 patients. Extensive experiments demonstrate that MCMeshGAN consistently outperforms state-of-the-art baselines in both geometric accuracy and clinically important diameter estimation. This framework offers a robust step toward clinically deployable, personalized 3D disease trajectory modeling. The source code for MCMeshGAN and the baseline methods is publicly available at https://github.com/ImperialCollegeLondon/MCMeshGAN.

