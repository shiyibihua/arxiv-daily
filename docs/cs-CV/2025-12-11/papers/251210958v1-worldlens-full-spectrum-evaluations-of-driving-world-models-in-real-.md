---
layout: default
title: WorldLens: Full-Spectrum Evaluations of Driving World Models in Real World
---

# WorldLens: Full-Spectrum Evaluations of Driving World Models in Real World

<div class="paper-toolbar">
  <div class="toolbar-left">
    <a href="https://arxiv.org/abs/2512.10958" target="_blank" class="toolbar-btn">arXiv: 2512.10958v1</a>
    <a href="https://arxiv.org/pdf/2512.10958.pdf" target="_blank" class="toolbar-btn">PDF</a>
  </div>
  <div class="toolbar-right">
    <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.10958v1" 
            onclick="toggleFavorite(this, '2512.10958v1', 'WorldLens: Full-Spectrum Evaluations of Driving World Models in Real World')" title="收藏">
      ☆ 收藏
    </button>
    <button class="toolbar-btn share-btn" onclick="copyLink()" title="复制链接">
      🔗 分享
    </button>
  </div>
</div>


**作者**: Ao Liang, Lingdong Kong, Tianyi Yan, Hongsi Liu, Wesley Yang, Ziqi Huang, Wei Yin, Jialong Zuo, Yixuan Hu, Dekai Zhu, Dongyue Lu, Youquan Liu, Guangfeng Jiang, Linfeng Li, Xiangtai Li, Long Zhuo, Lai Xing Ng, Benoit R. Cottereau, Changxin Gao, Liang Pan, Wei Tsang Ooi, Ziwei Liu

**分类**: cs.CV

**发布日期**: 2025-12-11

**备注**: Preprint; 80 pages, 37 figures, 29 tables; Project Page at https://worldbench.github.io/worldlens

---

## 💡 一句话要点

**WorldLens：真实世界中驾驶世界模型的全方位评估基准**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱七：动作重定向 (Motion Retargeting)**

**关键词**: `世界模型` `驾驶场景` `评估基准` `具身智能` `生成式模型`

## 📋 核心要点

1. 现有世界模型在视觉真实感、物理合理性和行为保真度之间存在trade-off，缺乏统一的评估标准。
2. WorldLens通过五个方面（生成、重建、动作跟随、下游任务、人类偏好）综合评估世界模型的性能。
3. 构建大规模人工标注数据集WorldLens-26K，并训练评估模型WorldLens-Agent，实现可扩展的评估。

## 📝 摘要（中文）

生成式世界模型正在重塑具身智能，使智能体能够合成逼真的4D驾驶环境。然而，这些环境在视觉上令人信服，但在物理或行为上常常失败。尽管进展迅速，但该领域仍然缺乏统一的方法来评估生成的世界是否保留了几何结构、遵守物理定律或支持可靠的控制。我们推出了WorldLens，这是一个全方位基准，用于评估模型在其生成的世界中构建、理解和行为的能力。它涵盖五个方面——生成、重建、动作跟随、下游任务和人类偏好——共同涵盖视觉真实感、几何一致性、物理合理性和功能可靠性。结果表明，没有现有的世界模型在所有方面都表现出色：纹理强的模型常常违反物理定律，而几何稳定的模型则缺乏行为保真度。为了使客观指标与人类判断对齐，我们进一步构建了WorldLens-26K，这是一个大规模的人工标注视频数据集，包含数值评分和文本理由，并开发了WorldLens-Agent，这是一个从这些标注中提炼出来的评估模型，以实现可扩展、可解释的评分。基准、数据集和智能体共同构成了一个统一的生态系统，用于衡量世界保真度——标准化未来模型不仅要根据它们看起来有多真实来判断，还要根据它们行为有多真实来判断。

## 🔬 方法详解

**问题定义**：现有生成式世界模型虽然在视觉上逼真，但在几何一致性、物理合理性和行为控制方面存在不足，缺乏一个统一的、全方位的评估标准来衡量模型的综合性能。现有方法难以平衡视觉真实感、物理合理性和行为保真度，导致模型在实际应用中表现不佳。

**核心思路**：WorldLens的核心思路是构建一个全面的评估体系，从多个维度评估世界模型的性能，包括生成质量、重建精度、动作跟随能力、下游任务表现以及人类偏好。通过多方面的评估，可以更准确地了解模型的优缺点，并指导模型改进。

**技术框架**：WorldLens评估体系包含五个主要模块：1) **生成 (Generation)**：评估生成环境的视觉真实感；2) **重建 (Reconstruction)**：评估模型重建环境的能力；3) **动作跟随 (Action-Following)**：评估模型预测动作执行后环境变化的能力；4) **下游任务 (Downstream Task)**：评估模型在实际驾驶任务中的表现；5) **人类偏好 (Human Preference)**：通过人工评估来衡量模型的整体质量。此外，还构建了WorldLens-26K数据集，包含人工标注的视频，用于训练WorldLens-Agent评估模型。

**关键创新**：WorldLens的关键创新在于其全方位的评估体系，它不仅关注视觉真实感，还关注几何一致性、物理合理性和行为保真度。此外，WorldLens-Agent的引入使得评估过程更加高效和可扩展，能够自动评估生成环境的质量。

**关键设计**：WorldLens-26K数据集包含大量人工标注的驾驶场景视频，每个视频都包含数值评分和文本理由，用于训练WorldLens-Agent。WorldLens-Agent是一个深度学习模型，通过学习人类的评估标准，能够自动评估生成环境的质量。具体的网络结构和损失函数等细节在论文中可能有所描述，但摘要中未明确提及。

## 📊 实验亮点

实验结果表明，没有现有的世界模型在所有评估维度上都表现出色。某些模型在视觉真实感方面表现良好，但在物理合理性方面存在缺陷；而另一些模型在几何一致性方面表现出色，但在行为保真度方面存在不足。WorldLens-Agent能够有效地学习人类的评估标准，并自动评估生成环境的质量。

## 🎯 应用场景

WorldLens可应用于自动驾驶、机器人、游戏等领域，用于评估和改进生成式世界模型。通过该基准，可以开发出更逼真、更可靠的世界模型，从而提高智能体在复杂环境中的适应性和决策能力。未来，WorldLens可以扩展到其他领域，例如室内导航、虚拟现实等。

## 📄 摘要（原文）

> Generative world models are reshaping embodied AI, enabling agents to synthesize realistic 4D driving environments that look convincing but often fail physically or behaviorally. Despite rapid progress, the field still lacks a unified way to assess whether generated worlds preserve geometry, obey physics, or support reliable control. We introduce WorldLens, a full-spectrum benchmark evaluating how well a model builds, understands, and behaves within its generated world. It spans five aspects -- Generation, Reconstruction, Action-Following, Downstream Task, and Human Preference -- jointly covering visual realism, geometric consistency, physical plausibility, and functional reliability. Across these dimensions, no existing world model excels universally: those with strong textures often violate physics, while geometry-stable ones lack behavioral fidelity. To align objective metrics with human judgment, we further construct WorldLens-26K, a large-scale dataset of human-annotated videos with numerical scores and textual rationales, and develop WorldLens-Agent, an evaluation model distilled from these annotations to enable scalable, explainable scoring. Together, the benchmark, dataset, and agent form a unified ecosystem for measuring world fidelity -- standardizing how future models are judged not only by how real they look, but by how real they behave.

