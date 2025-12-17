---
layout: default
title: Start Small, Think Big: Curriculum-based Relative Policy Optimization for Visual Grounding
---

# Start Small, Think Big: Curriculum-based Relative Policy Optimization for Visual Grounding

<div class="paper-toolbar">
  <div class="toolbar-left">
    <a href="https://arxiv.org/abs/2511.13924" target="_blank" class="toolbar-btn">arXiv: 2511.13924v1</a>
    <a href="https://arxiv.org/pdf/2511.13924.pdf" target="_blank" class="toolbar-btn">PDF</a>
  </div>
  <div class="toolbar-right">
    <button class="toolbar-btn favorite-btn" data-arxiv-id="2511.13924v1" 
            onclick="toggleFavorite(this, '2511.13924v1', 'Start Small, Think Big: Curriculum-based Relative Policy Optimization for Visual Grounding')" title="收藏">
      ☆ 收藏
    </button>
    <button class="toolbar-btn share-btn" onclick="copyLink()" title="复制链接">
      🔗 分享
    </button>
  </div>
</div>


**作者**: Qingyang Yan, Guangyao Chen, Yixiong Zou

**分类**: cs.CV

**发布日期**: 2025-11-17

**备注**: AAAI 2026 (Oral)

**🔗 代码/项目**: [GITHUB](https://github.com/qyoung-yan/CuRPO)

---

## 💡 一句话要点

**提出基于课程学习的相对策略优化CuRPO，提升视觉定位任务中CoT推理的性能。**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱三：空间感知 (Perception & SLAM)**

**关键词**: `视觉定位` `Chain-of-Thought` `课程学习` `强化学习` `相对策略优化`

## 📋 核心要点

1. 现有基于强化学习微调的CoT推理在视觉定位任务中表现不佳，尤其是在处理复杂或冗长的CoT输出时。
2. 提出CuRPO，利用CoT长度和gIoU奖励作为复杂度指标，通过课程学习的方式，由简入难地组织训练数据。
3. 实验结果表明，CuRPO在多个视觉定位数据集上显著优于现有方法，尤其在少样本学习场景下表现出色。

## 📝 摘要（中文）

本文发现，基于强化学习微调的CoT推理在视觉定位任务中，尤其是在CoT输出冗长或复杂时，反而会降低性能。此外，由于数据复杂度的差异，增加数据集大小并不总能提高性能。为此，本文提出了一种新的训练策略——基于课程学习的相对策略优化（CuRPO）。CuRPO利用CoT长度和广义交并比（gIoU）奖励作为复杂度指标，逐步构建训练数据，从简单到更具挑战性的示例。在RefCOCO、RefCOCO+、RefCOCOg和LISA数据集上的大量实验表明了该方法的有效性。CuRPO始终优于现有方法，包括Visual-RFT，在RefCOCO上实现了高达+12.52 mAP的显著改进。此外，CuRPO表现出卓越的效率和鲁棒性，即使在少样本学习场景中也能提供强大的定位性能，尤其有利于以模糊和复杂的文本描述为特征的任务。代码已开源。

## 🔬 方法详解

**问题定义**：视觉定位任务旨在根据给定的文本描述，在图像中定位到对应的目标区域。现有的基于Chain-of-Thought (CoT) 的方法虽然在很多任务上表现出色，但在视觉定位任务中，直接使用强化学习微调CoT推理反而可能导致性能下降，尤其是在CoT输出变得复杂或冗长时。此外，简单地增加数据集大小并不一定能提升性能，因为数据集中的样本复杂度各不相同。

**核心思路**：CuRPO的核心思路是采用课程学习的方式，逐步引入更复杂的训练样本，从而避免模型在训练初期就被过于复杂的CoT推理过程所困扰。通过将CoT长度和gIoU奖励作为复杂度指标，CuRPO能够有效地组织训练数据，从简单到复杂地进行学习。这种由简入难的学习方式有助于模型更好地理解文本描述和图像之间的关系，从而提高定位精度。

**技术框架**：CuRPO的整体框架包括以下几个主要模块：1) CoT推理模块：用于生成中间推理步骤；2) 策略优化模块：使用强化学习方法优化CoT推理策略；3) 课程学习模块：根据CoT长度和gIoU奖励动态调整训练数据的难度。训练过程首先从简单的样本开始，随着训练的进行，逐步引入更复杂的样本。在每个训练迭代中，模型根据当前的策略生成CoT推理过程，并根据gIoU奖励更新策略。

**关键创新**：CuRPO最重要的技术创新点在于将课程学习与相对策略优化相结合，从而有效地解决了CoT推理在视觉定位任务中遇到的问题。与传统的强化学习方法不同，CuRPO不是直接优化整个CoT推理过程，而是通过课程学习的方式，逐步引入更复杂的推理步骤，从而避免了模型在训练初期就被过于复杂的推理过程所困扰。此外，CuRPO还使用了相对策略优化，从而更好地利用了CoT推理过程中的中间信息。

**关键设计**：CuRPO的关键设计包括：1) 使用CoT长度和gIoU奖励作为复杂度指标，用于衡量训练样本的难度；2) 设计了课程学习策略，用于动态调整训练数据的难度；3) 使用相对策略优化，从而更好地利用CoT推理过程中的中间信息。具体的参数设置和网络结构取决于具体的视觉定位任务和数据集。

## 📊 实验亮点

CuRPO在RefCOCO、RefCOCO+、RefCOCOg和LISA数据集上进行了广泛的实验，结果表明CuRPO始终优于现有方法，包括Visual-RFT。在RefCOCO数据集上，CuRPO实现了高达+12.52 mAP的显著改进。此外，CuRPO在少样本学习场景中也表现出色，证明了其具有良好的泛化能力和鲁棒性。

## 🎯 应用场景

CuRPO在视觉定位任务中表现出色，可应用于智能零售、自动驾驶、机器人导航等领域。例如，在智能零售中，CuRPO可以帮助机器人根据顾客的语音指令，准确地定位到货架上的商品。在自动驾驶中，CuRPO可以帮助车辆根据交通标志的文本描述，准确地识别交通标志。未来，CuRPO有望进一步扩展到其他视觉任务，如图像描述生成、视觉问答等。

## 📄 摘要（原文）

> Chain-of-Thought (CoT) prompting has recently shown significant promise across various NLP and computer vision tasks by explicitly generating intermediate reasoning steps. However, we find that reinforcement learning (RL)-based fine-tuned CoT reasoning can paradoxically degrade performance in Visual Grounding tasks, particularly as CoT outputs become lengthy or complex. Additionally, our analysis reveals that increased dataset size does not always enhance performance due to varying data complexities. Motivated by these findings, we propose Curriculum-based Relative Policy Optimization (CuRPO), a novel training strategy that leverages CoT length and generalized Intersection over Union (gIoU) rewards as complexity indicators to progressively structure training data from simpler to more challenging examples. Extensive experiments on RefCOCO, RefCOCO+, RefCOCOg, and LISA datasets demonstrate the effectiveness of our approach. CuRPO consistently outperforms existing methods, including Visual-RFT, with notable improvements of up to +12.52 mAP on RefCOCO. Moreover, CuRPO exhibits exceptional efficiency and robustness, delivering strong localization performance even in few-shot learning scenarios, particularly benefiting tasks characterized by ambiguous and intricate textual descriptions.The code is released on https://github.com/qyoung-yan/CuRPO.

