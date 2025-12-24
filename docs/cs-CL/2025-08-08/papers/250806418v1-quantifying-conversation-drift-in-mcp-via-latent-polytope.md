---
layout: default
title: Quantifying Conversation Drift in MCP via Latent Polytope
---

# Quantifying Conversation Drift in MCP via Latent Polytope

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.06418" class="toolbar-btn" target="_blank">📄 arXiv: 2508.06418v1</a>
  <a href="https://arxiv.org/pdf/2508.06418.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.06418v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.06418v1', 'Quantifying Conversation Drift in MCP via Latent Polytope')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Haoran Shi, Hongwei Yao, Shuo Shao, Shaopeng Jiao, Ziqi Peng, Zhan Qin, Cong Wang

**分类**: cs.CL

**发布日期**: 2025-08-08

---

## 💡 一句话要点

**提出SecMCP以解决MCP中的对话漂移问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `模型上下文协议` `对话漂移` `潜在多面体` `安全框架` `大型语言模型` `异常检测` `信息安全`

## 📋 核心要点

1. 现有方法在应对MCP中的安全威胁时存在不足，无法有效量化对话劫持和动态变化。
2. 论文提出SecMCP框架，通过潜在多面体空间建模LLM激活向量，检测对话漂移。
3. 实验结果显示SecMCP在三种LLM上表现优异，AUROC得分超过0.915，且保持良好的系统可用性。

## 📝 摘要（中文）

模型上下文协议（MCP）通过整合外部工具增强了大型语言模型（LLMs），实现实时数据的动态聚合以改善任务执行。然而，其非隔离的执行环境引入了严重的安全和隐私风险，尤其是对抗性内容可能导致工具中毒或间接提示注入，从而引发对话劫持、错误信息传播或数据外泄。现有的防御措施如基于规则的过滤器或LLM驱动的检测方法，由于依赖静态特征、计算效率低下以及无法量化对话劫持，显得不足。为了解决这些问题，我们提出了SecMCP，一个安全框架，能够检测和量化对话漂移，即由对抗性外部知识引起的潜在空间轨迹偏差。通过在潜在多面体空间中建模LLM激活向量，SecMCP能够识别对话动态中的异常变化，从而实现对劫持、误导和数据外泄的主动检测。我们在三种最先进的LLM（Llama3、Vicuna、Mistral）上对SecMCP进行了评估，结果显示其检测能力强大，AUROC得分超过0.915，同时保持系统可用性。

## 🔬 方法详解

**问题定义**：本论文旨在解决MCP中由于外部对抗性知识引起的对话漂移问题。现有方法依赖静态特征，无法有效应对动态变化和量化对话劫持的风险。

**核心思路**：SecMCP通过在潜在多面体空间中建模LLM的激活向量，识别对话动态中的异常变化，从而实现对劫持和误导信息的主动检测。这样的设计使得系统能够动态适应对抗性输入。

**技术框架**：SecMCP的整体架构包括数据输入模块、潜在多面体建模模块、异常检测模块和输出反馈模块。数据输入模块负责接收LLM的激活向量，潜在多面体建模模块则用于构建潜在空间，异常检测模块通过分析潜在空间的变化来识别对话漂移。

**关键创新**：最重要的技术创新在于提出了基于潜在多面体的方法来量化对话漂移，这与现有依赖静态特征的检测方法本质上不同，能够更好地应对动态变化。

**关键设计**：在设计中，SecMCP采用了特定的损失函数来优化潜在多面体的构建，并通过调整参数来提高检测的灵敏度和准确性。网络结构方面，结合了多层感知机和聚类算法，以增强对异常模式的识别能力。

## 📊 实验亮点

实验结果表明，SecMCP在三种最先进的LLM上实现了超过0.915的AUROC得分，显著优于现有的静态检测方法，展示了其在对话漂移检测中的强大能力和系统可用性。

## 🎯 应用场景

该研究的潜在应用领域包括智能客服、在线教育和社交媒体等场景，能够有效提升系统的安全性和用户信任度。通过实时监测对话动态，SecMCP可以帮助企业防范信息泄露和误导性内容的传播，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> The Model Context Protocol (MCP) enhances large language models (LLMs) by integrating external tools, enabling dynamic aggregation of real-time data to improve task execution. However, its non-isolated execution context introduces critical security and privacy risks. In particular, adversarially crafted content can induce tool poisoning or indirect prompt injection, leading to conversation hijacking, misinformation propagation, or data exfiltration. Existing defenses, such as rule-based filters or LLM-driven detection, remain inadequate due to their reliance on static signatures, computational inefficiency, and inability to quantify conversational hijacking. To address these limitations, we propose SecMCP, a secure framework that detects and quantifies conversation drift, deviations in latent space trajectories induced by adversarial external knowledge. By modeling LLM activation vectors within a latent polytope space, SecMCP identifies anomalous shifts in conversational dynamics, enabling proactive detection of hijacking, misleading, and data exfiltration. We evaluate SecMCP on three state-of-the-art LLMs (Llama3, Vicuna, Mistral) across benchmark datasets (MS MARCO, HotpotQA, FinQA), demonstrating robust detection with AUROC scores exceeding 0.915 while maintaining system usability. Our contributions include a systematic categorization of MCP security threats, a novel latent polytope-based methodology for quantifying conversation drift, and empirical validation of SecMCP's efficacy.

