---
layout: default
title: Hybrid Adaptive Conformal Offline Reinforcement Learning for Fair Population Health Management
---

# Hybrid Adaptive Conformal Offline Reinforcement Learning for Fair Population Health Management

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.09772" class="toolbar-btn" target="_blank">📄 arXiv: 2509.09772v1</a>
  <a href="https://arxiv.org/pdf/2509.09772.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.09772v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.09772v1', 'Hybrid Adaptive Conformal Offline Reinforcement Learning for Fair Population Health Management')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Sanjay Basu, Sadiq Y. Patel, Parth Sheth, Bhairavi Muralidharan, Namrata Elamaran, Aakriti Kinra, Rajaie Batniji

**分类**: cs.LG, stat.AP

**发布日期**: 2025-09-11

**备注**: 10 pages, 5 figures, 4 tables

---

## 💡 一句话要点

**提出混合自适应保形离线强化学习框架HACO，用于公平的人群健康管理。**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `离线强化学习` `人群健康管理` `保形推理` `风险控制` `公平性` `医疗决策` `风险评估`

## 📋 核心要点

1. 现有医疗补助人群健康管理项目需保证安全性、公平性和可审计性，但缺乏有效的大规模决策支持。
2. HACO框架分离风险校准与偏好优化，通过保形推理屏蔽高风险行动，并在安全子集上学习偏好策略。
3. 实验表明HACO在风险区分上表现出色（AUC~0.81），同时保持高安全覆盖率，并能发现不同人群的价值差异。

## 📝 摘要（中文）

本文提出了一种混合自适应保形离线强化学习（HACO）框架，该框架将风险校准与偏好优化分离，从而大规模地生成保守的行动建议，应用于医疗补助人群的健康管理项目。在我们的设置中，每一步都涉及在常见的协调行动中进行选择（例如，联系哪个成员，通过哪种方式，以及是否转到专门的服务），同时控制近期不良利用事件的风险（例如，计划外的急诊就诊或住院）。使用来自Waymark的包含168,126名患者的277万个连续决策的去标识化运营数据集，HACO（i）训练一个轻量级的不良事件风险模型，（ii）导出一个保形阈值以在目标风险水平下屏蔽不安全的行动，以及（iii）在由此产生的安全子集上学习偏好策略。我们使用与版本无关的拟合Q评估（FQE）在分层子集上评估策略，并审核跨年龄、性别和种族的分组表现。HACO实现了强大的风险区分（AUC〜0.81），并具有校准的阈值（α=0.10时τ〜0.038），同时保持了较高的安全覆盖率。亚组分析揭示了不同人群在估计价值方面的系统性差异，突显了公平性审核的重要性。我们的结果表明，保形风险门控与离线强化学习无缝集成，可为人群健康管理团队提供保守的、可审计的决策支持。

## 🔬 方法详解

**问题定义**：人群健康管理项目需要协调外联和服务，例如福利导航、行为健康、社会需求支持和临床安排。现有方法难以在保证安全、公平和可审计性的前提下，对大规模人群进行个性化干预决策，尤其是在控制不良事件风险方面存在挑战。

**核心思路**：HACO的核心思路是将风险评估和策略优化解耦。首先，通过风险模型预测不良事件的风险，然后使用保形推理确定一个阈值，将高风险的行动屏蔽掉，最后在剩余的安全行动集合上学习最优策略。这样可以确保策略的安全性，同时提高策略的公平性和可审计性。

**技术框架**：HACO框架包含三个主要阶段：（1）风险模型训练：使用历史数据训练一个轻量级的风险模型，用于预测每个行动导致不良事件的概率。（2）保形阈值推导：利用保形推理，根据设定的风险水平α，计算出一个阈值τ，用于过滤掉风险高于τ的行动。（3）偏好策略学习：在过滤后的安全行动集合上，使用离线强化学习算法（如FQE）学习一个偏好策略，该策略旨在最大化长期回报。

**关键创新**：HACO的关键创新在于将保形推理与离线强化学习相结合，用于风险控制和策略优化。保形推理提供了一种非参数化的方法来估计风险，并保证在给定的风险水平下，策略的安全性。与传统的风险约束强化学习方法相比，HACO不需要显式地定义风险约束，而是通过数据驱动的方式学习风险阈值。

**关键设计**：风险模型可以使用任何分类算法，例如逻辑回归或梯度提升树。保形阈值τ的选择基于历史数据的风险分布，并通过交叉验证进行优化。偏好策略的学习可以使用任何离线强化学习算法，例如拟合Q评估（FQE）。论文中使用了版本无关的FQE，以提高策略的泛化能力。目标风险水平α是一个重要的超参数，需要根据实际应用场景进行调整。

## 📊 实验亮点

实验结果表明，HACO在Waymark的真实数据集上取得了显著的成果。HACO实现了强大的风险区分能力（AUC约为0.81），并找到了一个校准的阈值（α=0.10时τ约为0.038），同时保持了较高的安全覆盖率。亚组分析揭示了不同人群在估计价值方面的系统性差异，强调了公平性审核的重要性。

## 🎯 应用场景

HACO框架可应用于各种人群健康管理场景，例如医疗补助计划、慢性病管理和预防性保健。它可以帮助医疗机构制定个性化的干预策略，降低不良事件的风险，提高医疗服务的效率和公平性。此外，HACO框架的可审计性使其能够满足监管要求，并提高患者和医疗机构的信任度。

## 📄 摘要（原文）

> Population health management programs for Medicaid populations coordinate longitudinal outreach and services (e.g., benefits navigation, behavioral health, social needs support, and clinical scheduling) and must be safe, fair, and auditable. We present a Hybrid Adaptive Conformal Offline Reinforcement Learning (HACO) framework that separates risk calibration from preference optimization to generate conservative action recommendations at scale. In our setting, each step involves choosing among common coordination actions (e.g., which member to contact, by which modality, and whether to route to a specialized service) while controlling the near-term risk of adverse utilization events (e.g., unplanned emergency department visits or hospitalizations). Using a de-identified operational dataset from Waymark comprising 2.77 million sequential decisions across 168,126 patients, HACO (i) trains a lightweight risk model for adverse events, (ii) derives a conformal threshold to mask unsafe actions at a target risk level, and (iii) learns a preference policy on the resulting safe subset. We evaluate policies with a version-agnostic fitted Q evaluation (FQE) on stratified subsets and audit subgroup performance across age, sex, and race. HACO achieves strong risk discrimination (AUC ~0.81) with a calibrated threshold ( τ ~0.038 at α = 0.10), while maintaining high safe coverage. Subgroup analyses reveal systematic differences in estimated value across demographics, underscoring the importance of fairness auditing. Our results show that conformal risk gating integrates cleanly with offline RL to deliver conservative, auditable decision support for population health management teams.

