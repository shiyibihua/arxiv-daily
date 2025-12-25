---
layout: default
title: "MiST: Understanding the Role of Mid-Stage Scientific Training in Developing Chemical Reasoning Models"
---

# MiST: Understanding the Role of Mid-Stage Scientific Training in Developing Chemical Reasoning Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.21231" class="toolbar-btn" target="_blank">📄 arXiv: 2512.21231v1</a>
  <a href="https://arxiv.org/pdf/2512.21231.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.21231v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.21231v1', 'MiST: Understanding the Role of Mid-Stage Scientific Training in Developing Chemical Reasoning Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Andres M Bran, Tong Xie, Shai Pranesh, Jeffrey Meng, Xuan Vu Nguyen, Jeremy Goumaz, David Ming Segura, Ruizhi Xu, Dongzhan Zhou, Wenjie Zhang, Bram Hoex, Philippe Schwaller

**分类**: cs.LG, cond-mat.mtrl-sci

**发布日期**: 2025-12-24

---

## 💡 一句话要点

**提出MiST，通过中阶段科学训练提升化学推理模型性能**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `化学推理` `大型语言模型` `中阶段训练` `强化学习` `潜在可解性`

## 📋 核心要点

1. 现有方法在利用强化学习提升化学推理能力时，受限于模型自身的“潜在可解性”，即模型需具备初步的正确答案预测能力。
2. 论文提出中阶段科学训练（MiST），通过数据混合、持续预训练和监督微调等技术，增强模型的符号能力和潜在化学知识。
3. 实验表明，MiST能显著提升模型在有机反应命名和无机材料生成等任务上的准确率，并生成可解释的推理过程。

## 📝 摘要（中文）

大型语言模型可以通过基于规则奖励的在线微调来发展推理能力。然而，最近的研究表明一个关键约束：强化学习只有在基础模型已经为正确答案分配了不可忽略的概率时才能成功——我们称之为“潜在可解性”。本文研究了化学推理能力的出现，以及这些先决条件对化学的意义。我们确定了基于强化学习的化学推理的两个必要条件：1) 符号能力，2) 潜在的化学知识。我们提出了中阶段科学训练（MiST）：一套满足这些条件的中阶段训练技术，包括使用SMILES/CIF感知预处理的数据混合、在29亿tokens上的持续预训练以及在10亿tokens上的监督微调。这些步骤将3B和7B模型的潜在可解性得分提高了高达1.8倍，并使强化学习能够将有机反应命名上的top-1准确率从10.9%提高到63.9%，并将无机材料生成上的top-1准确率从40.6%提高到67.4%。在其他具有挑战性的化学任务中也观察到了类似的结果，同时产生了可解释的推理轨迹。我们的结果定义了化学推理训练的明确先决条件，并强调了中阶段训练在解锁推理能力方面的更广泛作用。

## 🔬 方法详解

**问题定义**：现有的大型语言模型在化学推理任务中表现出潜力，但直接使用强化学习进行微调往往效果不佳。一个关键问题是，强化学习的成功依赖于模型本身是否具备“潜在可解性”，即模型在训练前已经对正确答案有一定的概率预测。如果模型缺乏必要的化学知识和符号处理能力，强化学习很难有效提升其推理能力。

**核心思路**：论文的核心思路是通过中阶段科学训练（MiST）来增强模型的“潜在可解性”。MiST旨在使模型具备进行有效化学推理所需的两个关键要素：符号能力和潜在的化学知识。通过精心设计的中阶段训练，提升模型对化学结构和反应的理解，从而为后续的强化学习奠定坚实的基础。

**技术框架**：MiST框架主要包含以下几个阶段：
1. **数据混合与预处理**：将包含SMILES和CIF格式的化学数据与通用文本数据混合，并进行SMILES/CIF感知的预处理，以增强模型对化学结构的理解。
2. **持续预训练**：在29亿个tokens上进行持续预训练，进一步提升模型对化学领域知识的掌握。
3. **监督微调**：在10亿个tokens上进行监督微调，使模型能够更好地完成特定的化学任务。
4. **强化学习（可选）**：在MiST的基础上，可以使用强化学习进一步提升模型的性能。

**关键创新**：该论文的关键创新在于提出了“中阶段科学训练”（MiST）的概念，并将其应用于化学推理模型的训练。与传统的预训练+微调方法不同，MiST强调在预训练和最终任务微调之间进行有针对性的训练，以弥补模型在化学领域知识和符号处理能力方面的不足。这种中阶段训练能够显著提升模型的“潜在可解性”，从而为后续的强化学习奠定基础。

**关键设计**：
* **数据混合比例**：需要仔细调整化学数据和通用文本数据的混合比例，以避免模型过度拟合化学领域知识，同时保持其通用语言能力。
* **SMILES/CIF感知预处理**：针对SMILES和CIF格式的化学数据，需要进行专门的预处理，例如tokenization和数据增强，以提高模型对化学结构的理解。
* **持续预训练目标**：持续预训练的目标可以是masked language modeling或因果语言建模，具体选择取决于模型的架构和任务需求。
* **监督微调损失函数**：监督微调的损失函数通常是交叉熵损失，用于衡量模型预测结果与真实标签之间的差异。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.21231v1/figures/figure1.jpg" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.21231v1/figures/scs_cr.jpg" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.21231v1/figures/scs_prepost.jpg" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

实验结果表明，MiST能够显著提升模型的化学推理能力。在有机反应命名任务中，MiST将top-1准确率从10.9%提升到63.9%，提升幅度高达53%。在无机材料生成任务中，MiST将top-1准确率从40.6%提升到67.4%，提升幅度为26.8%。这些结果表明，MiST是一种有效的化学推理模型训练方法。

## 🎯 应用场景

该研究成果可应用于药物发现、材料设计等领域。通过提升化学推理模型的性能，可以加速新药和新材料的研发过程，降低研发成本。此外，该方法还可以推广到其他科学领域，例如物理学和生物学，以提升相关领域的AI模型性能。

## 📄 摘要（原文）

> Large Language Models can develop reasoning capabilities through online fine-tuning with rule-based rewards. However, recent studies reveal a critical constraint: reinforcement learning succeeds only when the base model already assigns non-negligible probability to correct answers -- a property we term 'latent solvability'. This work investigates the emergence of chemical reasoning capabilities and what these prerequisites mean for chemistry. We identify two necessary conditions for RL-based chemical reasoning: 1) Symbolic competence, and 2) Latent chemical knowledge. We propose mid-stage scientific training (MiST): a set of mid-stage training techniques to satisfy these, including data-mixing with SMILES/CIF-aware pre-processing, continued pre-training on 2.9B tokens, and supervised fine-tuning on 1B tokens. These steps raise the latent-solvability score on 3B and 7B models by up to 1.8x, and enable RL to lift top-1 accuracy from 10.9 to 63.9% on organic reaction naming, and from 40.6 to 67.4% on inorganic material generation. Similar results are observed for other challenging chemical tasks, while producing interpretable reasoning traces. Our results define clear prerequisites for chemical reasoning training and highlight the broader role of mid-stage training in unlocking reasoning capabilities.

