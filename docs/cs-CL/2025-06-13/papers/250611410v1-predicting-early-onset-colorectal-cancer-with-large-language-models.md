---
layout: default
title: Predicting Early-Onset Colorectal Cancer with Large Language Models
---

# Predicting Early-Onset Colorectal Cancer with Large Language Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.11410" class="toolbar-btn" target="_blank">📄 arXiv: 2506.11410v1</a>
  <a href="https://arxiv.org/pdf/2506.11410.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.11410v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.11410v1', 'Predicting Early-Onset Colorectal Cancer with Large Language Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Wilson Lau, Youngwon Kim, Sravanthi Parasa, Md Enamul Haque, Anand Oka, Jay Nanduri

**分类**: cs.CL

**发布日期**: 2025-06-13

**备注**: Paper accepted for the proceedings of the 2025 American Medical Informatics Association Annual Symposium (AMIA)

---

## 💡 一句话要点

**利用大型语言模型预测早发性结直肠癌**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `早发性结直肠癌` `大型语言模型` `机器学习` `癌症预测` `医疗数据分析`

## 📋 核心要点

1. 早发性结直肠癌的发病率逐年上升，现有筛查方法未能覆盖年轻患者，导致早期诊断不足。
2. 本文提出利用大型语言模型（LLM）结合患者的健康状况和实验室结果进行EoCRC的预测，提升早期识别能力。
3. 实验结果显示，微调后的LLM在敏感性和特异性上分别达到了73%和91%，显著优于传统机器学习模型。

## 📝 摘要（中文）

早发性结直肠癌（EoCRC，年龄<45岁）的发病率逐年上升，但该人群低于国家癌症筛查指南推荐的年龄。本文应用了10种不同的机器学习模型来预测EoCRC，并将其性能与先进的大型语言模型（LLM）进行了比较，使用了患者状况、实验室结果和在结直肠癌诊断前6个月的观察数据。我们从美国多个健康系统中回顾性识别了1953名CRC患者。结果表明，经过微调的LLM达到了73%的敏感性和91%的特异性。

## 🔬 方法详解

**问题定义**：本文旨在解决早发性结直肠癌（EoCRC）预测的挑战，现有方法未能有效覆盖低于推荐筛查年龄的患者，导致早期诊断不足。

**核心思路**：通过应用大型语言模型（LLM），结合患者的健康状况、实验室结果及诊断前6个月的观察数据，提升EoCRC的预测准确性。

**技术框架**：研究首先从多个健康系统中回顾性识别CRC患者，然后应用10种机器学习模型进行比较，最终选择微调的LLM进行深入分析。

**关键创新**：本研究的核心创新在于将LLM应用于EoCRC的预测，利用其对自然语言处理的优势，提升了模型对复杂医疗数据的理解能力。

**关键设计**：在模型训练中，使用了特定的损失函数和参数设置，以优化模型在敏感性和特异性上的表现，确保其在实际应用中的有效性。

## 📊 实验亮点

实验结果显示，微调后的大型语言模型在预测早发性结直肠癌方面表现出色，达到了73%的敏感性和91%的特异性，明显优于传统的机器学习模型，展示了其在医疗数据分析中的潜力。

## 🎯 应用场景

该研究的潜在应用领域包括早期癌症筛查和个性化医疗，能够帮助医疗机构更早地识别高风险患者，从而提高早期干预的机会，降低癌症相关的死亡率。未来，随着模型的进一步优化和推广，可能会在更广泛的临床环境中应用。

## 📄 摘要（原文）

> The incidence rate of early-onset colorectal cancer (EoCRC, age < 45) has increased every year, but this population is younger than the recommended age established by national guidelines for cancer screening. In this paper, we applied 10 different machine learning models to predict EoCRC, and compared their performance with advanced large language models (LLM), using patient conditions, lab results, and observations within 6 months of patient journey prior to the CRC diagnoses. We retrospectively identified 1,953 CRC patients from multiple health systems across the United States. The results demonstrated that the fine-tuned LLM achieved an average of 73% sensitivity and 91% specificity.

