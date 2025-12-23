---
layout: default
title: Do Vision-Language Models Have Internal World Models? Towards an Atomic Evaluation
---

# Do Vision-Language Models Have Internal World Models? Towards an Atomic Evaluation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.21876" class="toolbar-btn" target="_blank">📄 arXiv: 2506.21876v1</a>
  <a href="https://arxiv.org/pdf/2506.21876.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.21876v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.21876v1', 'Do Vision-Language Models Have Internal World Models? Towards an Atomic Evaluation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Qiyue Gao, Xinyu Pi, Kevin Liu, Junrong Chen, Ruolan Yang, Xinqi Huang, Xinyu Fang, Lu Sun, Gautham Kishore, Bo Ai, Stone Tao, Mengyang Liu, Jiaxi Yang, Chao-Jung Lai, Chuanyang Jin, Jiannan Xiang, Benhao Huang, Zeming Chen, David Danks, Hao Su, Tianmin Shu, Ziqiao Ma, Lianhui Qin, Zhiting Hu

**分类**: cs.CL, cs.AI, cs.CV

**发布日期**: 2025-06-27

**备注**: ACL 2025 (Findings)

---

## 💡 一句话要点

**提出两阶段框架评估视觉语言模型的内部世界模型能力**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `视觉语言模型` `内部世界模型` `评估框架` `感知能力` `预测能力` `WM-ABench` `多模态学习`

## 📋 核心要点

1. 现有的视觉语言模型在基本世界建模能力上存在显著不足，缺乏系统的评估方法。
2. 论文提出了一个两阶段的评估框架，分别针对感知和预测能力进行评估，填补了现有研究的空白。
3. 通过660次实验，发现当前模型在基本能力上表现不佳，尤其是在运动轨迹区分和解耦理解方面。

## 📝 摘要（中文）

内部世界模型（WMs）使代理能够理解世界状态并预测转变，是高级推理的基础。尽管最新的大型视觉语言模型（VLMs）如OpenAI o3、GPT-4o和Gemini展现出作为通用WMs的潜力，但对其基本WM能力的系统评估仍然缺失。本文提出一个两阶段框架，评估感知（视觉、空间、时间、数量和运动）和预测（机械模拟、传递推理、组合推理），并引入WM-ABench基准，涵盖23个细分评估维度和6个多样化的模拟环境。通过660次实验，我们发现这些模型在基本世界建模能力上存在显著局限性，几乎所有模型在区分运动轨迹时表现接近随机准确率，且缺乏解耦理解。

## 🔬 方法详解

**问题定义**：本文旨在解决当前视觉语言模型在内部世界模型能力评估上的不足，现有方法未能系统性地评估其基本能力，导致对模型性能的理解不够全面。

**核心思路**：提出一个基于比较心理学和认知科学的两阶段框架，分别评估模型的感知和预测能力，以提供更细致的评估标准。

**技术框架**：框架分为两个主要阶段：第一阶段评估感知能力，包括视觉、空间、时间、数量和运动；第二阶段评估预测能力，包括机械模拟、传递推理和组合推理。

**关键创新**：引入WM-ABench基准，涵盖23个细分评估维度，提供了一个系统化的评估工具，与现有方法相比，能够更全面地评估模型的世界建模能力。

**关键设计**：在实验中使用了660次实验，涵盖15个最新的商业和开源VLMs，设计了控制反事实模拟的多样化环境，以确保评估的严谨性和有效性。

## 📊 实验亮点

实验结果显示，几乎所有模型在区分运动轨迹时的准确率接近随机水平，且在解耦理解方面存在显著缺陷。这些发现揭示了当前视觉语言模型在基本世界建模能力上的重大不足，为未来的研究指明了方向。

## 🎯 应用场景

该研究的潜在应用领域包括智能代理、自动驾驶、机器人导航等，能够帮助提升模型在复杂环境中的决策能力和推理能力。未来，随着评估方法的完善，可能推动更智能的多模态系统的发展。

## 📄 摘要（原文）

> Internal world models (WMs) enable agents to understand the world's state and predict transitions, serving as the basis for advanced deliberative reasoning. Recent large Vision-Language Models (VLMs), such as OpenAI o3, GPT-4o and Gemini, exhibit potential as general-purpose WMs. While the latest studies have evaluated and shown limitations in specific capabilities such as visual understanding, a systematic evaluation of VLMs' fundamental WM abilities remains absent. Drawing on comparative psychology and cognitive science, we propose a two-stage framework that assesses Perception (visual, spatial, temporal, quantitative, and motion) and Prediction (mechanistic simulation, transitive inference, compositional inference) to provide an atomic evaluation of VLMs as WMs. Guided by this framework, we introduce WM-ABench, a large-scale benchmark comprising 23 fine-grained evaluation dimensions across 6 diverse simulated environments with controlled counterfactual simulations. Through 660 experiments on 15 latest commercial and open-source VLMs, we find that these models exhibit striking limitations in basic world modeling abilities. For instance, almost all models perform at near-random accuracy when distinguishing motion trajectories. Additionally, they lack disentangled understanding -- e.g., some models tend to believe blue objects move faster than green ones. More rich results and analyses reveal significant gaps between VLMs and human-level world modeling.

