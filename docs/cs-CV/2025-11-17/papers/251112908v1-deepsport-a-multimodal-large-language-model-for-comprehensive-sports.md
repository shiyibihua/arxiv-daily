---
layout: default
title: DeepSport: A Multimodal Large Language Model for Comprehensive Sports Video Reasoning via Agentic Reinforcement Learning
---

# DeepSport: A Multimodal Large Language Model for Comprehensive Sports Video Reasoning via Agentic Reinforcement Learning

<div class="paper-toolbar">
  <div class="toolbar-left">
    <a href="https://arxiv.org/abs/2511.12908" target="_blank" class="toolbar-btn">arXiv: 2511.12908v1</a>
    <a href="https://arxiv.org/pdf/2511.12908.pdf" target="_blank" class="toolbar-btn">PDF</a>
  </div>
  <div class="toolbar-right">
    <button class="toolbar-btn favorite-btn" data-arxiv-id="2511.12908v1" 
            onclick="toggleFavorite(this, '2511.12908v1', 'DeepSport: A Multimodal Large Language Model for Comprehensive Sports Video Reasoning via Agentic Reinforcement Learning')" title="收藏">
      ☆ 收藏
    </button>
    <button class="toolbar-btn share-btn" onclick="copyLink()" title="复制链接">
      🔗 分享
    </button>
  </div>
</div>


**作者**: Junbo Zou, Haotian Xia, Zhen Ye, Shengjie Zhang, Christopher Lai, Vicente Ordonez, Weining Shen, Hanjie Chen

**分类**: cs.CV, cs.AI

**发布日期**: 2025-11-17

---

## 💡 一句话要点

**DeepSport：基于Agent强化学习的多模态大语言模型，用于全面的体育视频推理**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `体育视频理解` `多模态大语言模型` `强化学习` `主动推理` `数据蒸馏` `思维链` `视频问答`

## 📋 核心要点

1. 现有体育视频理解方法局限于单一运动或特定任务，缺乏通用的、可学习的推理能力。
2. DeepSport通过主动迭代推理，利用帧提取工具动态查询视频内容，实现“用视频思考”。
3. DeepSport在多任务、多运动视频理解上取得了显著的性能提升，超越了现有专有和开源模型。

## 📝 摘要（中文）

体育视频理解面临独特的挑战，需要模型感知高速动态、理解复杂规则并推理长期时序上下文。虽然多模态大语言模型(MLLM)在通用领域展现出潜力，但当前体育领域的研究仍然狭隘：现有方法要么以单一运动为中心，要么局限于特定任务，要么依赖于缺乏鲁棒学习推理过程的免训练范式。为了解决这一差距，我们引入DeepSport，这是第一个为多任务、多运动视频理解设计的端到端训练的MLLM框架。DeepSport将范式从被动帧处理转变为主动迭代推理，通过专门的帧提取工具动态地查询内容，从而使模型能够“用视频思考”。为此，我们提出了一个数据蒸馏管道，从10个不同的数据源合成高质量的思维链(CoT)轨迹，创建一个包含78k训练数据的统一资源。然后，我们采用两阶段训练策略，即监督微调(SFT)和强化学习(RL)，并使用一种新颖的门控工具使用奖励来优化模型的推理过程。在6.7k个问题的测试基准上进行的大量实验表明，DeepSport实现了最先进的性能，显著优于专有模型和开源模型的基线。我们的工作为特定领域的视频推理建立了一个新的基础，以解决各种运动的复杂性。

## 🔬 方法详解

**问题定义**：现有体育视频理解方法存在局限性，主要体现在三个方面：一是专注于单一运动项目，缺乏通用性；二是仅限于特定任务，例如动作识别，无法进行更深层次的推理；三是依赖于免训练范式，缺乏鲁棒的学习推理过程。这些问题导致模型难以应对复杂多变的体育视频场景，无法进行全面的理解和推理。

**核心思路**：DeepSport的核心思路是将传统的被动帧处理方式转变为主动迭代推理。模型不再是被动地接收和处理每一帧图像，而是通过一个专门的帧提取工具，根据当前推理的需求，动态地选择和查询视频内容。这种主动查询的方式使得模型能够更加高效地利用视频信息，从而更好地理解和推理体育视频。

**技术框架**：DeepSport的整体框架包括三个主要部分：数据蒸馏管道、两阶段训练策略和多模态大语言模型。数据蒸馏管道负责从多个数据源合成高质量的思维链(CoT)轨迹，构建训练数据集。两阶段训练策略包括监督微调(SFT)和强化学习(RL)，用于优化模型的推理过程。多模态大语言模型是DeepSport的核心，负责接收视频信息和文本信息，并进行推理和生成答案。

**关键创新**：DeepSport的关键创新在于其主动迭代推理机制和门控工具使用奖励。主动迭代推理机制使得模型能够动态地选择和查询视频内容，从而更加高效地利用视频信息。门控工具使用奖励用于鼓励模型合理地使用帧提取工具，避免过度或不必要的使用。

**关键设计**：DeepSport的关键设计包括数据蒸馏管道的细节、两阶段训练策略的具体实现以及多模态大语言模型的结构。数据蒸馏管道采用了多种技术来保证生成CoT轨迹的质量，例如数据增强和噪声过滤。两阶段训练策略中，SFT用于初始化模型的参数，RL用于优化模型的推理过程。多模态大语言模型采用了Transformer架构，并引入了视觉编码器来处理视频信息。

## 📊 实验亮点

DeepSport在测试基准上取得了显著的性能提升，超越了现有专有模型和开源模型。具体而言，DeepSport在多个体育视频理解任务上实现了最先进的性能，证明了其主动迭代推理机制和门控工具使用奖励的有效性。实验结果表明，DeepSport能够更好地理解和推理复杂的体育视频场景。

## 🎯 应用场景

DeepSport在体育视频分析领域具有广泛的应用前景，例如：智能赛事解说、运动员技术分析、体育视频内容检索等。该研究的实际价值在于提升体育视频理解的准确性和效率，为体育产业的智能化发展提供技术支持。未来，DeepSport可以扩展到其他视频理解领域，例如：自动驾驶、安防监控等。

## 📄 摘要（原文）

> Sports video understanding presents unique challenges, requiring models to perceive high-speed dynamics, comprehend complex rules, and reason over long temporal contexts. While Multimodal Large Language Models (MLLMs) have shown promise in genral domains, the current state of research in sports remains narrowly focused: existing approaches are either single-sport centric, limited to specific tasks, or rely on training-free paradigms that lack robust, learned reasoning process. To address this gap, we introduce DeepSport, the first end-to-end trained MLLM framework designed for multi-task, multi-sport video understanding. DeepSport shifts the paradigm from passive frame processing to active, iterative reasoning, empowering the model to ``think with videos'' by dynamically interrogating content via a specialized frame-extraction tool. To enable this, we propose a data distillation pipeline that synthesizes high-quality Chain-of-Thought (CoT) trajectories from 10 diverse data source, creating a unified resource of 78k training data. We then employ a two-stage training strategy, Supervised Fine-Tuning (SFT) followed by Reinforcement Learning (RL) with a novel gated tool-use reward, to optimize the model's reasoning process. Extensive experiments on the testing benchmark of 6.7k questions demonstrate that DeepSport achieves state-of-the-art performance, significantly outperforming baselines of both proprietary model and open-source models. Our work establishes a new foundation for domain-specific video reasoning to address the complexities of diverse sports.

