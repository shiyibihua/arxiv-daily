---
layout: default
title: Reviving DSP for Advanced Theorem Proving in the Era of Reasoning Models
---

# Reviving DSP for Advanced Theorem Proving in the Era of Reasoning Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.11487" class="toolbar-btn" target="_blank">📄 arXiv: 2506.11487v1</a>
  <a href="https://arxiv.org/pdf/2506.11487.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.11487v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.11487v1', 'Reviving DSP for Advanced Theorem Proving in the Era of Reasoning Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Chenrui Cao, Liangcheng Song, Zenan Li, Xinyi Le, Xian Zhang, Hui Xue, Fan Yang

**分类**: cs.AI

**发布日期**: 2025-06-13

**备注**: 31 pages. Associated code and results are available at https://github.com/microsoft/DSP-Plus

---

## 💡 一句话要点

**提出DSP+以提升自动定理证明的效率与准确性**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱五：交互与反应 (Interaction & Reaction)**

**关键词**: `自动定理证明` `神经符号协调` `强化学习` `形式化验证` `推理模型`

## 📋 核心要点

1. 现有的自动定理证明方法依赖于大规模的模型训练，面临着训练成本高和效果不稳定的问题。
2. DSP+通过神经符号协调，优化了定理证明的各个阶段，特别是在草拟、草图和证明阶段的处理。
3. 实验结果显示，DSP+在多个问题集上取得了显著的解决率，且无需额外的模型训练，表现出更高的效率。

## 📝 摘要（中文）

近年来，基于强化学习的大规模训练在自动定理证明中取得了显著进展。然而，本研究发现，通过精心设计的神经符号协调，现有推理模型与策略步骤证明器的结合能够在没有任何训练的情况下实现可比的性能。本文提出了DSP+，这是Draft, Sketch, and Prove框架的改进版本，针对每个阶段进行了细粒度的神经符号增强。实验结果表明，DSP+在多个基准测试中表现优异，解决了80.7%、32.8%和644个问题中的24个，且所需预算低于现有技术。此外，DSP+生成的证明模式易于人类专家理解，有助于识别形式化错误。

## 🔬 方法详解

**问题定义**：本研究旨在解决自动定理证明中对大规模模型训练的依赖，现有方法在训练成本和效果上存在不足。

**核心思路**：DSP+通过精细的神经符号协调，优化了定理证明的草拟、草图和证明三个阶段，旨在提高效率和准确性。

**技术框架**：DSP+框架分为三个主要阶段：草拟阶段生成自然语言子目标，草图阶段进行自动形式化，证明阶段结合符号搜索方法与步骤证明器。

**关键创新**：DSP+的核心创新在于无训练的情况下，通过神经符号增强实现了与现有方法的显著性能对比，特别是在草图和证明阶段的集成。

**关键设计**：在草拟阶段，去除了思维标记和人类证明的引用；草图阶段根据预定义规则屏蔽语法错误；证明阶段紧密结合符号搜索方法如Aesop与步骤证明器。

## 📊 实验亮点

DSP+在miniF2F、ProofNet和PutnamBench三个问题集上分别解决了80.7%、32.8%和24个问题，且在不进行任何额外模型训练的情况下，表现出比现有技术更低的预算需求。此外，DSP+成功解决了一个以往未被解决的IMO问题，展示了其强大的实用性。

## 🎯 应用场景

DSP+的研究成果在自动定理证明、形式化验证和人工智能推理等领域具有广泛的应用潜力。其高效的证明生成能力可以为软件验证、数学定理证明等提供支持，未来可能推动相关领域的进一步发展。

## 📄 摘要（原文）

> Recent advancements, such as DeepSeek-Prover-V2-671B and Kimina-Prover-Preview-72B, demonstrate a prevailing trend in leveraging reinforcement learning (RL)-based large-scale training for automated theorem proving. Surprisingly, we discover that even without any training, careful neuro-symbolic coordination of existing off-the-shelf reasoning models and tactic step provers can achieve comparable performance. This paper introduces \textbf{DSP+}, an improved version of the Draft, Sketch, and Prove framework, featuring a \emph{fine-grained and integrated} neuro-symbolic enhancement for each phase: (1) In the draft phase, we prompt reasoning models to generate concise natural-language subgoals to benefit the sketch phase, removing thinking tokens and references to human-written proofs; (2) In the sketch phase, subgoals are autoformalized with hypotheses to benefit the proving phase, and sketch lines containing syntactic errors are masked according to predefined rules; (3) In the proving phase, we tightly integrate symbolic search methods like Aesop with step provers to establish proofs for the sketch subgoals. Experimental results show that, without any additional model training or fine-tuning, DSP+ solves 80.7\%, 32.8\%, and 24 out of 644 problems from miniF2F, ProofNet, and PutnamBench, respectively, while requiring fewer budgets compared to state-of-the-arts. DSP+ proves \texttt{imo\_2019\_p1}, an IMO problem in miniF2F that is not solved by any prior work. Additionally, DSP+ generates proof patterns comprehensible by human experts, facilitating the identification of formalization errors; For example, eight wrongly formalized statements in miniF2F are discovered. Our results highlight the potential of classical reasoning patterns besides the RL-based training. All components will be open-sourced.

