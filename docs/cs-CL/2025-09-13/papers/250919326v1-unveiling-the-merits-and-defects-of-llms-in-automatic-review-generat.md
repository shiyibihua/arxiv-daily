---
layout: default
title: Unveiling the Merits and Defects of LLMs in Automatic Review Generation for Scientific Papers
---

# Unveiling the Merits and Defects of LLMs in Automatic Review Generation for Scientific Papers

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.19326" class="toolbar-btn" target="_blank">📄 arXiv: 2509.19326v1</a>
  <a href="https://arxiv.org/pdf/2509.19326.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.19326v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.19326v1', 'Unveiling the Merits and Defects of LLMs in Automatic Review Generation for Scientific Papers')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Ruochi Li, Haoxuan Zhang, Edward Gehringer, Ting Xiao, Junhua Ding, Haihua Chen

**分类**: cs.CL, cs.AI

**发布日期**: 2025-09-13

**备注**: Accepted as short paper at 25th IEEE International Conference on Data Mining

**🔗 代码/项目**: [GITHUB](https://github.com/RichardLRC/Peer-Review)

---

## 💡 一句话要点

**提出综合评估框架，揭示LLM在科学论文自动评审中的优缺点。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `自动评审生成` `同行评审` `知识图谱` `语义相似性分析`

## 📋 核心要点

1. 传统同行评审面临巨大压力，亟需探索LLM辅助自动评审以缓解审稿负担，但LLM的评审质量有待系统评估。
2. 论文提出综合评估框架，结合语义相似性分析和知识图指标，对比LLM与人工评审，全面评估LLM评审质量。
3. 实验结果表明，LLM擅长描述论文贡献，但在识别论文弱点、提出质疑和质量敏感性方面表现不足。

## 📝 摘要（中文）

科学论文投稿数量激增，传统同行评审压力增大，促使人们探索使用大型语言模型（LLM）进行自动评审生成。虽然LLM在生成结构化和连贯的反馈方面表现出能力，但其批判性推理、上下文理解和质量敏感性仍然有限。为了系统地评估这些方面，我们提出了一个综合评估框架，该框架集成了语义相似性分析和结构化知识图指标，以评估LLM生成的评论与人工撰写的评论的对比。我们构建了一个大规模基准，包含来自ICLR和NeurIPS多年份的1,683篇论文和6,495份专家评审，并使用五个LLM生成评审。我们的研究结果表明，LLM在描述性和肯定性内容方面表现良好，能够捕捉原始工作的主要贡献和方法，其中GPT-4o是一个例证，在ICLR 2025优秀论文的优势部分生成的实体比人工评审员多15.74%。然而，它们在识别弱点、提出实质性问题以及根据论文质量调整反馈方面始终表现不佳。GPT-4o在弱点部分产生的实体比真实评审员少59.42%，并且从优秀论文到较差论文的节点计数仅增加5.7%，而人工评审则为50%。在所有会议、年份和模型中都观察到类似的趋势，为理解LLM生成评论的优点和缺点提供了经验基础，并为开发未来的LLM辅助评审工具提供了信息。数据、代码和更详细的结果可在https://github.com/RichardLRC/Peer-Review公开获取。

## 🔬 方法详解

**问题定义**：现有同行评审系统面临着日益增长的论文提交量带来的巨大压力，审稿人资源有限，导致审稿周期长、质量参差不齐。利用LLM自动生成评审报告有望缓解这一问题，但LLM在评审过程中是否能够像人类专家一样进行批判性思考、准确把握论文的上下文，并对论文质量做出敏感的判断，仍然是一个开放的问题。现有方法缺乏对LLM评审质量的全面、系统的评估。

**核心思路**：论文的核心思路是构建一个综合性的评估框架，通过将LLM生成的评审报告与人类专家撰写的评审报告进行对比，从多个维度评估LLM在评审过程中的表现。该框架不仅关注评审报告的语义相似性，还利用知识图谱来分析评审报告中包含的关键信息和论证结构，从而更全面地了解LLM的优缺点。

**技术框架**：该研究的技术框架主要包含以下几个阶段：
1.  **数据收集与整理**：收集来自ICLR和NeurIPS等顶级会议的大量论文和对应的专家评审报告，构建大规模的基准数据集。
2.  **LLM评审生成**：使用多个主流的LLM（如GPT-4o）对论文进行评审，生成自动评审报告。
3.  **评审质量评估**：利用提出的综合评估框架，从语义相似性和知识图谱两个方面对LLM生成的评审报告和人工评审报告进行对比分析。
4.  **结果分析与总结**：分析实验结果，总结LLM在评审过程中的优点和不足，为未来的LLM辅助评审工具开发提供指导。

**关键创新**：该论文最重要的技术创新点在于提出了一个综合性的评估框架，该框架结合了语义相似性分析和结构化知识图谱指标，能够更全面、更深入地评估LLM在评审过程中的表现。与传统的评估方法相比，该框架不仅关注评审报告的内容相似性，还关注评审报告的结构和逻辑，从而能够更准确地反映LLM的评审质量。

**关键设计**：在评估框架的关键设计方面，论文采用了以下技术细节：
*   **语义相似性分析**：使用预训练语言模型计算LLM生成评审和人工评审之间的语义相似度，评估LLM是否能够准确理解论文的内容。
*   **知识图谱构建**：从评审报告中提取关键实体和关系，构建知识图谱，用于分析评审报告的结构和逻辑。
*   **知识图谱指标**：使用节点数量、边数量、平均度等指标来衡量知识图谱的复杂度和完整性，从而评估LLM是否能够全面地把握论文的关键信息。

## 📊 实验亮点

实验结果表明，GPT-4o在描述性和肯定性内容方面表现良好，在ICLR 2025优秀论文的优势部分生成的实体比人工评审员多15.74%。然而，在识别弱点方面，GPT-4o产生的实体比真实评审员少59.42%，并且从优秀论文到较差论文的节点计数仅增加5.7%，而人工评审则为50%。

## 🎯 应用场景

该研究成果可应用于开发LLM辅助的同行评审系统，减轻审稿人的工作负担，提高评审效率。通过了解LLM在评审中的优缺点，可以针对性地改进LLM，使其更好地辅助人类专家进行评审。此外，该研究提出的评估框架也可用于评估其他自动评审系统的性能。

## 📄 摘要（原文）

> The surge in scientific submissions has placed increasing strain on the traditional peer-review process, prompting the exploration of large language models (LLMs) for automated review generation. While LLMs demonstrate competence in producing structured and coherent feedback, their capacity for critical reasoning, contextual grounding, and quality sensitivity remains limited. To systematically evaluate these aspects, we propose a comprehensive evaluation framework that integrates semantic similarity analysis and structured knowledge graph metrics to assess LLM-generated reviews against human-written counterparts. We construct a large-scale benchmark of 1,683 papers and 6,495 expert reviews from ICLR and NeurIPS in multiple years, and generate reviews using five LLMs. Our findings show that LLMs perform well in descriptive and affirmational content, capturing the main contributions and methodologies of the original work, with GPT-4o highlighted as an illustrative example, generating 15.74% more entities than human reviewers in the strengths section of good papers in ICLR 2025. However, they consistently underperform in identifying weaknesses, raising substantive questions, and adjusting feedback based on paper quality. GPT-4o produces 59.42% fewer entities than real reviewers in the weaknesses and increases node count by only 5.7% from good to weak papers, compared to 50% in human reviews. Similar trends are observed across all conferences, years, and models, providing empirical foundations for understanding the merits and defects of LLM-generated reviews and informing the development of future LLM-assisted reviewing tools. Data, code, and more detailed results are publicly available at https://github.com/RichardLRC/Peer-Review.

