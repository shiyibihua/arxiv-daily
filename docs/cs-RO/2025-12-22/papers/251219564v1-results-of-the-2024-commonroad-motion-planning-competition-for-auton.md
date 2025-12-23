---
layout: default
title: Results of the 2024 CommonRoad Motion Planning Competition for Autonomous Vehicles
---

# Results of the 2024 CommonRoad Motion Planning Competition for Autonomous Vehicles

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.19564" class="toolbar-btn" target="_blank">📄 arXiv: 2512.19564v1</a>
  <a href="https://arxiv.org/pdf/2512.19564.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.19564v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.19564v1', 'Results of the 2024 CommonRoad Motion Planning Competition for Autonomous Vehicles')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yanliang Huang, Xia Yan, Peiran Yin, Zhenduo Zhang, Zeyan Shao, Youran Wang, Haoliang Huang, Matthias Althoff

**分类**: cs.RO, cs.AI

**发布日期**: 2025-12-22

---

## 💡 一句话要点

**CommonRoad自动驾驶运动规划竞赛：标准化评估复杂交通场景下的规划算法**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)**

**关键词**: `自动驾驶` `运动规划` `基准测试` `CommonRoad` `竞赛`

## 📋 核心要点

1. 现有自动驾驶运动规划算法缺乏在标准化基准上的比较，难以评估其优劣。
2. 论文通过CommonRoad运动规划竞赛，提供开源可复现的基准测试框架。
3. 竞赛在复杂交通场景中评估规划器的效率、安全、舒适和合规性。

## 📝 摘要（中文）

过去十年，自动驾驶车辆的运动规划方法得到了广泛发展，以应对日益复杂的交通场景。然而，这些方法很少在标准化的基准上进行比较，这限制了对相对优势和劣势的评估。为了解决这个问题，我们介绍了2024年举行的第四届CommonRoad运动规划竞赛的设置和结果，该竞赛使用CommonRoad基准套件进行。这项年度竞赛为运动规划算法的基准测试提供了一个开源和可复现的框架。基准场景涵盖高速公路和城市环境，包含各种交通参与者，包括乘用车、公共汽车和自行车。规划器的性能从四个维度进行评估：效率、安全性、舒适性和对选定交通规则的遵守情况。本报告介绍了比赛形式，并对2023年和2024年版本中具有代表性的高性能规划器进行了比较。

## 🔬 方法详解

**问题定义**：论文旨在解决自动驾驶运动规划算法缺乏标准化评估的问题。现有方法难以在统一的基准上进行比较，导致难以客观评估不同算法的优劣，阻碍了该领域的发展。现有方法在面对复杂交通场景时，其性能表现的差异性无法有效量化。

**核心思路**：论文的核心思路是通过组织年度CommonRoad运动规划竞赛，创建一个开源、可复现的基准测试平台。该平台提供了一系列具有挑战性的交通场景，并定义了明确的评估指标，从而为不同运动规划算法提供公平的比较环境。通过竞赛的方式，促进算法的迭代和优化。

**技术框架**：整体框架包括以下几个主要阶段：1) 定义CommonRoad基准场景，涵盖高速公路和城市环境，包含多种交通参与者；2) 制定评估指标，包括效率、安全性、舒适性和交通规则合规性；3) 组织竞赛，邀请研究团队提交其运动规划算法；4) 在CommonRoad平台上运行算法，并根据评估指标进行排名；5) 发布竞赛结果和算法分析报告。

**关键创新**：该研究的关键创新在于构建了一个开源、可复现的自动驾驶运动规划算法基准测试平台。该平台不仅提供了标准化的测试场景和评估指标，还通过竞赛的形式，激发了研究人员的创新热情，促进了该领域的发展。与以往的研究相比，该研究更注重实际应用和算法的公平比较。

**关键设计**：关键设计包括：1) CommonRoad场景的设计，需要覆盖各种复杂交通情况；2) 评估指标的选取，需要能够全面反映算法的性能；3) 竞赛规则的制定，需要保证公平性和激励性；4) 平台的可扩展性，需要能够支持未来的算法和场景。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.19564v1/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.19564v1/x2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.19564v1/figures/coverage_pie.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

2024年CommonRoad运动规划竞赛对来自2023年和2024年的高性能规划器进行了比较，结果表明，在效率、安全、舒适性和合规性等多个维度上，不同算法的表现存在显著差异。具体的性能数据和提升幅度需要在竞赛报告中查看，但总体而言，该竞赛为评估和改进自动驾驶运动规划算法提供了有价值的参考。

## 🎯 应用场景

该研究成果可应用于自动驾驶系统的开发与测试，帮助开发者选择和优化运动规划算法。此外，该平台也可用于自动驾驶安全性的评估和验证，为自动驾驶汽车的商业化部署提供技术支持。未来，该平台可以扩展到更多类型的自动驾驶场景，例如无人配送、自动泊车等。

## 📄 摘要（原文）

> Over the past decade, a wide range of motion planning approaches for autonomous vehicles has been developed to handle increasingly complex traffic scenarios. However, these approaches are rarely compared on standardized benchmarks, limiting the assessment of relative strengths and weaknesses. To address this gap, we present the setup and results of the 4th CommonRoad Motion Planning Competition held in 2024, conducted using the CommonRoad benchmark suite. This annual competition provides an open-source and reproducible framework for benchmarking motion planning algorithms. The benchmark scenarios span highway and urban environments with diverse traffic participants, including passenger cars, buses, and bicycles. Planner performance is evaluated along four dimensions: efficiency, safety, comfort, and compliance with selected traffic rules. This report introduces the competition format and provides a comparison of representative high-performing planners from the 2023 and 2024 editions.

