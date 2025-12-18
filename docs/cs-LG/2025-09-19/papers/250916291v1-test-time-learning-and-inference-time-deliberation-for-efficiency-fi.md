---
layout: default
title: Test-Time Learning and Inference-Time Deliberation for Efficiency-First Offline Reinforcement Learning in Care Coordination and Population Health Management
---

# Test-Time Learning and Inference-Time Deliberation for Efficiency-First Offline Reinforcement Learning in Care Coordination and Population Health Management

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.16291" class="toolbar-btn" target="_blank">📄 arXiv: 2509.16291v1</a>
  <a href="https://arxiv.org/pdf/2509.16291.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.16291v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.16291v1', 'Test-Time Learning and Inference-Time Deliberation for Efficiency-First Offline Reinforcement Learning in Care Coordination and Population Health Management')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Sanjay Basu, Sadiq Y. Patel, Parth Sheth, Bhairavi Muralidharan, Namrata Elamaran, Aakriti Kinra, Rajaie Batniji

**分类**: cs.CY, cs.LG

**发布日期**: 2025-09-19

---

## 💡 一句话要点

**提出TTL+ITD方法，用于高效、可审计的医疗协调离线强化学习。**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `离线强化学习` `测试时学习` `推理时审议` `医疗协调` `人群健康管理`

## 📋 核心要点

1. 现有医疗协调方法在时间和机会成本上存在显著差异，需要更高效的策略。
2. 论文提出TTL+ITD方法，利用测试时学习和推理时审议来优化离线强化学习策略。
3. 实验表明，该方法在价值估计上表现稳定，并能实现可预测的效率权衡和子组审计。

## 📝 摘要（中文）

针对医疗协调和人群健康管理项目需要服务大量医疗补助和安全网人群，并具备可审计性、效率和适应性的需求，本文提出了一种轻量级的离线强化学习（RL）方法。该方法通过（i）基于局部邻域校准的测试时学习（TTL）和（ii）通过包含预测不确定性和时间/努力成本的小型Q-集成进行推理时审议（ITD）来增强训练后的策略。该方法公开了邻域大小和不确定性/成本惩罚的透明控制，并保留了可审计的训练流程。在去识别化的运营数据集上进行评估，TTL+ITD实现了稳定的价值估计，具有可预测的效率权衡和子组审计。

## 🔬 方法详解

**问题定义**：论文旨在解决医疗协调和人群健康管理中，如何利用离线强化学习，在保证策略有效性的前提下，提高效率并实现可审计性。现有方法在不同干预方式（如短信、电话、视频、面访）的时间和机会成本上存在显著差异，需要更智能的策略选择。

**核心思路**：论文的核心思路是通过测试时学习（TTL）和推理时审议（ITD）来增强离线训练的强化学习策略。TTL通过局部邻域校准来适应新的数据，ITD则通过Q-集成考虑预测不确定性和时间/努力成本，从而做出更明智的决策。

**技术框架**：整体框架包含离线训练阶段和在线推理阶段。离线训练阶段使用历史数据训练一个初始的强化学习策略。在线推理阶段，首先利用TTL对策略进行校准，然后利用ITD进行决策。ITD模块使用一个小的Q-集成来估计不同动作的价值，并结合不确定性和成本信息选择最优动作。

**关键创新**：论文的关键创新在于将测试时学习和推理时审议相结合，用于优化离线强化学习策略。TTL使得策略能够适应新的数据分布，ITD则考虑了不确定性和成本因素，从而提高了决策的效率和鲁棒性。此外，该方法提供了透明的控制参数，方便用户根据实际需求进行调整。

**关键设计**：TTL的关键设计在于局部邻域校准，即利用与当前状态相似的历史数据来调整策略。ITD的关键设计在于Q-集成，通过多个Q函数的输出来估计价值的不确定性。论文还设计了成本惩罚项，用于在决策时考虑不同动作的成本。具体的损失函数和网络结构等细节在论文中未明确说明，属于未知信息。

## 📊 实验亮点

实验结果表明，TTL+ITD方法在去识别化的运营数据集上实现了稳定的价值估计，并能够实现可预测的效率权衡。该方法还支持子组审计，方便用户了解策略在不同人群中的表现。具体的性能数据和提升幅度在摘要中未明确说明，属于未知信息。

## 🎯 应用场景

该研究成果可应用于医疗健康领域，例如优化患者关怀计划、疾病管理、健康干预等。通过更智能地分配医疗资源，可以提高医疗服务的效率和质量，降低医疗成本，并改善患者的健康状况。该方法的可审计性也有助于提高医疗决策的透明度和可信度。

## 📄 摘要（原文）

> Care coordination and population health management programs serve large Medicaid and safety-net populations and must be auditable, efficient, and adaptable. While clinical risk for outreach modalities is typically low, time and opportunity costs differ substantially across text, phone, video, and in-person visits. We propose a lightweight offline reinforcement learning (RL) approach that augments trained policies with (i) test-time learning via local neighborhood calibration, and (ii) inference-time deliberation via a small Q-ensemble that incorporates predictive uncertainty and time/effort cost. The method exposes transparent dials for neighborhood size and uncertainty/cost penalties and preserves an auditable training pipeline. Evaluated on a de-identified operational dataset, TTL+ITD achieves stable value estimates with predictable efficiency trade-offs and subgroup auditing.

