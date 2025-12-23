---
layout: default
title: PsyLite Technical Report
---

# PsyLite Technical Report

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.21536" class="toolbar-btn" target="_blank">📄 arXiv: 2506.21536v1</a>
  <a href="https://arxiv.org/pdf/2506.21536.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.21536v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.21536v1', 'PsyLite Technical Report')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Fangjun Ding, Renyu Zhang, Xinyu Feng, Chengye Xie, Zheng Zhang, Yanting Zhang

**分类**: cs.AI, cs.HC

**发布日期**: 2025-06-26

---

## 💡 一句话要点

**提出PsyLite以解决心理咨询对话安全与轻量化部署问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱六：视频提取与匹配 (Video Extraction)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `心理咨询` `大语言模型` `对话安全` `轻量化部署` `深度推理` `条件RAG` `量化技术`

## 📋 核心要点

1. 现有的AI心理咨询模型在对话安全性和细节处理上存在明显不足，难以满足实际应用需求。
2. PsyLite通过两阶段训练策略和创新的条件RAG设计，提升了心理咨询的深度推理和对话安全能力。
3. 实验结果表明，PsyLite在心理咨询专业性和对话安全性方面显著优于基线模型，尤其在专业性评估中提升了47.6%。

## 📝 摘要（中文）

随着数字技术的快速发展，基于AI的心理咨询逐渐成为心理健康领域的重要研究方向。然而，现有模型在对话安全性、细节场景处理和轻量化部署方面仍存在不足。为了解决这些问题，本研究提出了PsyLite，这是一种基于InternLM2.5-7B-chat的轻量级心理咨询大语言模型代理。通过混合蒸馏数据微调和ORPO偏好优化的两阶段训练策略，PsyLite增强了模型的深度推理能力、心理咨询能力和安全对话能力。经过Ollama和Open WebUI的部署，创建了自定义工作流，并设计了创新的条件RAG，在心理咨询中适时引入幽默元素，以增强用户体验并降低危险请求，从而加强对话安全性。评估结果显示，PsyLite在中文通用评估、心理咨询专业评估和对话安全评估中均优于基线模型，尤其在心理咨询专业性方面提升了47.6%。

## 🔬 方法详解

**问题定义**：本研究旨在解决现有AI心理咨询模型在对话安全性、细节场景处理和轻量化部署方面的不足，尤其是在资源受限环境中的应用挑战。

**核心思路**：论文提出的PsyLite模型采用了混合蒸馏数据微调和ORPO偏好优化的两阶段训练策略，旨在增强模型的推理能力和安全对话能力，同时通过引入幽默元素提升用户体验。

**技术框架**：PsyLite的整体架构包括基础模型InternLM2.5-7B-chat，经过两阶段训练后进行Ollama和Open WebUI的部署，形成自定义工作流。关键模块包括数据微调、偏好优化和条件RAG设计。

**关键创新**：PsyLite的创新点在于引入条件RAG设计，能够在心理咨询中适时加入幽默元素，增强用户体验并降低危险请求，显著提升对话安全性。

**关键设计**：模型采用了量化技术（GGUF q4_k_m），使得在仅需5GB内存的情况下即可实现低硬件部署，适合资源受限环境的应用。

## 📊 实验亮点

PsyLite在多个评估指标上均优于基线模型，尤其在心理咨询专业性评估中提升了47.6%，在对话安全性评估中提升了2.4%。这些结果表明，PsyLite在实际应用中具有显著的性能优势。

## 🎯 应用场景

PsyLite的研究成果在心理健康领域具有广泛的应用潜力，尤其适用于需要高效、安全的心理咨询服务的场景。其轻量化特性使得在资源受限的环境中也能有效部署，为心理咨询的普及和可及性提供了新的解决方案。

## 📄 摘要（原文）

> With the rapid development of digital technology, AI-driven psychological counseling has gradually become an important research direction in the field of mental health. However, existing models still have deficiencies in dialogue safety, detailed scenario handling, and lightweight deployment. To address these issues, this study proposes PsyLite, a lightweight psychological counseling large language model agent developed based on the base model InternLM2.5-7B-chat. Through a two-stage training strategy (hybrid distillation data fine-tuning and ORPO preference optimization), PsyLite enhances the model's deep-reasoning ability, psychological counseling ability, and safe dialogue ability. After deployment using Ollama and Open WebUI, a custom workflow is created with Pipelines. An innovative conditional RAG is designed to introduce crosstalk humor elements at appropriate times during psychological counseling to enhance user experience and decline dangerous requests to strengthen dialogue safety. Evaluations show that PsyLite outperforms the baseline models in the Chinese general evaluation (CEval), psychological counseling professional evaluation (CPsyCounE), and dialogue safety evaluation (SafeDialBench), particularly in psychological counseling professionalism (CPsyCounE score improvement of 47.6\%) and dialogue safety (\safe{} score improvement of 2.4\%). Additionally, the model uses quantization technology (GGUF q4\_k\_m) to achieve low hardware deployment (5GB memory is sufficient for operation), providing a feasible solution for psychological counseling applications in resource-constrained environments.

