---
layout: default
title: Reward-Agnostic Prompt Optimization for Text-to-Image Diffusion Models
---

# Reward-Agnostic Prompt Optimization for Text-to-Image Diffusion Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.16853" class="toolbar-btn" target="_blank">📄 arXiv: 2506.16853v2</a>
  <a href="https://arxiv.org/pdf/2506.16853.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.16853v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.16853v2', 'Reward-Agnostic Prompt Optimization for Text-to-Image Diffusion Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Semin Kim, Yeonwoo Cha, Jaehoon Yoo, Seunghoon Hong

**分类**: cs.LG

**发布日期**: 2025-06-20 (更新: 2025-09-29)

**备注**: 29 pages, Under review

**🔗 代码/项目**: [GITHUB](https://github.com/seminkim/RATTPO)

---

## 💡 一句话要点

**提出RATTPO以解决文本到图像生成中的提示优化问题**

🎯 **匹配领域**: **支柱七：动作重定向 (Motion Retargeting)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `文本到图像生成` `提示优化` `扩散模型` `奖励无关` `自动提示工程` `多模态生成` `搜索效率`

## 📋 核心要点

1. 现有的自动提示工程方法通常针对特定的奖励配置，导致在不同奖励模型下的应用效果不佳。
2. 本文提出RATTPO方法，通过在测试时优化提示，能够适应多种奖励场景而无需修改。
3. 实验结果表明，RATTPO在搜索效率上显著优于其他基线，且在足够的推理预算下可与学习基线相媲美。

## 📝 摘要（中文）

本文研究了一种通用方法，通过在测试时寻找最大化奖励函数的提示，来改善文本到图像（T2I）扩散模型中的用户提示。现有的自动提示工程方法通常针对特定的奖励配置，导致在不同奖励模型下的应用效果不佳。为了解决这一问题，本文提出了RATTPO（奖励无关的测试时提示优化），该方法在不需要修改的情况下适用于各种奖励场景。RATTPO通过查询大型语言模型（LLMs）迭代搜索优化提示，使用优化轨迹和一种新颖的奖励感知反馈信号（称为“提示”）作为上下文。实验证明，RATTPO在多种奖励设置下有效提升用户提示，且在搜索效率上超越其他基线方法，平均运行速度比简单的奖励无关搜索基线快4.8倍。

## 🔬 方法详解

**问题定义**：本文要解决的问题是现有的自动提示工程方法在不同奖励模型下的适应性不足，导致生成效果不理想。

**核心思路**：RATTPO的核心思路是通过在测试时优化提示，利用大型语言模型进行迭代搜索，而不依赖于特定的奖励任务描述。

**技术框架**：RATTPO的整体架构包括提示生成模块、优化轨迹记录和奖励感知反馈信号生成。通过这些模块的协同工作，实现对用户提示的优化。

**关键创新**：RATTPO的主要创新在于其奖励无关的设计，使其能够在多种奖励场景下灵活应用，区别于现有方法的特定性。

**关键设计**：在参数设置上，RATTPO利用优化轨迹和反馈信号作为上下文信息，设计了高效的搜索策略，确保在不同奖励设置下的有效性。具体的损失函数和网络结构细节在论文中有详细描述。

## 📊 实验亮点

实验结果显示，RATTPO在搜索效率上超越其他基线，平均运行速度比简单的奖励无关搜索基线快4.8倍。此外，在足够的推理预算下，RATTPO的性能可与需要奖励特定微调的学习基线相媲美，展现出其强大的适应性和效率。

## 🎯 应用场景

该研究的潜在应用领域包括艺术创作、广告设计和游戏开发等，能够帮助用户生成更符合需求的图像。通过优化用户提示，RATTPO可以提升生成模型的实用性和灵活性，未来可能在多模态生成任务中发挥重要作用。

## 📄 摘要（原文）

> We investigate a general approach for improving user prompts in text-to-image (T2I) diffusion models by finding prompts that maximize a reward function specified at test-time. Although diverse reward models are used for evaluating image generation, existing automated prompt engineering methods typically target specific reward configurations. Consequently, these specialized designs exhibit suboptimal performance when applied to new prompt engineering scenarios involving different reward models. To address this limitation, we introduce RATTPO (Reward-Agnostic Test-Time Prompt Optimization), a flexible test-time optimization method applicable across various reward scenarios without modification. RATTPO iteratively searches for optimized prompts by querying large language models (LLMs) \textit{without} requiring reward-specific task descriptions. Instead, it uses the optimization trajectory and a novel reward-aware feedback signal (termed a "hint") as context. Empirical results demonstrate the versatility of RATTPO, effectively enhancing user prompts across diverse reward setups that assess various generation aspects, such as aesthetics, general human preference, or spatial relationships between objects. RATTPO surpasses other test-time search baselines in search efficiency, running 4.8 times faster than naive reward-agnostic test-time search baseline on average. Furthermore, with sufficient inference budget, it can achieve comparable performance to learning-based baselines that require reward-specific fine-tuning. The code is available at https://github.com/seminkim/RATTPO.

