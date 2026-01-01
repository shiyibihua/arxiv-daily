---
layout: default
title: "MoniRefer: A Real-world Large-scale Multi-modal Dataset based on Roadside Infrastructure for 3D Visual Grounding"
---

# MoniRefer: A Real-world Large-scale Multi-modal Dataset based on Roadside Infrastructure for 3D Visual Grounding

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.24605" class="toolbar-btn" target="_blank">📄 arXiv: 2512.24605v1</a>
  <a href="https://arxiv.org/pdf/2512.24605.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.24605v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.24605v1', 'MoniRefer: A Real-world Large-scale Multi-modal Dataset based on Roadside Infrastructure for 3D Visual Grounding')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Panquan Yang, Junfei Huang, Zongzhangbao Yin, Yingsong Hu, Anni Xu, Xinyi Luo, Xueqi Sun, Hai Wu, Sheng Ao, Zhaoxing Zhu, Chenglu Wen, Cheng Wang

**分类**: cs.CV

**发布日期**: 2025-12-31

**备注**: 14 pages

---

## 💡 一句话要点

**提出MoniRefer数据集，用于路侧基础设施的3D视觉定位任务**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `3D视觉定位` `多模态融合` `路侧基础设施` `智能交通` `点云处理`

## 📋 核心要点

1. 现有3D视觉定位数据集主要集中在室内和自动驾驶场景，缺乏路侧基础设施视角的户外监控场景数据。
2. 提出MoniRefer数据集和Moni3DVG方法，利用图像外观信息和点云几何、光学信息进行多模态特征学习和3D对象定位。
3. 实验结果表明，Moni3DVG方法在MoniRefer数据集上表现出优越性和有效性，为路侧3D视觉定位提供新基准。

## 📝 摘要（中文）

本文提出了一种新的任务：面向户外监控场景的3D视觉定位，旨在实现基础设施级别的交通场景理解，超越了自车视角。为此，构建了MoniRefer，这是第一个真实世界的大规模多模态数据集，用于路侧级别的3D视觉定位。该数据集包含约136,018个对象，以及从真实环境中的多个复杂交通路口收集的411,128个自然语言表达式。为了确保数据集的质量和准确性，我们手动验证了所有语言描述和对象的3D标签。此外，还提出了一种新的端到端方法Moni3DVG，该方法利用图像提供的丰富外观信息以及点云提供的几何和光学信息进行多模态特征学习和3D对象定位。在提出的基准上进行的大量实验和消融研究证明了该方法的优越性和有效性。数据集和代码将会开源。

## 🔬 方法详解

**问题定义**：论文旨在解决路侧基础设施视角下的3D视觉定位问题，即根据自然语言描述在3D点云场景中定位目标对象。现有方法和数据集主要集中在室内和自动驾驶场景，缺乏对路侧监控场景的有效支持，无法满足智能交通系统对基础设施级别场景理解的需求。

**核心思路**：论文的核心思路是构建一个大规模、高质量的路侧3D视觉定位数据集（MoniRefer），并提出一个端到端的多模态融合方法（Moni3DVG）。通过结合图像提供的丰富外观信息和点云提供的几何、光学信息，实现更准确的3D对象定位。

**技术框架**：Moni3DVG方法是一个端到端的框架，主要包含以下模块：1) 多模态特征提取模块，分别从图像和点云中提取特征；2) 特征融合模块，将图像和点云特征进行融合；3) 3D对象定位模块，根据融合后的特征预测3D bounding box。

**关键创新**：论文的关键创新在于：1) 构建了首个大规模路侧3D视觉定位数据集MoniRefer，填补了该领域的数据空白；2) 提出了Moni3DVG方法，有效融合了图像和点云的多模态信息，提高了3D对象定位的准确性。与现有方法相比，Moni3DVG更关注路侧场景的特点，并针对性地设计了多模态融合策略。

**关键设计**：Moni3DVG方法在特征提取方面，图像分支可能采用预训练的CNN模型（如ResNet），点云分支可能采用PointNet++等点云处理网络。在特征融合方面，可能采用注意力机制或跨模态Transformer等方法，学习不同模态之间的关联性。损失函数可能包括定位损失（如IoU loss）和分类损失（如交叉熵损失）。具体网络结构和参数设置在论文中应该有详细描述，但根据摘要信息无法得知。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.24605v1/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.24605v1/x2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.24605v1/x3.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

论文提出的Moni3DVG方法在MoniRefer数据集上进行了实验验证，结果表明该方法在3D对象定位方面取得了显著的性能提升。具体的性能数据（如定位精度、召回率等）以及与现有基线方法的对比结果需要在论文中查找。摘要中提到“extensive experiments and ablation studies on the proposed benchmarks demonstrate the superiority and effectiveness of our method”，表明该方法具有较强的竞争力。

## 🎯 应用场景

该研究成果可应用于智能交通系统、智慧城市等领域。通过路侧基础设施对交通场景进行3D视觉定位，可以实现更精确的交通监控、事件检测和自动驾驶辅助，提升交通效率和安全性。未来，该技术有望应用于更广泛的户外监控场景，例如安防监控、环境监测等。

## 📄 摘要（原文）

> 3D visual grounding aims to localize the object in 3D point cloud scenes that semantically corresponds to given natural language sentences. It is very critical for roadside infrastructure system to interpret natural languages and localize relevant target objects in complex traffic environments. However, most existing datasets and approaches for 3D visual grounding focus on the indoor and outdoor driving scenes, outdoor monitoring scenarios remain unexplored due to scarcity of paired point cloud-text data captured by roadside infrastructure sensors. In this paper, we introduce a novel task of 3D Visual Grounding for Outdoor Monitoring Scenarios, which enables infrastructure-level understanding of traffic scenes beyond the ego-vehicle perspective. To support this task, we construct MoniRefer, the first real-world large-scale multi-modal dataset for roadside-level 3D visual grounding. The dataset consists of about 136,018 objects with 411,128 natural language expressions collected from multiple complex traffic intersections in the real-world environments. To ensure the quality and accuracy of the dataset, we manually verified all linguistic descriptions and 3D labels for objects. Additionally, we also propose a new end-to-end method, named Moni3DVG, which utilizes the rich appearance information provided by images and geometry and optical information from point cloud for multi-modal feature learning and 3D object localization. Extensive experiments and ablation studies on the proposed benchmarks demonstrate the superiority and effectiveness of our method. Our dataset and code will be released.

