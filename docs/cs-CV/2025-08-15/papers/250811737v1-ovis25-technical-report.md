---
layout: default
title: Ovis2.5 Technical Report
---

# Ovis2.5 Technical Report

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.11737" class="toolbar-btn" target="_blank">📄 arXiv: 2508.11737v1</a>
  <a href="https://arxiv.org/pdf/2508.11737.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.11737v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.11737v1', 'Ovis2.5 Technical Report')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Shiyin Lu, Yang Li, Yu Xia, Yuwei Hu, Shanshan Zhao, Yanqing Ma, Zhichao Wei, Yinglun Li, Lunhao Duan, Jianshan Zhao, Yuxuan Han, Haijun Li, Wanying Chen, Junke Tang, Chengkun Hou, Zhixing Du, Tianli Zhou, Wenjie Zhang, Huping Ding, Jiahe Li, Wen Li, Gui Hu, Yiliang Gu, Siran Yang, Jiamang Wang, Hailong Sun, Yibo Wang, Hui Sun, Jinlong Huang, Yuping He, Shengze Shi, Weihong Zhang, Guodong Zheng, Junpeng Jiang, Sensen Gao, Yi-Feng Wu, Sijia Chen, Yuhui Chen, Qing-Guo Chen, Zhao Xu, Weihua Luo, Kaifu Zhang

**分类**: cs.CV, cs.AI, cs.CL, cs.LG

**发布日期**: 2025-08-15

---

## 💡 一句话要点

**提出Ovis2.5以解决多模态推理与视觉感知问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多模态推理` `视觉感知` `原生分辨率` `反思机制` `复杂图表分析` `模型训练` `开源模型` `智能助手`

## 📋 核心要点

1. 现有方法在处理复杂视觉内容时，常常因固定分辨率而导致细节损失和布局失真。
2. Ovis2.5通过原生分辨率视觉变换器处理图像，并引入反思能力以增强推理效果。
3. Ovis2.5-9B在OpenCompass多模态排行榜上平均得分78.3，显著超越前作Ovis2-8B，展示了其在复杂图表分析等任务中的领先能力。

## 📝 摘要（中文）

我们提出了Ovis2.5，作为Ovis2的继任者，旨在实现原生分辨率的视觉感知和强大的多模态推理能力。Ovis2.5集成了一个原生分辨率的视觉变换器，能够以其原生的可变分辨率处理图像，避免了固定分辨率切片带来的细节损失，保留了复杂图表等视觉密集内容的细节和全局布局。为了增强推理能力，我们训练模型超越线性思维链，进行反思，包括自我检查和修订。该高级能力在推理时以可选的“思考模式”形式展现，允许用户在延迟和准确性之间进行权衡。模型通过五个阶段的综合课程进行训练，逐步提升其技能，最终在对齐和推理增强方面取得显著进展。

## 🔬 方法详解

**问题定义**：本论文旨在解决现有多模态模型在处理复杂视觉内容时的细节损失和推理能力不足的问题。现有方法通常依赖固定分辨率，导致信息丢失和推理链条的局限性。

**核心思路**：Ovis2.5的核心思路是采用原生分辨率视觉变换器，能够处理可变分辨率的图像，同时引入反思机制以提升推理能力，使模型在面对复杂输入时能够进行自我检查和修订。

**技术框架**：Ovis2.5的整体架构包括五个阶段：基础视觉和多模态预训练、大规模指令调优、对齐和推理增强。通过多模态数据打包和混合并行技术，提升了训练效率和模型性能。

**关键创新**：Ovis2.5的主要创新在于其原生分辨率处理能力和反思推理机制，这与传统的固定分辨率模型形成了本质区别，显著提高了模型在复杂任务中的表现。

**关键设计**：在模型设计中，采用了多阶段的训练流程，结合DPO和GRPO方法进行对齐和推理增强，确保模型在不同任务中的适应性和准确性。

## 📊 实验亮点

Ovis2.5-9B在OpenCompass多模态排行榜上平均得分78.3，较Ovis2-8B有显著提升，且在复杂图表分析等STEM基准测试中表现优异。Ovis2.5-2B也以73.9的得分在其规模上达到了SOTA，展示了小模型的强大性能。

## 🎯 应用场景

Ovis2.5在多个领域具有广泛的应用潜力，包括教育、科学研究和数据分析等。其强大的视觉感知和推理能力使其能够处理复杂的图表和多模态数据，为用户提供更准确的分析和决策支持。未来，Ovis2.5有望在智能助手、自动化报告生成等场景中发挥重要作用。

## 📄 摘要（原文）

> We present Ovis2.5, a successor to Ovis2 designed for native-resolution visual perception and strong multimodal reasoning. Ovis2.5 integrates a native-resolution vision transformer that processes images at their native, variable resolutions, avoiding the degradation from fixed-resolution tiling and preserving both fine detail and global layout -- crucial for visually dense content like complex charts. To strengthen reasoning, we train the model to move beyond linear chain-of-thought and perform reflection -- including self-checking and revision. This advanced capability is exposed as an optional "thinking mode" at inference time, allowing users to trade latency for enhanced accuracy on difficult inputs. The model is trained via a comprehensive five-phase curriculum that progressively builds its skills. The process begins with foundational visual and multimodal pretraining, advances through large-scale instruction tuning, and culminates in alignment and reasoning enhancement using DPO and GRPO. To scale these upgrades efficiently, we employ multimodal data packing and hybrid parallelism, yielding a significant end-to-end speedup. We release two open-source models: Ovis2.5-9B and Ovis2.5-2B. The latter continues the "small model, big performance" philosophy of Ovis2, making it ideal for resource-constrained, on-device scenarios. On the OpenCompass multimodal leaderboard, Ovis2.5-9B averages 78.3, marking a substantial improvement over its predecessor, Ovis2-8B, and achieving state-of-the-art results among open-source MLLMs in the sub-40B parameter range; Ovis2.5-2B scores 73.9, establishing SOTA for its size. Beyond aggregate scores, Ovis2.5 achieves leading results on STEM benchmarks, exhibits strong capabilities on grounding and video tasks, and achieves open-source SOTA at its scale for complex chart analysis.

