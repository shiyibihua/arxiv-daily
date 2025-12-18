---
layout: default
title: Where Did I Leave My Glasses? Open-Vocabulary Semantic Exploration in Real-World Semi-Static Environments
---

# Where Did I Leave My Glasses? Open-Vocabulary Semantic Exploration in Real-World Semi-Static Environments

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.19851" class="toolbar-btn" target="_blank">📄 arXiv: 2509.19851v1</a>
  <a href="https://arxiv.org/pdf/2509.19851.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.19851v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.19851v1', 'Where Did I Leave My Glasses? Open-Vocabulary Semantic Exploration in Real-World Semi-Static Environments')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Benjamin Bogenberger, Oliver Harrison, Orrin Dahanaggamaarachchi, Lukas Brunke, Jingxing Qian, Siqi Zhou, Angela P. Schoellig

**分类**: cs.RO

**发布日期**: 2025-09-24

---

## 💡 一句话要点

**提出一种开放词汇语义探索系统，用于真实半静态环境中进行对象级别的长期跟踪和导航。**

🎯 **匹配领域**: **支柱三：空间感知与语义 (Perception & Semantics)**

**关键词**: `语义探索` `半静态环境` `对象跟踪` `主动探索` `LLM推理` `机器人导航` `环境感知`

## 📋 核心要点

1. 现有语义探索主要关注静态场景，缺乏对对象级别实例的持久跟踪，这限制了其在物体可能移动或移除的真实环境中的应用。
2. 该论文提出了一种开放词汇语义探索系统，通过概率模型跟踪对象实例的稳定性，并结合LLM进行上下文推理，实现高效的地图维护和目标导航。
3. 实验结果表明，该系统能够有效检测环境变化，显著提升探索效率，并在对象目标导航任务中优于现有方法。

## 📝 摘要（中文）

本文提出了一种用于真实半静态环境的开放词汇语义探索系统。该系统通过构建对象实例稳定性的概率模型来维护一致的地图，系统地跟踪半静态变化，并主动探索长时间未访问的区域。除了主动地图维护外，该方法还利用地图的语义丰富性，通过基于LLM的推理进行开放词汇对象目标导航，从而通过优先考虑上下文相关的区域来更有效地搜索。在多个真实半静态环境中评估了该方法，系统平均检测到95%的地图变化，与随机和巡逻基线相比，效率提高了29%以上。总体而言，该方法实现了在完全重建地图的2%以内的映射精度，同时需要更少的探索，并且比次优策略（覆盖巡逻）更快地完成约14%的对象目标导航任务。

## 🔬 方法详解

**问题定义**：现有语义探索方法主要关注静态环境，无法有效处理真实世界中物体位置变化或移除的情况。缺乏对物体实例的长期跟踪和对环境变化的适应能力，导致地图不一致，影响机器人任务的执行效率。现有方法难以利用语义信息进行高效的探索和导航。

**核心思路**：该论文的核心思路是构建一个能够适应半静态环境的语义地图，通过概率模型来跟踪物体实例的稳定性，并利用大型语言模型（LLM）进行上下文推理，从而实现高效的地图维护和对象目标导航。通过主动探索长时间未访问的区域，及时发现环境变化。

**技术框架**：该系统包含以下主要模块：1) 语义地图构建模块，用于构建和维护环境的语义地图，包括物体的位置、类别和稳定性信息。2) 变化检测模块，通过比较当前观测和历史地图，检测环境中的变化。3) 主动探索模块，根据变化检测的结果和LLM的推理，确定需要探索的区域。4) 对象目标导航模块，利用语义地图和LLM的推理，规划到达目标物体的路径。

**关键创新**：该论文的关键创新在于：1) 提出了一个基于概率模型的物体实例稳定性跟踪方法，能够有效处理半静态环境中的物体位置变化。2) 将大型语言模型（LLM）引入到语义探索中，利用LLM进行上下文推理，从而实现更高效的探索和导航。3) 提出了一个主动探索策略，能够根据环境变化和LLM的推理，动态调整探索目标。

**关键设计**：论文中使用了基于深度学习的物体检测和分割模型来提取环境中的物体信息。概率模型用于估计物体实例的稳定性，并根据观测结果进行更新。LLM用于推理物体之间的关系，并指导探索方向。主动探索策略根据信息增益和探索成本来选择探索目标。具体的参数设置和损失函数等技术细节在论文中有详细描述（未知）。

## 📊 实验亮点

该系统在真实半静态环境中进行了评估，结果表明，该系统能够平均检测到95%的地图变化，与随机和巡逻基线相比，效率提高了29%以上。在映射精度方面，该方法实现了在完全重建地图的2%以内的精度，同时需要更少的探索。此外，该系统在对象目标导航任务中比次优策略（覆盖巡逻）快约14%。

## 🎯 应用场景

该研究成果可应用于家庭服务机器人、仓库管理机器人、安防巡逻机器人等领域。通过构建能够适应环境变化的语义地图，机器人可以更好地理解周围环境，更有效地完成各种任务，例如寻找特定物品、执行清洁任务、进行安全巡逻等。该研究有助于提升机器人在真实世界中的自主性和智能化水平。

## 📄 摘要（原文）

> Robots deployed in real-world environments, such as homes, must not only navigate safely but also understand their surroundings and adapt to environment changes. To perform tasks efficiently, they must build and maintain a semantic map that accurately reflects the current state of the environment. Existing research on semantic exploration largely focuses on static scenes without persistent object-level instance tracking. A consistent map is, however, crucial for real-world robotic applications where objects in the environment can be removed, reintroduced, or shifted over time. In this work, to close this gap, we propose an open-vocabulary, semantic exploration system for semi-static environments. Our system maintains a consistent map by building a probabilistic model of object instance stationarity, systematically tracking semi-static changes, and actively exploring areas that have not been visited for a prolonged period of time. In addition to active map maintenance, our approach leverages the map's semantic richness with LLM-based reasoning for open-vocabulary object-goal navigation. This enables the robot to search more efficiently by prioritizing contextually relevant areas. We evaluate our approach across multiple real-world semi-static environments. Our system detects 95% of map changes on average, improving efficiency by more than 29% as compared to random and patrol baselines. Overall, our approach achieves a mapping precision within 2% of a fully rebuilt map while requiring substantially less exploration and further completes object goal navigation tasks about 14% faster than the next-best tested strategy (coverage patrolling). A video of our work can be found at http://tiny.cc/sem-explor-semi-static .

