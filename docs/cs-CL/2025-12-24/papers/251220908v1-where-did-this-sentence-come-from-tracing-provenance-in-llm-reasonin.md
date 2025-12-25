---
layout: default
title: Where Did This Sentence Come From? Tracing Provenance in LLM Reasoning Distillation
---

# Where Did This Sentence Come From? Tracing Provenance in LLM Reasoning Distillation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.20908" class="toolbar-btn" target="_blank">📄 arXiv: 2512.20908v1</a>
  <a href="https://arxiv.org/pdf/2512.20908.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.20908v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.20908v1', 'Where Did This Sentence Come From? Tracing Provenance in LLM Reasoning Distillation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Kaiyuan Liu, Shaotian Yan, Rui Miao, Bing Wang, Chen Shen, Jun Zhang, Jieping Ye

**分类**: cs.CL

**发布日期**: 2025-12-24

---

## 💡 一句话要点

**提出跨模型推理蒸馏溯源框架，分析学生模型能力来源并指导数据选择。**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `推理蒸馏` `知识蒸馏` `模型溯源` `模型分析` `数据选择` `自然语言处理` `模型压缩` `模型泛化`

## 📋 核心要点

1. 现有推理蒸馏方法缺乏对学生模型能力来源的细致分析，难以判断学生模型在测试时能否保持与教师模型的一致性。
2. 提出跨模型推理蒸馏溯源框架，通过比较教师、学生和蒸馏模型的预测概率，追踪学生模型行为的来源。
3. 实验表明，蒸馏模型在测试时可以生成源自教师模型的动作，且与性能相关。基于此，提出教师引导的数据选择方法。

## 📝 摘要（中文）

推理蒸馏日益受到关注。它通常利用大型教师模型生成推理路径，然后用于微调学生模型，使其在训练环境中模仿教师的行为。然而，先前的方法缺乏对蒸馏模型能力来源的详细分析。目前尚不清楚学生模型是否能在新的测试环境中保持与教师模型一致的行为，或者是否会退回到其原始输出模式，这引发了对蒸馏模型泛化能力的担忧。为了分析这个问题，我们引入了一个跨模型推理蒸馏溯源框架。对于蒸馏模型产生的每个动作（例如，一个句子），我们获取教师模型、原始学生模型和蒸馏模型在相同上下文下的预测概率。通过比较这些概率，我们将每个动作分类到不同的类别中。通过系统地解耦每个动作的来源，我们通过实验证明，在测试环境中，蒸馏模型确实可以生成源自教师模型的动作，这与观察到的蒸馏模型性能相关，并可能解释其性能。在此分析的基础上，我们进一步提出了一种教师引导的数据选择方法。与依赖启发式方法的先前方法不同，我们的方法直接比较训练数据上教师-学生模型的差异，提供了一个有原则的选择标准。我们在多个具有代表性的教师模型和不同的学生模型上验证了我们方法的有效性。结果突出了我们的溯源框架的实用性，并强调了其在推理蒸馏中的前景。我们希望与社区分享推理蒸馏溯源和我们对推理蒸馏的见解。

## 🔬 方法详解

**问题定义**：推理蒸馏旨在将大型教师模型的推理能力迁移到小型学生模型。然而，现有方法难以分析学生模型在蒸馏后获得的推理能力究竟来源于教师模型还是学生模型自身，尤其是在面对新的测试环境时，学生模型可能退化回原始状态，导致泛化能力不足。因此，需要一种方法来追踪和分析学生模型推理行为的来源，从而更好地理解和改进蒸馏过程。

**核心思路**：核心思路是通过比较教师模型、原始学生模型和蒸馏后学生模型在相同上下文下的预测概率，来判断蒸馏后学生模型的行为（例如生成的句子）是来源于教师模型的指导，还是来源于学生模型自身的固有行为。通过分析不同来源的行为对最终性能的影响，可以更好地理解蒸馏过程，并指导数据选择。

**技术框架**：该框架包含以下几个主要步骤：1) 对于学生模型生成的每个动作（例如，一个句子），获取教师模型、原始学生模型和蒸馏后学生模型在相同上下文下的预测概率分布。2) 基于这些概率分布，将每个动作分类到不同的类别，例如“教师模型来源”、“学生模型来源”等。3) 分析不同来源的动作与最终性能之间的关系，例如，教师模型来源的动作是否与更高的准确率相关。4) 基于分析结果，提出教师引导的数据选择方法，选择那些教师模型和学生模型差异较大的数据进行蒸馏，以提高蒸馏效果。

**关键创新**：关键创新在于提出了一个跨模型的溯源框架，能够细粒度地分析蒸馏后学生模型行为的来源，并将其与最终性能联系起来。与以往依赖启发式方法的数据选择不同，该方法直接比较教师-学生模型的差异，提供了一个更具原则性的数据选择标准。

**关键设计**：框架的关键设计包括：1) 如何定义和计算教师模型、原始学生模型和蒸馏后学生模型之间的预测概率差异。2) 如何将学生模型的行为分类到不同的来源类别。3) 如何设计教师引导的数据选择策略，例如，选择哪些数据进行蒸馏，以及如何平衡不同来源的数据。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.20908v1/sections/1_intro/0_motivation.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.20908v1/sections/3_analyse/0_action_split.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.20908v1/x1.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

实验结果表明，蒸馏模型在测试时可以生成源自教师模型的动作，并且这些动作与性能提升相关。通过教师引导的数据选择方法，可以在多个教师模型和学生模型上验证其有效性，表明该方法具有良好的泛化能力。具体性能提升数据未知，但强调了溯源框架的实用性。

## 🎯 应用场景

该研究成果可应用于各种需要模型压缩和加速的场景，例如移动设备上的自然语言处理、边缘计算环境下的智能问答等。通过更有效地进行推理蒸馏，可以降低模型部署的成本和延迟，提高用户体验。此外，该溯源框架有助于理解模型行为，提升模型的可解释性和可靠性。

## 📄 摘要（原文）

> Reasoning distillation has attracted increasing attention. It typically leverages a large teacher model to generate reasoning paths, which are then used to fine-tune a student model so that it mimics the teacher's behavior in training contexts. However, previous approaches have lacked a detailed analysis of the origins of the distilled model's capabilities. It remains unclear whether the student can maintain consistent behaviors with the teacher in novel test-time contexts, or whether it regresses to its original output patterns, raising concerns about the generalization of distillation models. To analyse this question, we introduce a cross-model Reasoning Distillation Provenance Tracing framework. For each action (e.g., a sentence) produced by the distilled model, we obtain the predictive probabilities assigned by the teacher, the original student, and the distilled model under the same context. By comparing these probabilities, we classify each action into different categories. By systematically disentangling the provenance of each action, we experimentally demonstrate that, in test-time contexts, the distilled model can indeed generate teacher-originated actions, which correlate with and plausibly explain observed performance on distilled model. Building on this analysis, we further propose a teacher-guided data selection method. Unlike prior approach that rely on heuristics, our method directly compares teacher-student divergences on the training data, providing a principled selection criterion. We validate the effectiveness of our approach across multiple representative teacher models and diverse student models. The results highlight the utility of our provenance-tracing framework and underscore its promise for reasoning distillation. We hope to share Reasoning Distillation Provenance Tracing and our insights into reasoning distillation with the community.

