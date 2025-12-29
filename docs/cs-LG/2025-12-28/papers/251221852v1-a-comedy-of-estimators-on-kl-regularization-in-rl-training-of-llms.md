---
layout: default
title: "A Comedy of Estimators: On KL Regularization in RL Training of LLMs"
---

# A Comedy of Estimators: On KL Regularization in RL Training of LLMs

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.21852" class="toolbar-btn" target="_blank">📄 arXiv: 2512.21852v1</a>
  <a href="https://arxiv.org/pdf/2512.21852.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.21852v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.21852v1', 'A Comedy of Estimators: On KL Regularization in RL Training of LLMs')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Vedant Shah, Johan Obando-Ceron, Vineet Jain, Brian Bartoldson, Bhavya Kailkhura, Sarthak Mittal, Glen Berseth, Pablo Samuel Castro, Yoshua Bengio, Nikolay Malkin, Moksh Jain, Siddarth Venkatraman, Aaron Courville

**分类**: cs.LG, cs.AI

**发布日期**: 2025-12-26

---

## 💡 一句话要点

**研究KL散度估计器对LLM的RL训练影响，提升模型在分布内外的泛化性能。**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `强化学习` `大型语言模型` `KL散度` `梯度偏差` `策略优化`

## 📋 核心要点

1. 现有LLM的RL训练中，KL散度估计不准确导致梯度偏差，影响模型性能和训练稳定性。
2. 分析不同KL散度估计器的梯度偏差，并提出使用无偏梯度估计器来优化RL训练过程。
3. 实验表明，使用无偏梯度估计器能提升LLM在分布内和分布外任务上的性能，并稳定训练。

## 📝 摘要（中文）

大型语言模型（LLM）的推理性能可以通过强化学习（RL）训练得到显著提升。LLM训练的RL目标包含一个正则化项，即训练策略与参考策略之间的反向Kullback-Leibler（KL）散度。由于精确计算KL散度是难以实现的，因此实践中通常使用各种估计器从on-policy样本中对其进行估计。尽管KL散度估计器被广泛采用，包括在多个开源库中，但目前还没有系统的研究来分析将KL估计器纳入目标函数的各种方式及其对RL训练模型下游性能的影响。最近的研究表明，目前采用的KL正则化方法并没有为既定目标提供正确的梯度，从而在目标函数和实现之间造成了差异。在本文中，我们进一步分析了这些实践，并研究了几种估计器配置的梯度，揭示了设计选择如何影响梯度偏差。我们通过使用不同的配置对	exttt{Qwen2.5-7B}、	exttt{Llama-3.1-8B-Instruct}和	exttt{Qwen3-4B-Instruct-2507}进行RL微调，并在分布内和分布外任务上评估其性能，从而证实了这些发现。通过我们的分析，我们观察到，在on-policy设置中：（1）具有偏差梯度的估计器配置可能导致训练不稳定；（2）使用产生无偏梯度的估计器配置可以提高在域内和域外任务上的性能。我们还研究了在off-policy设置中不同KL配置所产生的性能，并观察到KL正则化可以帮助稳定由异步设置导致的off-policy RL训练。

## 🔬 方法详解

**问题定义**：论文旨在解决大型语言模型（LLM）通过强化学习（RL）进行训练时，由于KL散度估计不准确而导致的训练不稳定和性能下降问题。现有的KL散度估计方法存在梯度偏差，使得实际优化目标与理论目标不一致，从而影响模型的泛化能力和训练过程的稳定性。

**核心思路**：论文的核心思路是通过分析不同KL散度估计器的梯度偏差，找到能够产生无偏梯度的估计器配置，并将其应用于LLM的RL训练中。通过使用无偏梯度，可以更准确地优化RL目标，从而提高模型的性能和训练稳定性。论文还研究了在off-policy设置下KL正则化的作用，发现它可以帮助稳定异步设置下的RL训练。

**技术框架**：论文的技术框架主要包括以下几个部分：1) 分析不同KL散度估计器的梯度偏差；2) 设计实验，使用不同的KL估计器配置对LLM进行RL微调；3) 在分布内和分布外任务上评估微调后的模型性能；4) 研究KL正则化在off-policy RL训练中的作用。主要模块包括KL散度估计模块、RL训练模块和性能评估模块。

**关键创新**：论文最重要的技术创新点在于对不同KL散度估计器的梯度偏差进行了深入分析，并揭示了梯度偏差对LLM的RL训练的影响。此外，论文还提出了使用无偏梯度估计器来优化RL训练过程，并验证了其有效性。与现有方法相比，该方法能够更准确地优化RL目标，从而提高模型的性能和训练稳定性。

**关键设计**：论文的关键设计包括：1) 选择合适的KL散度估计器，例如使用能够产生无偏梯度的估计器；2) 设计合适的RL训练目标，包括奖励函数和KL正则化系数；3) 选择合适的LLM架构和数据集进行实验；4) 使用分布内和分布外任务来评估模型的泛化能力；5) 在off-policy设置下研究KL正则化的作用。

## 📊 实验亮点

实验结果表明，使用无偏梯度估计器配置进行RL微调后，LLM在分布内和分布外任务上的性能均得到提升。具体而言，使用无偏梯度估计器能够稳定训练过程，并使模型在未见过的任务上表现更好。例如，在特定任务上，模型性能提升了X%，证明了无偏梯度估计器的有效性。

## 🎯 应用场景

该研究成果可应用于提升各种大型语言模型的推理能力和泛化性能，尤其是在需要通过强化学习进行微调的场景中。例如，可以用于优化对话系统、文本生成模型和代码生成模型，提高它们在实际应用中的表现和鲁棒性。此外，该研究对于开发更稳定和高效的LLM训练方法具有重要意义。

## 📄 摘要（原文）

> The reasoning performance of large language models (LLMs) can be substantially improved by training them with reinforcement learning (RL). The RL objective for LLM training involves a regularization term, which is the reverse Kullback-Leibler (KL) divergence between the trained policy and the reference policy. Since computing the KL divergence exactly is intractable, various estimators are used in practice to estimate it from on-policy samples. Despite its wide adoption, including in several open-source libraries, there is no systematic study analyzing the numerous ways of incorporating KL estimators in the objective and their effect on the downstream performance of RL-trained models. Recent works show that prevailing practices for incorporating KL regularization do not provide correct gradients for stated objectives, creating a discrepancy between the objective and its implementation. In this paper, we further analyze these practices and study the gradients of several estimators configurations, revealing how design choices shape gradient bias. We substantiate these findings with empirical observations by RL fine-tuning \texttt{Qwen2.5-7B}, \texttt{Llama-3.1-8B-Instruct} and \texttt{Qwen3-4B-Instruct-2507} with different configurations and evaluating their performance on both in- and out-of-distribution tasks. Through our analysis, we observe that, in on-policy settings: (1) estimator configurations with biased gradients can result in training instabilities; and (2) using estimator configurations resulting in unbiased gradients leads to better performance on in-domain as well as out-of-domain tasks. We also investigate the performance resulting from different KL configurations in off-policy settings and observe that KL regularization can help stabilize off-policy RL training resulting from asynchronous setups.

