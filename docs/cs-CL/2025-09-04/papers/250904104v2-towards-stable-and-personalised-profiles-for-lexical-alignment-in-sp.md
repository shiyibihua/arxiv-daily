---
layout: default
title: Towards Stable and Personalised Profiles for Lexical Alignment in Spoken Human-Agent Dialogue
---

# Towards Stable and Personalised Profiles for Lexical Alignment in Spoken Human-Agent Dialogue

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.04104" class="toolbar-btn" target="_blank">📄 arXiv: 2509.04104v2</a>
  <a href="https://arxiv.org/pdf/2509.04104.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.04104v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.04104v2', 'Towards Stable and Personalised Profiles for Lexical Alignment in Spoken Human-Agent Dialogue')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Keara Schaaij, Roel Boumans, Tibor Bosse, Iris Hendrickx

**分类**: cs.CL, cs.HC

**发布日期**: 2025-09-04 (更新: 2025-11-04)

**备注**: This preprint has not undergone peer review or any post-submission improvements or corrections. The Version of Record of this contribution is published in TSD 2025. Lecture Notes in Computer Science, vol 16029

**DOI**: [10.1007/978-3-032-02548-7_5](https://doi.org/10.1007/978-3-032-02548-7_5)

---

## 💡 一句话要点

**构建稳定且个性化的词汇配置文件，为口语人机对话中的词汇对齐奠定基础**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `词汇对齐` `人机对话` `个性化` `词汇配置文件` `语音转录`

## 📋 核心要点

1. 现有对话代理缺乏有效的词汇对齐机制，无法充分利用词汇相似性提升交流质量。
2. 本研究提出构建个性化词汇配置文件，通过分析用户语音数据，提取代表性的词汇特征。
3. 实验表明，使用少量语音数据即可构建稳定且高效的词汇配置文件，为后续词汇对齐策略提供基础。

## 📝 摘要（中文）

词汇对齐，即对话者开始在对话中使用相似的词语，已知有助于成功的交流。然而，其在对话代理中的实现仍未被充分探索，尤其是在大型语言模型（LLM）取得最新进展的情况下。作为在人机对话中实现词汇对齐的第一步，本研究借鉴了个性化对话代理的策略，并研究了构建稳定、个性化的词汇配置文件，作为词汇对齐的基础。具体而言，我们改变了用于构建的转录语音数据的量，以及每个词性（POS）类别中包含的项目数量，并使用召回率、覆盖率和余弦相似度指标评估了配置文件随时间的性能。结果表明，较小且更紧凑的配置文件，在包含形容词5个、连词5个、副词、名词、代词和动词各10个项目的10分钟转录语音后创建，在性能和数据效率方面提供了最佳平衡。总之，本研究提供了构建稳定、个性化的词汇配置文件的实践见解，同时考虑了最小数据需求，为对话代理中的词汇对齐策略奠定了基础。

## 🔬 方法详解

**问题定义**：论文旨在解决口语人机对话中，如何为对话代理构建稳定且个性化的词汇配置文件，从而为后续的词汇对齐策略奠定基础。现有方法缺乏对个性化词汇特征的有效建模，难以实现自然的词汇对齐，影响了人机交互的流畅性和效率。

**核心思路**：论文的核心思路是通过分析用户的语音数据，构建一个能够代表用户个性化词汇使用习惯的配置文件。该配置文件包含不同词性的代表性词汇，并随着用户对话的进行不断更新和优化。通过比较对话代理和用户的词汇配置文件，可以识别出相似的词汇，从而实现词汇对齐。

**技术框架**：整体框架包括数据收集、语音转录、词性标注、词汇提取和配置文件构建等主要阶段。首先，收集用户的语音数据并进行转录。然后，对转录文本进行词性标注，识别出不同词性的词汇。接着，根据词频或其他指标，从每个词性类别中提取出最具代表性的词汇。最后，将这些词汇组成用户的个性化词汇配置文件。

**关键创新**：论文的关键创新在于探索了构建稳定且个性化的词汇配置文件的最佳策略，包括确定最佳的数据量和每个词性类别中包含的项目数量。通过实验，论文发现使用少量语音数据即可构建出性能良好的配置文件，这降低了数据收集和处理的成本。

**关键设计**：论文的关键设计包括：1) 实验中改变了用于构建配置文件的转录语音数据的量（例如，10分钟的语音数据）。2) 改变了每个词性（POS）类别中包含的项目数量（例如，形容词5个，连词5个，副词、名词、代词和动词各10个）。3) 使用召回率、覆盖率和余弦相似度等指标来评估配置文件随时间的性能。

## 📊 实验亮点

实验结果表明，使用10分钟的转录语音数据，并为形容词、连词分别设置5个项目，副词、名词、代词和动词分别设置10个项目，可以构建出在性能和数据效率方面达到最佳平衡的词汇配置文件。该配置文件的召回率、覆盖率和余弦相似度等指标均表现良好，证明了其稳定性和有效性。

## 🎯 应用场景

该研究成果可应用于各种口语人机对话系统，例如智能客服、虚拟助手和教育机器人。通过实现词汇对齐，可以提高人机交互的自然性和流畅性，增强用户的参与感和满意度。此外，个性化的词汇配置文件还可以用于用户画像和情感分析等任务。

## 📄 摘要（原文）

> Lexical alignment, where speakers start to use similar words across conversation, is known to contribute to successful communication. However, its implementation in conversational agents remains underexplored, particularly considering the recent advancements in large language models (LLMs). As a first step towards enabling lexical alignment in human-agent dialogue, this study draws on strategies for personalising conversational agents and investigates the construction of stable, personalised lexical profiles as a basis for lexical alignment. Specifically, we varied the amounts of transcribed spoken data used for construction as well as the number of items included in the profiles per part-of-speech (POS) category and evaluated profile performance across time using recall, coverage, and cosine similarity metrics. It was shown that smaller and more compact profiles, created after 10 min of transcribed speech containing 5 items for adjectives, 5 items for conjunctions, and 10 items for adverbs, nouns, pronouns, and verbs each, offered the best balance in both performance and data efficiency. In conclusion, this study offers practical insights into constructing stable, personalised lexical profiles, taking into account minimal data requirements, serving as a foundational step toward lexical alignment strategies in conversational agents.

