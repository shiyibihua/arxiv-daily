---
layout: default
title: Normalizing Flows are Capable Visuomotor Policy Learning Models
---

# Normalizing Flows are Capable Visuomotor Policy Learning Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.21073" class="toolbar-btn" target="_blank">📄 arXiv: 2509.21073v1</a>
  <a href="https://arxiv.org/pdf/2509.21073.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.21073v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.21073v1', 'Normalizing Flows are Capable Visuomotor Policy Learning Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Simon Kristoffersson Lind, Jialong Li, Maj Stenmark, Volker Krüger

**分类**: cs.RO

**发布日期**: 2025-09-25

---

## 💡 一句话要点

**提出基于Normalizing Flows的视觉运动策略学习模型，提升推理速度和置信度评估。**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `Normalizing Flows` `视觉运动策略学习` `机器人` `策略学习` `置信度评估`

## 📋 核心要点

1. 扩散模型在机器人领域应用广泛，但其推理计算成本高，且难以量化输出的不确定性。
2. 提出Normalizing Flows Policy，利用Normalizing Flows高效推理和提供置信度度量的优势，替代扩散模型。
3. 实验表明，该方法在多个机器人任务中性能媲美甚至超越扩散模型，且推理速度提升显著。

## 📝 摘要（中文）

本文提出了一种基于Normalizing Flows的视觉运动策略学习模型，称为Normalizing Flows Policy。该模型旨在解决现有方法（如扩散模型）在通用机器人领域中存在的计算成本高昂和无法量化输出不确定性的问题。作者认为，模型的可信度与提供置信度度量的能力密切相关。实验结果表明，Normalizing Flows Policy在四个不同的模拟机器人任务中，性能可与扩散策略相媲美，甚至超越，同时提高了样本效率，并将推理速度提高了30倍。此外，消融研究验证了使Normalizing Flows在该领域表现良好的关键架构和训练技术。

## 🔬 方法详解

**问题定义**：现有基于扩散模型的视觉运动策略学习方法，虽然能够建模复杂的行为，但存在两个主要痛点：一是推理过程计算成本高昂，导致实时性较差；二是缺乏对输出结果不确定性的有效量化，难以评估策略的可靠性，这对于安全至关重要的机器人应用来说是不可接受的。

**核心思路**：论文的核心思路是利用Normalizing Flows来建模视觉运动策略。Normalizing Flows是一种概率生成模型，它通过一系列可逆变换将一个简单的概率分布（如高斯分布）转换为复杂的数据分布。由于变换是可逆的，因此可以高效地进行采样和密度估计，从而实现快速推理和置信度评估。

**技术框架**：Normalizing Flows Policy的整体框架包括以下几个主要模块：1) 视觉编码器：将输入的视觉信息（如图像）编码成低维的特征向量；2) Normalizing Flows模型：将视觉特征向量作为条件，学习一个从简单分布到动作空间的映射；3) 策略执行器：根据Normalizing Flows模型生成的动作，控制机器人执行相应的操作。训练过程通常采用最大似然估计，即最大化观测到的动作序列在Normalizing Flows模型下的概率。

**关键创新**：该论文最重要的技术创新在于将Normalizing Flows成功应用于视觉运动策略学习。与扩散模型相比，Normalizing Flows具有以下优势：1) 推理速度更快，因为不需要迭代采样；2) 可以直接计算输出的概率密度，从而提供置信度度量；3) 样本效率更高，因为训练过程更加稳定。

**关键设计**：论文中提到了一些关键的架构和训练技巧，包括：1) 使用特定的Normalizing Flows架构，如RealNVP或Glow，以提高模型的表达能力和训练稳定性；2) 采用合适的损失函数，如负对数似然损失，来优化Normalizing Flows模型的参数；3) 使用数据增强技术，如随机裁剪和颜色抖动，来提高模型的泛化能力；4) 通过消融实验验证了这些设计选择的有效性。

## 📊 实验亮点

实验结果表明，Normalizing Flows Policy在四个不同的模拟机器人任务中，性能可与Diffusion Policy相媲美，甚至超越。更重要的是，Normalizing Flows Policy的推理速度比Diffusion Policy快30倍，并且具有更高的样本效率。消融研究验证了关键架构和训练技术的有效性。

## 🎯 应用场景

该研究成果可应用于各种机器人任务，如自主导航、物体抓取、装配等。通过提供快速推理和置信度评估，Normalizing Flows Policy有望提高机器人的自主性和可靠性，使其能够更好地适应复杂和动态的环境。未来，该方法还可以扩展到其他领域，如自动驾驶和医疗机器人。

## 📄 摘要（原文）

> The field of general purpose robotics has recently embraced powerful probabilistic models, such as diffusion models, to model and learn complex behaviors. However, these models often come with significant trade-offs, namely high computational costs for inference and a fundamental inability to quantify output uncertainty. We argue that a model's trustworthiness, a critical factor for reliable, general-purpose robotics, is inherently linked to its ability to provide confidence measures.
>   In this work, we introduce Normalizing Flows Policy, a novel visuomotor policy learning model based on Normalizing Flows. We show that Normalizing Flows are a natural and powerful alternative to diffusion models, providing both a statistically sound measure of confidence and a highly efficient inference process. Through comprehensive experiments across four distinct simulated robotic tasks, we demonstrate that Normalizing Flows Policy achieves performance comparable to, and often surpassing, Diffusion Policy, and it does so not only with improved sample efficiency but also with up to 30 times faster inference. Additionally, our ablation study validates several key architectural and training techniques that enable Normalizing Flows to perform well in this domain.

