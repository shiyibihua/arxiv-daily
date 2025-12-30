---
layout: default
title: "Act2Goal: From World Model To General Goal-conditioned Policy"
---

# Act2Goal: From World Model To General Goal-conditioned Policy

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.23541" class="toolbar-btn" target="_blank">📄 arXiv: 2512.23541v1</a>
  <a href="https://arxiv.org/pdf/2512.23541.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.23541v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.23541v1', 'Act2Goal: From World Model To General Goal-conditioned Policy')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Pengfei Zhou, Liliang Chen, Shengcong Chen, Di Chen, Wenzhi Zhao, Rongjun Jin, Guanghui Ren, Jianlan Luo

**分类**: cs.RO, cs.AI

**发布日期**: 2025-12-29

---

## 💡 一句话要点

**Act2Goal：融合世界模型与多尺度时序控制的通用目标条件策略**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `机器人操作` `目标条件策略` `世界模型` `多尺度时序控制` `长时程规划` `零样本泛化` `在线自适应`

## 📋 核心要点

1. 现有目标条件策略难以处理长时程操作，主要因为它们依赖单步动作预测，缺乏对任务进度的显式建模。
2. Act2Goal通过结合目标条件视觉世界模型和多尺度时序控制，生成中间视觉状态序列，实现长时程任务规划。
3. 实验表明，Act2Goal在零样本泛化和在线自适应方面表现出色，真实机器人实验成功率从30%提升到90%。

## 📝 摘要（中文）

本文提出Act2Goal，一种通用的目标条件操作策略，它将目标条件视觉世界模型与多尺度时序控制相结合。针对现有方法在长时程操作中依赖单步动作预测且缺乏显式任务进度建模的问题，Act2Goal利用世界模型生成中间视觉状态序列，捕捉长时程结构。引入多尺度时序哈希(MSTH)将轨迹分解为密集的近端帧和稀疏的远端帧，分别用于细粒度闭环控制和全局任务一致性。该策略通过端到端交叉注意力将这些表示与电机控制耦合，实现连贯的长时程行为并对局部扰动做出反应。Act2Goal在新的物体、空间布局和环境中实现了强大的零样本泛化。通过基于LoRA的后见目标重标记在线自适应，无需外部监督即可快速自主改进。真实机器人实验表明，Act2Goal在具有挑战性的分布外任务中，通过几分钟的自主交互，成功率从30%提高到90%，验证了具有多尺度时序控制的目标条件世界模型为鲁棒的长时程操作提供了必要的结构化指导。

## 🔬 方法详解

**问题定义**：现有的机器人操作任务指定方法难以兼顾表达性和精确性。视觉目标虽然提供了紧凑且明确的任务规范，但现有的目标条件策略在长时程操作中表现不佳，主要原因是它们依赖于单步动作预测，缺乏对任务进度的显式建模，难以应对长期规划中的不确定性。

**核心思路**：Act2Goal的核心思路是将目标条件视觉世界模型与多尺度时序控制相结合。世界模型负责生成从当前状态到目标状态的合理中间视觉状态序列，从而捕捉长时程任务的结构信息。多尺度时序控制则将该视觉计划转化为鲁棒的执行策略，兼顾局部控制的精确性和全局任务的一致性。

**技术框架**：Act2Goal的整体框架包含以下几个主要模块：1) **目标条件视觉世界模型**：根据当前观测和目标视觉状态，预测一系列中间视觉状态。2) **多尺度时序哈希(MSTH)**：将预测的视觉轨迹分解为密集的近端帧和稀疏的远端帧。近端帧用于细粒度的闭环控制，远端帧用于保持全局任务的一致性。3) **策略网络**：通过端到端交叉注意力机制，将MSTH输出的视觉信息与电机控制指令进行融合，生成最终的动作。

**关键创新**：Act2Goal的关键创新在于将世界模型生成的长时程视觉规划与多尺度时序控制相结合。与传统的单步预测方法不同，Act2Goal能够显式地建模任务进度，并利用多尺度信息来平衡局部控制和全局规划。此外，通过引入基于LoRA的后见目标重标记在线自适应方法，实现了无需外部监督的快速自主改进。

**关键设计**：MSTH的关键设计在于如何选择近端帧和远端帧。论文采用了一种基于哈希的方法来选择关键帧，保证了帧的选择具有代表性，同时降低了计算复杂度。策略网络采用交叉注意力机制，将视觉信息和电机控制指令进行融合，实现了端到端的学习。损失函数包括重构损失和动作预测损失，用于训练世界模型和策略网络。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.23541v1/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.23541v1/x2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.23541v1/x3.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

Act2Goal在真实机器人实验中表现出色，在具有挑战性的分布外任务中，通过几分钟的自主交互，成功率从30%提高到90%。该方法在零样本泛化方面也表现出强大的能力，能够直接应用于新的物体、空间布局和环境，无需额外的训练。

## 🎯 应用场景

Act2Goal具有广泛的应用前景，可应用于各种机器人操作任务，例如装配、抓取、放置等。该方法尤其适用于复杂、长时程的操作任务，例如家庭服务机器人、工业自动化等领域。通过在线自适应，Act2Goal能够快速适应新的环境和任务，降低了机器人部署和维护的成本，加速了机器人技术的普及。

## 📄 摘要（原文）

> Specifying robotic manipulation tasks in a manner that is both expressive and precise remains a central challenge. While visual goals provide a compact and unambiguous task specification, existing goal-conditioned policies often struggle with long-horizon manipulation due to their reliance on single-step action prediction without explicit modeling of task progress. We propose Act2Goal, a general goal-conditioned manipulation policy that integrates a goal-conditioned visual world model with multi-scale temporal control. Given a current observation and a target visual goal, the world model generates a plausible sequence of intermediate visual states that captures long-horizon structure. To translate this visual plan into robust execution, we introduce Multi-Scale Temporal Hashing (MSTH), which decomposes the imagined trajectory into dense proximal frames for fine-grained closed-loop control and sparse distal frames that anchor global task consistency. The policy couples these representations with motor control through end-to-end cross-attention, enabling coherent long-horizon behavior while remaining reactive to local disturbances. Act2Goal achieves strong zero-shot generalization to novel objects, spatial layouts, and environments. We further enable reward-free online adaptation through hindsight goal relabeling with LoRA-based finetuning, allowing rapid autonomous improvement without external supervision. Real-robot experiments demonstrate that Act2Goal improves success rates from 30% to 90% on challenging out-of-distribution tasks within minutes of autonomous interaction, validating that goal-conditioned world models with multi-scale temporal control provide structured guidance necessary for robust long-horizon manipulation. Project page: https://act2goal.github.io/

