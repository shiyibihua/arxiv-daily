---
layout: default
title: "SPIRAL: Symbolic LLM Planning via Grounded and Reflective Search"
---

# SPIRAL: Symbolic LLM Planning via Grounded and Reflective Search

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.23167" class="toolbar-btn" target="_blank">📄 arXiv: 2512.23167v1</a>
  <a href="https://arxiv.org/pdf/2512.23167.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.23167v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.23167v1', 'SPIRAL: Symbolic LLM Planning via Grounded and Reflective Search')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yifan Zhang, Giridhar Ganapavarapu, Srideepika Jayaraman, Bhavna Agrawal, Dhaval Patel, Achille Fokoue

**分类**: cs.AI, cs.LG, cs.MA

**发布日期**: 2025-12-29

---

## 💡 一句话要点

**SPIRAL：通过具身和反思搜索实现符号LLM规划**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `规划` `蒙特卡洛树搜索` `具身智能` `反思学习` `自主代理` `符号推理`

## 📋 核心要点

1. 现有LLM在复杂规划任务中，由于线性推理和难以从早期错误恢复，表现不佳，而传统搜索算法又难以有效利用LLM的语义能力。
2. SPIRAL通过将三个LLM代理（规划器、模拟器、评论员）嵌入MCTS循环中，实现有指导、反思和具身的搜索过程，从而提升规划能力。
3. 实验表明，SPIRAL在DailyLifeAPIs数据集上超越现有最佳方法16个百分点，达到83.6%的准确率，并具有更高的token效率。

## 📝 摘要（中文）

大型语言模型(LLMs)在需要探索和自我纠正的复杂规划任务中常常表现不佳，因为它们的线性推理过程难以从早期错误中恢复。虽然像蒙特卡洛树搜索(MCTS)这样的搜索算法可以探索替代方案，但当受到稀疏奖励的指导时，它们通常是无效的，并且无法利用LLM丰富的语义能力。我们引入了SPIRAL（通过具身和反思搜索实现符号LLM规划），这是一个新颖的框架，它将三个专门的LLM代理的认知架构嵌入到MCTS循环中。SPIRAL的关键贡献在于其集成的规划流程，其中规划器提出创造性的下一步，模拟器通过预测现实的结果来支持搜索，而评论员通过反思提供密集的奖励信号。这种协同作用将MCTS从蛮力搜索转变为有指导的、自我纠正的推理过程。在DailyLifeAPIs和HuggingFace数据集上，SPIRAL始终优于默认的思维链规划方法和其他最先进的代理。更重要的是，它大大超过了其他最先进的代理；例如，SPIRAL在DailyLifeAPIs上实现了83.6%的总体准确率，比下一个最佳搜索框架提高了16个百分点以上，同时还表现出卓越的token效率。我们的工作表明，将LLM推理构建为有指导的、反思的和具身的搜索过程可以产生更强大和高效的自主规划器。源代码、完整附录和所有实验数据可在官方项目存储库中获得，以实现可重复性。

## 🔬 方法详解

**问题定义**：论文旨在解决大型语言模型在复杂规划任务中表现不佳的问题。现有方法，如思维链（Chain-of-Thought）推理，通常采用线性推理方式，难以从早期错误中恢复。而传统的搜索算法，如蒙特卡洛树搜索（MCTS），在稀疏奖励下效率低下，且无法充分利用LLM的语义理解能力。

**核心思路**：论文的核心思路是将LLM的推理过程构建为一个有指导的、反思的和具身的搜索过程。通过引入三个专门的LLM代理（规划器、模拟器和评论员），并将其嵌入到MCTS循环中，实现更高效和鲁棒的规划。这种设计旨在结合LLM的语义理解能力和MCTS的探索能力，从而克服传统方法的局限性。

**技术框架**：SPIRAL框架包含以下主要模块：1) **规划器（Planner）**：负责提出创造性的下一步行动方案。2) **模拟器（Simulator）**：负责预测行动方案的现实结果，从而支持搜索过程的具身性。3) **评论员（Critic）**：负责通过反思提供密集的奖励信号，指导搜索过程。这三个模块嵌入到MCTS循环中，形成一个迭代的规划、模拟和评估过程。MCTS负责探索不同的行动序列，而LLM代理负责提供指导和反馈。

**关键创新**：SPIRAL的关键创新在于其集成的规划流程，将LLM的语义理解能力与MCTS的搜索能力相结合。通过引入专门的LLM代理，实现了有指导的、反思的和具身的搜索过程。与传统的MCTS方法相比，SPIRAL能够更有效地利用LLM的知识和推理能力，从而提高规划的效率和准确性。与传统的线性推理方法相比，SPIRAL能够更好地从错误中恢复，并探索更多的替代方案。

**关键设计**：论文中没有明确给出关键参数设置、损失函数或网络结构的具体细节。但是，可以推断，每个LLM代理（规划器、模拟器和评论员）都需要进行适当的prompt工程，以确保其能够有效地执行各自的任务。奖励函数的设计对于评论员的性能至关重要，需要仔细考虑如何将反思结果转化为密集的奖励信号。MCTS的探索策略（如UCT）也需要进行调整，以适应LLM代理的指导。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.23167v1/figures/revision_spiral_intro_final.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.23167v1/figures/revision_spiral_overview_final.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.23167v1/figures/cost_comparison_tokens.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

SPIRAL在DailyLifeAPIs数据集上取得了显著的性能提升，总体准确率达到83.6%，比下一个最佳搜索框架提高了16个百分点以上。此外，SPIRAL还表现出卓越的token效率，这意味着它在实现相同性能的同时，使用的计算资源更少。在HuggingFace数据集上，SPIRAL也优于其他最先进的代理，证明了其泛化能力。

## 🎯 应用场景

SPIRAL框架可应用于各种需要复杂规划和决策的领域，例如机器人导航、任务自动化、游戏AI和智能助手。该框架能够提高自主系统的鲁棒性和效率，使其能够更好地适应复杂和动态的环境。未来，SPIRAL可以扩展到处理更复杂的任务，并与其他技术（如强化学习）相结合，从而实现更强大的自主规划能力。

## 📄 摘要（原文）

> Large Language Models (LLMs) often falter at complex planning tasks that require exploration and self-correction, as their linear reasoning process struggles to recover from early mistakes. While search algorithms like Monte Carlo Tree Search (MCTS) can explore alternatives, they are often ineffective when guided by sparse rewards and fail to leverage the rich semantic capabilities of LLMs. We introduce SPIRAL (Symbolic LLM Planning via Grounded and Reflective Search), a novel framework that embeds a cognitive architecture of three specialized LLM agents into an MCTS loop. SPIRAL's key contribution is its integrated planning pipeline where a Planner proposes creative next steps, a Simulator grounds the search by predicting realistic outcomes, and a Critic provides dense reward signals through reflection. This synergy transforms MCTS from a brute-force search into a guided, self-correcting reasoning process. On the DailyLifeAPIs and HuggingFace datasets, SPIRAL consistently outperforms the default Chain-of-Thought planning method and other state-of-the-art agents. More importantly, it substantially surpasses other state-of-the-art agents; for example, SPIRAL achieves 83.6% overall accuracy on DailyLifeAPIs, an improvement of over 16 percentage points against the next-best search framework, while also demonstrating superior token efficiency. Our work demonstrates that structuring LLM reasoning as a guided, reflective, and grounded search process yields more robust and efficient autonomous planners. The source code, full appendices, and all experimental data are available for reproducibility at the official project repository.

