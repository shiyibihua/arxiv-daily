---
layout: default
title: Distillation of Large Language Models via Concrete Score Matching
---

# Distillation of Large Language Models via Concrete Score Matching

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.25837" class="toolbar-btn" target="_blank">📄 arXiv: 2509.25837v1</a>
  <a href="https://arxiv.org/pdf/2509.25837.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.25837v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.25837v1', 'Distillation of Large Language Models via Concrete Score Matching')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yeongmin Kim, Donghyeok Shin, Mina Kang, Byeonghu Na, Il-Chul Moon

**分类**: cs.LG, cs.AI

**发布日期**: 2025-09-30

---

## 💡 一句话要点

**提出Concrete Score Distillation，解决LLM蒸馏中logit信息损失和解空间限制问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `知识蒸馏` `大型语言模型` `Concrete Score Matching` `模型压缩` `logit蒸馏`

## 📋 核心要点

1. 现有知识蒸馏方法依赖softmax概率匹配，损失了logit中的丰富信息，限制了模型性能。
2. Concrete Score Distillation (CSD)通过离散分数匹配，对齐学生和教师模型间的相对logit差异。
3. 实验表明，CSD在多个LLM上优于现有KD方法，实现了更好的保真度和多样性平衡，并可与on-policy方法结合。

## 📝 摘要（中文）

大型语言模型(LLMs)性能卓越但部署成本高昂，因此知识蒸馏(KD)对于高效推理至关重要。现有的KD目标通常通过softmax匹配学生和教师的概率，这模糊了宝贵的logit信息。直接logit蒸馏(DLD)虽然缓解了softmax平滑，但未能考虑logit移位不变性，从而限制了解空间。我们提出Concrete Score Distillation (CSD)，这是一种离散的分数匹配目标，克服了softmax引起的平滑以及对最优解集的限制。我们解决了自回归LLM中离散分数匹配的训练不稳定性和二次复杂度问题，由此产生的CSD目标以灵活的权重对齐学生和教师之间所有词汇对的相对logit差异。我们在任务无关的指令跟随和使用GPT-2-1.5B、OpenLLaMA-7B和GEMMA-7B-IT的任务特定蒸馏上评估CSD。实验表明，CSD始终优于最近的KD目标，实现了良好的保真度-多样性权衡，并且在与on-policy技术结合使用时产生互补的增益，证明了其LLM蒸馏的可扩展性和有效性。

## 🔬 方法详解

**问题定义**：现有的大型语言模型知识蒸馏方法，如基于softmax的概率匹配，会模糊logit中包含的丰富信息，导致学生模型无法充分学习教师模型的知识。直接logit蒸馏(DLD)虽然尝试直接匹配logit，但忽略了logit移位不变性，限制了最优解空间，影响了蒸馏效果。

**核心思路**：论文的核心思路是利用离散分数匹配(Concrete Score Matching)来对齐学生模型和教师模型之间的相对logit差异。通过直接对齐logit的相对关系，避免了softmax带来的信息损失，同时考虑了logit移位不变性，从而扩大了最优解空间，使得学生模型能够更好地学习教师模型的知识。

**技术框架**：CSD方法主要包含以下几个步骤：首先，计算教师模型和学生模型在相同输入下的logit输出。然后，利用Concrete Score Matching方法，计算学生模型和教师模型之间logit的相对差异。最后，通过优化一个损失函数，使得学生模型的logit相对差异尽可能接近教师模型的logit相对差异。该框架可以灵活地调整不同词汇对之间的权重，从而实现mode-seeking和mode-covering两种不同的蒸馏策略。

**关键创新**：该论文的关键创新在于提出了Concrete Score Distillation (CSD)方法，这是一种基于离散分数匹配的知识蒸馏方法。与传统的基于softmax的概率匹配方法相比，CSD能够更好地保留logit中的信息，并且考虑了logit移位不变性，从而扩大了最优解空间。此外，论文还解决了自回归LLM中离散分数匹配的训练不稳定性和二次复杂度问题。

**关键设计**：CSD的关键设计包括：1) 使用Concrete分布来近似离散分布，从而实现可微的优化；2) 设计了一种损失函数，用于衡量学生模型和教师模型之间logit相对差异的相似度；3) 采用灵活的权重机制，可以根据不同的任务和需求，调整不同词汇对之间的权重，实现mode-seeking和mode-covering两种不同的蒸馏策略。论文还提出了解决训练不稳定性和二次复杂度问题的具体方法，例如使用梯度裁剪和稀疏化技术。

## 📊 实验亮点

实验结果表明，CSD方法在任务无关的指令跟随和任务特定的蒸馏任务上，均优于现有的知识蒸馏方法。例如，在使用GPT-2-1.5B、OpenLLaMA-7B和GEMMA-7B-IT进行蒸馏时，CSD能够显著提升学生模型的性能，并且实现了更好的保真度-多样性权衡。此外，CSD还可以与on-policy技术结合使用，进一步提升模型性能。

## 🎯 应用场景

该研究成果可广泛应用于大型语言模型的压缩和加速，降低部署成本，提升推理效率。例如，可以将大型预训练模型蒸馏成更小的模型，部署在移动设备或边缘计算平台上，实现本地化的智能服务。此外，该方法还可以用于个性化模型的训练，根据用户的特定需求，定制化训练小型语言模型。

## 📄 摘要（原文）

> Large language models (LLMs) deliver remarkable performance but are costly to deploy, motivating knowledge distillation (KD) for efficient inference. Existing KD objectives typically match student and teacher probabilities via softmax, which blurs valuable logit information. While direct logit distillation (DLD) mitigates softmax smoothing, it fails to account for logit shift invariance, thereby restricting the solution space. We propose Concrete Score Distillation (CSD), a discrete score-matching objective that overcomes both softmax-induced smoothing and restrictions on the optimal solution set. We resolve the training instability and quadratic complexity of discrete score-matching in autoregressive LLMs, and the resulting CSD objective aligns relative logit differences across all vocabulary pairs between student and teacher with flexible weighting. We provide both mode-seeking and mode-covering instances within our framework and evaluate CSD on task-agnostic instruction-following and task-specific distillation using GPT-2-1.5B, OpenLLaMA-7B, and GEMMA-7B-IT. Experiments show that CSD consistently surpasses recent KD objectives, achieves favorable fidelity-diversity trade-offs, and yields complementary gains when combined with on-policy techniques, demonstrating its scalability and effectiveness for LLM distillation.

