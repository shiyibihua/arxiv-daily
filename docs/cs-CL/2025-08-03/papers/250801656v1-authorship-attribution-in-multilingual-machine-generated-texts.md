---
layout: default
title: Authorship Attribution in Multilingual Machine-Generated Texts
---

# Authorship Attribution in Multilingual Machine-Generated Texts

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.01656" class="toolbar-btn" target="_blank">📄 arXiv: 2508.01656v1</a>
  <a href="https://arxiv.org/pdf/2508.01656.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.01656v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.01656v1', 'Authorship Attribution in Multilingual Machine-Generated Texts')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Lucio La Cava, Dominik Macko, Róbert Móro, Ivan Srba, Andrea Tagarelli

**分类**: cs.CL, cs.AI, cs.CY, cs.HC, physics.soc-ph

**发布日期**: 2025-08-03

---

## 💡 一句话要点

**提出多语言作者归属方法以解决机器生成文本识别问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `作者归属` `机器生成文本` `多语言处理` `大型语言模型` `文本分析` `信息验证` `社交媒体监控`

## 📋 核心要点

1. 现有的作者归属方法主要集中在单语环境，缺乏对多语言文本的有效处理，限制了其应用范围。
2. 本文提出了多语言作者归属的概念，旨在识别多种语言中人类与LLM生成的文本，扩展了现有研究的边界。
3. 实验结果显示，尽管某些单语方法可适应多语言设置，但在不同语言家族间的迁移能力仍然有限，需进一步研究。

## 📝 摘要（中文）

随着大型语言模型（LLMs）达到人类般的流畅性和连贯性，区分机器生成文本（MGT）与人类撰写内容变得愈加困难。早期的MGT检测主要集中于二分类，而随着LLMs的多样性，作者归属（AA）问题变得更加复杂。本文引入了多语言作者归属问题，旨在识别文本背后的生成者（人类或多种LLM），并覆盖18种语言和8个生成器。研究表明，尽管某些单语AA方法可以适应多语言环境，但在不同语言家族间的迁移仍面临显著挑战，强调了多语言AA的复杂性和对更强大方法的需求。

## 🔬 方法详解

**问题定义**：本文旨在解决多语言环境下的作者归属问题，现有方法主要局限于单一语言，无法有效处理多样化的LLM生成文本。

**核心思路**：通过引入多语言作者归属的框架，识别文本背后的生成者，考虑多种语言和生成器的影响，以适应现代LLM的多样性。

**技术框架**：研究涵盖18种语言和8个生成器，采用单语AA方法的适应性分析，评估其在多语言环境中的表现和迁移能力。

**关键创新**：提出了多语言作者归属的概念，强调了不同语言家族间的迁移挑战，推动了该领域的研究进展。

**关键设计**：在实验中，采用了多种单语AA方法，并对其在多语言设置下的表现进行了系统评估，关注生成器对归属性能的影响。

## 📊 实验亮点

实验结果表明，尽管某些单语AA方法在多语言环境中表现出一定的适应性，但在不同语言家族间的迁移能力仍显不足，强调了多语言作者归属的复杂性。具体数据未提供，需进一步研究以优化现有方法。

## 🎯 应用场景

该研究的潜在应用领域包括内容审核、信息验证和社交媒体监控等，能够帮助识别和追踪机器生成内容的来源，提升信息的可信度和透明度。未来，随着LLM技术的不断发展，该方法将对多语言环境下的文本分析和处理产生深远影响。

## 📄 摘要（原文）

> As Large Language Models (LLMs) have reached human-like fluency and coherence, distinguishing machine-generated text (MGT) from human-written content becomes increasingly difficult. While early efforts in MGT detection have focused on binary classification, the growing landscape and diversity of LLMs require a more fine-grained yet challenging authorship attribution (AA), i.e., being able to identify the precise generator (LLM or human) behind a text. However, AA remains nowadays confined to a monolingual setting, with English being the most investigated one, overlooking the multilingual nature and usage of modern LLMs. In this work, we introduce the problem of Multilingual Authorship Attribution, which involves attributing texts to human or multiple LLM generators across diverse languages. Focusing on 18 languages -- covering multiple families and writing scripts -- and 8 generators (7 LLMs and the human-authored class), we investigate the multilingual suitability of monolingual AA methods, their cross-lingual transferability, and the impact of generators on attribution performance. Our results reveal that while certain monolingual AA methods can be adapted to multilingual settings, significant limitations and challenges remain, particularly in transferring across diverse language families, underscoring the complexity of multilingual AA and the need for more robust approaches to better match real-world scenarios.

