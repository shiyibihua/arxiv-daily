---
layout: default
title: Evaluating the Robustness of Retrieval-Augmented Generation to Adversarial Evidence in the Health Domain
---

# Evaluating the Robustness of Retrieval-Augmented Generation to Adversarial Evidence in the Health Domain

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.03787" class="toolbar-btn" target="_blank">📄 arXiv: 2509.03787v1</a>
  <a href="https://arxiv.org/pdf/2509.03787.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.03787v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.03787v1', 'Evaluating the Robustness of Retrieval-Augmented Generation to Adversarial Evidence in the Health Domain')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Shakiba Amirshahi, Amin Bigdeli, Charles L. A. Clarke, Amira Ghenai

**分类**: cs.IR, cs.CL

**发布日期**: 2025-09-04

**🔗 代码/项目**: [GITHUB](https://github.com/shakibaam/RAG_ROBUSTNESS_EVAL)

---

## 💡 一句话要点

**评估检索增强生成在医疗领域对抗性证据下的鲁棒性**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `检索增强生成` `RAG` `对抗性证据` `鲁棒性评估` `医疗领域` `大型语言模型` `信息检索`

## 📋 核心要点

1. 现有RAG系统易受检索到的对抗性证据影响，导致LLM产生错误信息，尤其是在高风险的医疗领域。
2. 该研究通过控制检索文档类型和提问方式，系统评估RAG在医疗领域对抗性证据下的鲁棒性。
3. 实验表明，对抗性文档显著降低RAG的一致性，但同时存在有益证据可以提升鲁棒性。

## 📝 摘要（中文）

检索增强生成（RAG）系统通过提供检索到的证据（即上下文）作为支持，为大型语言模型（LLM）的响应提供事实依据。在上下文的引导下，RAG系统可以减少幻觉，并扩展LLM准确回答超出其训练数据范围之外问题的能力。然而，这种设计引入了一个关键漏洞：LLM可能会吸收并再现检索到的证据中存在的错误信息。如果检索到的证据包含明确旨在传播错误信息的对抗性材料，这个问题会更加严重。本文对RAG在医疗领域的鲁棒性进行了系统评估，并检查了模型输出与真实答案之间的一致性。我们关注医疗领域，因为不正确的回答可能造成危害，并且许多常见的健康相关问题都有循证的真实答案。我们使用常见的健康问题进行对照实验，改变检索到的文档的类型和组成（有帮助的、有害的和对抗性的），以及用户提问的方式（一致的、中性的和不一致的）。我们的研究结果表明，对抗性文档会显著降低一致性，但当检索池中也存在有帮助的证据时，可以保持鲁棒性。这些发现为在高风险领域设计更安全的RAG系统提供了可操作的见解，强调了检索保障的必要性。为了实现可重复性并促进未来的研究，所有实验结果都可以在我们的github存储库中公开获得。

## 🔬 方法详解

**问题定义**：论文旨在解决RAG系统在医疗领域应用时，由于检索到的证据中包含对抗性信息而导致LLM产生错误或有害回答的问题。现有RAG系统容易受到检索到的错误信息的影响，缺乏对对抗性证据的鲁棒性，这在高风险的医疗领域尤其危险。

**核心思路**：论文的核心思路是通过系统地评估RAG系统在不同类型的检索证据（有益的、有害的和对抗性的）和不同提问方式下的表现，来量化其鲁棒性。通过分析模型输出与真实答案之间的一致性，揭示对抗性证据对RAG系统性能的影响。

**技术框架**：该研究采用实验方法，主要流程包括：1) 构建包含健康相关问题的测试集，并为每个问题准备有益的、有害的和对抗性的证据文档；2) 使用RAG系统检索相关文档，并生成答案；3) 评估生成的答案与真实答案之间的一致性，作为鲁棒性的指标；4) 分析不同类型的证据和提问方式对鲁棒性的影响。

**关键创新**：该研究的关键创新在于系统性地评估了RAG系统在医疗领域对抗性证据下的鲁棒性。通过控制实验，量化了对抗性证据对RAG系统性能的影响，并揭示了同时存在有益证据可以提升鲁棒性的现象。这为设计更安全的RAG系统提供了重要的见解。

**关键设计**：实验设计中，关键参数包括：1) 检索文档的类型（有益的、有害的和对抗性的）及其比例；2) 用户提问的方式（一致的、中性的和不一致的）；3) 一致性的评估指标（例如，与ground truth答案的语义相似度）。论文没有详细描述损失函数或网络结构，因为重点在于评估RAG系统的整体鲁棒性，而不是优化特定的模型组件。

## 📊 实验亮点

实验结果表明，对抗性文档显著降低了RAG系统输出与真实答案之间的一致性。然而，当检索池中同时包含有益的证据时，RAG系统的鲁棒性可以得到显著提升。这表明，在设计RAG系统时，需要重视检索结果的质量和多样性，以减轻对抗性证据的影响。

## 🎯 应用场景

该研究成果可应用于开发更安全可靠的医疗健康问答系统。通过提升RAG系统对抗错误信息的能力，可以减少LLM产生有害或不准确的医疗建议的风险。未来的研究可以探索更有效的检索保障机制，例如对抗性证据检测和过滤，以进一步提高RAG系统在医疗领域的应用价值。

## 📄 摘要（原文）

> Retrieval augmented generation (RAG) systems provide a method for factually grounding the responses of a Large Language Model (LLM) by providing retrieved evidence, or context, as support. Guided by this context, RAG systems can reduce hallucinations and expand the ability of LLMs to accurately answer questions outside the scope of their training data. Unfortunately, this design introduces a critical vulnerability: LLMs may absorb and reproduce misinformation present in retrieved evidence. This problem is magnified if retrieved evidence contains adversarial material explicitly intended to promulgate misinformation. This paper presents a systematic evaluation of RAG robustness in the health domain and examines alignment between model outputs and ground-truth answers. We focus on the health domain due to the potential for harm caused by incorrect responses, as well as the availability of evidence-based ground truth for many common health-related questions. We conduct controlled experiments using common health questions, varying both the type and composition of the retrieved documents (helpful, harmful, and adversarial) as well as the framing of the question by the user (consistent, neutral, and inconsistent). Our findings reveal that adversarial documents substantially degrade alignment, but robustness can be preserved when helpful evidence is also present in the retrieval pool. These findings offer actionable insights for designing safer RAG systems in high-stakes domains by highlighting the need for retrieval safeguards. To enable reproducibility and facilitate future research, all experimental results are publicly available in our github repository.
>   https://github.com/shakibaam/RAG_ROBUSTNESS_EVAL

