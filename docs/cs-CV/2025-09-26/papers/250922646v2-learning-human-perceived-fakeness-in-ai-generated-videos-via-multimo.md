---
layout: default
title: Learning Human-Perceived Fakeness in AI-Generated Videos via Multimodal LLMs
---

# Learning Human-Perceived Fakeness in AI-Generated Videos via Multimodal LLMs

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.22646" class="toolbar-btn" target="_blank">📄 arXiv: 2509.22646v2</a>
  <a href="https://arxiv.org/pdf/2509.22646.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.22646v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.22646v2', 'Learning Human-Perceived Fakeness in AI-Generated Videos via Multimodal LLMs')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Xingyu Fu, Siyi Liu, Yinuo Xu, Pan Lu, Guangqiuse Hu, Tianbo Yang, Taran Anantasagar, Christopher Shen, Yikai Mao, Yuanzhe Liu, Keyush Shah, Chung Un Lee, Yejin Choi, James Zou, Dan Roth, Chris Callison-Burch

**分类**: cs.CV, cs.AI, cs.CL

**发布日期**: 2025-09-26 (更新: 2025-10-01)

**备注**: Project Page: https://deeptracereward.github.io/

---

## 💡 一句话要点

**提出DeeptraceReward以解决AI生成视频的伪造检测问题**

🎯 **匹配领域**: **支柱八：物理动画 (Physics-based Animation)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `深度伪造检测` `多模态学习` `视频生成` `人类感知` `奖励模型` `数据集构建` `自然语言处理` `时空感知`

## 📋 核心要点

1. 现有视频生成模型在伪造检测方面存在不足，未能有效识别深度伪造痕迹。
2. 论文提出DeeptraceReward基准，通过细粒度注释帮助模型学习人类如何识别伪造视频。
3. 实验结果表明，所提7B奖励模型在伪造线索识别等任务上显著优于现有模型，提升幅度达到34.7%。

## 📝 摘要（中文）

人类能否识别AI生成（伪造）视频并提供合理解释？尽管视频生成模型快速发展，但人类能否检测生成视频中的深度伪造痕迹这一关键维度却被忽视。我们引入DeeptraceReward，这是首个细粒度、时空感知的基准，注释了人类感知的伪造痕迹以用于视频生成奖励。该数据集包含4300个详细注释，覆盖3300个高质量生成视频。每个注释提供自然语言解释，标记包含伪造痕迹的边界框区域，并精确标记起止时间。我们将这些注释整合为9个主要类别，训练多模态语言模型作为奖励模型，以模拟人类判断和定位。在DeeptraceReward上，我们的7B奖励模型在伪造线索识别、定位和解释方面平均超越GPT-5 34.7%。

## 🔬 方法详解

**问题定义**：本论文旨在解决人类如何识别AI生成视频中的伪造痕迹这一具体问题。现有方法未能充分考虑人类的感知能力，导致伪造检测效果不佳。

**核心思路**：论文的核心思路是引入DeeptraceReward基准，通过详细的注释和自然语言解释，帮助多模态语言模型学习人类的判断标准和定位能力。

**技术框架**：整体架构包括数据集构建、注释整合、模型训练和评估四个主要模块。数据集包含伪造痕迹的详细注释，模型则通过这些数据进行训练。

**关键创新**：最重要的技术创新在于DeeptraceReward基准的提出，它提供了时空感知的伪造痕迹注释，显著提升了模型的学习效果，与现有方法相比具有本质区别。

**关键设计**：在模型设计中，采用了7B参数的奖励模型，并使用了多模态融合的策略，结合自然语言处理和视觉信息，以提高伪造线索的识别能力。损失函数的设计也针对伪造痕迹的特征进行了优化。

## 📊 实验亮点

实验结果显示，所提7B奖励模型在伪造线索识别、定位和解释方面的平均性能超越GPT-5 34.7%。此外，研究发现伪造与真实视频的二分类任务相对简单，而细粒度的伪造痕迹检测则表现出明显的难度梯度，反映了模型在不同任务上的表现差异。

## 🎯 应用场景

该研究的潜在应用领域包括社交媒体内容审核、视频监控系统以及虚假信息检测等。通过提高AI生成视频的可信度和可解释性，能够有效减少虚假信息的传播，提升用户对视频内容的信任度。未来，该技术还可能扩展到其他多模态生成任务中，推动更广泛的应用。

## 📄 摘要（原文）

> Can humans identify AI-generated (fake) videos and provide grounded reasons? While video generation models have advanced rapidly, a critical dimension -- whether humans can detect deepfake traces within a generated video, i.e., spatiotemporal grounded visual artifacts that reveal a video as machine generated -- has been largely overlooked. We introduce DeeptraceReward, the first fine-grained, spatially- and temporally- aware benchmark that annotates human-perceived fake traces for video generation reward. The dataset comprises 4.3K detailed annotations across 3.3K high-quality generated videos. Each annotation provides a natural-language explanation, pinpoints a bounding-box region containing the perceived trace, and marks precise onset and offset timestamps. We consolidate these annotations into 9 major categories of deepfake traces that lead humans to identify a video as AI-generated, and train multimodal language models (LMs) as reward models to mimic human judgments and localizations. On DeeptraceReward, our 7B reward model outperforms GPT-5 by 34.7% on average across fake clue identification, grounding, and explanation. Interestingly, we observe a consistent difficulty gradient: binary fake v.s. real classification is substantially easier than fine-grained deepfake trace detection; within the latter, performance degrades from natural language explanations (easiest), to spatial grounding, to temporal labeling (hardest). By foregrounding human-perceived deepfake traces, DeeptraceReward provides a rigorous testbed and training signal for socially aware and trustworthy video generation.

