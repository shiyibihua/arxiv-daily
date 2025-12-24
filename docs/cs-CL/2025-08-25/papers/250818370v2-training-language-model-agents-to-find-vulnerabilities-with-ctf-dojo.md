---
layout: default
title: Training Language Model Agents to Find Vulnerabilities with CTF-Dojo
---

# Training Language Model Agents to Find Vulnerabilities with CTF-Dojo

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.18370" class="toolbar-btn" target="_blank">📄 arXiv: 2508.18370v2</a>
  <a href="https://arxiv.org/pdf/2508.18370.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.18370v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.18370v2', 'Training Language Model Agents to Find Vulnerabilities with CTF-Dojo')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Terry Yue Zhuo, Dingmin Wang, Hantian Ding, Varun Kumar, Zijian Wang

**分类**: cs.SE, cs.CL, cs.CR, cs.LG

**发布日期**: 2025-08-25 (更新: 2025-09-23)

---

## 💡 一句话要点

**提出CTF-Dojo以解决可扩展执行环境不足问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `可执行环境` `自动化管道` `网络安全` `机器学习代理`

## 📋 核心要点

1. 现有方法缺乏可扩展和通用的执行环境，限制了高性能机器学习代理的训练。
2. CTF-Dojo提供了一个大规模的可执行运行时环境，结合CTF挑战和自动化环境构建工具CTF-Forge。
3. 在CTF-Dojo上训练的LLM代理在多个基准测试中表现优异，取得了显著的性能提升。

## 📝 摘要（中文）

大型语言模型（LLMs）在可执行运行环境中训练时表现出色，尤其在软件工程任务中通过验证反馈循环取得了显著成果。然而，缺乏可扩展和通用的执行基础环境限制了更强大机器学习代理的训练进展。为此，我们推出了CTF-Dojo，这是第一个针对LLMs训练的可验证反馈的大规模可执行运行时，包含658个功能齐全的CTF风格挑战，且通过Docker容器化确保可重现性。我们还开发了CTF-Forge，一个自动化管道，能够在几分钟内将公开可用的工件转化为可用的执行环境，消除传统上需要的数周专家配置。通过在CTF-Dojo上训练基于LLM的代理，我们在三个竞争基准上实现了高达11.6%的绝对提升，建立了新的开放权重最先进模型。

## 🔬 方法详解

**问题定义**：本论文旨在解决现有机器学习代理训练中缺乏可扩展和通用的执行环境的问题。现有方法通常依赖于昂贵的专有系统，导致训练效率低下和可重复性差。

**核心思路**：论文提出CTF-Dojo作为一个大规模的可执行运行时环境，结合CTF风格的挑战和自动化的环境构建工具CTF-Forge，以实现快速、可重复的训练过程。

**技术框架**：CTF-Dojo的整体架构包括658个CTF挑战，所有挑战均通过Docker容器化，确保可重现性。同时，CTF-Forge自动化管道能够将公开工件转化为可用环境，极大地减少了配置时间。

**关键创新**：CTF-Dojo的最大创新在于其提供了可验证反馈的执行环境，允许LLM在真实的执行上下文中进行训练，从而提升了模型的泛化能力和性能。

**关键设计**：在训练过程中，使用了486条高质量的执行验证轨迹，模型的参数设置和损失函数经过精心设计，以确保在多个基准测试中达到最佳性能。

## 📊 实验亮点

在CTF-Dojo上训练的32B模型在多个基准测试中表现优异，达到31.9%的Pass@1，较强基线提升了11.6%。该模型的性能与前沿模型如DeepSeek-V3-0324和Gemini-2.5-Flash相媲美，建立了新的开放权重最先进水平。

## 🎯 应用场景

该研究的潜在应用领域包括网络安全、软件工程和自动化测试等。通过提供一个可扩展的训练环境，CTF-Dojo能够帮助开发更强大的机器学习代理，推动相关领域的技术进步，降低开发成本。

## 📄 摘要（原文）

> Large language models (LLMs) have demonstrated exceptional capabilities when trained within executable runtime environments, notably excelling at software engineering tasks through verified feedback loops. Yet, scalable and generalizable execution-grounded environments remain scarce, limiting progress in training more capable ML agents. We introduce CTF-Dojo, the first large-scale executable runtime tailored for training LLMs with verifiable feedback, featuring 658 fully functional Capture-The-Flag (CTF)-style challenges containerized in Docker with guaranteed reproducibility. To enable rapid scaling without manual intervention, we develop CTF-Forge, an automated pipeline that transforms publicly available artifacts into ready-to-use execution environments in minutes, eliminating weeks of expert configuration traditionally required. We trained LLM-based agents on just 486 high-quality, execution-verified trajectories from CTF-Dojo, achieving up to 11.6% absolute gains over strong baselines across three competitive benchmarks: InterCode-CTF, NYU CTF Bench, and Cybench. Our best-performing 32B model reaches 31.9% Pass@1, establishing a new open-weight state-of-the-art that rivals frontier models like DeepSeek-V3-0324 and Gemini-2.5-Flash. By framing CTF-style tasks as a benchmark for executable-agent learning, CTF-Dojo demonstrates that execution-grounded training signals are not only effective but pivotal in advancing high-performance ML agents without dependence on costly proprietary systems.

