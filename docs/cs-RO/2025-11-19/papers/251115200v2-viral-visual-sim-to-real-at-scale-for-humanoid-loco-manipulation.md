---
layout: default
title: VIRAL: Visual Sim-to-Real at Scale for Humanoid Loco-Manipulation
---

# VIRAL: Visual Sim-to-Real at Scale for Humanoid Loco-Manipulation

**arXiv**: [2511.15200v2](https://arxiv.org/abs/2511.15200) | [PDF](https://arxiv.org/pdf/2511.15200.pdf)

**作者**: Tairan He, Zi Wang, Haoru Xue, Qingwei Ben, Zhengyi Luo, Wenli Xiao, Ye Yuan, Xingye Da, Fernando Castañeda, Shankar Sastry, Changliu Liu, Guanya Shi, Linxi Fan, Yuke Zhu

**分类**: cs.RO

**发布日期**: 2025-11-19 (更新: 2025-11-27)

**备注**: Project website: https://viral-humanoid.github.io/

---

## 💡 一句话要点

**VIRAL：面向人形机器人loco-manipulation的大规模视觉Sim-to-Real框架**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `人形机器人` `loco-manipulation` `Sim-to-Real` `强化学习` `域随机化`

## 📋 核心要点

1. 人形机器人缺乏自主loco-manipulation技能，限制了其在现实世界的部署。
2. VIRAL框架通过teacher-student架构，在仿真环境中学习loco-manipulation技能，并零样本迁移到真实机器人。
3. 实验表明，该方法在Unitree G1机器人上实现了连续的loco-manipulation，性能接近专家级遥操作水平。

## 📝 摘要（中文）

本文提出VIRAL，一个视觉sim-to-real框架，完全在仿真中学习人形机器人的loco-manipulation技能，并零样本部署到真实硬件。VIRAL采用teacher-student设计：一个特权强化学习teacher，基于完整状态信息，学习使用delta动作空间和参考状态初始化进行长时程loco-manipulation。然后，通过大规模仿真（使用分块渲染）从teacher中蒸馏出一个基于视觉的student策略，并采用在线DAgger和行为克隆的混合方法进行训练。研究发现，计算规模至关重要：将仿真扩展到数十个GPU（最多64个）可以使teacher和student的训练都变得可靠，而低计算量往往会导致失败。为了弥合sim-to-real的差距，VIRAL结合了大规模的视觉域随机化（包括光照、材质、相机参数、图像质量和传感器延迟）以及灵巧手和相机的real-to-sim对齐。在Unitree G1人形机器人上部署后，基于RGB的策略可以执行多达54个周期的连续loco-manipulation，推广到各种空间和外观变化，无需任何真实世界的微调，并接近专家级遥操作性能。大量的消融实验剖析了在实践中实现基于RGB的人形机器人loco-manipulation所需的关键设计选择。

## 🔬 方法详解

**问题定义**：现有的人形机器人loco-manipulation方法难以在真实世界中部署，主要原因是缺乏足够的训练数据和难以克服的sim-to-real差距。现有方法通常需要大量的真实世界数据进行微调，或者在仿真环境中训练的策略难以泛化到真实环境。

**核心思路**：VIRAL的核心思路是通过大规模仿真和域随机化来弥合sim-to-real差距。通过teacher-student框架，首先训练一个在理想状态下运行的teacher策略，然后通过蒸馏的方式将知识迁移到基于视觉的student策略。大规模仿真和域随机化使得student策略能够适应真实世界的各种变化。

**技术框架**：VIRAL框架包含以下几个主要模块：1) 特权强化学习teacher：使用完整状态信息学习loco-manipulation策略。2) 基于视觉的student策略：通过蒸馏从teacher策略学习，并使用RGB图像作为输入。3) 大规模仿真环境：使用分块渲染技术加速仿真，并进行大规模的域随机化。4) Real-to-sim对齐：对灵巧手和相机进行real-to-sim对齐，以减少sim-to-real差距。

**关键创新**：VIRAL的关键创新在于其大规模的仿真和域随机化策略，以及teacher-student框架的应用。通过将仿真扩展到数十个GPU，可以训练出更鲁棒的策略。同时，通过对光照、材质、相机参数等进行随机化，可以使student策略更好地适应真实世界的变化。teacher-student框架使得可以将teacher策略的知识迁移到基于视觉的student策略，从而避免了直接训练基于视觉的策略的困难。

**关键设计**：VIRAL的关键设计包括：1) 使用delta动作空间和参考状态初始化来训练teacher策略。2) 使用在线DAgger和行为克隆的混合方法来训练student策略。3) 对光照、材质、相机参数、图像质量和传感器延迟进行大规模的视觉域随机化。4) 对灵巧手和相机进行real-to-sim对齐。

## 📊 实验亮点

VIRAL在Unitree G1人形机器人上进行了实验，结果表明，该方法可以实现多达54个周期的连续loco-manipulation，并且能够推广到各种空间和外观变化，无需任何真实世界的微调。该方法的性能接近专家级遥操作水平，表明其具有很强的实用价值。

## 🎯 应用场景

VIRAL框架具有广泛的应用前景，可以应用于人形机器人在各种复杂环境中的自主操作，例如家庭服务、工业自动化、搜索救援等。通过在仿真环境中进行训练，可以大大降低人形机器人的开发成本和风险，并加速其在现实世界中的部署。该研究为人形机器人的自主loco-manipulation提供了一种新的解决方案。

## 📄 摘要（原文）

> A key barrier to the real-world deployment of humanoid robots is the lack of autonomous loco-manipulation skills. We introduce VIRAL, a visual sim-to-real framework that learns humanoid loco-manipulation entirely in simulation and deploys it zero-shot to real hardware. VIRAL follows a teacher-student design: a privileged RL teacher, operating on full state, learns long-horizon loco-manipulation using a delta action space and reference state initialization. A vision-based student policy is then distilled from the teacher via large-scale simulation with tiled rendering, trained with a mixture of online DAgger and behavior cloning. We find that compute scale is critical: scaling simulation to tens of GPUs (up to 64) makes both teacher and student training reliable, while low-compute regimes often fail. To bridge the sim-to-real gap, VIRAL combines large-scale visual domain randomization over lighting, materials, camera parameters, image quality, and sensor delays--with real-to-sim alignment of the dexterous hands and cameras. Deployed on a Unitree G1 humanoid, the resulting RGB-based policy performs continuous loco-manipulation for up to 54 cycles, generalizing to diverse spatial and appearance variations without any real-world fine-tuning, and approaching expert-level teleoperation performance. Extensive ablations dissect the key design choices required to make RGB-based humanoid loco-manipulation work in practice.

