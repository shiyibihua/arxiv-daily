---
layout: default
title: WAM-Flow: Parallel Coarse-to-Fine Motion Planning via Discrete Flow Matching for Autonomous Driving
---

# WAM-Flow: Parallel Coarse-to-Fine Motion Planning via Discrete Flow Matching for Autonomous Driving

<div class="paper-toolbar">
  <div class="toolbar-left">
    <a href="https://arxiv.org/abs/2512.06112" target="_blank" class="toolbar-btn">arXiv: 2512.06112v2</a>
    <a href="https://arxiv.org/pdf/2512.06112.pdf" target="_blank" class="toolbar-btn">PDF</a>
  </div>
  <div class="toolbar-right">
    <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.06112v2" 
            onclick="toggleFavorite(this, '2512.06112v2', 'WAM-Flow: Parallel Coarse-to-Fine Motion Planning via Discrete Flow Matching for Autonomous Driving')" title="收藏">
      ☆ 收藏
    </button>
    <button class="toolbar-btn share-btn" onclick="copyLink()" title="复制链接">
      🔗 分享
    </button>
  </div>
</div>


**作者**: Yifang Xu, Jiahao Cui, Feipeng Cai, Zhihao Zhu, Hanlin Shang, Shan Luan, Mingwang Xu, Neng Zhang, Yaoyi Li, Jia Cai, Siyu Zhu

**分类**: cs.RO, cs.AI, cs.CV

**发布日期**: 2025-12-05 (更新: 2025-12-11)

**备注**: 18 pages, 11 figures. Code & Model: https://github.com/fudan-generative-vision/WAM-Flow

---

## 💡 一句话要点

**提出WAM-Flow以解决自主驾驶中的轨迹规划问题**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `自主驾驶` `轨迹规划` `离散流匹配` `多模态学习` `并行处理` `性能优化`

## 📋 核心要点

1. 现有的轨迹规划方法多依赖自回归解码器，导致推理速度慢且难以实现并行处理。
2. WAM-Flow通过离散流匹配的方式进行轨迹规划，采用双向去噪和可调的计算-精度权衡，提升了效率和精度。
3. 在NAVSIM v1基准测试中，WAM-Flow的1步和5步推理分别达到了89.1 PDMS和90.3 PDMS，显著优于现有基线。

## 📝 摘要（中文）

我们介绍了WAM-Flow，这是一种将自我轨迹规划视为结构化标记空间中的离散流匹配的视觉-语言-动作（VLA）模型。与自回归解码器不同，WAM-Flow实现了完全并行的双向去噪，能够以可调的计算-精度权衡进行粗到细的优化。该方法结合了通过三元组边距学习保持标量几何的度量对齐数值标记器、几何感知流目标和集成安全性、自我进展及舒适奖励的模拟器引导GRPO对齐，同时保持并行生成。多阶段适应将预训练的自回归骨干网络（Janus-1.5B）从因果解码转换为非因果流模型，并通过持续的多模态预训练增强道路场景能力。得益于一致性模型训练和并行解码推理的固有特性，WAM-Flow在闭环性能上优于自回归和扩散基线，在NAVSIM v1基准测试中，1步推理达到89.1 PDMS，5步推理达到90.3 PDMS。这些结果确立了离散流匹配作为端到端自主驾驶的新有前景的范式。代码将很快公开发布。

## 🔬 方法详解

**问题定义**：论文旨在解决自主驾驶中的轨迹规划问题，现有方法在推理速度和并行处理能力上存在不足，限制了其应用。

**核心思路**：WAM-Flow通过将轨迹规划视为离散流匹配，采用双向去噪的方式，能够实现更高效的并行处理和精度优化。

**技术框架**：WAM-Flow的整体架构包括多个主要模块：度量对齐的数值标记器、几何感知流目标、模拟器引导的GRPO对齐，以及多阶段适应过程，将自回归模型转化为流模型。

**关键创新**：该研究的核心创新在于引入离散流匹配作为新的轨迹规划范式，显著提高了闭环性能，尤其是在并行生成方面的优势。

**关键设计**：WAM-Flow采用三元组边距学习的损失函数，设计了几何感知流目标，并通过多模态预训练增强了模型对道路场景的理解能力。

## 📊 实验亮点

WAM-Flow在NAVSIM v1基准测试中表现出色，1步推理达到了89.1 PDMS，5步推理达到了90.3 PDMS，显著优于自回归和扩散基线，展示了其在闭环性能上的优势。

## 🎯 应用场景

WAM-Flow在自主驾驶领域具有广泛的应用潜力，能够有效提升车辆在复杂环境中的轨迹规划能力。其高效的并行处理特性使得实时决策成为可能，未来可应用于自动驾驶汽车、智能交通系统等场景，推动智能出行的发展。

## 📄 摘要（原文）

> We introduce WAM-Flow, a vision-language-action (VLA) model that casts ego-trajectory planning as discrete flow matching over a structured token space. In contrast to autoregressive decoders, WAM-Flow performs fully parallel, bidirectional denoising, enabling coarse-to-fine refinement with a tunable compute-accuracy trade-off. Specifically, the approach combines a metric-aligned numerical tokenizer that preserves scalar geometry via triplet-margin learning, a geometry-aware flow objective and a simulator-guided GRPO alignment that integrates safety, ego progress, and comfort rewards while retaining parallel generation. A multi-stage adaptation converts a pre-trained auto-regressive backbone (Janus-1.5B) from causal decoding to non-causal flow model and strengthens road-scene competence through continued multimodal pretraining. Thanks to the inherent nature of consistency model training and parallel decoding inference, WAM-Flow achieves superior closed-loop performance against autoregressive and diffusion-based VLA baselines, with 1-step inference attaining 89.1 PDMS and 5-step inference reaching 90.3 PDMS on NAVSIM v1 benchmark. These results establish discrete flow matching as a new promising paradigm for end-to-end autonomous driving. The code will be publicly available soon.

