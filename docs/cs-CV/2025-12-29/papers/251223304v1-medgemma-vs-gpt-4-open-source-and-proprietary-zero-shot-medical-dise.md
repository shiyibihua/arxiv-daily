---
layout: default
title: "MedGemma vs GPT-4: Open-Source and Proprietary Zero-shot Medical Disease Classification from Images"
---

# MedGemma vs GPT-4: Open-Source and Proprietary Zero-shot Medical Disease Classification from Images

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.23304" class="toolbar-btn" target="_blank">📄 arXiv: 2512.23304v1</a>
  <a href="https://arxiv.org/pdf/2512.23304.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.23304v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.23304v1', 'MedGemma vs GPT-4: Open-Source and Proprietary Zero-shot Medical Disease Classification from Images')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Md. Sazzadul Islam Prottasha, Nabil Walid Rafi

**分类**: cs.CV, cs.AI

**发布日期**: 2025-12-29

**备注**: Accepted for publication in the Journal of Machine Learning and Deep Learning (JMLDL). 9 pages, 9 figures, 10 tables

---

## 💡 一句话要点

**MedGemma在医学图像疾病分类中优于GPT-4，领域微调至关重要**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `医学图像分类` `多模态大模型` `领域微调` `MedGemma` `GPT-4` `低秩适应` `疾病诊断`

## 📋 核心要点

1. 现有通用多模态大模型在医学图像诊断中存在幻觉问题，限制了其临床应用。
2. 论文提出利用领域知识微调开源模型MedGemma，提升其在特定疾病分类任务上的性能。
3. 实验结果表明，微调后的MedGemma在准确率和灵敏度上均优于未微调的GPT-4。

## 📝 摘要（中文）

本研究对比了两种架构迥异的AI模型在医学图像疾病分类中的表现：专门的开源模型MedGemma和专有的多模态大模型GPT-4，用于诊断六种不同的疾病。结果表明，经过低秩适应(LoRA)微调的MedGemma-4b-it模型表现出更优越的诊断能力，平均测试准确率达到80.37%，而未调优的GPT-4为69.58%。此外，MedGemma在高风险临床任务（如癌症和肺炎检测）中表现出明显更高的灵敏度。通过混淆矩阵和分类报告进行的定量分析，全面深入地展示了模型在所有类别中的性能。这些结果强调，领域特定的微调对于最小化临床应用中的幻觉至关重要，使MedGemma成为复杂、基于证据的医学推理的强大工具。

## 🔬 方法详解

**问题定义**：论文旨在解决医学图像疾病分类问题。现有通用多模态大模型（如GPT-4）虽然拥有广泛的知识，但在医学领域缺乏专业知识，容易产生幻觉，导致诊断错误。这限制了它们在临床环境中的可靠应用。

**核心思路**：论文的核心思路是利用领域特定的数据对开源模型MedGemma进行微调，使其更好地适应医学图像的特点和疾病的诊断逻辑。通过微调，模型可以学习到更准确的医学知识，从而减少幻觉，提高诊断准确率。

**技术框架**：整体框架包括两个主要阶段：首先，使用低秩适应(LoRA)方法对MedGemma-4b-it模型进行微调，使其适应医学图像数据。其次，将微调后的MedGemma与未微调的GPT-4进行比较，评估它们在六种不同疾病的分类任务中的性能。评估指标包括准确率、灵敏度、混淆矩阵和分类报告。

**关键创新**：论文的关键创新在于证明了领域特定微调对于提高多模态大模型在医学图像诊断中的性能至关重要。通过对开源模型MedGemma进行微调，使其在特定任务上超越了未微调的专有模型GPT-4，突出了领域知识的重要性。

**关键设计**：论文使用了低秩适应(LoRA)方法进行微调，这是一种参数高效的微调技术，可以在不修改原始模型参数的情况下，通过引入少量可训练的参数来适应新的任务。具体来说，LoRA通过在预训练模型的权重矩阵旁边添加低秩矩阵来实现。此外，论文还仔细选择了用于微调的数据集，并针对不同的疾病类别进行了性能评估。

## 📊 实验亮点

实验结果表明，经过LoRA微调的MedGemma-4b-it模型在六种疾病的平均测试准确率达到80.37%，显著高于未调优的GPT-4的69.58%。尤其在癌症和肺炎等高风险疾病的检测中，MedGemma表现出更高的灵敏度，表明领域微调能够有效提升模型在关键临床任务中的性能。

## 🎯 应用场景

该研究成果可应用于辅助医生进行疾病诊断，尤其是在资源有限的地区，可以利用开源模型和领域微调技术构建低成本、高性能的医学图像诊断系统。未来，该技术有望扩展到更多疾病的诊断，并与其他医疗信息系统集成，提升医疗服务的效率和质量。

## 📄 摘要（原文）

> Multimodal Large Language Models (LLMs) introduce an emerging paradigm for medical imaging by interpreting scans through the lens of extensive clinical knowledge, offering a transformative approach to disease classification. This study presents a critical comparison between two fundamentally different AI architectures: the specialized open-source agent MedGemma and the proprietary large multimodal model GPT-4 for diagnosing six different diseases. The MedGemma-4b-it model, fine-tuned using Low-Rank Adaptation (LoRA), demonstrated superior diagnostic capability by achieving a mean test accuracy of 80.37% compared to 69.58% for the untuned GPT-4. Furthermore, MedGemma exhibited notably higher sensitivity in high-stakes clinical tasks, such as cancer and pneumonia detection. Quantitative analysis via confusion matrices and classification reports provides comprehensive insights into model performance across all categories. These results emphasize that domain-specific fine-tuning is essential for minimizing hallucinations in clinical implementation, positioning MedGemma as a sophisticated tool for complex, evidence-based medical reasoning.

