---
layout: default
title: LLM Unlearning Without an Expert Curated Dataset
---

# LLM Unlearning Without an Expert Curated Dataset

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.06595" class="toolbar-btn" target="_blank">📄 arXiv: 2508.06595v3</a>
  <a href="https://arxiv.org/pdf/2508.06595.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.06595v3" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.06595v3', 'LLM Unlearning Without an Expert Curated Dataset')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Xiaoyuan Zhu, Muru Zhang, Ollie Liu, Robin Jia, Willie Neiswanger

**分类**: cs.CL, cs.AI, cs.LG

**发布日期**: 2025-08-08 (更新: 2025-10-07)

**🔗 代码/项目**: [GITHUB](https://github.com/xyzhu123/Synthetic_Textbook)

---

## 💡 一句话要点

**提出一种自动化生成遗忘集的方法以解决大语言模型的知识遗忘问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `知识遗忘` `语言模型` `数据合成` `自动化生成` `隐私保护` `模型安全`

## 📋 核心要点

1. 现有的遗忘方法在构建有效的遗忘集方面存在瓶颈，难以实现高效的知识移除。
2. 本文提出了一种自动化生成遗忘集的方法，利用语言模型自身合成教科书风格的数据，简化了遗忘集的构建过程。
3. 实验结果显示，合成数据集在多个领域的遗忘任务中表现优于基线方法，且数据多样性显著提升。

## 📝 摘要（中文）

现代大型语言模型往往编码敏感、有害或受版权保护的知识，因此需要后期遗忘的能力，即在不完全重训练的情况下从模型中移除特定领域的知识。目前，现有的遗忘流程中，构建有效的遗忘集是一个主要瓶颈。本文提出了一种可扩展的自动化方法，通过语言模型自身生成高质量的遗忘集。该方法仅需输入领域名称，通过结构化提示生成教科书风格的数据。实验结果表明，合成数据集在生物安全、网络安全和《哈利·波特》小说的遗忘任务中，表现优于基线合成数据集，并与专家策划的数据集相当。此外，消融研究表明，多步骤生成管道显著提高了数据多样性，从而提升了遗忘的有效性。我们的研究结果表明，合成数据集为广泛新兴领域的实际、可扩展的遗忘提供了有希望的路径。

## 🔬 方法详解

**问题定义**：本文旨在解决大型语言模型中敏感知识的遗忘问题，现有方法在构建有效的遗忘集时面临数据质量和构建效率的挑战。

**核心思路**：我们提出了一种基于语言模型的自动化生成遗忘集的方法，通过结构化提示生成高质量的合成数据，避免了手动干预。

**技术框架**：该方法的整体架构包括输入领域名称、结构化提示生成教科书风格数据、以及最终形成遗忘集的多步骤生成管道。

**关键创新**：最重要的技术创新在于利用语言模型自身生成遗忘集，显著提高了数据的多样性和质量，与传统的手动构建方法相比，效率更高且更具可扩展性。

**关键设计**：在生成过程中，采用了多步骤的提示设计，确保生成数据的多样性和相关性，具体参数设置和损失函数设计未在摘要中详细说明，需参考原文获取更多细节。

## 📊 实验亮点

实验结果表明，合成数据集在生物安全、网络安全和《哈利·波特》小说的遗忘任务中，均优于基线合成数据集，且与专家策划的数据集相当，显示出合成数据集的有效性和实用性。

## 🎯 应用场景

该研究的潜在应用领域包括数据隐私保护、模型安全性提升以及知识管理等。通过有效的知识遗忘机制，能够帮助企业和组织在处理敏感信息时，降低法律风险和道德责任。此外，未来可能在教育、医疗等领域中，促进对特定知识的安全管理和使用。

## 📄 摘要（原文）

> Modern large language models often encode sensitive, harmful, or copyrighted knowledge, raising the need for post-hoc unlearning-the ability to remove specific domains of knowledge from a model without full retraining. A major bottleneck in current unlearning pipelines is constructing effective forget sets-datasets that approximate the target domain and guide the model to forget it. In this work, we introduce a scalable, automated approach to generate high-quality forget sets using language models themselves. Our method synthesizes textbook-style data through a structured prompting pipeline, requiring only a domain name as input. Through experiments on unlearning biosecurity, cybersecurity, and Harry Potter novels, we show that our synthetic datasets consistently outperform the baseline synthetic alternatives and are comparable to the expert-curated ones. Additionally, ablation studies reveal that the multi-step generation pipeline significantly boosts data diversity, which in turn improves unlearning utility. Overall, our findings suggest that synthetic datasets offer a promising path toward practical, scalable unlearning for a wide range of emerging domains without the need for manual intervention. We release our code and dataset at https://github.com/xyzhu123/Synthetic_Textbook.

