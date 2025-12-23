---
layout: default
title: Learning Smooth State-Dependent Traversability from Dense Point Clouds
---

# Learning Smooth State-Dependent Traversability from Dense Point Clouds

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.04362" class="toolbar-btn" target="_blank">📄 arXiv: 2506.04362v2</a>
  <a href="https://arxiv.org/pdf/2506.04362.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.04362v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.04362v2', 'Learning Smooth State-Dependent Traversability from Dense Point Clouds')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zihao Dong, Alan Papalia, Leonard Jung, Alenna Spiro, Philip R. Osteen, Christa S. Robison, Michael Everett

**分类**: cs.RO, cs.CV

**发布日期**: 2025-06-04 (更新: 2025-09-29)

**备注**: 18 pages, 13 figures

**🔗 代码/项目**: [GITHUB](https://github.com/neu-autonomy/SPARTA)

---

## 💡 一句话要点

**提出SPARTA以解决越野自主驾驶中的地形可通行性问题**

🎯 **匹配领域**: **支柱三：空间感知与语义 (Perception & Semantics)**

**关键词**: `越野自主驾驶` `地形可通行性` `点云处理` `傅里叶基函数` `风险预测` `机器人导航` `模型泛化`

## 📋 核心要点

1. 现有方法在越野自主驾驶中面临地形可通行性依赖车辆状态的挑战，尤其是接近角度的影响。
2. 本文提出SPARTA，通过将几何结构引入网络，输出平滑的解析函数来预测接近角度的风险分布，减少计算开销。
3. 在高保真模拟平台上，SPARTA模型在穿越40米岩石场时成功率达到91%，显著高于基线的73%。

## 📝 摘要（中文）

在越野自主驾驶中，地形的可通行性通常依赖于车辆的状态，尤其是某些障碍物仅在特定方向上可通行。现有方法需要大量多样的训练数据，并在规划时因重复模型推理而计算效率低下。为此，本文提出SPARTA，一种基于点云估计接近角度条件下的可通行性的方法。该方法通过输出平滑的解析函数，预测任意接近角度的风险分布，具有较小的开销并可重复使用。SPARTA在高保真模拟平台上实现了91%的成功率，显著优于基线的73%。

## 🔬 方法详解

**问题定义**：本文旨在解决越野自主驾驶中地形可通行性与车辆接近角度之间的复杂关系。现有方法需要大量训练数据，且在规划时计算效率低下。

**核心思路**：SPARTA通过输出一个平滑的解析函数来预测任意接近角度的风险分布，利用傅里叶基函数的周期性和光滑性，提升模型的泛化能力。

**技术框架**：SPARTA的整体架构包括输入点云数据，经过网络处理后输出风险分布。该方法通过几何结构的引入，确保了输出的平滑性和可重复使用性。

**关键创新**：SPARTA的主要创新在于将几何结构与傅里叶基函数结合，形成一个高效的风险预测模型，显著减少了计算开销，并提高了模型的泛化能力。

**关键设计**：在网络设计中，采用傅里叶基函数作为输出层，确保风险分布的平滑性。此外，损失函数的设计也考虑了输出的连续性和准确性，以优化模型性能。

## 📊 实验亮点

SPARTA在高保真模拟平台上实现了91%的成功率，成功穿越40米的岩石场，相较于基线模型的73%提升了18个百分点，展示了其在实际应用中的优越性能和强大的泛化能力。

## 🎯 应用场景

该研究在越野自主驾驶领域具有广泛的应用潜力，尤其是在复杂地形的导航和障碍物避让方面。SPARTA的高效性和准确性使其能够在实际环境中有效应用，推动无人驾驶技术的进步。未来，该方法还可以扩展到其他需要考虑状态依赖性的机器人导航任务中。

## 📄 摘要（原文）

> A key open challenge in off-road autonomy is that the traversability of terrain often depends on the vehicle's state. In particular, some obstacles are only traversable from some orientations. However, learning this interaction by encoding the angle of approach as a model input demands a large and diverse training dataset and is computationally inefficient during planning due to repeated model inference. To address these challenges, we present SPARTA, a method for estimating approach angle conditioned traversability from point clouds. Specifically, we impose geometric structure into our network by outputting a smooth analytical function over the 1-Sphere that predicts risk distribution for any angle of approach with minimal overhead and can be reused for subsequent queries. The function is composed of Fourier basis functions, which has important advantages for generalization due to their periodic nature and smoothness. We demonstrate SPARTA both in a high-fidelity simulation platform, where our model achieves a 91\% success rate crossing a 40m boulder field (compared to 73\% for the baseline), and on hardware, illustrating the generalization ability of the model to real-world settings. Our code will be available at https://github.com/neu-autonomy/SPARTA.

