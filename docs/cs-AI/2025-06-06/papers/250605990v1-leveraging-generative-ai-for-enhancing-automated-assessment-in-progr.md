---
layout: default
title: Leveraging Generative AI for Enhancing Automated Assessment in Programming Education Contests
---

# Leveraging Generative AI for Enhancing Automated Assessment in Programming Education Contests

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.05990" class="toolbar-btn" target="_blank">📄 arXiv: 2506.05990v1</a>
  <a href="https://arxiv.org/pdf/2506.05990.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.05990v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.05990v1', 'Leveraging Generative AI for Enhancing Automated Assessment in Programming Education Contests')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Stefan Dascalescu, Adrian Marius Dumitran, Mihai Alexandru Vasiluta

**分类**: cs.SE, cs.AI, cs.CY, cs.LG

**发布日期**: 2025-06-06

**备注**: 11 pages, 2 chart pies, 1 figure Pre-print version Accepted at BEA 2025

---

## 💡 一句话要点

**提出基于生成式AI的自动化编程评估测试用例生成方法**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `生成式AI` `自动化评估` `编程教育` `测试用例生成` `自然语言处理` `教育技术` `算法评估`

## 📋 核心要点

1. 现有方法在生成高质量测试用例时资源消耗大，且难以全面覆盖编程解决方案的评估需求。
2. 论文提出利用生成式AI技术，自动生成高质量的测试用例，从而减轻教育者的负担并提高评估效率。
3. 实验结果显示，AI生成的测试用例在67%的情况下识别出未被发现的错误，显著提升了评估的准确性和全面性。

## 📝 摘要（中文）

竞争性编程竞赛在培养学习者的计算思维和算法技能方面发挥着重要作用。然而，为有效评估编程解决方案而生成全面的测试用例仍然是资源密集且具有挑战性的任务。本文提出了一种创新的自然语言处理驱动的方法，利用生成式AI（大型语言模型）自动创建高质量的测试用例。我们在多个数据集上进行了广泛评估，包括25年的罗马尼亚信息学奥林匹克（OJI）数据、Kilonova.ro平台上的近期竞赛以及国际信息学团队奥林匹克（IIOT）。结果表明，AI生成的测试用例显著提升了评估质量，特别是在67%的OJI五年级编程问题中识别出了之前未发现的错误。这些改进凸显了我们技术在形成性评估中的补充教育价值。

## 🔬 方法详解

**问题定义**：本文旨在解决在编程教育竞赛中生成全面且高质量的测试用例这一资源密集型问题。现有方法往往难以满足评估需求，导致评估效果不佳。

**核心思路**：论文的核心思路是利用生成式AI，特别是大型语言模型，自动生成测试用例。这种设计旨在通过AI的强大生成能力，减少人工干预，提高测试用例的多样性和质量。

**技术框架**：整体架构包括数据收集、模型训练和测试用例生成三个主要模块。首先，收集历史竞赛数据以训练生成模型；然后，利用训练好的模型生成新的测试用例；最后，对生成的用例进行评估和优化。

**关键创新**：最重要的技术创新在于将生成式AI应用于测试用例的自动生成，显著提高了测试用例的质量和覆盖率。这与传统的手动生成方法形成鲜明对比，后者往往效率低下且容易遗漏重要场景。

**关键设计**：在模型训练过程中，采用了特定的损失函数以优化生成用例的质量，并通过调节模型参数来提高生成的多样性和准确性。此外，使用了多种数据增强技术以丰富训练数据集。

## 📊 实验亮点

实验结果显示，AI生成的测试用例在67%的OJI五年级编程问题中识别出未被发现的错误，显著提升了评估的准确性。这一成果表明，生成式AI在编程教育评估中的应用具有重要的实际价值和潜力。

## 🎯 应用场景

该研究的潜在应用领域包括教育技术、在线编程竞赛平台和自动化评估工具。通过提供高质量的测试用例生成，教育者可以更有效地评估学生的编程能力，减轻工作负担，并深入了解学习者的表现。未来，该技术有望在更广泛的教育场景中推广应用，提升整体教育质量。

## 📄 摘要（原文）

> Competitive programming contests play a crucial role in cultivating computational thinking and algorithmic skills among learners. However, generating comprehensive test cases to effectively assess programming solutions remains resource-intensive and challenging for educators. This paper introduces an innovative NLP-driven method leveraging generative AI (large language models) to automate the creation of high-quality test cases for competitive programming assessments. We extensively evaluated our approach on diverse datasets, including 25 years of Romanian Informatics Olympiad (OJI) data for 5th graders, recent competitions hosted on the Kilonova.ro platform, and the International Informatics Olympiad in Teams (IIOT). Our results demonstrate that AI-generated test cases substantially enhanced assessments, notably identifying previously undetected errors in 67% of the OJI 5th grade programming problems. These improvements underscore the complementary educational value of our technique in formative assessment contexts. By openly sharing our prompts, translated datasets, and methodologies, we offer practical NLP-based tools that educators and contest organizers can readily integrate to enhance assessment quality, reduce workload, and deepen insights into learner performance.

