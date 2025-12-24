---
layout: default
title: Adversarial Generation and Collaborative Evolution of Safety-Critical Scenarios for Autonomous Vehicles
---

# Adversarial Generation and Collaborative Evolution of Safety-Critical Scenarios for Autonomous Vehicles

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.14527" class="toolbar-btn" target="_blank">📄 arXiv: 2508.14527v2</a>
  <a href="https://arxiv.org/pdf/2508.14527.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.14527v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.14527v2', 'Adversarial Generation and Collaborative Evolution of Safety-Critical Scenarios for Autonomous Vehicles')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jiangfan Liu, Yongkang Guo, Fangzhi Zhong, Tianyuan Zhang, Zonglei Jing, Siyuan Liang, Jiakai Wang, Mingchuan Zhang, Aishan Liu, Xianglong Liu

**分类**: cs.CV

**发布日期**: 2025-08-20 (更新: 2025-08-22)

---

## 💡 一句话要点

**提出ScenGE框架以生成安全关键场景，提升自动驾驶安全性**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `自动驾驶` `安全评估` `对抗生成` `场景演化` `强化学习` `模型鲁棒性` `交通流模拟`

## 📋 核心要点

1. 现有方法依赖于预定义的威胁模式，难以暴露多样化和不可预见的故障模式。
2. 提出ScenGE框架，通过推理对抗案例并利用复杂交通流生成安全关键场景。
3. 实验表明，ScenGE在发现碰撞案例方面比现有基线提升了31.96%。

## 📝 摘要（中文）

安全关键场景的生成在自动驾驶车辆的安全评估中变得愈发重要。然而，现有方法主要依赖于预定义的威胁模式或基于规则的策略，限制了其暴露多样化和不可预见的故障模式的能力。为此，本文提出了ScenGE框架，通过推理新颖的对抗案例并利用复杂的交通流来生成丰富的安全关键场景。该框架首先通过一个大型语言模型进行元场景生成，推断出一种可能且具有挑战性的对抗代理行为。随后，通过背景车辆放大核心威胁，并构建对抗协作图以优化关键代理轨迹。实验结果表明，ScenGE在多个强化学习基础的自动驾驶模型上发现的碰撞案例比现有方法平均提升了31.96%。

## 🔬 方法详解

**问题定义**：本文旨在解决自动驾驶车辆在安全评估中生成多样化安全关键场景的不足，现有方法无法有效暴露潜在的故障模式。

**核心思路**：ScenGE框架通过推理对抗案例并结合复杂交通流，生成丰富的安全关键场景，以提高自动驾驶系统的安全性和鲁棒性。

**技术框架**：整体架构包括两个主要模块：元场景生成和复杂场景演化。元场景生成利用大型语言模型推断对抗代理行为，复杂场景演化则通过背景车辆放大核心威胁。

**关键创新**：最重要的创新在于构建了对抗协作图，以识别关键代理轨迹进行优化，从而有效减少自我车辆的操控空间并创造关键遮挡。

**关键设计**：在设计中，采用了基于强化学习的模型进行实验，设置了特定的损失函数以优化对抗场景的生成，并确保生成的场景在模拟器中可执行。

## 📊 实验亮点

实验结果显示，ScenGE框架在多个强化学习基础的自动驾驶模型上发现的严重碰撞案例平均比现有最先进基线提升了31.96%。此外，框架可应用于大型模型基础的自动驾驶系统，并在不同模拟器上部署，进一步验证了其有效性。

## 🎯 应用场景

该研究的潜在应用领域包括自动驾驶系统的安全评估与测试，能够为自动驾驶车辆在实际道路部署前提供更为全面的安全保障。未来，ScenGE框架有望推动自动驾驶技术的安全性提升，增强公众信任。

## 📄 摘要（原文）

> The generation of safety-critical scenarios in simulation has become increasingly crucial for safety evaluation in autonomous vehicles prior to road deployment in society. However, current approaches largely rely on predefined threat patterns or rule-based strategies, which limit their ability to expose diverse and unforeseen failure modes. To overcome these, we propose ScenGE, a framework that can generate plentiful safety-critical scenarios by reasoning novel adversarial cases and then amplifying them with complex traffic flows. Given a simple prompt of a benign scene, it first performs Meta-Scenario Generation, where a large language model, grounded in structured driving knowledge, infers an adversarial agent whose behavior poses a threat that is both plausible and deliberately challenging. This meta-scenario is then specified in executable code for precise in-simulator control. Subsequently, Complex Scenario Evolution uses background vehicles to amplify the core threat introduced by Meta-Scenario. It builds an adversarial collaborator graph to identify key agent trajectories for optimization. These perturbations are designed to simultaneously reduce the ego vehicle's maneuvering space and create critical occlusions. Extensive experiments conducted on multiple reinforcement learning based AV models show that ScenGE uncovers more severe collision cases (+31.96%) on average than SoTA baselines. Additionally, our ScenGE can be applied to large model based AV systems and deployed on different simulators; we further observe that adversarial training on our scenarios improves the model robustness. Finally, we validate our framework through real-world vehicle tests and human evaluation, confirming that the generated scenarios are both plausible and critical. We hope our paper can build up a critical step towards building public trust and ensuring their safe deployment.

