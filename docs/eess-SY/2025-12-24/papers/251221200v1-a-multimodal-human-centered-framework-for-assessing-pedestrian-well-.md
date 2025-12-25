---
layout: default
title: A Multimodal Human-Centered Framework for Assessing Pedestrian Well-Being in the Wild
---

# A Multimodal Human-Centered Framework for Assessing Pedestrian Well-Being in the Wild

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.21200" class="toolbar-btn" target="_blank">📄 arXiv: 2512.21200v1</a>
  <a href="https://arxiv.org/pdf/2512.21200.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.21200v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.21200v1', 'A Multimodal Human-Centered Framework for Assessing Pedestrian Well-Being in the Wild')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yasaman Hakiminejad, Arash Tavakoli

**分类**: eess.SY

**发布日期**: 2025-12-24

---

## 💡 一句话要点

**提出多模态行人福祉评估框架，用于城市可持续发展和宜居性设计。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `行人福祉` `多模态数据融合` `体验抽样法` `生理传感` `城市规划` `可持续交通` `以人为本的城市分析`

## 📋 核心要点

1. 现有行人环境评估方法忽略了步行体验的动态、主观和心理生理维度。
2. 提出多模态框架，整合生理传感、地理空间跟踪和体验抽样自我报告。
3. 案例研究表明，主观体验和生理反应存在显著差异，且与环境因素相关。

## 📝 摘要（中文）

行人福祉是可持续城市交通和宜居城市设计中一个关键但很少被衡量的组成部分。现有的行人环境评估方法通常依赖于静态的、基于基础设施的指标或回顾性调查，忽略了日常步行体验的动态、主观和心理生理维度。本文介绍了一种多模态、以人为中心的框架，用于评估“野外”的行人福祉，通过整合三个互补的数据流：连续生理传感、地理空间跟踪和使用体验抽样法收集的即时自我报告。该框架将行人体验概念化为一种三角测量，从而能够全面了解城市环境如何影响福祉。通过在大费城地区进行的自然案例研究，证明了我们框架的实用性，参与者在日常活动中佩戴研究级可穿戴传感器并携带支持GPS的智能手机。自主神经系统活动的生理指标，包括心率变异性和皮肤电活动，与空间轨迹和压力、情感和感知基础设施条件的现场自我报告同步。结果表明，主观体验和生理反应存在显着的个体间和个体内部差异，以及与交通暴露、行人基础设施质量和环境封闭相关的上下文相关模式。研究结果还表明，常用的步行性指数可能无法完全捕捉行人福祉的体验维度。通过实现对行人体验的真实世界、多模态测量，所提出的框架为推进以人为中心的城市分析提供了一种可扩展和可转移的方法。

## 🔬 方法详解

**问题定义**：现有评估行人福祉的方法，如基于基础设施的指标或回顾性调查，无法捕捉行人步行体验的动态性、主观性和生理心理维度。这些方法缺乏对行人实时状态和环境影响的细粒度理解，难以有效指导城市规划和设计，提升行人福祉。

**核心思路**：论文的核心思路是将行人福祉的评估从静态、回顾性方法转变为动态、实时的多模态数据融合。通过同时收集行人的生理数据、地理位置信息和主观体验报告，构建一个全面的行人体验模型。这种方法能够更准确地反映城市环境对行人福祉的实际影响。

**技术框架**：该框架包含三个主要模块：1) **生理传感模块**：使用可穿戴传感器（如心率变异性传感器和皮肤电活动传感器）连续监测行人的生理指标，反映其自主神经系统的活动状态。2) **地理空间跟踪模块**：利用GPS设备记录行人的空间轨迹，确定其所处的城市环境和基础设施条件。3) **体验抽样模块**：通过智能手机应用，在行人步行过程中随机触发问卷调查，收集其对压力、情感和感知基础设施条件的主观报告。这三个模块的数据进行时间同步和整合，形成一个多维度的行人体验数据集。

**关键创新**：该框架的关键创新在于其多模态数据融合方法和“野外”数据收集策略。传统的行人福祉评估方法通常依赖于实验室环境或模拟场景，而该框架能够在真实的城市环境中收集数据，更贴近行人的实际体验。此外，通过整合生理、空间和主观数据，该框架能够更全面地理解城市环境对行人福祉的影响机制。

**关键设计**：在案例研究中，参与者佩戴研究级可穿戴传感器并携带支持GPS的智能手机。生理数据以高频率（例如，心率变异性数据以1Hz采样）记录，以捕捉细微的生理变化。体验抽样调查采用随机触发机制，避免对行人的干扰。数据同步采用精确的时间戳，确保不同模态数据的一致性。研究人员还设计了专门的问卷，用于收集行人对压力、情感和感知基础设施条件的主观评价。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.21200v1/triangular.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.21200v1/Framework.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.21200v1/map.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

研究结果表明，行人的主观体验和生理反应存在显著的个体间和个体内部差异。例如，交通暴露、行人基础设施质量和环境封闭等因素与行人的压力水平和情感状态密切相关。此外，研究发现常用的步行性指数可能无法完全捕捉行人福祉的体验维度，表明需要更全面、多维度的评估方法。

## 🎯 应用场景

该研究成果可应用于城市规划、交通管理和公共健康等领域。通过实时监测和评估行人福祉，城市规划者可以优化城市设计，改善行人基础设施，提升城市宜居性。交通管理者可以评估交通流量和拥堵对行人福祉的影响，制定更合理的交通管理策略。公共健康机构可以利用该框架评估城市环境对居民心理健康的影响，制定相应的干预措施。

## 📄 摘要（原文）

> Pedestrian well-being is a critical yet rarely measured component of sustainable urban mobility and livable city design. Existing approaches to evaluating pedestrian environments often rely on static, infrastructure-based indices or retrospective surveys, which overlook the dynamic, subjective, and psychophysiological dimensions of everyday walking experience. This paper introduces a multimodal, human-centered framework for assessing pedestrian well-being in the wild by integrating three complementary data streams: continuous physiological sensing, geospatial tracking, and momentary self-reports collected using the Experience Sampling Method. The framework conceptualizes pedestrian experience as a triangulation enabling a holistic understanding of how urban environments influence well-being. The utility of our framework is then demonstrated through a naturalistic case study conducted in the Greater Philadelphia region, in which participants wore research-grade wearable sensors and carried GPS-enabled smartphones during their regular daily activities. Physiological indicators of autonomic nervous system activity, including heart rate variability and electrodermal activity, were synchronized with spatial trajectories and in situ self-reports of stress, affect, and perceived infrastructure conditions. Results illustrate substantial inter- and intra-individual variability in both subjective experience and physiological response, as well as context-dependent patterns associated with traffic exposure, pedestrian infrastructure quality, and environmental enclosure. The findings also suggest that commonly used walkability indices may not fully capture experiential dimensions of pedestrian well-being. By enabling real-world, multimodal measurement of pedestrian experience, the proposed framework offers a scalable and transferable approach for advancing human-centered urban analytics.

