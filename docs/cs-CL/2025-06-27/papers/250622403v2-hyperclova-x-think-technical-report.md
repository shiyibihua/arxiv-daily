---
layout: default
title: HyperCLOVA X THINK Technical Report
---

# HyperCLOVA X THINK Technical Report

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.22403" class="toolbar-btn" target="_blank">📄 arXiv: 2506.22403v2</a>
  <a href="https://arxiv.org/pdf/2506.22403.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.22403v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.22403v2', 'HyperCLOVA X THINK Technical Report')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: NAVER Cloud HyperCLOVA X Team

**分类**: cs.CL, cs.AI

**发布日期**: 2025-06-27 (更新: 2025-07-01)

**备注**: 50 pages, 13 figures; fixed figures in the appendix

---

## 💡 一句话要点

**提出HyperCLOVA X THINK以增强推理能力的语言模型**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `推理能力` `双语一致性` `强化学习` `上下文处理` `韩语应用` `模型蒸馏` `计算-内存平衡`

## 📋 核心要点

1. 现有大型语言模型在推理能力和双语一致性方面存在不足，尤其是在特定语言和领域的应用中。
2. HyperCLOVA X THINK通过计算-内存平衡的Peri-LN Transformer架构和三阶段课程预训练，显著提升了推理能力和上下文处理能力。
3. 在多个韩国基准测试中，HyperCLOVA X THINK的表现优于同类模型，并在KCSAT STEM基准测试中与GPT-4.1相当。

## 📝 摘要（中文）

我们介绍了HyperCLOVA X THINK，这是HyperCLOVA X系列中首个专注于推理的大型语言模型，预训练数据量约为6万亿高质量韩文和英文标记，并通过针对性的合成韩文数据进行增强。该模型采用计算-内存平衡的Peri-LN Transformer架构，经过三阶段课程预训练，扩展上下文窗口至128K标记，并通过可验证奖励的强化学习进行监督微调，支持详细推理和简洁回答模式。在韩国相关基准测试中，该模型表现出色，同时保持了强大的双语一致性和翻译质量。此外，视觉增强变体在KCSAT STEM基准测试中与GPT-4.1相匹配或超越，且训练计算需求显著低于同类模型。我们还提出了一种剪枝和蒸馏技术，未来将应用于HyperCLOVA X THINK，旨在打造一个开源且适合商业应用的基础模型。

## 🔬 方法详解

**问题定义**：本论文旨在解决现有大型语言模型在推理能力和双语一致性方面的不足，尤其是在韩文和英文的应用场景中。现有模型在处理复杂推理任务时表现不佳，且在特定语言的翻译质量上存在差距。

**核心思路**：HyperCLOVA X THINK的核心思路是通过计算-内存平衡的Peri-LN Transformer架构，结合三阶段课程预训练和强化学习微调，提升模型的推理能力和上下文处理能力。这样的设计使得模型能够在更大上下文窗口内进行推理，适应复杂的语言任务。

**技术框架**：该模型的整体架构包括三个主要阶段：首先是预训练阶段，使用6万亿标记进行大规模训练；其次是扩展上下文窗口至128K标记；最后是通过强化学习进行监督微调，以优化模型在推理和回答模式下的表现。

**关键创新**：最重要的技术创新点在于其计算-内存平衡的Peri-LN Transformer架构和三阶段课程预训练方法，这使得模型在处理长文本时能够保持高效性和准确性，显著优于传统模型。

**关键设计**：模型的关键设计包括上下文窗口的扩展、损失函数的优化以及在微调阶段引入可验证奖励机制，以确保模型在推理和回答时的准确性和一致性。

## 📊 实验亮点

HyperCLOVA X THINK在多个韩国基准测试中表现优异，尤其是在KMMLU、CSAT和KoBALT-700等测试中，其性能超过同类模型。此外，视觉增强变体在KCSAT STEM基准测试中与GPT-4.1相当，且训练计算需求显著低于同类模型，展示了其高效性和实用性。

## 🎯 应用场景

HyperCLOVA X THINK的潜在应用场景包括教育、翻译、客户服务等领域，能够为用户提供高质量的双语支持和复杂推理能力。其创新的训练方法和架构设计将推动韩语及其他语言的人工智能应用发展，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> We introduce HyperCLOVA X THINK, the first reasoning-focused large language model in the HyperCLOVA X family, pre-trained on roughly $6$ trillion high-quality Korean, and English tokens, augmented with targeted synthetic Korean data. It was implemented as a compute-memory-balanced Peri-LN Transformer scaled with $μ$P, pre-trained through a three-stage curriculum that expands the context window to $128$K tokens, and post-trained via supervised fine-tuning with Reinforcement Learning from Verifiable Rewards supports both detailed rationale and concise-answer modes. It delivers competitive performance against similarly sized models on Korea-focused benchmarks such as KMMLU, CSAT, KoBALT-700, HAERAE-1.0, and KoBigBench, while preserving robust bilingual consistency and translation quality. In addition, a vision-augmented variant matches or exceeds GPT-4.1 on the KCSAT STEM benchmark, all of which are achieved with substantially lower training compute than existing models of similar sizes. We also present a pruning and distillation technique that will soon be applied to HyperCLOVA X THINK for an open-source and business-friendly foundation model. Altogether, these capabilities position HyperCLOVA X THINK as a robust foundation for Korean AI innovation and a valuable resource for the global research community.

