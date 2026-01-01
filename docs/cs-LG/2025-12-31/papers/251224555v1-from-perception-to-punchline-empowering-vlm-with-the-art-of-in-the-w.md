---
layout: default
title: "From Perception to Punchline: Empowering VLM with the Art of In-the-wild Meme"
---

# From Perception to Punchline: Empowering VLM with the Art of In-the-wild Meme

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.24555" class="toolbar-btn" target="_blank">📄 arXiv: 2512.24555v1</a>
  <a href="https://arxiv.org/pdf/2512.24555.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.24555v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.24555v1', 'From Perception to Punchline: Empowering VLM with the Art of In-the-wild Meme')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Xueyan Li, Yingyi Xue, Mengjie Jiang, Qingzi Zhu, Yazhe Niu

**分类**: cs.LG

**发布日期**: 2025-12-31

**备注**: 46 pages, 20 figures

---

## 💡 一句话要点

**提出HUMOR框架，赋能VLM生成更幽默、符合人类偏好的野生表情包**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱六：视频提取与匹配 (Video Extraction)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `表情包生成` `视觉语言模型` `思维链` `强化学习` `人类偏好` `多模态学习` `幽默感` `群体智能`

## 📋 核心要点

1. 现有表情包生成方法难以捕捉视觉内容、上下文和主观幽默之间的复杂关系，缺乏细致的推理能力。
2. HUMOR框架通过分层多路径思维链引导VLM进行推理，并使用成对奖励模型对齐人类偏好，提升幽默感。
3. 实验表明，HUMOR框架显著提升了VLM在表情包生成任务中的推理多样性、偏好对齐和整体质量。

## 📝 摘要（中文）

生成幽默表情包是一项具有挑战性的多模态任务，它超越了直接的图像到标题的监督。它需要对视觉内容、上下文线索和主观幽默进行细致的推理。为了弥合视觉感知和幽默妙语创作之间的差距，我们提出了HUMOR，这是一个新颖的框架，通过分层推理引导视觉语言模型（VLM），并使其与群体人类偏好对齐。首先，HUMOR采用分层的多路径思维链（CoT）：模型首先识别模板级别的意图，然后探索不同上下文下的多样化推理路径，最后锚定到高质量、特定于上下文的路径。这种从真实标题追溯的CoT监督增强了推理多样性。我们进一步分析，在高质量路径保留显著概率质量的实际条件下，这种具有锚定的多路径探索保持了较高的预期幽默质量。其次，为了捕捉主观幽默，我们训练了一个成对奖励模型，该模型在共享相同模板的表情包组内运行。根据既定理论，即使存在主观和嘈杂的标签，这种方法也能确保人类偏好的一致且稳健的代理。然后，奖励模型支持组内强化学习优化，从而为信任区域内的单调改进提供理论保证。大量实验表明，HUMOR使各种VLM具有卓越的推理多样性、更可靠的偏好对齐和更高的整体表情包质量。除了表情包之外，我们的工作还提出了一种通用的训练范式，用于开放式、人类对齐的多模态生成，其中成功由连贯输出组内的比较判断来指导。

## 🔬 方法详解

**问题定义**：表情包生成任务需要模型理解图像内容、捕捉上下文信息，并生成具有幽默感的文字。现有的方法通常采用图像到文本的直接监督，缺乏对幽默感和人类偏好的建模，导致生成的表情包质量不高，难以引起共鸣。此外，主观幽默的建模也是一个挑战，因为不同的人对同一表情包的幽默程度可能有不同的看法。

**核心思路**：HUMOR框架的核心思路是通过分层推理和群体偏好学习来提升表情包的幽默感和质量。首先，利用分层多路径思维链（CoT）引导VLM进行推理，增强推理的多样性。然后，通过成对奖励模型学习人类对幽默的主观偏好，并利用强化学习优化生成策略，使生成的表情包更符合人类的期望。

**技术框架**：HUMOR框架主要包含两个阶段：1) 分层多路径思维链推理：首先，模型识别表情包的模板意图；然后，在不同的上下文下探索多条推理路径；最后，选择一条高质量的、特定于上下文的路径。2) 基于群体偏好的强化学习：训练一个成对奖励模型，用于评估表情包的幽默程度；然后，利用强化学习算法，根据奖励模型的反馈，优化VLM的生成策略。

**关键创新**：HUMOR框架的关键创新在于：1) 提出了分层多路径思维链，增强了VLM的推理多样性，使其能够生成更具创意的表情包。2) 引入了基于群体偏好的奖励模型，能够更好地捕捉主观幽默，使生成的表情包更符合人类的偏好。3) 采用组内强化学习优化，保证了在信任区域内的单调改进。

**关键设计**：在分层多路径思维链中，模型首先识别模板级别的意图，例如“嘲讽”、“惊讶”等。然后，模型在不同的上下文下探索多条推理路径，例如“如果图像是猫，那么可以生成‘猫：我每天都在努力工作’的文字”。最后，模型选择一条高质量的、特定于上下文的路径，生成最终的表情包。在基于群体偏好的强化学习中，奖励模型采用pairwise ranking loss进行训练，用于评估表情包的幽默程度。强化学习算法采用PPO，优化VLM的生成策略。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.24555v1/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.24555v1/x2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.24555v1/x3.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

实验结果表明，HUMOR框架在表情包生成任务中取得了显著的性能提升。相比于基线方法，HUMOR框架生成的表情包在幽默感、相关性和整体质量方面均有明显提高。具体来说，HUMOR框架在人工评估中获得了更高的评分，并且在客观指标上也表现出更好的性能。

## 🎯 应用场景

该研究成果可应用于智能对话系统、社交媒体内容生成、广告创意设计等领域。通过生成更幽默、更符合人类偏好的内容，可以提升用户体验，增强用户粘性，并创造更大的商业价值。未来，该方法有望扩展到其他开放式、人类对齐的多模态生成任务中。

## 📄 摘要（原文）

> Generating humorous memes is a challenging multimodal task that moves beyond direct image-to-caption supervision. It requires a nuanced reasoning over visual content, contextual cues, and subjective humor. To bridge this gap between visual perception and humorous punchline creation, we propose HUMOR}, a novel framework that guides VLMs through hierarchical reasoning and aligns them with group-wise human preferences. First, HUMOR employs a hierarchical, multi-path Chain-of-Thought (CoT): the model begins by identifying a template-level intent, then explores diverse reasoning paths under different contexts, and finally anchors onto a high-quality, context-specific path. This CoT supervision, which traces back from ground-truth captions, enhances reasoning diversity. We further analyze that this multi-path exploration with anchoring maintains a high expected humor quality, under the practical condition that high-quality paths retain significant probability mass. Second, to capture subjective humor, we train a pairwise reward model that operates within groups of memes sharing the same template. Following established theory, this approach ensures a consistent and robust proxy for human preference, even with subjective and noisy labels. The reward model then enables a group-wise reinforcement learning optimization, guaranteeing providing a theoretical guarantee for monotonic improvement within the trust region. Extensive experiments show that HUMOR empowers various VLMs with superior reasoning diversity, more reliable preference alignment, and higher overall meme quality. Beyond memes, our work presents a general training paradigm for open-ended, human-aligned multimodal generation, where success is guided by comparative judgment within coherent output group.

