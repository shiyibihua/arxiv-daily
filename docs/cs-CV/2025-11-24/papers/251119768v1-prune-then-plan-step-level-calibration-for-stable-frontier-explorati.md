---
layout: default
title: Prune-Then-Plan: Step-Level Calibration for Stable Frontier Exploration in Embodied Question Answering
---

# Prune-Then-Plan: Step-Level Calibration for Stable Frontier Exploration in Embodied Question Answering

<div class="paper-toolbar">
  <div class="toolbar-left">
    <a href="https://arxiv.org/abs/2511.19768" target="_blank" class="toolbar-btn">arXiv: 2511.19768v1</a>
    <a href="https://arxiv.org/pdf/2511.19768.pdf" target="_blank" class="toolbar-btn">PDF</a>
  </div>
  <div class="toolbar-right">
    <button class="toolbar-btn favorite-btn" data-arxiv-id="2511.19768v1" 
            onclick="toggleFavorite(this, '2511.19768v1', 'Prune-Then-Plan: Step-Level Calibration for Stable Frontier Exploration in Embodied Question Answering')" title="收藏">
      ☆ 收藏
    </button>
    <button class="toolbar-btn share-btn" onclick="copyLink()" title="复制链接">
      🔗 分享
    </button>
  </div>
</div>


**作者**: Noah Frahm, Prakrut Patel, Yue Zhang, Shoubin Yu, Mohit Bansal, Roni Sengupta

**分类**: cs.CV, cs.AI, cs.RO

**发布日期**: 2025-11-24

**备注**: webpage: https://noahfrahm.github.io/Prune-Then-Plan-project-page/

---

## 💡 一句话要点

**Prune-Then-Plan：通过步级校准实现具身问答中稳定的边界探索**

🎯 **匹配领域**: **支柱三：空间感知 (Perception & SLAM)**

**关键词**: `具身问答` `视觉-语言模型` `步级校准` `边界探索` `机器人导航`

## 📋 核心要点

1. 现有具身问答智能体在步级探索中，视觉-语言模型常因过度自信和错误校准导致不稳定移动。
2. Prune-Then-Plan框架通过剪枝不合理的边界选择，并将决策委托给基于覆盖率的规划器来稳定探索。
3. 实验表明，该方法在视觉接地的SPL和LLM-Match指标上分别实现了显著提升，并提高了场景覆盖率。

## 📝 摘要（中文）

大型视觉-语言模型(VLMs)通过为开放词汇推理提供强大的语义先验，改进了具身问答(EQA)智能体。然而，当直接用于步级探索时，VLMs常常表现出边界振荡，即由过度自信和错误校准导致的不稳定的来回移动，从而导致低效的导航和降低的答案质量。我们提出了Prune-Then-Plan，一个简单而有效的框架，通过步级校准来稳定探索。我们的方法不信任原始VLM分数，而是使用受Holm-Bonferroni启发的剪枝程序来剪除不合理的边界选择，然后将最终决策委托给基于覆盖率的规划器。这种分离通过依赖人类水平的判断来校准VLMs的步级行为，将过度自信的预测转化为保守的、可解释的行动。集成到3D-Mem EQA框架中，我们的方法在视觉接地的SPL和LLM-Match指标上分别实现了高达49%和33%的相对改进。总的来说，我们的方法在OpenEQA和EXPRESS-Bench数据集上，在相同的探索预算下实现了更好的场景覆盖。

## 🔬 方法详解

**问题定义**：现有具身问答（EQA）智能体在进行步级探索时，直接使用视觉-语言模型（VLM）的原始预测分数，容易受到VLM过度自信和错误校准的影响，导致智能体在探索过程中出现不稳定的来回移动（边界振荡），降低了导航效率和答案质量。因此，需要一种方法来校准VLM的步级行为，使其能够更稳定地进行探索。

**核心思路**：论文的核心思路是将VLM的预测结果进行校准，使其更加保守和可信。具体来说，首先使用剪枝策略去除VLM预测中不合理的选项，然后将最终决策交给一个基于覆盖率的规划器。这种“先剪枝，后规划”的策略能够有效地抑制VLM的过度自信，并利用规划器来保证探索的效率。

**技术框架**：Prune-Then-Plan框架主要包含两个阶段：剪枝阶段和规划阶段。在剪枝阶段，使用受Holm-Bonferroni启发的剪枝程序，根据VLM的预测分数，去除那些置信度较低或者不合理的边界选择。在规划阶段，使用一个基于覆盖率的规划器，根据剩余的边界选择，选择能够最大化场景覆盖率的行动。整个框架集成到3D-Mem EQA框架中。

**关键创新**：该方法最重要的创新点在于提出了一个简单而有效的步级校准框架，通过剪枝和规划相结合的方式，有效地解决了VLM在步级探索中过度自信和错误校准的问题。与直接使用VLM的原始预测分数相比，该方法能够生成更保守、更可解释的行动，从而提高探索的稳定性和效率。

**关键设计**：剪枝阶段的关键在于Holm-Bonferroni inspired pruning procedure，它根据VLM给出的每个frontier的置信度打分，进行排序，然后依次进行假设检验，如果某个frontier的置信度过低，则将其剪除。规划阶段的关键在于coverage-based planner，它根据剩余的frontier，选择能够最大化场景覆盖率的行动。具体实现中，使用了3D-Mem EQA框架作为基础，并对其中的探索策略进行了改进。

## 📊 实验亮点

实验结果表明，Prune-Then-Plan框架在OpenEQA和EXPRESS-Bench数据集上，在视觉接地的SPL指标上分别实现了高达49%的相对改进，在LLM-Match指标上实现了33%的相对改进。此外，该方法在相同的探索预算下，实现了更好的场景覆盖，证明了其在提高探索效率和稳定性方面的有效性。

## 🎯 应用场景

该研究成果可应用于机器人导航、自动驾驶、虚拟现实等领域。通过校准视觉-语言模型的步级行为，可以提高智能体在复杂环境中的探索效率和稳定性，使其能够更好地完成各种任务，例如搜索特定物体、回答问题等。该方法具有广泛的应用前景，有望推动相关领域的发展。

## 📄 摘要（原文）

> Large vision-language models (VLMs) have improved embodied question answering (EQA) agents by providing strong semantic priors for open-vocabulary reasoning. However, when used directly for step-level exploration, VLMs often exhibit frontier oscillations, unstable back-and-forth movements caused by overconfidence and miscalibration, leading to inefficient navigation and degraded answer quality. We propose Prune-Then-Plan, a simple and effective framework that stabilizes exploration through step-level calibration. Instead of trusting raw VLM scores, our method prunes implausible frontier choices using a Holm-Bonferroni inspired pruning procedure and then delegates final decisions to a coverage-based planner. This separation converts overconfident predictions into conservative, interpretable actions by relying on human-level judgments to calibrate the step-level behavior of VLMs. Integrated into the 3D-Mem EQA framework, our approach achieves relative improvements of up to 49% and 33% in visually grounded SPL and LLM-Match metrics respectively over baselines. Overall, our method achieves better scene coverage under equal exploration budgets on both OpenEQA and EXPRESS-Bench datasets.

