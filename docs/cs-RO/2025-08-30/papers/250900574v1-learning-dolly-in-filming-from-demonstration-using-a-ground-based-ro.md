---
layout: default
title: Learning Dolly-In Filming From Demonstration Using a Ground-Based Robot
---

# Learning Dolly-In Filming From Demonstration Using a Ground-Based Robot

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.00574" class="toolbar-btn" target="_blank">📄 arXiv: 2509.00574v1</a>
  <a href="https://arxiv.org/pdf/2509.00574.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.00574v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.00574v1', 'Learning Dolly-In Filming From Demonstration Using a Ground-Based Robot')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Philip Lorimer, Alan Hunter, Wenbin Li

**分类**: cs.RO, cs.LG

**发布日期**: 2025-08-30

**备注**: Preprint; under double-anonymous review. 6 pages

---

## 💡 一句话要点

**提出基于示范学习的自动化拍摄方法以解决电影拍摄中的控制难题**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `示范学习` `生成对抗网络` `机器人电影制作` `自动化摄像` `强化学习`

## 📋 核心要点

1. 现有的机器人电影制作方法依赖于手工设计的奖励函数，难以实现艺术性与精确性的平衡。
2. 本文提出了一种基于示范学习的生成对抗模仿学习方法，旨在自动化地面拍摄机器人的推进镜头。
3. 实验结果表明，GAIL策略在模拟中优于PPO基线，且能够无缝转移到真实机器人上，提升了构图一致性。

## 📝 摘要（中文）

电影摄像控制需要精确与艺术性的平衡，这一特性难以通过手工设计的奖励函数来编码。尽管强化学习（RL）已被应用于机器人电影制作，但其对定制奖励和广泛调优的依赖限制了创造性使用。本文提出了一种基于示范学习（LfD）的方法，利用生成对抗模仿学习（GAIL）来自动化地面拍摄机器人的推进镜头。通过模拟中的操纵杆遥控收集专家轨迹，捕捉流畅且富有表现力的运动，而无需明确的目标设计。经过训练的GAIL策略在模拟中优于PPO基线，获得更高的奖励、更快的收敛速度和更低的方差。重要的是，该方法可以直接转移到真实机器人上，无需微调，且在构图和主体对齐方面表现出比之前基于TD3的方法更一致的效果。这些结果表明，LfD为电影领域提供了一种稳健的、无奖励的替代RL方法，使实时部署变得简单。我们的流程使直观且风格化的摄像控制更易于创意专业人士使用，弥合了艺术意图与机器人自主性之间的差距。

## 🔬 方法详解

**问题定义**：本文旨在解决机器人电影制作中对手工奖励函数的依赖，导致的艺术性与精确性难以平衡的问题。现有方法在创造性使用上存在局限性。

**核心思路**：通过示范学习的方法，利用生成对抗模仿学习（GAIL）来学习专家的拍摄轨迹，从而实现自动化的推进镜头控制，避免了复杂的奖励设计。

**技术框架**：整体流程包括专家轨迹的收集、GAIL模型的训练和在真实机器人上的应用。专家轨迹通过操纵杆遥控在模拟环境中获取，GAIL模型则在这些轨迹上进行训练。

**关键创新**：最重要的创新在于使用GAIL替代传统的强化学习方法，提供了一种无奖励的学习方式，能够直接应用于真实环境，提升了拍摄的稳定性和一致性。

**关键设计**：在模型训练中，采用了特定的损失函数来优化模仿学习过程，确保生成的轨迹与专家轨迹的相似性，同时设计了适合于实时控制的网络结构。具体的参数设置和网络架构细节在论文中进行了详细讨论。

## 📊 实验亮点

实验结果显示，GAIL策略在模拟环境中获得的奖励显著高于PPO基线，且收敛速度更快、方差更低。此外，该方法能够无缝转移到真实机器人上，构图和主体对齐的一致性明显优于之前的TD3方法。

## 🎯 应用场景

该研究的潜在应用领域包括电影制作、广告拍摄以及任何需要高质量摄像控制的场景。通过简化机器人控制过程，创意专业人士能够更专注于艺术创作，而非技术细节，未来可能推动更多自动化摄像技术的发展。

## 📄 摘要（原文）

> Cinematic camera control demands a balance of precision and artistry - qualities that are difficult to encode through handcrafted reward functions. While reinforcement learning (RL) has been applied to robotic filmmaking, its reliance on bespoke rewards and extensive tuning limits creative usability. We propose a Learning from Demonstration (LfD) approach using Generative Adversarial Imitation Learning (GAIL) to automate dolly-in shots with a free-roaming, ground-based filming robot. Expert trajectories are collected via joystick teleoperation in simulation, capturing smooth, expressive motion without explicit objective design.
>   Trained exclusively on these demonstrations, our GAIL policy outperforms a PPO baseline in simulation, achieving higher rewards, faster convergence, and lower variance. Crucially, it transfers directly to a real-world robot without fine-tuning, achieving more consistent framing and subject alignment than a prior TD3-based method. These results show that LfD offers a robust, reward-free alternative to RL in cinematic domains, enabling real-time deployment with minimal technical effort. Our pipeline brings intuitive, stylized camera control within reach of creative professionals, bridging the gap between artistic intent and robotic autonomy.

