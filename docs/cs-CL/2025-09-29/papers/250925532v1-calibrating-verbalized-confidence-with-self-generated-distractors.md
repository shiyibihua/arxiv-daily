---
layout: default
title: Calibrating Verbalized Confidence with Self-Generated Distractors
---

# Calibrating Verbalized Confidence with Self-Generated Distractors

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.25532" class="toolbar-btn" target="_blank">📄 arXiv: 2509.25532v1</a>
  <a href="https://arxiv.org/pdf/2509.25532.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.25532v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.25532v1', 'Calibrating Verbalized Confidence with Self-Generated Distractors')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Victor Wang, Elias Stengel-Eskin

**分类**: cs.CL, cs.AI

**发布日期**: 2025-09-29

**备注**: Code: https://github.com/dubai03nsr/dinco

---

## 💡 一句话要点

**提出DINCO，通过自生成干扰项校准LLM的置信度，提升可靠性。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `置信度校准` `自生成干扰项` `暗示性偏差` `一致性评估`

## 📋 核心要点

1. 现有LLM的置信度表达存在校准不佳的问题，尤其是在低准确率情况下表现出过度自信，影响用户信任。
2. 论文提出Distractor-Normalized Coherence (DINCO)方法，通过自生成干扰项来估计和校正LLM的暗示性偏差。
3. 实验结果表明，DINCO能提供更可靠的置信度估计，且在较少推理次数下优于自洽性方法。

## 📝 摘要（中文）

校准的置信度估计对于人类用户信任大型语言模型（LLM）的输出至关重要。尽管LLM可以用人类可解释的方式表达其置信度，但经验表明，LLM生成的置信度分数校准不佳，在低准确率的实例上报告高置信度，从而损害信任和安全性。我们假设这种过度自信通常源于LLM在面对它编码信息较少的声明时，易受暗示的影响；我们通过实验验证了这一假设，发现LLM在较低准确率的声明上更容易受到暗示。基于这一发现，我们引入了干扰项归一化一致性（DINCO），它通过让模型独立地在几个自生成的干扰项（即替代声明）上表达其置信度，并按总置信度进行归一化，来估计和解释LLM的暗示性偏差。为了进一步提高校准，我们利用生成器-验证器不一致性，用基于一致性的生成器置信度估计来增强归一化的验证器置信度。在这里，我们将流行的自洽方法视为利用跨采样生成的一致性，并将归一化的口头置信度视为利用跨不兼容声明的验证的一致性，从而使我们能够将这些互补的一致性维度集成到DINCO中。此外，我们的分析表明，DINCO提供了不太饱和——因此更可用——的置信度估计，并且进一步的采样本身无法缩小DINCO和基线之间的差距，DINCO在10次推理调用中优于100次的自洽性。

## 🔬 方法详解

**问题定义**：现有大型语言模型（LLM）在生成文本的同时，也能够输出置信度评估，但这些置信度往往与实际准确率不匹配，尤其是在模型对某些问题了解较少时，容易受到暗示而给出过高的置信度。这种置信度校准问题降低了LLM输出的可信度，限制了其在安全敏感场景中的应用。

**核心思路**：论文的核心思路是通过引入“干扰项”来评估LLM的“暗示性”，即模型在面对不确定信息时，是否容易受到误导而给出高置信度。通过让模型对多个自生成的干扰项进行置信度评估，并进行归一化，从而消除模型固有的暗示性偏差。

**技术框架**：DINCO方法包含以下几个主要步骤：1) **生成干扰项**：针对给定的问题，LLM生成多个不同的、甚至相互矛盾的答案（干扰项）。2) **置信度评估**：LLM对原始答案和所有干扰项分别进行置信度评估，得到一系列置信度分数。3) **归一化处理**：将原始答案的置信度除以所有答案（包括原始答案和干扰项）的置信度之和，得到归一化后的置信度。4) **生成器-验证器一致性**：结合生成器和验证器之间的不一致性，进一步校准置信度。

**关键创新**：DINCO的关键创新在于：1) **利用自生成干扰项评估暗示性偏差**：通过让模型对多个不同的答案进行评估，从而量化模型对不确定信息的敏感程度。2) **归一化处理消除偏差**：通过归一化处理，降低模型在不确定情况下给出高置信度的可能性，从而提高置信度校准的准确性。3) **整合生成器-验证器不一致性**：将生成器和验证器的信息结合起来，进一步提高置信度评估的可靠性。

**关键设计**：论文中，干扰项的数量是一个重要的参数，需要根据具体任务进行调整。此外，生成器-验证器一致性的具体实现方式也会影响最终的性能。论文中使用了常见的自洽性方法作为生成器一致性的度量，并将其与归一化的验证器置信度相结合。

## 📊 实验亮点

实验结果表明，DINCO方法能够显著提高LLM置信度校准的准确性，尤其是在模型对某些问题了解较少的情况下。DINCO在仅使用10次推理调用时，性能就超过了使用100次推理调用的自洽性方法，表明DINCO具有更高的效率。此外，DINCO提供的置信度估计更加可靠，不易饱和，更易于用户理解和使用。

## 🎯 应用场景

该研究成果可应用于各种需要LLM提供可靠置信度评估的场景，例如医疗诊断、金融风险评估、法律咨询等。通过提高LLM置信度校准的准确性，可以增强用户对LLM输出的信任，并降低因错误信息导致的风险。未来，该方法可以进一步扩展到其他类型的模型和任务中。

## 📄 摘要（原文）

> Calibrated confidence estimates are necessary for large language model (LLM) outputs to be trusted by human users. While LLMs can express their confidence in human-interpretable ways, verbalized LLM-generated confidence scores have empirically been found to be miscalibrated, reporting high confidence on instances with low accuracy and thereby harming trust and safety. We hypothesize that this overconfidence often stems from a given LLM's heightened suggestibility when faced with claims that it encodes little information about; we empirically validate this hypothesis, finding more suggestibility on lower-accuracy claims. Building on this finding, we introduce Distractor-Normalized Coherence (DINCO), which estimates and accounts for an LLM's suggestibility bias by having the model verbalize its confidence independently across several self-generated distractors (i.e. alternative claims), and normalizes by the total verbalized confidence. To further improve calibration, we leverage generator-validator disagreement, augmenting normalized validator confidence with a consistency-based estimate of generator confidence. Here, we frame the popular approach of self-consistency as leveraging coherence across sampled generations, and normalized verbalized confidence as leveraging coherence across validations on incompatible claims, allowing us to integrate these complementary dimensions of coherence into DINCO. Moreover, our analysis shows that DINCO provides less saturated -- and therefore more usable -- confidence estimates, and that further sampling alone cannot close the gap between DINCO and baselines, with DINCO at 10 inference calls outperforming self-consistency at 100.

