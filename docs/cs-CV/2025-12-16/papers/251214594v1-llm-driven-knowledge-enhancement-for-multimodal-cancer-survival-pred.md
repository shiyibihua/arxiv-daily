---
layout: default
title: LLM-driven Knowledge Enhancement for Multimodal Cancer Survival Prediction
---

# LLM-driven Knowledge Enhancement for Multimodal Cancer Survival Prediction

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.14594" class="toolbar-btn" target="_blank">📄 arXiv: 2512.14594v1</a>
  <a href="https://arxiv.org/pdf/2512.14594.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.14594v1" onclick="toggleFavorite(this, '2512.14594v1', 'LLM-driven Knowledge Enhancement for Multimodal Cancer Survival Prediction')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Chenyu Zhao, Yingxue Xu, Fengtao Zhou, Yihui Wang, Hao Chen

**分类**: cs.CV

**发布日期**: 2025-12-16

---

## 💡 一句话要点

**提出KEMM模型，利用LLM增强知识的多模态癌症生存预测。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多模态学习` `癌症生存预测` `大型语言模型` `知识增强` `跨模态注意力`

## 📋 核心要点

1. 现有方法难以从高维冗余的病理图像和基因组数据中提取有效特征，且缺乏充分的监督信号。
2. KEMM模型利用LLM处理专家报告和生成预后背景知识，增强模型对生存预测相关特征的关注。
3. 在五个数据集上的实验表明，KEMM模型取得了state-of-the-art的性能，验证了方法的有效性。

## 📝 摘要（中文）

当前的多模态生存预测方法通常依赖于病理图像（WSIs）和基因组数据，这些数据维度高且冗余，难以提取判别性特征并对齐不同模态。此外，使用简单的生存随访标签不足以监督如此复杂的任务。为了解决这些挑战，我们提出了KEMM，一种由LLM驱动的知识增强多模态模型，用于癌症生存预测，它集成了专家报告和预后背景知识。1) 专家报告由病理学家逐个案例提供，并由大型语言模型（LLM）提炼，提供简洁且临床重点突出的诊断陈述。这些信息通常暗示不同的生存结果。2) 预后背景知识（PBK）由LLM简洁地生成，提供关于不同癌症类型的有价值的预后背景知识，这也增强了生存预测。为了利用这些知识，我们引入了知识增强的跨模态（KECM）注意力模块。KECM可以有效地引导网络关注来自高度冗余模态的判别性和生存相关的特征。在五个数据集上的大量实验表明，KEMM实现了最先进的性能。代码将在接受后发布。

## 🔬 方法详解

**问题定义**：论文旨在解决多模态癌症生存预测中，病理图像和基因组数据维度高、冗余度大，难以有效提取判别性特征，以及现有方法缺乏充分监督信号的问题。现有方法难以有效对齐不同模态的信息，导致预测精度不高。

**核心思路**：论文的核心思路是利用大型语言模型（LLM）从专家报告中提取关键诊断信息，并生成预后背景知识，从而为多模态模型提供更丰富的上下文信息和更强的监督信号。通过知识增强的跨模态注意力机制，引导模型关注与生存预测相关的特征。

**技术框架**：KEMM模型主要包含以下几个模块：1) LLM驱动的知识提取模块，用于处理专家报告并生成预后背景知识；2) 多模态特征提取模块，用于提取病理图像和基因组数据的特征；3) 知识增强的跨模态注意力（KECM）模块，用于融合不同模态的特征和知识；4) 生存预测模块，用于预测患者的生存概率。整体流程是先利用LLM提取知识，然后将知识与多模态特征融合，最后进行生存预测。

**关键创新**：论文的关键创新在于引入了LLM来增强多模态模型的知识，并设计了知识增强的跨模态注意力机制。与现有方法相比，KEMM模型能够更有效地利用专家知识和预后背景知识，从而提高生存预测的准确性。KECM模块能够自适应地学习不同模态之间的关系，并突出与生存预测相关的特征。

**关键设计**：KECM模块的设计是关键。该模块利用注意力机制，根据LLM提取的知识，动态地调整不同模态特征的权重。具体的注意力计算方式未知，但可以推测是基于query-key-value的注意力机制，其中query来自LLM提取的知识，key和value来自多模态特征。损失函数可能包括生存分析中常用的C-index损失和可能存在的交叉熵损失，用于监督模型的训练。

## 📊 实验亮点

KEMM模型在五个癌症数据集上取得了state-of-the-art的性能，表明其在多模态癌症生存预测方面的优越性。具体的性能提升幅度未知，但摘要中强调了“achieves state-of-the-art performance”，说明KEMM模型相比现有方法有显著的提升。实验结果验证了利用LLM增强知识的有效性。

## 🎯 应用场景

该研究成果可应用于临床辅助诊断，帮助医生更准确地预测癌症患者的生存概率，从而制定更个性化的治疗方案。通过整合病理图像、基因组数据和专家知识，KEMM模型有望提高癌症治疗的有效性和患者的生存质量。未来，该方法可以扩展到其他疾病的生存预测和诊断。

## 📄 摘要（原文）

> Current multimodal survival prediction methods typically rely on pathology images (WSIs) and genomic data, both of which are high-dimensional and redundant, making it difficult to extract discriminative features from them and align different modalities. Moreover, using a simple survival follow-up label is insufficient to supervise such a complex task. To address these challenges, we propose KEMM, an LLM-driven Knowledge-Enhanced Multimodal Model for cancer survival prediction, which integrates expert reports and prognostic background knowledge. 1) Expert reports, provided by pathologists on a case-by-case basis and refined by large language model (LLM), offer succinct and clinically focused diagnostic statements. This information may typically suggest different survival outcomes. 2) Prognostic background knowledge (PBK), generated concisely by LLM, provides valuable prognostic background knowledge on different cancer types, which also enhances survival prediction. To leverage these knowledge, we introduce the knowledge-enhanced cross-modal (KECM) attention module. KECM can effectively guide the network to focus on discriminative and survival-relevant features from highly redundant modalities. Extensive experiments on five datasets demonstrate that KEMM achieves state-of-the-art performance. The code will be released upon acceptance.

