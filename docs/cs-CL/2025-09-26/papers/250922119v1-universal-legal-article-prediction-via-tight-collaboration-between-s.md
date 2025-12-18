---
layout: default
title: Universal Legal Article Prediction via Tight Collaboration between Supervised Classification Model and LLM
---

# Universal Legal Article Prediction via Tight Collaboration between Supervised Classification Model and LLM

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.22119" class="toolbar-btn" target="_blank">📄 arXiv: 2509.22119v1</a>
  <a href="https://arxiv.org/pdf/2509.22119.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.22119v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.22119v1', 'Universal Legal Article Prediction via Tight Collaboration between Supervised Classification Model and LLM')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Xiao Chi, Wenlin Zhong, Yiquan Wu, Wei Wang, Kun Kuang, Fei Wu, Minghui Xiong

**分类**: cs.CL, cs.AI

**发布日期**: 2025-09-26

**备注**: 10 pages, 6 figures, Accepted to ICAIL 2025 (International Conference on Artificial Intelligence and Law)

**DOI**: [10.1145/3769126.3769221](https://doi.org/10.1145/3769126.3769221)

---

## 💡 一句话要点

**提出Uni-LAP框架，通过监督分类模型与LLM紧密协作，实现通用法律条文预测。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `法律条文预测` `自然语言处理` `监督分类模型` `大型语言模型` `三段论推理` `法律人工智能` `多司法管辖区` `Top-K损失`

## 📋 核心要点

1. 现有监督分类模型难以捕捉复杂案件事实，大型语言模型在预测任务中表现不佳，且缺乏跨司法管辖区的通用性。
2. Uni-LAP框架通过监督分类模型生成候选条文，并利用大型语言模型进行三段论推理，从而实现更准确的预测。
3. 在多司法管辖区数据集上的实验表明，Uni-LAP始终优于现有基线方法，验证了其有效性和泛化能力。

## 📝 摘要（中文）

法律条文预测（LAP）是法律文本分类中的关键任务，它利用自然语言处理（NLP）技术，根据案件的事实描述自动预测相关的法律条文。作为法律决策的基础步骤，LAP在确定后续判决（如指控和处罚）方面起着关键作用。然而，现有方法在处理LAP的复杂性方面面临重大挑战。监督分类模型（SCM），如CNN和BERT，由于其固有的局限性，难以充分捕捉复杂的案件事实模式。另一方面，大型语言模型（LLM）虽然擅长生成任务，但在预测场景中的表现欠佳，因为法律条文是抽象的且基于ID的。此外，不同司法管辖区法律体系的多样性加剧了这个问题，因为大多数方法都是针对特定国家/地区量身定制的，缺乏更广泛的适用性。为了解决这些局限性，我们提出了Uni-LAP，一个通用的法律条文预测框架，通过紧密协作整合了SCM和LLM的优势。具体来说，在Uni-LAP中，SCM通过一种新颖的Top-K损失函数进行增强，以生成准确的候选条文，而LLM采用受三段论启发的推理来改进最终预测。我们在来自多个司法管辖区的数据集上评估了Uni-LAP，实验结果表明，我们的方法始终优于现有的基线，展示了其有效性和泛化能力。

## 🔬 方法详解

**问题定义**：论文旨在解决法律条文预测（LAP）任务中，现有方法难以兼顾准确性和通用性的问题。监督分类模型（SCM）在捕捉复杂案件事实方面存在局限，而大型语言模型（LLM）在预测任务中表现不佳，且现有方法通常针对特定司法管辖区定制，缺乏跨区域的泛化能力。

**核心思路**：Uni-LAP的核心思路是结合SCM和LLM的优势，通过紧密协作来提升法律条文预测的准确性和通用性。SCM负责生成候选条文，利用其在判别任务上的优势；LLM则负责对候选条文进行推理和排序，利用其在理解和生成方面的能力。这种结合旨在弥补各自的不足，实现更优的预测效果。

**技术框架**：Uni-LAP框架包含两个主要模块：增强的监督分类模型（SCM）和基于三段论推理的大型语言模型（LLM）。首先，SCM接收案件的事实描述作为输入，并使用Top-K损失函数生成K个候选法律条文。然后，LLM接收案件描述和候选条文，利用三段论推理对候选条文进行排序和选择，最终输出预测结果。整个流程旨在利用SCM的判别能力和LLM的推理能力，实现更准确的法律条文预测。

**关键创新**：Uni-LAP的关键创新在于其紧密协作的框架，以及Top-K损失函数和三段论推理的应用。Top-K损失函数增强了SCM生成准确候选条文的能力，而三段论推理则使LLM能够更好地理解案件描述和法律条文之间的关系。这种协作方式与现有方法中SCM或LLM单独使用的模式有本质区别，能够更好地利用两者的优势。

**关键设计**：Uni-LAP的关键设计包括：1) Top-K损失函数，用于训练SCM，鼓励模型生成更准确的候选条文；2) 三段论推理，用于LLM对候选条文进行排序和选择，模拟法律推理过程；3) SCM和LLM之间的信息传递机制，确保两者能够有效地协作。具体的参数设置和网络结构细节在论文中应该有更详细的描述（未知）。

## 📊 实验亮点

Uni-LAP在多个司法管辖区的数据集上进行了评估，实验结果表明，该方法始终优于现有的基线方法。具体的性能提升数据（例如准确率、召回率等）和对比基线的名称在摘要中未提及，需要查阅论文全文才能获得（未知）。但总体而言，实验结果证明了Uni-LAP的有效性和泛化能力。

## 🎯 应用场景

Uni-LAP可应用于智能法律咨询、辅助判案、法律知识检索等领域。通过自动预测相关法律条文，可以提高法律从业人员的工作效率，降低法律服务的成本，并为公众提供更便捷的法律信息服务。该研究的成果有助于推动法律人工智能的发展，并促进法律服务的智能化和普及化。

## 📄 摘要（原文）

> Legal Article Prediction (LAP) is a critical task in legal text classification, leveraging natural language processing (NLP) techniques to automatically predict relevant legal articles based on the fact descriptions of cases. As a foundational step in legal decision-making, LAP plays a pivotal role in determining subsequent judgments, such as charges and penalties. Despite its importance, existing methods face significant challenges in addressing the complexities of LAP. Supervised classification models (SCMs), such as CNN and BERT, struggle to fully capture intricate fact patterns due to their inherent limitations. Conversely, large language models (LLMs), while excelling in generative tasks, perform suboptimally in predictive scenarios due to the abstract and ID-based nature of legal articles. Furthermore, the diversity of legal systems across jurisdictions exacerbates the issue, as most approaches are tailored to specific countries and lack broader applicability. To address these limitations, we propose Uni-LAP, a universal framework for legal article prediction that integrates the strengths of SCMs and LLMs through tight collaboration. Specifically, in Uni-LAP, the SCM is enhanced with a novel Top-K loss function to generate accurate candidate articles, while the LLM employs syllogism-inspired reasoning to refine the final predictions. We evaluated Uni-LAP on datasets from multiple jurisdictions, and empirical results demonstrate that our approach consistently outperforms existing baselines, showcasing its effectiveness and generalizability.

