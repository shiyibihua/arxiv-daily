---
layout: default
title: Scaling Whole-body Multi-contact Manipulation with Contact Optimization
---

# Scaling Whole-body Multi-contact Manipulation with Contact Optimization

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.12980" class="toolbar-btn" target="_blank">📄 arXiv: 2508.12980v1</a>
  <a href="https://arxiv.org/pdf/2508.12980.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.12980v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.12980v1', 'Scaling Whole-body Multi-contact Manipulation with Contact Optimization')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Victor Levé, João Moura, Sachiya Fujita, Tamon Miyake, Steve Tonneau, Sethu Vijayakumar

**分类**: cs.RO

**发布日期**: 2025-08-18

**备注**: This work has been accepted for publication in IEEE-RAS 24th International Conference on Humanoid Robots (Humanoids 2025). Copyrights to IEEE

**期刊**: 2025 IEEE-RAS 24th International Conference on Humanoid Robots (Humanoids)

**DOI**: [10.1109/Humanoids65713.2025.11203010](https://doi.org/10.1109/Humanoids65713.2025.11203010)

---

## 💡 一句话要点

**提出一种接触优化方法以解决全身多接触操控问题**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)**

**关键词**: `全身操控` `类人机器人` `接触优化` `规划方法` `梯度优化` `机器人技术` `自动化`

## 📋 核心要点

1. 现有的全身操控规划方法主要依赖离散采样，难以处理接触表面的连续性，限制了其扩展性。
2. 本文提出了一种新的接触表面表示方法，结合梯度优化技术，以更有效地解决全身操控任务。
3. 实验结果显示，所提框架在规划时间上比现有最优方法提高了77%，并成功在真实硬件上进行验证。

## 📝 摘要（中文）

日常任务要求我们利用全身来操控物体，尤其是在双手不可用时。本文探讨了赋予类人机器人自主执行类似全身操控任务的能力。现有规划方法主要依赖离散采样，难以应对接触表面的无限可能性。为此，本文提出了一种机器人和物体表面的表示方法，能够实现接触点的闭式计算，并设计了一种有效引导全身操控规划的成本函数。实验结果表明，该框架能够解决现有方法未能解决的问题，并在规划时间上比现有最优方法提升了77%。此外，我们还通过类人机器人对箱子的全身操控验证了该方法在实际硬件上的适用性。

## 🔬 方法详解

**问题定义**：本文旨在解决类人机器人在全身多接触操控任务中的规划效率问题。现有方法因依赖离散采样，无法有效处理接触表面的连续性，导致扩展性不足。

**核心思路**：论文提出了一种新的接触表面表示方法，能够实现接触点的闭式计算，并设计了一种成本函数来有效引导全身操控规划。通过这种方式，能够更好地利用梯度优化技术，提升规划的效率和准确性。

**技术框架**：整体架构包括接触表面表示模块、接触点计算模块和全身操控规划模块。首先，通过新的表示方法计算接触点，然后利用设计的成本函数进行全身操控的优化规划。

**关键创新**：最重要的技术创新在于提出了一种新的接触表面表示方法，能够实现闭式计算，这与现有方法的离散采样本质上不同，从而显著提高了规划效率。

**关键设计**：在成本函数设计上，考虑了接触点的有效性和操控任务的需求，确保优化过程能够引导机器人实现更复杂的操控任务。

## 📊 实验亮点

实验结果表明，所提框架在规划时间上比现有最优方法提升了77%，并成功在真实硬件上实现了类人机器人对箱子的全身操控，验证了其实际应用的有效性。

## 🎯 应用场景

该研究的潜在应用领域包括服务机器人、工业自动化和人机协作等场景。通过提升类人机器人在复杂环境中的操控能力，可以显著提高其在实际任务中的效率和灵活性，推动智能机器人技术的发展。

## 📄 摘要（原文）

> Daily tasks require us to use our whole body to manipulate objects, for instance when our hands are unavailable. We consider the issue of providing humanoid robots with the ability to autonomously perform similar whole-body manipulation tasks. In this context, the infinite possibilities for where and how contact can occur on the robot and object surfaces hinder the scalability of existing planning methods, which predominantly rely on discrete sampling. Given the continuous nature of contact surfaces, gradient-based optimization offers a more suitable approach for finding solutions. However, a key remaining challenge is the lack of an efficient representation of robot surfaces. In this work, we propose (i) a representation of robot and object surfaces that enables closed-form computation of proximity points, and (ii) a cost design that effectively guides whole-body manipulation planning. Our experiments demonstrate that the proposed framework can solve problems unaddressed by existing methods, and achieves a 77% improvement in planning time over the state of the art. We also validate the suitability of our approach on real hardware through the whole-body manipulation of boxes by a humanoid robot.

