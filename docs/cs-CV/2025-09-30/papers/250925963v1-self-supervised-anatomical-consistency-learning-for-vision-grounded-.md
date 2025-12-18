---
layout: default
title: Self-Supervised Anatomical Consistency Learning for Vision-Grounded Medical Report Generation
---

# Self-Supervised Anatomical Consistency Learning for Vision-Grounded Medical Report Generation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.25963" class="toolbar-btn" target="_blank">📄 arXiv: 2509.25963v1</a>
  <a href="https://arxiv.org/pdf/2509.25963.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.25963v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.25963v1', 'Self-Supervised Anatomical Consistency Learning for Vision-Grounded Medical Report Generation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Longzhen Yang, Zhangkai Ni, Ying Wen, Yihang Liu, Lianghua He, Heng Tao Shen

**分类**: cs.CV

**发布日期**: 2025-09-30

**DOI**: [10.1145/3746027.3754913](https://doi.org/10.1145/3746027.3754913)

---

## 💡 一句话要点

**提出自监督解剖一致性学习框架，用于视觉引导的医学报告生成。**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `医学报告生成` `自监督学习` `解剖一致性` `对比学习` `视觉定位`

## 📋 核心要点

1. 现有医学报告生成方法依赖大量专家标注的检测模块，成本高且泛化性受限。
2. 提出自监督解剖一致性学习（SS-ACL），利用文本提示对齐报告与解剖区域，无需人工标注。
3. 实验表明，SS-ACL在词汇准确率和临床有效性方面显著优于现有方法，并在视觉定位任务上表现出色。

## 📝 摘要（中文）

本文提出了一种自监督解剖一致性学习（SS-ACL）框架，用于视觉引导的医学报告生成，旨在生成临床上准确的医学图像描述，并锚定在明确的视觉证据上，以提高可解释性并促进集成到临床工作流程中。现有方法通常依赖于单独训练的检测模块，需要大量的专家标注，导致标注成本高昂，并因数据集之间的病理分布偏差而限制了泛化能力。SS-ACL利用简单的文本提示将生成的报告与相应的解剖区域对齐，无需任何人工标注。该方法构建了一个受人类解剖结构不变的自上而下包含结构启发的层级解剖图，按空间位置组织实体，并递归地重建细粒度的解剖区域，以加强样本内的空间对齐，从而引导注意力图关注文本提示的视觉相关区域。为了进一步增强异常识别的样本间语义对齐，SS-ACL引入了一种基于解剖一致性的区域级对比学习。这些对齐的嵌入作为报告生成的先验，使注意力图能够提供可解释的视觉证据。大量实验表明，SS-ACL在不依赖专家标注的情况下，生成了准确且具有视觉基础的报告，在词汇准确率方面优于现有方法10%，在临床有效性方面优于25%，并在各种下游视觉任务上取得了具有竞争力的性能，在零样本视觉定位方面超过了当前领先的视觉基础模型8%。

## 🔬 方法详解

**问题定义**：医学报告生成旨在根据医学图像生成准确的临床描述，并提供可解释的视觉证据。现有方法依赖于预训练的目标检测器，需要大量的人工标注，成本高昂，且容易受到数据集偏见的影响，泛化能力较差。因此，如何减少对人工标注的依赖，提高模型的泛化能力，是本文要解决的关键问题。

**核心思路**：本文的核心思路是利用自监督学习的方式，通过解剖一致性约束来学习图像和文本之间的对齐关系，从而生成更准确、更可信的医学报告。具体来说，通过构建解剖结构图，并利用对比学习来增强模型对解剖区域的理解，从而引导模型关注与报告相关的视觉区域。

**技术框架**：SS-ACL框架主要包含以下几个模块：1) **解剖结构图构建模块**：构建一个层级的解剖结构图，用于表示不同解剖区域之间的空间关系。2) **区域重建模块**：递归地重建细粒度的解剖区域，以加强样本内的空间对齐。3) **对比学习模块**：引入基于解剖一致性的区域级对比学习，增强样本间的语义对齐。4) **报告生成模块**：利用对齐的嵌入作为先验，生成医学报告。

**关键创新**：该方法最大的创新在于提出了自监督的解剖一致性学习框架，无需人工标注即可学习图像和文本之间的对齐关系。通过构建解剖结构图和利用对比学习，增强了模型对解剖区域的理解，从而生成更准确、更可信的医学报告。与现有方法相比，该方法减少了对人工标注的依赖，提高了模型的泛化能力。

**关键设计**：1) **解剖结构图**：采用层级结构，模拟人体解剖结构，例如从全身到器官再到组织。2) **对比学习损失**：设计区域级别的对比学习损失，鼓励相似解剖区域的嵌入更接近，不同区域的嵌入更远离。3) **注意力机制**：利用学习到的解剖区域嵌入来引导注意力机制，使模型能够关注与报告相关的视觉区域。

## 📊 实验亮点

实验结果表明，SS-ACL在医学报告生成任务上取得了显著的性能提升。在词汇准确率方面，SS-ACL优于现有方法10%；在临床有效性方面，优于现有方法25%。此外，SS-ACL在零样本视觉定位任务上也表现出色，超过了当前领先的视觉基础模型8%。这些结果表明，SS-ACL能够生成更准确、更可信的医学报告，并具有良好的泛化能力。

## 🎯 应用场景

该研究成果可应用于辅助医学诊断、医学报告自动生成、医学图像检索等领域。通过自动生成高质量的医学报告，可以减轻医生的工作负担，提高诊断效率和准确性。此外，该方法还可以用于医学教育和培训，帮助学生更好地理解人体解剖结构和病理特征。未来，该技术有望与临床工作流程深度融合，提升医疗服务的智能化水平。

## 📄 摘要（原文）

> Vision-grounded medical report generation aims to produce clinically accurate descriptions of medical images, anchored in explicit visual evidence to improve interpretability and facilitate integration into clinical workflows. However, existing methods often rely on separately trained detection modules that require extensive expert annotations, introducing high labeling costs and limiting generalizability due to pathology distribution bias across datasets. To address these challenges, we propose Self-Supervised Anatomical Consistency Learning (SS-ACL) -- a novel and annotation-free framework that aligns generated reports with corresponding anatomical regions using simple textual prompts. SS-ACL constructs a hierarchical anatomical graph inspired by the invariant top-down inclusion structure of human anatomy, organizing entities by spatial location. It recursively reconstructs fine-grained anatomical regions to enforce intra-sample spatial alignment, inherently guiding attention maps toward visually relevant areas prompted by text. To further enhance inter-sample semantic alignment for abnormality recognition, SS-ACL introduces a region-level contrastive learning based on anatomical consistency. These aligned embeddings serve as priors for report generation, enabling attention maps to provide interpretable visual evidence. Extensive experiments demonstrate that SS-ACL, without relying on expert annotations, (i) generates accurate and visually grounded reports -- outperforming state-of-the-art methods by 10\% in lexical accuracy and 25\% in clinical efficacy, and (ii) achieves competitive performance on various downstream visual tasks, surpassing current leading visual foundation models by 8\% in zero-shot visual grounding.

