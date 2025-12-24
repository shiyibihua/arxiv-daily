---
layout: default
title: Optimized Renewable Energy Planning MDP for Socially-Equitable Electricity Coverage in the US
---

# Optimized Renewable Energy Planning MDP for Socially-Equitable Electricity Coverage in the US

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.00008" class="toolbar-btn" target="_blank">📄 arXiv: 2509.00008v1</a>
  <a href="https://arxiv.org/pdf/2509.00008.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.00008v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.00008v1', 'Optimized Renewable Energy Planning MDP for Socially-Equitable Electricity Coverage in the US')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Riya Kinnarkar, Mansur Arief

**分类**: eess.SY, cs.AI, cs.CE, econ.GN

**发布日期**: 2025-08-15

---

## 💡 一句话要点

**提出马尔可夫决策过程优化可再生能源规划以解决美国电力覆盖不平等问题**

🎯 **匹配领域**: **支柱四：生成式动作 (Generative Motion)**

**关键词**: `可再生能源` `社会公平` `马尔可夫决策过程` `电力分配` `低收入社区` `政策评估` `能源规划`

## 📋 核心要点

1. 现有电网基础设施在可再生能源整合方面存在障碍，导致低收入社区面临更长的停电时间，能源获取不平等问题突出。
2. 本研究提出了一种基于马尔可夫决策过程的框架，优化可再生能源的分配，关注社会公平，考虑预算、需求变动和脆弱性指标。
3. 实验结果显示，公平优化策略实现了32.9%的可再生能源渗透率，并将低收入人群的服务不足减少了55%，表现优于传统方法。

## 📝 摘要（中文）

传统电网基础设施在可再生能源整合方面存在显著障碍，并加剧了能源获取的不平等，低收入社区经历了更长的停电时间。本研究开发了一种马尔可夫决策过程（MDP）框架，以优化可再生能源分配，同时明确关注电力分配中的社会公平问题。该模型考虑了预算约束、能源需求变动和社会脆弱性指标，评估了美国八个主要城市的政策替代方案。数值实验将基于MDP的方法与随机分配、贪婪可再生扩展和专家启发式等基线政策进行了比较。结果表明，关注公平的优化可以实现32.9%的可再生能源渗透率，同时将服务不足的低收入人群减少55%，与传统方法相比，专家政策获得了最高奖励，而蒙特卡洛树搜索基线在预算利用上表现出竞争力，表明在不牺牲整体系统性能的情况下，实现清洁能源资源的公平分配是可行的。

## 🔬 方法详解

**问题定义**：本研究旨在解决传统电网在可再生能源整合中存在的障碍，特别是如何在电力分配中实现社会公平，避免低收入社区的能源获取不平等。

**核心思路**：论文提出的核心思路是利用马尔可夫决策过程（MDP）框架，优化可再生能源的分配，明确考虑社会公平因素，以实现更均衡的电力覆盖。

**技术框架**：该框架包括多个模块，首先是需求预测和社会脆弱性评估，然后是基于预算约束的优化决策过程，最后通过数值实验评估不同政策的效果。

**关键创新**：最重要的创新点在于将社会公平与可再生能源分配的优化结合起来，形成了一个新的评估标准，与传统方法相比，强调了公平性的重要性。

**关键设计**：模型中设置了预算约束、需求波动和社会脆弱性指标等关键参数，损失函数设计上考虑了公平性和效率的平衡，确保优化结果能够兼顾系统性能与社会影响。

## 📊 实验亮点

实验结果表明，基于MDP的优化方法实现了32.9%的可再生能源渗透率，并将低收入人群的服务不足减少了55%。与传统随机分配和贪婪扩展策略相比，专家政策获得了最高奖励，而蒙特卡洛树搜索基线在预算利用上表现出竞争力，显示出公平分配与系统性能之间的良好平衡。

## 🎯 应用场景

该研究的潜在应用领域包括城市电力规划、可再生能源政策制定及社会公平评估等。其实际价值在于为政策制定者提供了一种新的工具，以实现更公平的电力分配，促进低收入社区的可持续发展，未来可能对电力基础设施的改进和社会公平政策的实施产生深远影响。

## 📄 摘要（原文）

> Traditional power grid infrastructure presents significant barriers to renewable energy integration and perpetuates energy access inequities, with low-income communities experiencing disproportionately longer power outages. This study develops a Markov Decision Process (MDP) framework to optimize renewable energy allocation while explicitly addressing social equity concerns in electricity distribution. The model incorporates budget constraints, energy demand variability, and social vulnerability indicators across eight major U.S. cities to evaluate policy alternatives for equitable clean energy transitions. Numerical experiments compare the MDP-based approach against baseline policies including random allocation, greedy renewable expansion, and expert heuristics. Results demonstrate that equity-focused optimization can achieve 32.9% renewable energy penetration while reducing underserved low-income populations by 55% compared to conventional approaches. The expert policy achieved the highest reward, while the Monte Carlo Tree Search baseline provided competitive performance with significantly lower budget utilization, demonstrating that fair distribution of clean energy resources is achievable without sacrificing overall system performance and providing ways for integrating social equity considerations with climate goals and inclusive access to clean power infrastructure.

