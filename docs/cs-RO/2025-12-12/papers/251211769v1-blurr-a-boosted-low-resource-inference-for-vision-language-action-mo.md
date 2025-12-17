---
layout: default
title: BLURR: A Boosted Low-Resource Inference for Vision-Language-Action Models
---

# BLURR: A Boosted Low-Resource Inference for Vision-Language-Action Models

<div class="paper-toolbar">
  <div class="toolbar-left">
    <a href="https://arxiv.org/abs/2512.11769" target="_blank" class="toolbar-btn">arXiv: 2512.11769v1</a>
    <a href="https://arxiv.org/pdf/2512.11769.pdf" target="_blank" class="toolbar-btn">PDF</a>
  </div>
  <div class="toolbar-right">
    <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.11769v1" 
            onclick="toggleFavorite(this, '2512.11769v1', 'BLURR: A Boosted Low-Resource Inference for Vision-Language-Action Models')" title="收藏">
      ☆ 收藏
    </button>
    <button class="toolbar-btn share-btn" onclick="copyLink()" title="复制链接">
      🔗 分享
    </button>
  </div>
</div>


**作者**: Xiaoyu Ma, Zhengqing Yuan, Zheyuan Zhang, Kaiwen Shi, Lichao Sun, Yanfang Ye

**分类**: cs.RO

**发布日期**: 2025-12-12

**备注**: 10 pages, 3 figures. Code and integration scripts will be released at this http URL: https://github.com/JijiKing-Sam/BLURR-A-Boosted-Low-Resource-Inference-for-Vision-Language-Action-Model

---

## 💡 一句话要点

**BLURR：一种加速VLA模型低资源推理的轻量级封装器**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)**

**关键词**: `视觉语言动作模型` `低资源推理` `模型加速` `键值缓存` `混合精度`

## 📋 核心要点

1. 现有VLA模型推理计算量大，难以在算力受限的设备上部署，限制了其应用场景。
2. BLURR通过指令前缀键值缓存、混合精度执行和单步rollout策略，在不重训练的情况下加速VLA模型推理。
3. 实验表明，BLURR在保持任务成功率的同时，显著降低了FLOPs和延迟，并支持交互式Web演示。

## 📝 摘要（中文）

视觉-语言-动作(VLA)模型在零样本操作方面表现出色，但其推理堆栈通常过于庞大，难以在消费级GPU上实现响应式Web演示或高频机器人控制。我们提出了BLURR，一个轻量级的推理封装器，可以插入到现有的VLA控制器中，而无需重新训练或更改模型检查点。BLURR在pi-zero VLA控制器上实例化，保留了原始的观察接口，并通过结合指令前缀键值缓存、混合精度执行和减少每步计算的单步 rollout 策略来加速控制。在基于SimplerEnv的评估中，BLURR保持了与原始控制器相当的任务成功率，同时显著降低了有效FLOPs和wall clock延迟。我们还构建了一个交互式Web演示，允许用户在观看操作过程时实时切换控制器和切换推理选项。这突出了BLURR作为在紧张的计算预算下部署现代VLA策略的一种实用方法。

## 🔬 方法详解

**问题定义**：VLA模型虽然在零样本操作上表现出色，但其庞大的计算需求限制了其在资源受限环境中的部署，例如低功耗机器人或实时Web应用。现有方法通常需要大量的计算资源，难以满足实时性和低延迟的要求。

**核心思路**：BLURR的核心思路是通过一个轻量级的推理封装器，在不修改或重新训练VLA模型本身的情况下，优化推理过程。它利用缓存、量化和优化的rollout策略来减少计算量，从而实现加速。

**技术框架**：BLURR作为一个独立的模块，可以插入到现有的VLA控制器中。它主要包含三个关键组件：1) 指令前缀键值缓存：缓存重复指令的计算结果，避免重复计算；2) 混合精度执行：使用较低精度的数据类型进行计算，减少内存占用和计算量；3) 单步rollout策略：减少每一步的计算量，加速推理过程。整体流程是接收环境观测和指令，利用缓存、量化等技术优化推理，输出动作指令。

**关键创新**：BLURR的关键创新在于其轻量级和即插即用的特性，能够在不影响VLA模型性能的前提下，显著降低推理所需的计算资源。它通过结合多种优化技术，实现了在低资源设备上的高效推理。与需要重新训练或修改模型结构的方法不同，BLURR提供了一种更灵活和实用的解决方案。

**关键设计**：指令前缀键值缓存的设计需要考虑缓存大小和命中率之间的平衡。混合精度执行需要选择合适的精度级别，以在计算效率和精度之间取得平衡。单步rollout策略需要仔细设计，以确保控制器的稳定性和性能。具体的参数设置和实现细节取决于具体的VLA模型和应用场景。

## 📊 实验亮点

实验结果表明，BLURR在SimplerEnv环境中，保持了与原始控制器相当的任务成功率，同时显著降低了有效FLOPs和wall clock延迟。此外，BLURR还支持交互式Web演示，允许用户实时切换控制器和推理选项，展示了其在实际应用中的可行性和灵活性。

## 🎯 应用场景

BLURR可应用于资源受限的机器人控制、实时Web演示、移动设备上的VLA模型部署等场景。它能够降低VLA模型部署的门槛，使其能够在更广泛的设备和应用中使用，例如家庭服务机器人、智能助手和在线教育平台。

## 📄 摘要（原文）

> Vision-language-action (VLA) models enable impressive zero shot manipulation, but their inference stacks are often too heavy for responsive web demos or high frequency robot control on commodity GPUs. We present BLURR, a lightweight inference wrapper that can be plugged into existing VLA controllers without retraining or changing model checkpoints. Instantiated on the pi-zero VLA controller, BLURR keeps the original observation interfaces and accelerates control by combining an instruction prefix key value cache, mixed precision execution, and a single step rollout schedule that reduces per step computation. In our SimplerEnv based evaluation, BLURR maintains task success rates comparable to the original controller while significantly lowering effective FLOPs and wall clock latency. We also build an interactive web demo that allows users to switch between controllers and toggle inference options in real time while watching manipulation episodes. This highlights BLURR as a practical approach for deploying modern VLA policies under tight compute budgets.

