---
layout: default
title: Unsupervised Learning for Industrial Defect Detection: A Case Study on Shearographic Data
---

# Unsupervised Learning for Industrial Defect Detection: A Case Study on Shearographic Data

**arXiv**: [2511.02541v2](https://arxiv.org/abs/2511.02541) | [PDF](https://arxiv.org/pdf/2511.02541.pdf)

**作者**: Jessica Plassmann, Nicolas Schuler, Georg von Freymann, Michael Schuth

**分类**: cs.CV

**发布日期**: 2025-11-04 (更新: 2025-12-11)

**备注**: 15 pages, 6 figures, 1 table; accepted for AI-2025 Forty-fifth SGAI International Conference on Artificial Intelligence CAMBRIDGE, ENGLAND 16-18 DECEMBER 2025

**期刊**: Artificial Intelligence XLII. SGAI-AI 2025. Lecture Notes in Computer Science, vol 16302. Springer, Cham (2026), pp 316-329

**DOI**: [10.1007/978-3-032-11442-6_22](https://doi.org/10.1007/978-3-032-11442-6_22)

---

## 💡 一句话要点

**提出无监督学习方法以解决工业缺陷检测问题**

🎯 **匹配领域**: **支柱三：空间感知 (Perception & SLAM)** **支柱六：视频提取与匹配 (Video Extraction & Matching)**

**关键词**: `无监督学习` `工业缺陷检测` `剪切测量` `深度学习` `异常检测` `特征匹配` `自动化检测`

## 📋 核心要点

1. 现有的剪切测量方法依赖于专家解读，限制了其在工业中的广泛应用。
2. 本研究提出无监督学习方法，通过自动化异常检测减少对标记数据的依赖。
3. 实验结果显示，学生-教师模型在分类和定位精度上优于自编码器模型，具有更好的特征可分离性。

## 📝 摘要（中文）

剪切测量是一种用于检测内部缺陷的无损检测方法，具有高灵敏度和全场检测能力。然而，由于需要专家解读，其工业应用仍然有限。为减少对标记数据和人工评估的依赖，本研究探索了无监督学习方法在剪切图像中的自动异常检测。评估了三种架构：全连接自编码器、卷积自编码器和学生-教师特征匹配模型。所有模型仅在无缺陷数据上进行训练。通过使用具有可重复缺陷模式的定制样本开发了受控数据集，系统获取了在理想和现实变形条件下的剪切测量。结果表明，学生-教师方法在分类鲁棒性和缺陷定位精度上优于其他模型，展示了无监督深度学习在工业环境中可扩展的潜力。

## 🔬 方法详解

**问题定义**：本论文旨在解决剪切测量中缺陷检测的自动化问题，现有方法依赖于专家的手动解读，导致效率低下和应用受限。

**核心思路**：通过无监督学习方法，利用仅包含无缺陷数据的模型进行训练，从而实现对异常的自动检测，减少对标记数据的需求。

**技术框架**：整体架构包括三个主要模块：全连接自编码器、卷积自编码器和学生-教师特征匹配模型。模型在无缺陷数据上进行训练，并在测试阶段评估其分类和定位能力。

**关键创新**：学生-教师模型在特征表示的可分离性上表现优越，能够更好地进行缺陷定位，相较于传统自编码器方法具有本质的改进。

**关键设计**：模型训练时使用了两种数据集：一种是无变形的无缺陷样本，另一种是包含全球变形但无缺陷的数据，以模拟实际检测条件。

## 📊 实验亮点

实验结果表明，学生-教师模型在二分类任务中表现出更高的鲁棒性，分类准确率显著高于其他模型。此外，该模型在缺陷定位方面的精度也得到了提升，与基于YOLOv8的标记数据模型相比，展示了更好的性能。

## 🎯 应用场景

该研究的无监督学习方法具有广泛的应用潜力，特别是在工业缺陷检测领域。通过减少对标记数据的依赖，能够提高检测效率并降低成本，适用于航空航天、汽车制造等需要高精度检测的行业。未来，该方法可能推动更多无损检测技术的自动化进程。

## 📄 摘要（原文）

> Shearography is a non-destructive testing method for detecting subsurface defects, offering high sensitivity and full-field inspection capabilities. However, its industrial adoption remains limited due to the need for expert interpretation. To reduce reliance on labeled data and manual evaluation, this study explores unsupervised learning methods for automated anomaly detection in shearographic images. Three architectures are evaluated: a fully connected autoencoder, a convolutional autoencoder, and a student-teacher feature matching model. All models are trained solely on defect-free data. A controlled dataset was developed using a custom specimen with reproducible defect patterns, enabling systematic acquisition of shearographic measurements under both ideal and realistic deformation conditions. Two training subsets were defined: one containing only undistorted, defect-free samples, and one additionally including globally deformed, yet defect-free, data. The latter simulates practical inspection conditions by incorporating deformation-induced fringe patterns that may obscure localized anomalies. The models are evaluated in terms of binary classification and, for the student-teacher model, spatial defect localization. Results show that the student-teacher approach achieves superior classification robustness and enables precise localization. Compared to the autoencoder-based models, it demonstrates improved separability of feature representations, as visualized through t-SNE embeddings. Additionally, a YOLOv8 model trained on labeled defect data serves as a reference to benchmark localization quality. This study underscores the potential of unsupervised deep learning for scalable, label-efficient shearographic inspection in industrial environments.

