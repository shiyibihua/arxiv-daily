---
layout: default
title: Agentic Explainable Artificial Intelligence (Agentic XAI) Approach To Explore Better Explanation
---

# Agentic Explainable Artificial Intelligence (Agentic XAI) Approach To Explore Better Explanation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.21066" class="toolbar-btn" target="_blank">📄 arXiv: 2512.21066v1</a>
  <a href="https://arxiv.org/pdf/2512.21066.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.21066v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.21066v1', 'Agentic Explainable Artificial Intelligence (Agentic XAI) Approach To Explore Better Explanation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Tomoaki Yamaguchi, Yutong Zhou, Masahiro Ryo, Keisuke Katsura

**分类**: cs.AI, cs.HC

**发布日期**: 2025-12-24

---

## 💡 一句话要点

**提出Agentic XAI框架，结合SHAP与多模态LLM迭代优化解释质量，应用于农业推荐系统。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `可解释人工智能` `Agentic AI` `大型语言模型` `SHAP` `迭代优化` `农业推荐系统` `人机协作`

## 📋 核心要点

1. 现有XAI方法难以向非专业人士有效传达解释，影响了对AI预测的信任。
2. 提出Agentic XAI框架，利用LLM作为智能体迭代改进SHAP解释，提升可理解性。
3. 实验表明，该框架能显著提高农业推荐系统的解释质量，但过度迭代会降低效果。

## 📝 摘要（中文）

可解释人工智能(XAI)能够基于数据理解因素与响应变量之间的关联，但将XAI输出传达给非专业人士仍然具有挑战性，阻碍了对基于AI的预测的信任。大型语言模型(LLM)已成为将技术解释转化为易于理解的叙述的有前途的工具，但agentic AI（LLM作为自主agent通过迭代改进运行）与XAI的集成仍未被探索。本研究提出了一个agentic XAI框架，该框架结合了基于SHAP的可解释性与多模态LLM驱动的迭代改进，以生成逐步增强的解释。作为一个用例，我们使用来自日本26个田地的水稻产量数据，将该框架测试为一个农业推荐系统。Agentic XAI最初提供SHAP结果，并通过11轮改进迭代(第0-10轮)探索如何改进解释。解释由人类专家(作物科学家)(n=12)和LLM(n=14)根据七个指标进行评估：特异性、清晰度、简洁性、实用性、情境相关性、成本考虑和作物科学可信度。两个评估组都证实，该框架成功地提高了推荐质量，从第0轮开始平均得分提高了30-33%，并在第3-4轮达到峰值。然而，过度改进显示推荐质量大幅下降，表明存在偏差-方差权衡，早期轮次缺乏解释深度(偏差)，而过度迭代引入了冗长和无根据的抽象(方差)，正如指标特定分析所揭示的那样。这些发现表明，需要战略性提前停止(正则化)来优化实际效用，挑战了关于单调改进的假设，并为agentic XAI系统提供了基于证据的设计原则。

## 🔬 方法详解

**问题定义**：现有XAI方法生成的解释往往过于技术化，难以被领域专家或普通用户理解和信任。这限制了XAI在实际应用中的价值，尤其是在需要人机协作的场景中。因此，如何将复杂的XAI结果转化为易于理解、具有实用价值的解释，是一个亟待解决的问题。

**核心思路**：论文的核心思路是利用大型语言模型（LLM）的自然语言生成能力，将XAI结果转化为更易于理解的解释。同时，将LLM视为一个智能体，通过迭代改进的方式，逐步优化解释的质量，使其更具特异性、清晰度、简洁性、实用性、情境相关性、成本考虑和作物科学可信度。

**技术框架**：Agentic XAI框架主要包含以下几个阶段：
1. **初始解释生成**：使用SHAP等XAI方法，生成初始的特征重要性解释。
2. **LLM迭代改进**：将初始解释输入LLM，LLM根据预设的评估指标，生成改进后的解释。这个过程会进行多轮迭代，每一轮LLM都会根据上一轮的反馈，进一步优化解释。
3. **解释评估**：使用人工专家和LLM对每一轮迭代生成的解释进行评估，评估指标包括特异性、清晰度、简洁性等。
4. **提前停止机制**：根据评估结果，设置提前停止机制，防止过度迭代导致解释质量下降。

**关键创新**：该论文的关键创新在于将agentic AI的思想引入XAI领域，利用LLM的自主学习能力，迭代优化解释的质量。与传统的XAI方法相比，Agentic XAI能够生成更易于理解、更具实用价值的解释。此外，该论文还提出了一个基于人工专家和LLM的综合评估体系，用于评估解释的质量。

**关键设计**：在实验中，LLM被设置为一个智能体，通过与环境（即XAI结果和评估指标）交互，不断学习和改进解释的质量。论文中使用了特定的prompt工程技术，引导LLM生成符合要求的解释。此外，论文还设计了一个提前停止机制，防止过度迭代导致解释质量下降。具体来说，当评估指标的得分不再显著提升时，迭代过程就会停止。

## 📊 实验亮点

实验结果表明，Agentic XAI框架能够显著提高农业推荐系统的解释质量，平均得分提高了30-33%。在第3-4轮迭代时，解释质量达到峰值。然而，过度迭代会导致解释质量下降，表明存在偏差-方差权衡。这些结果验证了Agentic XAI框架的有效性，并为设计可解释AI系统提供了重要的设计原则。

## 🎯 应用场景

该研究成果可应用于各种需要可解释AI的领域，例如医疗诊断、金融风控、智能制造等。通过将复杂的AI决策转化为易于理解的解释，可以提高用户对AI系统的信任度，促进人机协作，并最终提升决策效率和质量。未来，该方法有望被集成到各种AI应用中，成为提升AI可解释性的重要工具。

## 📄 摘要（原文）

> Explainable artificial intelligence (XAI) enables data-driven understanding of factor associations with response variables, yet communicating XAI outputs to laypersons remains challenging, hindering trust in AI-based predictions. Large language models (LLMs) have emerged as promising tools for translating technical explanations into accessible narratives, yet the integration of agentic AI, where LLMs operate as autonomous agents through iterative refinement, with XAI remains unexplored. This study proposes an agentic XAI framework combining SHAP-based explainability with multimodal LLM-driven iterative refinement to generate progressively enhanced explanations. As a use case, we tested this framework as an agricultural recommendation system using rice yield data from 26 fields in Japan. The Agentic XAI initially provided a SHAP result and explored how to improve the explanation through additional analysis iteratively across 11 refinement rounds (Rounds 0-10). Explanations were evaluated by human experts (crop scientists) (n=12) and LLMs (n=14) against seven metrics: Specificity, Clarity, Conciseness, Practicality, Contextual Relevance, Cost Consideration, and Crop Science Credibility. Both evaluator groups confirmed that the framework successfully enhanced recommendation quality with an average score increase of 30-33% from Round 0, peaking at Rounds 3-4. However, excessive refinement showed a substantial drop in recommendation quality, indicating a bias-variance trade-off where early rounds lacked explanation depth (bias) while excessive iteration introduced verbosity and ungrounded abstraction (variance), as revealed by metric-specific analysis. These findings suggest that strategic early stopping (regularization) is needed for optimizing practical utility, challenging assumptions about monotonic improvement and providing evidence-based design principles for agentic XAI systems.

