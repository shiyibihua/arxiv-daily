---
layout: default
title: A Scenario-based Model Predictive Control Scheme for Pandemic Response through Non-pharmaceutical Interventions
---

# A Scenario-based Model Predictive Control Scheme for Pandemic Response through Non-pharmaceutical Interventions

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.17972" class="toolbar-btn" target="_blank">📄 arXiv: 2506.17972v1</a>
  <a href="https://arxiv.org/pdf/2506.17972.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.17972v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.17972v1', 'A Scenario-based Model Predictive Control Scheme for Pandemic Response through Non-pharmaceutical Interventions')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Domagoj Herceg, Marco DellOro, Riccardo Bertollo, Fuminari Miura, Paul de Klaver, Valentina Breschi, Dinesh Krishnamoorthy, Mauro Salazar

**分类**: eess.SY

**发布日期**: 2025-06-22

---

## 💡 一句话要点

**提出基于场景的模型预测控制方案以应对疫情**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)**

**关键词**: `模型预测控制` `非药物干预` `疫情应对` `公共卫生` `不确定性管理`

## 📋 核心要点

1. 现有方法在应对疫情时往往无法有效处理不确定性，导致医院压力过大。
2. 论文提出了一种基于场景的MPC方案，通过预测疫情演变来动态调整NPI的实施程度。
3. 实验结果显示，该方案在多种复杂场景下均能有效控制医院压力，优于传统MPC方法。

## 📝 摘要（中文）

本文提出了一种基于场景的模型预测控制（MPC）方案，旨在通过非药物干预措施（NPI）控制不断演变的疫情。该方法结合了对疫情可能演变的预测，以决定在多个星期内实施的NPI的严重程度，从而保持医院压力在规定阈值以下，同时最小化对社会的影响。具体而言，首先引入了一个将人群划分为易感、感染、检测、威胁、康复和死亡（SIDTHE）子人群的分隔模型，并描述其正不变集。该模型能够明确捕捉住住院患者的比例，同时保持与公开数据集的参数可识别性。其次，设计了一种基于场景的MPC方案，考虑了模型参数的潜在不确定性，例如由于人口行为或季节性变化。结果表明，所提出的控制器能够有效应对各种场景，即使在常规MPC方法失效的情况下，也能保持医院压力在可控范围内。

## 🔬 方法详解

**问题定义**：本文旨在解决在疫情期间如何有效控制医院压力的问题。现有方法在面对不确定性时表现不佳，无法适应快速变化的疫情情况。

**核心思路**：论文的核心思路是结合场景预测与模型预测控制，通过动态调整非药物干预措施的强度来应对疫情的演变。这种设计能够更好地适应不同的疫情发展情境。

**技术框架**：整体架构包括一个分隔模型（SIDTHE），用于描述人群的不同状态，以及一个基于场景的MPC控制器，能够根据预测的疫情演变动态调整干预措施。主要模块包括状态预测、干预决策和反馈调整。

**关键创新**：最重要的技术创新在于引入了场景预测机制，使得控制器能够在面对不确定性时仍然保持有效性。这与传统MPC方法的静态决策机制形成了鲜明对比。

**关键设计**：关键设计包括对SIDTHE模型的参数设置，确保其能够准确反映住院患者的比例，并通过损失函数优化控制策略，以平衡医院压力与社会影响。

## 📊 实验亮点

实验结果表明，所提出的基于场景的MPC方案在多种复杂场景下均能有效控制医院压力，保持在规定阈值以下，相较于传统MPC方法，提升幅度显著，尤其在高不确定性情况下表现尤为突出。

## 🎯 应用场景

该研究的潜在应用领域包括公共卫生管理、疫情应对策略制定及医院资源调配等。通过有效控制医院压力，能够提升医疗系统的应对能力，减少疫情对社会的负面影响，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> This paper presents a scenario-based model predictive control (MPC) scheme designed to control an evolving pandemic via non-pharmaceutical intervention (NPIs). The proposed approach combines predictions of possible pandemic evolution to decide on a level of severity of NPIs to be implemented over multiple weeks to maintain hospital pressure below a prescribed threshold, while minimizing their impact on society. Specifically, we first introduce a compartmental model which divides the population into Susceptible, Infected, Detected, Threatened, Healed, and Expired (SIDTHE) subpopulations and describe its positive invariant set. This model is expressive enough to explicitly capture the fraction of hospitalized individuals while preserving parameter identifiability w.r.t. publicly available datasets. Second, we devise a scenario-based MPC scheme with recourse actions that captures potential uncertainty of the model parameters. e.g., due to population behavior or seasonality. Our results show that the scenario-based nature of the proposed controller manages to adequately respond to all scenarios, keeping the hospital pressure at bay also in very challenging situations when conventional MPC methods fail.

