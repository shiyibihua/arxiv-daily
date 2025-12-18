---
layout: default
title: Geometric Red-Teaming for Robotic Manipulation
---

# Geometric Red-Teaming for Robotic Manipulation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.12379" class="toolbar-btn" target="_blank">📄 arXiv: 2509.12379v1</a>
  <a href="https://arxiv.org/pdf/2509.12379.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.12379v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.12379v1', 'Geometric Red-Teaming for Robotic Manipulation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Divyam Goel, Yufei Wang, Tiancheng Wu, Guixiu Qiao, Pavel Piliptchak, David Held, Zackory Erickson

**分类**: cs.RO, cs.AI, cs.LG

**发布日期**: 2025-09-15

**备注**: Accepted at the 9th Annual Conference on Robot Learning (CoRL 2025, Oral)

---

## 💡 一句话要点

**提出几何红队（GRT）框架，通过几何扰动自动发现机器人操作策略的脆弱性。**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)**

**关键词**: `机器人操作` `鲁棒性评估` `几何红队` `对抗性样本` `策略优化`

## 📋 核心要点

1. 现有机器人操作评估主要依赖于精心设计的测试集，难以发现策略在真实变化下的潜在缺陷。
2. GRT通过引入物体为中心的几何扰动，自动生成导致策略失败的CrashShapes，从而探测策略的鲁棒性。
3. 实验表明，GRT能有效发现策略的脆弱点，且基于CrashShapes的微调能显著提升策略在特定形状上的性能。

## 📝 摘要（中文）

本文提出了一种名为几何红队（GRT）的红队框架，旨在通过以物体为中心的几何扰动来探测机器人操作策略的鲁棒性。GRT能够自动生成CrashShapes，即在结构上有效且满足用户约束的网格变形，这些变形会触发预训练操作策略中的灾难性失败。该方法结合了基于雅可比场的变形模型和无梯度、模拟器在环的优化策略。在插入、铰接和抓取任务中，GRT始终如一地发现能够导致策略性能崩溃的变形，揭示了静态基准测试遗漏的脆弱失败模式。通过结合任务级策略rollout和约束感知的形状探索，旨在构建一个通用的框架，用于在机器人操作中进行结构化的、以物体为中心的鲁棒性评估。此外，文章还展示了在单个CrashShape上进行微调（称为蓝队）可以将这些形状上的任务成功率提高高达60个百分点，同时保持原始对象上的性能，证明了红队几何体在有针对性的策略改进中的效用。最后，通过真实的机器人手臂验证了红队和蓝队的结果，观察到模拟的CrashShape将任务成功率从90%降低到低至22.5%，而蓝队将相应真实世界几何体的性能恢复到高达90%，与模拟结果非常吻合。

## 🔬 方法详解

**问题定义**：现有机器人操作策略的评估方法通常使用预定义的、分布内的数据集，这无法充分评估策略在面对真实世界中可能出现的各种几何变化时的鲁棒性。策略在这些精心设计的测试集上表现良好，但可能在稍微不同的几何形状下就会失效，而这些失效模式往往难以通过传统方法发现。因此，需要一种能够自动发现策略脆弱性的方法，以便更好地评估和改进机器人操作策略的鲁棒性。

**核心思路**：本文的核心思路是通过对物体几何形状进行有针对性的扰动，生成能够导致机器人操作策略失败的“CrashShapes”。通过优化这些扰动，可以系统地探索策略的弱点，并揭示其对几何变化的敏感性。这种方法模拟了“红队”攻击，旨在发现系统的潜在漏洞。

**技术框架**：GRT框架包含以下主要模块：1) 基于雅可比场的变形模型，用于生成结构上有效的几何扰动；2) 无梯度优化策略，用于在模拟环境中搜索能够导致策略失败的CrashShapes；3) 任务级策略rollout，用于评估策略在变形后的物体上的性能；4) 约束感知模块，用于确保生成的变形满足用户定义的约束条件。整个流程通过模拟器在环的方式进行，不断迭代优化几何形状，直到找到能够显著降低策略性能的CrashShape。

**关键创新**：GRT的关键创新在于其自动化的红队测试方法，能够系统地探索物体几何形状空间，发现导致机器人操作策略失败的特定几何变形。与传统的静态基准测试相比，GRT能够更全面地评估策略的鲁棒性，并揭示其潜在的脆弱性。此外，GRT还提供了一种蓝队策略，即通过在CrashShapes上进行微调，可以显著提高策略在这些特定形状上的性能，同时保持在原始形状上的性能。

**关键设计**：雅可比场变形模型用于生成平滑且结构有效的网格变形。无梯度优化算法（如CMA-ES）用于在模拟环境中搜索CrashShapes，目标是最小化策略在变形物体上的成功率。损失函数的设计需要平衡策略性能的降低和变形的幅度，以避免生成过于极端的、不真实的变形。约束条件可以包括变形的最大幅度、物体的体积变化等，以确保生成的变形在物理上是可行的。

## 📊 实验亮点

实验结果表明，GRT能够有效地发现导致机器人操作策略失败的几何变形。在真实机器人手臂上的实验验证表明，模拟的CrashShapes可以将任务成功率从90%降低到低至22.5%，而通过在CrashShapes上进行微调（蓝队），可以将相应真实世界几何体的性能恢复到高达90%，与模拟结果非常吻合。这证明了GRT框架在真实世界中的有效性和实用性。

## 🎯 应用场景

该研究成果可应用于机器人操作策略的鲁棒性评估与提升，例如在工业自动化、医疗机器人、家庭服务机器人等领域。通过GRT框架，可以发现并修复策略在面对未知环境和物体时的潜在缺陷，提高机器人的可靠性和安全性。此外，该方法还可以用于生成对抗性样本，用于训练更鲁棒的机器人操作策略。

## 📄 摘要（原文）

> Standard evaluation protocols in robotic manipulation typically assess policy performance over curated, in-distribution test sets, offering limited insight into how systems fail under plausible variation. We introduce Geometric Red-Teaming (GRT), a red-teaming framework that probes robustness through object-centric geometric perturbations, automatically generating CrashShapes -- structurally valid, user-constrained mesh deformations that trigger catastrophic failures in pre-trained manipulation policies. The method integrates a Jacobian field-based deformation model with a gradient-free, simulator-in-the-loop optimization strategy. Across insertion, articulation, and grasping tasks, GRT consistently discovers deformations that collapse policy performance, revealing brittle failure modes missed by static benchmarks. By combining task-level policy rollouts with constraint-aware shape exploration, we aim to build a general purpose framework for structured, object-centric robustness evaluation in robotic manipulation. We additionally show that fine-tuning on individual CrashShapes, a process we refer to as blue-teaming, improves task success by up to 60 percentage points on those shapes, while preserving performance on the original object, demonstrating the utility of red-teamed geometries for targeted policy refinement. Finally, we validate both red-teaming and blue-teaming results with a real robotic arm, observing that simulated CrashShapes reduce task success from 90% to as low as 22.5%, and that blue-teaming recovers performance to up to 90% on the corresponding real-world geometry -- closely matching simulation outcomes. Videos and code can be found on our project website: https://georedteam.github.io/ .

