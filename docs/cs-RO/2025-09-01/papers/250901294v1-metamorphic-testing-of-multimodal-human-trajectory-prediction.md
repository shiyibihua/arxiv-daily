---
layout: default
title: Metamorphic Testing of Multimodal Human Trajectory Prediction
---

# Metamorphic Testing of Multimodal Human Trajectory Prediction

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.01294" class="toolbar-btn" target="_blank">📄 arXiv: 2509.01294v1</a>
  <a href="https://arxiv.org/pdf/2509.01294.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.01294v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.01294v1', 'Metamorphic Testing of Multimodal Human Trajectory Prediction')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Helge Spieker, Nadjib Lazaar, Arnaud Gotlieb, Nassim Belmecheri

**分类**: cs.SE, cs.RO

**发布日期**: 2025-09-01

**备注**: Information and Software Technology

**DOI**: [10.1016/j.infsof.2025.107890](https://doi.org/10.1016/j.infsof.2025.107890)

---

## 💡 一句话要点

**提出一种基于变质测试的多模态人类轨迹预测模型评估框架**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `变质测试` `人类轨迹预测` `多模态模型` `自动驾驶` `模型评估` `鲁棒性测试` `概率分布距离`

## 📋 核心要点

1. 多模态人类轨迹预测模型在自动驾驶等领域至关重要，但缺乏有效的测试方法来保证其安全性和可靠性。
2. 论文提出利用变质测试的思想，通过设计一系列变质关系，在没有ground truth的情况下评估预测模型的鲁棒性。
3. 通过对历史轨迹和环境地图进行变换，并观察预测轨迹的相应变化，从而实现对模型的有效测试。

## 📝 摘要（中文）

本文提出了一种针对多模态人类轨迹预测（HTP）系统进行测试的变质测试（MT）方法。由于HTP模型通常使用多个输入源（例如，轨迹历史和环境地图）并产生随机输出（多个可能的未来路径），因此对其进行严格测试极具挑战性，主要困难在于缺乏明确的测试预言。本文通过适用于HTP复杂性和随机性的变质关系（MR）来解决预言问题。提出了五个MR，针对历史轨迹数据和用作环境上下文的语义分割地图的转换。这些MR包括：1）应用于轨迹和地图输入的标签保持几何变换（镜像、旋转、缩放），预期输出相应变换；2）地图改变变换（改变语义类标签、引入障碍物），轨迹分布产生可预测的变化。提出了基于概率分布之间距离度量（如Wasserstein或Hellinger距离）的概率违反准则。该研究引入了一个MT框架，用于对多模态、随机HTP系统进行无预言测试，无需依赖真实轨迹即可评估模型对输入转换和上下文变化的鲁棒性。

## 🔬 方法详解

**问题定义**：多模态人类轨迹预测（HTP）模型在自动驾驶和机器人等领域应用广泛，但由于其输入的多样性（历史轨迹、环境信息等）和输出的随机性（多个可能的未来轨迹），传统的测试方法难以有效评估模型的性能。缺乏明确的测试预言（ground truth）是主要痛点，难以判断预测结果的正确性。现有方法难以保证模型在各种复杂场景下的鲁棒性和可靠性。

**核心思路**：本文的核心思路是利用变质测试（Metamorphic Testing, MT）的思想，通过设计一系列变质关系（Metamorphic Relations, MRs），在没有ground truth的情况下，间接验证模型的正确性。如果输入发生某种可预测的变化，那么输出也应该发生相应的变化。如果模型违反了这些变质关系，则表明模型存在缺陷。

**技术框架**：该框架主要包含以下几个步骤：1）定义变质关系：针对HTP模型的特点，设计一系列MRs，包括对历史轨迹和环境地图的几何变换（如旋转、缩放、镜像）以及语义信息的改变（如添加障碍物）。2）生成测试用例：根据定义的MRs，对原始输入数据进行变换，生成新的测试用例。3）执行模型预测：使用原始输入和变换后的输入分别运行HTP模型，得到预测的轨迹分布。4）验证变质关系：比较原始预测结果和变换后的预测结果，判断是否满足预定义的MRs。如果违反MRs，则认为模型存在缺陷。

**关键创新**：最重要的技术创新点在于针对多模态HTP模型设计了一系列有效的变质关系。这些MRs不仅考虑了轨迹数据的几何变换，还考虑了环境语义信息的变化，能够更全面地评估模型的鲁棒性。此外，论文还提出了基于概率分布距离（如Wasserstein距离和Hellinger距离）的概率违反准则，用于量化评估模型是否违反MRs。

**关键设计**：论文设计了五种MRs，包括：1）轨迹和地图的镜像变换；2）轨迹和地图的旋转变换；3）轨迹和地图的缩放变换；4）改变地图的语义类标签；5）在地图中引入障碍物。对于概率违反准则，论文使用Wasserstein距离或Hellinger距离来衡量原始预测轨迹分布和变换后预测轨迹分布之间的差异。如果该距离超过预定义的阈值，则认为模型违反了MRs。

## 📊 实验亮点

该研究提出了五种针对多模态人类轨迹预测模型的变质关系，并使用Wasserstein距离和Hellinger距离等指标来量化评估模型是否违反这些关系。实验结果表明，该方法能够有效地检测出模型在处理输入变换和上下文变化时的潜在问题，为提高模型的鲁棒性提供了有效手段。

## 🎯 应用场景

该研究成果可应用于自动驾驶、机器人导航、智能监控等领域，用于评估和验证人类轨迹预测模型的安全性和可靠性。通过变质测试，可以发现模型在特定场景下的潜在缺陷，提高系统的整体安全性，减少事故发生的可能性。未来，该方法可以扩展到其他类型的预测模型，例如车辆轨迹预测和行为预测。

## 📄 摘要（原文）

> Context: Predicting human trajectories is crucial for the safety and reliability of autonomous systems, such as automated vehicles and mobile robots. However, rigorously testing the underlying multimodal Human Trajectory Prediction (HTP) models, which typically use multiple input sources (e.g., trajectory history and environment maps) and produce stochastic outputs (multiple possible future paths), presents significant challenges. The primary difficulty lies in the absence of a definitive test oracle, as numerous future trajectories might be plausible for any given scenario. Objectives: This research presents the application of Metamorphic Testing (MT) as a systematic methodology for testing multimodal HTP systems. We address the oracle problem through metamorphic relations (MRs) adapted for the complexities and stochastic nature of HTP. Methods: We present five MRs, targeting transformations of both historical trajectory data and semantic segmentation maps used as an environmental context. These MRs encompass: 1) label-preserving geometric transformations (mirroring, rotation, rescaling) applied to both trajectory and map inputs, where outputs are expected to transform correspondingly. 2) Map-altering transformations (changing semantic class labels, introducing obstacles) with predictable changes in trajectory distributions. We propose probabilistic violation criteria based on distance metrics between probability distributions, such as the Wasserstein or Hellinger distance. Conclusion: This study introduces tool, a MT framework for the oracle-less testing of multimodal, stochastic HTP systems. It allows for assessment of model robustness against input transformations and contextual changes without reliance on ground-truth trajectories.

