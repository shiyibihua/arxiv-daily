---
layout: default
title: Probing the effectiveness of World Models for Spatial Reasoning through Test-time Scaling
---

# Probing the effectiveness of World Models for Spatial Reasoning through Test-time Scaling

<div class="paper-toolbar">
  <div class="toolbar-left">
    <a href="https://arxiv.org/abs/2512.05809" target="_blank" class="toolbar-btn">arXiv: 2512.05809v1</a>
    <a href="https://arxiv.org/pdf/2512.05809.pdf" target="_blank" class="toolbar-btn">PDF</a>
  </div>
  <div class="toolbar-right">
    <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.05809v1" 
            onclick="toggleFavorite(this, '2512.05809v1', 'Probing the effectiveness of World Models for Spatial Reasoning through Test-time Scaling')" title="收藏">
      ☆ 收藏
    </button>
    <button class="toolbar-btn share-btn" onclick="copyLink()" title="复制链接">
      🔗 分享
    </button>
  </div>
</div>


**作者**: Saurav Jha, M. Jehanzeb Mirza, Wei Lin, Shiqi Yang, Sarath Chandar

**分类**: cs.CV, cs.AI

**发布日期**: 2025-12-05

**备注**: Extended abstract at World Modeling Workshop 2026

**🔗 代码/项目**: [GITHUB](https://github.com/chandar-lab/visa-for-mindjourney)

---

## 💡 一句话要点

**提出ViSA框架，通过空间断言改进世界模型在空间推理中的测试时缩放效果**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `空间推理` `世界模型` `视觉-语言模型` `测试时缩放` `空间断言`

## 📋 核心要点

1. 现有的视觉-语言模型在空间推理任务中表现不足，尤其是在需要多视角理解和视角转换时。
2. 论文提出Verification through Spatial Assertions (ViSA)框架，通过可验证的空间断言来改进测试时奖励信号。
3. ViSA在SAT-Real基准测试中提升了空间推理性能，并纠正了轨迹选择偏差，但在MMSI-Bench上效果不明显。

## 📝 摘要（中文）

视觉-语言模型(VLMs)在需要多视角理解和具身视角转换的空间推理任务中仍然存在局限性。MindJourney等方法尝试通过测试时缩放来弥补这一差距，即世界模型想象动作条件轨迹，启发式验证器从这些轨迹中选择有用的视图。本文系统地研究了这种测试时验证器在基准测试中的行为，揭示了它们的潜力和缺陷。不确定性分析表明，MindJourney的验证器提供的校准意义不大，随机评分通常也能同样有效地降低答案熵，从而暴露了系统的动作偏差和不可靠的奖励信号。为了缓解这些问题，我们引入了通过空间断言进行验证(ViSA)的框架，该框架将测试时奖励建立在可验证的、帧锚定的微声明之上。这种基于原则的验证器持续改进了SAT-Real基准上的空间推理，并通过更平衡的探索行为纠正了轨迹选择偏差。然而，在具有挑战性的MMSI-Bench上，包括我们的验证器在内的所有验证器都未能实现一致的缩放，这表明当前的世界模型形成了一个信息瓶颈，想象的视图未能丰富细粒度的推理。总之，这些发现描绘了基于世界模型的推理的测试时验证的好、坏和丑陋的方面。

## 🔬 方法详解

**问题定义**：论文旨在解决视觉-语言模型在空间推理任务中，由于缺乏有效的多视角信息融合和视角转换能力而导致的性能瓶颈。现有方法，如MindJourney，虽然尝试通过测试时缩放来解决这个问题，但其验证器存在校准不足、动作偏差和奖励信号不可靠等问题。

**核心思路**：论文的核心思路是通过引入基于空间断言的验证机制，来提供更可靠的测试时奖励信号，从而引导世界模型生成更有用的轨迹。这种方法将奖励与可验证的、帧锚定的微声明联系起来，避免了启发式验证器可能存在的偏差。

**技术框架**：ViSA框架的核心在于使用空间断言来验证世界模型生成的轨迹。整体流程如下：1) 世界模型生成一系列动作条件轨迹，即想象不同的视角；2) 对于每个视角，ViSA框架提取与空间关系相关的微声明（例如，物体A在物体B的左边）；3) 这些微声明被用来计算奖励信号，奖励信号用于选择最佳轨迹；4) 最终，选择的轨迹被用来进行空间推理。

**关键创新**：ViSA框架的关键创新在于将测试时奖励与可验证的空间断言联系起来。与传统的启发式验证器相比，ViSA提供了一种更具原则性和可解释性的验证方法，能够有效减少动作偏差，并提供更可靠的奖励信号。

**关键设计**：ViSA框架的关键设计包括：1) 如何定义和提取空间断言；2) 如何将空间断言转化为奖励信号；3) 如何平衡探索和利用，以避免过早收敛到次优轨迹。具体的实现细节，例如空间断言的类型、奖励函数的具体形式以及探索策略，可能需要根据具体的任务进行调整。

## 📊 实验亮点

ViSA框架在SAT-Real基准测试中取得了显著的性能提升，表明其能够有效改进世界模型在空间推理中的表现。实验结果表明，ViSA能够纠正轨迹选择偏差，并提供更平衡的探索行为。然而，在更具挑战性的MMSI-Bench上，ViSA和其他验证器均未能实现一致的缩放，揭示了当前世界模型的信息瓶颈。

## 🎯 应用场景

该研究成果可应用于机器人导航、自动驾驶、虚拟现实等领域，提升智能体在复杂环境中的空间理解和推理能力。通过更可靠的视角选择和环境建模，可以提高智能体在未知环境中的适应性和决策能力，例如在灾难救援、智能家居等场景中。

## 📄 摘要（原文）

> Vision-Language Models (VLMs) remain limited in spatial reasoning tasks that require multi-view understanding and embodied perspective shifts. Recent approaches such as MindJourney attempt to mitigate this gap through test-time scaling where a world model imagines action-conditioned trajectories and a heuristic verifier selects helpful views from such trajectories. In this work, we systematically examine how such test-time verifiers behave across benchmarks, uncovering both their promise and their pitfalls. Our uncertainty-based analyses show that MindJourney's verifier provides little meaningful calibration, and that random scoring often reduces answer entropy equally well, thus exposing systematic action biases and unreliable reward signals. To mitigate these, we introduce a Verification through Spatial Assertions (ViSA) framework that grounds the test-time reward in verifiable, frame-anchored micro-claims. This principled verifier consistently improves spatial reasoning on the SAT-Real benchmark and corrects trajectory-selection biases through more balanced exploratory behavior. However, on the challenging MMSI-Bench, none of the verifiers, including ours, achieve consistent scaling, suggesting that the current world models form an information bottleneck where imagined views fail to enrich fine-grained reasoning. Together, these findings chart the bad, good, and ugly aspects of test-time verification for world-model-based reasoning. Our code is available at https://github.com/chandar-lab/visa-for-mindjourney.

