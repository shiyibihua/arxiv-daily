---
layout: default
title: An Inference-Based Architecture for Intent and Affordance Saturation in Decision-Making
---

# An Inference-Based Architecture for Intent and Affordance Saturation in Decision-Making

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.23144" class="toolbar-btn" target="_blank">📄 arXiv: 2512.23144v1</a>
  <a href="https://arxiv.org/pdf/2512.23144.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.23144v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.23144v1', 'An Inference-Based Architecture for Intent and Affordance Saturation in Decision-Making')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Wendyam Eric Lionel Ilboudo, Saori C Tanaka

**分类**: q-bio.NC, cs.AI, cs.LG

**发布日期**: 2025-12-29

**备注**: 32 pages, 12 figures

---

## 💡 一句话要点

**提出基于推理的架构，解决决策中意图和可供性饱和导致的决策瘫痪问题**

🎯 **匹配领域**: **支柱三：空间感知与语义 (Perception & Semantics)**

**关键词**: `决策瘫痪` `意图选择` `可供性选择` `KL散度` `推理模型` `自闭症` `漂移扩散模型`

## 📋 核心要点

1. 现有选择模型难以解释决策瘫痪现象，即充分了解情况却无法行动，因为它们假设选项已明确且易于比较。
2. 该论文提出一种基于推理的计算模型，将意图选择和可供性选择分离，并使用混合KL散度目标来模拟决策过程。
3. 通过静态和动态模型仿真，验证了该模型能够重现决策惯性和关闭等现象，并将自闭症视为决策连续体的一个极端。

## 📝 摘要（中文）

决策瘫痪，即在充分了解情况和具备足够动机的情况下，仍然犹豫不决、停滞不前或无法行动，对假设选项已明确且易于比较的选择模型提出了挑战。借鉴自闭症研究中尤其显著的定性报告，我们提出了一种计算模型，其中瘫痪源于分层决策过程中的收敛失败。我们将意图选择（追求什么）与可供性选择（如何实现目标）分离，并将承诺形式化为在反向和前向Kullback-Leibler (KL)目标混合下的推理。反向KL是模式寻求的，促进快速承诺，而前向KL是模式覆盖的，保留多个合理的目标或行动。在静态和动态（漂移扩散）模型中，当前向KL偏差的推理产生缓慢、重尾的响应时间以及两种不同的失败模式：意图饱和和可供性饱和，尤其是在价值相似时。在多选项任务中的模拟重现了决策惯性和关闭的关键特征，并将自闭症视为基于推理的通用决策连续体的极端状态。

## 🔬 方法详解

**问题定义**：论文旨在解决决策瘫痪问题，即个体在拥有充分信息和动机的情况下，仍然难以做出决策。现有选择模型通常假设选项是明确且易于比较的，无法解释犹豫不决、停滞不前等现象，尤其是在选项价值相似时。这些模型忽略了意图选择（what to pursue）和可供性选择（how to pursue the goal）之间的差异，以及决策过程中的不确定性。

**核心思路**：论文的核心思路是将决策过程建模为一种基于推理的过程，该过程涉及意图选择和可供性选择两个阶段。通过引入反向和前向KL散度的混合目标，模型能够平衡快速承诺（反向KL）和保留多种可能性（前向KL）的需求。这种设计允许模型在选项价值相似时，表现出犹豫不决和决策瘫痪的现象。

**技术框架**：该论文构建了一个分层决策模型，包含意图选择和可供性选择两个模块。模型使用混合KL散度作为推理目标，其中反向KL促进快速决策，前向KL保留多种可能性。该模型在静态和动态（漂移扩散）环境中进行了仿真，以验证其行为。

**关键创新**：该论文的关键创新在于将决策过程形式化为一种基于推理的过程，并引入了混合KL散度目标。这种方法能够更好地模拟人类决策中的不确定性和犹豫不决现象，并解释了决策瘫痪的产生机制。与传统选择模型相比，该模型更加灵活和具有解释性。

**关键设计**：模型使用反向KL和前向KL的加权和作为损失函数，权重参数控制了模型对快速承诺和保留多种可能性的偏好。在漂移扩散模型中，漂移率由意图和可供性的价值差异决定。模型的参数设置允许其模拟不同的决策风格，包括快速决策和犹豫不决。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.23144v1/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.23144v1/x2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.23144v1/x3.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

该论文通过仿真实验验证了模型的有效性。结果表明，当前向KL偏差较大时，模型会表现出缓慢、重尾的响应时间，以及意图饱和和可供性饱和两种失败模式。此外，该模型还能够重现决策惯性和关闭等现象，并将自闭症视为决策连续体的一个极端。这些结果表明，该模型能够捕捉人类决策中的关键特征。

## 🎯 应用场景

该研究成果可应用于开发更智能的决策支持系统，帮助用户在复杂和不确定的环境中做出更好的决策。此外，该模型还可以用于理解和治疗自闭症等认知障碍，为个性化干预提供理论基础。该研究对于理解人类决策过程具有重要意义，并可能影响人工智能和认知科学领域。

## 📄 摘要（原文）

> Decision paralysis, i.e. hesitation, freezing, or failure to act despite full knowledge and motivation, poses a challenge for choice models that assume options are already specified and readily comparable. Drawing on qualitative reports in autism research that are especially salient, we propose a computational account in which paralysis arises from convergence failure in a hierarchical decision process. We separate intent selection (what to pursue) from affordance selection (how to pursue the goal) and formalize commitment as inference under a mixture of reverse- and forward-Kullback-Leibler (KL) objectives. Reverse KL is mode-seeking and promotes rapid commitment, whereas forward KL is mode-covering and preserves multiple plausible goals or actions. In static and dynamic (drift-diffusion) models, forward-KL-biased inference yields slow, heavy-tailed response times and two distinct failure modes, intent saturation and affordance saturation, when values are similar. Simulations in multi-option tasks reproduce key features of decision inertia and shutdown, treating autism as an extreme regime of a general, inference-based, decision-making continuum.

