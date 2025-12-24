---
layout: default
title: Physical Autoregressive Model for Robotic Manipulation without Action Pretraining
---

# Physical Autoregressive Model for Robotic Manipulation without Action Pretraining

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.09822" class="toolbar-btn" target="_blank">📄 arXiv: 2508.09822v4</a>
  <a href="https://arxiv.org/pdf/2508.09822.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.09822v4" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.09822v4', 'Physical Autoregressive Model for Robotic Manipulation without Action Pretraining')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zijian Song, Sihan Qin, Tianshui Chen, Liang Lin, Guangrun Wang

**分类**: cs.CV

**发布日期**: 2025-08-13 (更新: 2025-09-08)

**备注**: 16 pages, 6 figures

**🔗 代码/项目**: [PROJECT_PAGE](https://hcplab-sysu.github.io/PhysicalAutoregressiveModel/)

---

## 💡 一句话要点

**提出物理自回归模型以解决机器人操作数据稀缺问题**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)**

**关键词**: `物理自回归模型` `机器人操作` `视频预测` `动作轨迹` `数据稀缺` `自回归生成` `世界知识`

## 📋 核心要点

1. 现有方法在机器人操作中面临数据稀缺的问题，尤其是在缺乏动作预训练的情况下。
2. 本文提出的物理自回归模型（PAR）通过结合帧和动作的物理标记，利用视频预训练的世界知识来理解物理动态。
3. 实验结果显示，PAR在PushCube任务上取得100%成功率，并在其他任务上与动作预训练基线相当，展示了其优越的预测能力。

## 📝 摘要（中文）

由于操作数据的稀缺，研究者们开始利用其他模态的预训练大模型来辅助机器人技术。本文基于自回归视频生成模型，提出了一种物理自回归模型（PAR），通过物理标记将帧和动作结合，表示机器人与环境的联合演变。PAR利用视频预训练中嵌入的世界知识来理解物理动态，无需动作预训练，从而实现准确的视频预测和一致的动作轨迹。此外，PAR采用基于DiT的去标记器，将帧和动作建模为连续标记，减轻量化误差并促进相互增强。实验结果表明，PAR在ManiSkill基准测试中，在PushCube任务上实现了100%的成功率，并在其他任务上与动作预训练基线的性能相匹配，准确预测未来视频并紧密对齐动作轨迹。这些发现为通过自回归视频预训练转移世界知识到机器人操作提供了有希望的方向。

## 🔬 方法详解

**问题定义**：本文旨在解决机器人操作中数据稀缺的问题，尤其是在缺乏动作预训练的情况下，现有方法难以准确预测物理动态和生成一致的动作轨迹。

**核心思路**：提出物理自回归模型（PAR），通过物理标记将帧和动作结合，利用视频预训练中嵌入的世界知识来理解物理动态，从而实现准确的视频预测和一致的动作轨迹。

**技术框架**：PAR的整体架构包括物理标记的生成、基于DiT的去标记器、因果掩码、逆向运动学和KV-cache机制等模块，形成一个高效的训练和预测流程。

**关键创新**：PAR的核心创新在于无需动作预训练即可理解物理动态，同时通过将帧和动作建模为连续标记，减轻了量化误差，提升了模型的预测能力。

**关键设计**：在设计中，PAR采用了因果掩码以确保时间序列的因果性，结合逆向运动学优化动作生成，并通过并行训练和KV-cache机制提升了性能和效率。

## 📊 实验亮点

PAR在ManiSkill基准测试中表现出色，在PushCube任务上实现了100%的成功率，并在其他任务中与动作预训练基线的性能相匹配，展示了其在视频预测和动作轨迹一致性方面的显著提升。

## 🎯 应用场景

该研究的潜在应用领域包括智能机器人、自动化生产线和人机交互等场景。通过有效地转移世界知识，PAR能够提升机器人在复杂环境中的操作能力，具有广泛的实际价值和未来影响。

## 📄 摘要（原文）

> The scarcity of manipulation data has motivated the use of pretrained large models from other modalities in robotics. In this work, we build upon autoregressive video generation models to propose a Physical Autoregressive Model (PAR), where physical tokens combine frames and actions to represent the joint evolution of the robot and its environment. PAR leverages the world knowledge embedded in video pretraining to understand physical dynamics without requiring action pretraining, enabling accurate video prediction and consistent action trajectories. It also adopts a DiT-based de-tokenizer to model frames and actions as continuous tokens, mitigating quantization errors and facilitating mutual enhancement. Furthermore, we incorporate a causal mask with inverse kinematics, parallel training, and the KV-cache mechanism to further improve performance and efficiency. Experiments on the ManiSkill benchmark show that PAR achieves a 100\% success rate on the PushCube task, matches the performance of action-pretrained baselines on other tasks, and accurately predicts future videos with tightly aligned action trajectories. These findings underscore a promising direction for robotic manipulation by transferring world knowledge from autoregressive video pretraining. The project page is here: https://hcplab-sysu.github.io/PhysicalAutoregressiveModel/

