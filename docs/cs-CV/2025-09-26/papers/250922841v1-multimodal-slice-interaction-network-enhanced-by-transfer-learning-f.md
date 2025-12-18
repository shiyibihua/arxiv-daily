---
layout: default
title: Multimodal Slice Interaction Network Enhanced by Transfer Learning for Precise Segmentation of Internal Gross Tumor Volume in Lung Cancer PET/CT Imaging
---

# Multimodal Slice Interaction Network Enhanced by Transfer Learning for Precise Segmentation of Internal Gross Tumor Volume in Lung Cancer PET/CT Imaging

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.22841" class="toolbar-btn" target="_blank">📄 arXiv: 2509.22841v1</a>
  <a href="https://arxiv.org/pdf/2509.22841.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.22841v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.22841v1', 'Multimodal Slice Interaction Network Enhanced by Transfer Learning for Precise Segmentation of Internal Gross Tumor Volume in Lung Cancer PET/CT Imaging')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yi Luo, Yike Guo, Hamed Hooshangnejad, Rui Zhang, Xue Feng, Quan Chen, Wil Ngwa, Kai Ding

**分类**: cs.CV, cs.AI

**发布日期**: 2025-09-26

**备注**: 11 pages, 5 figures

---

## 💡 一句话要点

**提出基于迁移学习和多模态交互网络的肺癌IGTV精确分割方法**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `肺癌分割` `IGTV分割` `PET/CT影像` `迁移学习` `多模态融合` `切片交互模块` `深度学习`

## 📋 核心要点

1. 肺癌放疗需要精确的IGTV分割，但标注数据稀缺且肿瘤边界PET信号弱，导致分割精度低。
2. 利用迁移学习，在GTV数据集上预训练网络，再在IGTV数据集上微调，提升模型泛化能力。
3. 引入切片交互模块(SIM)，通过建模切片间依赖关系，增强对弱PET信号区域的分割能力，显著提升Dice系数。

## 📝 摘要（中文）

肺癌是全球癌症死亡的主要原因。精确勾画PET/CT影像中的内部肿瘤体积(IGTV)对于肺癌等移动肿瘤的优化放疗至关重要，但受到带标注IGTV数据集有限以及肿瘤边界PET信号衰减的阻碍。本研究提出了一种基于迁移学习的方法，利用在大量肿瘤体积(GTV)数据集上预训练的、具有MAMBA的多模态交互感知网络，然后在私有的IGTV队列上进行微调。该队列是肺癌统一跨模态影像数据集(LUCID)的PET/CT子集。为了进一步解决IGTV外周切片中PET信号弱的问题，我们在2.5D分割框架中引入了切片交互模块(SIM)，以有效地建模切片间的关系。我们提出的模块集成了通道和空间注意力分支与深度卷积，从而能够更稳健地学习切片间的依赖关系，并提高整体分割性能。全面的实验评估表明，我们的方法在私有IGTV数据集上实现了0.609的Dice系数，大大超过了传统基线的0.385。这项工作突出了迁移学习的潜力，结合先进的多模态技术和SIM，可以提高IGTV分割的可靠性和临床相关性，从而改进肺癌放疗计划。

## 🔬 方法详解

**问题定义**：论文旨在解决肺癌PET/CT影像中内部肿瘤体积(IGTV)的精确分割问题。现有方法面临的痛点在于：一是缺乏大规模标注的IGTV数据集，导致模型训练困难；二是肿瘤边界区域的PET信号衰减，使得分割精度降低，尤其是在IGTV的外周切片上。

**核心思路**：论文的核心思路是利用迁移学习和多模态信息交互来提升IGTV的分割精度。首先，通过在大量GTV数据集上预训练模型，学习通用的肿瘤分割特征，然后将这些特征迁移到IGTV分割任务中，从而缓解数据稀缺的问题。其次，设计切片交互模块(SIM)来建模切片间的依赖关系，利用相邻切片的信息来增强对当前切片的分割，尤其是在PET信号较弱的区域。

**技术框架**：整体框架是一个2.5D分割网络，输入是PET/CT影像的多个相邻切片。主要包含以下模块：1)预训练的分割网络（基于MAMBA），用于提取图像特征；2)切片交互模块(SIM)，用于建模切片间的关系；3)分割头，用于预测每个像素属于肿瘤的概率。整个流程是：首先，PET/CT影像经过预处理；然后，输入到预训练的网络中提取特征；接着，SIM模块对特征进行增强；最后，分割头输出分割结果。

**关键创新**：论文的关键创新点在于：1)将迁移学习应用于IGTV分割，利用GTV数据集的知识来提升IGTV分割的性能；2)提出了切片交互模块(SIM)，通过建模切片间的依赖关系，有效地利用了相邻切片的信息，从而提高了分割精度，尤其是在PET信号较弱的区域。

**关键设计**：SIM模块的关键设计包括：1)采用通道和空间注意力机制，自适应地学习不同通道和空间位置的重要性；2)使用深度卷积来降低计算复杂度，同时保持感受野的大小；3)损失函数采用Dice loss，以优化分割结果的Dice系数。预训练模型使用了在GTV数据集上训练好的权重，并在IGTV数据集上进行微调。

## 📊 实验亮点

实验结果表明，该方法在私有IGTV数据集上实现了0.609的Dice系数，相比于传统基线方法（Dice系数为0.385）有了显著提升。这表明该方法能够有效地提高IGTV的分割精度，具有重要的临床价值。

## 🎯 应用场景

该研究成果可应用于肺癌放疗计划的制定，通过精确分割IGTV，医生可以更准确地确定肿瘤的范围和位置，从而制定更有效的放疗方案，减少对健康组织的损伤。此外，该方法也可推广到其他肿瘤的分割任务中，具有广泛的应用前景。

## 📄 摘要（原文）

> Lung cancer remains the leading cause of cancerrelated deaths globally. Accurate delineation of internal gross tumor volume (IGTV) in PET/CT imaging is pivotal for optimal radiation therapy in mobile tumors such as lung cancer to account for tumor motion, yet is hindered by the limited availability of annotated IGTV datasets and attenuated PET signal intensity at tumor boundaries. In this study, we present a transfer learningbased methodology utilizing a multimodal interactive perception network with MAMBA, pre-trained on extensive gross tumor volume (GTV) datasets and subsequently fine-tuned on a private IGTV cohort. This cohort constitutes the PET/CT subset of the Lung-cancer Unified Cross-modal Imaging Dataset (LUCID). To further address the challenge of weak PET intensities in IGTV peripheral slices, we introduce a slice interaction module (SIM) within a 2.5D segmentation framework to effectively model inter-slice relationships. Our proposed module integrates channel and spatial attention branches with depthwise convolutions, enabling more robust learning of slice-to-slice dependencies and thereby improving overall segmentation performance. A comprehensive experimental evaluation demonstrates that our approach achieves a Dice of 0.609 on the private IGTV dataset, substantially surpassing the conventional baseline score of 0.385. This work highlights the potential of transfer learning, coupled with advanced multimodal techniques and a SIM to enhance the reliability and clinical relevance of IGTV segmentation for lung cancer radiation therapy planning.

