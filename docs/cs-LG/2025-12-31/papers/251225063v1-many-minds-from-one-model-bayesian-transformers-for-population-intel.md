---
layout: default
title: "Many Minds from One Model: Bayesian Transformers for Population Intelligence"
---

# Many Minds from One Model: Bayesian Transformers for Population Intelligence

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.25063" class="toolbar-btn" target="_blank">📄 arXiv: 2512.25063v1</a>
  <a href="https://arxiv.org/pdf/2512.25063.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.25063v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.25063v1', 'Many Minds from One Model: Bayesian Transformers for Population Intelligence')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Diji Yang, Yi Zhang

**分类**: cs.LG, cs.CL

**发布日期**: 2025-12-31

---

## 💡 一句话要点

**提出Population Bayesian Transformers，提升Transformer模型的多样性和决策能力**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `贝叶斯Transformer` `群体智能` `多样性生成` `强化学习` `零样本学习` `变分推断` `大型语言模型`

## 📋 核心要点

1. 现有Transformer模型通常训练为单一确定性系统，缺乏多样性，限制了其探索能力和泛化性能。
2. B-Trans将Transformer模型转化为贝叶斯模型，通过对归一化层偏置进行随机采样，生成多样化的模型实例。
3. 实验表明，B-Trans在零样本生成和强化学习任务中，能够提升语义多样性和任务性能，有效利用群体智慧。

## 📝 摘要（中文）

本文提出Population Bayesian Transformers (B-Trans)，旨在将标准大型语言模型转化为贝叶斯Transformer模型，从而能够从单个预训练权重集中采样出多样且连贯的模型实例。B-Trans通过将归一化层中的偏置类偏移视为具有高斯变分近似的随机变量，引入了一种受贝叶斯启发的后验代理，从而在不训练完整贝叶斯神经网络的情况下，诱导模型行为的分布。通过在序列级别冻结采样的噪声，B-Trans保持了每个生成内部的连贯性，从而在token之间强制执行时间一致性。B-Trans支持群体层面的决策，通过聚合采样个体的预测，显著增强了探索能力。在零样本生成、具有可验证奖励的强化学习（RLVR）以及没有显式标签的强化学习等实验中，B-Trans有效地利用了群体智慧，与确定性基线相比，在实现更好任务性能的同时，产生了卓越的语义多样性。

## 🔬 方法详解

**问题定义**：现有Transformer模型通常被训练成单一的确定性系统，即优化过程产生一组固定的参数，代表着关于数据的单一功能假设。这种单调性限制了模型在探索未知空间和处理不确定性方面的能力。尤其是在强化学习等任务中，缺乏多样性的模型难以有效地进行探索，从而影响最终的性能。

**核心思路**：本文的核心思路是将Transformer模型转化为贝叶斯模型，从而能够从单个预训练权重集中采样出多个具有不同行为的模型实例。通过引入模型参数的概率分布，B-Trans能够模拟“群体智慧”，即通过聚合多个模型的预测来提高决策的鲁棒性和准确性。

**技术框架**：B-Trans的核心在于将Transformer模型中的归一化层（Normalization Layer）的偏置项视为随机变量，并使用高斯变分近似来建模这些变量的后验分布。具体来说，对于每个归一化层，B-Trans引入一个可学习的均值和方差参数，用于定义高斯分布。在推理阶段，从这些高斯分布中采样偏置项，从而生成不同的模型实例。为了保证生成序列的连贯性，B-Trans在序列级别冻结采样的噪声，即对于同一个序列中的所有token，使用相同的偏置项。

**关键创新**：B-Trans的关键创新在于提出了一种轻量级的贝叶斯Transformer实现方法。与传统的贝叶斯神经网络相比，B-Trans不需要训练完整的概率模型，而是通过对归一化层偏置进行随机采样来近似后验分布，从而大大降低了计算成本。此外，B-Trans通过在序列级别冻结噪声，保证了生成序列的连贯性，避免了随机采样带来的不稳定性。

**关键设计**：B-Trans的关键设计包括：1) 使用高斯变分近似来建模归一化层偏置的后验分布；2) 在序列级别冻结采样的噪声，以保证生成序列的连贯性；3) 通过聚合多个模型实例的预测来进行决策，从而利用群体智慧。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.25063v1/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.25063v1/x2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.25063v1/x3.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

实验结果表明，B-Trans在零样本生成、具有可验证奖励的强化学习（RLVR）以及没有显式标签的强化学习等任务中，均取得了显著的性能提升。例如，在零样本生成任务中，B-Trans生成的文本具有更高的语义多样性。在强化学习任务中，B-Trans能够更快地学习到最优策略，并取得更高的奖励。

## 🎯 应用场景

B-Trans具有广泛的应用前景，例如可以应用于零样本生成、强化学习、对话系统等领域。在零样本生成中，B-Trans可以生成更多样化的文本内容。在强化学习中，B-Trans可以提高探索效率和策略的鲁棒性。在对话系统中，B-Trans可以生成更自然、更流畅的对话。

## 📄 摘要（原文）

> Despite their scale and success, modern transformers are almost universally trained as single-minded systems: optimization produces one deterministic set of parameters, representing a single functional hypothesis about the data. Motivated by the idea that intelligence emerge from many minds, we propose Population Bayesian Transformers (B-Trans), which transform a standard Large Language Model into a Bayesian Transformer model to supports sampling diverse yet coherent model instances from a single set of pre-trained weights.
>   B-Trans introduces a Bayesian-motivated posterior proxy by treating the bias-like offsets in normalization layers as stochastic variables with a Gaussian variational approximation, inducing a distribution over model behavior without the cost of training full Bayesian neural networks. Sampling from this proxy yields a set of model instances with diverse behaviors while maintaining general competence. To preserve coherence within each generation, we freeze the sampled noise at the sequence level, enforcing temporal consistency across tokens. B-Trans allows for population-level decision-making, where aggregating predictions across sampled individuals significantly enhances exploration. Experiments across zero-shot generation, Reinforcement Learning with Verifiable Rewards (RLVR), and RL without explicit labels demonstrate that B-Trans effectively leverage the wisdom of crowds, yielding superior semantic diversity while achieving better task performance compared to deterministic baselines.

