---
layout: default
title: Long-Term Variability in Physiological-Arousal Relationships for Robust Emotion Estimation
---

# Long-Term Variability in Physiological-Arousal Relationships for Robust Emotion Estimation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.18782" class="toolbar-btn" target="_blank">📄 arXiv: 2508.18782v1</a>
  <a href="https://arxiv.org/pdf/2508.18782.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.18782v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.18782v1', 'Long-Term Variability in Physiological-Arousal Relationships for Robust Emotion Estimation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Hiroto Sakimura, Takayuki Nagaya, Tomoki Nishi, Tetsuo Kurahashi, Katsunori Kohda, Nobuhiko Muramoto

**分类**: cs.HC, cs.AI

**发布日期**: 2025-08-26

**备注**: 9 pages, 5 figures, accepted at 13th International Conference on Affective Computing and Intelligent Interaction (ACII 2025)

---

## 💡 一句话要点

**提出长期生理唤醒关系变异性研究以提升情感估计模型的鲁棒性**

🎯 **匹配领域**: **支柱八：物理动画 (Physics-based Animation)**

**关键词**: `情感估计` `生理信号` `长期变异性` `可解释性模型` `心理生理学` `数据收集` `个体差异` `情感计算`

## 📋 核心要点

1. 现有情感估计方法通常假设生理信号与情感状态之间的关系是稳定的，但缺乏长期验证，可能导致模型性能下降。
2. 本研究通过开发定制测量系统，收集纵向生理信号和情感状态数据，探讨生理唤醒关系的时间变异性。
3. 实验结果显示，模型在不同时间段的准确率存在显著差异，心率预测相对稳定，而EDA则表现出个体差异，提示模型需定期更新。

## 📝 摘要（中文）

从生理信号中估计情感状态是情感计算和心理生理学的核心课题。尽管许多情感估计系统隐含假设生理特征与主观情感之间的关系是稳定的，但这一假设在长期时间框架内鲜有验证。本研究探讨了个体在数月内生理唤醒关系的一致性。我们开发了定制测量系统，并通过收集24名参与者在自然工作环境中的生理信号和自我报告的情感状态，构建了一个纵向数据集。研究发现，生理唤醒关系随时间演变，模型在第一阶段数据训练后，第二阶段测试准确率下降5%，表明生理唤醒关联的长期变异性。心率作为相对稳定的预测因子，而最小EDA则在个体层面上表现出显著波动。这些发现强调了考虑生理唤醒关系的时间变异性的重要性，并建议情感估计模型应定期更新以维持鲁棒性能。

## 🔬 方法详解

**问题定义**：本研究旨在解决生理信号与情感状态之间关系的长期稳定性问题。现有方法通常假设这种关系是恒定的，但缺乏对时间变化的考虑，可能导致情感估计模型的准确性下降。

**核心思路**：本研究的核心思路是通过纵向数据分析，探讨个体在不同时间段内生理信号与情感状态之间的关系变化。通过使用可解释的增强机器（EBM），确保模型的可解释性和透明度。

**技术框架**：研究首先开发了一个定制的测量系统，收集包括血容量脉搏、皮肤电活动、皮肤温度和加速度等生理信号。数据在自然工作环境中收集，形成纵向数据集。接着，使用EBM对数据进行分析，比较不同时间段的生理唤醒关系。

**关键创新**：本研究的关键创新在于首次系统性地验证了生理信号与情感状态之间关系的长期变异性，强调了情感估计模型需定期更新的必要性。与现有方法相比，提供了更具时效性的情感估计策略。

**关键设计**：研究中使用的EBM模型确保了结果的可解释性，关键参数设置包括对生理信号的特征提取和模型训练过程中的超参数优化。模型在第一阶段训练后，第二阶段测试准确率下降5%，显示出生理唤醒关系的个体差异和时间依赖性。

## 📊 实验亮点

实验结果表明，使用EBM模型时，第一阶段数据训练后，第二阶段测试准确率下降5%，显示出生理唤醒关系的长期变异性。心率作为稳定预测因子，而最小EDA在个体层面上表现出显著波动，提示情感估计模型需考虑时间变化。

## 🎯 应用场景

该研究的潜在应用领域包括情感计算、心理健康监测和人机交互等。通过定期更新情感估计模型，可以提高情感识别的准确性和鲁棒性，进而提升用户体验和心理干预效果。未来，基于此研究的情感估计系统可能在智能设备和健康管理中发挥重要作用。

## 📄 摘要（原文）

> Estimating emotional states from physiological signals is a central topic in affective computing and psychophysiology. While many emotion estimation systems implicitly assume a stable relationship between physiological features and subjective affect, this assumption has rarely been tested over long timeframes. This study investigates whether such relationships remain consistent across several months within individuals. We developed a custom measurement system and constructed a longitudinal dataset by collecting physiological signals -- including blood volume pulse, electrodermal activity (EDA), skin temperature, and acceleration--along with self-reported emotional states from 24 participants over two three-month periods. Data were collected in naturalistic working environments, allowing analysis of the relationship between physiological features and subjective arousal in everyday contexts. We examined how physiological-arousal relationships evolve over time by using Explainable Boosting Machines (EBMs) to ensure model interpretability. A model trained on 1st-period data showed a 5\% decrease in accuracy when tested on 2nd-period data, indicating long-term variability in physiological-arousal associations. EBM-based comparisons further revealed that while heart rate remained a relatively stable predictor, minimum EDA exhibited substantial individual-level fluctuations between periods. While the number of participants is limited, these findings highlight the need to account for temporal variability in physiological-arousal relationships and suggest that emotion estimation models should be periodically updated -- e.g., every five months -- based on observed shift trends to maintain robust performance over time.

