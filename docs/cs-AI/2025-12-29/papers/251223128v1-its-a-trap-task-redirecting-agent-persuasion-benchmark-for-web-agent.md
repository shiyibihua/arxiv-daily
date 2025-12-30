---
layout: default
title: "It's a TRAP! Task-Redirecting Agent Persuasion Benchmark for Web Agents"
---

# It's a TRAP! Task-Redirecting Agent Persuasion Benchmark for Web Agents

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.23128" class="toolbar-btn" target="_blank">📄 arXiv: 2512.23128v1</a>
  <a href="https://arxiv.org/pdf/2512.23128.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.23128v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.23128v1', 'It\'s a TRAP! Task-Redirecting Agent Persuasion Benchmark for Web Agents')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Karolina Korgul, Yushi Yang, Arkadiusz Drohomirecki, Piotr Błaszczyk, Will Howard, Lukas Aichberger, Chris Russell, Philip H. S. Torr, Adam Mahdi, Adel Bibi

**分类**: cs.HC, cs.AI, cs.MA

**发布日期**: 2025-12-29

---

## 💡 一句话要点

**提出TRAP基准测试，评估Web Agent在提示注入攻击下的任务重定向脆弱性**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `Web Agent` `提示注入攻击` `基准测试` `任务重定向` `安全评估`

## 📋 核心要点

1. Web Agent依赖动态Web内容，易受恶意提示注入攻击，导致任务被重定向。
2. TRAP基准测试通过模拟真实Web环境，评估Agent在对抗性指令下的行为。
3. 实验表明，现有Agent对提示注入攻击的抵抗力较弱，存在显著的安全漏洞。

## 📝 摘要（中文）

本文介绍了一个名为任务重定向代理说服基准（TRAP）的评估方法，用于研究说服技术如何误导自主Web Agent执行非预期任务。这些Agent由大型语言模型驱动，常用于电子邮件管理或专业社交等任务。然而，它们对动态Web内容的依赖使其容易受到提示注入攻击，即隐藏在界面元素中的对抗性指令，诱使Agent偏离其原始任务。实验表明，六个前沿模型平均有25%的任务容易受到提示注入的影响（GPT-5为13%，DeepSeek-R1为43%）。界面或上下文的微小变化通常会使成功率翻倍，揭示了Web Agent中系统性的、心理驱动的漏洞。此外，本文还提供了一个模块化的社会工程注入框架，通过对高保真网站克隆进行受控实验，从而进一步扩展基准测试。

## 🔬 方法详解

**问题定义**：论文旨在解决Web Agent容易受到提示注入攻击，导致其执行非预期任务的问题。现有方法缺乏对这种攻击的系统性评估和防御机制，使得Agent在实际应用中面临安全风险。现有的Web Agent在处理网页内容时，容易受到恶意构造的提示的影响，从而偏离其预定的目标。

**核心思路**：论文的核心思路是构建一个基准测试环境，模拟真实的Web环境，并设计各种社会工程学攻击手段，评估Agent在这些攻击下的表现。通过分析Agent的脆弱性，为开发更安全的Web Agent提供指导。

**技术框架**：TRAP基准测试包含以下主要模块：1) 高保真网站克隆：创建与真实网站相似的克隆环境，模拟Agent的实际操作场景。2) 任务定义：定义Agent需要完成的各种任务，例如发送邮件、添加联系人等。3) 攻击策略：设计各种提示注入攻击策略，例如在网页文本中嵌入恶意指令。4) 评估指标：评估Agent在攻击下的表现，例如任务完成率、任务重定向率等。5) 模块化社会工程注入框架：允许用户自定义攻击策略，扩展基准测试。

**关键创新**：论文的关键创新在于提出了一个专门针对Web Agent的提示注入攻击评估基准。该基准不仅模拟了真实的Web环境，还设计了多种社会工程学攻击手段，能够全面评估Agent的安全性。此外，该基准还提供了一个模块化的攻击框架，方便用户自定义攻击策略。

**关键设计**：TRAP基准测试的关键设计包括：1) 高保真网站克隆，保证了评估的真实性。2) 多样化的任务定义，覆盖了Agent的常见应用场景。3) 精心设计的攻击策略，模拟了真实的攻击手段。4) 模块化的攻击框架，方便用户扩展和定制。具体参数设置和网络结构取决于被评估的Agent模型。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.23128v1/Figures/environments.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.23128v1/Figures/pipeline.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.23128v1/iclr/Figures/injection_creation_iteration2.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

实验结果表明，现有Web Agent对提示注入攻击的抵抗力较弱，平均有25%的任务容易受到攻击。不同模型之间的表现差异显著，GPT-5的攻击成功率为13%，而DeepSeek-R1则高达43%。此外，实验还发现，界面或上下文的微小变化会显著影响攻击成功率，揭示了Agent中存在的系统性漏洞。

## 🎯 应用场景

该研究成果可应用于提升Web Agent的安全性，防止其受到恶意攻击。通过TRAP基准测试，可以评估和改进Agent的防御能力，降低任务被重定向的风险。这对于保护用户隐私、防止信息泄露以及确保Agent的可靠运行具有重要意义。未来，该研究可以促进开发更安全的Web Agent，使其能够更好地服务于用户。

## 📄 摘要（原文）

> Web-based agents powered by large language models are increasingly used for tasks such as email management or professional networking. Their reliance on dynamic web content, however, makes them vulnerable to prompt injection attacks: adversarial instructions hidden in interface elements that persuade the agent to divert from its original task. We introduce the Task-Redirecting Agent Persuasion Benchmark (TRAP), an evaluation for studying how persuasion techniques misguide autonomous web agents on realistic tasks. Across six frontier models, agents are susceptible to prompt injection in 25\% of tasks on average (13\% for GPT-5 to 43\% for DeepSeek-R1), with small interface or contextual changes often doubling success rates and revealing systemic, psychologically driven vulnerabilities in web-based agents. We also provide a modular social-engineering injection framework with controlled experiments on high-fidelity website clones, allowing for further benchmark expansion.

