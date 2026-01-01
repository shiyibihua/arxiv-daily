---
layout: default
title: "Vulcan: Instance-Optimal Systems Heuristics Through LLM-Driven Search"
---

# Vulcan: Instance-Optimal Systems Heuristics Through LLM-Driven Search

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.25065" class="toolbar-btn" target="_blank">📄 arXiv: 2512.25065v1</a>
  <a href="https://arxiv.org/pdf/2512.25065.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.25065v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.25065v1', 'Vulcan: Instance-Optimal Systems Heuristics Through LLM-Driven Search')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Rohit Dwivedula, Divyanshu Saxena, Sujay Yadalam, Daehyeok Kim, Aditya Akella

**分类**: cs.OS, cs.AI, cs.DC

**发布日期**: 2025-12-31

**备注**: 27 pages, 11 figures, 7 tables

---

## 💡 一句话要点

**Vulcan：利用LLM驱动搜索，合成实例最优的系统启发式算法**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `启发式搜索` `资源管理` `系统优化` `缓存驱逐` `内存分层` `进化算法` `代码生成`

## 📋 核心要点

1. 现有资源管理依赖手工启发式算法，设计成本高且难以适应硬件和工作负载的快速变化。
2. Vulcan利用LLM生成代码，通过进化搜索合成针对特定实例优化的启发式策略，分离策略与机制。
3. 实验表明，Vulcan合成的缓存驱逐和内存分层策略，性能超越现有算法高达69%和7.9%。

## 📝 摘要（中文）

现代操作系统和分布式系统中的资源管理任务，如调度、缓存或主动队列管理，仍然主要依赖于手工设计的启发式算法。设计高性能的启发式算法既昂贵又耗时，并且由于硬件、工作负载和环境的不断变化，我们不得不持续进行这一过程。本文提出了一种新的替代方案：使用代码生成的大型语言模型（LLM）合成实例最优的启发式算法，专门针对部署它们的确切工作负载和硬件。为了使这种合成易于处理，Vulcan通过LLM友好的、任务无关的接口分离策略和机制。通过这些接口，用户可以指定所需策略的输入和目标，而Vulcan通过对LLM生成的代码进行进化搜索来寻找高性能的策略。该接口具有足够的表达能力来捕获广泛的系统策略，同时又受到足够的约束，即使是小型、廉价的LLM也能生成正确且可执行的代码。我们使用Vulcan合成了用于缓存驱逐和内存分层的高性能启发式算法，发现这些启发式算法在性能上优于所有人工设计的最先进算法，对于每个任务分别高达69%和7.9%。

## 🔬 方法详解

**问题定义**：论文旨在解决现代操作系统和分布式系统中资源管理任务（如缓存驱逐、内存分层等）对人工设计启发式算法的依赖问题。现有方法的痛点在于，设计高性能的启发式算法成本高昂、耗时，且难以适应不断变化的硬件、工作负载和环境，导致系统性能难以达到最优。

**核心思路**：论文的核心思路是利用大型语言模型（LLM）的代码生成能力，自动合成针对特定实例（即特定的硬件和工作负载）优化的启发式算法。通过将策略（policy）与机制（mechanism）分离，并提供LLM友好的接口，降低了LLM生成高质量代码的难度，使得即使是小型LLM也能胜任。

**技术框架**：Vulcan的技术框架主要包含以下几个模块：1) 用户通过任务无关的接口指定策略的输入和目标；2) Vulcan利用LLM生成候选代码，这些代码实现了不同的启发式策略；3) Vulcan使用进化搜索算法，在生成的代码空间中搜索高性能的策略；4) 最终，Vulcan输出针对特定实例优化的启发式算法。

**关键创新**：论文最重要的技术创新点在于，它将LLM的代码生成能力与进化搜索算法相结合，实现了自动合成实例最优的系统启发式算法。与传统的手工设计方法相比，Vulcan能够更快速、更高效地找到针对特定场景的最佳策略。此外，通过分离策略与机制，并提供LLM友好的接口，降低了LLM生成高质量代码的难度。

**关键设计**：Vulcan的关键设计包括：1) LLM prompt的设计，需要保证生成的代码既能表达丰富的策略空间，又能保证代码的正确性和可执行性；2) 进化搜索算法的选择和参数设置，需要平衡搜索效率和搜索质量；3) 任务无关接口的设计，需要保证接口的通用性和表达能力，能够支持各种不同的资源管理任务。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.25065v1/osdi26-sections/figures/heatmap-cloudphysics-nosize.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.25065v1/osdi26-sections/figures/system-overview.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.25065v1/osdi26-sections/figures/module-overview-v3.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

实验结果表明，Vulcan合成的缓存驱逐和内存分层策略，在性能上显著优于人工设计的state-of-the-art算法。具体而言，对于缓存驱逐任务，Vulcan的性能提升高达69%；对于内存分层任务，性能提升达到7.9%。这些结果表明，Vulcan具有强大的系统优化能力。

## 🎯 应用场景

Vulcan具有广泛的应用前景，可用于各种资源管理任务，如云计算资源调度、边缘计算缓存管理、数据库查询优化等。通过自动合成实例最优的启发式算法，Vulcan可以显著提升系统性能，降低运营成本，并加速新硬件和工作负载的部署。未来，Vulcan有望成为一种通用的系统优化工具，赋能各种智能系统。

## 📄 摘要（原文）

> Resource-management tasks in modern operating and distributed systems continue to rely primarily on hand-designed heuristics for tasks such as scheduling, caching, or active queue management. Designing performant heuristics is an expensive, time-consuming process that we are forced to continuously go through due to the constant flux of hardware, workloads and environments.
>   We propose a new alternative: synthesizing instance-optimal heuristics -- specialized for the exact workloads and hardware where they will be deployed -- using code-generating large language models (LLMs). To make this synthesis tractable, Vulcan separates policy and mechanism through LLM-friendly, task-agnostic interfaces. With these interfaces, users specify the inputs and objectives of their desired policy, while Vulcan searches for performant policies via evolutionary search over LLM-generated code. This interface is expressive enough to capture a wide range of system policies, yet sufficiently constrained to allow even small, inexpensive LLMs to generate correct and executable code.
>   We use Vulcan to synthesize performant heuristics for cache eviction and memory tiering, and find that these heuristics outperform all human-designed state-of-the-art algorithms by upto 69% and 7.9% in performance for each of these tasks respectively.

