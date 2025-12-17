---
layout: default
title: Mantis: A Versatile Vision-Language-Action Model with Disentangled Visual Foresight
---

# Mantis: A Versatile Vision-Language-Action Model with Disentangled Visual Foresight

<div class="paper-toolbar">
  <div class="toolbar-left">
    <a href="https://arxiv.org/abs/2511.16175" target="_blank" class="toolbar-btn">arXiv: 2511.16175v1</a>
    <a href="https://arxiv.org/pdf/2511.16175.pdf" target="_blank" class="toolbar-btn">PDF</a>
  </div>
  <div class="toolbar-right">
    <button class="toolbar-btn favorite-btn" data-arxiv-id="2511.16175v1" 
            onclick="toggleFavorite(this, '2511.16175v1', 'Mantis: A Versatile Vision-Language-Action Model with Disentangled Visual Foresight')" title="收藏">
      ☆ 收藏
    </button>
    <button class="toolbar-btn share-btn" onclick="copyLink()" title="复制链接">
      🔗 分享
    </button>
  </div>
</div>


**作者**: Yi Yang, Xueqi Li, Yiyang Chen, Jin Song, Yihan Wang, Zipeng Xiao, Jiadi Su, You Qiaoben, Pengfei Liu, Zhijie Deng

**分类**: cs.CV, cs.AI

**发布日期**: 2025-11-20

---

## 💡 一句话要点

**Mantis：一种具有解耦视觉预测的多功能视觉-语言-动作模型**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)**

**关键词**: `视觉-语言-动作模型` `解耦视觉预测` `扩散Transformer` `机器人操作` `指令跟随` `视觉预测` `元查询`

## 📋 核心要点

1. 现有VLA模型直接预测高维视觉状态或压缩视觉信息，导致模型能力下降和信息瓶颈。
2. Mantis通过解耦视觉预测，利用元查询和扩散Transformer，降低骨干网络负担，提升理解和推理能力。
3. Mantis在LIBERO基准测试中达到96.7%的成功率，并在真实世界环境中优于现有VLA模型。

## 📝 摘要（中文）

本文提出Mantis，一种新颖的视觉-语言-动作（VLA）模型框架，其核心是解耦视觉预测（DVF）。现有VLA模型直接预测高维视觉状态会分散模型能力并导致过高的训练成本，而将视觉状态压缩为更紧凑的监督信号不可避免地会造成信息瓶颈。此外，由于忽略了语言监督，现有方法通常存在较差的理解和推理能力。Mantis通过元查询和扩散Transformer（DiT）头的组合，将视觉预测与骨干网络解耦。通过残差连接将当前视觉状态提供给DiT，一个简单的下一状态预测目标使元查询能够自动捕获描绘视觉轨迹的潜在动作，从而促进显式动作的学习。这种解耦降低了VLA骨干网络的负担，使其能够通过语言监督保持理解和推理能力。在人类操作视频、机器人演示和图像-文本对上进行预训练后，Mantis在LIBERO基准测试中经过微调后达到了96.7%的成功率，超过了强大的基线，同时表现出很高的收敛速度。真实世界的评估表明，Mantis优于领先的开源VLA模型$π_{0.5}$，尤其是在指令跟随能力、对未见指令的泛化以及推理能力方面。代码和权重已发布以支持开源社区。

## 🔬 方法详解

**问题定义**：现有视觉-语言-动作（VLA）模型在处理高维视觉状态预测时面临挑战，直接预测导致模型能力分散和训练成本高昂，而压缩视觉信息则会造成信息瓶颈。此外，现有方法往往忽略了语言监督，导致理解和推理能力不足。

**核心思路**：Mantis的核心思路是通过解耦视觉预测来解决上述问题。具体来说，它将视觉预测任务从VLA骨干网络中分离出来，利用元查询和扩散Transformer（DiT）头来预测下一状态的视觉信息。这种解耦降低了骨干网络的负担，使其能够专注于语言理解和推理。

**技术框架**：Mantis的整体框架包括一个VLA骨干网络和一个解耦的视觉预测模块。VLA骨干网络负责处理视觉和语言输入，并生成动作指令。解耦的视觉预测模块则利用元查询和DiT头来预测下一状态的视觉信息。当前视觉状态通过残差连接提供给DiT，元查询负责捕获潜在动作，从而指导视觉轨迹的预测。

**关键创新**：Mantis的关键创新在于解耦视觉预测（DVF）。与现有方法直接预测或压缩视觉状态不同，Mantis将视觉预测任务分离出来，利用元查询和DiT头进行预测。这种解耦降低了骨干网络的负担，使其能够更好地利用语言监督，从而提升理解和推理能力。

**关键设计**：Mantis的关键设计包括：1) 使用元查询来捕获潜在动作，从而指导视觉轨迹的预测；2) 使用扩散Transformer（DiT）头来预测下一状态的视觉信息；3) 通过残差连接将当前视觉状态提供给DiT，从而提高预测的准确性；4) 使用简单的下一状态预测目标来训练视觉预测模块。

## 📊 实验亮点

Mantis在LIBERO基准测试中取得了显著成果，经过微调后成功率达到96.7%，超越了现有基线模型。在真实世界环境中，Mantis在指令跟随能力、对未见指令的泛化以及推理能力方面均优于领先的开源VLA模型$π_{0.5}$。这些结果表明，Mantis具有强大的视觉-语言-动作理解和预测能力。

## 🎯 应用场景

Mantis具有广泛的应用前景，可用于机器人操作、自动驾驶、虚拟现实等领域。通过理解人类指令并预测未来视觉状态，Mantis可以使机器人更智能地执行复杂任务，例如物品抓取、装配等。此外，Mantis还可以用于自动驾驶汽车的场景理解和行为预测，提高驾驶安全性。在虚拟现实领域，Mantis可以用于生成更逼真的虚拟环境和交互体验。

## 📄 摘要（原文）

> Recent advances in Vision-Language-Action (VLA) models demonstrate that visual signals can effectively complement sparse action supervisions. However, letting VLA directly predict high-dimensional visual states can distribute model capacity and incur prohibitive training cost, while compressing visual states into more compact supervisory signals inevitably incurs information bottlenecks. Moreover, existing methods often suffer from poor comprehension and reasoning capabilities due to the neglect of language supervision. This paper introduces Mantis, a novel framework featuring a Disentangled Visual Foresight (DVF) to tackle these issues. Specifically, Mantis decouples visual foresight prediction from the backbone with the combination of meta queries and a diffusion Transformer (DiT) head. With the current visual state provided to the DiT via a residual connection, a simple next-state prediction objective enables the meta queries to automatically capture the latent actions that delineate the visual trajectory, and hence boost the learning of explicit actions. The disentanglement reduces the burden of the VLA backbone, enabling it to maintain comprehension and reasoning capabilities through language supervision. Empirically, pretrained on human manipulation videos, robot demonstrations, and image-text pairs, Mantis achieves a 96.7% success rate on LIBERO benchmark after fine-tuning, surpassing powerful baselines while exhibiting high convergence speed. Real-world evaluations show that Mantis outperforms $π_{0.5}$, a leading open-source VLA model, particularly in instruction-following capability, generalization to unseen instructions, and reasoning ability. Code and weights are released to support the open-source community.

