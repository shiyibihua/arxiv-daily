---
layout: default
title: Captioning for Text-Video Retrieval via Dual-Group Direct Preference Optimization
---

# Captioning for Text-Video Retrieval via Dual-Group Direct Preference Optimization

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.16560" class="toolbar-btn" target="_blank">📄 arXiv: 2509.16560v1</a>
  <a href="https://arxiv.org/pdf/2509.16560.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.16560v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.16560v1', 'Captioning for Text-Video Retrieval via Dual-Group Direct Preference Optimization')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Ji Soo Lee, Byungoh Ko, Jaewon Cho, Howoong Lee, Jaewoon Byun, Hyunwoo J. Kim

**分类**: cs.CV

**发布日期**: 2025-09-20

**备注**: EMNLP 2025 Findings

**🔗 代码/项目**: [GITHUB](https://github.com/mlvlab/CaReDPO)

---

## 💡 一句话要点

**提出CaRe-DPO框架，通过双组直接偏好优化提升文本-视频检索中字幕生成质量。**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `文本-视频检索` `字幕生成` `多模态学习` `直接偏好优化` `双组优化` `MLLM` `角色嵌入`

## 📋 核心要点

1. 现有MLLM生成的字幕在文本-视频检索中存在通用性问题，难以区分视觉相似的视频，限制了细粒度检索的性能。
2. 提出CaRe-DPO框架，核心是双组直接偏好优化(DG-DPO)，通过建模不同视频-字幕对的偏好来优化字幕生成。
3. 实验结果表明，CaRe-DPO能有效利用辅助知识生成细粒度字幕，显著提升文本-视频检索的性能。

## 📝 摘要（中文）

在文本-视频检索中，辅助字幕常被用于增强视频理解，弥合模态间的差距。尽管多模态大型语言模型(MLLM)的最新进展实现了强大的零样本字幕生成，但我们观察到这些字幕往往是通用的，并且在视觉上相似的视频中难以区分，从而限制了它们在细粒度检索中的效用。此外，传统的字幕生成方法通常使用语言生成指标（如BLEU）进行评估，这些指标通常不是为需要区分候选者的检索任务量身定制的。为了解决这个问题，我们提出了CaRe-DPO，一个通过使用检索相关性分数直接优化字幕生成的检索框架。其核心是双组直接偏好优化(DG-DPO)，这是一种新颖的学习策略，通过对不同视频和字幕对组之间的偏好进行建模来监督字幕生成。此外，我们提出了一个基于MLLM的检索模型，该模型结合了角色嵌入，以更好地区分具有不同功能角色的文本输入，例如辅助字幕和文本查询。通过大量的实验，我们证明了CaRe-DPO通过有效地利用辅助知识来生成用于检索的细粒度字幕，从而显著提高了检索性能。

## 🔬 方法详解

**问题定义**：论文旨在解决文本-视频检索任务中，现有方法生成的辅助字幕泛化性强，难以区分视觉相似视频的问题。传统字幕生成方法使用BLEU等语言生成指标评估，与检索任务的需求不匹配，无法有效提升检索性能。

**核心思路**：论文的核心思路是直接利用检索相关性分数来优化字幕生成过程。通过学习不同视频-字幕对之间的偏好关系，使得生成的字幕更具区分性，从而提升检索效果。这种方法避免了传统字幕生成指标与检索任务目标不一致的问题。

**技术框架**：CaRe-DPO框架包含两个主要组成部分：字幕生成器和检索模型。字幕生成器基于MLLM，负责生成视频的辅助字幕。检索模型则用于计算文本查询与视频（及其辅助字幕）之间的相关性。DG-DPO作为核心学习策略，用于优化字幕生成器，使其生成的字幕更符合检索任务的需求。整体流程是：首先，使用DG-DPO优化字幕生成器；然后，使用优化后的字幕生成器为视频生成辅助字幕；最后，使用检索模型进行文本-视频检索。

**关键创新**：论文的关键创新在于提出了双组直接偏好优化(DG-DPO)策略。DG-DPO通过建模不同视频和字幕对组之间的偏好关系，直接优化字幕生成过程，使其生成的字幕更具区分性，从而提升检索性能。此外，论文还提出了一个基于MLLM的检索模型，该模型结合了角色嵌入，以更好地区分具有不同功能角色的文本输入（例如辅助字幕和文本查询）。

**关键设计**：DG-DPO的具体实现细节未知，但可以推测其损失函数的设计是基于不同视频-字幕对的检索得分差异。通过最大化正样本对的检索得分，同时最小化负样本对的检索得分，从而学习到更具区分性的字幕生成策略。角色嵌入的具体实现方式也未知，但其目的是为了区分文本查询和辅助字幕在检索模型中的作用。

## 📊 实验亮点

论文提出的CaRe-DPO框架通过实验验证了其有效性，显著提升了文本-视频检索的性能。具体的性能数据和对比基线在论文中给出，但摘要中未明确提及具体的提升幅度。实验结果表明，CaRe-DPO能够生成更具区分性的字幕，从而更好地利用辅助知识进行检索。

## 🎯 应用场景

该研究成果可应用于视频搜索引擎、智能视频推荐系统、视频内容理解等领域。通过生成更具区分性的视频字幕，可以提升检索和推荐的准确性，改善用户体验。未来，该方法有望扩展到其他多模态检索任务中，例如图像-文本检索。

## 📄 摘要（原文）

> In text-video retrieval, auxiliary captions are often used to enhance video understanding, bridging the gap between the modalities. While recent advances in multi-modal large language models (MLLMs) have enabled strong zero-shot caption generation, we observe that such captions tend to be generic and indistinguishable across visually similar videos, limiting their utility for fine-grained retrieval. Moreover, conventional captioning approaches are typically evaluated using language generation metrics, such as BLEU, which are not typically tailored for retrieval tasks that require making discriminative distinctions between candidates. To address this, we propose $\textbf{CaRe-DPO}$, a retrieval framework that directly optimizes caption generation using retrieval relevance scores. At its core is Dual-Group Direct Preference Optimization (DG-DPO), a novel learning strategy that supervises captioning by modeling preferences across groups of distinct video and caption pairs. In addition, we present an MLLM-based retrieval model that incorporates role-embeddings to better distinguish between textual inputs with different functional roles, such as an auxiliary caption and a text query. Through extensive experiments, we demonstrate that CaRe-DPO significantly enhances retrieval performance by effectively leveraging auxiliary knowledge to generate fine-grained captions for retrieval. Code is available at https://github.com/mlvlab/CaReDPO.

