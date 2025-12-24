---
layout: default
title: Learning Dynamics of Meta-Learning in Small Model Pretraining
---

# Learning Dynamics of Meta-Learning in Small Model Pretraining

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.02189" class="toolbar-btn" target="_blank">📄 arXiv: 2508.02189v2</a>
  <a href="https://arxiv.org/pdf/2508.02189.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.02189v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.02189v2', 'Learning Dynamics of Meta-Learning in Small Model Pretraining')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: David Demitri Africa, Yuval Weiss, Paula Buttery, Richard Diehl Martinez

**分类**: cs.CL, cs.AI

**发布日期**: 2025-08-04 (更新: 2025-11-07)

**备注**: Accepted (oral) to Student Research Workshop at IJCNLP-AACL 2025

---

## 💡 一句话要点

**提出元学习动态以优化小模型预训练**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `元学习` `小模型` `预训练` `自然语言处理` `多语言识别` `可解释性` `训练动态`

## 📋 核心要点

1. 现有的大型语言模型虽然性能优越，但训练成本高，限制了其在小型模型中的应用。
2. 本文提出将一阶MAML与子集掩蔽语言模型预训练相结合，旨在提升小模型的训练效率和可解释性。
3. 实验结果表明，模型在损失上最多提前1.6倍达到相同水平，并在多语言NER任务中表现出显著的F1提升。

## 📝 摘要（中文）

大型语言模型虽然强大，但训练成本高昂。本文探讨元学习是否能使小型语言模型的预训练不仅更优，还更具可解释性。我们将一阶MAML与子集掩蔽语言模型预训练相结合，构建了四个LLama风格的解码器模型（参数量从11M到570M），并在多个设置和实际应用中评估其在基础NLP任务上的表现。与传统训练相比，我们的模型在损失上最多提前1.6倍达到相同水平，且在相同计算条件下提升了多语言通用命名实体识别的F1分数，同时训练动态更易于理解，表现为网络表示的多样化和后续的压缩过程。这种两阶段的变化在有效秩曲线和注意力头熵中均有体现，清晰标识出各层的专业化和再收敛过程。代码、检查点和WandB日志已公开。

## 🔬 方法详解

**问题定义**：本文旨在解决小型语言模型预训练的效率和可解释性问题。现有方法通常训练成本高且缺乏可解释性，限制了其在实际应用中的推广。

**核心思路**：通过将一阶MAML与子集掩蔽语言模型预训练相结合，本文提出了一种新的训练策略，旨在加速模型收敛并提高其在多语言任务中的表现。

**技术框架**：整体架构包括两个主要阶段：首先是网络表示的多样化阶段，其次是压缩阶段。模型在这两个阶段中表现出不同的动态特征，便于理解和分析。

**关键创新**：最重要的创新在于将元学习动态引入小模型的预训练中，使得训练过程不仅更快，而且更具可解释性。这与传统的训练方法形成了鲜明对比。

**关键设计**：在模型设计中，采用了特定的损失函数和参数设置，以优化训练过程中的有效秩曲线和注意力头熵，确保模型在不同层次上能够有效地进行专业化和再收敛。

## 📊 实验亮点

实验结果显示，所提出的模型在损失上最多提前1.6倍达到相同水平，并在多语言通用命名实体识别任务中，在相同计算条件下实现了F1分数的显著提升，验证了模型的有效性和优势。

## 🎯 应用场景

该研究的潜在应用领域包括自然语言处理、机器翻译和多语言信息提取等。通过提升小型语言模型的训练效率和可解释性，研究成果可以促进其在资源受限环境中的应用，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> Large language models are powerful but costly. We ask whether meta-learning can make the pretraining of small language models not only better but also more interpretable. We integrate first-order MAML with subset-masked LM pretraining, producing four LLama-style decoder-only models (11M-570M params), and evaluate it on a fundamental NLP task with many settings and real-world applications. Compared with vanilla training, our model (i) reaches the same loss up to 1.6x sooner, (ii) improves F1 on multilingual Universal NER under equal compute, and (iii) makes the training dynamics easy to read: first the network's representations fan out ("diversify") and later they collapse into a smaller, shared subspace ("compress"). This two-stage shift shows up as a rise-and-fall in both effective-rank curves and attention-head entropy. The same curves pinpoint which layers specialise earliest and which later reconverge, giving a compact, interpretable signature of meta-adaptation. Code, checkpoints and WandB logs are released.

