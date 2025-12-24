---
layout: default
title: Physiology-informed layered sensing for intelligent human-exoskeleton interaction
---

# Physiology-informed layered sensing for intelligent human-exoskeleton interaction

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.12157" class="toolbar-btn" target="_blank">📄 arXiv: 2508.12157v2</a>
  <a href="https://arxiv.org/pdf/2508.12157.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.12157v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.12157v2', 'Physiology-informed layered sensing for intelligent human-exoskeleton interaction')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Chenyu Tang, Yu Zhu, Josée Mallah, Wentian Yi, Luyao Jin, Zibo Zhang, Shengbo Wang, Muzi Xu, Ming Shen, Calvin Kalun Or, Shuo Gao, Shaoping Bai, Luigi G. Occhipinti

**分类**: eess.SY

**发布日期**: 2025-08-16 (更新: 2025-10-16)

**备注**: 21 pages, 5 figures, 43 references

---

## 💡 一句话要点

**提出生理信息驱动的分层传感技术以提升人机外骨骼交互**

🎯 **匹配领域**: **支柱八：物理动画 (Physics-based Animation)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `外骨骼` `生理信息` `多模态传感` `实时监测` `智能控制` `康复技术` `用户体验`

## 📋 核心要点

1. 现有的外骨骼技术在实验室外的应用受到限制，主要因为传感系统无法捕捉用户的生理状态。
2. 本文提出了一种集成多种传感技术的智能腿套，能够实时监测用户的生理信息，以提升外骨骼的适应性和安全性。
3. 实验结果显示，该系统在踝关节力矩估计、代谢趋势分类和受伤风险检测方面表现优异，准确率和召回率均高于现有技术。

## 📝 摘要（中文）

可穿戴外骨骼在恢复肌肉无力或其他障碍用户的移动能力方面具有变革性潜力。然而，现有的传感系统仅捕捉运动而未能反映潜在生理状态。本文提出了一种柔软、轻便的智能腿套，通过整合基于纺织的表面肌电图（sEMG）电极、超灵敏纺织应变传感器和惯性测量单元（IMU），实现了解剖学对齐的分层多模态传感。每种传感方式针对不同的生理层次，IMU跟踪关节运动学，sEMG监测肌肉激活，应变传感器检测皮肤变形。这些传感器共同提供实时感知，支持个性化辅助控制、优化用户努力和防止受伤风险。该系统与皮肤紧密贴合，机械兼容性好，且与定制外骨骼无缝集成。实验结果表明，该系统在未见用户上实现了准确的踝关节力矩估计、实时代谢趋势分类和快速的受伤风险检测。

## 🔬 方法详解

**问题定义**：本文旨在解决现有外骨骼技术在实际应用中无法有效捕捉用户生理信息的问题，导致个性化辅助不足和安全风险增加。

**核心思路**：通过设计一种集成多种传感器的智能腿套，实时监测用户的生理状态，从而实现更智能的外骨骼控制和用户体验优化。

**技术框架**：该系统包括三个主要模块：1) 基于纺织的sEMG电极用于肌肉激活监测；2) 超灵敏的应变传感器用于皮肤变形检测；3) IMU用于关节运动学跟踪。所有传感器数据实时融合，提供全面的生理信息。

**关键创新**：该研究的创新在于将生理信息与运动跟踪结合，形成了一种新的感知架构，使外骨骼系统能够从单纯的运动捕捉转变为实时生理解码。

**关键设计**：系统设计中，传感器总重量小于20克，确保了用户的舒适性和可穿戴性；采用了高精度的算法进行数据处理，以实现踝关节力矩的准确估计和代谢趋势的实时分类。

## 📊 实验亮点

实验结果显示，该系统在踝关节力矩估计方面的均方根误差为0.13 Nm/kg，代谢趋势分类的准确率达到97.1%，而受伤风险检测的召回率高达0.96，所有结果均在未见用户上验证，显示出显著的性能提升。

## 🎯 应用场景

该研究的潜在应用领域包括康复医学、老年人辅助设备以及运动员训练等。通过实时监测用户的生理状态，外骨骼能够提供个性化的支持，提升用户的安全性和舒适性，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> Wearable exoskeletons hold transformative promise for restoring mobility across diverse users with muscular weakness or other impairments. However, their translation beyond laboratory environments remains limited by sensing systems that capture movement but not underlying physiology. Here, we present a soft, lightweight smart leg sleeve that achieves anatomically aligned, layered multimodal sensing by integrating textile-based surface electromyography (sEMG) electrodes, ultrasensitive textile strain sensors, and inertial measurement units (IMUs). Each sensing modality targets a distinct physiological layer: IMUs track joint kinematics at the skeletal level, sEMG monitors muscle activation at the muscular level, and strain sensors detect skin deformation at the cutaneous level. Together, these sensors provide real-time perception to support three core objectives: controlling personalized assistance, optimizing user effort, and safeguarding against injury risks. The system is skin-conformal, mechanically compliant, and seamlessly integrated with a custom exoskeleton ($<20$~g total sensor and electronics weight). We demonstrate: (1) accurate ankle joint moment estimation (RMSE = 0.13~Nm/kg), (2) real-time classification of metabolic trends (accuracy = 97.1\%), and (3) injury risk detection within 100~ms (recall = 0.96), all validated on unseen users using a leave-one-subject-out protocol. This work establishes a physiology-aligned sensing architecture that reframes exoskeleton perception from motion tracking to real-time physiological decoding, offering a pathway towards intelligent, adaptive, and personalized wearable robotics.

