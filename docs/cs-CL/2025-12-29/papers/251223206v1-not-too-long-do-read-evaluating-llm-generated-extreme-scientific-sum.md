---
layout: default
title: "Not too long do read: Evaluating LLM-generated extreme scientific summaries"
---

# Not too long do read: Evaluating LLM-generated extreme scientific summaries

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.23206" class="toolbar-btn" target="_blank">📄 arXiv: 2512.23206v1</a>
  <a href="https://arxiv.org/pdf/2512.23206.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.23206v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.23206v1', 'Not too long do read: Evaluating LLM-generated extreme scientific summaries')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zhuoqi Lyu, Qing Ke

**分类**: cs.CL, cs.AI

**发布日期**: 2025-12-29

**🔗 代码/项目**: [GITHUB](https://github.com/netknowledge/LLM_summarization)

---

## 💡 一句话要点

**提出BiomedTLDR数据集，评估大语言模型在生成科研论文极简摘要方面的能力**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大语言模型` `文本摘要` `科研摘要` `数据集构建` `自然语言处理`

## 📋 核心要点

1. 现有科研TLDR数据集的缺乏，限制了对LLM生成极简摘要能力的有效评估和提升。
2. 论文构建了BiomedTLDR数据集，包含研究人员撰写的摘要，用于训练和评估LLM。
3. 实验表明，LLM生成的摘要更倾向于抽取式，在词汇和结构上更依赖原文，与人类撰写存在差异。

## 📝 摘要（中文）

高质量的科研极简摘要（TLDR）有助于有效的科学传播。本文旨在评估大型语言模型（LLMs）在生成此类摘要方面的表现，并分析LLM生成的摘要与人类专家撰写的摘要之间的差异。由于缺乏全面、高质量的科研TLDR数据集，阻碍了LLMs摘要能力的开发和评估。为此，本文提出了一个新的数据集BiomedTLDR，其中包含大量研究人员撰写的科学论文摘要，该数据集利用了在参考文献条目旁边包含作者评论的常见做法。然后，我们测试了流行的开源LLMs，以基于摘要生成TLDR。分析表明，尽管其中一些模型成功生成了类人摘要，但与人类相比，LLMs通常更倾向于原始文本的词汇选择和修辞结构，因此总体上更偏向于抽取式而非生成式。

## 🔬 方法详解

**问题定义**：论文旨在解决缺乏高质量科研TLDR数据集的问题，并评估大型语言模型（LLMs）在生成此类摘要方面的能力。现有方法缺乏足够的数据支持，难以全面评估LLMs的摘要生成质量，也无法深入了解LLMs与人类专家在摘要生成策略上的差异。

**核心思路**：论文的核心思路是构建一个高质量的科研TLDR数据集BiomedTLDR，该数据集包含大量研究人员撰写的摘要，并利用这些数据来训练和评估LLMs的摘要生成能力。通过对比LLMs和人类专家生成的摘要，分析LLMs在词汇选择、修辞结构和摘要风格上的特点。

**技术框架**：论文的技术框架主要包括数据集构建和LLM评估两个部分。数据集构建方面，利用参考文献条目旁边的作者评论作为TLDR摘要的来源，构建BiomedTLDR数据集。LLM评估方面，选择流行的开源LLMs，基于论文摘要生成TLDR，并与人类专家撰写的摘要进行对比分析。

**关键创新**：论文的关键创新在于构建了BiomedTLDR数据集，该数据集为科研TLDR摘要生成任务提供了高质量的数据支持。此外，论文还深入分析了LLMs在摘要生成方面的特点，揭示了LLMs更倾向于抽取式摘要的倾向，这与人类专家的摘要风格存在差异。

**关键设计**：BiomedTLDR数据集的关键设计在于利用参考文献条目旁边的作者评论作为TLDR摘要的来源，这种方法能够有效地获取大量高质量的科研摘要。在LLM评估方面，论文选择了多个流行的开源LLMs，并采用了多种评估指标，包括ROUGE等，以全面评估LLMs的摘要生成质量。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.23206v1/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.23206v1/x2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.23206v1/x3.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

实验结果表明，虽然部分LLMs能够生成类人摘要，但总体而言，LLMs更倾向于原始文本的词汇选择和修辞结构，表现出更强的抽取式摘要倾向。与人类专家相比，LLMs在摘要生成方面仍有提升空间，尤其是在生成更具抽象性和概括性的摘要方面。

## 🎯 应用场景

该研究成果可应用于科学传播、科研信息检索和智能文献推荐等领域。高质量的科研TLDR摘要能够帮助研究人员快速了解论文的核心内容，提高科研效率。此外，该研究还可以促进LLMs在科研领域的应用，例如自动生成论文摘要、科研报告等。

## 📄 摘要（原文）

> High-quality scientific extreme summary (TLDR) facilitates effective science communication. How do large language models (LLMs) perform in generating them? How are LLM-generated summaries different from those written by human experts? However, the lack of a comprehensive, high-quality scientific TLDR dataset hinders both the development and evaluation of LLMs' summarization ability. To address these, we propose a novel dataset, BiomedTLDR, containing a large sample of researcher-authored summaries from scientific papers, which leverages the common practice of including authors' comments alongside bibliography items. We then test popular open-weight LLMs for generating TLDRs based on abstracts. Our analysis reveals that, although some of them successfully produce humanoid summaries, LLMs generally exhibit a greater affinity for the original text's lexical choices and rhetorical structures, hence tend to be more extractive rather than abstractive in general, compared to humans. Our code and datasets are available at https://github.com/netknowledge/LLM_summarization (Lyu and Ke, 2025).

