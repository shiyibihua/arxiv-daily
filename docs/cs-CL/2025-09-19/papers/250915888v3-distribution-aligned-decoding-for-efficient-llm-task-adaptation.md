---
layout: default
title: Distribution-Aligned Decoding for Efficient LLM Task Adaptation
---

# Distribution-Aligned Decoding for Efficient LLM Task Adaptation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.15888" class="toolbar-btn" target="_blank">📄 arXiv: 2509.15888v3</a>
  <a href="https://arxiv.org/pdf/2509.15888.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.15888v3" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.15888v3', 'Distribution-Aligned Decoding for Efficient LLM Task Adaptation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Senkang Hu, Xudong Han, Jinqi Jiang, Yihang Tao, Zihan Fang, Yong Dai, Sam Tak Wu Kwong, Yuguang Fang

**分类**: cs.CL, cs.AI

**发布日期**: 2025-09-19 (更新: 2025-10-12)

**备注**: Accepted by NeurIPS'25

---

## 💡 一句话要点

**提出SVDecode，通过分布对齐解码高效适应LLM下游任务**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `参数高效微调` `分布对齐` `解码引导` `迁移学习` `任务适配` `Steering Vector`

## 📋 核心要点

1. 现有PEFT方法在LLM任务适配中仍面临成本高昂的挑战，需要更高效的方案。
2. SVDecode通过提取steering vector，在解码阶段直接对齐输出分布和任务分布。
3. 实验表明，SVDecode能显著提升多项选择题准确率和开放式问题真实性，且无需额外可训练参数。

## 📝 摘要（中文）

即使采用参数高效微调（PEFT），将数十亿参数的语言模型适配到下游任务仍然成本高昂。本文将任务适配重新定义为输出分布对齐：目标是在解码过程中直接将输出分布引导至任务分布，而不是通过权重更新间接实现。基于此，我们引入了Steering Vector Decoding (SVDecode)，这是一种轻量级、兼容PEFT且具有理论基础的方法。我们首先进行一个简短的预热微调，并从预热微调模型和预训练模型的输出分布之间的Kullback-Leibler (KL)散度梯度中提取任务相关的steering vector。然后，该steering vector用于指导解码过程，以将模型的输出分布引导至任务分布。我们从理论上证明了SVDecode与完全微调的梯度步长一阶等价，并推导出了steering vector强度的全局最优解。在三个任务和九个基准测试中，SVDecode与四种标准PEFT方法相结合，将多项选择题的准确率提高了高达5个百分点，并将开放式问题的真实性提高了2个百分点，在常识数据集上获得了类似的收益（1-2个百分点），而无需在PEFT适配器之外添加可训练参数。因此，SVDecode为大型语言模型提供了更强大的任务适配的轻量级、理论基础坚实的途径。

## 🔬 方法详解

**问题定义**：论文旨在解决大型语言模型（LLM）在下游任务上的高效适配问题。即使使用参数高效微调（PEFT）方法，微调数十亿参数的LLM仍然需要大量的计算资源和时间。现有方法的痛点在于，它们通常通过更新模型权重来间接调整输出分布，效率较低。

**核心思路**：论文的核心思路是将任务适配问题转化为输出分布对齐问题。通过直接在解码阶段引导模型的输出分布向目标任务的分布靠拢，避免了通过权重更新的间接调整。这种方法旨在更直接、更高效地实现任务适配。

**技术框架**：SVDecode方法包含以下主要阶段：1) **预热微调（Warm-start Fine-tune）**：使用少量数据对预训练模型进行快速微调，使其初步适应目标任务。2) **Steering Vector提取**：计算预热微调模型和预训练模型输出分布之间的KL散度梯度，并从中提取任务相关的steering vector。3) **解码引导**：在解码过程中，使用提取的steering vector引导模型的输出分布向目标任务分布靠拢。

**关键创新**：SVDecode的关键创新在于其直接对齐输出分布的思路，以及steering vector的提取和应用方式。与传统的微调方法相比，SVDecode避免了对模型权重的直接修改，从而降低了计算成本。此外，论文还从理论上证明了SVDecode与完全微调的一阶等价性，并推导出了steering vector强度的全局最优解。

**关键设计**：论文的关键设计包括：1) 使用KL散度梯度作为steering vector的来源，以捕捉预训练模型和微调模型之间的分布差异。2) 推导steering vector强度的全局最优解，以确保解码过程的有效性和稳定性。3) 将SVDecode与现有的PEFT方法相结合，以进一步提高任务适配的性能。

## 📊 实验亮点

实验结果表明，SVDecode与四种标准PEFT方法相结合，在三个任务和九个基准测试中，将多项选择题的准确率提高了高达5个百分点，并将开放式问题的真实性提高了2个百分点。在常识数据集上，SVDecode也获得了1-2个百分点的提升，且无需在PEFT适配器之外添加可训练参数。这些结果表明，SVDecode是一种高效且有效的LLM任务适配方法。

## 🎯 应用场景

SVDecode具有广泛的应用前景，可用于各种需要快速、高效地将大型语言模型适配到特定下游任务的场景，如问答系统、文本摘要、机器翻译等。该方法尤其适用于资源受限的环境，例如边缘计算设备或移动设备。此外，SVDecode还可以用于个性化语言模型，根据用户的特定需求调整模型的输出风格和内容。

## 📄 摘要（原文）

> Adapting billion-parameter language models to a downstream task is still costly, even with parameter-efficient fine-tuning (PEFT). We re-cast task adaptation as output-distribution alignment: the objective is to steer the output distribution toward the task distribution directly during decoding rather than indirectly through weight updates. Building on this view, we introduce Steering Vector Decoding (SVDecode), a lightweight, PEFT-compatible, and theoretically grounded method. We start with a short warm-start fine-tune and extract a task-aware steering vector from the Kullback-Leibler (KL) divergence gradient between the output distribution of the warm-started and pre-trained models. This steering vector is then used to guide the decoding process to steer the model's output distribution towards the task distribution. We theoretically prove that SVDecode is first-order equivalent to the gradient step of full fine-tuning and derive a globally optimal solution for the strength of the steering vector. Across three tasks and nine benchmarks, SVDecode paired with four standard PEFT methods improves multiple-choice accuracy by up to 5 percentage points and open-ended truthfulness by 2 percentage points, with similar gains (1-2 percentage points) on commonsense datasets without adding trainable parameters beyond the PEFT adapter. SVDecode thus offers a lightweight, theoretically grounded path to stronger task adaptation for large language models.

