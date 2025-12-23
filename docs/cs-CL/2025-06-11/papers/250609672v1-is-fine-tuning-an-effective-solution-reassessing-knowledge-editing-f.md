---
layout: default
title: Is Fine-Tuning an Effective Solution? Reassessing Knowledge Editing for Unstructured Data
---

# Is Fine-Tuning an Effective Solution? Reassessing Knowledge Editing for Unstructured Data

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.09672" class="toolbar-btn" target="_blank">📄 arXiv: 2506.09672v1</a>
  <a href="https://arxiv.org/pdf/2506.09672.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.09672v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.09672v1', 'Is Fine-Tuning an Effective Solution? Reassessing Knowledge Editing for Unstructured Data')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Hao Xiong, Chuanyuan Tan, Wenliang Chen

**分类**: cs.CL, cs.AI

**发布日期**: 2025-06-11

---

## 💡 一句话要点

**提出Fine-Tuning方法以解决无结构知识编辑的局限性**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `无结构知识编辑` `微调方法` `局部性评估` `数据集构建` `性能优化` `自然语言处理` `知识更新`

## 📋 核心要点

1. 现有的无结构知识编辑方法存在局部性评估不足和微调方法异常失败的问题。
2. 本文通过构建新的数据集，提出了一种系统评估后编辑模型局部性的方法，并优化了微调方法的训练策略。
3. 实验结果显示，优化后的FT-UKE方法在性能上超越了现有最先进技术，尤其在批量编辑场景中表现更为突出。

## 📝 摘要（中文）

无结构知识编辑（UKE）对于更新大型语言模型（LLMs）的相关知识至关重要，尤其是在处理长文本和自由格式文本时。尽管已有研究提出了有效的方法并进行了测试，但仍存在一些问题：缺乏对UKE的局部性评估，以及基于微调（FT）的方法在UKE中的异常失败。为了解决这些问题，本文构建了两个数据集UnKEBench-Loc和AKEW-Loc（CF），通过扩展现有的UKE数据集，提供了系统评估后编辑模型局部性的基础。此外，研究识别了四个可能影响FT方法性能的因素，并进行了实验以确定FT方法在UKE任务中的最佳训练方式。实验结果表明，经过优化设置的FT-UKE方法表现优异，超越了现有的最先进技术（SOTA），在批量编辑场景中，FT-UKE的优势随着批量大小的增加而增强，平均指标提升幅度从+6.78%扩大至+10.80%。

## 🔬 方法详解

**问题定义**：本文旨在解决无结构知识编辑（UKE）中现有方法的局限性，尤其是缺乏局部性评估和微调方法的异常失败问题。

**核心思路**：通过构建新的数据集并识别影响微调方法性能的关键因素，本文提出了一种优化的训练策略，以提升UKE任务的效果。

**技术框架**：整体架构包括数据集构建、局部性评估、微调方法优化和实验验证四个主要模块。首先，构建UnKEBench-Loc和AKEW-Loc（CF）数据集以支持局部性测试；其次，识别影响性能的四个因素；最后，进行实验以验证优化后的微调方法。

**关键创新**：本文的主要创新在于系统性地评估了后编辑模型的局部性，并提出了一种经过优化的微调方法FT-UKE，显著提升了UKE任务的性能，超越了现有的最先进技术。

**关键设计**：在实验中，设置了多个关键参数，并设计了适合UKE任务的损失函数和网络结构，以确保微调方法的有效性和稳定性。具体的参数设置和网络结构细节在实验部分进行了详细描述。

## 📊 实验亮点

实验结果显示，优化后的FT-UKE方法在性能上显著优于现有最先进技术，尤其在批量编辑场景中，随着批量大小的增加，FT-UKE的优势从+6.78%提升至+10.80%，展现出强大的扩展性和有效性。

## 🎯 应用场景

该研究的潜在应用领域包括自然语言处理、知识图谱更新和智能问答系统等。通过提升无结构知识编辑的效果，能够更好地支持实时知识更新和信息检索，具有重要的实际价值和广泛的应用前景。

## 📄 摘要（原文）

> Unstructured Knowledge Editing (UKE) is crucial for updating the relevant knowledge of large language models (LLMs). It focuses on unstructured inputs, such as long or free-form texts, which are common forms of real-world knowledge. Although previous studies have proposed effective methods and tested them, some issues exist: (1) Lack of Locality evaluation for UKE, and (2) Abnormal failure of fine-tuning (FT) based methods for UKE. To address these issues, we first construct two datasets, UnKEBench-Loc and AKEW-Loc (CF), by extending two existing UKE datasets with locality test data from the unstructured and structured views. This enables a systematic evaluation of the Locality of post-edited models. Furthermore, we identify four factors that may affect the performance of FT-based methods. Based on these factors, we conduct experiments to determine how the well-performing FT-based methods should be trained for the UKE task, providing a training recipe for future research. Our experimental results indicate that the FT-based method with the optimal setting (FT-UKE) is surprisingly strong, outperforming the existing state-of-the-art (SOTA). In batch editing scenarios, FT-UKE shows strong performance as well, with its advantage over SOTA methods increasing as the batch size grows, expanding the average metric lead from +6.78% to +10.80%

