---
layout: default
title: Switch-JustDance: Benchmarking Whole Body Motion Tracking Policies Using a Commercial Console Game
---

# Switch-JustDance: Benchmarking Whole Body Motion Tracking Policies Using a Commercial Console Game

<div class="paper-toolbar">
  <div class="toolbar-left">
    <a href="https://arxiv.org/abs/2511.17925" target="_blank" class="toolbar-btn">arXiv: 2511.17925v2</a>
    <a href="https://arxiv.org/pdf/2511.17925.pdf" target="_blank" class="toolbar-btn">PDF</a>
  </div>
  <div class="toolbar-right">
    <button class="toolbar-btn favorite-btn" data-arxiv-id="2511.17925v2" 
            onclick="toggleFavorite(this, '2511.17925v2', 'Switch-JustDance: Benchmarking Whole Body Motion Tracking Policies Using a Commercial Console Game')" title="收藏">
      ☆ 收藏
    </button>
    <button class="toolbar-btn share-btn" onclick="copyLink()" title="复制链接">
      🔗 分享
    </button>
  </div>
</div>


**作者**: Jeonghwan Kim, Wontaek Kim, Yidan Lu, Jin Cheng, Fatemeh Zargarbashi, Zicheng Zeng, Zekun Qi, Zhiyang Dou, Nitish Sontakke, Donghoon Baek, Sehoon Ha, Tianyu Li

**分类**: cs.RO, cs.CV

**发布日期**: 2025-11-22 (更新: 2025-12-08)

---

## 💡 一句话要点

**提出Switch-JustDance：利用商业游戏评估全身运动跟踪策略的低成本基准测试方案**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱七：动作重定向 (Motion Retargeting)**

**关键词**: `全身运动控制` `机器人基准测试` `运动重定向` `人形机器人` `Just Dance`

## 📋 核心要点

1. 现有全身运动控制评估依赖预采集数据或仿真，缺乏真实环境下的可重复性和人机公平比较。
2. Switch-JustDance利用Nintendo Switch上的Just Dance游戏，将舞蹈动作转化为机器人可执行的运动。
3. 实验验证了Just Dance作为基准测试平台的可靠性，并对三种全身控制器进行了硬件基准测试。

## 📝 摘要（中文）

全身机器人控制的最新进展使人形和腿式机器人能够执行越来越敏捷和协调的运动。然而，在真实环境中评估这些能力，并与人类进行直接比较的标准基准仍然稀缺。现有的评估通常依赖于预先收集的人类运动数据集或基于仿真的实验，这限制了可重复性，忽略了硬件因素，并阻碍了公平的人机比较。我们提出了Switch-JustDance，一种低成本且可重复的基准测试流程，它利用运动感应主机游戏，即Nintendo Switch上的Just Dance，来评估机器人全身控制。Switch-JustDance以Nintendo Switch上的Just Dance作为代表性平台，通过流式传输、运动重建和运动重定向模块将游戏中的舞蹈动作转换为机器人可执行的运动，并使用游戏内置的评分系统评估控制器性能。我们首先验证了Just Dance的评估属性，分析了其可靠性、有效性、灵敏度和潜在的偏差来源。结果表明，该平台提供了一致且可解释的性能指标，使其成为具身人工智能基准测试的合适工具。在此基础上，我们在硬件上对三种最先进的人形全身控制器进行了基准测试，并深入了解了它们的相对优势和局限性。

## 🔬 方法详解

**问题定义**：现有全身运动控制算法的评估缺乏标准化的、低成本且可重复的真实环境基准。现有方法依赖于预先收集的人类运动数据或仿真环境，难以保证可重复性，忽略了硬件因素的影响，并且难以进行公平的人机性能比较。

**核心思路**：利用商业游戏（Nintendo Switch上的Just Dance）作为基准测试平台。Just Dance提供了一种低成本、易于获取且具有内置评分机制的运动捕捉和评估系统。通过将游戏中的舞蹈动作转化为机器人可执行的运动，可以实现对机器人全身运动控制算法的有效评估。

**技术框架**：Switch-JustDance包含以下主要模块：1) **流式传输模块**：从Nintendo Switch获取游戏数据。2) **运动重建模块**：将游戏数据重建为三维运动轨迹。3) **运动重定向模块**：将三维运动轨迹映射到机器人身上，生成机器人可执行的运动指令。4) **评估模块**：利用Just Dance内置的评分系统评估机器人的运动表现。

**关键创新**：该方法的核心创新在于将商业游戏作为机器人全身运动控制算法的基准测试平台。与传统的基于预采集数据或仿真的方法相比，Switch-JustDance具有低成本、可重复性高、易于获取等优点，并且能够进行公平的人机性能比较。

**关键设计**：运动重定向模块是关键设计之一，需要考虑机器人和人类的运动学差异，以及机器人的运动能力限制。论文中可能使用了逆运动学、优化算法等技术来实现运动重定向。评估模块直接使用Just Dance的评分系统，该系统考虑了动作的准确性、节奏感等因素。

## 📊 实验亮点

论文验证了Just Dance作为基准测试平台的可靠性、有效性和灵敏度。通过对三种最先进的人形全身控制器进行硬件基准测试，揭示了它们在真实环境中的相对优势和局限性。实验结果表明，Switch-JustDance可以提供一致且可解释的性能指标，为机器人全身运动控制算法的评估提供了一种有效的工具。

## 🎯 应用场景

该研究成果可应用于机器人全身运动控制算法的开发和评估，特别是在人形机器人和腿式机器人领域。该基准测试平台可以帮助研究人员快速评估不同控制算法的性能，并促进算法的改进和优化。此外，该方法还可以用于机器人运动技能的学习和模仿，以及人机协作等领域。

## 📄 摘要（原文）

> Recent advances in whole-body robot control have enabled humanoid and legged robots to perform increasingly agile and coordinated motions. However, standardized benchmarks for evaluating these capabilities in real-world settings, and in direct comparison to humans, remain scarce. Existing evaluations often rely on pre-collected human motion datasets or simulation-based experiments, which limit reproducibility, overlook hardware factors, and hinder fair human-robot comparisons. We present Switch-JustDance, a low-cost and reproducible benchmarking pipeline that leverages motion-sensing console games, Just Dance on the Nintendo Switch, to evaluate robot whole-body control. Using Just Dance on the Nintendo Switch as a representative platform, Switch-JustDance converts in-game choreography into robot-executable motions through streaming, motion reconstruction, and motion retargeting modules and enables users to evaluate controller performance through the game's built-in scoring system. We first validate the evaluation properties of Just Dance, analyzing its reliability, validity, sensitivity, and potential sources of bias. Our results show that the platform provides consistent and interpretable performance measures, making it a suitable tool for benchmarking embodied AI. Building on this foundation, we benchmark three state-of-the-art humanoid whole-body controllers on hardware and provide insights into their relative strengths and limitations.

