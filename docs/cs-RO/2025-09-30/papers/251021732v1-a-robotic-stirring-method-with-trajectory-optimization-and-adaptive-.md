---
layout: default
title: A Robotic Stirring Method with Trajectory Optimization and Adaptive Speed Control for Accurate Pest Counting in Water Traps
---

# A Robotic Stirring Method with Trajectory Optimization and Adaptive Speed Control for Accurate Pest Counting in Water Traps

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.21732" class="toolbar-btn" target="_blank">📄 arXiv: 2510.21732v1</a>
  <a href="https://arxiv.org/pdf/2510.21732.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.21732v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2510.21732v1', 'A Robotic Stirring Method with Trajectory Optimization and Adaptive Speed Control for Accurate Pest Counting in Water Traps')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Xumin Gao, Mark Stevens, Grzegorz Cielniak

**分类**: cs.RO, cs.CV

**发布日期**: 2025-09-30

**备注**: This paper has been submitted to ICRA 2026 and is currently under review

---

## 💡 一句话要点

**提出基于轨迹优化和自适应速度控制的机器人搅拌方法，用于水体陷阱中害虫的精确计数。**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)**

**关键词**: `机器人` `害虫计数` `轨迹优化` `自适应控制` `图像处理` `精准农业` `水体环境` `自动化`

## 📋 核心要点

1. 现有基于图像的害虫计数方法在处理害虫遮挡问题时存在局限性，影响计数准确性。
2. 该论文提出了一种基于机器人手臂的搅拌系统，通过优化搅拌轨迹和自适应速度控制来改善害虫计数。
3. 实验结果验证了该方法的有效性，能够提高在水体陷阱中害虫计数的准确性和置信度。

## 📝 摘要（中文）

为了在精准农业中做出明智的决策，准确监测害虫种群动态至关重要。目前，主流的基于图像的害虫计数方法主要依赖于图像处理结合机器学习或深度学习。然而，这些方法存在局限性，难以处理害虫遮挡的情况。为了解决这个问题，本文提出了一种基于轨迹优化和自适应速度控制的机器人搅拌方法，用于水体陷阱中的精确害虫计数。首先，我们开发了一个基于机器人手臂的自动搅拌系统，用于黄色水体陷阱中的害虫计数。搅拌改变了害虫在黄色水体陷阱中的分布，使一些被遮挡的个体能够被检测和计数。然后，我们研究了不同搅拌轨迹对害虫计数性能的影响，并选择了最佳轨迹。最后，我们提出了一个计数置信度驱动的闭环控制系统，以实现自适应速度搅拌。它使用连续帧之间害虫计数置信度的变化作为反馈来调整搅拌速度。据我们所知，这是第一个致力于研究不同搅拌轨迹对动态液体环境中物体计数的影响，并为这类任务实现自适应速度搅拌的研究。实验结果表明...

## 🔬 方法详解

**问题定义**：论文旨在解决水体陷阱中害虫计数时，由于害虫遮挡导致计数不准确的问题。现有方法依赖图像处理和机器学习，但在高密度或遮挡严重的情况下，计数性能显著下降。因此，需要一种能够有效分散害虫，减少遮挡的自动化计数方法。

**核心思路**：论文的核心思路是通过机器人手臂控制的搅拌动作，改变水体中害虫的分布，从而减少遮挡。通过优化搅拌轨迹，使尽可能多的害虫暴露在视野中，提高计数准确性。同时，采用自适应速度控制，根据计数置信度动态调整搅拌速度，进一步优化计数效果。

**技术框架**：整体框架包含以下几个主要模块：1) 机器人搅拌系统：使用机器人手臂控制搅拌棒在水体陷阱中进行搅拌；2) 轨迹优化模块：设计并比较不同的搅拌轨迹（圆形、方形、三角形、螺旋形、四个小圆、随机线），选择最优轨迹；3) 自适应速度控制模块：基于连续帧之间害虫计数置信度的变化，调整搅拌速度；4) 图像采集与处理模块：采集水体陷阱的图像，并进行害虫检测与计数。

**关键创新**：该研究的关键创新在于：1) 首次系统性地研究了不同搅拌轨迹对动态液体环境中物体计数的影响；2) 提出了基于计数置信度的自适应速度控制方法，实现了闭环优化；3) 将机器人技术应用于农业害虫监测，为自动化害虫计数提供了一种新的解决方案。

**关键设计**：轨迹优化中，通过比较不同轨迹下的平均计数误差和计数置信度来选择最优轨迹。自适应速度控制中，使用计数置信度的变化率作为反馈信号，控制搅拌速度。具体的控制算法和参数设置在论文中未详细描述，属于未知信息。

## 📊 实验亮点

论文通过实验验证了所提出的机器人搅拌方法的有效性。结果表明，优化的搅拌轨迹能够显著提高害虫计数的准确性和置信度。自适应速度控制进一步提升了计数性能，尤其是在害虫密度较高的情况下。具体的性能提升数据在摘要中未给出，属于未知信息。

## 🎯 应用场景

该研究成果可应用于精准农业中的害虫监测，帮助农民更准确地了解害虫种群动态，从而制定更有效的防治策略，减少农药使用，提高农作物产量和质量。此外，该方法也可推广到其他水体环境中的物体计数，例如水质监测中的微生物计数等，具有广泛的应用前景。

## 📄 摘要（原文）

> Accurate monitoring of pest population dynamics is crucial for informed decision-making in precision agriculture. Currently, mainstream image-based pest counting methods primarily rely on image processing combined with machine learning or deep learning for pest counting. However, these methods have limitations and struggle to handle situations involving pest occlusion. To address this issue, this paper proposed a robotic stirring method with trajectory optimization and adaptive speed control for accurate pest counting in water traps. First, we developed an automated stirring system for pest counting in yellow water traps based on a robotic arm. Stirring alters the distribution of pests in the yellow water trap, making some of the occluded individuals visible for detection and counting. Then, we investigated the impact of different stirring trajectories on pest counting performance and selected the optimal trajectory for pest counting. Specifically, we designed six representative stirring trajectories, including circle, square, triangle, spiral, four small circles, and random lines, for the robotic arm to stir. And by comparing the overall average counting error and counting confidence of different stirring trajectories across various pest density scenarios, we determined the optimal trajectory. Finally, we proposed a counting confidence-driven closed-loop control system to achieve adaptive-speed stirring. It uses changes in pest counting confidence between consecutive frames as feedback to adjust the stirring speed. To the best of our knowledge, this is the first study dedicated to investigating the effects of different stirring trajectories on object counting in the dynamic liquid environment and to implement adaptive-speed stirring for this type of task. Experimental results show ...

