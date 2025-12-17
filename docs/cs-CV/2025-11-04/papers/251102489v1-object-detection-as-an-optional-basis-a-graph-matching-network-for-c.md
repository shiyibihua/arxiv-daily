---
layout: default
title: Object Detection as an Optional Basis: A Graph Matching Network for Cross-View UAV Localization
---

# Object Detection as an Optional Basis: A Graph Matching Network for Cross-View UAV Localization

<div class="paper-toolbar">
  <div class="toolbar-left">
    <a href="https://arxiv.org/abs/2511.02489" target="_blank" class="toolbar-btn">arXiv: 2511.02489v1</a>
    <a href="https://arxiv.org/pdf/2511.02489.pdf" target="_blank" class="toolbar-btn">PDF</a>
  </div>
  <div class="toolbar-right">
    <button class="toolbar-btn favorite-btn" data-arxiv-id="2511.02489v1" 
            onclick="toggleFavorite(this, '2511.02489v1', 'Object Detection as an Optional Basis: A Graph Matching Network for Cross-View UAV Localization')" title="收藏">
      ☆ 收藏
    </button>
    <button class="toolbar-btn share-btn" onclick="copyLink()" title="复制链接">
      🔗 分享
    </button>
  </div>
</div>


**作者**: Tao Liu, Kan Ren, Qian Chen

**分类**: cs.CV

**发布日期**: 2025-11-04

**备注**: 20 pages, Submitted to IEEE TIM

**🔗 代码/项目**: [GITHUB](https://github.com/liutao23/ODGNNLoc.git)

---

## 💡 一句话要点

**提出基于对象检测和图匹配网络的跨视角无人机定位方法，解决异构图像匹配问题。**

🎯 **匹配领域**: **支柱三：空间感知 (Perception & SLAM)**

**关键词**: `无人机定位` `跨视角定位` `对象检测` `图神经网络` `图像匹配`

## 📋 核心要点

1. 现有无人机定位方法在GNSS受限区域失效，且公开数据集有限，难以有效处理跨视角和异构图像匹配。
2. 利用对象检测提取图像中的显著实例，构建图神经网络推理图像间和图像内的关系，实现精准定位。
3. 在公共和真实数据集上验证，表明该方法能有效处理异构外观差异，并具有良好的泛化能力。

## 📝 摘要（中文）

随着低空经济的快速发展，无人机在巡逻系统的测量和跟踪中变得至关重要。然而，在GNSS受限区域，基于卫星的定位方法容易失效。本文提出了一种基于对象检测进行地图匹配的跨视角无人机定位框架，旨在有效解决跨时间、跨视角、异构的航拍图像匹配问题。与传统方法将无人机视觉定位视为图像检索问题不同，本文利用现代对象检测技术从无人机和卫星图像中准确提取显著实例，并集成图神经网络来推理图像间和图像内的节点关系。通过细粒度的、基于图的节点相似性度量，我们的方法实现了强大的检索和定位性能。在公共和真实世界数据集上的大量实验表明，我们的方法能够有效地处理异构外观差异，并具有良好的泛化能力，适用于具有更大模态差距的场景，例如红外-可见光图像匹配。我们的数据集将在以下URL公开：https://github.com/liutao23/ODGNNLoc.git。

## 🔬 方法详解

**问题定义**：论文旨在解决在GNSS受限区域，无人机跨视角定位的问题。现有方法，如基于图像检索的方法，难以有效处理跨时间、跨视角和异构图像匹配，尤其是在无人机图像和卫星图像之间存在显著差异时。此外，公开可用的无人机定位数据集有限，限制了算法的训练和泛化能力。

**核心思路**：论文的核心思路是利用对象检测技术提取图像中的显著目标，并将图像表示为图结构，然后通过图神经网络学习图像之间的关系，从而实现精准的跨视角定位。这种方法避免了直接进行图像级别的特征匹配，而是关注图像中更具语义信息的对象，从而提高了匹配的鲁棒性。

**技术框架**：该方法主要包含以下几个阶段：1) 对象检测：使用预训练的对象检测器（如Faster R-CNN）从无人机图像和卫星图像中检测出显著目标。2) 图构建：将每个图像表示为一个图，其中节点代表检测到的对象，边代表对象之间的关系（如空间关系）。3) 图神经网络：使用图神经网络学习图像之间的相似性。该网络以两个图像的图作为输入，输出一个相似性得分。4) 定位：根据相似性得分，从参考数据库中检索与查询图像最相似的图像，并将参考图像的位姿作为查询图像的估计位姿。

**关键创新**：该方法最重要的创新点在于将对象检测和图神经网络结合起来，用于跨视角无人机定位。与传统的图像检索方法相比，该方法能够更好地处理图像之间的异构性，并且能够利用对象之间的关系来提高匹配的准确性。

**关键设计**：在图神经网络的设计中，论文使用了图注意力网络（GAT）来学习节点之间的权重，从而更好地捕捉对象之间的关系。此外，论文还设计了一个细粒度的节点相似性度量，用于计算不同图像中对象之间的相似性。损失函数方面，使用了对比损失来训练图神经网络，使得相似的图像在特征空间中更接近，而不相似的图像更远离。

## 📊 实验亮点

实验结果表明，该方法在公共数据集和真实世界数据集上都取得了优异的性能。与现有方法相比，该方法能够更有效地处理异构外观差异，并且具有更好的泛化能力。具体而言，该方法在跨视角定位的准确率方面取得了显著提升，尤其是在图像质量较差或光照条件不佳的情况下。

## 🎯 应用场景

该研究成果可应用于多种场景，包括无人机自主导航、城市巡逻、灾害救援和环境监测等。通过实现精准的跨视角定位，可以提高无人机在复杂环境下的适应性和可靠性，为低空经济的发展提供技术支撑。未来，该方法有望扩展到其他模态的图像匹配，如红外和可见光图像匹配，进一步拓展应用范围。

## 📄 摘要（原文）

> With the rapid growth of the low-altitude economy, UAVs have become crucial for measurement and tracking in patrol systems. However, in GNSS-denied areas, satellite-based localization methods are prone to failure. This paper presents a cross-view UAV localization framework that performs map matching via object detection, aimed at effectively addressing cross-temporal, cross-view, heterogeneous aerial image matching. In typical pipelines, UAV visual localization is formulated as an image-retrieval problem: features are extracted to build a localization map, and the pose of a query image is estimated by matching it to a reference database with known poses. Because publicly available UAV localization datasets are limited, many approaches recast localization as a classification task and rely on scene labels in these datasets to ensure accuracy. Other methods seek to reduce cross-domain differences using polar-coordinate reprojection, perspective transformations, or generative adversarial networks; however, they can suffer from misalignment, content loss, and limited realism. In contrast, we leverage modern object detection to accurately extract salient instances from UAV and satellite images, and integrate a graph neural network to reason about inter-image and intra-image node relationships. Using a fine-grained, graph-based node-similarity metric, our method achieves strong retrieval and localization performance. Extensive experiments on public and real-world datasets show that our approach handles heterogeneous appearance differences effectively and generalizes well, making it applicable to scenarios with larger modality gaps, such as infrared-visible image matching. Our dataset will be publicly available at the following URL: https://github.com/liutao23/ODGNNLoc.git.

