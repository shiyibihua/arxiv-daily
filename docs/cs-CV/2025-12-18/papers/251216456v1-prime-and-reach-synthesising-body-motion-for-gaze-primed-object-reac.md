---
layout: default
title: Prime and Reach: Synthesising Body Motion for Gaze-Primed Object Reach
---

# Prime and Reach: Synthesising Body Motion for Gaze-Primed Object Reach

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.16456" class="toolbar-btn" target="_blank">📄 arXiv: 2512.16456v1</a>
  <a href="https://arxiv.org/pdf/2512.16456.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.16456v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.16456v1', 'Prime and Reach: Synthesising Body Motion for Gaze-Primed Object Reach')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Masashi Hatano, Saptarshi Sinha, Jacob Chalk, Wei-Hong Li, Hideo Saito, Dima Damen

**分类**: cs.CV

**发布日期**: 2025-12-18

**备注**: Project Page: https://masashi-hatano.github.io/prime-and-reach/

---

## 💡 一句话要点

**提出基于注视启动的人体运动合成方法，用于模拟拾取/放置物体的自然行为。**

🎯 **匹配领域**: **支柱四：生成式动作 (Generative Motion)**

**关键词**: `人体运动生成` `注视启动` `扩散模型` `人机交互` `目标导向运动`

## 📋 核心要点

1. 现有方法难以生成逼真的人体运动，尤其是在涉及注视启动和目标导向的复杂交互行为时。
2. 本文提出一种基于扩散模型的运动生成方法，利用大规模注视启动数据集进行训练，从而模拟自然的人类运动。
3. 实验表明，该模型在HD-EPIC数据集上取得了显著的启动成功率（60%）和到达成功率（89%），验证了其有效性。

## 📝 摘要（中文）

人体运动生成是一项具有挑战性的任务，旨在创建模仿自然人类行为的逼真运动。本文关注一个经过充分研究的行为：启动一个物体/位置以进行拾取或放置——即，从远处发现一个物体/位置，称为注视启动，然后是接近和到达目标位置的运动。为此，我们首次整理了23.7K个注视启动的人体运动序列，用于从五个公开可用的数据集（即HD-EPIC、MoGaze、HOT3D、ADT和GIMO）到达目标物体位置。我们预训练了一个基于文本条件扩散的运动生成模型，然后在我们整理的序列上，以目标姿势或位置为条件对其进行微调。重要的是，我们通过包括“到达成功”和一个新引入的“启动成功”指标在内的多个指标，评估了生成的运动模仿自然人类运动的能力。在最大的数据集HD-EPIC上，当以目标物体位置为条件时，我们的模型实现了60%的启动成功率和89%的到达成功率。

## 🔬 方法详解

**问题定义**：论文旨在解决人体运动生成中，如何模拟注视启动（gaze-primed）的物体拾取或放置行为的问题。现有方法难以捕捉人类在执行此类任务时的自然运动模式，尤其是在长距离观察和接近目标的过程中，运动的连贯性和目标导向性难以保证。

**核心思路**：论文的核心思路是利用大规模的注视启动人体运动数据集，训练一个条件扩散模型，使其能够根据目标物体的位置或姿势，生成逼真且符合人类行为习惯的运动序列。通过模仿人类在注视目标后接近并与之交互的自然过程，提高生成运动的真实性和实用性。

**技术框架**：整体框架包含以下几个主要步骤：1) 数据收集与整理：从多个公开数据集（HD-EPIC、MoGaze、HOT3D、ADT和GIMO）中收集并整理包含注视信息的运动序列，构建大规模的注视启动数据集。2) 模型预训练：使用文本条件扩散模型进行预训练，学习人体运动的基本模式。3) 模型微调：在整理的注视启动数据集上，以目标物体的位置或姿势为条件，对预训练模型进行微调，使其能够生成与目标相关的运动。4) 运动生成与评估：输入目标物体的位置或姿势，生成相应的运动序列，并使用“到达成功”和“启动成功”等指标进行评估。

**关键创新**：该论文的关键创新在于：1) 首次整理并公开了一个大规模的注视启动人体运动数据集，为相关研究提供了宝贵的数据资源。2) 提出了“启动成功”这一新的评估指标，用于衡量生成的运动是否能够模仿人类在注视目标后的行为。3) 将扩散模型应用于注视启动的人体运动生成，并取得了显著的性能提升。

**关键设计**：论文使用了基于文本条件的扩散模型，具体结构未知。微调阶段，模型以目标物体的位置或姿势作为条件输入。损失函数的设计可能包含运动的平滑性、目标可达性以及注视行为的合理性等多个方面。具体参数设置和网络结构细节在论文中可能没有详细描述，属于未知信息。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16456v1/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16456v1/x2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16456v1/x3.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

该模型在HD-EPIC数据集上取得了显著的成果，在以目标物体位置为条件时，达到了60%的启动成功率和89%的到达成功率。这表明该模型能够有效地模仿人类在注视目标后接近并与之交互的行为，生成的运动更加自然和逼真。

## 🎯 应用场景

该研究成果可应用于虚拟现实、人机交互、机器人控制等领域。例如，可以用于创建更逼真的虚拟角色，使其能够自然地与虚拟环境中的物体进行交互。此外，还可以用于训练机器人执行复杂的任务，例如在仓库中拣选货物或在家庭环境中进行辅助。

## 📄 摘要（原文）

> Human motion generation is a challenging task that aims to create realistic motion imitating natural human behaviour. We focus on the well-studied behaviour of priming an object/location for pick up or put down -- that is, the spotting of an object/location from a distance, known as gaze priming, followed by the motion of approaching and reaching the target location. To that end, we curate, for the first time, 23.7K gaze-primed human motion sequences for reaching target object locations from five publicly available datasets, i.e., HD-EPIC, MoGaze, HOT3D, ADT, and GIMO. We pre-train a text-conditioned diffusion-based motion generation model, then fine-tune it conditioned on goal pose or location, on our curated sequences. Importantly, we evaluate the ability of the generated motion to imitate natural human movement through several metrics, including the 'Reach Success' and a newly introduced 'Prime Success' metric. On the largest dataset, HD-EPIC, our model achieves 60% prime success and 89% reach success when conditioned on the goal object location.

