---
layout: default
title: Occupancy Learning with Spatiotemporal Memory
---

# Occupancy Learning with Spatiotemporal Memory

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.04705" class="toolbar-btn" target="_blank">📄 arXiv: 2508.04705v1</a>
  <a href="https://arxiv.org/pdf/2508.04705.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.04705v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.04705v1', 'Occupancy Learning with Spatiotemporal Memory')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Ziyang Leng, Jiawei Yang, Wenlong Yi, Bolei Zhou

**分类**: cs.CV

**发布日期**: 2025-08-06

**备注**: Accepted to ICCV2025. Project website: https://matthew-leng.github.io/stocc

---

## 💡 一句话要点

**提出ST-Occ以解决3D占用率学习中的时空一致性问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱八：物理动画 (Physics-based Animation)**

**关键词**: `3D占用率` `时空记忆` `自动驾驶` `环境感知` `动态体素` `深度学习` `时空一致性`

## 📋 核心要点

1. 现有方法在处理多帧输入时，难以高效聚合3D占用率，面临高处理成本和体素动态性带来的不确定性。
2. 本文提出ST-Occ框架，通过时空记忆捕捉历史信息，并利用记忆注意力机制增强当前占用率表示的时空一致性。
3. 实验结果显示，ST-Occ在3D占用率预测任务中相较于现有最先进方法提升了3 mIoU，并减少了29%的时间不一致性。

## 📝 摘要（中文）

3D占用率作为一种有前景的感知表示，能够细致地建模自动驾驶环境。然而，由于处理成本高以及体素的不确定性和动态性，如何有效地在多个输入帧中聚合3D占用率仍然具有挑战性。为此，本文提出了ST-Occ，一个场景级占用率表示学习框架，能够有效学习具有时间一致性的时空特征。ST-Occ包括两个核心设计：一个捕捉全面历史信息并通过场景级表示高效存储的时空记忆，以及一个基于时空记忆对当前占用率表示进行条件化的记忆注意力机制。实验结果表明，该方法在3D占用率预测任务中显著提升了时空表示的学习效果，mIoU提升了3，并减少了29%的时间不一致性。

## 🔬 方法详解

**问题定义**：本文旨在解决在多帧输入下高效聚合3D占用率的挑战，现有方法在处理动态体素时存在高处理成本和不一致性的问题。

**核心思路**：ST-Occ框架通过引入时空记忆和记忆注意力机制，旨在有效捕捉和利用历史信息，从而增强时空特征的学习和表示。

**技术框架**：ST-Occ由两个主要模块组成：时空记忆模块用于存储历史信息，记忆注意力模块则根据时空记忆对当前占用率表示进行条件化。

**关键创新**：该方法的创新在于引入了时空记忆和动态感知的记忆注意力机制，显著提高了时空表示的学习效果，与传统方法相比，能够更好地处理动态环境中的不确定性。

**关键设计**：在网络结构上，ST-Occ采用了特定的损失函数来优化时空一致性，并通过参数设置来平衡时空记忆的存储效率与信息捕捉能力。具体的网络架构和参数设置在实验中进行了详细验证。

## 📊 实验亮点

实验结果表明，ST-Occ在3D占用率预测任务中相较于最先进的方法提升了3 mIoU，并成功减少了29%的时间不一致性，显示出其在时空特征学习方面的显著优势。

## 🎯 应用场景

该研究的潜在应用领域包括自动驾驶、机器人导航和智能交通系统等。通过提高3D占用率的学习效果，ST-Occ能够为自动驾驶系统提供更准确的环境感知，进而提升安全性和效率。未来，该方法可能在复杂动态环境下的实时感知任务中发挥重要作用。

## 📄 摘要（原文）

> 3D occupancy becomes a promising perception representation for autonomous driving to model the surrounding environment at a fine-grained scale. However, it remains challenging to efficiently aggregate 3D occupancy over time across multiple input frames due to the high processing cost and the uncertainty and dynamics of voxels. To address this issue, we propose ST-Occ, a scene-level occupancy representation learning framework that effectively learns the spatiotemporal feature with temporal consistency. ST-Occ consists of two core designs: a spatiotemporal memory that captures comprehensive historical information and stores it efficiently through a scene-level representation and a memory attention that conditions the current occupancy representation on the spatiotemporal memory with a model of uncertainty and dynamic awareness. Our method significantly enhances the spatiotemporal representation learned for 3D occupancy prediction tasks by exploiting the temporal dependency between multi-frame inputs. Experiments show that our approach outperforms the state-of-the-art methods by a margin of 3 mIoU and reduces the temporal inconsistency by 29%.

