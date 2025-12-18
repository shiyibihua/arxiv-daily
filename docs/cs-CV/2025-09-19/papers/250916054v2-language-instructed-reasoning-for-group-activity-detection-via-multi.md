---
layout: default
title: Language-Instructed Reasoning for Group Activity Detection via Multimodal Large Language Model
---

# Language-Instructed Reasoning for Group Activity Detection via Multimodal Large Language Model

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.16054" class="toolbar-btn" target="_blank">📄 arXiv: 2509.16054v2</a>
  <a href="https://arxiv.org/pdf/2509.16054.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.16054v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.16054v2', 'Language-Instructed Reasoning for Group Activity Detection via Multimodal Large Language Model')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jihua Peng, Qianxiong Xu, Yichen Liu, Chenxi Liu, Cheng Long, Rui Zhao, Ziyue Li

**分类**: cs.CV

**发布日期**: 2025-09-19 (更新: 2025-12-05)

**备注**: This work is being incorporated into a larger study

---

## 💡 一句话要点

**提出LIR-GAD，利用多模态大语言模型进行语言指导的群体活动检测。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `群体活动检测` `多模态大语言模型` `语言指导推理` `视频理解` `多模态融合`

## 📋 核心要点

1. 现有群体活动检测方法依赖视觉特征的隐式模式识别，缺乏上下文推理能力和可解释性。
2. LIR-GAD通过多模态大语言模型，结合语言指令和视觉信息，增强了模型对群体活动的语义理解。
3. 实验结果表明，LIR-GAD在群体活动检测任务中表现出色，显著提升了性能。

## 📝 摘要（中文）

群体活动检测(GAD)旨在视频序列中同时识别群体成员并分类他们的集体活动。现有的基于深度学习的方法开发了专门的架构（例如，Transformer网络）来建模个体角色的动态以及个体和群体之间的语义依赖关系。然而，它们仅仅依赖于视觉特征的隐式模式识别，并且难以进行上下文推理和解释。本文提出了LIR-GAD，这是一个新颖的语言指导推理框架，通过多模态大语言模型(MLLM)进行GAD。我们的方法通过引入活动级别的<ACT> token和多个特定于集群的<GROUP> token来扩展MLLM的原始词汇表。我们处理视频帧以及两个专门设计的token和语言指令，然后将其集成到MLLM中。MLLM中嵌入的预训练常识知识使<ACT> token和<GROUP> token能够有效地捕获集体活动的语义信息，并分别学习不同组的独特表示特征。此外，我们引入了多标签分类损失，以进一步增强<ACT> token学习区分性语义表示的能力。然后，我们设计了一个多模态双重对齐融合(MDAF)模块，该模块将MLLM的隐藏嵌入（对应于设计的token）与视觉特征集成，从而显着提高了GAD的性能。定量和定性实验都证明了我们提出的方法在GAD任务中的优越性能。

## 🔬 方法详解

**问题定义**：群体活动检测(GAD)旨在同时识别视频中群体成员及其集体活动。现有方法主要依赖深度学习模型，特别是Transformer，来建模个体角色动态和个体-群体间的语义依赖。然而，这些方法仅依赖视觉特征的隐式模式识别，缺乏利用上下文信息进行推理的能力，并且可解释性较差。

**核心思路**：LIR-GAD的核心在于利用多模态大语言模型(MLLM)的预训练知识和语言理解能力，结合视觉信息，进行语言指导的群体活动检测。通过引入特定token和语言指令，引导MLLM理解和推理群体活动，从而提升检测性能和可解释性。

**技术框架**：LIR-GAD框架主要包含以下几个阶段：1) **词汇扩展**：在MLLM的词汇表中引入活动级别的<ACT> token和多个集群特定的<GROUP> token。2) **多模态输入**：将视频帧、设计的token和语言指令输入到MLLM中。3) **特征学习**：利用MLLM的预训练知识，使<ACT>和<GROUP> token捕获集体活动的语义信息，学习不同组的表示特征。4) **多标签分类**：引入多标签分类损失，增强<ACT> token学习区分性语义表示的能力。5) **多模态融合**：设计多模态双重对齐融合(MDAF)模块，将MLLM的隐藏嵌入与视觉特征融合，提升GAD性能。

**关键创新**：LIR-GAD的关键创新在于：1) **语言指导的推理**：利用MLLM的语言理解能力，通过语言指令引导模型进行群体活动检测，增强了模型的推理能力和可解释性。2) **多模态双重对齐融合(MDAF)**：设计MDAF模块，有效融合MLLM的语义信息和视觉特征，提升了GAD的性能。

**关键设计**：1) **<ACT>和<GROUP> token设计**：通过引入活动级别和集群特定的token，使MLLM能够更好地理解和表示群体活动。2) **多标签分类损失**：使用多标签分类损失来训练<ACT> token，使其能够学习区分不同的活动类别。3) **MDAF模块**：MDAF模块的具体结构和融合策略（例如，注意力机制）是影响性能的关键因素。

## 📊 实验亮点

LIR-GAD通过引入语言指导和多模态融合，在群体活动检测任务上取得了显著的性能提升。具体实验数据（例如，在特定数据集上的mAP提升）需要在论文中查找。该方法优于现有的基于深度学习的方法，尤其是在处理复杂场景和需要上下文推理的任务时。

## 🎯 应用场景

LIR-GAD可应用于智能视频监控、人群行为分析、社交活动理解等领域。例如，在监控场景中，可以自动识别异常群体行为，如打架斗殴等。在社交媒体分析中，可以理解用户发布的视频内容，识别其中的群体活动类型。该研究有助于提升计算机视觉系统对复杂场景的理解能力，具有重要的实际应用价值。

## 📄 摘要（原文）

> Group activity detection (GAD) aims to simultaneously identify group members and categorize their collective activities within video sequences. Existing deep learning-based methods develop specialized architectures (e.g., transformer networks) to model the dynamics of individual roles and semantic dependencies between individuals and groups. However, they rely solely on implicit pattern recognition from visual features and struggle with contextual reasoning and explainability. In this work, we propose LIR-GAD, a novel framework of language-instructed reasoning for GAD via Multimodal Large Language Model (MLLM). Our approach expand the original vocabulary of MLLM by introducing an activity-level <ACT> token and multiple cluster-specific <GROUP> tokens. We process video frames alongside two specially designed tokens and language instructions, which are then integrated into the MLLM. The pretrained commonsense knowledge embedded in the MLLM enables the <ACT> token and <GROUP> tokens to effectively capture the semantic information of collective activities and learn distinct representational features of different groups, respectively. Also, we introduce a multi-label classification loss to further enhance the <ACT> token's ability to learn discriminative semantic representations. Then, we design a Multimodal Dual-Alignment Fusion (MDAF) module that integrates MLLM's hidden embeddings corresponding to the designed tokens with visual features, significantly enhancing the performance of GAD. Both quantitative and qualitative experiments demonstrate the superior performance of our proposed method in GAD taks.

