---
layout: default
title: PolaRiS: Scalable Real-to-Sim Evaluations for Generalist Robot Policies
---

# PolaRiS: Scalable Real-to-Sim Evaluations for Generalist Robot Policies

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.16881" class="toolbar-btn" target="_blank">📄 arXiv: 2512.16881v1</a>
  <a href="https://arxiv.org/pdf/2512.16881.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.16881v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.16881v1', 'PolaRiS: Scalable Real-to-Sim Evaluations for Generalist Robot Policies')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Arhan Jain, Mingtong Zhang, Kanav Arora, William Chen, Marcel Torne, Muhammad Zubair Irshad, Sergey Zakharov, Yue Wang, Sergey Levine, Chelsea Finn, Wei-Chiu Ma, Dhruv Shah, Abhishek Gupta, Karl Pertsch

**分类**: cs.RO, cs.LG

**发布日期**: 2025-12-18

**备注**: Website: https://polaris-evals.github.io/

---

## 💡 一句话要点

**PolaRiS：一种可扩展的真实到模拟的通用机器人策略评估框架**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `机器人学习` `策略评估` `真实到模拟` `神经重建` `仿真环境`

## 📋 核心要点

1. 机器人策略评估面临真实环境rollout成本高、难以复现等问题，通用策略的评估更具挑战。
2. PolaRiS利用神经重建技术将真实场景视频转化为交互式仿真环境，实现高效的策略评估。
3. 通过仿真数据协同训练，PolaRiS显著提升了仿真环境与真实环境的相关性，实现零样本评估。

## 📝 摘要（中文）

机器人学习研究面临的一个重要挑战是准确测量和比较机器人策略的性能。由于真实世界rollout的随机性、可重复性和耗时性，机器人技术的基准测试历来具有挑战性。对于最近的通用策略，需要在各种场景和任务中进行评估，这使得挑战更加严峻。仿真环境中的评估为真实世界评估提供了一种可扩展的补充，但现有仿真基准与真实世界之间的视觉和物理领域差距使其成为不可靠的策略改进信号。此外，构建逼真且多样化的仿真环境传统上需要大量的人工和专业知识。为了弥合差距，我们引入了仿真环境中的策略评估和环境重建（PolaRiS），这是一个可扩展的真实到模拟的框架，用于高保真仿真机器人评估。PolaRiS利用神经重建方法将真实世界场景的短视频扫描转换为交互式仿真环境。此外，我们开发了一种简单的仿真数据协同训练方法，弥合了剩余的真实到模拟的差距，并实现了在未见过的仿真环境中的零样本评估。通过仿真和真实世界之间的广泛配对评估，我们证明PolaRiS评估比现有的仿真基准更能提供与真实世界通用策略性能的更强相关性。它的简单性也使得能够快速创建多样化的仿真环境。因此，这项工作朝着为下一代机器人基础模型进行分布式和民主化的评估迈出了一步。

## 🔬 方法详解

**问题定义**：现有机器人策略评估方法，尤其是在通用机器人策略的评估上，面临着真实环境评估成本高昂、难以复现，以及现有仿真环境与真实环境存在较大差距的问题。这导致在仿真环境中评估的策略，在真实环境中表现不佳，阻碍了机器人学习的进展。现有方法难以快速构建逼真且多样化的仿真环境，需要大量人工干预和专业知识。

**核心思路**：PolaRiS的核心思路是利用神经重建技术，将真实世界的场景快速转化为高保真度的仿真环境。通过这种方式，可以低成本地创建大量多样化的仿真环境，用于机器人策略的评估和训练。此外，通过仿真数据协同训练，进一步缩小仿真环境与真实环境之间的差距，提高仿真评估的可靠性。

**技术框架**：PolaRiS框架主要包含两个阶段：环境重建和策略评估。首先，利用神经重建方法，将真实场景的短视频扫描转化为交互式仿真环境。然后，在这些仿真环境中对机器人策略进行评估。为了进一步提高仿真环境的真实性，采用仿真数据协同训练的方法，利用真实数据和仿真数据共同训练策略，从而缩小领域差距。

**关键创新**：PolaRiS的关键创新在于其可扩展的真实到模拟的框架，能够快速、低成本地创建高保真度的仿真环境。与传统方法相比，PolaRiS无需大量人工干预，即可构建多样化的仿真环境。此外，仿真数据协同训练方法能够有效缩小仿真环境与真实环境之间的差距，提高仿真评估的可靠性。

**关键设计**：PolaRiS使用神经辐射场（NeRF）或类似技术进行环境重建，将真实场景的视频转化为三维模型。在仿真数据协同训练中，可以使用对抗训练或领域自适应等技术，最小化真实数据和仿真数据之间的分布差异。具体的损失函数和网络结构选择取决于具体的任务和数据集。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16881v1/figures/Teaser_Karl_version.jpg" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16881v1/figures/polaris_pipeline.jpg" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16881v1/figures/scene_comp_gui.jpg" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

PolaRiS在仿真环境中评估的策略与真实世界中的性能表现出更强的相关性，优于现有的仿真基准。通过实验证明，PolaRiS能够快速创建多样化的仿真环境，并实现零样本评估，显著提升了机器人策略评估的效率和可靠性。

## 🎯 应用场景

PolaRiS可应用于机器人策略的开发、测试和验证，尤其适用于通用机器人策略的评估。该框架能够加速机器人学习的研究进程，降低机器人开发的成本。此外，PolaRiS还可用于创建虚拟现实环境，进行远程操作和训练等应用。

## 📄 摘要（原文）

> A significant challenge for robot learning research is our ability to accurately measure and compare the performance of robot policies. Benchmarking in robotics is historically challenging due to the stochasticity, reproducibility, and time-consuming nature of real-world rollouts. This challenge is exacerbated for recent generalist policies, which has to be evaluated across a wide variety of scenes and tasks. Evaluation in simulation offers a scalable complement to real world evaluations, but the visual and physical domain gap between existing simulation benchmarks and the real world has made them an unreliable signal for policy improvement. Furthermore, building realistic and diverse simulated environments has traditionally required significant human effort and expertise. To bridge the gap, we introduce Policy Evaluation and Environment Reconstruction in Simulation (PolaRiS), a scalable real-to-sim framework for high-fidelity simulated robot evaluation. PolaRiS utilizes neural reconstruction methods to turn short video scans of real-world scenes into interactive simulation environments. Additionally, we develop a simple simulation data co-training recipe that bridges remaining real-to-sim gaps and enables zero-shot evaluation in unseen simulation environments. Through extensive paired evaluations between simulation and the real world, we demonstrate that PolaRiS evaluations provide a much stronger correlation to real world generalist policy performance than existing simulated benchmarks. Its simplicity also enables rapid creation of diverse simulated environments. As such, this work takes a step towards distributed and democratized evaluation for the next generation of robotic foundation models.

