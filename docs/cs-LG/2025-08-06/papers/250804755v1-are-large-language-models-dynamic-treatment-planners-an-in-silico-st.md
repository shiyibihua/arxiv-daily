---
layout: default
title: Are Large Language Models Dynamic Treatment Planners? An In Silico Study from a Prior Knowledge Injection Angle
---

# Are Large Language Models Dynamic Treatment Planners? An In Silico Study from a Prior Knowledge Injection Angle

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.04755" class="toolbar-btn" target="_blank">📄 arXiv: 2508.04755v1</a>
  <a href="https://arxiv.org/pdf/2508.04755.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.04755v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.04755v1', 'Are Large Language Models Dynamic Treatment Planners? An In Silico Study from a Prior Knowledge Injection Angle')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zhiyao Luo, Tingting Zhu

**分类**: cs.LG, cs.CE

**发布日期**: 2025-08-06

**备注**: 20 pages

---

## 💡 一句话要点

**利用大型语言模型优化动态治疗方案以改善临床决策**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `动态治疗方案` `大型语言模型` `临床决策` `强化学习` `胰岛素剂量调整` `零-shot推理` `临床知识注入`

## 📋 核心要点

1. 现有的动态治疗方案在临床决策中面临知识注入和患者安全保障的工程挑战，限制了其实际应用。
2. 本文提出利用大型语言模型的零-shot推理能力，通过语言提示自然嵌入隐性临床知识，以优化胰岛素剂量调整。
3. 实验结果显示，经过设计的零-shot提示使得小型LLMs在稳定患者群体中表现出与专门训练的SRAs相当或更优的临床性能。

## 📝 摘要（中文）

基于强化学习的动态治疗方案在复杂临床决策中具有潜力，但其实际应用受到注入临床知识和确保患者安全的工程要求的限制。本文评估了开源大型语言模型（LLMs）在1型糖尿病模拟器中的动态胰岛素剂量调整能力，比较其零-shot推理性能与专门训练的小型神经网络强化学习代理（SRAs）。研究表明，经过精心设计的零-shot提示使得较小的LLMs（如Qwen2.5-7B）在稳定患者群体中能够实现与经过广泛训练的SRAs相当或更优的临床表现。然而，LLMs在链式推理提示下表现出过于激进的胰岛素剂量，揭示了算术幻觉、时间误解和临床逻辑不一致等关键失败模式。研究结果强调了在临床工作流程中谨慎整合LLMs的必要性，并建议结合语言推理与结构化生理建模的混合方法以实现安全有效的决策支持系统。

## 🔬 方法详解

**问题定义**：本文旨在解决动态治疗方案在临床应用中面临的知识注入和患者安全保障的挑战，现有方法往往需要大量的环境特定训练，限制了其灵活性和实用性。

**核心思路**：论文提出利用大型语言模型的零-shot推理能力，通过精心设计的语言提示，使模型能够自然地嵌入隐性临床知识，从而优化胰岛素剂量调整。

**技术框架**：研究采用了开源大型语言模型作为动态胰岛素剂量调整的代理，构建了一个基于1型糖尿病的模拟器，进行零-shot推理与小型神经网络强化学习代理的性能对比。

**关键创新**：最重要的技术创新在于将大型语言模型应用于动态治疗方案中，利用其语言理解能力进行临床决策，而不是依赖于传统的强化学习方法。

**关键设计**：在实验中，设计了多种零-shot提示以引导模型进行推理，特别关注了链式推理的影响，并分析了模型在处理潜在临床状态（如进餐）时的表现。

## 📊 实验亮点

实验结果表明，经过精心设计的零-shot提示使得小型LLMs（如Qwen2.5-7B）在稳定患者群体中实现了与经过广泛训练的SRAs相当或更优的临床表现，尤其在处理复杂的临床决策时显示出显著的潜力。

## 🎯 应用场景

该研究的潜在应用领域包括糖尿病管理、个性化医疗和智能决策支持系统。通过优化胰岛素剂量调整，能够提高患者的治疗效果和安全性，未来可能在更广泛的临床场景中推广。

## 📄 摘要（原文）

> Reinforcement learning (RL)-based dynamic treatment regimes (DTRs) hold promise for automating complex clinical decision-making, yet their practical deployment remains hindered by the intensive engineering required to inject clinical knowledge and ensure patient safety. Recent advancements in large language models (LLMs) suggest a complementary approach, where implicit prior knowledge and clinical heuristics are naturally embedded through linguistic prompts without requiring environment-specific training. In this study, we rigorously evaluate open-source LLMs as dynamic insulin dosing agents in an in silico Type 1 diabetes simulator, comparing their zero-shot inference performance against small neural network-based RL agents (SRAs) explicitly trained for the task. Our results indicate that carefully designed zero-shot prompts enable smaller LLMs (e.g., Qwen2.5-7B) to achieve comparable or superior clinical performance relative to extensively trained SRAs, particularly in stable patient cohorts. However, LLMs exhibit notable limitations, such as overly aggressive insulin dosing when prompted with chain-of-thought (CoT) reasoning, highlighting critical failure modes including arithmetic hallucination, temporal misinterpretation, and inconsistent clinical logic. Incorporating explicit reasoning about latent clinical states (e.g., meals) yielded minimal performance gains, underscoring the current model's limitations in capturing complex, hidden physiological dynamics solely through textual inference. Our findings advocate for cautious yet optimistic integration of LLMs into clinical workflows, emphasising the necessity of targeted prompt engineering, careful validation, and potentially hybrid approaches that combine linguistic reasoning with structured physiological modelling to achieve safe, robust, and clinically effective decision-support systems.

