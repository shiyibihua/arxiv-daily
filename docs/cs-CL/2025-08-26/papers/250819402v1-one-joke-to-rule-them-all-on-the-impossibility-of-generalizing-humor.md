---
layout: default
title: One Joke to Rule them All? On the (Im)possibility of Generalizing Humor
---

# One Joke to Rule them All? On the (Im)possibility of Generalizing Humor

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.19402" class="toolbar-btn" target="_blank">📄 arXiv: 2508.19402v1</a>
  <a href="https://arxiv.org/pdf/2508.19402.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.19402v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.19402v1', 'One Joke to Rule them All? On the (Im)possibility of Generalizing Humor')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Mor Turgeman, Chen Shani, Dafna Shahaf

**分类**: cs.CL, cs.AI

**发布日期**: 2025-08-26

---

## 💡 一句话要点

**提出幽默类型迁移学习方法以解决幽默理解问题**

🎯 **匹配领域**: **支柱六：视频提取与匹配 (Video Extraction)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `幽默理解` `迁移学习` `大语言模型` `社交媒体` `数据集`

## 📋 核心要点

1. 现有的幽默理解研究通常集中于特定类型，缺乏对幽默类型间迁移能力的探讨。
2. 本研究通过迁移学习实验，探讨在不同幽默任务间的知识迁移能力，旨在提升大语言模型的幽默理解能力。
3. 实验结果表明，模型在未见数据集上可达到75%的准确率，且多样化训练源提升了迁移能力，表现出幽默类型间的关系。

## 📝 摘要（中文）

幽默是一种广泛而复杂的交流形式，机器理解幽默仍然面临挑战。尽管已有研究集中于特定幽默类型的建模，但本研究旨在探讨在特定幽默任务上的能力是否能够迁移到新的、未见过的幽默类型。为此，研究团队进行了多项迁移学习实验，使用四个不同的幽默任务数据集进行训练，结果显示模型在未见数据集上可达到75%的准确率，且在多样化数据源训练下，迁移能力有所提升。研究还发现，父亲笑话在迁移中表现最佳，但其本身的迁移难度较大。研究团队发布了相关数据和代码。

## 🔬 方法详解

**问题定义**：本研究旨在解决机器在幽默理解中的迁移能力问题，现有方法往往局限于特定幽默类型，难以适应新兴幽默形式。

**核心思路**：通过迁移学习实验，探索在不同幽默任务间的知识迁移，验证大语言模型是否能够捕捉幽默的深层机制。

**技术框架**：研究使用四个不同的幽默任务数据集进行训练，模型在1-3个数据集上进行训练，并在新的幽默任务上进行测试。

**关键创新**：本研究的创新点在于通过多样化的数据源训练提升模型的迁移能力，发现父亲笑话在迁移中表现最佳，但其本身的迁移难度较高。

**关键设计**：实验中设置了多样化的训练数据源，评估了模型在不同幽默任务上的表现，采用了标准的准确率作为性能指标。实验结果显示，模型在未见数据集上可达到75%的准确率，且多样化训练源提升了1.88-4.05%的迁移能力。

## 📊 实验亮点

实验结果显示，模型在未见数据集上可达到75%的准确率，且通过多样化训练源，迁移能力提升了1.88-4.05%。特别是父亲笑话在迁移中表现最佳，尽管其本身的迁移难度较高，这一发现为幽默理解提供了新的视角。

## 🎯 应用场景

该研究的潜在应用领域包括社交媒体内容生成、在线幽默推荐系统以及人机交互中的幽默理解。通过提升机器对幽默的理解能力，可以改善用户体验，增强人机互动的自然性和趣味性。未来，该研究可能推动幽默生成和理解技术的进一步发展，适应不断变化的网络文化。

## 📄 摘要（原文）

> Humor is a broad and complex form of communication that remains challenging for machines. Despite its broadness, most existing research on computational humor traditionally focused on modeling a specific type of humor. In this work, we wish to understand whether competence on one or more specific humor tasks confers any ability to transfer to novel, unseen types; in other words, is this fragmentation inevitable? This question is especially timely as new humor types continuously emerge in online and social media contexts (e.g., memes, anti-humor, AI fails). If Large Language Models (LLMs) are to keep up with this evolving landscape, they must be able to generalize across humor types by capturing deeper, transferable mechanisms. To investigate this, we conduct a series of transfer learning experiments across four datasets, representing different humor tasks. We train LLMs under varied diversity settings (1-3 datasets in training, testing on a novel task). Experiments reveal that models are capable of some transfer, and can reach up to 75% accuracy on unseen datasets; training on diverse sources improves transferability (1.88-4.05%) with minimal-to-no drop in in-domain performance. Further analysis suggests relations between humor types, with Dad Jokes surprisingly emerging as the best enabler of transfer (but is difficult to transfer to). We release data and code.

