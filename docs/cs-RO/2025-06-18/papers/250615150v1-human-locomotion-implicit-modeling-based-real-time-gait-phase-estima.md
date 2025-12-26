---
layout: default
title: Human Locomotion Implicit Modeling Based Real-Time Gait Phase Estimation
---

# Human Locomotion Implicit Modeling Based Real-Time Gait Phase Estimation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.15150" class="toolbar-btn" target="_blank">📄 arXiv: 2506.15150v1</a>
  <a href="https://arxiv.org/pdf/2506.15150.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.15150v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.15150v1', 'Human Locomotion Implicit Modeling Based Real-Time Gait Phase Estimation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yuanlong Ji, Xingbang Yang, Ruoqi Zhao, Qihan Ye, Quan Zheng, Yubo Fan

**分类**: cs.RO, eess.SY

**发布日期**: 2025-06-18

---

## 💡 一句话要点

**提出基于隐式建模的实时步态相位估计方法以解决精确适应问题**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `步态相位估计` `隐式建模` `外骨骼` `时间卷积` `变换器` `IMU信号` `人机交互` `鲁棒性`

## 📋 核心要点

1. 现有步态相位估计方法在地形变化时准确性和鲁棒性不足，限制了外骨骼的适应能力。
2. 本文提出了一种结合时间卷积和变换器层的神经网络，通过隐式建模增强步态相位估计的准确性。
3. 实验结果显示，所提方法在稳定和变化地形下均显著优于现有基线，验证了其在实际应用中的有效性。

## 📝 摘要（中文）

基于惯性测量单元（IMU）信号的步态相位估计有助于外骨骼精确适应个体步态变化。然而，在地形变化期间，准确性和鲁棒性仍然面临挑战。为此，本文开发了一种基于隐式建模的人类运动步态相位估计神经网络，结合时间卷积进行特征提取，并利用变换器层进行多通道信息融合。提出的通道掩蔽重建预训练策略增强了模型的泛化能力。实验结果表明，该方法在稳定地形条件下的步态相位均方根误差（RMSE）为$2.729 	imes 1.071	ext{ % }$，在地形过渡下的RMSE为$3.215 	imes 1.303	ext{ % }$，验证了算法在各种连续运动场景中的可靠性。

## 🔬 方法详解

**问题定义**：本文旨在解决步态相位估计中的准确性和鲁棒性问题，尤其是在地形变化时现有方法的不足之处。

**核心思路**：通过隐式建模人类运动，结合时间卷积和变换器层，增强步态相位估计的特征提取和信息融合能力，从而提高模型的泛化性能。

**技术框架**：整体架构包括特征提取模块（时间卷积）、信息融合模块（变换器层）和通道掩蔽重建预训练策略，形成一个端到端的神经网络。

**关键创新**：提出的通道掩蔽重建预训练策略将步态相位状态向量与IMU信号视为人类运动的联合观测，显著提升了模型的泛化能力，与传统方法相比具有本质区别。

**关键设计**：在网络结构上，采用了多层时间卷积和变换器层，损失函数设计为结合步态相位和相位速率的综合损失，以优化模型性能。具体参数设置和训练细节在实验部分进行了详细描述。

## 📊 实验亮点

实验结果显示，所提方法在稳定地形条件下的步态相位均方根误差（RMSE）为$2.729 	imes 1.071	ext{ % }$，而在地形过渡下的RMSE为$3.215 	imes 1.303	ext{ % }$，相较于现有基线方法有显著提升，验证了算法的有效性和可靠性。

## 🎯 应用场景

该研究的潜在应用领域包括智能外骨骼系统、康复机器人和人机交互技术。通过提高步态相位估计的准确性和鲁棒性，能够实现更安全和高效的人机协作，推动智能机器人在复杂环境中的应用。

## 📄 摘要（原文）

> Gait phase estimation based on inertial measurement unit (IMU) signals facilitates precise adaptation of exoskeletons to individual gait variations. However, challenges remain in achieving high accuracy and robustness, particularly during periods of terrain changes. To address this, we develop a gait phase estimation neural network based on implicit modeling of human locomotion, which combines temporal convolution for feature extraction with transformer layers for multi-channel information fusion. A channel-wise masked reconstruction pre-training strategy is proposed, which first treats gait phase state vectors and IMU signals as joint observations of human locomotion, thus enhancing model generalization. Experimental results demonstrate that the proposed method outperforms existing baseline approaches, achieving a gait phase RMSE of $2.729 \pm 1.071%$ and phase rate MAE of $0.037 \pm 0.016%$ under stable terrain conditions with a look-back window of 2 seconds, and a phase RMSE of $3.215 \pm 1.303%$ and rate MAE of $0.050 \pm 0.023%$ under terrain transitions. Hardware validation on a hip exoskeleton further confirms that the algorithm can reliably identify gait cycles and key events, adapting to various continuous motion scenarios. This research paves the way for more intelligent and adaptive exoskeleton systems, enabling safer and more efficient human-robot interaction across diverse real-world environments.

