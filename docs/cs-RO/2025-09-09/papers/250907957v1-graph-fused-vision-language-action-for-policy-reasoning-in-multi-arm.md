---
layout: default
title: Graph-Fused Vision-Language-Action for Policy Reasoning in Multi-Arm Robotic Manipulation
---

# Graph-Fused Vision-Language-Action for Policy Reasoning in Multi-Arm Robotic Manipulation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.07957" class="toolbar-btn" target="_blank">📄 arXiv: 2509.07957v1</a>
  <a href="https://arxiv.org/pdf/2509.07957.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.07957v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.07957v1', 'Graph-Fused Vision-Language-Action for Policy Reasoning in Multi-Arm Robotic Manipulation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Shunlei Li, Longsen Gao, Jiuwen Cao, Yingbai Hu

**分类**: cs.RO

**发布日期**: 2025-09-09

**备注**: This paper is submitted to IEEE IROS 2025 Workshop AIR4S

---

## 💡 一句话要点

**提出Graph-Fused VLA框架，解决双臂机器人从人类演示中学习复杂操作策略的问题。**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `双臂机器人` `模仿学习` `视觉语言动作` `场景图` `任务规划`

## 📋 核心要点

1. 传统机器人技能学习依赖低级轨迹复制，难以泛化到不同物体、布局和机器人配置。
2. GF-VLA框架通过信息论提取关键交互线索，构建场景图，并结合语言条件Transformer生成分层行为树。
3. 实验表明，GF-VLA在双臂机器人任务中实现了高准确率和成功率，展现了强大的泛化能力。

## 📝 摘要（中文）

本文提出了一种名为Graph-Fused Vision-Language-Action (GF-VLA) 的统一框架，旨在使双臂机器人系统能够直接从RGB-D人类演示中进行任务级推理和执行。GF-VLA采用信息论方法提取任务相关线索，选择性地突出关键的手-物和物-物交互。这些线索被构建成时间排序的场景图，然后与语言条件Transformer集成，以生成分层行为树和可解释的笛卡尔运动原语。为了提高双手动执行的效率，我们提出了一种跨臂分配策略，该策略可以自动确定夹具分配，而无需显式的几何建模。在涉及符号结构构建和空间泛化的四个双臂积木组装基准上验证了GF-VLA。实验结果表明，所提出的表示实现了超过95%的图准确率和93%的子任务分割准确率，使语言-动作规划器能够生成鲁棒、可解释的任务策略。当部署在双臂机器人上时，这些策略在堆叠、字母形成和几何重构任务中实现了94%的抓取可靠性、89%的放置准确性和90%的总体任务成功率，证明了在各种空间和语义变化下的强大泛化性和鲁棒性。

## 🔬 方法详解

**问题定义**：现有机器人从人类演示中学习技能的方法，通常依赖于低层次的轨迹复现，这导致了在面对不同的物体、空间布局以及机器人配置时，泛化能力不足。尤其是在双臂机器人操作中，如何有效地进行任务分解、动作规划以及双臂协同是一个挑战。

**核心思路**：本文的核心思路是将视觉信息、语言信息和动作信息融合到一个统一的框架中，利用信息论方法提取任务相关的关键线索，并将其表示为时序场景图。然后，利用语言条件Transformer将场景图转化为分层的行为树和可解释的运动原语，从而实现任务级的推理和执行。

**技术框架**：GF-VLA框架主要包含以下几个模块：1) 视觉信息提取模块，利用RGB-D图像提取场景中的物体和它们之间的关系；2) 信息论线索提取模块，通过信息论方法选择性地突出关键的手-物和物-物交互；3) 场景图构建模块，将提取的线索构建成时间排序的场景图；4) 语言条件Transformer模块，将场景图和语言指令作为输入，生成分层的行为树和运动原语；5) 跨臂分配策略模块，自动确定夹具分配，无需显式的几何建模。

**关键创新**：该论文的关键创新在于：1) 提出了一种基于信息论的线索提取方法，能够有效地提取任务相关的关键交互信息；2) 将视觉、语言和动作信息融合到一个统一的框架中，实现了任务级的推理和执行；3) 提出了一种跨臂分配策略，能够自动确定夹具分配，提高了双臂操作的效率。

**关键设计**：论文中使用了Transformer网络进行序列建模，并使用语言指令作为条件来指导行为树的生成。此外，信息论线索提取模块的具体实现细节（例如，使用的信息论指标、阈值设置等）以及跨臂分配策略的具体算法是关键的设计细节。具体的损失函数和网络结构细节在论文中可能有所描述，但摘要中未提及。

## 📊 实验亮点

实验结果表明，GF-VLA在四个双臂积木组装基准上取得了显著的成果。该方法实现了超过95%的图准确率和93%的子任务分割准确率。在实际的双臂机器人部署中，该方法实现了94%的抓取可靠性、89%的放置准确性和90%的总体任务成功率，证明了其在不同空间和语义变化下的强大泛化性和鲁棒性。

## 🎯 应用场景

该研究成果可应用于自动化装配、智能制造、医疗机器人等领域。通过学习人类的操作演示，机器人能够完成复杂的装配任务，提高生产效率和灵活性。在医疗领域，该技术可用于辅助医生进行手术操作，提高手术精度和安全性。未来，该技术有望实现更高级别的自主操作和人机协作。

## 📄 摘要（原文）

> Acquiring dexterous robotic skills from human video demonstrations remains a significant challenge, largely due to conventional reliance on low-level trajectory replication, which often fails to generalize across varying objects, spatial layouts, and manipulator configurations. To address this limitation, we introduce Graph-Fused Vision-Language-Action (GF-VLA), a unified framework that enables dual-arm robotic systems to perform task-level reasoning and execution directly from RGB-D human demonstrations. GF-VLA employs an information-theoretic approach to extract task-relevant cues, selectively highlighting critical hand-object and object-object interactions. These cues are structured into temporally ordered scene graphs, which are subsequently integrated with a language-conditioned transformer to produce hierarchical behavior trees and interpretable Cartesian motion primitives. To enhance efficiency in bimanual execution, we propose a cross-arm allocation strategy that autonomously determines gripper assignment without requiring explicit geometric modeling. We validate GF-VLA on four dual-arm block assembly benchmarks involving symbolic structure construction and spatial generalization. Empirical results demonstrate that the proposed representation achieves over 95% graph accuracy and 93% subtask segmentation, enabling the language-action planner to generate robust, interpretable task policies. When deployed on a dual-arm robot, these policies attain 94% grasp reliability, 89% placement accuracy, and 90% overall task success across stacking, letter-formation, and geometric reconfiguration tasks, evidencing strong generalization and robustness under diverse spatial and semantic variations.

