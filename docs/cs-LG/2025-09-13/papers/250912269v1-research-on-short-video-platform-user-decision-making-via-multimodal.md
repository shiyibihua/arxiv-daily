---
layout: default
title: Research on Short-Video Platform User Decision-Making via Multimodal Temporal Modeling and Reinforcement Learning
---

# Research on Short-Video Platform User Decision-Making via Multimodal Temporal Modeling and Reinforcement Learning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.12269" class="toolbar-btn" target="_blank">📄 arXiv: 2509.12269v1</a>
  <a href="https://arxiv.org/pdf/2509.12269.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.12269v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.12269v1', 'Research on Short-Video Platform User Decision-Making via Multimodal Temporal Modeling and Reinforcement Learning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jinmeiyang Wang, Jing Dong, Li Zhou

**分类**: cs.LG, cs.IR

**发布日期**: 2025-09-13

**备注**: 26 pages

---

## 💡 一句话要点

**提出MT-DQN模型，通过多模态时序建模和强化学习优化短视频用户决策预测与推荐。**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `短视频推荐` `多模态学习` `时序建模` `强化学习` `用户行为预测` `Transformer` `图神经网络`

## 📋 核心要点

1. 现有短视频推荐方法难以有效融合多模态信息和用户行为的时序依赖关系，导致推荐效果不佳。
2. MT-DQN模型通过Transformer提取多模态特征，TGNN建模用户行为时序关系，DQN优化推荐策略，实现更精准的推荐。
3. 实验表明，MT-DQN在F1分数和NDCG@5指标上显著优于传统模型，并在MSE和MAE指标上优于Vanilla-DQN。

## 📝 摘要（中文）

本文提出了一种名为MT-DQN的模型，该模型集成了Transformer、时序图神经网络（TGNN）和深度Q网络（DQN），旨在解决短视频环境中预测用户行为和优化推荐策略的挑战。实验结果表明，MT-DQN始终优于传统的拼接模型（如Concat-Modal），平均F1分数提高了10.97%，平均NDCG@5提高了8.3%。与经典的强化学习模型Vanilla-DQN相比，MT-DQN的MSE降低了34.8%，MAE降低了26.5%。然而，我们也认识到在实际场景中部署MT-DQN面临挑战，例如其计算成本和在线推理期间的延迟敏感性，这些问题将在未来的架构优化中得到解决。

## 🔬 方法详解

**问题定义**：论文旨在解决短视频推荐系统中用户行为预测和推荐策略优化的问题。现有方法通常采用简单的拼接方式融合多模态信息，忽略了用户行为的时序依赖关系，并且缺乏有效的推荐策略优化机制，导致推荐精度不高。

**核心思路**：论文的核心思路是利用多模态时序建模来更准确地理解用户行为，并结合强化学习来优化推荐策略。通过Transformer提取多模态特征，TGNN建模用户行为的时序关系，最后利用DQN学习最优的推荐策略。

**技术框架**：MT-DQN模型主要包含三个模块：1) 多模态特征提取模块：使用Transformer提取短视频的视觉、文本等多种模态的特征。2) 时序建模模块：使用TGNN建模用户在短视频平台上的行为序列，捕捉用户行为的时序依赖关系。3) 强化学习模块：使用DQN学习最优的推荐策略，根据用户状态（由多模态特征和时序行为表示）选择合适的推荐动作（即推荐哪个短视频）。

**关键创新**：该模型最重要的创新点在于将多模态时序建模与强化学习相结合，充分利用了短视频的多模态信息和用户行为的时序关系，并利用强化学习优化推荐策略。与传统方法相比，MT-DQN能够更准确地预测用户行为，并提供更个性化的推荐。

**关键设计**：Transformer的层数和隐藏层维度需要根据具体数据集进行调整。TGNN采用GRU作为节点更新函数，并使用Attention机制来学习不同时间步的重要性。DQN使用ε-greedy策略进行探索，并采用经验回放机制来提高训练稳定性。损失函数包括DQN的Q值损失和TGNN的链接预测损失。

## 📊 实验亮点

实验结果表明，MT-DQN模型在短视频推荐任务中取得了显著的性能提升。与传统的拼接模型（Concat-Modal）相比，MT-DQN的平均F1分数提高了10.97%，平均NDCG@5提高了8.3%。与经典的强化学习模型Vanilla-DQN相比，MT-DQN的MSE降低了34.8%，MAE降低了26.5%。

## 🎯 应用场景

该研究成果可应用于各种短视频推荐平台，提升用户体验和平台收益。通过更精准的用户行为预测和个性化推荐，可以提高用户点击率、观看时长和用户粘性。此外，该方法还可以扩展到其他推荐场景，如电商、新闻等。

## 📄 摘要（原文）

> This paper proposes the MT-DQN model, which integrates a Transformer, Temporal Graph Neural Network (TGNN), and Deep Q-Network (DQN) to address the challenges of predicting user behavior and optimizing recommendation strategies in short-video environments. Experiments demonstrated that MT-DQN consistently outperforms traditional concatenated models, such as Concat-Modal, achieving an average F1-score improvement of 10.97% and an average NDCG@5 improvement of 8.3%. Compared to the classic reinforcement learning model Vanilla-DQN, MT-DQN reduces MSE by 34.8% and MAE by 26.5%. Nonetheless, we also recognize challenges in deploying MT-DQN in real-world scenarios, such as its computational cost and latency sensitivity during online inference, which will be addressed through future architectural optimization.

