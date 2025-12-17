---
layout: default
title: RefBench-PRO: Perceptual and Reasoning Oriented Benchmark for Referring Expression Comprehension
---

# RefBench-PRO: Perceptual and Reasoning Oriented Benchmark for Referring Expression Comprehension

<div class="paper-toolbar">
  <div class="toolbar-left">
    <a href="https://arxiv.org/abs/2512.06276" target="_blank" class="toolbar-btn">arXiv: 2512.06276v2</a>
    <a href="https://arxiv.org/pdf/2512.06276.pdf" target="_blank" class="toolbar-btn">PDF</a>
  </div>
  <div class="toolbar-right">
    <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.06276v2" 
            onclick="toggleFavorite(this, '2512.06276v2', 'RefBench-PRO: Perceptual and Reasoning Oriented Benchmark for Referring Expression Comprehension')" title="收藏">
      ☆ 收藏
    </button>
    <button class="toolbar-btn share-btn" onclick="copyLink()" title="复制链接">
      🔗 分享
    </button>
  </div>
</div>


**作者**: Tianyi Gao, Hao Li, Han Fang, Xin Wei, Xiaodong Dong, Hongbo Sun, Ye Yuan, Zhongjiang He, Jinglin Xu, Jingmin Xin, Hao Sun

**分类**: cs.CV, cs.AI

**发布日期**: 2025-12-06 (更新: 2025-12-13)

---

## 💡 一句话要点

**提出RefBench-PRO基准，用于评估多模态大模型在指代表达理解中的感知和推理能力。**

🎯 **匹配领域**: **支柱三：空间感知 (Perception & SLAM)**

**关键词**: `指代表达理解` `多模态学习` `视觉语言` `基准测试` `推理能力` `感知能力` `强化学习`

## 📋 核心要点

1. 现有REC基准侧重感知能力评估，缺乏对多模态大模型推理能力的针对性评估和可解释的评分机制。
2. RefBench-PRO基准将指代表达理解分解为感知和推理两个维度，并细分为六个更具挑战性的子任务。
3. 提出了Ref-R1学习方案，通过结合动态IoU的GRPO，提升了在复杂推理条件下的定位精度，并建立了更强的基线。

## 📝 摘要（中文）

指代表达理解（REC）是一项视觉-语言任务，旨在根据文本描述定位特定的图像区域。现有的REC基准主要评估感知能力，缺乏可解释的评分机制，无法揭示多模态大型语言模型（MLLM）在不同认知能力上的基础能力。为了解决这一局限性，我们引入了RefBench-PRO，这是一个全面的REC基准，它将指代表达分解为两个核心维度，即感知和推理，并进一步细分为六个渐进式挑战任务，如属性、位置、交互、常识、关系和拒绝。我们还开发了一个全自动的数据生成管道，用于生成跨这六个子维度的多样化指代表达。此外，我们提出了Ref-R1，一种基于RL的学习方案，它结合了基于动态IoU的GRPO，以提高在日益复杂的推理条件下的定位精度，为REC建立更强的基线。大量的实验表明，我们的RefBench-PRO能够对MLLM在指代表达理解方面进行可解释的评估，在感知和推理方面都提出了更大的挑战。

## 🔬 方法详解

**问题定义**：论文旨在解决现有指代表达理解（REC）基准的不足，即主要侧重于感知能力的评估，而忽略了多模态大型语言模型（MLLM）的推理能力。现有方法难以对MLLM在不同认知能力上的基础能力进行有效评估，缺乏可解释的评分机制。

**核心思路**：论文的核心思路是将指代表达理解任务分解为感知和推理两个核心维度，并进一步细分为六个具有递进难度的子任务。通过这种分解，可以更精细地评估MLLM在不同认知能力上的表现，并提供更具解释性的评估结果。

**技术框架**：RefBench-PRO基准包含一个全自动的数据生成管道，用于生成多样化的指代表达，涵盖属性、位置、交互、常识、关系和拒绝六个子维度。此外，论文还提出了Ref-R1学习方案，该方案基于强化学习，并结合了动态IoU的GRPO（未知具体含义），以提高在复杂推理条件下的定位精度。整体流程包括数据生成、模型训练和评估三个主要阶段。

**关键创新**：论文的关键创新在于提出了RefBench-PRO基准，该基准能够对MLLM在指代表达理解中的感知和推理能力进行更全面、更精细的评估。与现有基准相比，RefBench-PRO更注重推理能力的评估，并提供了更具解释性的评估结果。此外，Ref-R1学习方案的引入也为REC任务提供了一种新的解决思路。

**关键设计**：关于数据生成管道的具体实现细节、动态IoU-based GRPO的具体算法细节、强化学习的奖励函数设计、以及网络结构的具体参数设置等技术细节，论文摘要中未提供详细信息，因此无法进行深入描述。这些细节可能在论文正文中有所阐述。

## 📊 实验亮点

实验结果表明，RefBench-PRO基准能够有效评估MLLM在指代表达理解中的感知和推理能力，并对现有模型提出了更大的挑战。Ref-R1学习方案在复杂推理条件下显著提高了定位精度，为REC任务建立了一个更强的基线。具体的性能数据和提升幅度需要在论文正文中查找。

## 🎯 应用场景

该研究成果可应用于智能机器人、自动驾驶、图像搜索等领域。通过提升多模态大模型在指代表达理解方面的能力，可以使机器更好地理解人类指令，从而实现更智能的人机交互和更精准的目标定位。未来，该研究有望推动视觉-语言智能的发展，并为相关应用带来更广阔的前景。

## 📄 摘要（原文）

> Referring Expression Comprehension (REC) is a vision-language task that localizes a specific image region based on a textual description. Existing REC benchmarks primarily evaluate perceptual capabilities and lack interpretable scoring mechanisms, which cannot reveal the grounding capability of Multi-modal Large Language Model (MLLM) across different cognitive abilities. To address this limitation, we introduce RefBench-PRO, a comprehensive REC benchmark, which decomposes referring expressions into two core dimensions, i.e., perception and reasoning, and further subdivides them into six progressively challenging tasks, such as attribute, position, interaction, commonsense, relation and reject. We also develop a fully automated data-generation pipeline that produces diverse referring expressions across these six sub-dimensions. Furthermore, We propose Ref-R1, an RL-based learning scheme, which incorporates Dynamic IoU-based GRPO to improve localization accuracy under increasingly complex reasoning conditions, establishing a stronger baseline for REC. Extensive experiments demonstrate that our RefBench-PRO enables interpretable evaluation of MLLM on referring expression comprehension, presenting greater challenges in both perception and reasoning.

