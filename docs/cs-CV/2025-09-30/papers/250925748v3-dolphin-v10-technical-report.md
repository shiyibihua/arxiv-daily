---
layout: default
title: Dolphin v1.0 Technical Report
---

# Dolphin v1.0 Technical Report

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.25748" class="toolbar-btn" target="_blank">📄 arXiv: 2509.25748v3</a>
  <a href="https://arxiv.org/pdf/2509.25748.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.25748v3" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.25748v3', 'Dolphin v1.0 Technical Report')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Taohan Weng, Kaibing Hu, Henan Liu, Siya Liu, Xiaoyang Liu, Zhenyu Liu, Jiren Ren, Boyan Wang, Boyang Wang, Yiyu Wang, Yalun Wu, Chaoran Yan, Kaiwen Yan, Jinze Yu, Chi Zhang, Duo Zhang, Haoyun Zheng, Xiaoqing Guo, Jacques Souquet, Hongcheng Guo, Anjie Le

**分类**: cs.CV, cs.AI

**发布日期**: 2025-09-30 (更新: 2025-10-19)

---

## 💡 一句话要点

**Dolphin v1.0：首个大规模多模态超声影像基础模型，统一解决多种临床任务。**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `超声影像` `多模态学习` `医学影像` `深度学习` `强化学习` `基础模型` `临床诊断`

## 📋 核心要点

1. 现有超声影像分析依赖人工，易受噪声干扰，缺乏统一的AI解决方案。
2. Dolphin系列模型通过大规模多模态数据训练，结合领域知识和强化学习，实现超声影像的统一处理。
3. Dolphin R1在U2-Bench测试中U2评分达到0.5835，远超其他模型，显著提升诊断性能。

## 📝 摘要（中文）

超声技术在现代医学中至关重要，但面临操作者依赖性、图像噪声和实时扫描等挑战，阻碍了人工智能的整合。虽然大型多模态模型在其他医学影像领域表现出色，但它们难以应对超声的复杂性。为了解决这个问题，我们推出了Dolphin v1.0 (V1)及其推理增强版本Dolphin R1，这是首个大规模多模态超声基础模型，在一个统一的视觉-语言框架中整合了各种临床任务。为了解决超声的可变性和噪声问题，我们策划了一个200万规模的多模态数据集，结合了教科书知识、公共数据、合成样本和通用语料库。这确保了强大的感知、泛化和临床适应性。Dolphin系列采用三阶段训练策略：领域专业预训练、指令驱动对齐和基于强化学习的优化。Dolphin v1.0在分类、检测、回归和报告生成方面提供了可靠的性能。Dolphin R1通过使用超声特定奖励的强化学习，增强了诊断推理、推理透明度和可解释性。在U2-Bench上对八个超声任务进行评估，Dolphin R1实现了0.5835的U2评分，是第二好模型(0.2968)的两倍以上，创造了新的state of the art。Dolphin v1.0也表现出很强的竞争力，验证了统一框架的有效性。比较表明，推理增强训练显著提高了诊断准确性、一致性和可解释性，突出了其在高风险医疗人工智能中的重要性。

## 🔬 方法详解

**问题定义**：现有超声影像分析方法存在操作者依赖性强、图像质量受噪声影响大、缺乏统一的AI框架等问题。现有的大型多模态模型难以直接应用于超声影像，无法有效解决超声影像的特殊挑战。

**核心思路**：Dolphin系列模型的核心思路是构建一个大规模多模态超声影像基础模型，通过统一的视觉-语言框架来处理各种临床任务。通过大规模数据训练和强化学习，提升模型的感知、泛化和临床适应性，从而实现更准确、可靠和可解释的超声影像分析。

**技术框架**：Dolphin系列模型采用三阶段训练策略：1) 领域专业预训练：利用大规模超声影像数据进行预训练，使模型具备初步的超声影像理解能力。2) 指令驱动对齐：通过指令微调，使模型能够根据指令执行各种临床任务，如分类、检测、回归和报告生成。3) 基于强化学习的优化：使用超声特定奖励的强化学习，进一步提升模型的诊断推理、推理透明度和可解释性。

**关键创新**：Dolphin系列模型的关键创新在于：1) 构建了首个大规模多模态超声影像基础模型，统一解决多种临床任务。2) 提出了基于强化学习的推理增强训练方法，显著提升了诊断准确性、一致性和可解释性。3) 策划了一个200万规模的多模态数据集，有效解决了超声影像的可变性和噪声问题。

**关键设计**：Dolphin R1的关键设计包括：1) 使用超声特定奖励的强化学习，例如，奖励模型诊断的准确性和一致性。2) 设计了专门的损失函数，用于优化模型的推理透明度和可解释性。3) 采用了Transformer架构，能够有效处理超声影像的复杂特征。

## 📊 实验亮点

Dolphin R1在U2-Bench测试中取得了显著的成果，U2评分达到0.5835，是第二名（0.2968）的两倍以上，刷新了SOTA。Dolphin v1.0也表现出很强的竞争力，验证了统一框架的有效性。实验结果表明，推理增强训练显著提高了诊断准确性、一致性和可解释性。

## 🎯 应用场景

Dolphin系列模型可广泛应用于临床超声影像分析，辅助医生进行疾病诊断、病情评估和治疗方案制定。其统一的框架和强大的性能，有望降低对操作者的依赖，提高诊断效率和准确性，并促进超声影像在远程医疗和移动医疗等领域的应用。

## 📄 摘要（原文）

> Ultrasound is crucial in modern medicine but faces challenges like operator dependence, image noise, and real-time scanning, hindering AI integration. While large multimodal models excel in other medical imaging areas, they struggle with ultrasound's complexities. To address this, we introduce Dolphin v1.0 (V1) and its reasoning-augmented version, Dolphin R1-the first large-scale multimodal ultrasound foundation models unifying diverse clinical tasks in a single vision-language framework.To tackle ultrasound variability and noise, we curated a 2-million-scale multimodal dataset, combining textbook knowledge, public data, synthetic samples, and general corpora. This ensures robust perception, generalization, and clinical adaptability.The Dolphin series employs a three-stage training strategy: domain-specialized pretraining, instruction-driven alignment, and reinforcement-based refinement. Dolphin v1.0 delivers reliable performance in classification, detection, regression, and report generation. Dolphin R1 enhances diagnostic inference, reasoning transparency, and interpretability through reinforcement learning with ultrasound-specific rewards.Evaluated on U2-Bench across eight ultrasound tasks, Dolphin R1 achieves a U2-score of 0.5835-over twice the second-best model (0.2968) setting a new state of the art. Dolphin v1.0 also performs competitively, validating the unified framework. Comparisons show reasoning-enhanced training significantly improves diagnostic accuracy, consistency, and interpretability, highlighting its importance for high-stakes medical AI.

