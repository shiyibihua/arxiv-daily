---
layout: default
title: Generation of Programmatic Rules for Document Forgery Detection Using Large Language Models
---

# Generation of Programmatic Rules for Document Forgery Detection Using Large Language Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.19228" class="toolbar-btn" target="_blank">📄 arXiv: 2512.19228v1</a>
  <a href="https://arxiv.org/pdf/2512.19228.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.19228v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.19228v1', 'Generation of Programmatic Rules for Document Forgery Detection Using Large Language Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Valentin Schmidberger, Manuel Eberhardinger, Setareh Maghsudi, Johannes Maucher

**分类**: cs.AI

**发布日期**: 2025-12-22

**备注**: Accepted at ICMLA 2025, the first two authors contributed equally

---

## 💡 一句话要点

**利用大语言模型生成程序化规则，用于文档伪造检测**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `文档伪造检测` `大语言模型` `代码生成` `规则生成` `领域微调`

## 📋 核心要点

1. 现有文档伪造检测的合理性检查依赖人工实现，效率低下且难以扩展。
2. 论文提出利用大语言模型自动生成规则，通过领域数据微调使其适应伪造检测任务。
3. 实验表明，微调后的LLM能够生成有效且可执行的验证程序，提升检测效率。

## 📝 摘要（中文）

文档伪造对法律、经济和政府流程构成日益严重的威胁，需要越来越复杂的验证机制。一种方法是使用合理性检查，即基于规则的程序，评估数据的正确性和内部一致性，以检测异常或篡改迹象。虽然这些验证程序对于确保数据完整性至关重要，但现有的合理性检查是由软件工程师手动实现的，这非常耗时。大语言模型（LLM）在代码生成方面的最新进展为自动化和扩展这些检查的生成提供了新的潜力。然而，使LLM适应未知领域的特定需求仍然是一个重大挑战。本研究探讨了通过不同的微调策略，在领域特定代码和数据上进行调整的LLM，在受限的硬件资源上生成用于伪造检测的基于规则的合理性检查的能力。我们对开源LLM，Llama 3.1 8B和OpenCoder 8B，在从真实应用场景中提取的结构化数据集上进行微调，并评估生成的合理性检查在以前未见过的伪造模式上的效果。结果表明，这些模型能够生成可执行且有效的验证程序。这也突出了LLM作为可扩展工具的潜力，以支持安全敏感环境中需要可理解性的人工决策。

## 🔬 方法详解

**问题定义**：论文旨在解决文档伪造检测中，人工编写合理性检查规则耗时且难以扩展的问题。现有的方法依赖于软件工程师手动实现，不仅效率低下，而且难以应对不断涌现的新型伪造手段。因此，迫切需要一种能够自动生成和维护这些规则的方法。

**核心思路**：论文的核心思路是利用大语言模型（LLM）的代码生成能力，通过在领域特定数据上进行微调，使LLM能够自动生成用于文档伪造检测的程序化规则。这种方法旨在将人工编写规则的过程自动化，从而提高效率和可扩展性。

**技术框架**：整体框架包括以下几个主要阶段：1) 构建领域特定数据集，该数据集包含从真实应用场景中提取的结构化数据，用于训练和评估LLM。2) 选择合适的开源LLM，例如Llama 3.1 8B和OpenCoder 8B。3) 使用领域特定数据集对LLM进行微调，采用不同的微调策略以优化模型性能。4) 使用微调后的LLM生成程序化规则，用于文档伪造检测。5) 在未见过的伪造模式上评估生成的规则的有效性。

**关键创新**：论文的关键创新在于将大语言模型应用于文档伪造检测领域，并探索了利用LLM自动生成程序化规则的可能性。与传统的手动编写规则的方法相比，该方法具有更高的效率和可扩展性。此外，论文还研究了不同的微调策略对模型性能的影响，为实际应用提供了指导。

**关键设计**：论文的关键设计包括：1) 领域特定数据集的构建，需要仔细选择和处理数据，以确保其能够反映真实应用场景中的伪造模式。2) 微调策略的选择，需要根据具体的任务和数据集进行调整，以获得最佳性能。3) 生成规则的评估，需要设计合适的评估指标，以衡量规则的有效性和可靠性。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.19228v1/x1.png" alt="fig_0" loading="lazy">
</figure>
</div>

## 📊 实验亮点

实验结果表明，经过领域数据微调的Llama 3.1 8B和OpenCoder 8B模型，能够生成可执行且有效的文档伪造检测规则。这些规则在未见过的伪造模式上表现良好，验证了LLM在自动化生成安全敏感领域规则的潜力。具体性能数据和对比基线在论文中进行了详细展示。

## 🎯 应用场景

该研究成果可应用于金融、法律、政府等多个领域，用于自动检测和预防文档伪造行为。通过自动生成合理性检查规则，可以显著提高文档验证的效率和准确性，降低人工成本，并有效应对不断演变的伪造技术。未来，该技术有望集成到各种文档管理和验证系统中，提升整体安全性。

## 📄 摘要（原文）

> Document forgery poses a growing threat to legal, economic, and governmental processes, requiring increasingly sophisticated verification mechanisms. One approach involves the use of plausibility checks, rule-based procedures that assess the correctness and internal consistency of data, to detect anomalies or signs of manipulation. Although these verification procedures are essential for ensuring data integrity, existing plausibility checks are manually implemented by software engineers, which is time-consuming. Recent advances in code generation with large language models (LLMs) offer new potential for automating and scaling the generation of these checks. However, adapting LLMs to the specific requirements of an unknown domain remains a significant challenge. This work investigates the extent to which LLMs, adapted on domain-specific code and data through different fine-tuning strategies, can generate rule-based plausibility checks for forgery detection on constrained hardware resources. We fine-tune open-source LLMs, Llama 3.1 8B and OpenCoder 8B, on structured datasets derived from real-world application scenarios and evaluate the generated plausibility checks on previously unseen forgery patterns. The results demonstrate that the models are capable of generating executable and effective verification procedures. This also highlights the potential of LLMs as scalable tools to support human decision-making in security-sensitive contexts where comprehensibility is required.

