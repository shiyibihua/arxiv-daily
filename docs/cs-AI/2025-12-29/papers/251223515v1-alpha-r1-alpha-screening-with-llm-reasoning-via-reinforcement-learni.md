---
layout: default
title: "Alpha-R1: Alpha Screening with LLM Reasoning via Reinforcement Learning"
---

# Alpha-R1: Alpha Screening with LLM Reasoning via Reinforcement Learning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.23515" class="toolbar-btn" target="_blank">📄 arXiv: 2512.23515v1</a>
  <a href="https://arxiv.org/pdf/2512.23515.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.23515v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.23515v1', 'Alpha-R1: Alpha Screening with LLM Reasoning via Reinforcement Learning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zuoyou Jiang, Li Zhao, Rui Sun, Ruohan Sun, Zhongjian Li, Jing Li, Daxin Jiang, Zuo Bai, Cheng Hua

**分类**: q-fin.TR, cs.AI, cs.CE, cs.LG

**发布日期**: 2025-12-29

**🔗 代码/项目**: [GITHUB](https://github.com/FinStep-AI/Alpha-R1)

---

## 💡 一句话要点

**提出Alpha-R1，利用强化学习训练LLM进行上下文感知的Alpha筛选，提升量化投资策略的鲁棒性。**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `量化投资` `大型语言模型` `强化学习` `因子筛选` `上下文感知`

## 📋 核心要点

1. 传统量化投资方法依赖历史数据，难以应对市场环境变化带来的信号衰减和机制转变。
2. Alpha-R1利用大型语言模型进行经济推理，结合因子逻辑和实时新闻，实现上下文感知的alpha筛选。
3. 实验结果表明，Alpha-R1在多个资产池中优于基准策略，并提高了对alpha衰减的鲁棒性。

## 📝 摘要（中文）

非平稳市场中，信号衰减和机制转变对数据驱动的投资策略提出了持续的挑战。传统的时序和机器学习方法主要依赖历史相关性，难以在经济环境变化时泛化。大型语言模型(LLM)在处理非结构化信息方面表现出强大的能力，但其通过显式经济推理支持量化因子筛选的潜力尚未得到充分探索。现有的基于因子的方法通常将alphas简化为数值时间序列，忽略了决定因子何时具有经济相关性的语义原理。我们提出了Alpha-R1，一个通过强化学习训练的80亿参数推理模型，用于上下文感知的alpha筛选。Alpha-R1基于因子逻辑和实时新闻进行推理，以评估alpha在变化的市场条件下的相关性，并根据上下文一致性选择性地激活或停用因子。跨多个资产池的实证结果表明，Alpha-R1始终优于基准策略，并表现出对alpha衰减的改进的鲁棒性。完整的实现和资源可在https://github.com/FinStep-AI/Alpha-R1获得。

## 🔬 方法详解

**问题定义**：论文旨在解决量化投资中因子有效性随时间衰减以及市场环境变化导致因子失效的问题。现有方法主要依赖历史数据，缺乏对市场环境变化的适应性，无法有效识别和利用在特定市场条件下有效的alpha因子。

**核心思路**：论文的核心思路是利用大型语言模型（LLM）的推理能力，结合因子逻辑和实时新闻，对alpha因子进行上下文感知的筛选。通过让LLM理解市场环境变化对因子有效性的影响，从而选择性地激活或停用因子，提高投资策略的鲁棒性。

**技术框架**：Alpha-R1的技术框架包含以下几个主要模块：1)因子逻辑和实时新闻输入模块，负责收集和处理因子逻辑描述和实时市场新闻；2)LLM推理模块，利用预训练的LLM进行经济推理，评估alpha因子在当前市场环境下的相关性；3)强化学习训练模块，通过强化学习算法优化LLM的推理能力，使其能够更好地适应市场变化；4)因子激活/停用模块，根据LLM的推理结果，选择性地激活或停用alpha因子。

**关键创新**：论文最重要的技术创新点在于将大型语言模型的推理能力引入到量化因子筛选中，实现了上下文感知的alpha筛选。与现有方法相比，Alpha-R1能够更好地理解市场环境变化对因子有效性的影响，从而提高投资策略的鲁棒性。现有方法通常将alpha简化为数值时间序列，忽略了语义信息。

**关键设计**：Alpha-R1使用一个80亿参数的LLM作为推理引擎。强化学习的奖励函数设计至关重要，需要能够反映投资组合的收益和风险。论文中使用了特定的奖励函数来鼓励模型选择能够带来更高收益且风险可控的alpha因子。具体参数设置和网络结构细节在论文中有详细描述，但此处未给出。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.23515v1/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.23515v1/images/nav/main_result_comparison.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.23515v1/images/nav/main_result_csi1000_comparison.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

Alpha-R1在多个资产池的实验结果表明，其性能始终优于基准策略，并且对alpha衰减具有更强的鲁棒性。具体的性能提升数据在论文中给出，但此处未提供详细数值。实验结果验证了利用LLM进行上下文感知alpha筛选的有效性。

## 🎯 应用场景

Alpha-R1可应用于量化投资、风险管理和资产配置等领域。通过利用LLM的推理能力，可以更有效地识别和利用在特定市场条件下有效的alpha因子，提高投资组合的收益和风险调整后收益。该研究为开发更智能、更鲁棒的量化投资策略提供了新的思路。

## 📄 摘要（原文）

> Signal decay and regime shifts pose recurring challenges for data-driven investment strategies in non-stationary markets. Conventional time-series and machine learning approaches, which rely primarily on historical correlations, often struggle to generalize when the economic environment changes. While large language models (LLMs) offer strong capabilities for processing unstructured information, their potential to support quantitative factor screening through explicit economic reasoning remains underexplored. Existing factor-based methods typically reduce alphas to numerical time series, overlooking the semantic rationale that determines when a factor is economically relevant. We propose Alpha-R1, an 8B-parameter reasoning model trained via reinforcement learning for context-aware alpha screening. Alpha-R1 reasons over factor logic and real-time news to evaluate alpha relevance under changing market conditions, selectively activating or deactivating factors based on contextual consistency. Empirical results across multiple asset pools show that Alpha-R1 consistently outperforms benchmark strategies and exhibits improved robustness to alpha decay. The full implementation and resources are available at https://github.com/FinStep-AI/Alpha-R1.

