---
layout: default
title: Lexical Hints of Accuracy in LLM Reasoning Chains
---

# Lexical Hints of Accuracy in LLM Reasoning Chains

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.15842" class="toolbar-btn" target="_blank">📄 arXiv: 2508.15842v1</a>
  <a href="https://arxiv.org/pdf/2508.15842.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.15842v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.15842v1', 'Lexical Hints of Accuracy in LLM Reasoning Chains')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Arne Vanhoyweghen, Brecht Verbeken, Andres Algaba, Vincent Ginis

**分类**: cs.CL, cs.LG

**发布日期**: 2025-08-19

**备注**: 21 pages, 7 figures, 6 tables

---

## 💡 一句话要点

**提出词汇提示以提高大型语言模型推理链的准确性**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `推理链` `自信度校准` `不确定性指标` `情感分析`

## 📋 核心要点

1. 现有方法在低准确率基准测试中表现不佳，且自信度校准不足，导致错误预测频繁。
2. 论文提出通过分析推理链中的特征，如长度和情感波动，来评估LLM的内部信心，从而提高预测准确性。
3. 实验结果表明，不确定性词汇是错误响应的强指示，而推理链长度在中等难度基准中有效，提升了模型的可靠性。

## 📝 摘要（中文）

通过强化学习微调大型语言模型（LLMs），在回答前生成明确的推理链（CoT），能显著提升其在代码、数学和常识基准测试中的整体表现。然而，在一些准确率较低的基准测试中，如人类最后考试（HLE），LLMs常常报告高自信度，反映出其校准不佳。本文测试了推理链的可测量特性是否能可靠地反映LLM对答案的内部信心。我们分析了三类特征：推理链长度、推理链内部情感波动和词汇提示，包括模糊词。研究发现，推理链中的不确定性词汇是错误响应的强指示，而情感变化提供了较弱但互补的信号。推理链长度在中等难度基准中有预测能力，但在HLE中则无效，表明推理链长度仅在模型能力范围内有效。最后，我们发现推理链中的不确定性指标比高自信度标记更显著，使得错误预测更为容易。

## 🔬 方法详解

**问题定义**：本文旨在解决大型语言模型在低准确率基准测试中自信度校准不足的问题，现有方法无法有效反映模型的真实信心。

**核心思路**：通过分析推理链中的特征（如长度、情感波动和词汇提示），提供一种可靠的信心评估信号，以辅助模型的决策过程。

**技术框架**：整体架构包括数据收集、特征提取和模型评估三个主要模块。首先收集推理链数据，然后提取相关特征，最后通过实验验证特征与模型表现的关系。

**关键创新**：本研究的关键创新在于识别推理链中的不确定性词汇作为错误预测的强指示，这一发现与现有方法的自信度评估机制形成鲜明对比。

**关键设计**：在特征提取中，重点关注推理链长度、情感波动和模糊词的使用，采用适当的损失函数来优化模型的表现，并确保模型在不同难度基准上的适应性。

## 📊 实验亮点

实验结果显示，推理链中的不确定性词汇（如'guess'、'stuck'、'hard'）是错误响应的最强指示，而推理链长度在中等难度基准（Omni-MATH）中有效，准确率达到约70%。在更难的基准（HLE）中，准确率仅为约9%，表明该方法在不同难度下的表现差异。

## 🎯 应用场景

该研究的潜在应用领域包括教育评估、自动化问答系统和智能助手等。通过提高大型语言模型的预测准确性和信心校准，可以在实际应用中减少错误响应，提升用户体验和信任度。未来，该方法可能推动更安全的LLM部署，尤其是在高风险场景中。

## 📄 摘要（原文）

> Fine-tuning Large Language Models (LLMs) with reinforcement learning to produce an explicit Chain-of-Thought (CoT) before answering produces models that consistently raise overall performance on code, math, and general-knowledge benchmarks. However, on benchmarks where LLMs currently achieve low accuracy, such as Humanity's Last Exam (HLE), they often report high self-confidence, reflecting poor calibration. Here, we test whether measurable properties of the CoT provide reliable signals of an LLM's internal confidence in its answers. We analyze three feature classes: (i) CoT length, (ii) intra-CoT sentiment volatility, and (iii) lexicographic hints, including hedging words. Using DeepSeek-R1 and Claude 3.7 Sonnet on both Humanity's Last Exam (HLE), a frontier benchmark with very low accuracy, and Omni-MATH, a saturated benchmark of moderate difficulty, we find that lexical markers of uncertainty (e.g., $\textit{guess}$, $\textit{stuck}$, $\textit{hard}$) in the CoT are the strongest indicators of an incorrect response, while shifts in the CoT sentiment provide a weaker but complementary signal. CoT length is informative only on Omni-MATH, where accuracy is already high ($\approx 70\%$), and carries no signal on the harder HLE ($\approx 9\%$), indicating that CoT length predicts correctness only in the intermediate-difficulty benchmarks, i.e., inside the model's demonstrated capability, but still below saturation. Finally, we find that uncertainty indicators in the CoT are consistently more salient than high-confidence markers, making errors easier to predict than correct responses. Our findings support a lightweight post-hoc calibration signal that complements unreliable self-reported probabilities and supports safer deployment of LLMs.

