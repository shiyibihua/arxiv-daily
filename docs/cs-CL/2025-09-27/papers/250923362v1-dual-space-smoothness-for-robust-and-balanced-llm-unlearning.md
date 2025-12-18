---
layout: default
title: Dual-Space Smoothness for Robust and Balanced LLM Unlearning
---

# Dual-Space Smoothness for Robust and Balanced LLM Unlearning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.23362" class="toolbar-btn" target="_blank">📄 arXiv: 2509.23362v1</a>
  <a href="https://arxiv.org/pdf/2509.23362.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.23362v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.23362v1', 'Dual-Space Smoothness for Robust and Balanced LLM Unlearning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Han Yan, Zheyuan Liu, Meng Jiang

**分类**: cs.CL, cs.AI

**发布日期**: 2025-09-27

**备注**: A unified framework that enforces dual-space smoothness in representation and parameter spaces to improve robustness and balance unlearning metrics

---

## 💡 一句话要点

**PRISM：通过双空间平滑实现鲁棒且均衡的LLM不可学习**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `机器不可学习` `隐私保护` `鲁棒性` `双空间平滑`

## 📋 核心要点

1. 现有LLM不可学习方法面临灾难性遗忘和指标不平衡问题，难以兼顾有效性、效用保持和隐私保护。
2. PRISM框架通过在表示空间和参数空间中实施双空间平滑，提高模型鲁棒性，平衡不可学习的各项指标。
3. 实验表明，PRISM在多种攻击下优于现有方法，并在关键指标之间取得了更好的平衡。

## 📝 摘要（中文）

随着大型语言模型的快速发展，机器不可学习技术应运而生，以解决用户隐私、版权侵犯和整体安全性等日益增长的问题。然而，目前最先进的不可学习方法通常会遭受灾难性遗忘和指标不平衡的困扰，例如，以牺牲其他目标（如不可学习有效性、效用保持或隐私保护）为代价过度优化一个目标。此外，表示或参数空间中的微小扰动可能被重新学习和越狱攻击利用。为了应对这些挑战，我们提出了PRISM，一个统一的框架，它在表示和参数空间中强制执行双空间平滑，以提高鲁棒性并平衡不可学习指标。PRISM包含两个平滑优化阶段：（i）表示空间阶段，该阶段采用经过鲁棒训练的探针来防御越狱攻击，以及（ii）参数空间阶段，该阶段解耦保留-遗忘梯度冲突，减少不平衡，并平滑参数空间以减轻重新学习攻击。在WMDP和MUSE上，跨越对话和连续文本设置的大量实验表明，PRISM在多种攻击下优于SOTA基线，同时在关键指标之间实现了更好的平衡。

## 🔬 方法详解

**问题定义**：现有的大型语言模型不可学习方法，在尝试删除特定信息时，容易导致灾难性遗忘，即模型忘记了大量有用的知识。此外，这些方法往往在不可学习有效性、效用保持和隐私保护等指标上表现不平衡，过度优化一个指标而牺牲其他指标。同时，模型容易受到重新学习攻击和越狱攻击，鲁棒性不足。

**核心思路**：PRISM的核心思路是通过在表示空间和参数空间中引入平滑性约束，来提高模型的鲁棒性和平衡性。表示空间平滑旨在防御越狱攻击，参数空间平滑旨在减轻重新学习攻击，并解耦retain-forget梯度冲突，从而减少指标不平衡。

**技术框架**：PRISM框架包含两个主要的优化阶段：1) 表示空间平滑阶段：利用一个经过鲁棒训练的探针网络，对模型的表示空间进行平滑，以防御越狱攻击。2) 参数空间平滑阶段：通过解耦retain-forget梯度，减少指标不平衡，并对参数空间进行平滑，以减轻重新学习攻击。这两个阶段共同作用，实现鲁棒且均衡的不可学习。

**关键创新**：PRISM的关键创新在于提出了双空间平滑的概念，并将其应用于LLM的不可学习任务中。通过在表示空间和参数空间同时进行平滑，可以有效地提高模型的鲁棒性和平衡性，从而克服了现有方法的局限性。

**关键设计**：在表示空间平滑阶段，使用对抗训练来训练探针网络，使其对输入扰动具有鲁棒性。在参数空间平滑阶段，设计了一种新的损失函数，用于解耦retain-forget梯度，并引入正则化项来平滑参数空间。具体的参数设置和损失函数形式在论文中有详细描述，但此处未知。

## 📊 实验亮点

PRISM在WMDP和MUSE数据集上进行了广泛的实验，结果表明，PRISM在多种攻击下优于SOTA基线。具体来说，PRISM在不可学习有效性、效用保持和隐私保护等指标上都取得了显著的提升，并且在这些指标之间实现了更好的平衡。具体的性能数据和提升幅度未知，需要查阅论文原文。

## 🎯 应用场景

PRISM框架可应用于各种需要保护用户隐私、版权和模型安全的场景，例如：在线教育、智能客服、金融风控等。通过该技术，可以安全地删除模型中的敏感信息，防止模型被用于非法目的，并提高模型的可靠性和可信度。未来，该技术有望成为LLM安全领域的重要组成部分。

## 📄 摘要（原文）

> With the rapid advancement of large language models, Machine Unlearning has emerged to address growing concerns around user privacy, copyright infringement, and overall safety. Yet state-of-the-art (SOTA) unlearning methods often suffer from catastrophic forgetting and metric imbalance, for example by over-optimizing one objective (e.g., unlearning effectiveness, utility preservation, or privacy protection) at the expense of others. In addition, small perturbations in the representation or parameter space can be exploited by relearn and jailbreak attacks. To address these challenges, we propose PRISM, a unified framework that enforces dual-space smoothness in representation and parameter spaces to improve robustness and balance unlearning metrics. PRISM consists of two smoothness optimization stages: (i) a representation space stage that employs a robustly trained probe to defend against jailbreak attacks, and (ii) a parameter-space stage that decouples retain-forget gradient conflicts, reduces imbalance, and smooths the parameter space to mitigate relearning attacks. Extensive experiments on WMDP and MUSE, across conversational-dialogue and continuous-text settings, show that PRISM outperforms SOTA baselines under multiple attacks while achieving a better balance among key metrics.

