---
layout: default
title: Learning dissection trajectories from expert surgical videos via imitation learning with equivariant diffusion
---

# Learning dissection trajectories from expert surgical videos via imitation learning with equivariant diffusion

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.04716" class="toolbar-btn" target="_blank">📄 arXiv: 2506.04716v1</a>
  <a href="https://arxiv.org/pdf/2506.04716.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.04716v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.04716v1', 'Learning dissection trajectories from expert surgical videos via imitation learning with equivariant diffusion')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Hongyu Wang, Yonghao Long, Yueyao Chen, Hon-Chi Yip, Markus Scheppach, Philip Wai-Yan Chiu, Yeung Yam, Helen Mei-Ling Meng, Qi Dou

**分类**: cs.CV

**发布日期**: 2025-06-05

**DOI**: [10.1016/j.media.2025.103599](https://doi.org/10.1016/j.media.2025.103599)

---

## 💡 一句话要点

**提出iDPOE以解决内镜下粘膜剥离术轨迹预测问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `内镜手术` `模仿学习` `轨迹预测` `扩散模型` `几何对称性` `外科培训` `智能医疗`

## 📋 核心要点

1. 现有方法在处理内镜下粘膜剥离术（ESD）视频中的不确定运动和几何对称性时存在不足，导致轨迹预测的准确性和泛化能力不足。
2. 论文提出的iDPOE方法通过隐式扩散策略和等变表示，能够有效捕捉专家行为的随机性，并提升对不同内镜视图的视觉表示学习能力。
3. 实验结果显示，iDPOE在轨迹预测方面超越了现有的最先进方法，证明了其在外科技能培训中的实际应用潜力。

## 📝 摘要（中文）

内镜下粘膜剥离术（ESD）是一种成熟的去除上皮病变的技术。预测ESD视频中的剥离轨迹对提升外科技能培训和简化学习过程具有重要潜力，但这一领域仍然未被充分探索。尽管模仿学习在从专家演示中获取技能方面表现出色，但在处理未来运动的不确定性、学习几何对称性和在多样化外科场景中进行泛化时仍面临挑战。为此，我们提出了一种新方法：隐式扩散策略与等变表示的模仿学习（iDPOE）。该方法通过联合状态动作分布建模专家行为，捕捉剥离轨迹的随机特性，并在各种内镜视图中实现稳健的视觉表示学习。通过将扩散模型融入策略学习，iDPOE确保了高效的训练和采样，从而实现更准确的预测和更好的泛化。此外，我们通过将等变性嵌入学习过程，增强了模型对几何对称性的泛化能力。使用近2000个剪辑的ESD视频数据集，实验结果表明我们的方法在轨迹预测上超越了现有的显式和隐式方法。

## 🔬 方法详解

**问题定义**：本论文旨在解决内镜下粘膜剥离术（ESD）视频中剥离轨迹预测的挑战。现有方法在处理未来运动的不确定性、学习几何对称性及在多样化外科场景中泛化能力不足，限制了其实际应用。

**核心思路**：论文提出的iDPOE方法通过引入隐式扩散模型与等变表示，能够有效建模专家的行为，捕捉剥离轨迹的随机性，从而提升预测的准确性和泛化能力。

**技术框架**：iDPOE的整体架构包括数据预处理、专家行为建模、扩散模型训练和条件采样等主要模块。通过这些模块的协同工作，模型能够在不同的内镜视图中进行有效的学习和预测。

**关键创新**：iDPOE的核心创新在于将扩散模型与模仿学习相结合，并引入等变性以增强模型的几何泛化能力。这一设计使得模型能够更好地适应不同的外科场景，显著提升了轨迹预测的性能。

**关键设计**：在模型设计中，采用了联合状态动作分布来捕捉专家行为的随机性，并通过前向过程引导的动作推断策略来解决状态不匹配问题。此外，损失函数的设计也考虑了轨迹预测的准确性和泛化能力。

## 📊 实验亮点

实验结果表明，iDPOE在轨迹预测任务中超越了现有的最先进方法，具体表现为在近2000个ESD视频剪辑上，预测准确率显著提高，验证了其在外科技能培训中的有效性和实用性。

## 🎯 应用场景

该研究的潜在应用领域包括外科手术培训、智能手术辅助系统和自动化手术机器人等。通过提升对内镜下粘膜剥离术的轨迹预测能力，能够有效提高外科医生的技能培训效率，降低手术风险，推动智能医疗的发展。

## 📄 摘要（原文）

> Endoscopic Submucosal Dissection (ESD) is a well-established technique for removing epithelial lesions. Predicting dissection trajectories in ESD videos offers significant potential for enhancing surgical skill training and simplifying the learning process, yet this area remains underexplored. While imitation learning has shown promise in acquiring skills from expert demonstrations, challenges persist in handling uncertain future movements, learning geometric symmetries, and generalizing to diverse surgical scenarios. To address these, we introduce a novel approach: Implicit Diffusion Policy with Equivariant Representations for Imitation Learning (iDPOE). Our method models expert behavior through a joint state action distribution, capturing the stochastic nature of dissection trajectories and enabling robust visual representation learning across various endoscopic views. By incorporating a diffusion model into policy learning, iDPOE ensures efficient training and sampling, leading to more accurate predictions and better generalization. Additionally, we enhance the model's ability to generalize to geometric symmetries by embedding equivariance into the learning process. To address state mismatches, we develop a forward-process guided action inference strategy for conditional sampling. Using an ESD video dataset of nearly 2000 clips, experimental results show that our approach surpasses state-of-the-art methods, both explicit and implicit, in trajectory prediction. To the best of our knowledge, this is the first application of imitation learning to surgical skill development for dissection trajectory prediction.

