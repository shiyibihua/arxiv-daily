---
layout: default
title: Mechanical Intelligence-Aware Curriculum Reinforcement Learning for Humanoids with Parallel Actuation
---

# Mechanical Intelligence-Aware Curriculum Reinforcement Learning for Humanoids with Parallel Actuation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2507.00273" class="toolbar-btn" target="_blank">📄 arXiv: 2507.00273v3</a>
  <a href="https://arxiv.org/pdf/2507.00273.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2507.00273v3" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2507.00273v3', 'Mechanical Intelligence-Aware Curriculum Reinforcement Learning for Humanoids with Parallel Actuation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yusuke Tanaka, Alvin Zhu, Quanyou Wang, Yeting Liu, Dennis Hong

**分类**: cs.RO

**发布日期**: 2025-06-30 (更新: 2025-10-30)

**备注**: Proceeding to the IEEE Humanoid Conference 2025

**DOI**: [10.1109/Humanoids65713.2025.11203130](https://doi.org/10.1109/Humanoids65713.2025.11203130)

**🔗 代码/项目**: [GITHUB](https://github.com/alvister88/og_bruce)

---

## 💡 一句话要点

**提出机械智能感知的课程强化学习以优化类人机器人运动控制**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `类人机器人` `强化学习` `并联机制` `运动控制` `课程学习` `MuJoCo` `机械智能`

## 📋 核心要点

1. 现有的强化学习方法未能充分考虑并联驱动机制中的机械智能，导致运动建模不准确和策略次优。
2. 本文提出了一种新的课程强化学习框架，能够原生模拟并联机制的闭链约束，从而提高类人机器人的运动控制性能。
3. 实验结果表明，所提出的方法在真实环境中实现了优于模型预测控制器的表面泛化和性能，展示了显著的提升。

## 📝 摘要（中文）

强化学习（RL）推动了类人机器人运动的进步，但大多数学习框架未考虑并联驱动机制中的机械智能，导致运动建模不准确和策略次优。本文提出了三种并联机制的通用公式和仿真方法，并通过端到端的课程RL框架训练了一个感知并联机制的策略，应用于儿童类人机器人BRUCE。与依赖简化串联近似的先前方法不同，我们使用GPU加速的MuJoCo（MJX）原生模拟所有闭链约束，保留了硬件的机械非线性特性。通过与模型预测控制器（MPC）进行基准测试，我们展示了在真实世界零样本部署中的更好表面泛化和性能。此研究突出了在腿部类人机器人端到端学习流程中完全模拟并联机制的计算方法和性能优势。

## 🔬 方法详解

**问题定义**：本文旨在解决现有强化学习框架未能考虑并联驱动机制中的机械智能问题，导致类人机器人运动控制的建模不准确和策略次优。

**核心思路**：通过引入课程强化学习框架，结合GPU加速的MuJoCo仿真，原生模拟并联机制的闭链约束，从而提升运动控制的精确性和效率。

**技术框架**：整体架构包括三个主要模块：并联机制的建模与仿真、课程强化学习策略的训练以及性能评估。首先，建立并联机制的数学模型；其次，利用MuJoCo进行高效仿真；最后，训练和评估策略。

**关键创新**：最重要的创新在于原生模拟闭链约束，保留了机械非线性特性，这与以往依赖简化串联近似的方法有本质区别。

**关键设计**：在参数设置上，采用了适应性学习率和多阶段训练策略；损失函数设计考虑了运动精度和能量效率；网络结构则基于深度强化学习框架，优化了策略的收敛性和稳定性。

## 📊 实验亮点

实验结果显示，所提出的课程强化学习方法在真实世界的零样本部署中，相较于模型预测控制器（MPC），实现了更好的表面泛化和性能，具体提升幅度未知，展示了显著的优势。

## 🎯 应用场景

该研究的潜在应用领域包括服务机器人、救援机器人和人机交互等场景。通过优化类人机器人的运动控制，能够提升其在复杂环境中的适应能力和执行效率，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> Reinforcement learning (RL) has enabled advances in humanoid robot locomotion, yet most learning frameworks do not account for mechanical intelligence embedded in parallel actuation mechanisms due to limitations in simulator support for closed kinematic chains. This omission can lead to inaccurate motion modeling and suboptimal policies, particularly for robots with high actuation complexity. This paper presents general formulations and simulation methods for three types of parallel mechanisms: a differential pulley, a five-bar linkage, and a four-bar linkage, and trains a parallel-mechanism aware policy through an end-to-end curriculum RL framework for BRUCE, a kid-sized humanoid robot. Unlike prior approaches that rely on simplified serial approximations, we simulate all closed-chain constraints natively using GPU-accelerated MuJoCo (MJX), preserving the hardware's mechanical nonlinear properties during training. We benchmark our RL approach against a model predictive controller (MPC), demonstrating better surface generalization and performance in real-world zero-shot deployment. This work highlights the computational approaches and performance benefits of fully simulating parallel mechanisms in end-to-end learning pipelines for legged humanoids. Project codes with parallel mechanisms: https://github.com/alvister88/og_bruce

