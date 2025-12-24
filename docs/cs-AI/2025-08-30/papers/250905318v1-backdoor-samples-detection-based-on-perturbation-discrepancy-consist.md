---
layout: default
title: Backdoor Samples Detection Based on Perturbation Discrepancy Consistency in Pre-trained Language Models
---

# Backdoor Samples Detection Based on Perturbation Discrepancy Consistency in Pre-trained Language Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.05318" class="toolbar-btn" target="_blank">📄 arXiv: 2509.05318v1</a>
  <a href="https://arxiv.org/pdf/2509.05318.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.05318v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.05318v1', 'Backdoor Samples Detection Based on Perturbation Discrepancy Consistency in Pre-trained Language Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zuquan Peng, Jianming Fu, Lixin Zou, Li Zheng, Yanzhen Ren, Guojun Peng

**分类**: cs.CR, cs.AI

**发布日期**: 2025-08-30

**备注**: 13 pages, 9 figures, 8 tables, journal

**期刊**: Neural Networks 193(2026) 108025

**DOI**: [10.1016/j.neunet.2025.108025](https://doi.org/10.1016/j.neunet.2025.108025)

---

## 💡 一句话要点

**提出基于扰动差异一致性的后门样本检测方法**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `后门攻击` `样本检测` `预训练模型` `扰动一致性` `网络安全` `机器学习` `对抗性样本`

## 📋 核心要点

1. 现有的后门样本检测方法通常需要访问被污染的模型或额外的干净样本，限制了其实用性。
2. 本文提出了一种新颖的后门样本检测方法，基于扰动差异的一致性评估，能够在预训练和后训练阶段使用。
3. 在四种典型的后门攻击和五种大型语言模型后门攻击的实验中，所提方法表现优于现有的零样本黑盒检测方法。

## 📝 摘要（中文）

随着未经过审查的第三方和互联网数据的使用，预训练模型变得容易受到后门攻击。检测后门样本对于防止推理期间的后门激活或训练期间的注入至关重要。然而，现有检测方法通常要求防御者访问被污染的模型、额外的干净样本或显著的计算资源，这限制了其实用性。为了解决这一限制，本文提出了一种基于扰动差异一致性评估的后门样本检测方法（NETE），该方法可在预训练和后训练阶段使用。在检测过程中，仅需一个现成的预训练模型来计算样本的对数概率，并基于掩码填充策略生成扰动。我们的研究基于一个有趣的现象：后门样本的扰动差异变化小于干净样本。通过使用曲率来测量不同扰动样本与输入样本之间的对数概率差异，从而评估扰动差异的一致性，以确定输入样本是否为后门样本。实验结果表明，我们的检测策略优于现有的零样本黑盒检测方法。

## 🔬 方法详解

**问题定义**：本文旨在解决后门样本检测中的实用性问题，现有方法往往依赖于对被污染模型的访问或额外的干净样本，导致检测过程复杂且资源消耗大。

**核心思路**：提出的NETE方法利用扰动差异的一致性现象，认为后门样本的扰动差异变化小于干净样本，从而通过计算对数概率的曲率来进行检测。

**技术框架**：整体流程包括使用现成的预训练模型计算样本的对数概率，应用掩码填充策略生成扰动，并通过评估扰动差异的一致性来判断样本是否为后门样本。

**关键创新**：最重要的创新点在于提出了基于扰动差异一致性的检测方法，显著降低了对额外资源的依赖，与现有方法相比，具有更高的灵活性和适用性。

**关键设计**：在技术细节上，采用了曲率作为测量标准，并设计了自动化的扰动生成函数，确保检测过程的高效性和准确性。通过这些设计，方法能够在多种攻击场景下保持良好的检测性能。

## 📊 实验亮点

实验结果显示，所提方法在四种典型后门攻击和五种大型语言模型后门攻击中均表现优异，相较于现有的零样本黑盒检测方法，检测准确率提升显著，验证了方法的有效性和实用性。

## 🎯 应用场景

该研究的潜在应用领域包括网络安全、机器学习模型的安全性评估以及对抗性样本检测等。通过有效识别后门样本，可以提升模型的安全性，防止潜在的攻击，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> The use of unvetted third-party and internet data renders pre-trained models susceptible to backdoor attacks. Detecting backdoor samples is critical to prevent backdoor activation during inference or injection during training. However, existing detection methods often require the defender to have access to the poisoned models, extra clean samples, or significant computational resources to detect backdoor samples, limiting their practicality. To address this limitation, we propose a backdoor sample detection method based on perturbatio\textbf{N} discr\textbf{E}pancy consis\textbf{T}ency \textbf{E}valuation (\NETE). This is a novel detection method that can be used both pre-training and post-training phases. In the detection process, it only requires an off-the-shelf pre-trained model to compute the log probability of samples and an automated function based on a mask-filling strategy to generate perturbations. Our method is based on the interesting phenomenon that the change in perturbation discrepancy for backdoor samples is smaller than that for clean samples. Based on this phenomenon, we use curvature to measure the discrepancy in log probabilities between different perturbed samples and input samples, thereby evaluating the consistency of the perturbation discrepancy to determine whether the input sample is a backdoor sample. Experiments conducted on four typical backdoor attacks and five types of large language model backdoor attacks demonstrate that our detection strategy outperforms existing zero-shot black-box detection methods.

