---
layout: default
title: Benchmarking Information Retrieval Models on Complex Retrieval Tasks
---

# Benchmarking Information Retrieval Models on Complex Retrieval Tasks

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.07253" class="toolbar-btn" target="_blank">📄 arXiv: 2509.07253v1</a>
  <a href="https://arxiv.org/pdf/2509.07253.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.07253v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.07253v1', 'Benchmarking Information Retrieval Models on Complex Retrieval Tasks')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Julian Killingback, Hamed Zamani

**分类**: cs.IR, cs.AI, cs.CL

**发布日期**: 2025-09-08

---

## 💡 一句话要点

**构建复杂检索任务基准，评估并提升信息检索模型性能**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `信息检索` `复杂检索任务` `基准测试` `大型语言模型` `查询扩展` `查询重写` `模型评估`

## 📋 核心要点

1. 现有检索模型难以处理包含多方面约束的复杂查询，限制了其在实际场景中的应用。
2. 构建了多样且真实的复杂检索任务数据集，用于全面评估现有检索模型的能力。
3. 实验表明，现有最佳模型在复杂检索任务上表现不佳，LLM增强对强模型效果反而下降。

## 📝 摘要（中文）

大型语言模型（LLMs）在文本任务中表现出色，催生了无数应用。相比之下，检索模型尚未涌现出同样强大的通用模型。为了实现这一目标，检索模型必须能够执行复杂的检索任务，即查询包含多个部分、约束或自然语言要求。这些任务代表了从简单、单方面查询到更高级的自然演进，正如人们期望搜索系统处理更具体和雄心勃勃的信息请求一样，LLM信息系统的使用也证明了这一点。尽管对检索模型在复杂检索任务中扩展能力的需求日益增长，但评估检索模型在各种复杂任务上的能力的资源有限。现有的少数资源范围有限，且缺乏现实设置，难以了解检索模型在复杂真实检索任务中的真正能力。为了解决这一不足，并激发下一代检索模型的创新，我们构建了一组多样且真实的复杂检索任务，并对一组具有代表性的最先进的检索模型进行了基准测试。此外，我们还探讨了基于LLM的查询扩展和重写对检索质量的影响。结果表明，即使是最好的模型也很难产生高质量的检索结果，所有任务的平均nDCG@10最高仅为0.346，R@100最高仅为0.587。虽然LLM增强可以帮助较弱的模型，但最强模型在所有重写技术下的所有指标上的性能都有所下降。

## 🔬 方法详解

**问题定义**：论文旨在解决现有信息检索模型在处理复杂检索任务时表现不佳的问题。复杂检索任务指的是那些包含多个约束条件、需要理解自然语言描述的查询。现有方法通常针对简单查询设计，无法有效处理复杂查询，导致检索结果质量下降。

**核心思路**：论文的核心思路是构建一个包含多样化复杂检索任务的基准数据集，并在此数据集上评估现有检索模型的性能。通过分析模型在不同任务上的表现，可以发现模型的优势和不足，从而指导模型改进。此外，论文还探索了利用大型语言模型（LLM）进行查询扩展和重写，以提升检索性能。

**技术框架**：论文的技术框架主要包括以下几个部分：1) 构建复杂检索任务数据集；2) 选择具有代表性的最先进检索模型；3) 在数据集上评估这些模型的性能；4) 探索LLM增强方法，如查询扩展和重写；5) 分析实验结果，总结模型的优缺点。

**关键创新**：论文的关键创新在于构建了一个多样且真实的复杂检索任务数据集。该数据集涵盖了各种类型的复杂查询，能够更全面地评估检索模型的能力。此外，论文还对LLM增强方法进行了深入研究，发现LLM增强对弱模型有帮助，但对强模型可能会降低性能。

**关键设计**：论文在构建数据集时，考虑了任务的多样性和真实性。任务类型包括多方面约束、自然语言描述等。在评估模型性能时，使用了nDCG@10和R@100等常用指标。在探索LLM增强方法时，使用了不同的LLM模型和重写策略。

## 📊 实验亮点

实验结果表明，现有最佳模型在复杂检索任务上的平均nDCG@10仅为0.346，R@100仅为0.587，表明性能仍有很大提升空间。LLM增强方法对弱模型有一定帮助，但对最强模型，所有重写技术都导致性能下降，提示需要更精细的LLM集成策略。

## 🎯 应用场景

该研究成果可应用于智能搜索引擎、问答系统、推荐系统等领域。通过提升模型处理复杂查询的能力，可以改善用户体验，提高信息检索的效率和准确性。未来，该研究可以推动下一代检索模型的发展，使其能够更好地满足用户日益增长的复杂信息需求。

## 📄 摘要（原文）

> Large language models (LLMs) are incredible and versatile tools for text-based tasks that have enabled countless, previously unimaginable, applications. Retrieval models, in contrast, have not yet seen such capable general-purpose models emerge. To achieve this goal, retrieval models must be able to perform complex retrieval tasks, where queries contain multiple parts, constraints, or requirements in natural language. These tasks represent a natural progression from the simple, single-aspect queries that are used in the vast majority of existing, commonly used evaluation sets. Complex queries naturally arise as people expect search systems to handle more specific and often ambitious information requests, as is demonstrated by how people use LLM-based information systems. Despite the growing desire for retrieval models to expand their capabilities in complex retrieval tasks, there exist limited resources to assess the ability of retrieval models on a comprehensive set of diverse complex tasks. The few resources that do exist feature a limited scope and often lack realistic settings making it hard to know the true capabilities of retrieval models on complex real-world retrieval tasks. To address this shortcoming and spur innovation in next-generation retrieval models, we construct a diverse and realistic set of complex retrieval tasks and benchmark a representative set of state-of-the-art retrieval models. Additionally, we explore the impact of LLM-based query expansion and rewriting on retrieval quality. Our results show that even the best models struggle to produce high-quality retrieval results with the highest average nDCG@10 of only 0.346 and R@100 of only 0.587 across all tasks. Although LLM augmentation can help weaker models, the strongest model has decreased performance across all metrics with all rewriting techniques.

