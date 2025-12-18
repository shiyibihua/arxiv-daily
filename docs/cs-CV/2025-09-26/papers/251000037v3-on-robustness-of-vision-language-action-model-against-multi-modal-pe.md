---
layout: default
title: On Robustness of Vision-Language-Action Model against Multi-Modal Perturbations
---

# On Robustness of Vision-Language-Action Model against Multi-Modal Perturbations

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.00037" class="toolbar-btn" target="_blank">📄 arXiv: 2510.00037v3</a>
  <a href="https://arxiv.org/pdf/2510.00037.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.00037v3" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2510.00037v3', 'On Robustness of Vision-Language-Action Model against Multi-Modal Perturbations')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jianing Guo, Zhenhong Wu, Chang Tu, Yiyao Ma, Xiangqi Kong, Zhiqian Liu, Jiaming Ji, Shuning Zhang, Yuanpei Chen, Kai Chen, Qi Dou, Yaodong Yang, Xianglong Liu, Huijie Zhao, Weifeng Lv, Simin Li

**分类**: cs.CV, cs.AI, cs.RO

**发布日期**: 2025-09-26 (更新: 2025-10-28)

---

## 💡 一句话要点

**提出RobustVLA，增强视觉-语言-动作模型在多模态扰动下的鲁棒性**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `视觉-语言-动作模型` `多模态鲁棒性` `对抗训练` `多臂老虎机` `机器人学习`

## 📋 核心要点

1. 现有VLA模型在真实场景中面临多模态扰动挑战，例如动作、指令和环境变化，而现有方法主要关注视觉扰动。
2. RobustVLA通过离线鲁棒优化增强输出动作的鲁棒性，并强制输入动作一致性，同时利用多臂老虎机算法识别最有害的噪声。
3. 实验表明，RobustVLA在LIBERO和真实机器人FR5上，相比现有方法，在多模态扰动下显著提升了性能和鲁棒性。

## 📝 摘要（中文）

在视觉-语言-动作（VLA）模型中，对真实世界扰动的鲁棒性对于部署至关重要。现有方法主要关注简单的视觉干扰，忽略了动作、指令、环境和观察中出现的更广泛的多模态扰动。本文首先评估了主流VLA在四种模态的17种扰动下的鲁棒性。研究发现：（1）动作是最脆弱的模态；（2）现有的视觉鲁棒VLA在其他模态中没有获得鲁棒性；（3）pi0通过基于扩散的动作头表现出卓越的鲁棒性。为了构建多模态鲁棒的VLA，本文提出了RobustVLA，以应对VLA输入和输出中的扰动。对于输出鲁棒性，我们执行离线鲁棒优化，以对抗最坏情况下的动作噪声，从而最大化流匹配目标中的不匹配。这可以看作是对抗训练、标签平滑和异常值惩罚。对于输入鲁棒性，我们强制执行跨输入变化的动作一致性，以保留任务语义。为了解决多个扰动问题，我们将鲁棒性建模为一个多臂老虎机问题，并应用上限置信区间算法来自动识别最有害的噪声。在LIBERO上的实验表明，我们的RobustVLA在所有17种扰动下，在pi0骨干网络上实现了12.6%的绝对增益，在OpenVLA骨干网络上实现了10.4%的绝对增益，比现有的视觉鲁棒VLA实现了快50.6倍的推理速度，并在混合扰动下实现了10.4%的增益。我们的RobustVLA在真实世界的FR5机器人上尤其有效，在有限的演示下，在四种模态的扰动下实现了65.6%的绝对增益。

## 🔬 方法详解

**问题定义**：现有视觉-语言-动作（VLA）模型在真实世界部署时，容易受到多种模态的扰动影响，例如动作执行噪声、指令模糊、环境变化以及观测误差。现有方法主要关注视觉扰动，忽略了其他模态的脆弱性，导致模型在复杂场景下的泛化能力不足。

**核心思路**：RobustVLA的核心思路是同时增强VLA模型在输入和输出两个层面的鲁棒性。对于输出，通过对抗训练的方式，使模型对动作噪声具有抵抗力。对于输入，通过保持输入变化时动作的一致性，提高模型对输入扰动的鲁棒性。同时，采用多臂老虎机算法自动识别并应对最有害的噪声类型。

**技术框架**：RobustVLA包含两个主要模块：输出鲁棒性模块和输入鲁棒性模块。输出鲁棒性模块通过离线鲁棒优化，对抗最坏情况下的动作噪声，采用流匹配目标函数来衡量动作的匹配程度，并最大化不匹配程度。输入鲁棒性模块通过强制执行跨输入变化的动作一致性来保持任务语义。此外，使用多臂老虎机算法来自动识别最有害的噪声，并根据噪声的危害程度调整优化策略。

**关键创新**：RobustVLA的关键创新在于其多模态鲁棒性增强策略，它不仅考虑了视觉扰动，还同时关注动作、指令和环境等多种模态的扰动。此外，RobustVLA采用多臂老虎机算法自动识别最有害的噪声，并针对性地进行优化，从而提高了模型的鲁棒性和泛化能力。

**关键设计**：在输出鲁棒性模块中，采用了对抗训练的思想，通过最大化流匹配目标函数中的不匹配程度来模拟最坏情况下的动作噪声。在输入鲁棒性模块中，通过强制执行跨输入变化的动作一致性来保持任务语义。多臂老虎机算法采用上限置信区间（UCB）算法来平衡探索和利用，从而有效地识别最有害的噪声。具体的损失函数设计包括对抗损失、一致性损失等。

## 📊 实验亮点

RobustVLA在LIBERO数据集上，相比基线模型pi0和OpenVLA，在所有17种扰动下分别取得了12.6%和10.4%的绝对性能提升。在真实世界的FR5机器人实验中，RobustVLA在四种模态的扰动下实现了65.6%的绝对增益，验证了其在真实场景中的有效性。

## 🎯 应用场景

RobustVLA可应用于各种需要与环境交互的机器人任务，例如家庭服务机器人、工业自动化机器人和自动驾驶汽车。通过提高模型在复杂和不确定环境中的鲁棒性，可以显著提升机器人的可靠性和安全性，使其能够更好地适应真实世界的挑战。

## 📄 摘要（原文）

> In Vision-Language-Action (VLA) models, robustness to real-world perturbations is critical for deployment. Existing methods target simple visual disturbances, overlooking the broader multi-modal perturbations that arise in actions, instructions, environments, and observations. Here, we first evaluate the robustness of mainstream VLAs under 17 perturbations across four modalities. We find (1) actions as the most fragile modality, (2) Existing visual-robust VLA do not gain robustness in other modality, and (3) pi0 demonstrates superior robustness with a diffusion-based action head. To build multi-modal robust VLAs, we propose RobustVLA against perturbations in VLA inputs and outputs. For output robustness, we perform offline robust optimization against worst-case action noise that maximizes mismatch in flow matching objective. This can be seen as adversarial training, label smoothing, and outlier penalization. For input robustness, we enforce consistent actions across input variations that preserve task semantics. To account for multiple perturbations, we formulate robustness as a multi-armed bandit problem and apply an upper confidence bound algorithm to automatically identify the most harmful noise. Experiments on LIBERO demonstrate our RobustVLA delivers absolute gains over baselines of 12.6% on the pi0 backbone and 10.4% on the OpenVLA backbone across all 17 perturbations, achieving 50.6x faster inference than existing visual-robust VLAs, and a 10.4% gain under mixed perturbations. Our RobustVLA is particularly effective on real-world FR5 robot with limited demonstrations, showing absolute gains by 65.6% under perturbations of four modalities.

