---
layout: default
title: Fine-Scale Soil Mapping in Alaska with Multimodal Machine Learning
---

# Fine-Scale Soil Mapping in Alaska with Multimodal Machine Learning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.17302" class="toolbar-btn" target="_blank">📄 arXiv: 2506.17302v1</a>
  <a href="https://arxiv.org/pdf/2506.17302.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.17302v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.17302v1', 'Fine-Scale Soil Mapping in Alaska with Multimodal Machine Learning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yijun Lin, Theresa Chen, Colby Brungard, Grunwald Sabine, Sue Ives, Matt Macander, Timm Nawrocki, Yao-Yi Chiang, Nic Jelinski

**分类**: cs.CV, cs.LG

**发布日期**: 2025-06-17

**备注**: 12 pages, Submitted to SIGSPATIAL 2025

**🔗 代码/项目**: [GITHUB](https://github.com/knowledge-computing/Peatland-permafrost)

---

## 💡 一句话要点

**提出MISO模型以解决阿拉斯加细尺度土壤制图问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `细尺度土壤制图` `多模态机器学习` `永久冻土监测` `地理空间模型` `隐式神经表示` `对比学习` `环境适应策略`

## 📋 核心要点

1. 现有的土壤制图方法主要依赖实地调查，效率低且难以覆盖偏远地区，限制了对永久冻土的监测和管理。
2. MISO模型通过结合视觉特征提取、隐式神经表示和对比学习，实现了对土壤和永久冻土的细尺度制图，提升了空间预测的连续性和准确性。
3. 实验结果显示，MISO在不同的永久冻土区域和主要土地资源区的空间交叉验证中，泛化能力优于随机森林模型，召回率显著提高。

## 📝 摘要（中文）

阿拉斯加的细尺度土壤制图传统上依赖于实地工作和局部模拟，尽管该地区生态重要性和广泛的永久冻土覆盖使其成为关键任务。随着气候变化加速永久冻土融化，威胁基础设施稳定性和土壤碳储存等生态系统服务。高分辨率土壤图对于表征永久冻土分布、识别脆弱区域和指导适应策略至关重要。本文提出了MISO模型，该模型结合了地理空间基础模型、隐式神经表示和对比学习，能够生成全州范围内的细尺度土壤图。实验结果表明，MISO在遥远未见位置的泛化能力优于传统的随机森林模型，并在监测永久冻土融化方面表现出更高的召回率。

## 🔬 方法详解

**问题定义**：本文旨在解决阿拉斯加地区细尺度土壤制图的挑战，现有方法依赖实地调查，难以覆盖偏远区域，且效率低下，无法满足对永久冻土监测的需求。

**核心思路**：MISO模型通过整合多种机器学习技术，包括视觉特征提取和对比学习，提供了一种新的方法来生成高分辨率的土壤图，能够更好地适应复杂的地理环境。

**技术框架**：MISO的整体架构包括三个主要模块：地理空间基础模型用于提取视觉特征，隐式神经表示用于实现连续空间预测，对比学习则用于多模态对齐和地理位置感知。

**关键创新**：MISO的最大创新在于其结合了多模态学习和隐式神经表示，显著提升了对遥远未见位置的泛化能力，与传统的随机森林模型相比，能够更准确地捕捉土壤和永久冻土的空间分布特征。

**关键设计**：在模型设计中，采用了特定的损失函数以优化多模态对齐，同时在网络结构上引入了隐式神经表示，确保了空间预测的连续性和准确性。实验中还进行了参数调优，以提高模型的整体性能。

## 📊 实验亮点

实验结果表明，MISO模型在空间交叉验证中对遥远未见位置的泛化能力优于随机森林模型，召回率显著提高，具体数据未提供。该模型展示了先进机器学习方法在细尺度土壤制图中的潜力，为未来的土壤采样和基础设施规划提供了实用指导。

## 🎯 应用场景

该研究的潜在应用领域包括环境监测、基础设施规划和生态恢复等。通过提供高分辨率的土壤地图，MISO模型能够为政策制定者和研究人员提供重要的数据支持，帮助应对气候变化带来的挑战，尤其是在永久冻土地区的管理和保护方面。

## 📄 摘要（原文）

> Fine-scale soil mapping in Alaska, traditionally relying on fieldwork and localized simulations, remains a critical yet underdeveloped task, despite the region's ecological importance and extensive permafrost coverage. As permafrost thaw accelerates due to climate change, it threatens infrastructure stability and key ecosystem services, such as soil carbon storage. High-resolution soil maps are essential for characterizing permafrost distribution, identifying vulnerable areas, and informing adaptation strategies. We present MISO, a vision-based machine learning (ML) model to produce statewide fine-scale soil maps for near-surface permafrost and soil taxonomy. The model integrates a geospatial foundation model for visual feature extraction, implicit neural representations for continuous spatial prediction, and contrastive learning for multimodal alignment and geo-location awareness. We compare MISO with Random Forest (RF), a traditional ML model that has been widely used in soil mapping applications. Spatial cross-validation and regional analysis across Permafrost Zones and Major Land Resource Areas (MLRAs) show that MISO generalizes better to remote, unseen locations and achieves higher recall than RF, which is critical for monitoring permafrost thaw and related environmental processes. These findings demonstrate the potential of advanced ML approaches for fine-scale soil mapping and provide practical guidance for future soil sampling and infrastructure planning in permafrost-affected landscapes. The project will be released at https://github.com/knowledge-computing/Peatland-permafrost.

