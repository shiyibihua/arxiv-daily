---
layout: default
title: Depth Any Panoramas: A Foundation Model for Panoramic Depth Estimation
---

# Depth Any Panoramas: A Foundation Model for Panoramic Depth Estimation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.16913" class="toolbar-btn" target="_blank">📄 arXiv: 2512.16913v1</a>
  <a href="https://arxiv.org/pdf/2512.16913.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.16913v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.16913v1', 'Depth Any Panoramas: A Foundation Model for Panoramic Depth Estimation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Xin Lin, Meixi Song, Dizhe Zhang, Wenxuan Lu, Haodong Li, Bo Du, Ming-Hsuan Yang, Truong Nguyen, Lu Qi

**分类**: cs.CV

**发布日期**: 2025-12-18

**备注**: Project Page: https://insta360-research-team.github.io/DAP_website/

**🔗 代码/项目**: [PROJECT_PAGE](https://insta360-research-team.github.io/DAP_website/) | [PROJECT_PAGE](https://insta360-research-team.github.io/DAP)

---

## 💡 一句话要点

**提出全景深度估计基础模型DAP，提升跨场景距离的泛化能力。**

🎯 **匹配领域**: **支柱三：空间感知与语义 (Perception & Semantics)** **支柱七：动作重定向 (Motion Retargeting)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `全景深度估计` `基础模型` `数据闭环` `伪标签` `DINOv3` `几何一致性` `领域泛化`

## 📋 核心要点

1. 现有全景深度估计方法在处理不同场景距离和领域泛化性方面存在不足，尤其是在真实场景中。
2. 论文提出一种数据闭环范式，结合合成数据、真实数据和伪标签技术，构建大规模、多样化的训练数据集。
3. 采用DINOv3-Large作为骨干，并引入范围掩码头、清晰度优化和几何优化，提升模型鲁棒性和几何一致性。

## 📝 摘要（中文）

本文提出了一种全景度量深度基础模型，该模型能够泛化到各种场景距离。我们探索了一种数据闭环范式，从数据构建和框架设计的角度出发。我们通过结合公共数据集、来自UE5模拟器的高质量合成数据、文本到图像模型以及来自网络的真实全景图像，收集了一个大规模数据集。为了减少室内/室外和合成/真实数据之间的领域差距，我们引入了一个三阶段伪标签生成流程，为未标记图像生成可靠的真值。在模型方面，我们采用DINOv3-Large作为骨干网络，因为它具有强大的预训练泛化能力，并引入了一个即插即用的范围掩码头、以清晰度为中心的优化和以几何为中心的优化，以提高对不同距离的鲁棒性并加强跨视图的几何一致性。在多个基准测试（例如，Stanford2D3D、Matterport3D和Deep360）上的实验表明，该模型具有强大的性能和零样本泛化能力，尤其是在各种真实场景中具有鲁棒和稳定的度量预测。

## 🔬 方法详解

**问题定义**：全景深度估计旨在从单张全景图像中预测场景的深度信息。现有方法在处理不同场景距离（近距离、远距离）以及室内外场景的泛化能力上存在挑战。真实世界全景图像的标注成本高昂，导致训练数据不足，模型难以适应真实场景的复杂性。

**核心思路**：论文的核心思路是构建一个大规模、多样化的全景深度数据集，并设计一个能够有效利用该数据集进行训练的基础模型。通过数据闭环的方式，不断迭代优化数据集和模型，提升模型的泛化能力和鲁棒性。

**技术框架**：整体框架包含三个主要阶段：1) 数据收集与增强：结合公共数据集、UE5合成数据、文本到图像生成数据和真实网络图像，构建大规模数据集。2) 伪标签生成：采用三阶段伪标签流程，为未标注图像生成可靠的深度真值，缩小领域差距。3) 模型训练：使用DINOv3-Large作为骨干网络，并引入范围掩码头、清晰度优化和几何优化策略。

**关键创新**：论文的关键创新在于数据闭环范式和针对全景深度估计的优化策略。数据闭环通过伪标签生成，有效利用了未标注数据，提升了模型的泛化能力。范围掩码头、清晰度优化和几何优化则分别解决了不同场景距离的鲁棒性问题和跨视图的几何一致性问题。

**关键设计**：范围掩码头用于区分不同距离范围内的深度预测，提高模型对不同距离的敏感性。清晰度优化通过关注图像的清晰区域，提高深度预测的准确性。几何优化则通过约束相邻像素的深度关系，保证跨视图的几何一致性。具体损失函数的设计和参数设置在论文中有详细描述。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16913v1/x2.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16913v1/x3.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16913v1/x4.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

实验结果表明，该模型在Stanford2D3D、Matterport3D和Deep360等多个基准测试上取得了优异的性能，并展现出强大的零样本泛化能力。尤其是在真实场景中，该模型能够生成鲁棒且稳定的度量深度预测，显著优于现有方法。具体性能数据和对比结果可在论文中查阅。

## 🎯 应用场景

该研究成果可应用于机器人导航、虚拟现实/增强现实、三维重建、自动驾驶等领域。高质量的全景深度估计能够为这些应用提供更准确的环境感知信息，提升系统的性能和用户体验。未来，该模型可以进一步扩展到其他全景理解任务，例如语义分割、目标检测等。

## 📄 摘要（原文）

> In this work, we present a panoramic metric depth foundation model that generalizes across diverse scene distances. We explore a data-in-the-loop paradigm from the view of both data construction and framework design. We collect a large-scale dataset by combining public datasets, high-quality synthetic data from our UE5 simulator and text-to-image models, and real panoramic images from the web. To reduce domain gaps between indoor/outdoor and synthetic/real data, we introduce a three-stage pseudo-label curation pipeline to generate reliable ground truth for unlabeled images. For the model, we adopt DINOv3-Large as the backbone for its strong pre-trained generalization, and introduce a plug-and-play range mask head, sharpness-centric optimization, and geometry-centric optimization to improve robustness to varying distances and enforce geometric consistency across views. Experiments on multiple benchmarks (e.g., Stanford2D3D, Matterport3D, and Deep360) demonstrate strong performance and zero-shot generalization, with particularly robust and stable metric predictions in diverse real-world scenes. The project page can be found at: \href{https://insta360-research-team.github.io/DAP_website/} {https://insta360-research-team.github.io/DAP\_website/}

