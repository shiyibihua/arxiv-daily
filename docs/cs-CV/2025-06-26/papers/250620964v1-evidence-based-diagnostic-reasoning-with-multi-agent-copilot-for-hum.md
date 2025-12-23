---
layout: default
title: Evidence-based diagnostic reasoning with multi-agent copilot for human pathology
---

# Evidence-based diagnostic reasoning with multi-agent copilot for human pathology

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.20964" class="toolbar-btn" target="_blank">📄 arXiv: 2506.20964v1</a>
  <a href="https://arxiv.org/pdf/2506.20964.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.20964v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.20964v1', 'Evidence-based diagnostic reasoning with multi-agent copilot for human pathology')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Chengkuan Chen, Luca L. Weishaupt, Drew F. K. Williamson, Richard J. Chen, Tong Ding, Bowen Chen, Anurag Vaidya, Long Phi Le, Guillaume Jaume, Ming Y. Lu, Faisal Mahmood

**分类**: cs.CV, cs.AI

**发布日期**: 2025-06-26

---

## 💡 一句话要点

**提出PathChat+以解决病理学诊断推理不足问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多模态大语言模型` `计算病理学` `自主诊断推理` `全切片成像` `人工智能` `病理特定指令` `图像分析` `差异诊断`

## 📋 核心要点

1. 现有的计算病理学模型主要集中于图像分析，缺乏对自然语言指令和文本背景的整合，导致诊断推理能力不足。
2. 本文提出了PathChat+，一个专为病理学设计的多模态大语言模型，能够处理丰富的病理特定指令和问答数据。
3. 实验结果表明，PathChat+在多个病理基准测试中显著超越了之前的模型，并在开放式差异诊断任务中表现出色。

## 📝 摘要（中文）

病理学正在经历由全切片成像和人工智能驱动的快速数字化转型。尽管基于深度学习的计算病理学取得了显著成功，但传统模型主要集中于图像分析，未能整合自然语言指令或丰富的文本背景。当前的多模态大语言模型在计算病理学中面临训练数据不足、对多图像理解支持不足及缺乏自主诊断推理能力等限制。为了解决这些问题，本文提出了PathChat+，这是一个专为人类病理学设计的新型多模态大语言模型，经过超过100万个多样化的病理特定指令样本和近550万个问答轮次的训练。广泛的评估显示，PathChat+在多个病理基准测试中显著优于之前的PathChat助手，以及其他最先进的通用和病理特定模型。此外，我们还展示了SlideSeek，一个利用PathChat+进行自主评估的多代理AI系统，能够通过迭代的分层诊断推理高效处理千兆像素的全切片图像，并在开放式的差异诊断基准DDxBench上达到高准确率，同时生成可视化的、易于理解的总结报告。

## 🔬 方法详解

**问题定义**：本文旨在解决现有计算病理学模型在图像分析与自然语言处理结合方面的不足，尤其是在自主诊断推理能力上的缺失。

**核心思路**：论文提出的PathChat+通过整合丰富的病理特定指令和问答数据，增强了模型的多模态理解能力，从而提升了诊断推理的准确性和效率。

**技术框架**：PathChat+的整体架构包括数据预处理、模型训练和推理模块。数据预处理阶段负责收集和整理病理特定的指令和问答数据，模型训练阶段则使用深度学习技术进行训练，推理模块则利用训练好的模型进行实际的病理图像分析和诊断推理。

**关键创新**：PathChat+的主要创新在于其训练数据的多样性和丰富性，特别是针对病理学的特定指令样本和问答轮次，这使得模型在处理复杂的病理图像时具备更强的推理能力。

**关键设计**：在模型设计中，采用了特定的损失函数以优化多模态数据的融合效果，同时在网络结构上进行了调整，以适应大规模病理图像的处理需求。

## 📊 实验亮点

实验结果显示，PathChat+在多个病理基准测试中显著优于之前的PathChat助手，且在开放式差异诊断基准DDxBench上达到了高准确率，展示了其在处理复杂病理图像时的卓越性能。

## 🎯 应用场景

该研究的潜在应用领域包括临床病理诊断、医学教育和病理图像分析等。PathChat+和SlideSeek的结合可以提高病理学诊断的自动化水平，减少人为错误，提升诊断效率，未来可能在医疗行业产生深远影响。

## 📄 摘要（原文）

> Pathology is experiencing rapid digital transformation driven by whole-slide imaging and artificial intelligence (AI). While deep learning-based computational pathology has achieved notable success, traditional models primarily focus on image analysis without integrating natural language instruction or rich, text-based context. Current multimodal large language models (MLLMs) in computational pathology face limitations, including insufficient training data, inadequate support and evaluation for multi-image understanding, and a lack of autonomous, diagnostic reasoning capabilities. To address these limitations, we introduce PathChat+, a new MLLM specifically designed for human pathology, trained on over 1 million diverse, pathology-specific instruction samples and nearly 5.5 million question answer turns. Extensive evaluations across diverse pathology benchmarks demonstrated that PathChat+ substantially outperforms the prior PathChat copilot, as well as both state-of-the-art (SOTA) general-purpose and other pathology-specific models. Furthermore, we present SlideSeek, a reasoning-enabled multi-agent AI system leveraging PathChat+ to autonomously evaluate gigapixel whole-slide images (WSIs) through iterative, hierarchical diagnostic reasoning, reaching high accuracy on DDxBench, a challenging open-ended differential diagnosis benchmark, while also capable of generating visually grounded, humanly-interpretable summary reports.

