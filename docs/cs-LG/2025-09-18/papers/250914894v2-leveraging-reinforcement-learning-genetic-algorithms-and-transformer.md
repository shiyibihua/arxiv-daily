---
layout: default
title: Leveraging Reinforcement Learning, Genetic Algorithms and Transformers for background determination in particle physics
---

# Leveraging Reinforcement Learning, Genetic Algorithms and Transformers for background determination in particle physics

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.14894" class="toolbar-btn" target="_blank">📄 arXiv: 2509.14894v2</a>
  <a href="https://arxiv.org/pdf/2509.14894.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.14894v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.14894v2', 'Leveraging Reinforcement Learning, Genetic Algorithms and Transformers for background determination in particle physics')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Guillermo Hijano Mendizabal, Davide Lancierini, Alex Marshall, Andrea Mauri, Patrick Haworth Owen, Mitesh Patel, Konstantinos Petridis, Shah Rukh Qasim, Nicola Serra, William Sutcliffe, Hanae Tilquin

**分类**: cs.LG, hep-ex

**发布日期**: 2025-09-18 (更新: 2025-11-20)

**备注**: 34 pages, 12 figures

---

## 💡 一句话要点

**利用强化学习、遗传算法和Transformer解决粒子物理背景确定问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `强化学习` `遗传算法` `Transformer` `粒子物理` `背景确定`

## 📋 核心要点

1. 美强子衰变研究中，背景噪声识别依赖专家经验，缺乏系统方法，且计算资源有限。
2. 提出结合强化学习和遗传算法的新方法，系统性确定关键背景，并用Transformer处理衰变序列。
3. 该方法适用于美强子物理，并可推广到其他粒子物理测量，为背景确定提供新思路。

## 📝 摘要（中文）

在研究美强子衰变时，由于存在大量具有相似末态的不同衰变通道，实验研究面临着各种背景的重大挑战。对于特定的信号衰变，确定最相关的背景过程需要对末态粒子、潜在的误识别和运动学重叠进行详细分析。由于计算资源的限制，这种分析通常仅限于模拟最相关的背景。此外，这个过程通常依赖于物理学家的直觉和专业知识，缺乏系统性的方法。本文旨在提出一种新颖的方法，利用强化学习（RL）系统地确定影响美强子衰变测量的关键背景，从而克服上述挑战。虽然美强子物理学是本研究的案例，但所提出的策略可以广泛地应用于其他类型的粒子物理测量。此外，本文还介绍了一种新的算法，该算法利用RL和遗传算法（GA）之间的协同作用，用于具有高度稀疏奖励和大型轨迹空间的环境。该策略利用GA有效地探索轨迹空间并识别成功的轨迹，这些轨迹用于指导RL代理的训练。我们的方法还包含一个用于RL代理的Transformer架构，以处理表示衰变的token序列。

## 🔬 方法详解

**问题定义**：论文旨在解决粒子物理实验中，特别是美强子衰变研究中，背景噪声难以系统性确定的问题。现有方法依赖物理学家的经验和直觉，缺乏自动化和系统性，且计算资源限制导致无法模拟所有可能的背景过程，影响了信号的准确提取。

**核心思路**：论文的核心思路是利用强化学习（RL）来学习如何识别和确定关键的背景过程。通过将背景确定问题建模为一个序列决策问题，RL agent 可以学习在复杂的实验环境中找到最佳的背景识别策略。同时，结合遗传算法（GA）来加速RL agent的训练，尤其是在奖励稀疏的情况下。

**技术框架**：整体框架包含以下几个主要模块：1) **环境建模**：将粒子物理实验数据转化为RL环境，包括状态空间、动作空间和奖励函数。状态空间可能包括末态粒子的信息，动作空间包括选择不同的背景过程进行模拟，奖励函数则基于模拟结果与真实数据的匹配程度。2) **RL Agent**：使用Transformer架构作为RL agent，处理表示衰变的token序列，学习选择最佳背景过程的策略。3) **遗传算法（GA）**：用于探索轨迹空间，寻找有潜力的轨迹，并用这些轨迹来指导RL agent的训练。GA通过交叉和变异操作，生成新的轨迹，并根据轨迹的奖励值进行选择。4) **训练过程**：RL agent和GA协同工作，GA负责探索，RL agent负责学习和优化策略。

**关键创新**：论文的关键创新在于：1) 将强化学习应用于粒子物理的背景确定问题，提供了一种系统性的解决方案。2) 结合遗传算法和强化学习，加速了RL agent在稀疏奖励环境下的训练。3) 使用Transformer架构处理衰变序列，能够更好地捕捉衰变过程中的复杂关系。

**关键设计**：1) **状态表示**：使用token序列来表示衰变过程，每个token代表一个粒子或中间态。2) **动作空间**：定义了可选择的背景过程集合，每个动作对应选择一个背景过程进行模拟。3) **奖励函数**：根据模拟数据与真实数据的匹配程度来设计奖励函数，例如可以使用卡方检验或似然比检验来衡量匹配程度。4) **Transformer架构**：使用Transformer编码器来处理token序列，提取特征，并使用Transformer解码器来生成动作。5) **GA参数**：需要设置GA的种群大小、交叉概率和变异概率等参数，以控制GA的探索能力。

## 📊 实验亮点

论文提出了一种结合强化学习和遗传算法的新方法，用于粒子物理实验中的背景确定。该方法利用遗传算法加速强化学习的训练，并使用Transformer架构处理衰变序列。虽然论文中没有给出具体的性能数据，但该方法为解决背景确定问题提供了一种新的思路，具有潜在的性能提升空间。未来的工作可以集中在实验验证和性能评估上。

## 🎯 应用场景

该研究成果可应用于粒子物理实验的数据分析，特别是美强子衰变等复杂衰变过程的研究。通过自动识别和排除背景噪声，可以提高信号提取的准确性，从而更精确地测量物理参数，检验标准模型，并寻找新物理的迹象。该方法还可推广到其他科学领域，如生物信息学和金融建模，用于解决类似的背景噪声识别和信号提取问题。

## 📄 摘要（原文）

> Experimental studies of beauty hadron decays face significant challenges due to a wide range of backgrounds arising from the numerous possible decay channels with similar final states. For a particular signal decay, the process for ascertaining the most relevant background processes necessitates a detailed analysis of final state particles, potential misidentifications, and kinematic overlaps, which, due to computational limitations, is restricted to the simulation of only the most relevant backgrounds. Moreover, this process typically relies on the physicist's intuition and expertise, as no systematic method exists.
>   This paper has two primary goals. First, from a particle physics perspective, we present a novel approach that utilises Reinforcement Learning (RL) to overcome the aforementioned challenges by systematically determining the critical backgrounds affecting beauty hadron decay measurements. While beauty hadron physics serves as the case study in this work, the proposed strategy is broadly adaptable to other types of particle physics measurements. Second, from a Machine Learning perspective, we introduce a novel algorithm which exploits the synergy between RL and Genetic Algorithms (GAs) for environments with highly sparse rewards and a large trajectory space. This strategy leverages GAs to efficiently explore the trajectory space and identify successful trajectories, which are used to guide the RL agent's training. Our method also incorporates a transformer architecture for the RL agent to handle token sequences representing decays.

