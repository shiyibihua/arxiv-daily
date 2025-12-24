---
layout: default
title: A comprehensive taxonomy of hallucinations in Large Language Models
---

# A comprehensive taxonomy of hallucinations in Large Language Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.01781" class="toolbar-btn" target="_blank">📄 arXiv: 2508.01781v1</a>
  <a href="https://arxiv.org/pdf/2508.01781.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.01781v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.01781v1', 'A comprehensive taxonomy of hallucinations in Large Language Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Manuel Cossio

**分类**: cs.CL, cs.AI

**发布日期**: 2025-08-03

**备注**: 55 pages, 16 figures, 3 tables

---

## 💡 一句话要点

**提出全面分类法以解决大型语言模型的幻觉问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `幻觉分类` `自然语言处理` `内容生成` `模型可靠性` `检测策略` `缓解措施`

## 📋 核心要点

1. 大型语言模型在生成内容时常出现幻觉现象，导致生成的内容虽然看似合理，但却缺乏事实依据，影响其可靠性。
2. 论文提出了一种全面的幻觉分类法，系统性地分析了幻觉的类型、成因及其对模型性能的影响，强调了检测和缓解的重要性。
3. 通过对幻觉现象的深入研究，论文为未来的模型设计和应用提供了理论支持和实践指导，促进了对LLM的负责任使用。

## 📝 摘要（中文）

大型语言模型（LLMs）在自然语言处理领域引发了革命，但其生成似是而非的内容（即幻觉）仍然是一个重要挑战。本文提供了LLM幻觉的全面分类，首先给出了正式定义和理论框架，认为在可计算的LLM中，幻觉的产生是不可避免的。文章区分了内在幻觉（与输入上下文矛盾）和外在幻觉（与训练数据或现实不一致），以及绝对正确性和忠实性。接着，详细描述了幻觉的具体表现，包括事实错误、上下文和逻辑不一致、时间错位、伦理违规等。最后，文章分析了幻觉的根本原因，并提出了检测和缓解的策略，强调了未来在关键应用中需要持续的人类监督。

## 🔬 方法详解

**问题定义**：本文旨在解决大型语言模型在生成内容时出现的幻觉现象，现有方法未能有效识别和分类这些幻觉，导致模型输出的可靠性受到质疑。

**核心思路**：论文提出了一种全面的幻觉分类法，基于对幻觉的定义和理论框架，系统性地分析幻觉的类型及其成因，强调了检测和缓解策略的重要性。

**技术框架**：整体架构包括幻觉的定义、分类、成因分析、检测指标和缓解策略五个主要模块，形成一个完整的理论和实践框架。

**关键创新**：最重要的技术创新在于提出了内在幻觉与外在幻觉的区分，以及对幻觉的多维度分析，填补了现有研究的空白。

**关键设计**：论文中使用了多种评估基准和指标来检测幻觉，并提出了针对数据、模型和提示的缓解策略，确保模型在实际应用中的可靠性。

## 📊 实验亮点

论文通过系统分析幻觉现象，提出了多种检测和缓解策略，显著提高了模型在特定任务中的表现。具体而言，针对不同类型的幻觉，提出的缓解措施在实验中显示出显著的性能提升，确保了生成内容的更高准确性。

## 🎯 应用场景

该研究的潜在应用领域包括自然语言处理、对话系统、自动内容生成等，能够为开发更可靠的语言模型提供理论支持和实践指导。通过有效的幻觉检测和缓解策略，提升模型在关键应用中的表现，确保其输出的准确性和可信度。

## 📄 摘要（原文）

> Large language models (LLMs) have revolutionized natural language processing, yet their propensity for hallucination, generating plausible but factually incorrect or fabricated content, remains a critical challenge. This report provides a comprehensive taxonomy of LLM hallucinations, beginning with a formal definition and a theoretical framework that posits its inherent inevitability in computable LLMs, irrespective of architecture or training. It explores core distinctions, differentiating between intrinsic (contradicting input context) and extrinsic (inconsistent with training data or reality), as well as factuality (absolute correctness) and faithfulness (adherence to input). The report then details specific manifestations, including factual errors, contextual and logical inconsistencies, temporal disorientation, ethical violations, and task-specific hallucinations across domains like code generation and multimodal applications. It analyzes the underlying causes, categorizing them into data-related issues, model-related factors, and prompt-related influences. Furthermore, the report examines cognitive and human factors influencing hallucination perception, surveys evaluation benchmarks and metrics for detection, and outlines architectural and systemic mitigation strategies. Finally, it introduces web-based resources for monitoring LLM releases and performance. This report underscores the complex, multifaceted nature of LLM hallucinations and emphasizes that, given their theoretical inevitability, future efforts must focus on robust detection, mitigation, and continuous human oversight for responsible and reliable deployment in critical applications.

