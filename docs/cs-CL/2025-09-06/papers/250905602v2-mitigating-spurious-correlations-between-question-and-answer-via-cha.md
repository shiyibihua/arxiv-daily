---
layout: default
title: Mitigating Spurious Correlations Between Question and Answer via Chain-of-Thought Correctness Perception Distillation
---

# Mitigating Spurious Correlations Between Question and Answer via Chain-of-Thought Correctness Perception Distillation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.05602" class="toolbar-btn" target="_blank">📄 arXiv: 2509.05602v2</a>
  <a href="https://arxiv.org/pdf/2509.05602.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.05602v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.05602v2', 'Mitigating Spurious Correlations Between Question and Answer via Chain-of-Thought Correctness Perception Distillation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Hongyan Xie, Yitong Yao, Yikun Ban, Zixuan Huang, Deqing Wang, Zhenhe Wu, Haoxiang Su, Chao Wang, Shuangyong Song

**分类**: cs.CL

**发布日期**: 2025-09-06 (更新: 2025-09-09)

**备注**: PrePrint

---

## 💡 一句话要点

**提出CoPeD，通过纠正性感知蒸馏缓解CoT数据中的伪相关性问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `链式思考` `知识蒸馏` `伪相关性` `推理质量` `语言模型`

## 📋 核心要点

1. 现有方法依赖大型语言模型生成的CoT数据微调小型模型，但CoT数据中包含的噪声推理会引入问题与答案之间的伪相关性。
2. CoPeD通过引入正确性感知的任务设置和损失函数，鼓励模型基于正确的推理预测答案，并从错误中学习，从而提高推理的忠实性。
3. 实验结果表明，CoPeD在同分布和异分布的推理数据集上均表现出良好的性能，有效提升了模型的推理能力。

## 📝 摘要（中文）

大型语言模型(LLMs)在推理任务中表现出色，但部署成本高昂。因此，小型语言模型(SLMs)通常在LLMs生成的CoT数据上进行微调，以复制LLMs的能力。然而，这些CoT数据可能包含噪声推理，这些推理要么未能证实答案，要么没有提供额外的支持答案预测的信息，这导致SLMs捕获问题和答案之间的虚假相关性，并损害推理质量。在这项工作中，我们提出了Chain-of-Thought Correctness Perception Distillation (CoPeD)，旨在从任务设置和数据利用的角度提高学生模型的推理质量。首先，我们引入了一种正确性感知任务设置，鼓励学生模型基于正确的推理来预测答案，并在推理不正确时修改答案。这种设置提高了推理的忠实性，并允许模型从错误中学习。然后，我们提出了一种正确性感知加权损失，它根据推理和答案的组合损失动态调整每个训练实例的贡献。这种策略鼓励模型更多地关注推理为正确答案提供更强支持的样本。实验表明，CoPeD在同分布(IND)和异分布(OOD)基准推理数据集上均有效。

## 🔬 方法详解

**问题定义**：论文旨在解决小型语言模型(SLMs)在模仿大型语言模型(LLMs)的推理能力时，由于训练数据（LLMs生成的Chain-of-Thought, CoT）中存在噪声推理而导致的伪相关性问题。现有方法直接在CoT数据上训练SLMs，忽略了CoT推理过程的正确性，导致SLMs学习到问题和答案之间的虚假关联，降低了模型的泛化能力。

**核心思路**：论文的核心思路是通过引入正确性感知机制，让SLM能够区分和利用正确的CoT推理，同时避免受到错误推理的影响。具体来说，CoPeD鼓励模型在推理错误时进行修正，并根据推理的正确性动态调整训练样本的权重，从而提高模型的推理质量和鲁棒性。

**技术框架**：CoPeD包含两个主要组成部分：正确性感知任务设置和正确性感知加权损失。在正确性感知任务设置中，模型不仅需要预测答案，还需要判断推理过程是否正确，并在推理错误时修正答案。在正确性感知加权损失中，模型根据推理和答案的组合损失动态调整每个训练实例的贡献，使得模型更加关注那些推理能够有效支持正确答案的样本。整体训练流程为：首先，使用LLM生成CoT数据；然后，使用CoPeD方法训练SLM，使其能够识别和利用正确的推理过程。

**关键创新**：CoPeD的关键创新在于其正确性感知机制。与现有方法不同，CoPeD不仅关注答案的正确性，还关注推理过程的正确性，并利用推理的正确性来指导模型的学习。这种方法能够有效地缓解CoT数据中的伪相关性问题，提高模型的推理质量和泛化能力。

**关键设计**：正确性感知加权损失是CoPeD的关键设计之一。该损失函数根据推理和答案的组合损失动态调整每个训练实例的权重。具体来说，如果推理和答案都正确，则赋予较高的权重；如果推理错误但答案正确，则赋予较低的权重；如果推理和答案都错误，则赋予最低的权重。这种加权方式鼓励模型更加关注那些推理能够有效支持正确答案的样本，从而提高模型的推理能力。具体的权重计算公式未知，需要在论文中查找。

## 📊 实验亮点

论文通过实验验证了CoPeD在同分布和异分布数据集上的有效性。具体性能数据未知，但摘要表明CoPeD能够有效提高模型的推理质量和泛化能力。与直接在CoT数据上训练的模型相比，CoPeD能够更好地缓解伪相关性问题，提高模型的鲁棒性。具体的提升幅度需要在论文中查找。

## 🎯 应用场景

CoPeD方法可应用于各种需要进行复杂推理的任务，例如数学问题求解、常识推理和知识图谱推理等。该方法能够提高小型语言模型的推理能力，使其能够在资源受限的环境中部署，例如移动设备和嵌入式系统。此外，CoPeD还可以用于提高大型语言模型的推理能力，通过纠正推理过程中的错误，提高模型的可靠性和可信度。

## 📄 摘要（原文）

> Large language models (LLMs) excel at reasoning tasks but are expensive to deploy. Thus small language models (SLMs) are fine-tuned on CoT data generated by LLMs to copy LLMs' abilities. However, these CoT data may include noisy rationales that either fail to substantiate the answers or contribute no additional information to support answer prediction, which leads SLMs to capture spurious correlations between questions and answers and compromise the quality of reasoning. In this work, we propose Chain-of-Thought Correctness Perception Distillation (CoPeD), which aims to improve the reasoning quality of the student model from the perspectives of task setting and data utilization. Firstly, we introduce a correctness-aware task setting that encourages the student model to predict answers based on correct rationales and revise them when they are incorrect. This setting improves the faithfulness of reasoning and allows the model to learn from its mistakes. Then, we propose a Correctness-Aware Weighted loss, which dynamically adjusts the contribution of each training instance based on the combined loss of the rationale and the answer. This strategy encourages the model to focus more on samples where the rationale offers stronger support for the correct answer. Experiments have shown that CoPeD is effective on both in-distribution (IND) and out-of-distribution (OOD) benchmark reasoning datasets.

