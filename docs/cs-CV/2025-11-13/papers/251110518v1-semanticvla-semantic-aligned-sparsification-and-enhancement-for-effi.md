---
layout: default
title: SemanticVLA: Semantic-Aligned Sparsification and Enhancement for Efficient Robotic Manipulation
---

# SemanticVLA: Semantic-Aligned Sparsification and Enhancement for Efficient Robotic Manipulation

**arXiv**: [2511.10518v1](https://arxiv.org/abs/2511.10518) | [PDF](https://arxiv.org/pdf/2511.10518.pdf)

**作者**: Wei Li, Renshan Zhang, Rui Shao, Zhijian Fang, Kaiwen Zhou, Zhuotao Tian, Liqiang Nie

**分类**: cs.CV, cs.RO

**发布日期**: 2025-11-13

**备注**: Accepted to AAAI 2026 (Oral), Project Page: https://github.com/JiuTian-VL/SemanticVLA

**🔗 代码/项目**: [GITHUB](https://github.com/JiuTian-VL/SemanticVLA)

---

## 💡 一句话要点

**SemanticVLA：面向高效机器人操作的语义对齐稀疏化与增强**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)**

**关键词**: `机器人操作` `视觉语言动作模型` `语义对齐` `稀疏化` `特征融合` `深度学习` `机器人控制`

## 📋 核心要点

1. 现有VLA模型在机器人操作中存在感知冗余和指令-视觉对齐不足的问题，导致效率低下和泛化能力弱。
2. SemanticVLA通过语义对齐的稀疏化和增强，有效减少冗余信息，并增强语义与动作的关联，提升操作性能。
3. 实验结果表明，SemanticVLA在LIBERO基准测试中显著超越现有方法，并在训练和推理效率上均有提升。

## 📝 摘要（中文）

视觉-语言-动作(VLA)模型在机器人操作领域取得了显著进展，但实际部署仍受到两个关键限制的阻碍：1)感知冗余，即不相关的视觉输入被低效处理；2)表面指令-视觉对齐，阻碍了动作的语义基础。本文提出了SemanticVLA，一种新颖的VLA框架，它执行语义对齐的稀疏化和增强，以实现高效的机器人操作。具体来说：1)为了在保持语义对齐的同时稀疏化冗余感知，语义引导的双视觉修剪器(SD-Pruner)执行：指令驱动的修剪器(ID-Pruner)提取SigLIP中的全局动作线索和局部语义锚点；空间聚合修剪器(SA-Pruner)将几何丰富的特征压缩为DINOv2中的任务自适应tokens。2)为了利用稀疏化的特征并将语义与空间几何相结合，语义互补的分层融合器(SH-Fuser)融合SigLIP和DINOv2中的密集patches和稀疏tokens，以实现连贯的表示。3)为了增强从感知到动作的转换，语义条件动作耦合器(SA-Coupler)取代了传统的观察到自由度(DoF)的方法，从而为操作任务产生更高效和可解释的行为建模。在模拟和真实世界任务上的大量实验表明，SemanticVLA在性能和效率方面都创造了新的SOTA。在LIBERO基准测试中，SemanticVLA的成功率超过OpenVLA 21.1%，同时训练成本和推理延迟分别降低了3.0倍和2.7倍。SemanticVLA已开源，可在https://github.com/JiuTian-VL/SemanticVLA公开获取。

## 🔬 方法详解

**问题定义**：现有VLA模型在机器人操作任务中面临着两个主要问题：一是视觉感知的冗余，即模型需要处理大量与当前任务无关的视觉信息，导致计算资源的浪费；二是指令和视觉信息之间的对齐不够充分，使得模型难以准确理解指令的语义，从而影响操作的精度和效率。现有方法通常采用端到端的训练方式，缺乏对视觉信息的选择性处理和对语义信息的有效利用，导致模型难以在复杂环境中泛化。

**核心思路**：SemanticVLA的核心思路是通过语义对齐的稀疏化和增强来解决上述问题。具体来说，首先通过语义引导的双视觉修剪器(SD-Pruner)来减少视觉信息的冗余，同时保留关键的语义信息。然后，通过语义互补的分层融合器(SH-Fuser)将稀疏化的视觉特征与语义信息进行融合，从而得到更具表达力的表示。最后，通过语义条件动作耦合器(SA-Coupler)将融合后的表示映射到动作空间，从而实现高效的机器人操作。

**技术框架**：SemanticVLA的整体框架包括三个主要模块：SD-Pruner、SH-Fuser和SA-Coupler。SD-Pruner负责对视觉信息进行稀疏化，包括ID-Pruner和SA-Pruner两个子模块，分别从指令和空间几何的角度进行修剪。SH-Fuser负责将稀疏化的视觉特征与语义信息进行融合，采用分层融合的方式，逐步将不同尺度的特征进行整合。SA-Coupler负责将融合后的表示映射到动作空间，采用语义条件的方式，根据不同的语义信息生成不同的动作。

**关键创新**：SemanticVLA的关键创新在于提出了语义对齐的稀疏化和增强策略。传统的VLA模型通常直接将所有视觉信息输入到模型中，而SemanticVLA则通过SD-Pruner选择性地保留与当前任务相关的视觉信息，从而减少了计算资源的浪费。此外，SemanticVLA还通过SH-Fuser将视觉特征与语义信息进行融合，从而增强了模型对指令的理解能力。SA-Coupler则通过语义条件的方式，使得模型能够根据不同的语义信息生成不同的动作，从而提高了操作的精度和效率。

**关键设计**：SD-Pruner中的ID-Pruner利用SigLIP模型提取全局动作线索和局部语义锚点，SA-Pruner利用DINOv2模型提取几何丰富的特征，并将这些特征压缩为任务自适应的tokens。SH-Fuser采用分层融合的方式，逐步将SigLIP和DINOv2的特征进行整合。SA-Coupler采用语义条件的方式，根据不同的语义信息生成不同的动作。损失函数方面，采用了标准的交叉熵损失函数和回归损失函数，用于优化模型的参数。

## 📊 实验亮点

SemanticVLA在LIBERO基准测试中取得了显著的性能提升，成功率超过OpenVLA 21.1%，同时训练成本和推理延迟分别降低了3.0倍和2.7倍。这些结果表明，SemanticVLA在性能和效率方面都具有显著优势，为机器人操作领域的研究提供了新的思路。

## 🎯 应用场景

SemanticVLA具有广泛的应用前景，可应用于各种机器人操作任务，如物体抓取、装配、导航等。该研究成果有助于提高机器人在复杂环境中的操作效率和精度，降低计算成本，并为未来的机器人智能化发展奠定基础。此外，该方法还可以推广到其他视觉-语言任务中，如图像描述、视觉问答等。

## 📄 摘要（原文）

> Vision-Language-Action (VLA) models have advanced in robotic manipulation, yet practical deployment remains hindered by two key limitations: 1) perceptual redundancy, where irrelevant visual inputs are processed inefficiently, and 2) superficial instruction-vision alignment, which hampers semantic grounding of actions. In this paper, we propose SemanticVLA, a novel VLA framework that performs Semantic-Aligned Sparsification and Enhancement for Efficient Robotic Manipulation. Specifically: 1) To sparsify redundant perception while preserving semantic alignment, Semantic-guided Dual Visual Pruner (SD-Pruner) performs: Instruction-driven Pruner (ID-Pruner) extracts global action cues and local semantic anchors in SigLIP; Spatial-aggregation Pruner (SA-Pruner) compacts geometry-rich features into task-adaptive tokens in DINOv2. 2) To exploit sparsified features and integrate semantics with spatial geometry, Semantic-complementary Hierarchical Fuser (SH-Fuser) fuses dense patches and sparse tokens across SigLIP and DINOv2 for coherent representation. 3) To enhance the transformation from perception to action, Semantic-conditioned Action Coupler (SA-Coupler) replaces the conventional observation-to-DoF approach, yielding more efficient and interpretable behavior modeling for manipulation tasks. Extensive experiments on simulation and real-world tasks show that SemanticVLA sets a new SOTA in both performance and efficiency. SemanticVLA surpasses OpenVLA on LIBERO benchmark by 21.1% in success rate, while reducing training cost and inference latency by 3.0-fold and 2.7-fold.SemanticVLA is open-sourced and publicly available at https://github.com/JiuTian-VL/SemanticVLA

