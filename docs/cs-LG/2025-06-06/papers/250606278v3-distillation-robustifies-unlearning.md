---
layout: default
title: Distillation Robustifies Unlearning
---

# Distillation Robustifies Unlearning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.06278" class="toolbar-btn" target="_blank">📄 arXiv: 2506.06278v3</a>
  <a href="https://arxiv.org/pdf/2506.06278.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.06278v3" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.06278v3', 'Distillation Robustifies Unlearning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Bruce W. Lee, Addie Foote, Alex Infanger, Leni Shor, Harish Kamath, Jacob Goldman-Wetzler, Bryce Woodworth, Alex Cloud, Alexander Matt Turner

**分类**: cs.LG, cs.AI

**发布日期**: 2025-06-06 (更新: 2025-10-24)

**备注**: NeurIPS 2025 (Spotlight)

---

## 💡 一句话要点

**提出UNDO方法以增强大规模模型的去学习鲁棒性**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `去学习` `鲁棒性` `蒸馏训练` `大规模语言模型` `合成任务` `噪声处理` `模型安全性`

## 📋 核心要点

1. 现有的大规模语言模型去学习方法在鲁棒性方面存在不足，容易受到微调的影响而失效。
2. 本文提出的UNDO方法通过蒸馏未学习模型的输出，生成带噪声的副本，从而增强去学习的鲁棒性。
3. 实验结果表明，UNDO在合成语言和算术任务上表现出色，显著降低了计算成本，同时保持了高鲁棒性。

## 📝 摘要（中文）

当前的大规模语言模型去学习方法缺乏鲁棒性，几步微调就可能逆转其效果。本文展示了即使在理想化的去学习形式下，训练模型也能显著改变其输入输出行为。我们提出了一种新的方法——Unlearn-Noise-Distill-on-Outputs（UNDO），该方法通过蒸馏未学习模型的输出，生成一个带噪声的副本，从而增强去学习的鲁棒性。UNDO在合成语言和算术任务上建立了新的帕累托前沿，能够在计算成本和鲁棒性之间进行可调的权衡，且在最强设置下，使用60-80%的计算资源和0.01%的预训练数据标记，达到了与完美数据过滤下从头再训练模型相当的鲁棒性。

## 🔬 方法详解

**问题定义**：本文旨在解决当前大规模语言模型去学习方法的鲁棒性不足问题，现有方法在微调后容易失效，无法有效去除不必要的信息。

**核心思路**：论文的核心思路是通过蒸馏技术，将未学习模型的输出转移到一个随机初始化的学生模型上，从而在保留潜在能力的同时增强去学习的鲁棒性。

**技术框架**：整体架构包括三个主要阶段：首先，训练一个未学习模型；其次，使用该模型的输出训练一个随机初始化的学生模型；最后，通过引入噪声来生成一个鲁棒的副本。

**关键创新**：最重要的技术创新在于提出了UNDO方法，该方法通过蒸馏和噪声引入的结合，显著提高了去学习的鲁棒性，与现有方法相比，提供了新的解决方案。

**关键设计**：在设计中，UNDO方法引入了可调的参数，以平衡计算成本和鲁棒性，损失函数的设计也考虑了输出的噪声处理，确保了模型在不同设置下的性能表现。

## 📊 实验亮点

实验结果显示，UNDO方法在合成语言和算术任务上达到了新的帕累托前沿。在最强设置下，UNDO的鲁棒性与完美数据过滤下从头再训练的模型相当，同时仅使用60-80%的计算资源和0.01%的预训练数据标记，展现了显著的性能提升。

## 🎯 应用场景

该研究的潜在应用领域包括需要去除特定信息的大规模语言模型，如法律、医疗和金融等领域。通过增强去学习的鲁棒性，UNDO方法为模型的安全性和合规性提供了新的解决方案，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> Current LLM unlearning methods are not robust. A few steps of finetuning can revert their effects. We begin by showing that this is true even for an idealized form of unlearning: training to imitate a model that was never trained on unwanted information. This shows that training a model can drastically modify its input-output behavior while leaving its underlying capabilities intact. In light of this dynamic, we show our main result. Training a randomly initialized student on the outputs of an unlearned model transfers behaviors while leaving latent capabilities behind. In short, distillation robustifies unlearning. Based on this result, we propose Unlearn-Noise-Distill-on-Outputs (UNDO), a scalable method that distills an unlearned model into a noised copy of itself. UNDO introduces a tunable tradeoff between compute cost and robustness, establishing a new Pareto frontier on synthetic language and arithmetic tasks. At its strongest setting, UNDO matches the robustness of a model retrained from scratch with perfect data filtering while using only 60-80% of the compute and requiring only 0.01% of the pretraining data to be labeled. We also show that UNDO robustifies unlearning on the more realistic Weapons of Mass Destruction Proxy (WMDP) benchmark. Since distillation is widely used in practice, incorporating an unlearning step beforehand offers a convenient path to robust capability removal.

