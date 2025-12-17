---
layout: default
title: DISCODE: Distribution-Aware Score Decoder for Robust Automatic Evaluation of Image Captioning
---

# DISCODE: Distribution-Aware Score Decoder for Robust Automatic Evaluation of Image Captioning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.14420" class="toolbar-btn" target="_blank">📄 arXiv: 2512.14420v1</a>
  <a href="https://arxiv.org/pdf/2512.14420.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.14420v1" onclick="toggleFavorite(this, '2512.14420v1', 'DISCODE: Distribution-Aware Score Decoder for Robust Automatic Evaluation of Image Captioning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Nakamasa Inoue, Kanoko Goto, Masanari Oi, Martyna Gruszka, Mahiro Ukai, Takumi Hirose, Yusuke Sekikawa

**分类**: cs.CV, cs.AI

**发布日期**: 2025-12-16

**备注**: Paper accepted to AAAI 2026

---

## 💡 一句话要点

**提出DISCODE，一种分布感知的分数解码器，用于提升图像描述自动评估的鲁棒性。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `图像描述评估` `领域自适应` `视觉-语言模型` `鲁棒性` `无参考评估`

## 📋 核心要点

1. 现有LVLMs在图像描述评估中，领域偏移会导致性能下降，缺乏鲁棒性。
2. DISCODE通过引入自适应测试时损失(ATT)，利用高斯先验提高评估分数估计的鲁棒性。
3. 实验表明，DISCODE在MCEval等多个基准测试中，作为无参考指标，达到了SOTA性能。

## 📝 摘要（中文）

大型视觉-语言模型(LVLMs)在广泛的多模态任务中表现出令人印象深刻的性能。然而，使用LVLMs进行鲁棒的图像描述评估仍然具有挑战性，尤其是在领域偏移的情况下。为了解决这个问题，我们引入了分布感知的分数解码器(DISCODE)，这是一种新颖的无需微调的方法，可以生成与不同领域的人工判断更好地对齐的鲁棒评估分数。DISCODE背后的核心思想在于其测试时自适应评估方法，该方法引入了自适应测试时(ATT)损失，利用高斯先验分布来提高评估分数估计的鲁棒性。这种损失可以在测试时使用我们推导出的解析解有效地最小化。此外，我们还引入了多领域描述评估(MCEval)基准，这是一个新的图像描述评估基准，涵盖六个不同的领域，旨在评估评估指标的鲁棒性。在我们的实验中，我们证明了DISCODE在MCEval和四个具有代表性的现有基准上，作为一种无参考评估指标，实现了最先进的性能。

## 🔬 方法详解

**问题定义**：论文旨在解决图像描述自动评估在领域偏移下鲁棒性不足的问题。现有方法在面对不同领域的数据时，评估结果与人类判断的一致性较差，无法准确反映图像描述的质量。

**核心思路**：DISCODE的核心思路是在测试时进行自适应调整，通过引入一个基于高斯先验的损失函数，使评估分数能够更好地适应当前领域的分布。这种方法无需额外的微调，即可提高评估的鲁棒性。

**技术框架**：DISCODE主要包含以下几个关键部分：1) 使用LVLM提取图像和描述的特征；2) 定义一个评估分数解码器，将特征映射到评估分数；3) 引入自适应测试时损失(ATT)，该损失基于高斯先验，用于在测试时调整解码器的参数；4) 使用推导出的解析解最小化ATT损失，从而得到更鲁棒的评估分数。

**关键创新**：DISCODE的关键创新在于其自适应测试时评估方法和ATT损失的设计。与传统的固定评估方法不同，DISCODE能够根据当前领域的特征分布动态调整评估策略，从而提高鲁棒性。ATT损失利用高斯先验，鼓励评估分数接近一个合理的分布，避免出现极端值。

**关键设计**：ATT损失的关键设计在于高斯先验的选择和损失函数的具体形式。论文选择高斯分布作为先验，并推导出了损失函数的解析解，使得在测试时可以高效地进行优化。此外，论文还提出了MCEval基准，用于评估评估指标在不同领域的鲁棒性。

## 📊 实验亮点

DISCODE在MCEval和四个现有基准测试中均取得了SOTA性能，证明了其在领域偏移下的鲁棒性。尤其是在MCEval基准上，DISCODE显著优于其他无参考评估指标，表明其在多领域环境下的优越性。此外，DISCODE无需微调，降低了应用成本。

## 🎯 应用场景

DISCODE可应用于各种需要自动评估图像描述质量的场景，例如图像搜索引擎、视觉问答系统、图像编辑工具等。该研究有助于提高人机交互的自然性和准确性，并为开发更智能的视觉-语言系统提供支持。未来，该方法可以扩展到其他多模态任务的评估中。

## 📄 摘要（原文）

> Large vision-language models (LVLMs) have shown impressive performance across a broad range of multimodal tasks. However, robust image caption evaluation using LVLMs remains challenging, particularly under domain-shift scenarios. To address this issue, we introduce the Distribution-Aware Score Decoder (DISCODE), a novel finetuning-free method that generates robust evaluation scores better aligned with human judgments across diverse domains. The core idea behind DISCODE lies in its test-time adaptive evaluation approach, which introduces the Adaptive Test-Time (ATT) loss, leveraging a Gaussian prior distribution to improve robustness in evaluation score estimation. This loss is efficiently minimized at test time using an analytical solution that we derive. Furthermore, we introduce the Multi-domain Caption Evaluation (MCEval) benchmark, a new image captioning evaluation benchmark covering six distinct domains, designed to assess the robustness of evaluation metrics. In our experiments, we demonstrate that DISCODE achieves state-of-the-art performance as a reference-free evaluation metric across MCEval and four representative existing benchmarks.

