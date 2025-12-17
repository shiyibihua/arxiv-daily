---
layout: default
title: AttackVLA: Benchmarking Adversarial and Backdoor Attacks on Vision-Language-Action Models
---

# AttackVLA: Benchmarking Adversarial and Backdoor Attacks on Vision-Language-Action Models

**arXiv**: [2511.12149v1](https://arxiv.org/abs/2511.12149) | [PDF](https://arxiv.org/pdf/2511.12149.pdf)

**作者**: Jiayu Li, Yunhan Zhao, Xiang Zheng, Zonghuan Xu, Yige Li, Xingjun Ma, Yu-Gang Jiang

**分类**: cs.CR, cs.AI, cs.CV

**发布日期**: 2025-11-15

---

## 💡 一句话要点

**AttackVLA提出统一框架，评估并提升视觉-语言-动作模型的对抗鲁棒性。**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)**

**关键词**: `视觉-语言-动作模型` `对抗攻击` `后门攻击` `机器人安全` `具身智能`

## 📋 核心要点

1. 现有VLA模型攻击方法缺乏统一评估框架，且真实场景验证不足，导致攻击效果不明确。
2. AttackVLA框架统一数据构建、模型训练和推理流程，并提出BackdoorVLA实现精准长程动作序列攻击。
3. BackdoorVLA在模拟和真实机器人环境中取得了平均58.4%的目标攻击成功率，部分任务达到100%。

## 📝 摘要（中文）

视觉-语言-动作（VLA）模型使机器人能够理解自然语言指令并执行各种任务，但其感知、语言和控制的集成引入了新的安全漏洞。尽管人们对攻击此类模型的兴趣日益浓厚，但由于缺乏统一的评估框架，现有技术的有效性仍不清楚。一个主要问题是，VLA架构之间动作标记器的差异阻碍了可重复性和公平比较。更重要的是，大多数现有攻击尚未在真实场景中得到验证。为了应对这些挑战，我们提出了AttackVLA，这是一个与VLA开发生命周期保持一致的统一框架，涵盖数据构建、模型训练和推理。在该框架内，我们实施了一套广泛的攻击，包括所有现有的针对VLA的攻击和多个最初为视觉-语言模型开发的改编攻击，并在模拟和真实环境中对其进行评估。我们对现有攻击的分析揭示了一个关键差距：当前的方法倾向于导致无目标失败或静态动作状态，使得驱动VLA执行精确的长程动作序列的有目标攻击在很大程度上未被探索。为了填补这一空白，我们引入了BackdoorVLA，这是一种有目标的后门攻击，它迫使VLA在出现触发器时执行攻击者指定的长程动作序列。我们在模拟基准和真实机器人环境中评估了BackdoorVLA，平均目标成功率为58.4%，在选定的任务中达到100%。我们的工作提供了一个用于评估VLA漏洞的标准框架，并展示了精确对抗操纵的潜力，从而推动了对保护基于VLA的具身系统的进一步研究。

## 🔬 方法详解

**问题定义**：现有视觉-语言-动作（VLA）模型的安全性评估缺乏统一的标准和框架，导致不同攻击方法难以比较。此外，现有攻击方法主要集中于无目标攻击或诱导静态动作，无法实现精确控制VLA执行特定长程动作序列的有目标攻击。真实场景的验证也相对不足。

**核心思路**：AttackVLA的核心思路是构建一个统一的评估框架，涵盖VLA开发的整个生命周期，包括数据构建、模型训练和推理。通过在该框架下实现和评估各种攻击方法，可以更全面地了解VLA模型的脆弱性。针对有目标攻击的不足，提出了BackdoorVLA，通过后门触发机制，实现对VLA行为的精确控制。

**技术框架**：AttackVLA框架包含三个主要阶段：数据构建阶段，用于生成包含对抗样本和后门触发样本的数据集；模型训练阶段，用于训练或微调VLA模型；推理阶段，用于评估各种攻击方法在模拟和真实环境中的效果。BackdoorVLA作为框架内的一种攻击方法，通过在训练数据中插入带有特定触发器的样本，使模型在检测到触发器时执行预定义的动作序列。

**关键创新**：最重要的技术创新点在于BackdoorVLA，它是一种有目标的后门攻击，能够精确控制VLA执行攻击者指定的长程动作序列。与现有方法主要关注无目标攻击或静态动作诱导不同，BackdoorVLA实现了对VLA行为的精细化操纵，从而揭示了VLA模型更深层次的安全风险。

**关键设计**：BackdoorVLA的关键设计包括：1) 选择合适的触发器，使其在真实环境中不易被察觉；2) 设计有效的后门训练策略，确保模型在检测到触发器时能够准确执行目标动作序列；3) 针对不同的VLA架构，调整后门注入方式，以保证攻击的有效性和通用性。损失函数的设计需要平衡正常任务的性能和后门攻击的成功率。

## 📊 实验亮点

AttackVLA框架成功实现了对VLA模型的多种攻击，并揭示了现有攻击方法的局限性。BackdoorVLA在模拟和真实机器人环境中取得了显著的攻击效果，平均目标成功率为58.4%，在特定任务中甚至达到了100%。这些实验结果表明，VLA模型面临着严重的安全威胁，需要进一步研究和开发有效的防御方法。

## 🎯 应用场景

该研究成果可应用于评估和提升各种基于VLA的具身智能系统的安全性，例如服务机器人、自动驾驶汽车和智能家居设备。通过AttackVLA框架，可以系统地识别VLA模型的潜在漏洞，并开发相应的防御机制，从而提高这些系统在真实世界中的可靠性和安全性，避免恶意攻击造成的潜在危害。

## 📄 摘要（原文）

> Vision-Language-Action (VLA) models enable robots to interpret natural-language instructions and perform diverse tasks, yet their integration of perception, language, and control introduces new safety vulnerabilities. Despite growing interest in attacking such models, the effectiveness of existing techniques remains unclear due to the absence of a unified evaluation framework. One major issue is that differences in action tokenizers across VLA architectures hinder reproducibility and fair comparison. More importantly, most existing attacks have not been validated in real-world scenarios. To address these challenges, we propose AttackVLA, a unified framework that aligns with the VLA development lifecycle, covering data construction, model training, and inference. Within this framework, we implement a broad suite of attacks, including all existing attacks targeting VLAs and multiple adapted attacks originally developed for vision-language models, and evaluate them in both simulation and real-world settings. Our analysis of existing attacks reveals a critical gap: current methods tend to induce untargeted failures or static action states, leaving targeted attacks that drive VLAs to perform precise long-horizon action sequences largely unexplored. To fill this gap, we introduce BackdoorVLA, a targeted backdoor attack that compels a VLA to execute an attacker-specified long-horizon action sequence whenever a trigger is present. We evaluate BackdoorVLA in both simulated benchmarks and real-world robotic settings, achieving an average targeted success rate of 58.4% and reaching 100% on selected tasks. Our work provides a standardized framework for evaluating VLA vulnerabilities and demonstrates the potential for precise adversarial manipulation, motivating further research on securing VLA-based embodied systems.

