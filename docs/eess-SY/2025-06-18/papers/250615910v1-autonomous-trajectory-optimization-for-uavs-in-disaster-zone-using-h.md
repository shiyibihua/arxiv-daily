---
layout: default
title: Autonomous Trajectory Optimization for UAVs in Disaster Zone Using Henry Gas Optimization Scheme
---

# Autonomous Trajectory Optimization for UAVs in Disaster Zone Using Henry Gas Optimization Scheme

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.15910" class="toolbar-btn" target="_blank">📄 arXiv: 2506.15910v1</a>
  <a href="https://arxiv.org/pdf/2506.15910.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.15910v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.15910v1', 'Autonomous Trajectory Optimization for UAVs in Disaster Zone Using Henry Gas Optimization Scheme')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zakria Qadir, Muhammad Bilal, Guoqiang Liu, Xiaolong Xu

**分类**: eess.SY, cs.DC, cs.NI

**发布日期**: 2025-06-18

**备注**: 12 pages, 9 figuers

---

## 💡 一句话要点

**提出亨利气体优化方案以解决无人机灾区自主轨迹优化问题**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)**

**关键词**: `无人机` `轨迹优化` `亨利气体优化` `集群优化` `灾害响应` `智能城市` `元启发式算法`

## 📋 核心要点

1. 无人机在灾区的轨迹优化面临复杂环境下路径选择的挑战，现有方法在效率和成本上存在不足。
2. 本文提出的集群优化方案（COS）利用亨利气体优化算法，旨在寻找最短路径以降低运输成本和计算复杂度。
3. 实验结果表明，HGO算法在多种环境下均优于现有算法，特别是在环境友好场景中显著降低了运输成本和计算时间。

## 📝 摘要（中文）

在灾害易发环境中，无人机（UAV）在协助救援服务和提供互联网连接方面发挥着重要作用。然而，在复杂环境中，选择无人机的最佳轨迹至关重要。本文提出了一种基于亨利气体优化（HGO）元启发式算法的集群优化方案（COS），旨在识别具有最低运输成本和算法复杂度的最短路径。通过与粒子群优化（PSO）、灰狼优化（GWO）、布谷鸟搜索算法（CSA）和海葵交配优化器（BMO）等先进算法进行比较，证明了该模型的鲁棒性。在不同环境场景下，HGO算法均表现优异，尤其在环境友好场景中，相较于PSO算法，运输成本降低了39.3%，计算时间减少了16.8%。

## 🔬 方法详解

**问题定义**：本文旨在解决无人机在灾区环境中轨迹优化的问题，现有方法在复杂环境下的路径选择效率和成本控制上存在不足。

**核心思路**：通过引入亨利气体优化算法，设计集群优化方案（COS），以实现最短路径的识别，降低运输成本和算法复杂度。

**技术框架**：整体架构包括环境建模、路径搜索和优化算法三个主要模块。首先对环境进行建模，然后利用HGO算法进行路径搜索，最后优化结果以实现最优轨迹。

**关键创新**：HGO算法作为一种新型的元启发式算法，其在复杂环境下的应用展现出优越性，尤其是在运输成本和计算时间方面的显著降低，与现有算法相比具有本质区别。

**关键设计**：在算法设计中，关键参数包括环境模型的构建、适应度函数的定义以及算法迭代过程中的参数调节，以确保优化效果的最大化。具体的损失函数和网络结构细节在论文中进行了详细描述。

## 📊 实验亮点

实验结果显示，HGO算法在环境友好场景中相较于PSO算法，运输成本降低了39.3%，计算时间减少了16.8%。在其他复杂环境下，HGO算法同样表现出色，证明了其在无人机轨迹优化中的有效性和优越性。

## 🎯 应用场景

该研究的潜在应用领域包括智能城市的无人机救援、灾后恢复和基础设施监测等。通过优化无人机的轨迹，可以显著提升救援效率和资源配置，具有重要的实际价值和社会影响。

## 📄 摘要（原文）

> The unmanned aerial vehicles (UAVs) in a disaster-prone environment plays important role in assisting the rescue services and providing the internet connectivity with the outside world. However, in such a complex environment the selection of optimum trajectory of UAVs is of utmost importance. UAV trajectory optimization deals with finding the shortest path in the minimal possible time. In this paper, a cluster optimization scheme (COS) is proposed using the Henry gas optimization (HGO) metaheuristic algorithm to identify the shortest path having minimal transportation cost and algorithm complexity. The mathematical model is designed for COS using the HGO algorithm and compared with the state-of-the-art metaheuristic algorithms such as particle swarm optimization (PSO), grey wolf optimization (GWO), cuckoo search algorithm (CSA) and barnacles mating optimizer (BMO). In order to prove the robustness of the proposed model, four different scenarios are evaluated that includes ambient environment, constrict environment, tangled environment, and complex environment. In all the aforementioned scenarios, the HGO algorithm outperforms the existing algorithms. Particularly, in the ambient environment, the HGO algorithm achieves a 39.3% reduction in transportation cost and a 16.8% reduction in computational time as compared to the PSO algorithm. Hence, the HGO algorithm can be used for autonomous trajectory optimization of UAVs in smart cities.

