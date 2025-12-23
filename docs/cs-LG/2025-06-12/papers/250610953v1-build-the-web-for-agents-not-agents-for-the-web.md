---
layout: default
title: Build the web for agents, not agents for the web
---

# Build the web for agents, not agents for the web

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.10953" class="toolbar-btn" target="_blank">📄 arXiv: 2506.10953v1</a>
  <a href="https://arxiv.org/pdf/2506.10953.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.10953v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.10953v1', 'Build the web for agents, not agents for the web')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Xing Han Lù, Gaurav Kamath, Marius Mosbach, Siva Reddy

**分类**: cs.LG, cs.CL

**发布日期**: 2025-06-12

---

## 💡 一句话要点

**提出代理网络接口以解决现有网页代理适应性不足问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `网页代理` `大型语言模型` `多模态模型` `代理网络接口` `自动化交互` `人工智能`

## 📋 核心要点

1. 当前网页代理方法面临人类设计界面与LLM能力之间的根本不匹配，导致复杂网页交互的自动化困难。
2. 论文提出代理网络接口（AWI），旨在为代理提供专门设计的界面，优化其导航和任务完成能力。
3. 通过建立六项设计原则，论文强调安全性、效率和标准化，为网页代理的高效、可靠和透明设计奠定基础。

## 📝 摘要（中文）

近年来，大型语言模型（LLMs）和多模态模型的进展激发了对网页代理的广泛关注，这些代理是能够在网页环境中自主导航和完成任务的人工智能系统。尽管在自动化复杂网页交互方面具有巨大潜力，但当前方法面临着人类设计的界面与LLM能力之间的根本不匹配所带来的重大挑战。本文倡导在网页代理研究中进行范式转变：我们应开发一种专门优化代理能力的新交互范式，而不是强迫网页代理适应人类设计的界面。为此，我们提出了代理网络接口（AWI）的概念，旨在为代理导航网站提供专门设计的界面，并建立了六项设计原则，以确保安全性、效率和标准化，考虑到所有主要利益相关者的利益。

## 🔬 方法详解

**问题定义**：当前网页代理方法在处理复杂网页输入时存在显著不足，尤其是在解析庞大的DOM树、依赖于截图和额外信息，或通过API交互绕过用户界面等方面。

**核心思路**：本论文的核心思路是提出代理网络接口（AWI），旨在为代理提供一种专门优化的交互界面，使其能够更有效地与网页环境进行交互，而不是强迫代理适应现有的人类设计界面。

**技术框架**：AWI的设计包括六项指导原则，涵盖安全性、效率和标准化等方面。这些原则为AWI的具体实现提供了框架，确保其能够满足所有主要利益相关者的需求。

**关键创新**：最重要的技术创新点在于AWI的概念本身，它重新定义了网页代理与网页交互的方式，与现有方法相比，AWI更注重代理的能力和需求，而不是人类用户的界面设计。

**关键设计**：在AWI的设计中，关键参数包括安全性标准、效率优化策略和标准化接口设计等，这些设计细节确保了AWI在实际应用中的有效性和可靠性。

## 📊 实验亮点

论文通过提出代理网络接口（AWI）显著提升了网页代理的交互效率和可靠性。虽然具体的性能数据尚未披露，但AWI的设计原则为未来的实验和应用奠定了坚实基础，预示着在网页代理领域的重大进展。

## 🎯 应用场景

该研究的潜在应用领域包括自动化网页数据采集、在线服务交互和智能助手等。通过优化网页代理的交互方式，AWI能够提高任务完成的效率和准确性，推动人工智能在复杂网页环境中的应用，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> Recent advancements in Large Language Models (LLMs) and multimodal counterparts have spurred significant interest in developing web agents -- AI systems capable of autonomously navigating and completing tasks within web environments. While holding tremendous promise for automating complex web interactions, current approaches face substantial challenges due to the fundamental mismatch between human-designed interfaces and LLM capabilities. Current methods struggle with the inherent complexity of web inputs, whether processing massive DOM trees, relying on screenshots augmented with additional information, or bypassing the user interface entirely through API interactions. This position paper advocates for a paradigm shift in web agent research: rather than forcing web agents to adapt to interfaces designed for humans, we should develop a new interaction paradigm specifically optimized for agentic capabilities. To this end, we introduce the concept of an Agentic Web Interface (AWI), an interface specifically designed for agents to navigate a website. We establish six guiding principles for AWI design, emphasizing safety, efficiency, and standardization, to account for the interests of all primary stakeholders. This reframing aims to overcome fundamental limitations of existing interfaces, paving the way for more efficient, reliable, and transparent web agent design, which will be a collaborative effort involving the broader ML community.

