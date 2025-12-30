---
layout: default
title: "Multi-Track Multimodal Learning on iMiGUE: Micro-Gesture and Emotion Recognition"
---

# Multi-Track Multimodal Learning on iMiGUE: Micro-Gesture and Emotion Recognition

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.23291" class="toolbar-btn" target="_blank">📄 arXiv: 2512.23291v1</a>
  <a href="https://arxiv.org/pdf/2512.23291.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.23291v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.23291v1', 'Multi-Track Multimodal Learning on iMiGUE: Micro-Gesture and Emotion Recognition')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Arman Martirosyan, Shahane Tigranyan, Maria Razzhivina, Artak Aslanyan, Nazgul Salikhova, Ilya Makarov, Andrey Savchenko, Aram Avetisyan

**分类**: cs.CV

**发布日期**: 2025-12-29

---

## 💡 一句话要点

**针对iMiGUE数据集，提出多轨多模态学习框架用于微手势和情感识别**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `微手势识别` `情感识别` `多模态学习` `跨模态融合` `行为分析` `深度学习` `iMiGUE数据集`

## 📋 核心要点

1. 微手势和情感识别面临捕捉细微行为模式的挑战，现有方法难以有效融合多模态信息。
2. 提出多轨多模态学习框架，针对微手势和情感识别分别设计了跨模态融合策略。
3. 在iMiGUE数据集上的实验表明，该方法在基于行为的情感预测任务中取得了优异的性能，排名第二。

## 📝 摘要（中文）

微手势识别和基于行为的情感预测都是极具挑战性的任务，需要对细微的人类行为进行建模，主要利用视频和骨骼姿态数据。本文提出了两种多模态框架，旨在解决iMiGUE数据集上的这两个问题。对于微手势分类，探索了RGB和3D姿态表示的互补优势，以捕捉细致的时空模式。为了全面表示手势，分别使用MViTv2-S和2s-AGCN提取视频和骨骼嵌入，然后通过跨模态Token融合模块整合空间和姿态信息。对于情感识别，框架扩展到基于行为的情感预测，这是一个基于视觉线索识别情绪状态的二元分类任务。利用SwinFace和MViTv2-S模型提取面部和上下文嵌入，并通过InterFusion模块融合它们，旨在捕捉情感表达和身体手势。在MiGA 2025挑战赛的iMiGUE数据集上进行的实验表明，该方法在基于行为的情感预测任务中表现出强大的性能和准确性，并获得了第二名。

## 🔬 方法详解

**问题定义**：论文旨在解决微手势识别和基于行为的情感预测两个问题。现有方法在处理细微的人类行为模式，以及有效融合来自视频、骨骼姿态等不同模态的信息方面存在不足，难以充分利用多模态数据的互补性。

**核心思路**：论文的核心思路是利用多模态学习框架，针对微手势和情感识别任务，分别设计专门的跨模态融合策略。通过提取不同模态的特征表示，并采用有效的融合机制，从而捕捉细微的时空模式和情感表达。

**技术框架**：整体框架包含两个主要分支：微手势识别和情感识别。对于微手势识别，首先使用MViTv2-S和2s-AGCN分别提取视频和骨骼姿态的嵌入表示，然后通过Cross-Modal Token Fusion模块进行融合。对于情感识别，使用SwinFace和MViTv2-S提取面部和上下文嵌入，并通过InterFusion模块进行融合。两个分支的最终输出分别是微手势类别和情感状态的预测结果。

**关键创新**：论文的关键创新在于针对不同的任务，设计了专门的跨模态融合模块。Cross-Modal Token Fusion模块旨在融合视频和骨骼姿态的空间和姿态信息，而InterFusion模块旨在捕捉情感表达和身体手势之间的关联。这种针对特定任务的融合策略能够更有效地利用多模态数据的互补性。

**关键设计**：在微手势识别分支，MViTv2-S和2s-AGCN的选择考虑了它们在视频和骨骼姿态特征提取方面的优势。Cross-Modal Token Fusion模块的具体实现细节（例如，注意力机制的选择、融合方式等）未知。在情感识别分支，SwinFace用于提取面部特征，MViTv2-S用于提取上下文特征，InterFusion模块的具体实现细节也未知。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.23291v1/dt1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.23291v1/cmtf.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.23291v1/architecture3.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

该方法在iMiGUE数据集的MiGA 2025挑战赛中，在基于行为的情感预测任务中取得了第二名的成绩，验证了该方法在处理细微行为模式和融合多模态信息方面的有效性。具体的性能数据和对比基线未知，但排名结果表明该方法具有竞争力。

## 🎯 应用场景

该研究成果可应用于人机交互、智能监控、医疗健康等领域。例如，在人机交互中，可以利用微手势识别实现更自然、更精细的交互方式；在智能监控中，可以利用情感识别技术检测异常行为和潜在风险；在医疗健康领域，可以辅助医生进行心理评估和疾病诊断。

## 📄 摘要（原文）

> Micro-gesture recognition and behavior-based emotion prediction are both highly challenging tasks that require modeling subtle, fine-grained human behaviors, primarily leveraging video and skeletal pose data. In this work, we present two multimodal frameworks designed to tackle both problems on the iMiGUE dataset. For micro-gesture classification, we explore the complementary strengths of RGB and 3D pose-based representations to capture nuanced spatio-temporal patterns. To comprehensively represent gestures, video, and skeletal embeddings are extracted using MViTv2-S and 2s-AGCN, respectively. Then, they are integrated through a Cross-Modal Token Fusion module to combine spatial and pose information. For emotion recognition, our framework extends to behavior-based emotion prediction, a binary classification task identifying emotional states based on visual cues. We leverage facial and contextual embeddings extracted using SwinFace and MViTv2-S models and fuse them through an InterFusion module designed to capture emotional expressions and body gestures. Experiments conducted on the iMiGUE dataset, within the scope of the MiGA 2025 Challenge, demonstrate the robust performance and accuracy of our method in the behavior-based emotion prediction task, where our approach secured 2nd place.

