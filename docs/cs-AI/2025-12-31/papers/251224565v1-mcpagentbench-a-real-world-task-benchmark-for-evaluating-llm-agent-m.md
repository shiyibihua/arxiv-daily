---
layout: default
title: "MCPAgentBench: A Real-world Task Benchmark for Evaluating LLM Agent MCP Tool Use"
---

# MCPAgentBench: A Real-world Task Benchmark for Evaluating LLM Agent MCP Tool Use

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.24565" class="toolbar-btn" target="_blank">📄 arXiv: 2512.24565v1</a>
  <a href="https://arxiv.org/pdf/2512.24565.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.24565v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.24565v1', 'MCPAgentBench: A Real-world Task Benchmark for Evaluating LLM Agent MCP Tool Use')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Wenrui Liu, Zixiang Liu, Elsie Dai, Wenhan Yu, Lei Yu, Tong Yang

**分类**: cs.AI

**发布日期**: 2025-12-31

---

## 💡 一句话要点

**MCPAgentBench：构建真实世界MCP工具使用评估基准，提升LLM Agent工具调用能力**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `LLM Agent` `模型上下文协议` `MCP` `工具使用` `评估基准` `真实世界任务`

## 📋 核心要点

1. 现有MCP评估方法依赖外部服务，缺乏对任务难度的有效区分，限制了对Agent工具使用能力的全面评估。
2. MCPAgentBench通过构建真实任务和模拟MCP工具的数据集，并在动态沙箱环境中评估Agent的工具选择和辨别能力，解决上述问题。
3. 实验结果表明，不同LLM在处理复杂多步骤工具调用时表现出显著差异，验证了MCPAgentBench的有效性和区分度。

## 📝 摘要（中文）

大型语言模型（LLMs）越来越多地被用作自主Agent，并且通过模型上下文协议（MCP）利用外部工具被认为是未来的趋势。现有的MCP评估集存在依赖外部MCP服务和缺乏难度感知等问题。为了解决这些限制，我们提出了MCPAgentBench，这是一个基于真实世界MCP定义的基准，旨在评估Agent的工具使用能力。我们构建了一个包含真实任务和模拟MCP工具的数据集。评估采用动态沙箱环境，为Agent提供包含干扰项的候选工具列表，从而测试它们的工具选择和辨别能力。此外，我们引入了全面的指标来衡量任务完成率和执行效率。对各种最新的主流大型语言模型进行的实验表明，在处理复杂的、多步骤的工具调用时，性能存在显著差异。所有代码均已在Github上开源。

## 🔬 方法详解

**问题定义**：现有MCP评估基准依赖外部MCP服务，这限制了其可扩展性和可控性。此外，现有基准缺乏对任务难度的有效建模，难以区分不同Agent在复杂任务上的工具使用能力。因此，需要一个更贴近真实场景、难度可控、且不依赖外部服务的评估基准来全面评估LLM Agent的MCP工具使用能力。

**核心思路**：MCPAgentBench的核心思路是构建一个基于真实世界MCP定义的基准，包含真实任务和模拟MCP工具。通过动态沙箱环境，Agent需要从包含干扰项的候选工具列表中选择合适的工具来完成任务。这种设计模拟了真实世界中Agent需要面对的复杂环境和不确定性，从而更有效地评估Agent的工具使用能力。

**技术框架**：MCPAgentBench的整体框架包括以下几个主要模块：1) 任务定义模块：定义一系列真实世界的任务，例如预定机票、查询天气等。2) MCP工具模拟模块：模拟与任务相关的MCP工具，例如机票预订API、天气查询API等。3) 动态沙箱环境：创建一个动态的沙箱环境，为Agent提供任务描述和候选工具列表。4) 评估指标模块：定义一系列评估指标，例如任务完成率、执行效率等。Agent在沙箱环境中接收任务，并根据任务描述选择合适的工具进行调用，最终完成任务。

**关键创新**：MCPAgentBench的关键创新在于其真实性和动态性。它基于真实世界的MCP定义构建数据集，并采用动态沙箱环境进行评估。这种设计使得评估更加贴近真实场景，能够更有效地评估Agent的工具选择和辨别能力。此外，MCPAgentBench还引入了全面的评估指标，可以更全面地衡量Agent的工具使用性能。

**关键设计**：在动态沙箱环境中，候选工具列表中包含干扰项，Agent需要从这些干扰项中选择正确的工具。任务的难度可以通过增加干扰项的数量和复杂性来控制。评估指标包括任务完成率（衡量Agent是否能够成功完成任务）和执行效率（衡量Agent完成任务所需的步骤数）。此外，还考虑了工具选择的准确率，以评估Agent的工具辨别能力。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.24565v1/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.24565v1/x2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.24565v1/figures/tefs_tfs_comparison.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

实验结果表明，不同LLM在MCPAgentBench上的表现存在显著差异，尤其是在处理复杂的多步骤工具调用任务时。例如，某些LLM在任务完成率方面表现出色，但执行效率较低；而另一些LLM则在执行效率方面表现更好，但任务完成率较低。这些结果表明，MCPAgentBench能够有效地评估和区分不同LLM的工具使用能力。

## 🎯 应用场景

MCPAgentBench可用于评估和提升LLM Agent在各种实际应用场景中的工具使用能力，例如智能助手、自动化客服、智能家居控制等。通过该基准，可以更好地了解不同LLM在处理复杂任务时的优缺点，从而选择合适的LLM并进行针对性的优化，最终提升Agent的智能化水平和服务质量。

## 📄 摘要（原文）

> Large Language Models (LLMs) are increasingly serving as autonomous agents, and their utilization of external tools via the Model Context Protocol (MCP) is considered a future trend. Current MCP evaluation sets suffer from issues such as reliance on external MCP services and a lack of difficulty awareness. To address these limitations, we propose MCPAgentBench, a benchmark based on real-world MCP definitions designed to evaluate the tool-use capabilities of agents. We construct a dataset containing authentic tasks and simulated MCP tools. The evaluation employs a dynamic sandbox environment that presents agents with candidate tool lists containing distractors, thereby testing their tool selection and discrimination abilities. Furthermore, we introduce comprehensive metrics to measure both task completion rates and execution efficiency. Experiments conducted on various latest mainstream Large Language Models reveal significant performance differences in handling complex, multi-step tool invocations. All code is open-source at Github.

