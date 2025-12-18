---
layout: default
title: Boosting Embodied AI Agents through Perception-Generation Disaggregation and Asynchronous Pipeline Execution
---

# Boosting Embodied AI Agents through Perception-Generation Disaggregation and Asynchronous Pipeline Execution

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.09560" class="toolbar-btn" target="_blank">📄 arXiv: 2509.09560v1</a>
  <a href="https://arxiv.org/pdf/2509.09560.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.09560v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.09560v1', 'Boosting Embodied AI Agents through Perception-Generation Disaggregation and Asynchronous Pipeline Execution')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Shulai Zhang, Ao Xu, Quan Chen, Han Zhao, Weihao Cui, Ningxin Zheng, Haibin Lin, Xin Liu, Minyi Guo

**分类**: cs.AI, cs.LG

**发布日期**: 2025-09-11

---

## 💡 一句话要点

**Auras：通过解耦感知-生成和异步流水线执行提升具身智能体性能**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `具身智能` `异步流水线` `感知生成解耦` `高吞吐量` `共享上下文`

## 📋 核心要点

1. 现有具身智能体系统采用顺序计算模式，难以满足实时性要求，限制了其在动态环境中的应用。
2. Auras通过解耦感知和生成模块，并引入异步流水线并行执行，显著提升了系统的推理频率。
3. 实验表明，Auras在保证准确率的前提下，吞吐量平均提升2.54倍，有效克服了传统方法的瓶颈。

## 📝 摘要（中文）

具身智能系统在动态环境中运行，需要无缝集成感知和生成模块，以处理高频输入和输出需求。传统的顺序计算模式虽然能保证准确性，但在实现现实应用所需的“思考”频率方面面临重大限制。本文提出Auras，一种算法-系统协同设计的推理框架，旨在优化具身智能体的推理频率。Auras解耦了感知和生成过程，并为它们提供可控的流水线并行性，以实现高且稳定的吞吐量。针对并行性增加时出现的数据陈旧问题，Auras建立了一个感知和生成共享的公共上下文，从而保证了具身智能体的准确性。实验结果表明，Auras在达到原始准确率的102.7%的同时，平均提高了2.54倍的吞吐量，证明了其在克服顺序计算约束和提供高吞吐量方面的有效性。

## 🔬 方法详解

**问题定义**：具身智能体需要在动态环境中实时感知环境并做出决策，传统的感知和生成模块串行执行方式限制了系统的推理速度，无法满足高频输入输出的需求。现有方法难以在保证准确性的前提下，显著提升推理吞吐量。

**核心思路**：Auras的核心思路是将感知和生成模块解耦，允许它们并行执行。通过异步流水线的方式，感知模块持续处理输入数据，生成模块则基于感知结果进行决策。为了解决并行执行带来的数据陈旧问题，Auras引入了共享上下文机制，使得感知和生成模块可以共享最新的环境信息。

**技术框架**：Auras框架主要包含感知模块、生成模块和共享上下文三个部分。感知模块负责从传感器数据中提取环境信息，并将结果写入共享上下文。生成模块从共享上下文中读取环境信息，并根据当前状态生成控制指令。感知和生成模块通过异步流水线并行执行，互不阻塞。框架还包含一个同步机制，用于保证生成模块读取到的环境信息的一致性。

**关键创新**：Auras的关键创新在于解耦感知和生成模块，并采用异步流水线并行执行。这种设计打破了传统串行计算的瓶颈，显著提升了系统的推理吞吐量。同时，共享上下文机制有效地解决了并行执行带来的数据陈旧问题，保证了系统的准确性。

**关键设计**：共享上下文采用环形缓冲区实现，感知模块将最新的环境信息写入缓冲区，生成模块则从缓冲区中读取数据。同步机制采用读写锁实现，保证生成模块读取数据时的一致性。感知和生成模块的执行频率可以根据实际需求进行调整，以达到最佳的性能平衡。

## 📊 实验亮点

实验结果表明，Auras框架在保证102.7%原始准确率的前提下，平均提高了2.54倍的吞吐量。与传统的顺序计算方法相比，Auras在推理速度上取得了显著提升。这些结果验证了Auras在克服顺序计算约束和提供高吞吐量方面的有效性，为具身智能系统的性能优化提供了新的思路。

## 🎯 应用场景

Auras框架可广泛应用于机器人导航、自动驾驶、智能家居等需要实时感知和决策的具身智能系统中。通过提升推理频率，Auras能够使智能体更快地响应环境变化，从而提高其在复杂环境中的适应性和鲁棒性。未来，Auras有望推动具身智能技术在更多实际场景中的应用。

## 📄 摘要（原文）

> Embodied AI systems operate in dynamic environments, requiring seamless integration of perception and generation modules to process high-frequency input and output demands. Traditional sequential computation patterns, while effective in ensuring accuracy, face significant limitations in achieving the necessary "thinking" frequency for real-world applications. In this work, we present Auras, an algorithm-system co-designed inference framework to optimize the inference frequency of embodied AI agents. Auras disaggregates the perception and generation and provides controlled pipeline parallelism for them to achieve high and stable throughput. Faced with the data staleness problem that appears when the parallelism is increased, Auras establishes a public context for perception and generation to share, thereby promising the accuracy of embodied agents. Experimental results show that Auras improves throughput by 2.54x on average while achieving 102.7% of the original accuracy, demonstrating its efficacy in overcoming the constraints of sequential computation and providing high throughput.

