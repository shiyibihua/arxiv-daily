---
layout: default
title: "Foundation Model-based Evaluation of Neuropsychiatric Disorders: A Lifespan-Inclusive, Multi-Modal, and Multi-Lingual Study"
---

# Foundation Model-based Evaluation of Neuropsychiatric Disorders: A Lifespan-Inclusive, Multi-Modal, and Multi-Lingual Study

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.20948" class="toolbar-btn" target="_blank">📄 arXiv: 2512.20948v1</a>
  <a href="https://arxiv.org/pdf/2512.20948.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.20948v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.20948v1', 'Foundation Model-based Evaluation of Neuropsychiatric Disorders: A Lifespan-Inclusive, Multi-Modal, and Multi-Lingual Study')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zhongren Dong, Haotian Guo, Weixiang Xu, Huan Zhao, Zixing Zhang

**分类**: cs.CL, cs.SD

**发布日期**: 2025-12-24

---

## 💡 一句话要点

**提出FEND框架，用于基于多模态融合和预训练模型评估神经精神疾病。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `神经精神疾病` `多模态融合` `预训练模型` `自然语言处理` `语音识别`

## 📋 核心要点

1. 现有神经精神疾病评估方法缺乏多语言泛化能力和统一评估框架，限制了其应用。
2. FEND框架融合语音和文本模态，利用预训练模型进行多语言、全生命周期的神经精神疾病评估。
3. 实验结果表明，FEND在AD和抑郁症检测中表现良好，但受数据集异质性和模态不平衡影响。

## 📝 摘要（中文）

神经精神疾病，如阿尔茨海默病(AD)、抑郁症和自闭症谱系障碍(ASD)，其特征是语言和声音异常，这为早期检测提供了潜在的生物标志物。尽管多模态方法前景广阔，但多语言泛化和缺乏统一的评估框架等挑战依然存在。为了解决这些问题，我们提出了FEND（基于基础模型的神经精神疾病评估），这是一个综合的多模态框架，集成了语音和文本模态，用于检测整个生命周期的AD、抑郁症和ASD。我们利用跨越英语、中文、希腊语、法语和荷兰语的13个多语言数据集，系统地评估了多模态融合性能。结果表明，多模态融合在AD和抑郁症检测中表现出色，但在ASD中由于数据集异质性而表现不佳。我们还发现模态不平衡是一个普遍问题，多模态融合未能超过最佳单模态模型。跨语料库实验表明，在任务和语言一致的场景中表现出稳健的性能，但在多语言和任务异构设置中性能明显下降。通过提供广泛的基准和对性能影响因素的详细分析，FEND推动了自动化、全生命周期和多语言神经精神疾病评估领域的发展。我们鼓励研究人员采用FEND框架进行公平比较和可重复的研究。

## 🔬 方法详解

**问题定义**：论文旨在解决神经精神疾病（如阿尔茨海默病、抑郁症和自闭症谱系障碍）的自动评估问题。现有方法在多语言环境下的泛化能力不足，且缺乏统一的评估框架，难以进行公平比较和可重复研究。此外，多模态融合方法在实际应用中面临数据集异质性和模态不平衡等挑战。

**核心思路**：论文的核心思路是利用预训练的基础模型，构建一个多模态融合的评估框架（FEND），该框架能够同时处理语音和文本信息，并支持多种语言。通过在多个数据集上进行实验，分析多模态融合的性能，并识别影响性能的关键因素。这样设计的目的是为了提高神经精神疾病评估的准确性和泛化能力，并为未来的研究提供一个统一的基准。

**技术框架**：FEND框架主要包含以下几个模块：1) 数据预处理模块：负责对语音和文本数据进行清洗和标准化。2) 特征提取模块：利用预训练的基础模型（如语音和文本领域的预训练模型）提取语音和文本特征。3) 多模态融合模块：将语音和文本特征进行融合，得到一个综合的特征表示。4) 分类模块：利用分类器（如支持向量机、神经网络等）对融合后的特征进行分类，判断个体是否患有神经精神疾病。

**关键创新**：该论文的关键创新在于提出了一个统一的多模态评估框架（FEND），该框架能够同时处理语音和文本信息，并支持多种语言。此外，论文还对多模态融合的性能进行了深入分析，识别了数据集异质性和模态不平衡等问题，并提出了相应的解决方案。

**关键设计**：论文的关键设计包括：1) 选择合适的预训练模型，以提取高质量的语音和文本特征。2) 设计有效的多模态融合方法，以充分利用语音和文本信息。3) 采用合适的分类器，以提高分类的准确性。4) 通过实验分析，优化框架的参数设置，如学习率、batch size等。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.20948v1/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.20948v1/x2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.20948v1/x3.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

实验结果表明，FEND框架在AD和抑郁症检测中表现出色，但在ASD检测中由于数据集异质性而表现不佳。跨语料库实验表明，在任务和语言一致的场景中表现出稳健的性能，但在多语言和任务异构设置中性能明显下降。研究还发现模态不平衡是一个普遍问题，多模态融合未能超过最佳单模态模型。

## 🎯 应用场景

该研究成果可应用于神经精神疾病的早期筛查和诊断，尤其是在多语言环境下。FEND框架能够为临床医生提供辅助决策支持，提高诊断效率和准确性。此外，该框架还可以用于药物研发和疗效评估，加速神经精神疾病的治疗进程。未来，该研究有望推动个性化医疗的发展，为患者提供更精准的治疗方案。

## 📄 摘要（原文）

> Neuropsychiatric disorders, such as Alzheimer's disease (AD), depression, and autism spectrum disorder (ASD), are characterized by linguistic and acoustic abnormalities, offering potential biomarkers for early detection. Despite the promise of multi-modal approaches, challenges like multi-lingual generalization and the absence of a unified evaluation framework persist. To address these gaps, we propose FEND (Foundation model-based Evaluation of Neuropsychiatric Disorders), a comprehensive multi-modal framework integrating speech and text modalities for detecting AD, depression, and ASD across the lifespan. Leveraging 13 multi-lingual datasets spanning English, Chinese, Greek, French, and Dutch, we systematically evaluate multi-modal fusion performance. Our results show that multi-modal fusion excels in AD and depression detection but underperforms in ASD due to dataset heterogeneity. We also identify modality imbalance as a prevalent issue, where multi-modal fusion fails to surpass the best mono-modal models. Cross-corpus experiments reveal robust performance in task- and language-consistent scenarios but noticeable degradation in multi-lingual and task-heterogeneous settings. By providing extensive benchmarks and a detailed analysis of performance-influencing factors, FEND advances the field of automated, lifespan-inclusive, and multi-lingual neuropsychiatric disorder assessment. We encourage researchers to adopt the FEND framework for fair comparisons and reproducible research.

