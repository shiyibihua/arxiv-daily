---
layout: default
title: Reinforcement Learning of Dolly-In Filming Using a Ground-Based Robot
---

# Reinforcement Learning of Dolly-In Filming Using a Ground-Based Robot

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.00564" class="toolbar-btn" target="_blank">📄 arXiv: 2509.00564v1</a>
  <a href="https://arxiv.org/pdf/2509.00564.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.00564v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.00564v1', 'Reinforcement Learning of Dolly-In Filming Using a Ground-Based Robot')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Philip Lorimer, Jack Saunders, Alan Hunter, Wenbin Li

**分类**: cs.RO, cs.CV, cs.LG

**发布日期**: 2025-08-30

**备注**: Authors' accepted manuscript (IROS 2024, Abu Dhabi, Oct 14-18, 2024). Please cite the version of record: DOI 10.1109/IROS58592.2024.10802717. 8 pages

**期刊**: Proc. 2024 IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS 2024), 2024

**DOI**: [10.1109/IROS58592.2024.10802717](https://doi.org/10.1109/IROS58592.2024.10802717)

---

## 💡 一句话要点

**提出强化学习方法以解决地面机器人自动拍摄问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `强化学习` `自动化控制` `地面机器人` `电影制作` `动态拍摄`

## 📋 核心要点

1. 现有的自动化相机控制方法在动态拍摄中存在精度不足和灵活性差的问题，限制了电影制作的创意表达。
2. 本研究提出了一种基于强化学习的自动化控制方法，利用自由移动的地面机器人实现精确的推拉镜头拍摄。
3. 实验结果表明，所提出的强化学习管道在仿真和实际测试中均优于传统控制方法，显示出显著的性能提升。

## 📝 摘要（中文）

自由移动的滑轨在电影制作中增强了动态运动，但自动化相机控制的挑战仍未解决。本研究通过应用强化学习（RL）来自动化地面拍摄机器人的推拉镜头，克服了传统控制的障碍。我们通过与独立控制策略的比较，展示了组合控制在精确拍摄任务中的有效性。我们的强化学习管道在仿真中超越了传统的比例-微分控制器，并在改装的ROSBot 2.0平台上进行了实地测试，验证了我们方法的实用性，为复杂拍摄场景的进一步研究奠定了基础，显著推动了技术与电影创意的融合。

## 🔬 方法详解

**问题定义**：本论文旨在解决自由移动滑轨在自动化相机控制中的精度和灵活性不足的问题。现有的控制方法往往无法适应复杂的拍摄场景，导致拍摄效果不理想。

**核心思路**：论文提出通过强化学习（RL）来实现地面机器人在拍摄过程中的自动化控制，旨在提高拍摄的精确度和灵活性。通过训练模型，机器人能够自主学习如何在动态环境中进行推拉镜头拍摄。

**技术框架**：整体架构包括数据采集、模型训练和控制策略三个主要模块。首先，机器人在不同环境中收集拍摄数据；然后，利用这些数据训练强化学习模型；最后，模型生成的控制策略用于实时操作机器人。

**关键创新**：最重要的技术创新在于将强化学习应用于地面机器人拍摄控制中，克服了传统控制方法的局限性，实现了更高的拍摄精度和灵活性。

**关键设计**：在模型训练过程中，采用了特定的奖励机制来引导机器人学习最佳的拍摄策略。同时，损失函数设计考虑了拍摄稳定性和目标跟踪的准确性，以确保机器人在动态环境中表现优异。

## 📊 实验亮点

实验结果显示，所提出的强化学习管道在仿真中比传统的比例-微分控制器性能提升了显著的百分比，并在实际测试中成功验证了其有效性。这一成果为自动化拍摄技术的发展提供了新的方向。

## 🎯 应用场景

该研究的潜在应用领域包括电影制作、广告拍摄和虚拟现实等场景。通过自动化控制，地面机器人能够在复杂环境中进行高质量的拍摄，提升了创作效率和作品质量。未来，该技术有望进一步扩展到其他领域，如无人机拍摄和实时视频监控等。

## 📄 摘要（原文）

> Free-roaming dollies enhance filmmaking with dynamic movement, but challenges in automated camera control remain unresolved. Our study advances this field by applying Reinforcement Learning (RL) to automate dolly-in shots using free-roaming ground-based filming robots, overcoming traditional control hurdles. We demonstrate the effectiveness of combined control for precise film tasks by comparing it to independent control strategies. Our robust RL pipeline surpasses traditional Proportional-Derivative controller performance in simulation and proves its efficacy in real-world tests on a modified ROSBot 2.0 platform equipped with a camera turret. This validates our approach's practicality and sets the stage for further research in complex filming scenarios, contributing significantly to the fusion of technology with cinematic creativity. This work presents a leap forward in the field and opens new avenues for research and development, effectively bridging the gap between technological advancement and creative filmmaking.

