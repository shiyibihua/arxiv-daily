---
layout: default
title: Open-Vocabulary Spatio-Temporal Scene Graph for Robot Perception and Teleoperation Planning
---

# Open-Vocabulary Spatio-Temporal Scene Graph for Robot Perception and Teleoperation Planning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.23107" class="toolbar-btn" target="_blank">📄 arXiv: 2509.23107v2</a>
  <a href="https://arxiv.org/pdf/2509.23107.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.23107v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.23107v2', 'Open-Vocabulary Spatio-Temporal Scene Graph for Robot Perception and Teleoperation Planning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yi Wang, Zeyu Xue, Mujie Liu, Tongqin Zhang, Yan Hu, Zhou Zhao, Chenguang Yang, Zhenyu Lu

**分类**: cs.RO, cs.AI

**发布日期**: 2025-09-27 (更新: 2025-10-27)

---

## 💡 一句话要点

**提出时空开放词汇场景图(ST-OVSG)，增强机器人远程操作在时延下的规划鲁棒性。**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱三：空间感知与语义 (Perception & Semantics)**

**关键词**: `远程操作` `时空场景图` `开放词汇` `视觉语言模型` `机器人规划` `时延鲁棒性` `场景理解`

## 📋 核心要点

1. 远程操作中，双向通信时延导致远程感知状态与操作者意图不一致，造成指令误解和错误执行。
2. 提出ST-OVSG，通过时空场景图和时延标签，使LVLM规划器能回顾过去状态，解决状态不匹配问题。
3. 实验表明，ST-OVSG在Replica数据集上节点准确率达74%，且显著提升了LVLM规划器在时延下的规划成功率。

## 📝 摘要（中文）

本文提出时空开放词汇场景图(ST-OVSG)，旨在解决远程操作中因通信时延导致远程感知状态与操作者意图不匹配的问题。ST-OVSG利用大型视觉语言模型(LVLM)构建开放词汇3D对象表示，并通过匈牙利算法和时间匹配代价将其扩展到时域，形成统一的时空场景图。嵌入时延标签使LVLM规划器能够回顾过去场景状态，从而解决由传输延迟引起的本地-远程状态不匹配。此外，提出面向任务的子图过滤策略，生成紧凑的规划器输入。ST-OVSG无需微调即可泛化到新类别，并增强规划对传输延迟的鲁棒性。实验表明，该方法在Replica基准测试中实现了74%的节点准确率，优于ConceptGraph。在延迟鲁棒性实验中，ST-OVSG辅助的LVLM规划器实现了70.5%的规划成功率。

## 🔬 方法详解

**问题定义**：远程操作中，由于通信时延，机器人接收到的环境信息与操作员的意图存在时间差，导致规划出现偏差甚至失败。现有方法难以有效处理这种时延带来的状态不确定性，尤其是在动态环境中。现有场景图构建方法难以有效处理开放词汇场景，且缺乏对时序信息的建模。

**核心思路**：核心在于构建一个能够感知时空信息，并且能够处理开放词汇的场景图。通过将视觉语言模型与时序信息相结合，并引入时延标签，使得规划器能够回顾过去的状态，从而弥补因时延造成的信息不对称。同时，通过任务相关的子图过滤，减少冗余信息，提高规划效率。

**技术框架**：ST-OVSG的构建流程主要包含以下几个阶段：1) 利用LVLM构建开放词汇的3D对象表示；2) 通过匈牙利算法和时间匹配代价，将3D对象表示扩展到时域，构建时空场景图；3) 嵌入时延标签，记录每个对象的状态信息对应的时间戳；4) 根据任务需求，进行子图过滤，提取关键信息。

**关键创新**：主要创新点在于：1) 提出了时空开放词汇场景图(ST-OVSG)，将开放词汇感知与时序动态信息相结合；2) 引入了时延标签，使得规划器能够感知过去的状态；3) 提出了任务导向的子图过滤策略，减少了冗余信息，提高了规划效率。与现有方法相比，ST-OVSG能够更好地处理时延带来的状态不确定性，并且具有更强的泛化能力。

**关键设计**：时间匹配代价的设计是关键，用于在时间维度上关联不同的对象。具体的匹配代价函数未知，但可以推测其考虑了对象的位置、类别、属性等因素。子图过滤策略的具体实现也未知，但可以推测其利用了任务相关的先验知识，例如，只保留与任务目标相关的对象和关系。

## 📊 实验亮点

实验结果表明，ST-OVSG在Replica数据集上实现了74%的节点准确率，显著优于ConceptGraph。在模拟时延的实验中，ST-OVSG辅助的LVLM规划器实现了70.5%的规划成功率，验证了其在时延环境下的鲁棒性。这些结果表明，ST-OVSG能够有效提升远程操作的性能和可靠性。

## 🎯 应用场景

该研究成果可应用于各种需要远程操作的场景，例如：太空探索、深海作业、危险环境处理（如核泄漏、化工厂事故）、远程医疗等。通过提高远程操作的鲁棒性和效率，可以降低操作风险，扩展机器人的应用范围，并提升操作人员的安全性。

## 📄 摘要（原文）

> Teleoperation via natural-language reduces operator workload and enhances safety in high-risk or remote settings. However, in dynamic remote scenes, transmission latency during bidirectional communication creates gaps between remote perceived states and operator intent, leading to command misunderstanding and incorrect execution. To mitigate this, we introduce the Spatio-Temporal Open-Vocabulary Scene Graph (ST-OVSG), a representation that enriches open-vocabulary perception with temporal dynamics and lightweight latency annotations. ST-OVSG leverages LVLMs to construct open-vocabulary 3D object representations, and extends them into the temporal domain via Hungarian assignment with our temporal matching cost, yielding a unified spatio-temporal scene graph. A latency tag is embedded to enable LVLM planners to retrospectively query past scene states, thereby resolving local-remote state mismatches caused by transmission delays. To further reduce redundancy and highlight task-relevant cues, we propose a task-oriented subgraph filtering strategy that produces compact inputs for the planner. ST-OVSG generalizes to novel categories and enhances planning robustness against transmission latency without requiring fine-tuning. Experiments show that our method achieves 74 percent node accuracy on the Replica benchmark, outperforming ConceptGraph. Notably, in the latency-robustness experiment, the LVLM planner assisted by ST-OVSG achieved a planning success rate of 70.5 percent.

