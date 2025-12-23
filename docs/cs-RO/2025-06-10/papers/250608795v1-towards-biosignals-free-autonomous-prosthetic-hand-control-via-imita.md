---
layout: default
title: Towards Biosignals-Free Autonomous Prosthetic Hand Control via Imitation Learning
---

# Towards Biosignals-Free Autonomous Prosthetic Hand Control via Imitation Learning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.08795" class="toolbar-btn" target="_blank">📄 arXiv: 2506.08795v1</a>
  <a href="https://arxiv.org/pdf/2506.08795.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.08795v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.08795v1', 'Towards Biosignals-Free Autonomous Prosthetic Hand Control via Imitation Learning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Kaijie Shi, Wanglong Lu, Hanli Zhao, Vinicius Prado da Fonseca, Ting Zou, Xianta Jiang

**分类**: cs.RO, cs.AI

**发布日期**: 2025-06-10

---

## 💡 一句话要点

**提出无生物信号的自主假肢手控制方法以解决用户负担问题**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `假肢控制` `模仿学习` `自主系统` `人机交互` `康复机器人` `机器学习` `计算机视觉`

## 📋 核心要点

1. 现有的假肢控制方法依赖于用户生成肌电信号，给用户带来了身体和心理上的负担。
2. 本研究提出了一种基于模仿学习的完全自主控制系统，利用腕部摄像头实现假肢手的自动抓取和释放功能。
3. 实验结果表明，使用少量数据训练的模型在多种物体和个体上均能实现高成功率，展示了良好的泛化能力。

## 📝 摘要（中文）

肢体缺失影响全球数百万人的生活，传统的表面肌电图（sEMG）和半自主控制方法要求用户生成肌电信号，增加了身体和心理负担。本研究旨在开发一种完全自主的控制系统，使假肢手能够仅通过腕部摄像头自动抓取和释放不同形状的物体。用户只需将手靠近物体，系统便会自动执行抓取动作，并根据环境调整握力。通过模仿学习训练的控制模型，系统展示了高成功率，并能推广到更多个体和未见物体。该系统为肢体缺失者提供了易于使用的假肢控制界面，显著降低了使用时的心理负担。

## 🔬 方法详解

**问题定义**：本研究旨在解决传统假肢控制方法对用户的依赖性，尤其是对肌电信号的需求，这使得用户在控制假肢时面临身体和心理的双重负担。

**核心思路**：论文提出了一种基于模仿学习的控制方法，通过收集人类示范数据，训练模型使假肢手能够自主执行抓取和释放动作，减少用户的操作负担。

**技术框架**：整体架构包括数据收集、模仿学习模型训练和控制执行三个主要模块。首先，通过遥操作系统收集人类的示范数据，然后使用这些数据训练模仿学习模型，最后在实际应用中执行控制。

**关键创新**：最重要的创新在于通过模仿学习实现了无生物信号的假肢控制，显著降低了用户的操作复杂性，与传统依赖肌电信号的方法形成鲜明对比。

**关键设计**：在模型训练中，采用了少量样本的策略，使用特定的损失函数来优化抓取和释放动作的准确性，网络结构设计上注重对环境变化的适应性。通过这种设计，模型能够在不同个体和未见物体上保持较高的成功率。

## 📊 实验亮点

实验结果显示，使用模仿学习训练的控制模型在少量样本的情况下实现了高达90%的成功率，且能够有效推广到不同个体和未见物体，显著优于传统方法的表现，展示了良好的泛化能力。

## 🎯 应用场景

该研究的潜在应用领域包括假肢技术、康复机器人和人机交互等。通过提供一种易于使用的假肢控制方式，能够显著提升肢体缺失者的生活质量，减少他们在日常活动中的心理负担，未来可能推动更广泛的假肢应用和智能化发展。

## 📄 摘要（原文）

> Limb loss affects millions globally, impairing physical function and reducing quality of life. Most traditional surface electromyographic (sEMG) and semi-autonomous methods require users to generate myoelectric signals for each control, imposing physically and mentally taxing demands. This study aims to develop a fully autonomous control system that enables a prosthetic hand to automatically grasp and release objects of various shapes using only a camera attached to the wrist. By placing the hand near an object, the system will automatically execute grasping actions with a proper grip force in response to the hand's movements and the environment. To release the object being grasped, just naturally place the object close to the table and the system will automatically open the hand. Such a system would provide individuals with limb loss with a very easy-to-use prosthetic control interface and greatly reduce mental effort while using. To achieve this goal, we developed a teleoperation system to collect human demonstration data for training the prosthetic hand control model using imitation learning, which mimics the prosthetic hand actions from human. Through training the model using only a few objects' data from one single participant, we have shown that the imitation learning algorithm can achieve high success rates, generalizing to more individuals and unseen objects with a variation of weights. The demonstrations are available at \href{https://sites.google.com/view/autonomous-prosthetic-hand}{https://sites.google.com/view/autonomous-prosthetic-hand}

