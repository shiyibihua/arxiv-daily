---
layout: default
title: Sailing Towards Zero-Shot State Estimation using Foundation Models Combined with a UKF
---

# Sailing Towards Zero-Shot State Estimation using Foundation Models Combined with a UKF

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.04213" class="toolbar-btn" target="_blank">📄 arXiv: 2509.04213v1</a>
  <a href="https://arxiv.org/pdf/2509.04213.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.04213v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.04213v1', 'Sailing Towards Zero-Shot State Estimation using Foundation Models Combined with a UKF')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Tobin Holtmann, David Stenger, Andres Posada-Moreno, Friedrich Solowjow, Sebastian Trimpe

**分类**: eess.SY, cs.LG

**发布日期**: 2025-09-04

**备注**: Accepted for publication at CDC2025

---

## 💡 一句话要点

**提出FM-UKF，结合预训练模型与UKF实现零样本状态估计，提升船舶控制精度。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `零样本学习` `状态估计` `无迹卡尔曼滤波` `基础模型` `Transformer` `系统辨识` `船舶控制`

## 📋 核心要点

1. 传统状态估计依赖大量数据和人工系统辨识，泛化能力弱，难以适应新系统。
2. FM-UKF结合Transformer动力学模型和UKF，利用分析传感器模型，实现跨动力学零样本泛化。
3. 实验表明，FM-UKF在集装箱船模型上，精度、工作量和鲁棒性上优于传统方法和端到端方法。

## 📝 摘要（中文）

传统控制和系统工程中的状态估计需要大量的人工系统辨识或数据收集工作。然而，基于Transformer的基础模型通过利用预训练的通用模型，降低了数据需求。最终，开发系统动力学的零样本基础模型可以大幅减少人工部署工作。虽然最近的研究表明，基于Transformer的端到端方法可以在未见过的系统上实现零样本性能，但它们仅限于训练期间见过的传感器模型。我们引入了基础模型无迹卡尔曼滤波器（FM-UKF），它将基于Transformer的系统动力学模型与通过UKF分析已知的传感器模型相结合，从而能够在不同的动力学中泛化，而无需为新的传感器配置进行重新训练。我们在一个具有复杂动力学的集装箱船模型的新基准上评估了FM-UKF，与具有近似系统知识的经典方法和端到端方法相比，证明了其在精度、工作量和鲁棒性之间的竞争性折衷。该基准和数据集已开源，以进一步支持未来通过基础模型进行零样本状态估计的研究。

## 🔬 方法详解

**问题定义**：论文旨在解决状态估计中对大量数据和人工系统辨识的依赖问题，尤其是在传感器配置变化时，传统方法需要重新训练。现有端到端方法虽然能实现零样本性能，但仅限于训练期间见过的传感器模型，泛化能力受限。

**核心思路**：论文的核心思路是将预训练的Transformer模型用于学习系统动力学，并将其与分析已知的传感器模型通过无迹卡尔曼滤波器（UKF）相结合。这种方法利用了Transformer强大的动力学建模能力，同时保留了UKF处理传感器模型的灵活性，从而实现跨不同动力学和传感器配置的零样本泛化。

**技术框架**：FM-UKF的整体框架包含两个主要模块：1) 基于Transformer的系统动力学模型，用于预测系统状态的演化；2) 无迹卡尔曼滤波器（UKF），用于融合Transformer的预测和传感器测量值，估计当前状态。UKF利用分析已知的传感器模型，无需重新训练即可适应新的传感器配置。整个流程如下：首先，Transformer模型根据上一时刻的状态预测当前时刻的状态；然后，UKF将该预测与传感器测量值融合，得到最终的状态估计。

**关键创新**：最重要的技术创新点在于将预训练的Transformer模型与UKF相结合，实现了零样本状态估计。与传统的基于模型的方法相比，FM-UKF无需手动系统辨识或大量数据收集。与端到端方法相比，FM-UKF可以泛化到训练期间未见过的传感器配置。

**关键设计**：论文中Transformer模型的具体结构和训练方式未知（摘要未提及）。UKF的实现采用标准算法，关键在于如何将Transformer模型的输出作为UKF的状态转移函数输入。具体参数设置和损失函数等细节在摘要中未提及，需要参考论文全文。

## 📊 实验亮点

论文在一个具有复杂动力学的集装箱船模型的新基准上评估了FM-UKF，实验结果表明，与具有近似系统知识的经典方法和端到端方法相比，FM-UKF在精度、工作量和鲁棒性之间取得了竞争性的折衷。具体性能数据和提升幅度在摘要中未给出，需要参考论文全文。

## 🎯 应用场景

FM-UKF可应用于各种需要状态估计的控制系统，尤其是在系统动力学复杂且难以建模，或者传感器配置经常变化的情况下。例如，自主导航、机器人控制、过程控制等领域。该方法降低了系统部署和维护的成本，提高了系统的适应性和鲁棒性，具有重要的实际应用价值。

## 📄 摘要（原文）

> State estimation in control and systems engineering traditionally requires extensive manual system identification or data-collection effort. However, transformer-based foundation models in other domains have reduced data requirements by leveraging pre-trained generalist models. Ultimately, developing zero-shot foundation models of system dynamics could drastically reduce manual deployment effort. While recent work shows that transformer-based end-to-end approaches can achieve zero-shot performance on unseen systems, they are limited to sensor models seen during training. We introduce the foundation model unscented Kalman filter (FM-UKF), which combines a transformer-based model of system dynamics with analytically known sensor models via an UKF, enabling generalization across varying dynamics without retraining for new sensor configurations. We evaluate FM-UKF on a new benchmark of container ship models with complex dynamics, demonstrating a competitive accuracy, effort, and robustness trade-off compared to classical methods with approximate system knowledge and to an end-to-end approach. The benchmark and dataset are open sourced to further support future research in zero-shot state estimation via foundation models.

