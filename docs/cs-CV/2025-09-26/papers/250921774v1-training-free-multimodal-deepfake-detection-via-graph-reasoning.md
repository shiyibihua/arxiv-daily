---
layout: default
title: Training-Free Multimodal Deepfake Detection via Graph Reasoning
---

# Training-Free Multimodal Deepfake Detection via Graph Reasoning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.21774" class="toolbar-btn" target="_blank">📄 arXiv: 2509.21774v1</a>
  <a href="https://arxiv.org/pdf/2509.21774.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.21774v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.21774v1', 'Training-Free Multimodal Deepfake Detection via Graph Reasoning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yuxin Liu, Fei Wang, Kun Li, Yiqi Nie, Junjie Chen, Yanyan Wei, Zhangling Duan, Zhaohong Jia

**分类**: cs.CV, cs.CY

**发布日期**: 2025-09-26

---

## 💡 一句话要点

**提出GASP-ICL框架，无需训练即可实现多模态Deepfake检测。**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多模态Deepfake检测` `免训练学习` `图推理` `上下文学习` `视觉语言模型` `信息安全` `伪造检测`

## 📋 核心要点

1. 现有方法难以捕捉细微的伪造线索，无法有效解决跨模态不一致问题，且缺乏任务对齐的检索能力。
2. GASP-ICL框架通过引导式自适应评分器和传播上下文学习，将任务感知知识注入LVLMs，实现免训练的MDD。
3. 实验表明，GASP-ICL在四种伪造类型上超越了现有基线，无需对LVLM进行微调即可实现性能提升。

## 📝 摘要（中文）

多模态Deepfake检测(MDD)旨在揭示视觉、文本和听觉模态中的篡改，从而增强现代信息系统的可靠性。尽管大型视觉语言模型(LVLMs)表现出强大的多模态推理能力，但它们在MDD中的有效性受到捕捉细微伪造线索、解决跨模态不一致以及执行任务对齐检索等挑战的限制。为此，我们提出引导式自适应评分器和传播上下文学习(GASP-ICL)，这是一个用于MDD的免训练框架。GASP-ICL采用流水线来保持语义相关性，同时将任务感知知识注入LVLMs。我们利用MDD自适应特征提取器来检索对齐的图像-文本对并构建候选集。我们进一步设计了图结构泰勒自适应评分器(GSTAS)来捕获跨样本关系并传播查询对齐信号，从而产生区分性强的示例。这使得能够精确选择语义对齐的、任务相关的演示，从而增强LVLMs的鲁棒MDD能力。在四种伪造类型上的实验表明，GASP-ICL超越了强大的基线，在没有LVLM微调的情况下实现了性能提升。

## 🔬 方法详解

**问题定义**：论文旨在解决多模态Deepfake检测（MDD）问题，即检测在视觉、文本和听觉等多种模态上进行的篡改。现有方法，特别是基于大型视觉语言模型（LVLMs）的方法，在捕捉细微的伪造线索、解决跨模态不一致性以及执行任务对齐的检索方面存在不足，导致检测性能受限。

**核心思路**：论文的核心思路是设计一个免训练的框架，通过引导式自适应评分器和传播上下文学习（GASP-ICL），将任务相关的知识注入到LVLMs中，从而提高其在MDD任务中的性能。该方法旨在通过精确选择语义对齐且任务相关的示例，增强LVLMs的鲁棒性，而无需进行昂贵的微调。

**技术框架**：GASP-ICL框架包含以下主要模块：1) MDD自适应特征提取器，用于检索对齐的图像-文本对并构建候选集；2) 图结构泰勒自适应评分器（GSTAS），用于捕获跨样本关系并传播查询对齐信号，生成具有区分性的示例；3) 上下文学习模块，利用GSTAS选择的示例，增强LVLMs的MDD能力。整体流程是先提取特征，然后构建图并进行评分，最后利用评分结果进行上下文学习。

**关键创新**：该论文的关键创新在于提出了图结构泰勒自适应评分器（GSTAS），用于捕获跨样本关系并传播查询对齐信号。GSTAS能够更精确地选择与查询相关的示例，从而提高上下文学习的有效性。此外，该框架是免训练的，避免了对LVLMs进行微调的需要，降低了计算成本。

**关键设计**：MDD自适应特征提取器的具体实现细节未知，但其目标是提取适合MDD任务的特征。GSTAS的具体结构和参数设置未知，但其核心思想是利用图结构来建模样本之间的关系，并使用泰勒展开来近似评分函数。上下文学习模块的具体实现细节未知，但其目标是利用GSTAS选择的示例来指导LVLMs进行MDD。

## 📊 实验亮点

GASP-ICL框架在四种伪造类型上的实验中，超越了现有的强大基线方法，实现了性能提升，并且无需对大型视觉语言模型（LVLM）进行微调。具体的性能提升数据未知，但结果表明该框架在多模态Deepfake检测方面具有显著优势。

## 🎯 应用场景

该研究成果可应用于新闻媒体、社交平台等领域，用于检测和识别Deepfake内容，维护信息的真实性和可靠性，防止虚假信息传播，保障社会稳定。未来可扩展到更多模态的Deepfake检测，并与其他安全技术结合，构建更完善的网络安全体系。

## 📄 摘要（原文）

> Multimodal deepfake detection (MDD) aims to uncover manipulations across visual, textual, and auditory modalities, thereby reinforcing the reliability of modern information systems. Although large vision-language models (LVLMs) exhibit strong multimodal reasoning, their effectiveness in MDD is limited by challenges in capturing subtle forgery cues, resolving cross-modal inconsistencies, and performing task-aligned retrieval. To this end, we propose Guided Adaptive Scorer and Propagation In-Context Learning (GASP-ICL), a training-free framework for MDD. GASP-ICL employs a pipeline to preserve semantic relevance while injecting task-aware knowledge into LVLMs. We leverage an MDD-adapted feature extractor to retrieve aligned image-text pairs and build a candidate set. We further design the Graph-Structured Taylor Adaptive Scorer (GSTAS) to capture cross-sample relations and propagate query-aligned signals, producing discriminative exemplars. This enables precise selection of semantically aligned, task-relevant demonstrations, enhancing LVLMs for robust MDD. Experiments on four forgery types show that GASP-ICL surpasses strong baselines, delivering gains without LVLM fine-tuning.

