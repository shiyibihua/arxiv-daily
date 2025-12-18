---
layout: default
title: Anomaly detection for generic failure monitoring in robotic assembly, screwing and manipulation
---

# Anomaly detection for generic failure monitoring in robotic assembly, screwing and manipulation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.26308" class="toolbar-btn" target="_blank">📄 arXiv: 2509.26308v1</a>
  <a href="https://arxiv.org/pdf/2509.26308.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.26308v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.26308v1', 'Anomaly detection for generic failure monitoring in robotic assembly, screwing and manipulation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Niklas Grambow, Lisa-Marie Fenner, Felipe Kempkes, Philip Hotz, Dingyuan Wan, Jörg Krüger, Kevin Haninger

**分类**: cs.RO

**发布日期**: 2025-09-30

---

## 💡 一句话要点

**提出基于自编码器的异常检测方法，用于机器人装配、拧螺丝和操作中的通用故障监控。**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `机器人异常检测` `自编码器` `时间序列分析` `故障监控` `机器人操作`

## 📋 核心要点

1. 现有机器人异常检测方法缺乏跨任务和控制策略的通用性，限制了其在复杂工业场景中的应用。
2. 利用机器人与环境交互的时间序列数据，结合自编码器进行异常检测，无需针对特定任务进行精细调整。
3. 在机器人布线、拧螺丝和打磨任务中验证了该方法的有效性，AUROC在部分任务中超过0.93。

## 📝 摘要（中文）

机器人操作中超出分布的状态通常会导致不可预测的行为或任务失败，降低成功率并增加损坏风险。异常检测(AD)可以识别数据中与预期模式的偏差，用于触发安全行为和恢复策略。本文利用力/扭矩信号等时间序列数据，直接捕捉机器人与环境的交互，这对于操作和在线故障检测至关重要。研究在机器人布线、拧螺丝和打磨三个工业任务中构建了测试场景，并收集了多模态时间序列数据。比较了几种基于自编码器的方法，评估了它们在任务和控制方法（扩散策略、位置和阻抗控制）之间的泛化能力。结果表明，在布线和拧螺丝任务中，对于不正确或未对准的零件以及受阻目标等故障，AUROC超过0.93，实现了可靠的检测。在抛光任务中，只有严重的故障被可靠地检测到，而更细微的故障类型仍然未被检测到。

## 🔬 方法详解

**问题定义**：论文旨在解决机器人操作过程中，由于超出预期状态导致的故障检测问题。现有方法通常针对特定任务设计，缺乏通用性和泛化能力，难以适应复杂多变的工业环境。此外，现有方法对数据效率和检测延迟的要求较高，限制了其在实际应用中的可行性。

**核心思路**：论文的核心思路是利用机器人与环境交互过程中产生的力/扭矩等时间序列数据，通过学习正常操作模式的特征表示，从而检测出与正常模式的偏差。自编码器能够有效地学习数据的低维表示，并重建输入数据，因此可以用于异常检测。当输入数据与重建数据之间的差异较大时，则认为发生了异常。

**技术框架**：整体框架包括数据采集、数据预处理、模型训练和异常检测四个主要阶段。首先，通过传感器采集机器人操作过程中的力/扭矩等时间序列数据。然后，对数据进行预处理，例如归一化和滤波。接着，使用预处理后的数据训练自编码器模型，学习正常操作模式的特征表示。最后，在实际操作过程中，使用训练好的模型对新的数据进行重建，并计算重建误差，根据设定的阈值判断是否发生异常。

**关键创新**：论文的关键创新在于提出了一种通用的基于自编码器的异常检测方法，该方法可以应用于不同的机器人任务和控制策略，无需针对特定任务进行精细调整。此外，论文还评估了不同自编码器模型在机器人异常检测任务中的性能，并分析了影响检测效果的因素。

**关键设计**：论文比较了多种自编码器结构，包括标准自编码器、变分自编码器和对抗自编码器。损失函数采用均方误差（MSE）作为重建误差的度量。为了提高检测的鲁棒性，论文还采用了滑动窗口技术，将时间序列数据分割成多个窗口，并对每个窗口进行异常检测。异常阈值的设定通常基于训练数据的重建误差分布，例如设定为训练数据重建误差的某个百分位数。

## 📊 实验亮点

实验结果表明，该方法在机器人布线和拧螺丝任务中取得了良好的检测效果，AUROC超过0.93。通过对比不同自编码器模型，发现变分自编码器和对抗自编码器在某些任务中表现更好。此外，实验还分析了数据效率、检测延迟和任务特性对检测效果的影响，为实际应用提供了指导。

## 🎯 应用场景

该研究成果可应用于各种工业机器人应用场景，例如自动化装配、精密加工、质量检测等。通过实时监测机器人与环境的交互数据，及时发现潜在的故障和异常，可以有效提高生产效率、降低生产成本、保障产品质量，并减少机器人损坏的风险。该技术还有潜力应用于其他类型的时序数据异常检测，例如金融欺诈检测、网络安全监控等。

## 📄 摘要（原文）

> Out-of-distribution states in robot manipulation often lead to unpredictable robot behavior or task failure, limiting success rates and increasing risk of damage. Anomaly detection (AD) can identify deviations from expected patterns in data, which can be used to trigger failsafe behaviors and recovery strategies. Prior work has applied data-driven AD to time series data in specific robotic tasks, but its transferability across control strategies and task types has not been shown. Leveraging time series data, such as force/torque signals, allows to directly capture robot-environment interactions, crucial for manipulation and online failure detection. Their broad availability, high sampling rates, and low dimensionality enable high temporal resolution and efficient processing. As robotic tasks can have widely signal characteristics and requirements, AD methods which can be applied in the same way to a wide range of tasks is needed, ideally with good data efficiency. We examine three industrial robotic tasks, each presenting several anomalies. Test scenarios in robotic cabling, screwing, and sanding are built, and multimodal time series data is gathered. Several autoencoder-based methods are compared, evaluating generalization across tasks and control methods (diffusion policy, position, and impedance control). This allows us to validate the integration of AD in complex tasks involving tighter tolerances and variation from both the robot and its environment. Additionally, we evaluate data efficiency, detection latency, and task characteristics which support robust detection. The results indicate reliable detection with AUROC exceeding 0.93 in failures in the cabling and screwing task, such as incorrect or misaligned parts and obstructed targets. In the polishing task, only severe failures were reliably detected, while more subtle failure types remained undetected.

