---
layout: default
title: "ShowUI-$π$: Flow-based Generative Models as GUI Dexterous Hands"
---

# ShowUI-$π$: Flow-based Generative Models as GUI Dexterous Hands

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.24965" class="toolbar-btn" target="_blank">📄 arXiv: 2512.24965v1</a>
  <a href="https://arxiv.org/pdf/2512.24965.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.24965v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.24965v1', 'ShowUI-$π$: Flow-based Generative Models as GUI Dexterous Hands')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Siyuan Hu, Kevin Qinghong Lin, Mike Zheng Shou

**分类**: cs.CV, cs.AI, cs.HC

**发布日期**: 2025-12-31

**备注**: 17 pages, 15 figures

**🔗 代码/项目**: [GITHUB](https://github.com/showlab/showui-pi)

---

## 💡 一句话要点

**ShowUI-$π$：提出基于Flow的生成模型，实现GUI界面的灵巧操作。**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)**

**关键词**: `GUI代理` `Flow模型` `连续动作生成` `灵巧操作` `人机交互`

## 📋 核心要点

1. 现有GUI代理依赖离散点击预测，难以实现需要连续感知和调整的自由拖动轨迹。
2. 提出ShowUI-$π$，使用基于Flow的生成模型，统一建模离散点击和连续拖动动作。
3. 构建ScreenDrag基准测试，实验表明ShowUI-$π$在拖动任务上优于现有商业GUI代理。

## 📝 摘要（中文）

本文提出ShowUI-$π$，首个基于Flow的生成模型，作为GUI界面的灵巧手。该模型具有以下设计：（i）统一离散-连续动作空间，整合离散点击和连续拖动，灵活适应不同交互模式；（ii）基于Flow的动作生成，用于拖动建模，通过轻量级动作专家从连续视觉观察中预测增量光标调整，确保轨迹平滑稳定；（iii）拖动训练数据和基准测试，手动收集并合成跨五个领域的2万条拖动轨迹（如PowerPoint、Adobe Premiere Pro），并引入ScreenDrag基准，包含全面的在线和离线评估协议，用于评估GUI代理的拖动能力。实验表明，商业GUI代理在ScreenDrag上表现不佳（例如，Operator得分13.27，最佳Gemini-2.5-CUA达到22.18）。相比之下，ShowUI-$π$仅用4.5亿参数就达到了26.98，突显了任务的难度和该方法的有效性。希望这项工作能推动GUI代理朝着数字世界中类人灵巧控制的方向发展。

## 🔬 方法详解

**问题定义**：现有GUI代理主要通过预测离散的点击坐标来进行操作，这种方式无法处理需要连续、平滑控制的任务，例如拖动进度条。现有方法的痛点在于无法生成连续的动作轨迹，缺乏对环境变化的实时适应能力，限制了GUI代理的灵活性和操作能力。

**核心思路**：论文的核心思路是将GUI操作建模为一个连续的动作生成过程，利用Flow-based生成模型学习从视觉输入到连续动作的映射。通过预测光标的增量调整，实现平滑的拖动轨迹。这种方法允许代理根据实时视觉反馈进行动态调整，从而提高操作的稳定性和准确性。

**技术框架**：ShowUI-$π$的整体框架包含以下几个主要模块：1) 视觉感知模块：负责从GUI界面捕获视觉信息，提取特征表示。2) 动作专家模块：这是一个轻量级的神经网络，基于视觉特征预测光标的增量调整。3) Flow-based生成模型：利用Flow模型学习动作专家输出的动作分布，从而生成平滑、连续的拖动轨迹。4) 统一动作空间：将离散点击和连续拖动动作整合到一个共享的模型中，实现不同交互模式的灵活切换。

**关键创新**：最重要的技术创新点在于将Flow-based生成模型应用于GUI操作的连续动作生成。与传统的离散动作预测方法相比，ShowUI-$π$能够生成平滑、连续的动作轨迹，更好地模拟人类的灵巧操作。此外，统一离散-连续动作空间的设计也使得模型能够灵活适应不同的交互模式。

**关键设计**：在Flow-based生成模型中，论文可能采用了以下关键设计：1) 轻量级动作专家：为了保证实时性，动作专家采用轻量级网络结构，减少计算负担。2) 损失函数设计：可能采用了基于Flow模型的似然损失函数，以及额外的平滑性约束，以保证生成轨迹的平滑性。3) 数据增强策略：为了提高模型的泛化能力，可能采用了数据增强策略，例如对拖动轨迹进行扰动或变形。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.24965v1/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.24965v1/x2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.24965v1/x3.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

实验结果表明，ShowUI-$π$在ScreenDrag基准测试上取得了显著的性能提升。例如，商业GUI代理Operator的得分为13.27，最佳Gemini-2.5-CUA的得分为22.18，而ShowUI-$π$仅使用4.5亿参数就达到了26.98。这表明ShowUI-$π$在GUI拖动任务上具有更强的性能和更高的效率。

## 🎯 应用场景

该研究成果可应用于自动化测试、RPA（机器人流程自动化）、辅助功能等领域。例如，可以利用该技术自动执行复杂的GUI操作，提高测试效率；帮助残疾人士更方便地使用计算机；在RPA场景中，实现更智能、更灵活的自动化流程。未来，该技术有望进一步扩展到虚拟现实、游戏等领域，实现更自然、更沉浸式的交互体验。

## 📄 摘要（原文）

> Building intelligent agents capable of dexterous manipulation is essential for achieving human-like automation in both robotics and digital environments. However, existing GUI agents rely on discrete click predictions (x,y), which prohibits free-form, closed-loop trajectories (e.g. dragging a progress bar) that require continuous, on-the-fly perception and adjustment. In this work, we develop ShowUI-$π$, the first flow-based generative model as GUI dexterous hand, featuring the following designs: (i) Unified Discrete-Continuous Actions, integrating discrete clicks and continuous drags within a shared model, enabling flexible adaptation across diverse interaction modes; (ii) Flow-based Action Generation for drag modeling, which predicts incremental cursor adjustments from continuous visual observations via a lightweight action expert, ensuring smooth and stable trajectories; (iii) Drag Training data and Benchmark, where we manually collect and synthesize 20K drag trajectories across five domains (e.g. PowerPoint, Adobe Premiere Pro), and introduce ScreenDrag, a benchmark with comprehensive online and offline evaluation protocols for assessing GUI agents' drag capabilities. Our experiments show that proprietary GUI agents still struggle on ScreenDrag (e.g. Operator scores 13.27, and the best Gemini-2.5-CUA reaches 22.18). In contrast, ShowUI-$π$ achieves 26.98 with only 450M parameters, underscoring both the difficulty of the task and the effectiveness of our approach. We hope this work advances GUI agents toward human-like dexterous control in digital world. The code is available at https://github.com/showlab/showui-pi.

