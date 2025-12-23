---
layout: default
title: Adversarial Attacks on Robotic Vision Language Action Models
---

# Adversarial Attacks on Robotic Vision Language Action Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.03350" class="toolbar-btn" target="_blank">📄 arXiv: 2506.03350v1</a>
  <a href="https://arxiv.org/pdf/2506.03350.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.03350v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.03350v1', 'Adversarial Attacks on Robotic Vision Language Action Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Eliot Krzysztof Jones, Alexander Robey, Andy Zou, Zachary Ravichandran, George J. Pappas, Hamed Hassani, Matt Fredrikson, J. Zico Kolter

**分类**: cs.RO, cs.AI

**发布日期**: 2025-06-03

**🔗 代码/项目**: [GITHUB](https://github.com/eliotjones1/robogcg)

---

## 💡 一句话要点

**提出对抗攻击方法以解决机器人视觉语言行动模型的脆弱性问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `对抗攻击` `视觉语言模型` `机器人控制` `多模态融合` `安全性研究`

## 📋 核心要点

1. 现有的视觉语言行动模型在面对对抗性攻击时存在显著脆弱性，可能导致机器人控制失效。
2. 本文提出了一种将大型语言模型的越狱攻击适配到VLA的方法，旨在获取对VLA的完全控制权。
3. 实验结果表明，文本攻击能够有效覆盖VLA的动作空间，并在较长时间内保持攻击效果，显示出其潜在风险。

## 📝 摘要（中文）

视觉语言行动模型（VLA）的出现正在重塑机器人领域，使得多模态传感器输入的融合成为可能。然而，基于大型语言模型（LLM）的VLA在面对对抗性攻击时表现出脆弱性。本文首次研究了针对VLA控制机器人的对抗攻击，提出了一种将LLM越狱攻击适应并应用于VLA的方法。研究发现，文本攻击在执行初期施加后，可以实现对常用VLA的完整动作空间的访问，并且这种攻击效果在较长时间内持续存在。所有代码已在GitHub上公开。

## 🔬 方法详解

**问题定义**：本文旨在解决视觉语言行动模型（VLA）在面对对抗性攻击时的脆弱性问题。现有方法未能充分考虑机器人控制中的物理风险，导致VLA可能被恶意利用。

**核心思路**：论文的核心思路是将大型语言模型（LLM）的越狱攻击方法适配到VLA上，通过文本攻击实现对VLA的完全控制。这种设计旨在揭示VLA在实际应用中的潜在风险。

**技术框架**：整体架构包括对VLA的攻击模型设计，攻击流程分为文本攻击的施加和后续动作空间的访问。主要模块包括攻击生成模块和动作执行模块。

**关键创新**：最重要的技术创新在于将LLM越狱攻击方法成功应用于VLA控制的机器人，突破了传统攻击方法的限制，展示了攻击与语义无关的特性。

**关键设计**：在参数设置上，攻击文本的选择和施加时机至关重要，损失函数设计考虑了攻击的有效性和持久性，网络结构则基于现有的VLA架构进行调整以适应攻击需求。

## 📊 实验亮点

实验结果显示，文本攻击能够实现对常用VLA的完整动作空间访问，且攻击效果在较长时间内持续存在。这一发现与现有文献中的越狱攻击有显著不同，表明在实际应用中攻击不必与伤害概念语义相关。

## 🎯 应用场景

该研究的潜在应用领域包括机器人控制、智能家居、自动驾驶等，能够帮助开发更安全的机器人系统，减少对抗攻击带来的风险。未来，研究成果可用于提升机器人在复杂环境中的安全性和可靠性。

## 📄 摘要（原文）

> The emergence of vision-language-action models (VLAs) for end-to-end control is reshaping the field of robotics by enabling the fusion of multimodal sensory inputs at the billion-parameter scale. The capabilities of VLAs stem primarily from their architectures, which are often based on frontier large language models (LLMs). However, LLMs are known to be susceptible to adversarial misuse, and given the significant physical risks inherent to robotics, questions remain regarding the extent to which VLAs inherit these vulnerabilities. Motivated by these concerns, in this work we initiate the study of adversarial attacks on VLA-controlled robots. Our main algorithmic contribution is the adaptation and application of LLM jailbreaking attacks to obtain complete control authority over VLAs. We find that textual attacks, which are applied once at the beginning of a rollout, facilitate full reachability of the action space of commonly used VLAs and often persist over longer horizons. This differs significantly from LLM jailbreaking literature, as attacks in the real world do not have to be semantically linked to notions of harm. We make all code available at https://github.com/eliotjones1/robogcg .

