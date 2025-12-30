---
layout: default
title: Divergent-Convergent Thinking in Large Language Models for Creative Problem Generation
---

# Divergent-Convergent Thinking in Large Language Models for Creative Problem Generation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.23601" class="toolbar-btn" target="_blank">📄 arXiv: 2512.23601v1</a>
  <a href="https://arxiv.org/pdf/2512.23601.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.23601v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.23601v1', 'Divergent-Convergent Thinking in Large Language Models for Creative Problem Generation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Manh Hung Nguyen, Adish Singla

**分类**: cs.AI

**发布日期**: 2025-12-29

**备注**: Preprint

---

## 💡 一句话要点

**CreativeDC：利用大语言模型中的发散-收敛思维生成多样化创意问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大语言模型` `创造性问题生成` `发散-收敛思维` `提示工程` `教育应用`

## 📋 核心要点

1. 现有LLM生成教育问题时存在“人工蜂群”效应，导致问题同质化，限制了学生思维多样性。
2. CreativeDC方法借鉴发散-收敛思维，将问题生成分解为创意探索和约束满足两个阶段。
3. 实验表明，CreativeDC在多样性和新颖性方面显著优于基线方法，同时保持了较高的实用性。

## 📝 摘要（中文）

大型语言模型（LLMs）在生成教育问题方面具有巨大潜力，能够帮助教育工作者创建大规模的学习材料。然而，LLMs受到“人工蜂群”效应的根本限制，即在同一模型内生成相似的响应，并在不同模型之间产生同质的输出。因此，学生可能会接触到过于相似和重复的LLM生成的问题，这损害了思维的多样性。受Wallas创造力理论和Guilford发散-收敛思维框架的启发，我们提出了CreativeDC，一种两阶段提示方法，它将LLM的推理明确地分解为不同的阶段。通过将创造性探索与约束满足分离，我们的方法使LLMs能够在确定最终问题之前探索更广阔的创意空间。我们使用一套全面的指标来评估CreativeDC在创造性问题生成方面的性能，这些指标捕捉了多样性、新颖性和效用。结果表明，与基线方法相比，CreativeDC在保持高实用性的同时，实现了显著更高的多样性和新颖性。此外，规模分析表明，随着采样数量的增加，CreativeDC生成了更大数量的有效不同问题，其增长速度快于基线方法。

## 🔬 方法详解

**问题定义**：论文旨在解决大型语言模型（LLMs）在生成教育问题时存在的同质化问题。现有方法受限于“人工蜂群”效应，导致生成的问题相似度高，缺乏多样性和新颖性，不利于培养学生的创造性思维。这种同质化问题限制了LLMs在教育领域的应用价值。

**核心思路**：论文的核心思路是借鉴Wallas的创造力理论和Guilford的发散-收敛思维框架，将问题生成过程分解为两个阶段：发散阶段（Divergent Thinking）和收敛阶段（Convergent Thinking）。发散阶段鼓励LLM探索尽可能多的创意，生成各种不同的问题想法；收敛阶段则对这些想法进行筛选和优化，使其满足特定的约束条件，最终生成高质量的问题。

**技术框架**：CreativeDC方法包含两个主要阶段：
1. **发散阶段**：使用特定的prompt引导LLM进行自由联想，生成尽可能多的、不同的问题想法。这个阶段的目标是扩大搜索空间，避免过早陷入局部最优。
2. **收敛阶段**：使用另一个prompt引导LLM对发散阶段生成的想法进行评估和筛选，选择最有价值的想法，并将其转化为符合要求的具体问题。这个阶段的目标是保证生成问题的质量和实用性。

**关键创新**：CreativeDC的关键创新在于将创造性问题生成过程显式地分解为发散和收敛两个阶段，并分别使用不同的prompt进行引导。这种解耦使得LLM能够更好地探索创意空间，避免受到约束条件的限制，从而生成更多样化和新颖的问题。与现有方法相比，CreativeDC更注重激发LLM的创造性思维，而不是简单地模仿已有的问题模式。

**关键设计**：在发散阶段，prompt的设计需要鼓励LLM进行大胆的联想，例如使用“头脑风暴”、“自由写作”等关键词。在收敛阶段，prompt的设计需要明确问题的约束条件，例如问题的难度、知识点、适用对象等。此外，还可以使用一些评价指标来指导LLM进行筛选，例如问题的原创性、趣味性、挑战性等。具体的参数设置和损失函数未知，因为论文侧重于prompt工程而非模型训练。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.23601v1/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.23601v1/x2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.23601v1/x3.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

实验结果表明，CreativeDC在多样性（Diversity）和新颖性（Novelty）方面显著优于基线方法，同时保持了较高的实用性（Utility）。规模分析显示，随着采样数量的增加，CreativeDC生成有效不同问题的速度明显快于基线方法。具体性能数据未知，但整体趋势表明CreativeDC能够有效提升LLM生成问题的多样性和新颖性。

## 🎯 应用场景

CreativeDC方法可应用于教育领域，辅助教师快速生成大量多样化、高质量的练习题和考试题，减轻教师的备课负担。此外，该方法还可用于生成各种创意性任务，例如故事创作、产品设计等，激发用户的创造力。未来，该方法有望应用于更广泛的领域，例如科研探索、创新设计等。

## 📄 摘要（原文）

> Large language models (LLMs) have significant potential for generating educational questions and problems, enabling educators to create large-scale learning materials. However, LLMs are fundamentally limited by the ``Artificial Hivemind'' effect, where they generate similar responses within the same model and produce homogeneous outputs across different models. As a consequence, students may be exposed to overly similar and repetitive LLM-generated problems, which harms diversity of thought. Drawing inspiration from Wallas's theory of creativity and Guilford's framework of divergent-convergent thinking, we propose CreativeDC, a two-phase prompting method that explicitly scaffolds the LLM's reasoning into distinct phases. By decoupling creative exploration from constraint satisfaction, our method enables LLMs to explore a broader space of ideas before committing to a final problem. We evaluate CreativeDC for creative problem generation using a comprehensive set of metrics that capture diversity, novelty, and utility. The results show that CreativeDC achieves significantly higher diversity and novelty compared to baselines while maintaining high utility. Moreover, scaling analysis shows that CreativeDC generates a larger effective number of distinct problems as more are sampled, increasing at a faster rate than baseline methods.

