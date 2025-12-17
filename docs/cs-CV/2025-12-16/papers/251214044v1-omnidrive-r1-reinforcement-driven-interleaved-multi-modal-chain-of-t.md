---
layout: default
title: OmniDrive-R1: Reinforcement-driven Interleaved Multi-modal Chain-of-Thought for Trustworthy Vision-Language Autonomous Driving
---

# OmniDrive-R1: Reinforcement-driven Interleaved Multi-modal Chain-of-Thought for Trustworthy Vision-Language Autonomous Driving

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.14044" class="toolbar-btn" target="_blank">📄 arXiv: 2512.14044v1</a>
  <a href="https://arxiv.org/pdf/2512.14044.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.14044v1" onclick="toggleFavorite(this, '2512.14044v1', 'OmniDrive-R1: Reinforcement-driven Interleaved Multi-modal Chain-of-Thought for Trustworthy Vision-Language Autonomous Driving')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zhenguo Zhang, Haohan Zhen, Yishen Wang, Le Xu, Tianchen Deng, Xuefeng Chen, Qu Chen, Bo Zhang, Wuxiong Huang

**分类**: cs.CV, cs.AI

**发布日期**: 2025-12-16

---

## 💡 一句话要点

**OmniDrive-R1：基于强化学习的多模态交错CoT，提升自动驾驶视觉语言模型的可靠性**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `自动驾驶` `视觉语言模型` `多模态学习` `思维链` `强化学习`

## 📋 核心要点

1. 现有VLM在自动驾驶中面临目标幻觉问题，源于对无根据文本CoT推理的依赖，且感知与推理解耦。
2. OmniDrive-R1通过交错多模态CoT统一感知与推理，利用强化学习驱动视觉grounding，聚焦关键区域。
3. 在DriveLMM-o1数据集上，OmniDrive-R1显著提升了推理得分和答案准确率，优于基线模型Qwen2.5VL-7B。

## 📝 摘要（中文）

视觉语言模型(VLM)在自动驾驶等安全关键领域的部署受到可靠性问题的严重阻碍，尤其是目标幻觉。这种失败源于它们对无根据的、基于文本的思维链(CoT)推理的依赖。现有的多模态CoT方法试图缓解这个问题，但存在两个根本缺陷：(1)解耦的感知和推理阶段，阻碍了端到端联合优化；(2)依赖于昂贵的、密集的定位标签。因此，我们引入了OmniDrive-R1，一个为自动驾驶设计的端到端VLM框架，它通过交错的多模态思维链(iMCoT)机制统一了感知和推理。我们的核心创新是强化学习驱动的视觉 grounding 能力，使模型能够自主地将其注意力引导并“放大”到关键区域进行细粒度分析。这种能力由我们纯粹的两阶段强化学习训练流程和Clip-GRPO算法实现。至关重要的是，Clip-GRPO引入了一种无标注的、基于过程的 grounding 奖励。这种奖励不仅消除了对密集标签的需求，还通过强制视觉焦点和文本推理之间的实时跨模态一致性，规避了外部工具调用的不稳定性。在DriveLMM-o1上的大量实验证明了我们模型的显著改进。与基线Qwen2.5VL-7B相比，OmniDrive-R1将整体推理得分从51.77%提高到80.35%，最终答案准确率从37.81%提高到73.62%。

## 🔬 方法详解

**问题定义**：现有视觉语言模型在自动驾驶场景中存在目标幻觉问题，即模型会生成与实际图像内容不符的描述或推理。这主要是因为现有的方法依赖于纯文本的思维链推理，缺乏对视觉信息的有效利用和 grounding。此外，感知和推理阶段的解耦也阻碍了模型的端到端优化，限制了其性能的提升。同时，对密集标注的依赖也增加了训练成本。

**核心思路**：OmniDrive-R1的核心思路是通过交错的多模态思维链（iMCoT）机制，将感知和推理过程紧密结合。模型不再是先进行感知，然后进行推理，而是交替地进行视觉关注和文本推理，从而实现更准确和可靠的决策。此外，利用强化学习来驱动视觉 grounding，使模型能够自主地学习如何关注图像中的关键区域，从而减少对人工标注的依赖。

**技术框架**：OmniDrive-R1的整体框架是一个端到端的视觉语言模型，包含以下主要模块：(1) 视觉编码器：用于提取图像的视觉特征。(2) 语言模型：用于进行文本推理和生成。(3) 交错的多模态思维链（iMCoT）模块：将视觉特征和文本信息进行融合，并交替地进行视觉关注和文本推理。(4) 强化学习模块：用于训练视觉 grounding 能力，使模型能够自主地学习如何关注图像中的关键区域。训练过程分为两个阶段，首先进行预训练，然后使用强化学习进行微调。

**关键创新**：OmniDrive-R1的关键创新在于以下几点：(1) 提出了交错的多模态思维链（iMCoT）机制，实现了感知和推理的紧密结合。(2) 引入了强化学习来驱动视觉 grounding，使模型能够自主地学习如何关注图像中的关键区域，减少了对人工标注的依赖。(3) 提出了Clip-GRPO算法，使用基于过程的 grounding 奖励，避免了对密集标签的需求，并规避了外部工具调用的不稳定性。

**关键设计**：Clip-GRPO算法是关键设计之一，它使用了一种无标注的、基于过程的 grounding 奖励。该奖励基于视觉焦点和文本推理之间的实时跨模态一致性。具体来说，模型会根据当前的文本推理结果，预测应该关注的图像区域，然后计算预测区域和实际区域之间的相似度。相似度越高，奖励越高。这种设计鼓励模型学习如何关注图像中的关键区域，从而提高推理的准确性。此外，模型使用了Qwen2.5VL-7B作为基础模型，并对其进行了微调。

## 📊 实验亮点

OmniDrive-R1在DriveLMM-o1数据集上取得了显著的性能提升。与基线模型Qwen2.5VL-7B相比，OmniDrive-R1将整体推理得分从51.77%提高到80.35%，提升了28.58个百分点；最终答案准确率从37.81%提高到73.62%，提升了35.81个百分点。这些结果表明，OmniDrive-R1能够有效地解决目标幻觉问题，提高自动驾驶视觉语言模型的可靠性。

## 🎯 应用场景

OmniDrive-R1具有广泛的应用前景，可用于提升自动驾驶系统的安全性与可靠性，减少事故发生率。此外，该技术还可应用于智能监控、机器人导航、图像检索等领域，提高视觉语言模型的理解能力和决策水平，具有重要的实际应用价值和未来发展潜力。

## 📄 摘要（原文）

> The deployment of Vision-Language Models (VLMs) in safety-critical domains like autonomous driving (AD) is critically hindered by reliability failures, most notably object hallucination. This failure stems from their reliance on ungrounded, text-based Chain-of-Thought (CoT) reasoning.While existing multi-modal CoT approaches attempt mitigation, they suffer from two fundamental flaws: (1) decoupled perception and reasoning stages that prevent end-to-end joint optimization, and (2) reliance on expensive, dense localization labels.Thus we introduce OmniDrive-R1, an end-to-end VLM framework designed for autonomous driving, which unifies perception and reasoning through an interleaved Multi-modal Chain-of-Thought (iMCoT) mechanism. Our core innovation is an Reinforcement-driven visual grounding capability, enabling the model to autonomously direct its attention and "zoom in" on critical regions for fine-grained analysis. This capability is enabled by our pure two-stage reinforcement learning training pipeline and Clip-GRPO algorithm. Crucially, Clip-GRPO introduces an annotation-free, process-based grounding reward. This reward not only eliminates the need for dense labels but also circumvents the instability of external tool calls by enforcing real-time cross-modal consistency between the visual focus and the textual reasoning. Extensive experiments on DriveLMM-o1 demonstrate our model's significant improvements. Compared to the baseline Qwen2.5VL-7B, OmniDrive-R1 improves the overall reasoning score from 51.77% to 80.35%, and the final answer accuracy from 37.81% to 73.62%.

