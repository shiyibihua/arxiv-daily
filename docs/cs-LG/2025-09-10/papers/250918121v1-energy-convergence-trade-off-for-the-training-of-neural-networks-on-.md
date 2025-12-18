---
layout: default
title: Energy-convergence trade off for the training of neural networks on bio-inspired hardware
---

# Energy-convergence trade off for the training of neural networks on bio-inspired hardware

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.18121" class="toolbar-btn" target="_blank">📄 arXiv: 2509.18121v1</a>
  <a href="https://arxiv.org/pdf/2509.18121.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.18121v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.18121v1', 'Energy-convergence trade off for the training of neural networks on bio-inspired hardware')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Nikhil Garg, Paul Uriarte Vicandi, Yanming Zhang, Alexandre Baigol, Donato Francesco Falcone, Saketh Ram Mamidala, Bert Jan Offrein, Laura Bégon-Lours

**分类**: cs.ET, cs.LG

**发布日期**: 2025-09-10

---

## 💡 一句话要点

**提出能量收敛权衡方法以优化神经网络训练**

🎯 **匹配领域**: **支柱八：物理动画 (Physics-based Animation)**

**关键词**: `神经网络训练` `忆阻器` `能效优化` `边缘计算` `铁电突触` `短脉冲编程` `硬件感知`

## 📋 核心要点

1. 现有方法在极限边缘计算中面临能效与性能之间的权衡挑战，尤其是在神经网络训练时。
2. 论文提出了一种基于铁电突触器件的训练方法，通过短脉冲编程与定制训练来优化能量使用与准确性。
3. 实验结果显示，短脉冲编程结合定制训练显著提高了学习效率，减少了总能量消耗，同时保持了较高的分类准确性。

## 📝 摘要（中文）

随着可穿戴传感器和植入设备的广泛应用，人工智能处理需求逐渐向极限边缘转移，迫切需要超低功耗以实现持续运行。受大脑启发的新兴忆阻器设备有望通过消除计算与存储之间的昂贵数据传输来加速神经网络训练。然而，性能与能效之间的平衡仍然是一个挑战。本文研究了基于HfO2/ZrO2超晶格的铁电突触器件，并将实验测得的权重更新输入到硬件感知的神经网络模拟中。研究发现，较短的脉冲宽度虽然降低了每次更新的能量，但需要更多的训练周期，仍能在不牺牲准确度的前提下减少总能量。通过分析原因，提出了“对称点转移”技术，以解决不对称更新问题并恢复准确性。这些结果突显了准确性、收敛速度和能量使用之间的权衡，表明短脉冲编程与定制训练显著提升了片上学习效率。

## 🔬 方法详解

**问题定义**：本文旨在解决在极限边缘计算中神经网络训练的能效与性能之间的平衡问题。现有方法在能量消耗和训练效率上存在不足，尤其是在使用传统计算架构时，数据传输成本高昂。

**核心思路**：论文的核心思路是利用基于HfO2/ZrO2超晶格的铁电突触器件，通过短脉冲编程来降低每次更新的能量消耗，同时结合定制的训练策略来提高收敛速度和准确性。

**技术框架**：整体架构包括实验测量的权重更新输入到硬件感知的神经网络模拟中，采用不同脉冲宽度进行训练，评估能量消耗与分类准确性之间的关系。主要模块包括突触器件的设计、权重更新的实验测量和神经网络的训练模拟。

**关键创新**：最重要的技术创新在于提出了“对称点转移”技术，解决了不对称更新导致的准确性下降问题。这一方法与传统的训练方法相比，能够更有效地利用硬件特性。

**关键设计**：在实验中，脉冲宽度从20 ns到0.2 ms不等，较短的脉冲降低了每次更新的能量，但需要更多的训练周期。采用混合精度的随机梯度下降（SGD）方法来优化训练过程，并通过调整损失函数和网络结构来提高准确性。

## 📊 实验亮点

实验结果表明，采用短脉冲编程与定制训练的结合，能够在不牺牲分类准确性的情况下，显著降低总能量消耗。具体而言，短脉冲编程使得每次更新的能量降低，同时提高了学习效率，展示了在极限边缘计算中的应用潜力。

## 🎯 应用场景

该研究的潜在应用领域包括可穿戴设备、植入式医疗设备和其他需要高效能量管理的边缘计算场景。通过优化神经网络训练过程，可以实现更长的设备续航时间和更高的实时处理能力，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> The increasing deployment of wearable sensors and implantable devices is shifting AI processing demands to the extreme edge, necessitating ultra-low power for continuous operation. Inspired by the brain, emerging memristive devices promise to accelerate neural network training by eliminating costly data transfers between compute and memory. Though, balancing performance and energy efficiency remains a challenge. We investigate ferroelectric synaptic devices based on HfO2/ZrO2 superlattices and feed their experimentally measured weight updates into hardware-aware neural network simulations. Across pulse widths from 20 ns to 0.2 ms, shorter pulses lower per-update energy but require more training epochs while still reducing total energy without sacrificing accuracy. Classification accuracy using plain stochastic gradient descent (SGD) is diminished compared to mixed-precision SGD. We analyze the causes and propose a ``symmetry point shifting'' technique, addressing asymmetric updates and restoring accuracy. These results highlight a trade-off among accuracy, convergence speed, and energy use, showing that short-pulse programming with tailored training significantly enhances on-chip learning efficiency.

