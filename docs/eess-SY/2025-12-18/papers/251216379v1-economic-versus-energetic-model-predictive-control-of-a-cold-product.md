---
layout: default
title: Economic versus energetic model predictive control of a cold production plant with thermal energy storage
---

# Economic versus energetic model predictive control of a cold production plant with thermal energy storage

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.16379" class="toolbar-btn" target="_blank">📄 arXiv: 2512.16379v1</a>
  <a href="https://arxiv.org/pdf/2512.16379.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.16379v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.16379v1', 'Economic versus energetic model predictive control of a cold production plant with thermal energy storage')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Manuel G. Satué, Manuel R. Arahal, Luis F. Acedo, Manuel G. Ortega

**分类**: eess.SY

**发布日期**: 2025-12-18

**备注**: 14 pages

**期刊**: Applied Thermal Engineering 210 (2022) 118309

**DOI**: [10.1016/j.applthermaleng.2022.118309](https://doi.org/10.1016/j.applthermaleng.2022.118309)

---

## 💡 一句话要点

**对比经济与能量型模型预测控制，优化冷库生产能耗与成本**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)**

**关键词**: `模型预测控制` `经济优化` `能量优化` `冷库生产` `热能存储`

## 📋 核心要点

1. 多冷水机组冷却工厂面临机组负荷分配问题，经济型模型预测控制通过最小化电费来解决此问题，但鲜有研究关注能量优化。
2. 本文提出对比能量优化和经济优化两种目标，旨在评估在冷库生产中，哪种方法在不同条件下更具优势。
3. 实验结果表明，在用电高峰期，经济优化虽然降低了成本，但会导致能耗显著增加，因此能量优化在特定情况下更优。

## 📝 摘要（中文）

本文首次对比了能量优化目标和经济优化目标在冷库生产中的应用。研究对象为一个使用风冷式冷水机组和冷能存储系统的冷却工厂。论文将开发的模型集成到Simscape中，并使用非凸混合优化方法，分别针对能量和经济目标实现了最优控制轨迹。在不同场景和季节下的结果表明，尽管目前经济优化方法更为普遍，但能量优化方法也值得考虑。结果依赖于用电季节和可用的电价。特别是在用电高峰期，使用经济优化方法代替能量优化方法会导致能耗增加约2.15%，但成本降低2.94%。

## 🔬 方法详解

**问题定义**：论文旨在解决多冷水机组冷却工厂的单元负荷和单元分配问题，即如何控制冷水机组和冷能存储系统，以满足冷却需求的同时，最小化能源消耗或运行成本。现有方法主要集中于经济型模型预测控制，通过最小化电费来优化运行，但忽略了能源消耗本身，可能导致能源浪费。

**核心思路**：论文的核心思路是对比经济型模型预测控制（Economic MPC）和能量型模型预测控制（Energetic MPC）在冷却工厂中的性能。经济型MPC以最小化电费为目标，而能量型MPC以最小化能源消耗为目标。通过对比两种方法在不同场景和季节下的表现，评估其优缺点，从而为实际应用提供指导。

**技术框架**：该研究的技术框架主要包括以下几个部分：1) 建立冷却工厂的Simscape模型，包括冷水机组、冷能存储系统等组件；2) 设计经济型和能量型模型预测控制器，分别以最小化电费和能源消耗为目标；3) 使用非凸混合优化方法求解最优控制轨迹；4) 在不同场景和季节下进行仿真实验，对比两种控制器的性能。

**关键创新**：论文的关键创新在于首次在冷库生产领域对比了经济型和能量型模型预测控制的性能。以往的研究主要集中于经济型MPC，而忽略了能量优化。通过对比研究，论文揭示了在特定条件下，能量型MPC可能比经济型MPC更优，从而为冷却工厂的优化运行提供了新的思路。

**关键设计**：在模型预测控制器的设计中，关键的技术细节包括：1) 建立准确的冷却工厂模型，包括冷水机组的能耗模型、冷能存储系统的充放电模型等；2) 选择合适的优化算法，由于问题是非凸的，需要使用非凸混合优化方法；3) 设计合理的成本函数，经济型MPC的成本函数为电费，能量型MPC的成本函数为能源消耗；4) 根据实际情况设置约束条件，如冷水机组的运行范围、冷能存储系统的容量等。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16379v1/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16379v1/x2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16379v1/x3.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

实验结果表明，在用电高峰期，使用经济型MPC代替能量型MPC会导致能耗增加约2.15%，但成本降低2.94%。这表明在电价较高时，经济型MPC可以通过牺牲少量能耗来显著降低成本。然而，在其他季节或电价较低时，能量型MPC可能更具优势。因此，在实际应用中需要根据具体情况选择合适的控制策略。

## 🎯 应用场景

该研究成果可应用于各种需要冷却系统的工业和商业建筑，例如数据中心、医院、购物中心等。通过选择合适的控制策略，可以在满足冷却需求的同时，降低能源消耗和运行成本，提高能源利用效率，并减少对环境的影响。未来的研究可以进一步探索更复杂的冷却系统和控制策略，例如考虑可再生能源的利用、需求侧响应等。

## 📄 摘要（原文）

> Economic model predictive control has been proposed as a means for solving the unit loading and unit allocation problem in multi-chiller cooling plants. The adjective economic stems from the use of financial cost due to electricity consumption in a time horizon, such is the loss function minimized at each sampling period. The energetic approach is rarely encountered. This article presents for the first time a comparison between the energetic optimization objective and the economic one. The comparison is made on a cooling plant using air-cooled water chillers and a cold storage system. Models developed have been integrated into Simscape, and non-convex mixed optimization methods used to achieve optimal control trajectories for both energetic and economic goals considered separately. The results over several scenarios, and in different seasons, support the consideration of the energetic approach despite the current prevalence of the economic one. The results are dependent on the electric season and the available tariffs. In particular, for the high electric season and considering a representative tariff, the results show that an increment of about 2.15% in energy consumption takes place when using the economic approach instead of the energetic one. On the other hand, a reduction in cost of 2.94% is achieved.

