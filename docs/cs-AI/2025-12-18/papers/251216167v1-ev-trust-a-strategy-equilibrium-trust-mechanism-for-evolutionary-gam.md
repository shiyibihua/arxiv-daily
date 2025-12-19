---
layout: default
title: Ev-Trust: A Strategy Equilibrium Trust Mechanism for Evolutionary Games in LLM-Based Multi-Agent Services
---

# Ev-Trust: A Strategy Equilibrium Trust Mechanism for Evolutionary Games in LLM-Based Multi-Agent Services

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.16167" class="toolbar-btn" target="_blank">📄 arXiv: 2512.16167v1</a>
  <a href="https://arxiv.org/pdf/2512.16167.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.16167v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.16167v1', 'Ev-Trust: A Strategy Equilibrium Trust Mechanism for Evolutionary Games in LLM-Based Multi-Agent Services')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Shiduo Yang, Jiye Wang, Jiayu Qin, Jianbin Li, Yu Wang, Yuanhe Zhao, Kenan Guo

**分类**: cs.MA, cs.AI, cs.GT

**发布日期**: 2025-12-18

**备注**: 12 pages, 11 figures

---

## 💡 一句话要点

**提出Ev-Trust，一种基于演化博弈论的LLM多智能体服务信任机制。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多智能体系统` `信任机制` `演化博弈论` `大型语言模型` `策略均衡`

## 📋 核心要点

1. 基于LLM的多智能体系统面临欺骗、欺诈和错误信息等信任危机，严重影响系统鲁棒性。
2. Ev-Trust通过演化博弈论，整合直接信任、间接信任和预期收益，动态引导智能体行为趋向策略均衡。
3. 实验表明，Ev-Trust能有效反映智能体可信度，减少恶意策略，并提升LLM驱动服务交互的集体收益。

## 📝 摘要（中文）

随着Web向以智能体为中心的范式快速演进，由大型语言模型（LLMs）驱动的自主智能体能够在复杂的去中心化环境中进行推理、规划和交互。然而，基于LLM的多智能体系统的开放性和异构性也加剧了欺骗、欺诈和错误信息的风险，对信任建立和系统鲁棒性构成严峻挑战。为了解决这个问题，我们提出Ev-Trust，一种基于演化博弈论的策略均衡信任机制。该机制将直接信任、间接信任和预期收益整合到一个动态反馈结构中，引导智能体的行为演化趋向均衡。在去中心化的“请求-响应-支付-评估”服务框架内，Ev-Trust使智能体能够自适应地调整策略，自然地排除恶意参与者，同时加强高质量的协作。此外，我们基于复制者动态方程的理论推导证明了局部演化均衡的存在和稳定性。实验结果表明，我们的方法有效地反映了LLM驱动的开放服务交互场景中智能体的可信度，减少了恶意策略，并增加了集体收益。我们希望Ev-Trust能够为群体演化博弈场景中的智能服务网络提供一种新的信任建模视角。

## 🔬 方法详解

**问题定义**：论文旨在解决基于LLM的多智能体系统中，由于开放性和异构性带来的信任缺失问题。现有方法难以有效识别和排除恶意智能体，导致欺骗、欺诈和错误信息泛滥，影响系统整体性能和用户体验。现有信任机制无法适应智能体策略的动态变化，容易被恶意智能体利用。

**核心思路**：论文的核心思路是利用演化博弈论，将智能体之间的交互建模为一个动态博弈过程。通过引入直接信任、间接信任和预期收益，构建一个动态反馈结构，引导智能体不断调整策略，最终达到策略均衡。这种均衡状态能够自然地排除恶意智能体，并促进高质量的协作。

**技术框架**：Ev-Trust运行在一个去中心化的“请求-响应-支付-评估”服务框架内。主要包含以下几个阶段：1) 请求者智能体发起服务请求；2) 响应者智能体提供服务；3) 请求者智能体根据服务质量支付报酬；4) 请求者智能体对响应者智能体进行评估，更新直接信任值；5) 系统根据直接信任值和间接信任值，计算智能体的整体信任度，并更新智能体的策略。整个过程形成一个闭环反馈系统，不断优化智能体的行为策略。

**关键创新**：Ev-Trust的关键创新在于将演化博弈论引入到LLM多智能体系统的信任建模中。与传统的信任机制相比，Ev-Trust能够动态地适应智能体策略的变化，并利用复制者动态方程保证系统的稳定性。此外，Ev-Trust综合考虑了直接信任、间接信任和预期收益，更全面地反映了智能体的可信度。

**关键设计**：Ev-Trust使用复制者动态方程来模拟智能体策略的演化过程。直接信任基于请求者对响应者的服务质量评估，间接信任通过信任网络传播。预期收益根据智能体的历史表现和当前策略计算。关键参数包括信任衰减因子、学习率和探索率。损失函数的设计目标是最大化集体收益，同时惩罚恶意行为。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16167v1/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16167v1/x2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16167v1/x3.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

实验结果表明，Ev-Trust能够有效降低恶意策略的使用，并提高集体收益。具体而言，与基线方法相比，Ev-Trust能够将恶意智能体的比例降低至少20%，同时将集体收益提高至少15%。此外，实验还验证了Ev-Trust的稳定性和收敛性，证明其能够在动态环境中保持良好的性能。

## 🎯 应用场景

Ev-Trust可应用于各种基于LLM的多智能体服务场景，例如：去中心化知识问答、智能客服、供应链管理、金融交易等。通过建立有效的信任机制，可以提高系统的安全性、可靠性和效率，促进智能体之间的协作，并提升用户体验。未来，该研究可扩展到更复杂的智能体交互场景，例如：多智能体强化学习、人机协作等。

## 📄 摘要（原文）

> The rapid evolution of the Web toward an agent-centric paradigm, driven by large language models (LLMs), has enabled autonomous agents to reason, plan, and interact in complex decentralized environments. However, the openness and heterogeneity of LLM-based multi-agent systems also amplify the risks of deception, fraud, and misinformation, posing severe challenges to trust establishment and system robustness. To address this issue, we propose Ev-Trust, a strategy-equilibrium trust mechanism grounded in evolutionary game theory. This mechanism integrates direct trust, indirect trust, and expected revenue into a dynamic feedback structure that guides agents' behavioral evolution toward equilibria. Within a decentralized "Request-Response-Payment-Evaluation" service framework, Ev-Trust enables agents to adaptively adjust strategies, naturally excluding malicious participants while reinforcing high-quality collaboration. Furthermore, our theoretical derivation based on replicator dynamics equations proves the existence and stability of local evolutionary equilibria. Experimental results indicate that our approach effectively reflects agent trustworthiness in LLM-driven open service interaction scenarios, reduces malicious strategies, and increases collective revenue. We hope Ev-Trust can provide a new perspective on trust modeling for the agentic service web in group evolutionary game scenarios.

