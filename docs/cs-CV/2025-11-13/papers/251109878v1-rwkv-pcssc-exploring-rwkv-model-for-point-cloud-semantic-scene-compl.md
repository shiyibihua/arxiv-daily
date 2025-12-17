---
layout: default
title: RWKV-PCSSC: Exploring RWKV Model for Point Cloud Semantic Scene Completion
---

# RWKV-PCSSC: Exploring RWKV Model for Point Cloud Semantic Scene Completion

<div class="paper-toolbar">
  <div class="toolbar-left">
    <a href="https://arxiv.org/abs/2511.09878" target="_blank" class="toolbar-btn">arXiv: 2511.09878v1</a>
    <a href="https://arxiv.org/pdf/2511.09878.pdf" target="_blank" class="toolbar-btn">PDF</a>
  </div>
  <div class="toolbar-right">
    <button class="toolbar-btn favorite-btn" data-arxiv-id="2511.09878v1" 
            onclick="toggleFavorite(this, '2511.09878v1', 'RWKV-PCSSC: Exploring RWKV Model for Point Cloud Semantic Scene Completion')" title="收藏">
      ☆ 收藏
    </button>
    <button class="toolbar-btn share-btn" onclick="copyLink()" title="复制链接">
      🔗 分享
    </button>
  </div>
</div>


**作者**: Wenzhe He, Xiaojun Chen, Wentang Chen, Hongyu Wang, Ying Liu, Ruihui Li

**分类**: cs.CV

**发布日期**: 2025-11-13

**备注**: 13 pages, 8 figures, published to ACM MM

**期刊**: Proc. 33rd ACM Int. Conf. Multimedia (MM '25), Dublin, Ireland, 2025, pp. 161-170

**DOI**: [10.1145/3746027.3754908](https://doi.org/10.1145/3746027.3754908)

---

## 💡 一句话要点

**提出RWKV-PCSSC，利用RWKV机制实现轻量高效的点云语义场景补全。**

🎯 **匹配领域**: **支柱三：空间感知 (Perception & SLAM)**

**关键词**: `点云语义场景补全` `RWKV模型` `轻量级网络` `点云处理` `三维重建`

## 📋 核心要点

1. 现有语义场景补全方法参数量大，模型复杂，资源需求高，限制了其应用。
2. RWKV-PCSSC利用RWKV机制，设计RWKV-SG和RWKV-PD模块，逐步恢复点云特征。
3. 实验表明，RWKV-PCSSC在多个数据集上达到SOTA，并显著降低了参数量和提高了内存效率。

## 📝 摘要（中文）

语义场景补全(SSC)旨在从不完整的输入生成完整的语义场景。现有方法通常采用参数量大的密集网络架构，导致模型复杂性和资源需求增加。为了解决这些限制，我们提出了一种受Receptance Weighted Key Value (RWKV)机制启发的轻量级点云语义场景补全网络RWKV-PCSSC。具体来说，我们引入了RWKV Seed Generator (RWKV-SG)模块，该模块可以聚合来自部分点云的特征，以生成具有粗略特征的粗略点云。随后，通过多个阶段的RWKV Point Deconvolution (RWKV-PD)模块逐步恢复点云的点特征。通过利用紧凑而高效的设计，我们的方法实现了轻量级的模型表示。实验结果表明，与最先进的方法PointSSC相比，RWKV-PCSSC减少了4.18倍的参数量，并将内存效率提高了1.37倍。此外，我们的网络在已建立的室内(SSC-PC, NYUCAD-PC)和室外(PointSSC)场景数据集以及我们提出的数据集(NYUCAD-PC-V2, 3D-FRONT-PC)上实现了最先进的性能。

## 🔬 方法详解

**问题定义**：语义场景补全旨在从不完整的点云数据中恢复出完整的三维场景，并赋予每个点语义标签。现有方法通常依赖于参数量巨大的密集网络，导致计算资源消耗高，难以部署到资源受限的设备上。因此，如何设计轻量级且高性能的语义场景补全网络是一个关键问题。

**核心思路**：RWKV-PCSSC的核心思路是利用Receptance Weighted Key Value (RWKV)机制，构建轻量级的特征提取和融合模块。RWKV机制能够有效地建模序列数据之间的长距离依赖关系，并且具有较低的计算复杂度。通过将RWKV机制引入到点云处理中，可以有效地减少模型的参数量，并提高计算效率。

**技术框架**：RWKV-PCSSC主要包含两个核心模块：RWKV Seed Generator (RWKV-SG)和RWKV Point Deconvolution (RWKV-PD)。首先，RWKV-SG模块从输入的局部点云中提取粗略的特征，并生成一个粗略的点云。然后，通过多个阶段的RWKV-PD模块，逐步恢复点云的细节特征和语义信息。每个RWKV-PD模块都利用RWKV机制来融合局部邻域内的点特征，从而实现高效的特征传播和增强。

**关键创新**：RWKV-PCSSC的关键创新在于将RWKV机制引入到点云语义场景补全任务中。与传统的卷积神经网络或Transformer网络相比，RWKV机制具有更低的计算复杂度和更好的长距离依赖建模能力。此外，RWKV-SG和RWKV-PD模块的设计也充分考虑了点云数据的特点，能够有效地提取和融合点云特征。

**关键设计**：RWKV-SG模块使用多层感知机（MLP）和最大池化操作来提取粗略特征。RWKV-PD模块使用RWKV机制来融合局部邻域内的点特征，并使用反卷积操作来恢复点云的细节信息。损失函数包括语义分割损失和场景补全损失，用于监督网络的训练。具体的参数设置和网络结构细节在论文中有详细描述。

## 📊 实验亮点

RWKV-PCSSC在SSC-PC、NYUCAD-PC、PointSSC、NYUCAD-PC-V2和3D-FRONT-PC等多个数据集上取得了state-of-the-art的性能。与PointSSC相比，RWKV-PCSSC的参数量减少了4.18倍，内存效率提高了1.37倍，同时在性能上有所提升，证明了该方法的有效性和优越性。

## 🎯 应用场景

RWKV-PCSSC在自动驾驶、机器人导航、三维重建等领域具有广泛的应用前景。例如，在自动驾驶中，可以利用该方法从车载传感器获取的不完整点云数据中恢复出完整的场景信息，从而提高车辆的感知能力和安全性。在机器人导航中，可以利用该方法构建机器人的三维环境地图，从而实现自主导航和避障。

## 📄 摘要（原文）

> Semantic Scene Completion (SSC) aims to generate a complete semantic scene from an incomplete input. Existing approaches often employ dense network architectures with a high parameter count, leading to increased model complexity and resource demands. To address these limitations, we propose RWKV-PCSSC, a lightweight point cloud semantic scene completion network inspired by the Receptance Weighted Key Value (RWKV) mechanism. Specifically, we introduce a RWKV Seed Generator (RWKV-SG) module that can aggregate features from a partial point cloud to produce a coarse point cloud with coarse features. Subsequently, the point-wise feature of the point cloud is progressively restored through multiple stages of the RWKV Point Deconvolution (RWKV-PD) modules. By leveraging a compact and efficient design, our method achieves a lightweight model representation. Experimental results demonstrate that RWKV-PCSSC reduces the parameter count by 4.18$\times$ and improves memory efficiency by 1.37$\times$ compared to state-of-the-art methods PointSSC. Furthermore, our network achieves state-of-the-art performance on established indoor (SSC-PC, NYUCAD-PC) and outdoor (PointSSC) scene dataset, as well as on our proposed datasets (NYUCAD-PC-V2, 3D-FRONT-PC).

