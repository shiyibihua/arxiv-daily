---
layout: default
title: Robust Robotic Exploration and Mapping Using Generative Occupancy Map Synthesis
---

# Robust Robotic Exploration and Mapping Using Generative Occupancy Map Synthesis

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.20049" class="toolbar-btn" target="_blank">📄 arXiv: 2506.20049v1</a>
  <a href="https://arxiv.org/pdf/2506.20049.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.20049v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.20049v1', 'Robust Robotic Exploration and Mapping Using Generative Occupancy Map Synthesis')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Lorin Achey, Alec Reed, Brendan Crowe, Bradley Hayes, Christoffer Heckman

**分类**: cs.RO, cs.AI

**发布日期**: 2025-06-24

**备注**: arXiv admin note: text overlap with arXiv:2409.10681

---

## 💡 一句话要点

**提出SceneSense以解决机器人探索与映射中的不确定性问题**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱三：空间感知与语义 (Perception & Semantics)**

**关键词**: `生成占用图` `机器人探索` `扩散模型` `实时数据融合` `地图质量提升`

## 📋 核心要点

1. 现有的机器人探索方法在处理不完整观察数据时，往往导致地图质量低下和可通行性差。
2. 论文提出的SceneSense模型通过生成占用图，能够在实时环境中融合部分观察数据，提升地图的准确性。
3. 实验结果表明，使用SceneSense增强的地图在多个环境中表现出更高的探索一致性和更好的性能提升。

## 📝 摘要（中文）

我们提出了一种新颖的方法，通过生成占用映射来增强机器人探索。我们引入了SceneSense，这是一个专为根据部分观察预测3D占用图而设计和训练的扩散模型。我们的方案实时地将这些预测概率性地融合到运行中的占用图中，显著提高了地图质量和可通行性。我们在四足机器人上实现了SceneSense，并通过实际实验验证了其性能，结果显示，增强的占用图更好地代表了完全观察到的真实数据，周围区域的FID改善达24.44%，远程区域改善达75.59%。此外，将SceneSense增强的地图作为“即插即用”的地图改进集成到现有的规划器中，提升了鲁棒性和可通行时间。最后，我们在两个不同环境中进行了全面的探索评估，发现局部增强的地图提供了比仅依赖直接传感器测量构建的地图更一致的探索结果。

## 🔬 方法详解

**问题定义**：本论文旨在解决机器人在探索过程中由于观察数据不完整而导致的占用图质量低下和可通行性差的问题。现有方法通常依赖于直接传感器测量，难以有效处理不确定性。

**核心思路**：论文的核心解决思路是利用生成模型SceneSense，通过扩散模型生成3D占用图，并将其与实时数据融合，从而提高地图的质量和可通行性。这样的设计使得机器人能够在动态和复杂环境中更好地进行探索。

**技术框架**：整体架构包括三个主要模块：首先是数据采集模块，负责获取传感器数据；其次是SceneSense模型，负责生成占用图；最后是融合模块，将生成的占用图与实时数据结合，形成最终的运行占用图。

**关键创新**：最重要的技术创新在于引入了基于扩散模型的生成占用图方法，这与传统的基于传感器数据的映射方法有本质区别，能够更好地处理不确定性和局部信息。

**关键设计**：在模型设计中，采用了特定的损失函数以优化生成图的准确性，并通过调整网络结构来提高模型的生成能力，确保其在不同环境下的适应性和鲁棒性。具体参数设置和网络结构细节在论文中进行了详细描述。

## 📊 实验亮点

实验结果显示，使用SceneSense增强的占用图在周围区域的FID指标改善了24.44%，在远程区域改善了75.59%。此外，集成SceneSense的地图作为“即插即用”的改进，显著提升了机器人探索的鲁棒性和可通行时间，展示了其在实际应用中的有效性。

## 🎯 应用场景

该研究的潜在应用领域包括自主机器人导航、无人驾驶汽车、以及复杂环境下的搜索与救援任务。通过提升地图质量和可通行性，SceneSense能够显著提高机器人在未知环境中的探索效率和安全性，未来可能在智能城市和工业自动化等领域发挥重要作用。

## 📄 摘要（原文）

> We present a novel approach for enhancing robotic exploration by using generative occupancy mapping. We introduce SceneSense, a diffusion model designed and trained for predicting 3D occupancy maps given partial observations. Our proposed approach probabilistically fuses these predictions into a running occupancy map in real-time, resulting in significant improvements in map quality and traversability. We implement SceneSense onboard a quadruped robot and validate its performance with real-world experiments to demonstrate the effectiveness of the model. In these experiments, we show that occupancy maps enhanced with SceneSense predictions better represent our fully observed ground truth data (24.44% FID improvement around the robot and 75.59% improvement at range). We additionally show that integrating SceneSense-enhanced maps into our robotic exploration stack as a "drop-in" map improvement, utilizing an existing off-the-shelf planner, results in improvements in robustness and traversability time. Finally we show results of full exploration evaluations with our proposed system in two dissimilar environments and find that locally enhanced maps provide more consistent exploration results than maps constructed only from direct sensor measurements.

