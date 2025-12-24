---
layout: default
title: Apriel-Nemotron-15B-Thinker
---

# Apriel-Nemotron-15B-Thinker

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.10948" class="toolbar-btn" target="_blank">📄 arXiv: 2508.10948v1</a>
  <a href="https://arxiv.org/pdf/2508.10948.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.10948v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.10948v1', 'Apriel-Nemotron-15B-Thinker')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Shruthan Radhakrishna, Soham Parikh, Gopal Sarda, Anil Turkkan, Quaizar Vohra, Raymond Li, Dhruv Jhamb, Kelechi Ogueji, Aanjaneya Shukla, Oluwanifemi Bamgbose, Toby Liang, Luke Kumar, Oleksiy Ostapenko, Shiva Krishna Reddy Malay, Aman Tiwari, Tara Bogavelli, Vikas Yadav, Jash Mehta, Saloni Mittal, Akshay Kalkunte, Pulkit Pattnaik, Khalil Slimi, Anirudh Sreeram, Jishnu Nair, Akintunde Oladipo, Shashank Maiya, Khyati Mahajan, Rishabh Maheshwary, Masoud Hashemi, Sai Rajeswar Mudumba, Sathwik Tejaswi Madhusudhan, Torsten Scholak, Sebastien Paquet, Sagar Davasam, Srinivas Sunkara

**分类**: cs.LG, cs.AI

**发布日期**: 2025-08-13

---

## 💡 一句话要点

**提出Apriel-Nemotron-15B-Thinker以降低大语言模型的内存消耗**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `内存优化` `强化学习` `监督微调` `企业应用`

## 📋 核心要点

1. 现有大型语言模型在内存和计算成本上存在显著挑战，限制了其在企业中的应用。
2. 提出的Apriel-Nemotron-15B-Thinker模型通过四阶段训练流程，显著降低内存占用，同时保持高性能。
3. 实验结果表明，该模型在多个基准测试中表现优异，超越了参数更多的竞争对手。

## 📝 摘要（中文）

尽管大型语言模型（LLMs）在代码、数学及其他企业任务中展现了卓越的推理能力，但其显著的内存和计算成本常常限制了其在实际企业环境中的应用。为此，我们提出了Apriel-Nemotron-15B-Thinker，这是ServiceNow Apriel SLM系列中的一个150亿参数模型，它在性能上与中型最先进模型（如o1-mini、QWQ32B和EXAONE-Deep-32B）相当，同时内存占用仅为这些替代方案的一半。Apriel-Nemotron-15B-Thinker模型经过四个阶段的训练流程，包括基础模型放大、持续预训练、监督微调（SFT）和使用GRPO的强化学习。全面评估显示，尽管模型参数少于32亿的对手，Apriel-Nemotron-15B-Thinker的性能仍然匹配或超越了它们。

## 🔬 方法详解

**问题定义**：论文旨在解决大型语言模型在实际应用中面临的高内存和计算成本问题。现有方法如o1-mini、QWQ32B和EXAONE-Deep-32B虽然性能优越，但内存占用过高，限制了其广泛应用。

**核心思路**：Apriel-Nemotron-15B-Thinker通过优化模型架构和训练流程，降低内存占用，同时保持与更大模型相当的推理能力。这种设计旨在实现高效的计算资源利用。

**技术框架**：该模型的训练流程分为四个阶段：1) 基础模型放大，2) 持续预训练，3) 监督微调（SFT），4) 使用GRPO进行强化学习。每个阶段都旨在逐步提升模型的性能和适应性。

**关键创新**：最重要的创新在于模型的参数优化和训练策略，使得在仅150亿参数的情况下，模型性能能够与32亿参数的模型相媲美。这一设计显著降低了内存需求。

**关键设计**：在训练过程中，采用了特定的损失函数和网络结构设计，以确保模型在不同任务中的泛化能力和推理准确性。具体的参数设置和训练细节在论文中有详细描述。

## 📊 实验亮点

实验结果显示，Apriel-Nemotron-15B-Thinker在多个基准测试中表现优异，性能与32亿参数的模型相当，且内存占用仅为其一半。这一成果表明，模型在保持高效性能的同时，成功实现了资源的优化利用。

## 🎯 应用场景

Apriel-Nemotron-15B-Thinker模型具有广泛的应用潜力，尤其是在需要高效推理和低内存占用的企业环境中。它可以被应用于自动化客服、智能文档处理和数据分析等领域，帮助企业提升效率并降低成本。未来，该模型的设计理念可能会推动更多高效模型的研究与开发。

## 📄 摘要（原文）

> While large language models (LLMs) have achieved remarkable reasoning capabilities across domains like code, math and other enterprise tasks, their significant memory and computational costs often preclude their use in practical enterprise settings. To this end, we introduce Apriel-Nemotron-15B-Thinker, a 15-billion parameter model in the ServiceNow Apriel SLM series that achieves performance against medium sized state-of-the-art models such as o1-mini, QWQ32B, and EXAONE-Deep-32B while maintaining only half the memory footprint of those alternatives. Apriel-Nemotron-15B-Thinker model is trained in a four stage training pipeline including 1) Base Model upscaling, 2) Continual Pre-training 3) Supervised Fine-tuning (SFT) and 4) Reinforcement Learning using GRPO. Comprehensive evaluations across a diverse suite of benchmarks consistently demonstrate that our Apriel-Nemotron-15B-Thinker model matches or exceeds the performance of its 32-billion parameter counterparts, despite being less than half their size.

