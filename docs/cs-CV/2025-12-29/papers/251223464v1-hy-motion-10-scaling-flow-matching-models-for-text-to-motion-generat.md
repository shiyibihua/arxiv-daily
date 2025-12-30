---
layout: default
title: "HY-Motion 1.0: Scaling Flow Matching Models for Text-To-Motion Generation"
---

# HY-Motion 1.0: Scaling Flow Matching Models for Text-To-Motion Generation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.23464" class="toolbar-btn" target="_blank">📄 arXiv: 2512.23464v1</a>
  <a href="https://arxiv.org/pdf/2512.23464.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.23464v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.23464v1', 'HY-Motion 1.0: Scaling Flow Matching Models for Text-To-Motion Generation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yuxin Wen, Qing Shuai, Di Kang, Jing Li, Cheng Wen, Yue Qian, Ningxin Jiao, Changhai Chen, Weijie Chen, Yiran Wang, Jinkun Guo, Dongyue An, Han Liu, Yanyu Tong, Chao Zhang, Qing Guo, Juan Chen, Qiao Zhang, Youyi Zhang, Zihao Yao, Cheng Zhang, Hong Duan, Xiaoping Wu, Qi Chen, Fei Cheng, Liang Dong, Peng He, Hao Zhang, Jiaxin Lin, Chao Zhang, Zhongyi Fan, Yifan Li, Zhichao Hu, Yuhong Liu, Linus, Jie Jiang, Xiaolong Li, Linchao Bao

**分类**: cs.CV, cs.AI, cs.GR

**发布日期**: 2025-12-29

**备注**: Github: see https://github.com/Tencent-Hunyuan/HY-Motion-1.0

---

## 💡 一句话要点

**HY-Motion 1.0：扩展Flow Matching模型至十亿参数规模，实现文本驱动的3D人体动作生成。**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱四：生成式动作 (Generative Motion)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `文本到动作生成` `3D人体运动` `Diffusion Transformer` `Flow Matching` `大规模预训练` `强化学习` `运动捕捉` `动作生成`

## 📋 核心要点

1. 现有文本到动作生成模型在指令遵循和动作质量上存在不足，难以满足复杂场景需求。
2. HY-Motion 1.0 通过扩展 Diffusion Transformer (DiT) 架构，并结合大规模数据训练和强化学习，提升模型性能。
3. 该模型在超过200个运动类别上表现出色，显著超越现有开源基准，并已开源促进进一步研究。

## 📝 摘要（中文）

HY-Motion 1.0 是一系列先进的大规模运动生成模型，能够从文本描述生成 3D 人体运动。它是首次成功地将基于 Diffusion Transformer (DiT) 的 flow matching 模型扩展到运动生成领域中数十亿参数规模的尝试，提供了显著优于当前开源基准的指令遵循能力。该模型引入了一个全面的全阶段训练范式，包括超过 3,000 小时的运动数据的大规模预训练、400 小时精选数据上的高质量微调，以及来自人类反馈和奖励模型的强化学习，以确保与文本指令的精确对齐和高质量的运动。这一框架由我们细致的数据处理流程支持，该流程执行严格的运动清理和标注。因此，我们的模型实现了最广泛的覆盖，跨越 6 个主要类别中的 200 多个运动类别。我们将 HY-Motion 1.0 开源，以促进未来的研究并加速 3D 人体运动生成模型向商业成熟的过渡。

## 🔬 方法详解

**问题定义**：现有文本到动作生成模型难以生成高质量、符合文本描述的3D人体运动。痛点在于模型规模小，数据量不足，以及缺乏有效的训练策略来保证文本与动作的对齐。

**核心思路**：HY-Motion 1.0的核心思路是利用大规模数据和模型参数来提升模型的表达能力，并采用全阶段训练范式，包括预训练、微调和强化学习，以确保模型能够准确理解文本指令并生成高质量的动作。

**技术框架**：HY-Motion 1.0 采用基于 Diffusion Transformer (DiT) 的 flow matching 模型。整体流程包括：1) 大规模运动数据预训练；2) 高质量数据微调；3) 基于人类反馈和奖励模型的强化学习。数据处理流程包括运动清理和标注。

**关键创新**：最重要的创新点在于成功将 DiT-based flow matching 模型扩展到数十亿参数规模，并应用于运动生成领域。此外，全阶段训练范式，特别是结合人类反馈和奖励模型的强化学习，是提升模型性能的关键。

**关键设计**：具体的技术细节包括：大规模预训练数据集的构建，高质量微调数据集的筛选，以及强化学习中奖励函数的设计。模型参数规模达到数十亿级别，网络结构采用 Diffusion Transformer (DiT)。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.23464v1/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.23464v1/x2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.23464v1/x3.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

HY-Motion 1.0 在文本到动作生成任务上取得了显著的性能提升，超越了现有的开源基准。该模型能够生成覆盖超过200个运动类别的高质量3D人体运动。通过大规模预训练、高质量微调和强化学习，模型在指令遵循和动作质量上均有显著提升。

## 🎯 应用场景

HY-Motion 1.0 可广泛应用于虚拟现实、游戏开发、动画制作、机器人控制等领域。该模型能够根据文本描述生成逼真的人体运动，极大地降低了相关内容的制作成本，并为用户提供了更丰富的交互体验。未来，该技术有望应用于智能康复、运动训练等领域。

## 📄 摘要（原文）

> We present HY-Motion 1.0, a series of state-of-the-art, large-scale, motion generation models capable of generating 3D human motions from textual descriptions. HY-Motion 1.0 represents the first successful attempt to scale up Diffusion Transformer (DiT)-based flow matching models to the billion-parameter scale within the motion generation domain, delivering instruction-following capabilities that significantly outperform current open-source benchmarks. Uniquely, we introduce a comprehensive, full-stage training paradigm -- including large-scale pretraining on over 3,000 hours of motion data, high-quality fine-tuning on 400 hours of curated data, and reinforcement learning from both human feedback and reward models -- to ensure precise alignment with the text instruction and high motion quality. This framework is supported by our meticulous data processing pipeline, which performs rigorous motion cleaning and captioning. Consequently, our model achieves the most extensive coverage, spanning over 200 motion categories across 6 major classes. We release HY-Motion 1.0 to the open-source community to foster future research and accelerate the transition of 3D human motion generation models towards commercial maturity.

