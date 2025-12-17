---
layout: default
title: Learning Human-Like RL Agents Through Trajectory Optimization With Action Quantization
---

# Learning Human-Like RL Agents Through Trajectory Optimization With Action Quantization

<div class="paper-toolbar">
  <div class="toolbar-left">
    <a href="https://arxiv.org/abs/2511.15055" target="_blank" class="toolbar-btn">arXiv: 2511.15055v1</a>
    <a href="https://arxiv.org/pdf/2511.15055.pdf" target="_blank" class="toolbar-btn">PDF</a>
  </div>
  <div class="toolbar-right">
    <button class="toolbar-btn favorite-btn" data-arxiv-id="2511.15055v1" 
            onclick="toggleFavorite(this, '2511.15055v1', 'Learning Human-Like RL Agents Through Trajectory Optimization With Action Quantization')" title="收藏">
      ☆ 收藏
    </button>
    <button class="toolbar-btn share-btn" onclick="copyLink()" title="复制链接">
      🔗 分享
    </button>
  </div>
</div>


**作者**: Jian-Ting Guo, Yu-Cheng Chen, Ping-Chun Hsieh, Kuo-Hao Ho, Po-Wei Huang, Ti-Rong Wu, I-Chen Wu

**分类**: cs.AI, cs.LG, cs.RO

**发布日期**: 2025-11-19

**备注**: Accepted by the Thirty-Ninth Annual Conference on Neural Information Processing Systems (NeurIPS 2025)

---

## 💡 一句话要点

**提出基于轨迹优化的动作量化方法MAQ，提升强化学习Agent的人类相似度**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `强化学习` `类人Agent` `轨迹优化` `动作量化` `向量量化VAE`

## 📋 核心要点

1. 现有强化学习Agent通常表现出与人类不同的行为，缺乏可解释性和可信度，难以直接应用。
2. 论文提出宏动作量化(MAQ)框架，通过轨迹优化和向量量化VAE学习类人行为，兼顾奖励最大化和行为相似性。
3. 实验表明，MAQ显著提高了Agent的类人度，在D4RL Adroit基准测试中取得了优异的性能和人类评估排名。

## 📝 摘要（中文）

类人Agent一直是人工智能追求的目标之一。尽管强化学习(RL)在许多领域取得了超越人类的表现，但相对较少关注于设计类人RL Agent。因此，许多奖励驱动的RL Agent常常表现出与人类相比不自然的动作，引发了对可解释性和可信度的担忧。为了在RL中实现类人行为，本文首先将类人度形式化为轨迹优化问题，目标是找到一个与人类行为紧密对齐同时最大化奖励的动作序列，并将经典的后退视野控制应用于类人学习，作为一个易于处理和高效的实现。为此，我们引入了宏动作量化(MAQ)，这是一个类人RL框架，通过向量量化VAE将人类演示提炼成宏动作。在D4RL Adroit基准测试上的实验表明，MAQ显著提高了类人度，增加了轨迹相似度得分，并在人类评估研究中获得了所有RL Agent中最高的人类相似度排名。我们的结果还表明，MAQ可以很容易地集成到各种现成的RL算法中，为学习类人RL Agent开辟了一个有希望的方向。代码可在https://rlg.iis.sinica.edu.tw/papers/MAQ获得。

## 🔬 方法详解

**问题定义**：论文旨在解决强化学习Agent行为与人类行为差异大的问题。现有方法通常只关注奖励最大化，忽略了Agent行为的自然性和可解释性，导致Agent在某些场景下表现出不符合人类习惯的动作，降低了其可信度。

**核心思路**：论文的核心思路是将类人行为建模为轨迹优化问题，即寻找一个既能获得高奖励又能与人类行为轨迹相似的动作序列。通过学习人类的宏动作，并将其作为Agent的动作空间，可以约束Agent的行为，使其更接近人类。

**技术框架**：MAQ框架包含以下几个主要模块：1) 人类演示数据收集；2) 使用向量量化VAE (VQ-VAE) 从人类演示数据中学习宏动作；3) 将学习到的宏动作作为强化学习Agent的动作空间；4) 使用后退视野控制(Receding Horizon Control)进行轨迹优化，平衡奖励最大化和与人类行为的相似性。

**关键创新**：论文的关键创新在于提出了宏动作量化(MAQ)的概念，并将其应用于强化学习中。通过VQ-VAE学习人类的宏动作，有效地约束了Agent的动作空间，使其更符合人类的行为模式。此外，将类人度形式化为轨迹优化问题，并使用后退视野控制进行求解，为学习类人Agent提供了一种新的思路。

**关键设计**：VQ-VAE用于学习宏动作，其损失函数包括重构损失和量化损失，用于保证宏动作的表达能力和离散性。后退视野控制的优化目标是奖励和轨迹相似度的加权和，权重参数需要根据具体任务进行调整。Agent的网络结构可以采用各种现有的强化学习算法，如DDPG、SAC等。

## 📊 实验亮点

实验结果表明，MAQ在D4RL Adroit基准测试中显著提高了Agent的类人度，轨迹相似度得分高于其他基线方法。在人类评估研究中，MAQ获得了最高的人类相似度排名，表明其生成的行为更符合人类的认知。此外，MAQ可以很容易地集成到各种现成的RL算法中，具有良好的通用性。

## 🎯 应用场景

该研究成果可应用于机器人控制、游戏AI、自动驾驶等领域，使Agent的行为更自然、可预测，提高人机交互的效率和信任度。例如，在医疗机器人领域，类人Agent可以更好地辅助医生进行手术操作，减少患者的恐惧感。在自动驾驶领域，类人Agent可以更好地理解人类驾驶员的意图，提高驾驶安全性。

## 📄 摘要（原文）

> Human-like agents have long been one of the goals in pursuing artificial intelligence. Although reinforcement learning (RL) has achieved superhuman performance in many domains, relatively little attention has been focused on designing human-like RL agents. As a result, many reward-driven RL agents often exhibit unnatural behaviors compared to humans, raising concerns for both interpretability and trustworthiness. To achieve human-like behavior in RL, this paper first formulates human-likeness as trajectory optimization, where the objective is to find an action sequence that closely aligns with human behavior while also maximizing rewards, and adapts the classic receding-horizon control to human-like learning as a tractable and efficient implementation. To achieve this, we introduce Macro Action Quantization (MAQ), a human-like RL framework that distills human demonstrations into macro actions via Vector-Quantized VAE. Experiments on D4RL Adroit benchmarks show that MAQ significantly improves human-likeness, increasing trajectory similarity scores, and achieving the highest human-likeness rankings among all RL agents in the human evaluation study. Our results also demonstrate that MAQ can be easily integrated into various off-the-shelf RL algorithms, opening a promising direction for learning human-like RL agents. Our code is available at https://rlg.iis.sinica.edu.tw/papers/MAQ.

