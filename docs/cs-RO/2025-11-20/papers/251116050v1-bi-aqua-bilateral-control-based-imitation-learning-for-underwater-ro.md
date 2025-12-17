---
layout: default
title: Bi-AQUA: Bilateral Control-Based Imitation Learning for Underwater Robot Arms via Lighting-Aware Action Chunking with Transformers
---

# Bi-AQUA: Bilateral Control-Based Imitation Learning for Underwater Robot Arms via Lighting-Aware Action Chunking with Transformers

<div class="paper-toolbar">
  <div class="toolbar-left">
    <a href="https://arxiv.org/abs/2511.16050" target="_blank" class="toolbar-btn">arXiv: 2511.16050v1</a>
    <a href="https://arxiv.org/pdf/2511.16050.pdf" target="_blank" class="toolbar-btn">PDF</a>
  </div>
  <div class="toolbar-right">
    <button class="toolbar-btn favorite-btn" data-arxiv-id="2511.16050v1" 
            onclick="toggleFavorite(this, '2511.16050v1', 'Bi-AQUA: Bilateral Control-Based Imitation Learning for Underwater Robot Arms via Lighting-Aware Action Chunking with Transformers')" title="收藏">
      ☆ 收藏
    </button>
    <button class="toolbar-btn share-btn" onclick="copyLink()" title="复制链接">
      🔗 分享
    </button>
  </div>
</div>


**作者**: Takeru Tsunoori, Masato Kobayashi, Yuki Uranishi

**分类**: cs.RO

**发布日期**: 2025-11-20

**🔗 代码/项目**: [PROJECT_PAGE](https://mertcookimg.github.io/bi-aqua)

---

## 💡 一句话要点

**Bi-AQUA：基于双边控制的水下机器人臂光照感知模仿学习框架**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `水下机器人` `模仿学习` `双边控制` `光照感知` `Transformer`

## 📋 核心要点

1. 水下机器人操作受限于极端光照变化、颜色失真和低能见度，传统方法难以适应。
2. Bi-AQUA提出了一种分层光照适应机制，包括光照编码器、FiLM调制和光照token，以增强视觉特征的鲁棒性。
3. 实验表明，Bi-AQUA在真实水下环境中显著优于基线方法，验证了光照感知组件的有效性。

## 📝 摘要（中文）

水下机器人操作面临着极端的光照变化、颜色失真和能见度降低等根本性挑战。我们提出了Bi-AQUA，这是第一个基于双边控制的水下机器人臂模仿学习框架，它集成了光照感知的视觉处理。Bi-AQUA采用分层三级光照适应机制：一个光照编码器，从RGB图像中提取光照表示，无需手动标注，并通过模仿目标进行隐式监督；视觉骨干特征的FiLM调制，用于自适应的、光照感知的特征提取；以及添加到Transformer编码器输入的显式光照token，用于任务感知的条件控制。在各种静态和动态光照条件下进行的真实水下拾取和放置任务的实验表明，Bi-AQUA实现了稳健的性能，并且显著优于没有光照建模的双边基线。消融研究进一步证实了所有三个光照感知组件都至关重要。这项工作桥接了陆地双边控制的模仿学习和水下操作，从而能够在具有挑战性的海洋环境中实现力敏感的自主操作。

## 🔬 方法详解

**问题定义**：水下机器人操作任务中，光照变化是主要挑战，导致视觉感知困难，进而影响控制精度。现有方法通常忽略或简化光照影响，导致在复杂光照条件下性能下降。论文旨在解决水下机器人臂在不同光照条件下的稳定操作问题。

**核心思路**：论文的核心思路是通过模仿学习，学习人类专家在水下环境中的操作策略，并引入光照感知机制，使机器人能够适应不同的光照条件。通过光照编码器提取光照特征，并利用FiLM调制和光照token将光照信息融入视觉特征中，从而提高机器人对光照变化的鲁棒性。

**技术框架**：Bi-AQUA框架包含三个主要模块：1) 光照编码器：从RGB图像中提取光照表示；2) 光照感知的视觉骨干网络：利用FiLM调制将光照信息融入视觉特征；3) Transformer编码器：将视觉特征和光照token作为输入，预测机器人动作。整个框架通过模仿学习进行训练，目标是最小化机器人动作与专家动作之间的差异。

**关键创新**：论文的关键创新在于提出了一个端到端的光照感知模仿学习框架，能够显式地建模光照信息，并将其融入视觉特征中。这种方法无需手动标注光照信息，而是通过模仿学习目标进行隐式监督，从而提高了框架的实用性和泛化能力。此外，分层光照适应机制能够有效地提取和利用光照信息，从而提高了机器人在不同光照条件下的操作性能。

**关键设计**：光照编码器采用卷积神经网络，通过最小化重构误差进行训练。FiLM调制通过线性变换调整视觉骨干网络的特征，使其适应不同的光照条件。光照token是一个可学习的向量，添加到Transformer编码器的输入中，用于任务感知的条件控制。损失函数采用L1损失，用于衡量机器人动作与专家动作之间的差异。

## 📊 实验亮点

Bi-AQUA在真实水下拾取和放置任务中表现出色，显著优于没有光照建模的基线方法。消融实验表明，光照编码器、FiLM调制和光照token三个光照感知组件都对性能提升至关重要。具体性能数据（例如成功率、操作时间等）可在论文原文中找到。

## 🎯 应用场景

该研究成果可应用于水下考古、海洋资源勘探、水下设备维护等领域。通过提高水下机器人的自主操作能力，可以降低人工操作的风险和成本，提高工作效率。未来，该技术有望扩展到其他光照条件恶劣的环境，如深海、矿井等。

## 📄 摘要（原文）

> Underwater robotic manipulation is fundamentally challenged by extreme lighting variations, color distortion, and reduced visibility. We introduce Bi-AQUA, the first underwater bilateral control-based imitation learning framework that integrates lighting-aware visual processing for underwater robot arms. Bi-AQUA employs a hierarchical three-level lighting adaptation mechanism: a Lighting Encoder that extracts lighting representations from RGB images without manual annotation and is implicitly supervised by the imitation objective, FiLM modulation of visual backbone features for adaptive, lighting-aware feature extraction, and an explicit lighting token added to the transformer encoder input for task-aware conditioning. Experiments on a real-world underwater pick-and-place task under diverse static and dynamic lighting conditions show that Bi-AQUA achieves robust performance and substantially outperforms a bilateral baseline without lighting modeling. Ablation studies further confirm that all three lighting-aware components are critical. This work bridges terrestrial bilateral control-based imitation learning and underwater manipulation, enabling force-sensitive autonomous operation in challenging marine environments. For additional material, please check: https://mertcookimg.github.io/bi-aqua

