---
layout: default
title: Interleaving Reasoning for Better Text-to-Image Generation
---

# Interleaving Reasoning for Better Text-to-Image Generation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.06945" class="toolbar-btn" target="_blank">📄 arXiv: 2509.06945v2</a>
  <a href="https://arxiv.org/pdf/2509.06945.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.06945v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.06945v2', 'Interleaving Reasoning for Better Text-to-Image Generation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Wenxuan Huang, Shuang Chen, Zheyong Xie, Shaosheng Cao, Shixiang Tang, Yufan Shen, Qingyu Yin, Wenbo Hu, Xiaoman Wang, Yuntian Tang, Junbo Qiao, Yue Guo, Yao Hu, Zhenfei Yin, Philip Torr, Yu Cheng, Wanli Ouyang, Shaohui Lin

**分类**: cs.CV, cs.AI, cs.CL, cs.LG

**发布日期**: 2025-09-08 (更新: 2025-09-09)

**🔗 代码/项目**: [GITHUB](https://github.com/Osilly/Interleaving-Reasoning-Generation)

---

## 💡 一句话要点

**提出交错推理生成框架IRG，提升文本到图像生成中的指令遵循和细节保持能力**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `文本到图像生成` `交错推理` `图像合成` `文本理解` `多模态学习`

## 📋 核心要点

1. 现有文本到图像生成模型在指令遵循和细节保持方面存在不足，与紧耦合理解与生成的系统相比仍有差距。
2. 提出交错推理生成（IRG）框架，通过交替进行文本思考和图像合成，逐步优化图像质量和细节。
3. 构建IRGL-300K数据集，并设计两阶段训练方法，实验结果表明该方法在多个指标上取得了显著提升。

## 📝 摘要（中文）

本文提出交错推理生成（IRG）框架，旨在提升文本到图像（T2I）生成模型的指令遵循和细节保持能力，缩小与GPT-4o等紧耦合理解与生成系统之间的差距。IRG框架交替进行基于文本的思考和图像合成：模型首先生成文本思考指导初始图像，然后反思结果以改进细节、视觉质量和美学，同时保持语义一致性。为了有效训练IRG，提出了交错推理生成学习（IRGL）方法，针对两个子目标：增强初始思考和生成阶段以建立核心内容和基本质量，以及实现高质量的文本反思并在后续图像中忠实地实施这些改进。构建了IRGL-300K数据集，该数据集被组织成六种分解的学习模式，共同涵盖了学习基于文本的思考和完整的思考-图像轨迹。实验表明，该方法取得了SoTA性能，在GenEval、WISE、TIIF、GenAI-Bench和OneIG-EN上获得了5-10分的绝对收益，同时显著提高了视觉质量和精细的保真度。

## 🔬 方法详解

**问题定义**：文本到图像生成任务旨在根据给定的文本描述生成对应的图像。现有方法在指令遵循和细节保持方面存在不足，难以生成高质量、符合用户意图的图像。痛点在于模型难以理解文本描述中的细粒度信息，并且难以将这些信息准确地反映到生成的图像中。

**核心思路**：本文的核心思路是引入交错推理机制，让模型在生成图像的过程中进行文本思考和图像合成的交替迭代。通过文本思考来指导图像生成，并通过图像合成的结果来反思和改进文本思考，从而逐步优化图像的质量和细节。这种交错推理的方式可以帮助模型更好地理解文本描述，并将其准确地反映到生成的图像中。

**技术框架**：IRG框架包含两个主要阶段：初始思考和生成阶段，以及反思和改进阶段。在初始思考和生成阶段，模型首先根据文本描述生成一段文本思考，然后根据这段文本思考生成初始图像。在反思和改进阶段，模型对初始图像进行分析，并生成一段文本反思，然后根据这段文本反思对初始图像进行改进，生成最终的图像。整个过程可以迭代多次，直到生成满意的图像为止。

**关键创新**：最重要的技术创新点是引入了交错推理机制，将文本思考和图像合成结合起来，实现了更精细的图像生成控制。与现有方法相比，IRG框架可以更好地理解文本描述中的细粒度信息，并将其准确地反映到生成的图像中。

**关键设计**：IRGL-300K数据集包含六种分解的学习模式，用于训练模型的文本思考和图像合成能力。两阶段训练方法首先训练模型的文本思考和反思能力，然后训练模型的完整交错推理生成能力。损失函数包括文本思考损失、图像合成损失和反思损失，用于优化模型的各个模块。

## 📊 实验亮点

实验结果表明，IRG框架在GenEval、WISE、TIIF、GenAI-Bench和OneIG-EN等多个指标上取得了显著提升，绝对收益达到5-10分。同时，视觉质量和精细的保真度也得到了大幅提高。这些结果证明了IRG框架在文本到图像生成任务中的有效性。

## 🎯 应用场景

该研究成果可应用于各种需要高质量图像生成的场景，例如艺术创作、产品设计、游戏开发、广告制作等。通过提供更精确的文本控制和更逼真的图像效果，可以极大地提升创作效率和用户体验。未来，该技术有望进一步扩展到视频生成、3D模型生成等领域，为内容创作带来更多可能性。

## 📄 摘要（原文）

> Unified multimodal understanding and generation models recently have achieve significant improvement in image generation capability, yet a large gap remains in instruction following and detail preservation compared to systems that tightly couple comprehension with generation such as GPT-4o. Motivated by recent advances in interleaving reasoning, we explore whether such reasoning can further improve Text-to-Image (T2I) generation. We introduce Interleaving Reasoning Generation (IRG), a framework that alternates between text-based thinking and image synthesis: the model first produces a text-based thinking to guide an initial image, then reflects on the result to refine fine-grained details, visual quality, and aesthetics while preserving semantics. To train IRG effectively, we propose Interleaving Reasoning Generation Learning (IRGL), which targets two sub-goals: (1) strengthening the initial think-and-generate stage to establish core content and base quality, and (2) enabling high-quality textual reflection and faithful implementation of those refinements in a subsequent image. We curate IRGL-300K, a dataset organized into six decomposed learning modes that jointly cover learning text-based thinking, and full thinking-image trajectories. Starting from a unified foundation model that natively emits interleaved text-image outputs, our two-stage training first builds robust thinking and reflection, then efficiently tunes the IRG pipeline in the full thinking-image trajectory data. Extensive experiments show SoTA performance, yielding absolute gains of 5-10 points on GenEval, WISE, TIIF, GenAI-Bench, and OneIG-EN, alongside substantial improvements in visual quality and fine-grained fidelity. The code, model weights and datasets will be released in: https://github.com/Osilly/Interleaving-Reasoning-Generation .

