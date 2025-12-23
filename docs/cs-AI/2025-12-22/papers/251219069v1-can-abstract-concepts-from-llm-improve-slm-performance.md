---
layout: default
title: Can abstract concepts from LLM improve SLM performance?
---

# Can abstract concepts from LLM improve SLM performance?

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.19069" class="toolbar-btn" target="_blank">📄 arXiv: 2512.19069v1</a>
  <a href="https://arxiv.org/pdf/2512.19069.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.19069v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.19069v1', 'Can abstract concepts from LLM improve SLM performance?')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Siddharth Tandon

**分类**: cs.AI

**发布日期**: 2025-12-22

---

## 💡 一句话要点

**利用LLM抽象概念提升SLM性能，实现推理时动态调整**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `小型语言模型` `知识迁移` `steering vectors` `推理优化` `模型压缩` `资源受限设备`

## 📋 核心要点

1. 现有模型压缩方法（量化、剪枝等）部署复杂，需要大量实验和基础设施支持。
2. 论文提出将LLM中的高级概念（steering vectors）迁移到SLM，提升SLM的性能。
3. 实验表明，该方法可有效提升不同SLM家族（Phi, Llama, Qwen）的性能，Qwen3-0.6B准确率提升7-15%。

## 📝 摘要（中文）

大型语言模型(LLM)在各种任务中表现出色，但将其部署在资源受限的设备上仍然具有挑战性。量化、剪枝和蒸馏等现有方法可以减少内存占用，但通常需要大量的实验和仔细的基础设施设计。本文利用现有的从大型模型中提取高级概念（表示为steering vectors）的技术，研究它们在推理时对小型语言模型(SLM)的可迁移性。通过大量的实验证明，这些概念可以有效地转移到更小的模型，而不管它们的家族（例如，Phi，Llama，Qwen），从而提高各种任务的性能。此外，本文引入了推理时缩放，通过动态调整steering intensity来增强性能，从而使Qwen3-0.6B的准确率提高了7-15%。

## 🔬 方法详解

**问题定义**：论文旨在解决大型语言模型（LLM）难以在资源受限设备上部署的问题。现有模型压缩方法，如量化、剪枝和蒸馏，虽然可以减小模型体积，但通常需要大量的实验和复杂的工程设计，部署成本高昂。

**核心思路**：论文的核心思路是将LLM中学习到的高级抽象概念（steering vectors）迁移到小型语言模型（SLM）中，从而提升SLM的性能，而无需对SLM进行额外的训练或微调。这种方法旨在利用LLM的知识，以一种更轻量级的方式增强SLM的能力。

**技术框架**：该方法主要包含两个阶段：1) 从LLM中提取steering vectors，这些vectors代表了LLM学习到的高级概念。2) 在SLM的推理过程中，将这些steering vectors注入到SLM的激活中，从而引导SLM的输出。此外，论文还引入了推理时缩放，通过动态调整steering intensity来进一步优化性能。

**关键创新**：该方法最重要的创新点在于将LLM的抽象概念以steering vectors的形式迁移到SLM，实现知识迁移。与传统的模型蒸馏方法不同，该方法不需要训练SLM，而是直接在推理时注入知识，降低了计算成本。此外，推理时缩放机制允许动态调整steering intensity，进一步提升了性能。

**关键设计**：steering vectors的提取方式未知，论文中没有详细描述。推理时缩放的关键在于确定合适的steering intensity。论文通过实验确定了最佳的缩放因子，但具体的优化算法未知。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.19069v1/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.19069v1/x2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.19069v1/x3.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

实验结果表明，该方法可以有效地将LLM的抽象概念迁移到SLM，并显著提升SLM在各种任务上的性能。对于Qwen3-0.6B模型，通过引入推理时缩放，准确率提高了7-15%。该方法适用于不同的SLM家族，例如Phi, Llama和Qwen，具有较强的通用性。

## 🎯 应用场景

该研究成果可应用于各种资源受限的场景，例如移动设备、嵌入式系统和边缘计算设备。通过将LLM的知识迁移到SLM，可以在这些设备上部署更智能的应用，例如智能助手、机器翻译和文本生成。该方法还可以用于提升现有SLM的性能，而无需重新训练模型。

## 📄 摘要（原文）

> Large language models (LLMs) excel at diverse tasks, but their deployment on resource-constrained devices remains challenging. Existing methods like quantization, pruning, and distillation can reduce memory footprint but often demand extensive experimentation and careful infrastructure design. Leveraging existing techniques for extracting high-level concepts (represented as steering vectors) from larger models, we investigate their transferability to smaller language models (SLM) during inference. We demonstrate through extensive experimentation that these concepts can be effectively transferred to smaller models, irrespective of their family (e.g., Phi, Llama, Qwen), leading to performance improvements across a wide range of tasks. Furthermore, we introduce inference-time scaling to enhance performance by dynamically adjusting the steering intensity which has resulted in a 7-15\% of accuracy improvement for Qwen3-0.6B.

