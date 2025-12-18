---
layout: default
title: Overclocking Electrostatic Generative Models
---

# Overclocking Electrostatic Generative Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.22454" class="toolbar-btn" target="_blank">📄 arXiv: 2509.22454v1</a>
  <a href="https://arxiv.org/pdf/2509.22454.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.22454v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.22454v1', 'Overclocking Electrostatic Generative Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Daniil Shlenskii, Alexander Korotin

**分类**: cs.LG

**发布日期**: 2025-09-26

---

## 💡 一句话要点

**提出逆泊松流匹配以加速电静态生成模型**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `电静态生成模型` `逆泊松流匹配` `蒸馏训练` `图像合成` `计算机视觉` `优化性能`

## 📋 核心要点

1. 现有电静态生成模型如PFGM++在样本生成时依赖昂贵的ODE模拟，导致计算成本高昂。
2. 本文提出逆泊松流匹配（IPFM），将蒸馏过程重新定义为一个逆问题，以加速电静态生成模型的训练和生成过程。
3. 实验结果表明，IPFM在有限维度下的样本质量接近或优于教师模型，并且收敛速度更快，优化和采样性能更佳。

## 📝 摘要（中文）

电静态生成模型如PFGM++最近成为图像合成领域的强大框架，表现出色。然而，PFGM++在生成样本时依赖于昂贵的ODE模拟，计算成本高。为了解决这一问题，本文提出了逆泊松流匹配（IPFM），一种新的蒸馏框架，能够加速所有维度下的电静态生成模型。通过将蒸馏重新定义为逆问题，IPFM学习一个生成器，使其诱导的电静态场与教师模型匹配。实验证明，IPFM能够以少量函数评估生成接近或优于教师模型的样本质量，并且在有限维度下收敛速度更快。

## 🔬 方法详解

**问题定义**：本文旨在解决电静态生成模型在样本生成过程中计算成本高的问题，现有方法如PFGM++依赖于昂贵的ODE模拟，限制了其实用性。

**核心思路**：提出逆泊松流匹配（IPFM），将蒸馏过程视为一个逆问题，通过学习一个生成器，使其诱导的电静态场与教师模型的电静态场相匹配，从而加速生成过程。

**技术框架**：IPFM的整体架构包括一个生成器和一个教师模型，生成器通过优化其电静态场与教师模型的电静态场一致来进行训练。训练目标经过重新定义，使得学习过程更加高效。

**关键创新**：IPFM的主要创新在于将蒸馏过程重新定义为逆问题，这一设计使得生成器能够在有限维度下更快收敛，并且在样本质量上接近或优于教师模型。

**关键设计**：在训练过程中，IPFM采用了一种可处理的训练目标，关键参数设置和损失函数设计确保了生成器的电静态场能够有效匹配教师模型的电静态场。

## 📊 实验亮点

实验结果显示，IPFM在有限维度下生成的样本质量接近或优于教师模型，且仅需少量函数评估。此外，有限维度下的蒸馏过程收敛速度显著快于无穷维度的情况，验证了模型的优化和采样性能。

## 🎯 应用场景

该研究的潜在应用领域包括图像合成、计算机视觉和机器人等领域。通过加速电静态生成模型的训练和生成过程，IPFM能够在实际应用中提高生成效率和样本质量，推动相关技术的发展。

## 📄 摘要（原文）

> Electrostatic generative models such as PFGM++ have recently emerged as a powerful framework, achieving state-of-the-art performance in image synthesis. PFGM++ operates in an extended data space with auxiliary dimensionality $D$, recovering the diffusion model framework as $D\to\infty$, while yielding superior empirical results for finite $D$. Like diffusion models, PFGM++ relies on expensive ODE simulations to generate samples, making it computationally costly. To address this, we propose Inverse Poisson Flow Matching (IPFM), a novel distillation framework that accelerates electrostatic generative models across all values of $D$. Our IPFM reformulates distillation as an inverse problem: learning a generator whose induced electrostatic field matches that of the teacher. We derive a tractable training objective for this problem and show that, as $D \to \infty$, our IPFM closely recovers Score Identity Distillation (SiD), a recent method for distilling diffusion models. Empirically, our IPFM produces distilled generators that achieve near-teacher or even superior sample quality using only a few function evaluations. Moreover, we observe that distillation converges faster for finite $D$ than in the $D \to \infty$ (diffusion) limit, which is consistent with prior findings that finite-$D$ PFGM++ models exhibit more favorable optimization and sampling properties.

