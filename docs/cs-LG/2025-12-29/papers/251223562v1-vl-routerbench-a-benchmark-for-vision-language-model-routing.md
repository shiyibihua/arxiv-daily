---
layout: default
title: "VL-RouterBench: A Benchmark for Vision-Language Model Routing"
---

# VL-RouterBench: A Benchmark for Vision-Language Model Routing

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.23562" class="toolbar-btn" target="_blank">📄 arXiv: 2512.23562v1</a>
  <a href="https://arxiv.org/pdf/2512.23562.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.23562v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.23562v1', 'VL-RouterBench: A Benchmark for Vision-Language Model Routing')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zhehao Huang, Baijiong Lin, Jingyuan Zhang, Jingying Wang, Yuhang Liu, Ning Lu, Tao Li, Xiaolin Huang

**分类**: cs.LG, cs.AI, cs.CL

**发布日期**: 2025-12-29

---

## 💡 一句话要点

**提出VL-RouterBench，用于系统评估视觉-语言模型路由系统的性能。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `视觉-语言模型` `多模型路由` `基准测试` `性能评估` `多模态学习`

## 📋 核心要点

1. 现有VLM路由评估缺乏系统性、可复现的基准，难以有效衡量不同路由策略的优劣。
2. VL-RouterBench基于VLM的推理日志构建质量和成本矩阵，全面评估路由系统的性能。
3. 实验表明，现有最佳路由器与理想状态仍有差距，未来可通过优化视觉和文本建模提升性能。

## 📝 摘要（中文）

多模型路由已从工程技术发展成为关键基础设施，但现有工作缺乏系统性的、可复现的基准来评估视觉-语言模型（VLM）。我们提出了VL-RouterBench，旨在系统地评估VLM路由系统的整体能力。该基准基于VLM的原始推理和评分日志，构建样本-模型对的质量和成本矩阵。在规模上，VL-RouterBench涵盖3个任务组的14个数据集，共计30,540个样本，包括15个开源模型和2个API模型，产生519,180个样本-模型对，总输入-输出token量为34,494,977。评估协议联合衡量平均准确率、平均成本和吞吐量，并从归一化成本和准确率的调和平均值构建排名分数，以实现跨路由器配置和成本预算的比较。在该基准上，我们评估了10种路由方法和基线，观察到显著的可路由性增益，但目前最好的路由器与理想的Oracle之间仍存在明显差距，表明通过更精细的视觉线索和文本结构建模，路由器架构仍有很大的改进空间。我们将开源完整的数据构建和评估工具链，以促进多模态路由研究中的可比性、可复现性和实际部署。

## 🔬 方法详解

**问题定义**：论文旨在解决视觉-语言模型（VLM）路由系统缺乏系统性、可复现的评估基准的问题。现有的VLM路由研究难以进行公平比较和有效优化，阻碍了该领域的进一步发展。缺乏统一的评估标准导致研究结果难以推广和应用。

**核心思路**：论文的核心思路是构建一个全面的基准测试平台VL-RouterBench，该平台基于VLM的原始推理和评分日志，构建样本-模型对的质量和成本矩阵。通过综合考虑准确率、成本和吞吐量，为VLM路由系统的性能评估提供了一个客观、可复现的框架。

**技术框架**：VL-RouterBench的整体框架包括以下几个主要模块：1) 数据集构建：收集涵盖多种任务的14个数据集，共计30,540个样本。2) 模型集成：集成15个开源模型和2个API模型，形成包含519,180个样本-模型对的测试集。3) 评估指标：定义平均准确率、平均成本和吞吐量等评估指标，并构建基于归一化成本和准确率调和平均值的排名分数。4) 路由方法评估：评估10种路由方法和基线，并与理想的Oracle进行比较。

**关键创新**：VL-RouterBench的关键创新在于其系统性和全面性。它不仅提供了大规模的测试数据集和多种VLM模型，还定义了一套综合性的评估指标，能够全面衡量VLM路由系统的性能。此外，VL-RouterBench还开源了完整的数据构建和评估工具链，促进了研究的可比性、可复现性和实际部署。

**关键设计**：VL-RouterBench的关键设计包括：1) 数据集的选择：选择涵盖多种任务的数据集，以保证评估的全面性。2) 模型的集成：集成多种开源模型和API模型，以覆盖不同的模型架构和性能水平。3) 评估指标的定义：定义平均准确率、平均成本和吞吐量等评估指标，以综合衡量VLM路由系统的性能。4) 排名分数的构建：构建基于归一化成本和准确率调和平均值的排名分数，以实现跨路由器配置和成本预算的比较。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.23562v1/_figs/comprehensive_comparison_best_arxiv.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.23562v1/_figs/pipeline.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.23562v1/_figs/data_distribution.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

在VL-RouterBench上评估了10种路由方法和基线，结果显示现有最佳路由器与理想的Oracle之间仍存在明显差距，表明VLM路由技术仍有很大的提升空间。该基准的发布为后续研究提供了一个统一的评估平台，有助于推动VLM路由技术的快速发展。

## 🎯 应用场景

VL-RouterBench可应用于多模态智能客服、智能文档处理、自动驾驶等领域。通过优化VLM路由策略，可以降低计算成本，提高响应速度和准确率，从而提升用户体验和系统效率。该基准的开源将促进VLM路由技术的进一步发展和应用。

## 📄 摘要（原文）

> Multi-model routing has evolved from an engineering technique into essential infrastructure, yet existing work lacks a systematic, reproducible benchmark for evaluating vision-language models (VLMs). We present VL-RouterBench to assess the overall capability of VLM routing systems systematically. The benchmark is grounded in raw inference and scoring logs from VLMs and constructs quality and cost matrices over sample-model pairs. In scale, VL-RouterBench covers 14 datasets across 3 task groups, totaling 30,540 samples, and includes 15 open-source models and 2 API models, yielding 519,180 sample-model pairs and a total input-output token volume of 34,494,977. The evaluation protocol jointly measures average accuracy, average cost, and throughput, and builds a ranking score from the harmonic mean of normalized cost and accuracy to enable comparison across router configurations and cost budgets. On this benchmark, we evaluate 10 routing methods and baselines and observe a significant routability gain, while the best current routers still show a clear gap to the ideal Oracle, indicating considerable room for improvement in router architecture through finer visual cues and modeling of textual structure. We will open-source the complete data construction and evaluation toolchain to promote comparability, reproducibility, and practical deployment in multimodal routing research.

