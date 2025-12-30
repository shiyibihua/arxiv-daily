---
layout: default
title: Do You Have Freestyle? Expressive Humanoid Locomotion via Audio Control
---

# Do You Have Freestyle? Expressive Humanoid Locomotion via Audio Control

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.23650" class="toolbar-btn" target="_blank">📄 arXiv: 2512.23650v1</a>
  <a href="https://arxiv.org/pdf/2512.23650.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.23650v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.23650v1', 'Do You Have Freestyle? Expressive Humanoid Locomotion via Audio Control')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zhe Li, Cheng Chi, Yangyang Wei, Boan Zhu, Tao Huang, Zhenguo Sun, Yibo Peng, Pengwei Wang, Zhongyuan Wang, Fangzhou Liu, Chang Xu, Shanghang Zhang

**分类**: cs.RO

**发布日期**: 2025-12-29

---

## 💡 一句话要点

**RoboPerform：提出一种基于音频控制的拟人机器人自由运动生成框架**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)**

**关键词**: `音频控制` `拟人机器人` `运动生成` `扩散模型` `人机交互` `风格迁移` `ResMoE` `低延迟`

## 📋 核心要点

1. 现有拟人机器人缺乏表现力，通常局限于预定义的动作或稀疏的指令，难以实现即兴表演。
2. RoboPerform将音频作为隐式风格信号，避免了显式的运动重建，从而降低了延迟并提高了保真度。
3. 实验表明，RoboPerform在物理合理性和音频对齐方面表现出色，使机器人能够根据音频进行舞蹈和手势表演。

## 📝 摘要（中文）

本文提出RoboPerform，首个统一的音频到运动框架，能够直接从音频生成音乐驱动的舞蹈和语音驱动的伴随手势。该框架遵循“运动=内容+风格”的核心原则，将音频视为隐式的风格信号，无需显式的运动重建。RoboPerform集成了ResMoE教师策略以适应不同的运动模式，以及基于扩散的student策略以注入音频风格。这种无需重定向的设计确保了低延迟和高保真度。实验验证表明，RoboPerform在物理合理性和音频对齐方面取得了有希望的结果，成功地将机器人转变为能够对音频做出反应的表演者。

## 🔬 方法详解

**问题定义**：现有方法依赖于显式的运动重建，将音频转换为运动再重定向到机器人，导致级联误差、高延迟以及声学-驱动映射的脱节。因此，如何直接从音频生成高质量、低延迟的机器人运动是一个关键问题。

**核心思路**：RoboPerform的核心思路是将音频视为一种隐式的风格信号，并直接将其注入到运动生成过程中，避免了中间的运动重建步骤。这种方法基于“运动=内容+风格”的原则，认为音频可以提供运动的风格信息，而无需显式地定义运动的细节。

**技术框架**：RoboPerform框架包含一个ResMoE教师策略和一个基于扩散的student策略。ResMoE教师策略用于学习各种运动模式，从而适应不同的运动内容。基于扩散的student策略则负责将音频风格注入到运动生成过程中。整个框架无需运动重定向，直接生成机器人的运动控制信号。

**关键创新**：RoboPerform的关键创新在于其无需显式运动重建的架构。通过将音频作为隐式风格信号，并使用扩散模型进行风格注入，该框架能够生成高质量、低延迟的机器人运动。这种方法避免了传统方法中的级联误差和延迟问题。

**关键设计**：ResMoE教师策略使用混合专家模型（MoE）来学习不同的运动模式。基于扩散的student策略使用扩散模型将音频特征融入到运动生成过程中。损失函数包括运动平滑性损失、音频对齐损失和物理合理性损失，以确保生成的运动既自然又符合物理规律。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.23650v1/x2.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.23650v1/x3.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.23650v1/x4.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

RoboPerform在实验中表现出良好的物理合理性和音频对齐性能。与现有方法相比，RoboPerform能够生成更自然、更流畅的机器人运动，并且能够更好地与音频同步。实验结果表明，RoboPerform成功地将机器人转变为能够对音频做出反应的表演者。

## 🎯 应用场景

RoboPerform具有广泛的应用前景，包括娱乐机器人、人机交互、康复训练等领域。它可以使机器人能够根据音乐进行舞蹈表演，或者根据语音进行伴随手势，从而提高人机交互的自然性和趣味性。此外，该技术还可以应用于康复训练，通过音乐或语音引导患者进行运动。

## 📄 摘要（原文）

> Humans intuitively move to sound, but current humanoid robots lack expressive improvisational capabilities, confined to predefined motions or sparse commands. Generating motion from audio and then retargeting it to robots relies on explicit motion reconstruction, leading to cascaded errors, high latency, and disjointed acoustic-actuation mapping. We propose RoboPerform, the first unified audio-to-locomotion framework that can directly generate music-driven dance and speech-driven co-speech gestures from audio. Guided by the core principle of "motion = content + style", the framework treats audio as implicit style signals and eliminates the need for explicit motion reconstruction. RoboPerform integrates a ResMoE teacher policy for adapting to diverse motion patterns and a diffusion-based student policy for audio style injection. This retargeting-free design ensures low latency and high fidelity. Experimental validation shows that RoboPerform achieves promising results in physical plausibility and audio alignment, successfully transforming robots into responsive performers capable of reacting to audio.

