---
layout: default
title: "iSHIFT: Lightweight Slow-Fast GUI Agent with Adaptive Perception"
---

# iSHIFT: Lightweight Slow-Fast GUI Agent with Adaptive Perception

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.22009" class="toolbar-btn" target="_blank">📄 arXiv: 2512.22009v1</a>
  <a href="https://arxiv.org/pdf/2512.22009.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.22009v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.22009v1', 'iSHIFT: Lightweight Slow-Fast GUI Agent with Adaptive Perception')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Sarthak Mehrotra, Sairam V C Rebbapragada, Mani Hemanth Reddy Bonthu, Vineeth N Balasubramanian

**分类**: cs.CV

**发布日期**: 2025-12-26

---

## 💡 一句话要点

**iSHIFT：轻量级自适应感知慢-快GUI代理，提升交互效率与精度**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `GUI代理` `多模态学习` `大型语言模型` `视觉定位` `慢-快推理`

## 📋 核心要点

1. 现有GUI代理在处理需要精确视觉定位的任务时，准确性不足，且模型体积较大，推理深度无法自适应调整。
2. iSHIFT通过隐式慢-快混合推理，结合潜在思维和感知控制模块，使模型能根据任务需求切换推理模式。
3. 实验结果表明，iSHIFT在保持轻量级（2.5B）的同时，在多个基准数据集上达到了与最先进模型相当的性能。

## 📝 摘要（中文）

多模态大型语言模型(MLLM)在解释和交互复杂的、像素丰富的图形用户界面(GUI)环境方面显示出强大的潜力。然而，构建既能高效处理高层任务，又能精确进行细粒度交互的代理仍然具有挑战性。GUI代理必须高效地执行常规操作，同时处理需要精确视觉定位的任务，但现有方法在准确性依赖于识别特定界面元素时表现不佳。这些MLLM通常模型较大，并且无法根据手头的任务调整其推理深度。本文提出了iSHIFT：具有灵活令牌的隐式慢-快混合推理，这是一种轻量级代理，它集成了潜在思维（隐式思维链）和感知控制模块。iSHIFT使MLLM能够在慢速模式（利用详细的视觉定位以实现高精度）和快速模式（使用全局线索以提高效率）之间切换。特殊的感知令牌引导注意力到相关的屏幕区域，允许模型决定如何推理以及在哪里集中注意力。尽管iSHIFT只有2.5B大小，但它在多个基准数据集上匹配了最先进的性能。

## 🔬 方法详解

**问题定义**：现有GUI代理在处理需要精确定位的任务时，例如点击某个特定的按钮或链接，准确率不高。此外，现有模型通常体积庞大，计算成本高昂，并且无法根据任务的复杂程度动态调整推理深度，导致效率低下。

**核心思路**：iSHIFT的核心思路是引入一种慢-快混合推理机制，允许模型根据任务的需要，在快速的全局推理和慢速的精确定位之间切换。通过感知控制模块和特殊的感知令牌，引导模型关注屏幕上相关的区域，从而提高定位的准确性。

**技术框架**：iSHIFT的整体架构包含一个多模态大型语言模型（MLLM）作为基础，以及一个感知控制模块。该模块负责生成感知令牌，这些令牌用于引导MLLM的注意力。模型首先进行快速的全局推理，确定任务的类型和需要关注的区域。然后，如果需要精确定位，模型会切换到慢速模式，利用感知令牌引导注意力到相关的屏幕区域，进行更详细的分析。

**关键创新**：iSHIFT的关键创新在于其隐式慢-快混合推理机制和感知令牌的使用。传统的慢-快方法通常需要显式地切换不同的模型或计算路径，而iSHIFT通过感知令牌隐式地控制推理过程。感知令牌允许模型动态地调整其注意力，从而提高定位的准确性和效率。

**关键设计**：iSHIFT使用了2.5B参数的轻量级MLLM。感知令牌的设计允许模型学习哪些区域对于完成特定任务最重要。损失函数可能包含定位损失，用于鼓励模型将注意力集中在正确的区域。具体的网络结构细节和参数设置在论文中应该有更详细的描述（未知）。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.22009v1/images/iSHIFT_main_diagram_v4.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.22009v1/images/qual_result_3.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.22009v1/images/eff_metric_5.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

iSHIFT在多个GUI基准数据集上取得了与最先进模型相当的性能，同时保持了轻量级的模型尺寸（2.5B参数）。这表明iSHIFT在效率和准确性之间取得了良好的平衡。具体的性能数据和对比基线需要在论文中查找（未知）。

## 🎯 应用场景

iSHIFT具有广泛的应用前景，例如自动化测试、智能助手、无障碍辅助等。它可以用于自动执行GUI操作，例如填写表单、点击按钮等。此外，iSHIFT还可以帮助视力障碍人士更方便地使用计算机和移动设备。未来，iSHIFT可以进一步扩展到其他类型的多模态交互任务中。

## 📄 摘要（原文）

> Multimodal Large Language Models (MLLMs) show strong potential for interpreting and interacting with complex, pixel-rich Graphical User Interface (GUI) environments. However, building agents that are both efficient for high-level tasks and precise for fine-grained interactions remains challenging. GUI agents must perform routine actions efficiently while also handling tasks that demand exact visual grounding, yet existing approaches struggle when accuracy depends on identifying specific interface elements. These MLLMs also remain large and cannot adapt their reasoning depth to the task at hand. In this work, we introduce iSHIFT: Implicit Slow-fast Hybrid Inference with Flexible Tokens, a lightweight agent that integrates latent thinking (implicit chain-of-thought) with a perception control module. iSHIFT enables an MLLM to switch between a slow mode, which leverages detailed visual grounding for high precision and a fast mode that uses global cues for efficiency. Special perception tokens guide attention to relevant screen regions, allowing the model to decide both how to reason and where to focus. Despite its compact 2.5B size, iSHIFT matches state-of-the-art performance on multiple benchmark datasets.

