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

**对比经济与能量模型预测控制，优化冷库储能系统运行**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)**

**关键词**: `模型预测控制` `经济优化` `能量优化` `冷库储能` `冷却装置`

## 📋 核心要点

1. 传统多冷却器冷却装置的单元负荷和分配问题主要依赖经济模型预测控制，但鲜有研究关注能量优化。
2. 本文提出对比经济和能量两种优化目标，旨在评估在冷库冷却装置中采用能量优化策略的可行性。
3. 实验结果表明，在高用电季节，经济优化虽然降低了成本，但会导致能耗显著增加，突显了能量优化的价值。

## 📝 摘要（中文）

本文首次对比了能量优化目标和经济优化目标在冷库冷却装置中的应用。经济模型预测控制通过最小化时间范围内的电力消耗成本来解决多冷却器冷却装置的单元负荷和单元分配问题。研究在包含风冷式冷水机组和冷存储系统的冷却装置上进行了对比实验。模型集成到Simscape中，并使用非凸混合优化方法分别实现了能量和经济目标下的最优控制轨迹。结果表明，在不同场景和季节下，能量优化方法值得考虑，尽管目前经济优化方法更为普遍。结果依赖于用电季节和可用电价。在高用电季节和代表性电价下，与能量优化方法相比，经济优化方法会导致能耗增加约2.15%，但成本降低2.94%。

## 🔬 方法详解

**问题定义**：论文旨在解决冷库冷却装置的运行优化问题，具体而言，是在满足制冷需求的前提下，如何选择冷却器的运行状态和冷存储系统的充放电策略，以最小化能源消耗或运行成本。现有方法主要侧重于经济优化，即最小化电费支出，但忽略了能源效率，可能导致总体能耗增加。

**核心思路**：论文的核心思路是对比经济模型预测控制（EMPC）和能量模型预测控制（EnMPC）两种策略，评估它们在不同季节和电价下的性能差异。EMPC以最小化电费为目标，而EnMPC以最小化能耗为目标。通过对比两种策略的运行结果，揭示经济优化可能带来的能源浪费，并为实际应用提供决策依据。

**技术框架**：论文构建了一个冷库冷却装置的Simscape模型，该模型包括风冷式冷水机组和冷存储系统。然后，分别针对EMPC和EnMPC设计了模型预测控制器。控制器通过预测未来一段时间内的系统状态，并根据优化目标（电费或能耗）选择最优的控制策略。优化问题采用非凸混合优化方法求解。

**关键创新**：论文的主要创新在于首次在冷库冷却装置的控制中对比了经济优化和能量优化两种目标。以往的研究主要集中在经济优化上，而忽略了能源效率。通过对比实验，论文揭示了经济优化可能导致能源浪费，并为实际应用提供了新的视角。

**关键设计**：论文的关键设计包括：1) 精确的冷库冷却装置Simscape模型，能够准确模拟系统的动态特性；2) 基于模型预测控制的优化框架，能够根据预测信息选择最优控制策略；3) 非凸混合优化方法的应用，能够有效求解复杂的优化问题；4) 针对不同季节和电价的实验设计，能够全面评估两种控制策略的性能。

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

实验结果表明，在高用电季节和代表性电价下，使用经济模型预测控制（EMPC）代替能量模型预测控制（EnMPC）会导致能耗增加约2.15%，但成本降低2.94%。这表明在电价较高的时段，经济优化策略可能会牺牲能源效率以降低运行成本。该结果突出了在不同运行条件下选择合适控制策略的重要性。

## 🎯 应用场景

该研究成果可应用于各种需要冷量供应的场景，例如大型商场、数据中心、工业生产等。通过选择合适的控制策略，可以在保证制冷效果的同时，降低能源消耗和运行成本，提高能源利用效率，具有重要的经济和社会价值。未来的研究可以进一步探索更加智能化的控制策略，例如结合人工智能算法，实现自适应的能源优化。

## 📄 摘要（原文）

> Economic model predictive control has been proposed as a means for solving the unit loading and unit allocation problem in multi-chiller cooling plants. The adjective economic stems from the use of financial cost due to electricity consumption in a time horizon, such is the loss function minimized at each sampling period. The energetic approach is rarely encountered. This article presents for the first time a comparison between the energetic optimization objective and the economic one. The comparison is made on a cooling plant using air-cooled water chillers and a cold storage system. Models developed have been integrated into Simscape, and non-convex mixed optimization methods used to achieve optimal control trajectories for both energetic and economic goals considered separately. The results over several scenarios, and in different seasons, support the consideration of the energetic approach despite the current prevalence of the economic one. The results are dependent on the electric season and the available tariffs. In particular, for the high electric season and considering a representative tariff, the results show that an increment of about 2.15% in energy consumption takes place when using the economic approach instead of the energetic one. On the other hand, a reduction in cost of 2.94% is achieved.

