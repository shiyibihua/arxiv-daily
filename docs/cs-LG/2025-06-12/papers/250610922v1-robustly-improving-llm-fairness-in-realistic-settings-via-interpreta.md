---
layout: default
title: Robustly Improving LLM Fairness in Realistic Settings via Interpretability
---

# Robustly Improving LLM Fairness in Realistic Settings via Interpretability

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.10922" class="toolbar-btn" target="_blank">📄 arXiv: 2506.10922v1</a>
  <a href="https://arxiv.org/pdf/2506.10922.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.10922v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.10922v1', 'Robustly Improving LLM Fairness in Realistic Settings via Interpretability')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Adam Karvonen, Samuel Marks

**分类**: cs.LG, cs.AI, cs.CL

**发布日期**: 2025-06-12

---

## 💡 一句话要点

**通过可解释性方法提升LLM在招聘中的公平性**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `偏见缓解` `招聘公平性` `可解释性` `内部偏见识别` `仿射概念编辑` `模型性能`

## 📋 核心要点

1. 现有的反偏见方法在引入现实上下文时失效，导致招聘中的种族和性别偏见显著增加。
2. 论文提出通过内部偏见缓解，识别并中和模型激活中的敏感属性方向，以实现更稳健的偏见减少。
3. 实验结果显示，采用该方法后，偏见水平通常降至1%以下，且模型性能保持良好。

## 📝 摘要（中文）

大型语言模型（LLMs）在高风险招聘应用中越来越多地被使用，直接影响人们的职业生涯。尽管先前研究表明简单的反偏见提示可以消除控制评估中的人口统计偏见，但我们发现这些缓解措施在引入现实上下文细节时失效。我们通过内部偏见缓解来解决这些问题：通过识别和中和模型激活中的敏感属性方向，我们在所有测试场景中实现了稳健的偏见减少。我们的研究表明，招聘实践者应采用更现实的评估方法，并考虑内部缓解策略以实现公平结果。

## 🔬 方法详解

**问题定义**：本研究旨在解决大型语言模型在招聘应用中存在的种族和性别偏见问题。现有方法在引入现实上下文时表现不佳，导致偏见未能有效消除。

**核心思路**：论文的核心思路是通过内部偏见缓解技术，识别模型激活中的种族和性别相关方向，并在推理时进行仿射概念编辑，从而实现偏见的有效减少。

**技术框架**：整体架构包括三个主要模块：首先，识别敏感属性方向；其次，在推理阶段应用仿射编辑；最后，评估模型的偏见水平和性能。

**关键创新**：最重要的技术创新在于通过简单的合成数据集提取的方向能够在多种模型中稳健地推广，显著降低偏见水平，与现有方法相比，提供了更为有效的解决方案。

**关键设计**：在技术细节上，采用了特定的损失函数来优化偏见减少，同时保持模型的整体性能，确保在不同模型和场景下均能有效应用。

## 📊 实验亮点

实验结果表明，通过内部偏见缓解方法，模型的种族和性别偏见水平通常降至1%以下，且始终低于2.5%。在引入现实上下文后，偏见显著降低，模型在多个商业和开源模型中均表现出一致的效果，显示出该方法的广泛适用性。

## 🎯 应用场景

该研究的潜在应用领域包括高风险招聘、自动化人力资源管理和公平性评估等。通过引入更现实的评估方法和内部缓解策略，能够帮助企业在招聘过程中实现更公平的结果，减少潜在的偏见影响，对社会公平具有重要价值。未来，这一方法可能扩展到其他领域，如信贷审批和医疗决策等，推动更广泛的公平性实践。

## 📄 摘要（原文）

> Large language models (LLMs) are increasingly deployed in high-stakes hiring applications, making decisions that directly impact people's careers and livelihoods. While prior studies suggest simple anti-bias prompts can eliminate demographic biases in controlled evaluations, we find these mitigations fail when realistic contextual details are introduced. We address these failures through internal bias mitigation: by identifying and neutralizing sensitive attribute directions within model activations, we achieve robust bias reduction across all tested scenarios. Across leading commercial (GPT-4o, Claude 4 Sonnet, Gemini 2.5 Flash) and open-source models (Gemma-2 27B, Gemma-3, Mistral-24B), we find that adding realistic context such as company names, culture descriptions from public careers pages, and selective hiring constraints (e.g.,``only accept candidates in the top 10\%") induces significant racial and gender biases (up to 12\% differences in interview rates). When these biases emerge, they consistently favor Black over White candidates and female over male candidates across all tested models and scenarios. Moreover, models can infer demographics and become biased from subtle cues like college affiliations, with these biases remaining invisible even when inspecting the model's chain-of-thought reasoning. To address these limitations, our internal bias mitigation identifies race and gender-correlated directions and applies affine concept editing at inference time. Despite using directions from a simple synthetic dataset, the intervention generalizes robustly, consistently reducing bias to very low levels (typically under 1\%, always below 2.5\%) while largely maintaining model performance. Our findings suggest that practitioners deploying LLMs for hiring should adopt more realistic evaluation methodologies and consider internal mitigation strategies for equitable outcomes.

