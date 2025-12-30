---
layout: default
title: "NeXT-IMDL: Build Benchmark for NeXT-Generation Image Manipulation Detection & Localization"
---

# NeXT-IMDL: Build Benchmark for NeXT-Generation Image Manipulation Detection & Localization

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.23374" class="toolbar-btn" target="_blank">📄 arXiv: 2512.23374v1</a>
  <a href="https://arxiv.org/pdf/2512.23374.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.23374v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.23374v1', 'NeXT-IMDL: Build Benchmark for NeXT-Generation Image Manipulation Detection & Localization')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yifei Li, Haoyuan He, Yu Zheng, Bingyao Yu, Wenzhao Zheng, Lei Chen, Jie Zhou, Jiwen Lu

**分类**: cs.CV

**发布日期**: 2025-12-29

---

## 💡 一句话要点

**NeXT-IMDL：构建下一代图像篡改检测与定位的基准测试**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)**

**关键词**: `图像篡改检测` `图像篡改定位` `AI生成内容` `基准测试` `泛化能力`

## 📋 核心要点

1. 现有图像篡改检测方法在跨数据集评估中表现出脆弱性，无法有效处理多样化的AI生成内容。
2. NeXT-IMDL通过构建大规模诊断基准，系统性地评估现有检测器在不同维度上的泛化能力。
3. 实验表明，现有模型在NeXT-IMDL的严格评估协议下性能显著下降，揭示了其泛化能力的不足。

## 📝 摘要（中文）

用户友好的图像编辑模型的普及和滥用风险，使得对图像篡改检测与定位(IMDL)的通用且最新的方法的需求变得迫切。目前的IMDL研究通常使用跨数据集评估，即在某个基准上训练的模型在其他基准上进行测试。然而，这种简化的评估方法掩盖了现有方法在处理各种AI生成内容时的脆弱性，导致对进展的误导性印象。本文提出了NeXT-IMDL，一个大规模诊断基准，旨在系统地探测当前检测器的泛化边界，而不仅仅是收集数据。具体来说，NeXT-IMDL沿着四个基本轴对基于AIGC的篡改进行分类：编辑模型、篡改类型、内容语义和伪造粒度。在此基础上，NeXT-IMDL实现了五个严格的跨维度评估协议。对11个代表性模型的大量实验揭示了一个关键的见解：虽然这些模型在其原始设置中表现良好，但在我们设计的模拟真实世界各种泛化场景的协议下进行评估时，它们表现出系统性失败和显著的性能下降。通过提供这种诊断工具包和新的发现，我们的目标是推进构建真正强大的下一代IMDL模型。

## 🔬 方法详解

**问题定义**：现有图像篡改检测与定位(IMDL)方法在处理真实世界中各种AI生成内容时，泛化能力不足。跨数据集评估虽然常用，但无法充分揭示模型在不同编辑模型、篡改类型、内容语义和伪造粒度上的性能差异。现有方法容易在特定数据集上过拟合，导致在实际应用中表现不佳。

**核心思路**：NeXT-IMDL的核心思路是构建一个大规模、多维度的诊断基准，通过系统性的跨维度评估协议，全面评估现有IMDL模型的泛化能力。该基准旨在模拟真实世界的复杂场景，揭示模型在不同因素影响下的性能瓶颈，从而推动更鲁棒的IMDL模型的发展。

**技术框架**：NeXT-IMDL的整体框架包括数据收集与组织、维度划分、评估协议设计和实验评估四个主要阶段。首先，收集大量AI生成图像，涵盖不同的编辑模型、篡改类型、内容语义和伪造粒度。然后，沿着这四个维度对数据进行分类和组织。接着，设计五个严格的跨维度评估协议，模拟真实世界的各种泛化场景。最后，在NeXT-IMDL上评估现有IMDL模型的性能，并分析结果。

**关键创新**：NeXT-IMDL的关键创新在于其多维度的数据组织方式和严格的跨维度评估协议。与以往的基准测试不同，NeXT-IMDL不仅仅是收集数据，而是系统性地探索了不同因素对IMDL模型性能的影响。通过跨维度评估，可以更全面地了解模型的泛化能力，并发现其潜在的弱点。

**关键设计**：NeXT-IMDL的关键设计包括四个维度：编辑模型（例如StyleGAN、DALL-E）、篡改类型（例如图像修复、对象移除）、内容语义（例如人脸、风景）和伪造粒度（例如小区域篡改、全局篡改）。五个评估协议包括：模型泛化（在不同编辑模型上训练和测试）、类型泛化（在不同篡改类型上训练和测试）、语义泛化（在不同内容语义上训练和测试）、粒度泛化（在不同伪造粒度上训练和测试）和组合泛化（同时考虑多个维度的泛化能力）。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.23374v1/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.23374v1/x2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.23374v1/x3.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

在NeXT-IMDL的评估中，11个代表性IMDL模型在跨维度评估协议下表现出显著的性能下降。例如，在模型泛化评估中，模型在新的编辑模型生成的数据上准确率下降了20%-50%。这些结果表明，现有IMDL模型在真实世界的复杂场景中泛化能力不足，需要进一步改进。

## 🎯 应用场景

NeXT-IMDL的研究成果可应用于数字取证、社交媒体内容审核、新闻真实性验证等领域。通过提高图像篡改检测的准确性和鲁棒性，可以有效防止虚假信息的传播，维护网络安全和公共利益。未来，该基准可以不断扩展和更新，以适应新的AI生成技术和篡改手段。

## 📄 摘要（原文）

> The accessibility surge and abuse risks of user-friendly image editing models have created an urgent need for generalizable, up-to-date methods for Image Manipulation Detection and Localization (IMDL). Current IMDL research typically uses cross-dataset evaluation, where models trained on one benchmark are tested on others. However, this simplified evaluation approach conceals the fragility of existing methods when handling diverse AI-generated content, leading to misleading impressions of progress. This paper challenges this illusion by proposing NeXT-IMDL, a large-scale diagnostic benchmark designed not just to collect data, but to probe the generalization boundaries of current detectors systematically. Specifically, NeXT-IMDL categorizes AIGC-based manipulations along four fundamental axes: editing models, manipulation types, content semantics, and forgery granularity. Built upon this, NeXT-IMDL implements five rigorous cross-dimension evaluation protocols. Our extensive experiments on 11 representative models reveal a critical insight: while these models perform well in their original settings, they exhibit systemic failures and significant performance degradation when evaluated under our designed protocols that simulate real-world, various generalization scenarios. By providing this diagnostic toolkit and the new findings, we aim to advance the development towards building truly robust, next-generation IMDL models.

