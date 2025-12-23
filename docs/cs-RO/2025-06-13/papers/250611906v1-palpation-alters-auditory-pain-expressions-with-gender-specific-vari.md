---
layout: default
title: Palpation Alters Auditory Pain Expressions with Gender-Specific Variations in Robopatients
---

# Palpation Alters Auditory Pain Expressions with Gender-Specific Variations in Robopatients

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.11906" class="toolbar-btn" target="_blank">📄 arXiv: 2506.11906v1</a>
  <a href="https://arxiv.org/pdf/2506.11906.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.11906v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.11906v1', 'Palpation Alters Auditory Pain Expressions with Gender-Specific Variations in Robopatients')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Chapa Sirithunge, Yue Xie, Saitarun Nadipineni, Fumiya Iida, Thilina Dulantha Lalitharatne

**分类**: cs.RO

**发布日期**: 2025-06-13

**备注**: 11 pages, 9 figures, journal

---

## 💡 一句话要点

**提出动态生成听觉疼痛表达的机器人以改善医疗培训**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `机器人患者` `听觉疼痛表达` `强化学习` `医疗培训` `多模态反馈` `触诊力` `性别特异性` `疼痛管理`

## 📋 核心要点

1. 现有的医疗训练模拟器在生成多模态反馈方面存在困难，尤其是听觉疼痛表达的生成与触诊行为之间的复杂关系使得探索变得困难。
2. 本文提出了一种新颖的实验范式，利用强化学习技术，使机器人患者能够根据触诊力动态生成听觉疼痛表达，并通过人类反馈进行优化。
3. 实验结果表明，系统能够根据个体的触诊力和声音偏好进行调整，成功捕捉不同强度的疼痛表达，并揭示了性别特异性阈值的存在。

## 📝 摘要（中文）

诊断错误仍然是可预防死亡的主要原因，尤其是在资源有限的地区。医疗训练模拟器，如机器人患者，在减少这些错误方面发挥着重要作用。然而，生成多模态反馈，特别是听觉疼痛表达，依然具有挑战性。本文提出了一种新颖的实验范式，使机器人患者能够根据触诊力动态生成听觉疼痛表达，通过机器学习优化人类反馈。使用强化学习技术Proximal Policy Optimization (PPO)，机器人根据实时人类反馈迭代调整疼痛声音，展示了系统能够适应个体的触诊力和声音偏好，并捕捉从轻微不适到急性痛苦的广泛疼痛强度。研究还表明，疼痛声音感知在较低力量下表现出饱和，并存在性别特异性阈值。这些发现突显了该系统在增强腹部触诊培训中的潜力。

## 🔬 方法详解

**问题定义**：本文旨在解决医疗训练中生成听觉疼痛表达的困难，现有方法难以有效捕捉触诊行为与声音之间的复杂关系。

**核心思路**：通过引入强化学习技术，机器人能够根据触诊力动态生成疼痛声音，并通过实时人类反馈进行优化，从而提高模拟的真实感和有效性。

**技术框架**：整体架构包括机器人患者、触诊力传感器、声音生成模块和强化学习代理。机器人根据触诊力生成初始疼痛声音，RL代理根据反馈进行调整。

**关键创新**：最重要的创新在于将强化学习应用于疼痛声音生成，使机器人能够在动态环境中适应个体的反馈，这与传统静态模型有本质区别。

**关键设计**：在设计中，使用了Proximal Policy Optimization (PPO)算法，设置了适应性损失函数，以便在不同触诊力下优化声音输出，同时考虑性别特异性阈值。

## 📊 实验亮点

实验结果显示，系统能够根据个体的触诊力和声音偏好进行适应，成功捕捉从轻微不适到急性痛苦的广泛疼痛强度。研究还发现，疼痛声音感知在较低力量下表现出饱和，并存在性别特异性阈值，这为个性化医疗培训提供了新的视角。

## 🎯 应用场景

该研究的潜在应用领域包括医疗培训、机器人辅助治疗和疼痛管理等。通过提供可控和沉浸式的模拟平台，能够有效提升医务人员的触诊技能，降低误诊率，尤其在资源有限的地区具有重要的实际价值。

## 📄 摘要（原文）

> Diagnostic errors remain a major cause of preventable deaths, particularly in resource-limited regions. Medical training simulators, including robopatients, play a vital role in reducing these errors by mimicking real patients for procedural training such as palpation. However, generating multimodal feedback, especially auditory pain expressions, remains challenging due to the complex relationship between palpation behavior and sound. The high-dimensional nature of pain sounds makes exploration challenging with conventional methods. This study introduces a novel experimental paradigm for pain expressivity in robopatients where they dynamically generate auditory pain expressions in response to palpation force, by co-optimizing human feedback using machine learning. Using Proximal Policy Optimization (PPO), a reinforcement learning (RL) technique optimized for continuous adaptation, our robot iteratively refines pain sounds based on real-time human feedback. This robot initializes randomized pain responses to palpation forces, and the RL agent learns to adjust these sounds to align with human preferences. The results demonstrated that the system adapts to an individual's palpation forces and sound preferences and captures a broad spectrum of pain intensity, from mild discomfort to acute distress, through RL-guided exploration of the auditory pain space. The study further showed that pain sound perception exhibits saturation at lower forces with gender specific thresholds. These findings highlight the system's potential to enhance abdominal palpation training by offering a controllable and immersive simulation platform.

