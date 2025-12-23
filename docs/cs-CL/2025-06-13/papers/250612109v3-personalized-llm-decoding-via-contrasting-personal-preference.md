---
layout: default
title: Personalized LLM Decoding via Contrasting Personal Preference
---

# Personalized LLM Decoding via Contrasting Personal Preference

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.12109" class="toolbar-btn" target="_blank">📄 arXiv: 2506.12109v3</a>
  <a href="https://arxiv.org/pdf/2506.12109.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.12109v3" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.12109v3', 'Personalized LLM Decoding via Contrasting Personal Preference')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Hyungjune Bu, Chanjoo Jung, Minjae Kang, Jaehyung Kim

**分类**: cs.CL, cs.AI

**发布日期**: 2025-06-13 (更新: 2025-11-24)

**备注**: EMNLP 2025 Main

---

## 💡 一句话要点

**提出CoPe以解决大语言模型个性化解码问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `个性化生成` `大语言模型` `解码算法` `奖励引导` `文本生成`

## 📋 核心要点

1. 现有的个性化大语言模型方法多集中于提示和训练，但解码时的算法开发仍显不足，限制了个性化效果的提升。
2. 本文提出的CoPe方法通过在用户特定数据上进行参数高效微调后，利用奖励引导解码来实现个性化，最大化用户的隐性奖励信号。
3. 实验结果显示，CoPe在五个个性化文本生成任务中表现优异，ROUGE-L指标平均提升10.57%，证明了其有效性。

## 📝 摘要（中文）

随着大语言模型（LLMs）在各种实际应用中的逐步部署，个性化变得愈发重要。尽管已有多种个性化方法被探索，但解码时算法的开发仍被忽视。本文提出了一种新颖的解码时方法CoPe（Contrasting Personal Preference），该方法在用户特定数据上进行参数高效微调后应用。我们的核心思想是通过最大化每个用户的隐性奖励信号，利用奖励引导解码进行个性化。我们在五个开放式个性化文本生成任务中评估了CoPe，实验证明其在ROUGE-L指标上平均提升了10.57%，且无需依赖外部奖励模型或额外训练过程。

## 🔬 方法详解

**问题定义**：本文旨在解决大语言模型在个性化解码时的不足，现有方法多集中于训练阶段，缺乏有效的解码时个性化策略，导致个性化效果不佳。

**核心思路**：CoPe方法的核心在于通过奖励引导解码，最大化每个用户的隐性奖励信号，从而实现个性化文本生成。此设计旨在提升用户体验，使生成内容更符合用户偏好。

**技术框架**：CoPe的整体架构包括两个主要阶段：首先在用户特定数据上进行参数高效微调（PEFT），然后在解码过程中应用奖励引导策略。该方法不依赖外部奖励模型，简化了个性化过程。

**关键创新**：CoPe的主要创新在于将奖励引导解码应用于个性化任务，区别于传统方法仅依赖训练阶段的优化，提供了一种新的解码时个性化策略。

**关键设计**：在具体实现中，CoPe设置了适应用户偏好的损失函数，并设计了适合个性化的解码策略，确保生成内容能够更好地反映用户的隐性需求。通过这些设计，CoPe在个性化生成任务中展现出显著的效果提升。

## 📊 实验亮点

实验结果显示，CoPe在五个开放式个性化文本生成任务中表现出色，ROUGE-L指标平均提升10.57%。这一提升在不依赖外部奖励模型或额外训练的情况下，展示了CoPe的有效性和创新性。

## 🎯 应用场景

该研究的潜在应用领域包括个性化聊天机器人、智能助手、内容推荐系统等。通过提升大语言模型的个性化能力，CoPe能够为用户提供更符合其需求的文本生成服务，增强用户体验，具有广泛的实际价值和未来影响。

## 📄 摘要（原文）

> As large language models (LLMs) are progressively deployed in various real-world applications, personalization of LLMs has become increasingly important. While various approaches to LLM personalization such as prompt-based and training-based methods have been actively explored, the development of effective decoding-time algorithms remains largely overlooked, despite their demonstrated potential. In this paper, we propose CoPe (Contrasting Personal Preference), a novel decoding-time approach applied after performing parameter-efficient fine-tuning (PEFT) on user-specific data. Our core idea is to leverage reward-guided decoding specifically for personalization by maximizing each user's implicit reward signal. We evaluate CoPe across five open-ended personalized text generation tasks. Our empirical results demonstrate that CoPe achieves strong performance, improving personalization by an average of 10.57% in ROUGE-L, without relying on external reward models or additional training procedures.

