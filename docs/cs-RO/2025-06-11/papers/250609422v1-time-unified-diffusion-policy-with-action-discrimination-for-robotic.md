---
layout: default
title: Time-Unified Diffusion Policy with Action Discrimination for Robotic Manipulation
---

# Time-Unified Diffusion Policy with Action Discrimination for Robotic Manipulation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.09422" class="toolbar-btn" target="_blank">📄 arXiv: 2506.09422v1</a>
  <a href="https://arxiv.org/pdf/2506.09422.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.09422v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.09422v1', 'Time-Unified Diffusion Policy with Action Discrimination for Robotic Manipulation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Ye Niu, Sanping Zhou, Yizhe Li, Ye Den, Le Wang

**分类**: cs.RO, cs.LG

**发布日期**: 2025-06-11

---

## 💡 一句话要点

**提出时间统一扩散策略以解决机器人操作中的实时响应问题**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `扩散模型` `机器人操作` `动作辨别` `实时响应` `生成模型`

## 📋 核心要点

1. 现有扩散策略在机器人操作中需要大量时间进行动作去噪，影响实时性。
2. 本文提出时间统一扩散策略（TUDP），通过统一去噪过程和引入动作辨别信息来提高效率和准确性。
3. TUDP在RLBench上实现了82.6%的多视角成功率和83.8%的单视角成功率，表现优于现有方法。

## 📝 摘要（中文）

在复杂场景中，机器人操作依赖生成模型来估计多种成功动作的分布。尽管扩散模型在训练鲁棒性上优于其他生成模型，但其在机器人操作中的实时响应受到迭代去噪时间的限制。现有的扩散策略通常需要显著的时间来逐步去噪，且时间变化的去噪过程增加了模型训练的复杂性。为此，本文提出了时间统一扩散策略（TUDP），通过构建统一的去噪过程和引入动作辨别信息，显著提升了动作生成的效率和准确性。实验结果表明，TUDP在RLBench上达到了82.6%的多视角成功率和83.8%的单视角成功率，且在减少去噪迭代次数时成功率提升更为显著。

## 🔬 方法详解

**问题定义**：本文旨在解决现有扩散策略在机器人操作中实时响应不足的问题。现有方法在动作去噪过程中需要较长时间，且时间变化的去噪过程增加了模型训练的复杂性，导致动作准确性下降。

**核心思路**：提出时间统一扩散策略（TUDP），通过构建统一的速度场和引入动作辨别信息，简化去噪过程，从而提高动作生成的效率和准确性。

**技术框架**：TUDP的整体架构包括两个主要模块：时间统一速度场和动作辨别分支。前者通过统一所有时间步的去噪过程来加速学习，后者则提供额外的动作辨别信息以提高去噪准确性。

**关键创新**：TUDP的核心创新在于构建了时间统一的去噪过程，并引入了动作辨别分支。这一设计使得模型能够更好地识别成功动作，从而提升去噪效果，与现有方法相比具有显著优势。

**关键设计**：在模型设计中，采用了统一的速度场来简化动作去噪过程，并通过动作辨别分支来增强模型的辨别能力。损失函数设计上，结合了去噪损失和辨别损失，以确保模型在学习过程中兼顾效率和准确性。

## 📊 实验亮点

在RLBench实验中，TUDP在多视角设置下达到了82.6%的成功率，在单视角设置下达到了83.8%的成功率，均为当前最优表现。特别是在减少去噪迭代次数的情况下，TUDP的成功率提升更为显著，显示出其在实时应用中的潜力。

## 🎯 应用场景

该研究的潜在应用领域包括工业机器人、服务机器人以及自动化生产线等。通过提高机器人在复杂环境中的操作效率和准确性，TUDP能够显著提升机器人在实际任务中的表现，具有广泛的实际价值和未来影响。

## 📄 摘要（原文）

> In many complex scenarios, robotic manipulation relies on generative models to estimate the distribution of multiple successful actions. As the diffusion model has better training robustness than other generative models, it performs well in imitation learning through successful robot demonstrations. However, the diffusion-based policy methods typically require significant time to iteratively denoise robot actions, which hinders real-time responses in robotic manipulation. Moreover, existing diffusion policies model a time-varying action denoising process, whose temporal complexity increases the difficulty of model training and leads to suboptimal action accuracy. To generate robot actions efficiently and accurately, we present the Time-Unified Diffusion Policy (TUDP), which utilizes action recognition capabilities to build a time-unified denoising process. On the one hand, we build a time-unified velocity field in action space with additional action discrimination information. By unifying all timesteps of action denoising, our velocity field reduces the difficulty of policy learning and speeds up action generation. On the other hand, we propose an action-wise training method, which introduces an action discrimination branch to supply additional action discrimination information. Through action-wise training, the TUDP implicitly learns the ability to discern successful actions to better denoising accuracy. Our method achieves state-of-the-art performance on RLBench with the highest success rate of 82.6% on a multi-view setup and 83.8% on a single-view setup. In particular, when using fewer denoising iterations, TUDP achieves a more significant improvement in success rate. Additionally, TUDP can produce accurate actions for a wide range of real-world tasks.

