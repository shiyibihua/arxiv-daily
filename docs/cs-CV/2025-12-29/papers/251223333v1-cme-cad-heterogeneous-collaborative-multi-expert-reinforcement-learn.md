---
layout: default
title: "CME-CAD: Heterogeneous Collaborative Multi-Expert Reinforcement Learning for CAD Code Generation"
---

# CME-CAD: Heterogeneous Collaborative Multi-Expert Reinforcement Learning for CAD Code Generation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.23333" class="toolbar-btn" target="_blank">📄 arXiv: 2512.23333v1</a>
  <a href="https://arxiv.org/pdf/2512.23333.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.23333v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.23333v1', 'CME-CAD: Heterogeneous Collaborative Multi-Expert Reinforcement Learning for CAD Code Generation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Ke Niu, Haiyang Yu, Zhuofan Chen, Zhengtao Yao, Weitao Jia, Xiaodong Ge, Jingqun Tang, Benlei Cui, Bin Li, Xiangyang Xue

**分类**: cs.CV

**发布日期**: 2025-12-29

---

## 💡 一句话要点

**提出CME-CAD异构协作多专家强化学习框架，用于高精度可编辑CAD代码生成。**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `CAD代码生成` `强化学习` `多专家协作` `异构学习` `工业设计`

## 📋 核心要点

1. 现有方法从草图重建3D模型通常产生不可编辑且近似的模型，无法满足工业设计中对精度和可编辑性的严格要求。
2. CME-CAD通过异构多专家协作，结合多专家微调和强化学习，提升CAD代码生成的精度和可编辑性。
3. 论文构建了包含17,299个实例的CADExpert基准数据集，为CAD代码生成领域的研究提供了有力支持。

## 📝 摘要（中文）

本文提出了一种用于CAD代码生成的新型训练范式——异构协作多专家强化学习(CME-CAD)。该方法集成了不同模型的互补优势，促进协作学习，并提高模型生成精确、约束兼容且完全可编辑的CAD模型的能力。我们引入了一个两阶段训练过程：多专家微调(MEFT)和多专家强化学习(MERL)。此外，我们还提出了CADExpert，一个包含17,299个实例的开源基准，包括正交投影和精确的尺寸标注、专家生成的思维链(CoT)过程、可执行的CADQuery代码和渲染的3D模型。

## 🔬 方法详解

**问题定义**：现有CAD建模方法复杂，难以自动化生成高精度、可编辑的CAD模型。从草图重建3D模型的方法通常产生非可编辑的近似模型，无法满足工业设计的严格要求。依赖文本或图像输入的方法需要大量手动标注，限制了其在工业环境中的可扩展性和适用性。

**核心思路**：CME-CAD的核心思路是利用异构多专家的协作，结合各自的优势，共同学习生成CAD代码。通过多专家微调(MEFT)和多专家强化学习(MERL)两个阶段的训练，使模型能够生成精确、约束兼容且完全可编辑的CAD模型。这种方法旨在克服现有方法在精度、可编辑性和自动化程度方面的局限性。

**技术框架**：CME-CAD的整体框架包含两个主要阶段：MEFT和MERL。在MEFT阶段，不同的专家模型（例如，擅长几何推理的模型和擅长代码生成的模型）在CADExpert数据集上进行微调，以提高各自的专业能力。在MERL阶段，这些微调后的专家模型通过强化学习进行协作，共同生成CAD代码。强化学习的目标是最大化奖励函数，该奖励函数考虑了生成的CAD模型的精度、约束兼容性和可编辑性。

**关键创新**：CME-CAD的关键创新在于异构多专家的协作学习范式。与传统的单模型方法相比，CME-CAD能够更好地利用不同模型的优势，从而提高CAD代码生成的质量。此外，两阶段训练过程（MEFT和MERL）也是一个重要的创新，它能够有效地引导模型学习生成高质量的CAD代码。CADExpert数据集的构建也为该领域的研究提供了重要的资源。

**关键设计**：MEFT阶段的关键设计在于选择合适的专家模型和微调策略。MERL阶段的关键设计在于定义合适的奖励函数和强化学习算法。奖励函数需要综合考虑CAD模型的精度、约束兼容性和可编辑性。强化学习算法需要能够有效地探索CAD代码的搜索空间，并找到最优的生成策略。具体的参数设置、损失函数和网络结构等技术细节在论文中可能没有详细描述，属于未知信息。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.23333v1/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.23333v1/x2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.23333v1/x3.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

论文提出了CADExpert基准数据集，包含17,299个实例，为CAD代码生成研究提供了数据基础。CME-CAD框架通过异构多专家协作和两阶段训练，在CAD代码生成任务上取得了显著的性能提升，但具体性能数据和对比基线未知。

## 🎯 应用场景

CME-CAD技术可应用于工业设计、建筑设计、产品设计等领域，实现CAD模型的自动化生成，提高设计效率，降低设计成本。该技术还可以用于逆向工程，从现有产品或零件的图像或扫描数据中自动生成CAD模型。未来，CME-CAD有望与人工智能设计工具集成，实现更加智能化的设计流程。

## 📄 摘要（原文）

> Computer-Aided Design (CAD) is essential in industrial design, but the complexity of traditional CAD modeling and workflows presents significant challenges for automating the generation of high-precision, editable CAD models. Existing methods that reconstruct 3D models from sketches often produce non-editable and approximate models that fall short of meeting the stringent requirements for precision and editability in industrial design. Moreover, the reliance on text or image-based inputs often requires significant manual annotation, limiting their scalability and applicability in industrial settings. To overcome these challenges, we propose the Heterogeneous Collaborative Multi-Expert Reinforcement Learning (CME-CAD) paradigm, a novel training paradigm for CAD code generation. Our approach integrates the complementary strengths of these models, facilitating collaborative learning and improving the model's ability to generate accurate, constraint-compatible, and fully editable CAD models. We introduce a two-stage training process: Multi-Expert Fine-Tuning (MEFT), and Multi-Expert Reinforcement Learning (MERL). Additionally, we present CADExpert, an open-source benchmark consisting of 17,299 instances, including orthographic projections with precise dimension annotations, expert-generated Chain-of-Thought (CoT) processes, executable CADQuery code, and rendered 3D models.

