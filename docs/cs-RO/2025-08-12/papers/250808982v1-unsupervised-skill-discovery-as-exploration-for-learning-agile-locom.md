---
layout: default
title: Unsupervised Skill Discovery as Exploration for Learning Agile Locomotion
---

# Unsupervised Skill Discovery as Exploration for Learning Agile Locomotion

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.08982" class="toolbar-btn" target="_blank">📄 arXiv: 2508.08982v1</a>
  <a href="https://arxiv.org/pdf/2508.08982.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.08982v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.08982v1', 'Unsupervised Skill Discovery as Exploration for Learning Agile Locomotion')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Seungeun Rho, Kartik Garg, Morgan Byrd, Sehoon Ha

**分类**: cs.RO, cs.AI, cs.LG

**发布日期**: 2025-08-12

**备注**: Conference on Robot Learning 2025

---

## 💡 一句话要点

**提出SDAX框架以解决腿部机器人灵活运动学习中的探索问题**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `无监督学习` `技能发现` `动态探索` `四足机器人` `灵活运动` `强化学习` `机器人控制`

## 📋 核心要点

1. 现有方法在腿部机器人灵活运动学习中面临探索困难，依赖人工设计的奖励和示范，限制了其适应性和通用性。
2. 本文提出的SDAX框架通过无监督技能发现，自动获取多样技能，减少了对人工工程的依赖，并动态调节探索程度。
3. 实验结果显示，SDAX使四足机器人成功学习到多种灵活运动行为，并在真实硬件上验证了策略的有效性，具有良好的迁移能力。

## 📝 摘要（中文）

探索对于使四足机器人学习灵活的运动行为至关重要，这些行为能够克服多样的障碍。然而，现有方法往往依赖于大量的奖励工程、专家示范或课程学习，这限制了其通用性。本文提出了一种新的学习框架——技能发现作为探索（SDAX），显著减少了人类工程的努力。SDAX利用无监督的技能发现，自动获取多样的技能以克服障碍。通过双层优化过程，SDAX动态调节训练过程中的探索程度。实验表明，SDAX使四足机器人获得了包括爬行、攀爬、跳跃及复杂动作（如从垂直墙面跳下）的高度灵活行为，并成功将学习到的策略部署到真实硬件上，验证了其在现实世界中的有效性。

## 🔬 方法详解

**问题定义**：本文旨在解决腿部机器人在学习灵活运动行为时的探索困难，现有方法依赖于人工设计的奖励和示范，导致通用性不足。

**核心思路**：SDAX框架的核心思路是通过无监督技能发现，自动获取多样的运动技能，从而减少对人类工程的依赖，并通过双层优化动态调节探索程度。

**技术框架**：SDAX的整体架构包括技能发现模块和双层优化模块。技能发现模块负责自动获取技能，而双层优化模块则根据训练进展动态调整探索的强度。

**关键创新**：SDAX的主要创新在于将无监督技能发现与动态探索调节相结合，使得机器人能够在没有大量人工干预的情况下，学习到复杂的运动技能。与传统方法相比，SDAX显著提高了学习效率和技能多样性。

**关键设计**：在SDAX中，关键设计包括双层优化过程的具体实现，探索程度的调节策略，以及技能发现过程中使用的损失函数和网络结构，这些设计确保了技能的多样性和学习的有效性。

## 📊 实验亮点

实验结果表明，使用SDAX框架的四足机器人成功学习到多种灵活运动行为，包括爬行、攀爬和跳跃等。与基线方法相比，SDAX在学习效率和技能多样性上有显著提升，验证了其在真实环境中的有效性。

## 🎯 应用场景

该研究的潜在应用领域包括服务机器人、救援机器人和探索机器人等。通过提高机器人在复杂环境中的灵活运动能力，SDAX框架能够在灾难救援、环境监测等实际场景中发挥重要作用，提升机器人的自主性和适应性。

## 📄 摘要（原文）

> Exploration is crucial for enabling legged robots to learn agile locomotion behaviors that can overcome diverse obstacles. However, such exploration is inherently challenging, and we often rely on extensive reward engineering, expert demonstrations, or curriculum learning - all of which limit generalizability. In this work, we propose Skill Discovery as Exploration (SDAX), a novel learning framework that significantly reduces human engineering effort. SDAX leverages unsupervised skill discovery to autonomously acquire a diverse repertoire of skills for overcoming obstacles. To dynamically regulate the level of exploration during training, SDAX employs a bi-level optimization process that autonomously adjusts the degree of exploration. We demonstrate that SDAX enables quadrupedal robots to acquire highly agile behaviors including crawling, climbing, leaping, and executing complex maneuvers such as jumping off vertical walls. Finally, we deploy the learned policy on real hardware, validating its successful transfer to the real world.

