---
layout: default
title: Can Multimodal LLMs See Materials Clearly? A Multimodal Benchmark on Materials Characterization
---

# Can Multimodal LLMs See Materials Clearly? A Multimodal Benchmark on Materials Characterization

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.09307" class="toolbar-btn" target="_blank">📄 arXiv: 2509.09307v1</a>
  <a href="https://arxiv.org/pdf/2509.09307.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.09307v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.09307v1', 'Can Multimodal LLMs See Materials Clearly? A Multimodal Benchmark on Materials Characterization')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zhengzhao Lai, Youbin Zheng, Zhenyang Cai, Haonan Lyu, Jinpu Yang, Hongqing Liang, Yan Hu, Benyou Wang

**分类**: cs.CV, cs.AI, cs.CL, cs.MM

**发布日期**: 2025-09-11

**🔗 代码/项目**: [GITHUB](https://github.com/FreedomIntelligence/MatCha)

---

## 💡 一句话要点

**提出MatCha：材料表征多模态基准，评估MLLM在材料科学图像理解能力**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多模态学习` `材料表征` `图像理解` `大型语言模型` `基准数据集` `材料科学` `计算机视觉`

## 📋 核心要点

1. 现有MLLM在材料科学领域的应用潜力巨大，但对材料表征图像的理解能力不足，缺乏专门的评估基准。
2. 论文构建了MatCha基准，包含1500个问题，覆盖材料研究的四个阶段和21个任务，旨在评估MLLM对材料表征图像的理解能力。
3. 实验结果表明，现有MLLM在MatCha上的表现与人类专家存在显著差距，尤其是在需要高层次专业知识和复杂视觉感知的任务中。

## 📝 摘要（中文）

材料表征是获取材料信息、揭示加工-微观结构-性能关系的基础，对材料设计和优化至关重要。尽管多模态大型语言模型(MLLM)最近在材料科学的生成和预测任务中展现出潜力，但它们理解真实世界表征图像数据的能力仍未得到充分探索。为了弥合这一差距，我们提出了MatCha，这是首个用于材料表征图像理解的基准，包含1500个需要专家级领域知识的问题。MatCha涵盖材料研究的四个关键阶段，包含21个不同的任务，每个任务都旨在反映材料科学家面临的真实挑战。我们对最先进的MLLM在MatCha上的评估表明，与人类专家相比存在显著的性能差距。这些模型在处理需要更高层次专业知识和复杂视觉感知的题目时表现下降。简单的少样本和思维链提示难以缓解这些限制。这些发现表明，现有的MLLM在适应真实世界的材料表征场景方面仍然存在局限性。我们希望MatCha将促进新材料发现和自主科学智能体等领域的未来研究。MatCha可在https://github.com/FreedomIntelligence/MatCha获取。

## 🔬 方法详解

**问题定义**：现有MLLM在材料科学领域展现出潜力，但其对材料表征图像的理解能力，特别是对真实世界复杂图像的理解，缺乏充分的评估和验证。现有方法难以应对需要高层次专业知识和复杂视觉感知的材料表征任务，限制了其在材料科学领域的应用。

**核心思路**：论文的核心思路是构建一个专门用于评估MLLM在材料表征图像理解能力的基准数据集MatCha。通过设计包含不同难度和专业知识要求的任务，全面评估MLLM在材料科学领域的视觉理解能力，并揭示其局限性。

**技术框架**：MatCha基准包含四个关键阶段，涵盖材料研究的典型流程：材料制备、微观结构表征、性能测试和数据分析。每个阶段包含多个任务，共计21个任务，每个任务都包含材料表征图像和对应的问题，问题需要专家级的材料科学知识才能回答。整体流程为：输入材料表征图像和问题，MLLM模型进行推理，输出答案，与标准答案进行对比评估。

**关键创新**：MatCha是首个专门针对材料表征图像理解的基准数据集。它不仅包含大量真实世界的材料表征图像，还设计了需要高层次专业知识和复杂视觉感知的任务，更贴近材料科学家的实际工作场景。此外，MatCha的构建考虑了材料研究的完整流程，覆盖了多个关键阶段。

**关键设计**：MatCha基准包含1500个问题，涵盖扫描电子显微镜(SEM)、透射电子显微镜(TEM)、光学显微镜等多种材料表征技术产生的图像。问题设计涵盖图像识别、目标检测、图像分割、关系推理等多种类型，并根据难度进行分级。论文还尝试了少样本学习和思维链提示等方法来提升MLLM的性能，但效果有限。

## 📊 实验亮点

实验结果表明，现有最先进的MLLM在MatCha基准上的表现远低于人类专家水平，尤其是在需要高层次专业知识和复杂视觉感知的任务中。例如，在某些任务上，MLLM的准确率仅为个位数，表明其在材料表征图像理解方面仍存在显著差距。简单的少样本学习和思维链提示难以有效提升MLLM的性能。

## 🎯 应用场景

MatCha基准的提出，能够促进MLLM在材料科学领域的应用，例如新材料发现、材料性能预测、材料缺陷检测等。通过不断提升MLLM在材料表征图像理解方面的能力，可以加速材料研发进程，降低研发成本，并为自主科学智能体的开发奠定基础。

## 📄 摘要（原文）

> Materials characterization is fundamental to acquiring materials information, revealing the processing-microstructure-property relationships that guide material design and optimization. While multimodal large language models (MLLMs) have recently shown promise in generative and predictive tasks within materials science, their capacity to understand real-world characterization imaging data remains underexplored. To bridge this gap, we present MatCha, the first benchmark for materials characterization image understanding, comprising 1,500 questions that demand expert-level domain expertise. MatCha encompasses four key stages of materials research comprising 21 distinct tasks, each designed to reflect authentic challenges faced by materials scientists. Our evaluation of state-of-the-art MLLMs on MatCha reveals a significant performance gap compared to human experts. These models exhibit degradation when addressing questions requiring higher-level expertise and sophisticated visual perception. Simple few-shot and chain-of-thought prompting struggle to alleviate these limitations. These findings highlight that existing MLLMs still exhibit limited adaptability to real-world materials characterization scenarios. We hope MatCha will facilitate future research in areas such as new material discovery and autonomous scientific agents. MatCha is available at https://github.com/FreedomIntelligence/MatCha.

