---
layout: default
title: Language-Guided Grasp Detection with Coarse-to-Fine Learning for Robotic Manipulation
---

# Language-Guided Grasp Detection with Coarse-to-Fine Learning for Robotic Manipulation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.21065" class="toolbar-btn" target="_blank">📄 arXiv: 2512.21065v1</a>
  <a href="https://arxiv.org/pdf/2512.21065.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.21065v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.21065v1', 'Language-Guided Grasp Detection with Coarse-to-Fine Learning for Robotic Manipulation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zebin Jiang, Tianle Jin, Xiangtong Yao, Alois Knoll, Hu Cao

**分类**: cs.RO, cs.CV

**发布日期**: 2025-12-24

**备注**: Submitted to IEEE Journal

---

## 💡 一句话要点

**提出基于粗到精学习的语言引导抓取检测方法，用于机器人操作**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱三：空间感知与语义 (Perception & Semantics)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `机器人抓取` `语言引导` `跨模态融合` `粗到精学习` `动态卷积`

## 📋 核心要点

1. 现有语言引导的抓取方法依赖浅层融合，存在语义基础薄弱和语言意图与视觉推理对齐不足的问题。
2. 提出一种粗到精的语言引导抓取检测（LGGD）方法，通过分层跨模态融合逐步注入语言线索。
3. 实验表明，LGGD在泛化性和鲁棒性上优于现有方法，并在真实机器人平台上验证了其有效性。

## 📝 摘要（中文）

抓取是机器人操作中最具挑战性的基本能力之一，尤其是在非结构化、杂乱和语义多样的环境中。最近的研究越来越多地探索语言引导的操作，机器人不仅感知场景，还能理解任务相关的自然语言指令。然而，现有的语言条件抓取方法通常依赖于浅层融合策略，导致有限的语义基础和语言意图与视觉抓取推理之间的弱对齐。本文提出了一种基于粗到精学习范式的语言引导抓取检测（LGGD）方法，用于机器人操作。LGGD利用基于CLIP的视觉和文本嵌入，在分层跨模态融合管道中逐步将语言线索注入到视觉特征重建过程中。这种设计实现了细粒度的视觉-语义对齐，并提高了预测抓取相对于任务指令的可行性。此外，我们引入了一种语言条件动态卷积头（LDCH），它基于句子级特征混合多个卷积专家，从而实现指令自适应的粗掩码和抓取预测。最终的细化模块进一步增强了复杂场景中的抓取一致性和鲁棒性。在OCID-VLG和Grasp-Anything++数据集上的实验表明，LGGD超越了现有的语言引导抓取方法，对未见过的物体和不同的语言查询表现出强大的泛化能力。此外，在真实机器人平台上的部署证明了我们的方法在执行精确的、指令条件下的抓取动作方面的实际有效性。代码将在接收后公开发布。

## 🔬 方法详解

**问题定义**：论文旨在解决机器人操作中，如何利用自然语言指令更准确、更鲁棒地进行物体抓取的问题。现有方法通常采用浅层融合策略，无法充分理解语言指令中的语义信息，导致抓取位置不准确，对复杂环境的适应性较差。

**核心思路**：论文的核心思路是通过一种粗到精的学习范式，逐步将语言信息融入到视觉特征中，实现细粒度的视觉-语义对齐。首先进行粗略的抓取区域预测，然后逐步细化抓取姿态，从而提高抓取的准确性和鲁棒性。

**技术框架**：LGGD的整体架构包含以下几个主要模块：1) 基于CLIP的视觉和文本特征提取模块，用于提取视觉和语言的嵌入表示；2) 分层跨模态融合模块，逐步将语言信息注入到视觉特征重建过程中；3) 语言条件动态卷积头（LDCH），用于生成指令自适应的粗掩码和抓取预测；4) 抓取细化模块，进一步增强抓取的一致性和鲁棒性。

**关键创新**：论文的关键创新在于：1) 提出了粗到精的学习范式，实现了细粒度的视觉-语义对齐；2) 引入了语言条件动态卷积头（LDCH），能够根据不同的语言指令动态调整卷积核的参数，从而实现指令自适应的抓取预测。

**关键设计**：在分层跨模态融合模块中，采用了多层Transformer结构，逐步将语言特征融入到视觉特征中。LDCH模块中，使用了多个卷积专家，每个专家负责处理不同类型的语言指令。通过句子级别的特征来混合这些专家，从而实现指令自适应的抓取预测。损失函数包括抓取分类损失、抓取回归损失和掩码预测损失。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.21065v1/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.21065v1/Images/rectangular_grasp.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.21065v1/x2.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

LGGD在OCID-VLG和Grasp-Anything++数据集上超越了现有的语言引导抓取方法，展现出对未见物体的强大泛化能力和对多样语言查询的适应性。在真实机器人平台上的部署验证了其在执行精确、指令条件下的抓取动作方面的有效性。具体性能数据将在论文公开发布后提供。

## 🎯 应用场景

该研究成果可应用于智能仓储、智能制造、家庭服务机器人等领域。通过结合自然语言指令，机器人可以更灵活、更智能地完成各种抓取任务，例如根据用户指令抓取特定物品、在复杂环境中进行物体整理等，具有重要的实际应用价值和广阔的发展前景。

## 📄 摘要（原文）

> Grasping is one of the most fundamental challenging capabilities in robotic manipulation, especially in unstructured, cluttered, and semantically diverse environments. Recent researches have increasingly explored language-guided manipulation, where robots not only perceive the scene but also interpret task-relevant natural language instructions. However, existing language-conditioned grasping methods typically rely on shallow fusion strategies, leading to limited semantic grounding and weak alignment between linguistic intent and visual grasp reasoning.In this work, we propose Language-Guided Grasp Detection (LGGD) with a coarse-to-fine learning paradigm for robotic manipulation. LGGD leverages CLIP-based visual and textual embeddings within a hierarchical cross-modal fusion pipeline, progressively injecting linguistic cues into the visual feature reconstruction process. This design enables fine-grained visual-semantic alignment and improves the feasibility of the predicted grasps with respect to task instructions. In addition, we introduce a language-conditioned dynamic convolution head (LDCH) that mixes multiple convolution experts based on sentence-level features, enabling instruction-adaptive coarse mask and grasp predictions. A final refinement module further enhances grasp consistency and robustness in complex scenes.Experiments on the OCID-VLG and Grasp-Anything++ datasets show that LGGD surpasses existing language-guided grasping methods, exhibiting strong generalization to unseen objects and diverse language queries. Moreover, deployment on a real robotic platform demonstrates the practical effectiveness of our approach in executing accurate, instruction-conditioned grasp actions. The code will be released publicly upon acceptance.

