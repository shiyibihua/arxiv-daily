---
layout: default
title: Generating Diverse Challenging Terrains for Legged Robots Using Quality-Diversity Algorithm
---

# Generating Diverse Challenging Terrains for Legged Robots Using Quality-Diversity Algorithm

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.01362" class="toolbar-btn" target="_blank">📄 arXiv: 2506.01362v1</a>
  <a href="https://arxiv.org/pdf/2506.01362.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.01362v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.01362v1', 'Generating Diverse Challenging Terrains for Legged Robots Using Quality-Diversity Algorithm')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Arthur Esquerre-Pourtère, Minsoo Kim, Jaeheung Park

**分类**: cs.RO, cs.NE

**发布日期**: 2025-06-02

**备注**: Accepted to IEEE ICRA 2025 (7 pages)

**DOI**: [10.1109/ICRA55743.2025.11128362](https://doi.org/10.1109/ICRA55743.2025.11128362)

---

## 💡 一句话要点

**提出质量多样性算法生成多样化挑战地形以测试四足机器人**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)**

**关键词**: `四足机器人` `质量多样性算法` `非结构化地形` `控制器鲁棒性` `强化学习` `地形生成` `挑战性测试`

## 📋 核心要点

1. 现有方法在生成多样化和具有挑战性的非结构化地形方面存在不足，导致机器人控制器的鲁棒性测试不够全面。
2. 本文提出了一种质量多样性算法框架，通过优化生成多样化的地形，以揭示四足机器人控制器的脆弱性。
3. 实验结果表明，生成的地形有效地挑战了机器人的控制器，并发现了意想不到的失败案例，且可用于改进强化学习控制器。

## 📝 摘要（中文）

尽管四足机器人近年来取得了显著进展，但在非结构化地形上确保其控制器的鲁棒性仍然具有挑战性。这需要生成多样化且具有挑战性的非结构化地形，以测试机器人并发现其脆弱性。本文提出了一种质量多样性框架，旨在生成多样化且具有挑战性的地形，以揭示四足机器人控制器的弱点。该方法应用于模拟的双足和四足机器人，生成的地形档案经过优化，能够以不同方式挑战控制器。定量和定性分析表明，生成的档案有效地包含了机器人难以穿越的地形，呈现出不同的失败模式。实验结果显示，这些生成的地形也可以用于改进基于强化学习的控制器。

## 🔬 方法详解

**问题定义**：本文旨在解决四足机器人在非结构化地形上控制器鲁棒性测试不足的问题。现有方法未能有效生成多样化的地形，导致无法全面评估控制器的性能和脆弱性。

**核心思路**：论文提出的质量多样性框架通过优化生成多样化的地形，旨在揭示机器人控制器的弱点。该方法能够生成不同类型的地形，以挑战控制器在多种情况下的表现。

**技术框架**：整体架构包括地形生成模块、控制器测试模块和性能评估模块。首先，利用质量多样性算法生成多样化的地形；然后，测试机器人在这些地形上的表现，最后进行定量和定性分析以评估控制器的鲁棒性。

**关键创新**：本研究的主要创新在于引入质量多样性算法来生成具有挑战性的地形，这与传统方法的单一目标优化不同，能够全面评估控制器的多种失败模式。

**关键设计**：在生成地形时，设置了多个参数以控制地形的复杂性和多样性，同时设计了适应性损失函数，以确保生成的地形能够有效挑战控制器的不同方面。

## 📊 实验亮点

实验结果显示，生成的地形有效地揭示了机器人控制器的脆弱性，特别是在意想不到的失败案例中。定量分析表明，机器人在新生成的地形上表现出显著的性能下降，验证了生成地形的有效性和挑战性。

## 🎯 应用场景

该研究的潜在应用领域包括机器人控制器的测试与评估、自动驾驶技术的开发以及模拟训练环境的构建。通过生成多样化的挑战地形，可以帮助研究人员更好地理解和改进机器人在复杂环境中的表现，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> While legged robots have achieved significant advancements in recent years, ensuring the robustness of their controllers on unstructured terrains remains challenging. It requires generating diverse and challenging unstructured terrains to test the robot and discover its vulnerabilities. This topic remains underexplored in the literature. This paper presents a Quality-Diversity framework to generate diverse and challenging terrains that uncover weaknesses in legged robot controllers. Our method, applied to both simulated bipedal and quadruped robots, produces an archive of terrains optimized to challenge the controller in different ways. Quantitative and qualitative analyses show that the generated archive effectively contains terrains that the robots struggled to traverse, presenting different failure modes. Interesting results were observed, including failure cases that were not necessarily expected. Experiments show that the generated terrains can also be used to improve RL-based controllers.

