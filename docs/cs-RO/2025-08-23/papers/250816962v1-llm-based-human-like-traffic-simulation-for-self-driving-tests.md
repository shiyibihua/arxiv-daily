---
layout: default
title: LLM-based Human-like Traffic Simulation for Self-driving Tests
---

# LLM-based Human-like Traffic Simulation for Self-driving Tests

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.16962" class="toolbar-btn" target="_blank">📄 arXiv: 2508.16962v1</a>
  <a href="https://arxiv.org/pdf/2508.16962.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.16962v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.16962v1', 'LLM-based Human-like Traffic Simulation for Self-driving Tests')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Wendi Li, Hao Wu, Han Gao, Bing Mao, Fengyuan Xu, Sheng Zhong

**分类**: cs.RO, cs.AI

**发布日期**: 2025-08-23

---

## 💡 一句话要点

**提出HDSim以解决自驾系统模拟中交通动态真实感不足的问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `交通模拟` `自驾系统` `大型语言模型` `层次化模型` `行为影响策略` `安全检测` `真实感`

## 📋 核心要点

1. 现有交通模拟方法多依赖手工规则或狭窄数据驱动模型，无法全面反映真实驾驶行为。
2. HDSim框架结合认知理论与大型语言模型，采用层次化驾驶员模型和感知介导行为影响策略，提升交通模拟的真实感与多样性。
3. 实验结果显示，HDSim在自驾系统的安全关键失效检测中提升了68%，并增强了事故解释的真实感一致性。

## 📝 摘要（中文）

确保交通动态的真实感是评估自驾系统可靠性的重要前提。由于大多数道路使用者为人类驾驶员，模拟其多样化行为至关重要。然而，现有解决方案通常依赖手工启发式或狭窄的数据驱动模型，无法全面捕捉真实驾驶行为，导致驾驶风格多样性和可解释性有限。为此，本文提出了HDSim，一个结合认知理论与大型语言模型（LLM）辅助的高密度交通生成框架，旨在生成可扩展且真实的交通场景。该框架在两个方面推动了技术的进步：一是引入了层次化驾驶员模型，代表多样化的驾驶风格特征；二是开发了感知介导行为影响策略，通过LLM引导感知间接塑造驾驶员行为。实验表明，将HDSim嵌入模拟中可提升自驾系统对安全关键失效的检测率达68%，并实现事故解释的一致性真实感。

## 🔬 方法详解

**问题定义**：本文旨在解决现有交通模拟方法在真实驾驶行为捕捉上的不足，尤其是缺乏多样性和可解释性的问题。现有方法通常依赖于手工规则或狭窄的数据驱动模型，无法全面反映人类驾驶员的复杂行为。

**核心思路**：HDSim框架的核心思路是结合认知理论与大型语言模型（LLM），通过层次化的驾驶员模型来模拟多样化的驾驶风格，并通过感知介导行为影响策略来引导驾驶员行为的生成。这样的设计旨在提升模拟的真实感和多样性。

**技术框架**：HDSim的整体架构包括两个主要模块：层次化驾驶员模型和感知介导行为影响策略。层次化驾驶员模型通过不同层次的特征来表示驾驶员的个性化风格，而感知介导策略则利用LLM对驾驶员的感知过程进行引导，从而影响其行为决策。

**关键创新**：HDSim的关键创新在于引入了层次化驾驶员模型和感知介导行为影响策略，这与传统方法的手工规则或简单数据驱动模型有本质区别，能够更全面地模拟人类驾驶行为。

**关键设计**：在HDSim中，关键设计包括驾驶员模型的层次化结构、LLM的集成方式以及感知引导策略的实现细节。这些设计确保了模型能够有效捕捉驾驶员的多样化行为特征，并提高模拟的真实感。

## 📊 实验亮点

实验结果显示，将HDSim嵌入自驾系统模拟中，安全关键失效的检测率提升了68%。此外，HDSim在事故解释方面也实现了与真实场景一致的高真实感，为自驾系统的安全性评估提供了更可靠的依据。

## 🎯 应用场景

HDSim框架具有广泛的应用潜力，特别是在自动驾驶系统的开发和测试中。通过提供更真实的交通场景，HDSim能够帮助研发团队在实际部署前更好地评估自驾系统的安全性和可靠性。此外，该框架也可用于交通管理和智能交通系统的优化，推动智能交通技术的发展。

## 📄 摘要（原文）

> Ensuring realistic traffic dynamics is a prerequisite for simulation platforms to evaluate the reliability of self-driving systems before deployment in the real world. Because most road users are human drivers, reproducing their diverse behaviors within simulators is vital. Existing solutions, however, typically rely on either handcrafted heuristics or narrow data-driven models, which capture only fragments of real driving behaviors and offer limited driving style diversity and interpretability. To address this gap, we introduce HDSim, an HD traffic generation framework that combines cognitive theory with large language model (LLM) assistance to produce scalable and realistic traffic scenarios within simulation platforms. The framework advances the state of the art in two ways: (i) it introduces a hierarchical driver model that represents diverse driving style traits, and (ii) it develops a Perception-Mediated Behavior Influence strategy, where LLMs guide perception to indirectly shape driver actions. Experiments reveal that embedding HDSim into simulation improves detection of safety-critical failures in self-driving systems by up to 68% and yields realism-consistent accident interpretability.

