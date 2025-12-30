---
layout: default
title: "SurgWorld: Learning Surgical Robot Policies from Videos via World Modeling"
---

# SurgWorld: Learning Surgical Robot Policies from Videos via World Modeling

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.23162" class="toolbar-btn" target="_blank">📄 arXiv: 2512.23162v1</a>
  <a href="https://arxiv.org/pdf/2512.23162.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.23162v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.23162v1', 'SurgWorld: Learning Surgical Robot Policies from Videos via World Modeling')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yufan He, Pengfei Guo, Mengya Xu, Zhaoshuo Li, Andriy Myronenko, Dillan Imans, Bingjie Liu, Dongren Yang, Mingxue Gu, Yongnan Ji, Yueming Jin, Ren Zhao, Baiyong Shen, Daguang Xu

**分类**: cs.RO, cs.CV

**发布日期**: 2025-12-29

---

## 💡 一句话要点

**SurgWorld：通过世界建模从视频中学习手术机器人策略**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `手术机器人` `世界模型` `视觉语言动作` `逆动力学` `数据增强`

## 📋 核心要点

1. 手术机器人自主学习面临数据匮乏，尤其是缺乏带精确动作标签的视频数据。
2. 论文提出SurgWorld，一个基于物理AI的世界模型，用于生成逼真的手术视频。
3. 通过逆动力学模型从合成视频推断伪运动学，增强VLA策略训练，提升真实机器人性能。

## 📝 摘要（中文）

数据稀缺是实现完全自主手术机器人的根本障碍。大规模视觉语言动作（VLA）模型通过利用来自不同领域的配对视频动作数据，在家庭和工业操作中表现出令人印象深刻的泛化能力，但手术机器人技术却面临着缺乏包含视觉观察和精确机器人运动学的数据集的问题。相比之下，存在大量的手术视频语料库，但它们缺乏相应的动作标签，从而无法直接应用模仿学习或VLA训练。在这项工作中，我们旨在通过从SurgWorld（一个专为手术物理AI设计的世界模型）中学习策略模型来缓解这个问题。我们策划了手术动作文本对齐（SATA）数据集，其中包含专门针对手术机器人的详细动作描述。然后，我们基于最先进的物理AI世界模型和SATA构建了SurgWorld。它能够生成多样化、可泛化和逼真的手术视频。我们也是第一个使用逆动力学模型从合成手术视频中推断伪运动学，从而生成合成的配对视频动作数据。我们证明，使用这些增强数据训练的手术VLA策略在真实手术机器人平台上显著优于仅在真实演示上训练的模型。我们的方法通过利用大量未标记的手术视频和生成式世界建模，为自主手术技能获取提供了一条可扩展的路径，从而为可泛化和数据高效的手术机器人策略打开了大门。

## 🔬 方法详解

**问题定义**：手术机器人自主学习面临数据稀缺问题，特别是缺乏包含视觉信息和精确机器人运动学信息的配对数据。现有方法难以直接利用大量未标注的手术视频，限制了模仿学习和视觉语言动作模型的应用。

**核心思路**：论文的核心思路是构建一个合成数据生成平台SurgWorld，通过世界模型生成逼真的手术视频，并利用逆动力学模型从视频中推断伪运动学信息，从而创建大量的合成配对视频-动作数据。这样可以克服真实数据稀缺的问题，并用于训练手术机器人的策略模型。

**技术框架**：整体框架包含以下几个主要模块：1) Surgical Action Text Alignment (SATA)数据集的构建，包含手术动作的详细描述；2) 基于SATA和先进物理AI世界模型构建SurgWorld，用于生成手术视频；3) 使用逆动力学模型从合成视频中推断伪运动学信息；4) 使用合成数据训练手术VLA策略；5) 在真实手术机器人平台上进行评估。

**关键创新**：最重要的技术创新点在于利用世界模型和逆动力学模型，从大量未标注的手术视频中生成可用于训练机器人策略的配对视频-动作数据。这避免了对大量真实标注数据的依赖，并为手术机器人自主学习提供了一种可扩展的解决方案。

**关键设计**：SurgWorld基于先进的物理AI世界模型构建，能够生成多样化、可泛化和逼真的手术视频。逆动力学模型用于从视频中推断伪运动学信息，其具体实现细节（例如网络结构、损失函数等）未在摘要中详细说明。SATA数据集的构建是关键，它提供了手术动作的详细描述，用于指导世界模型的生成过程。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.23162v1/x2.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.23162v1/x3.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.23162v1/x4.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

论文通过实验证明，使用SurgWorld生成的合成数据训练的手术VLA策略，在真实手术机器人平台上显著优于仅在真实演示上训练的模型。具体的性能数据和提升幅度未在摘要中给出，但强调了合成数据在提升模型泛化能力和性能方面的有效性。

## 🎯 应用场景

该研究成果可应用于手术机器人的自主技能学习，降低对人工示教的依赖，提高手术效率和安全性。通过SurgWorld生成的大量合成数据，可以加速手术机器人在各种复杂手术场景中的应用，并为个性化手术方案的制定提供支持。未来，该技术有望推广到其他机器人操作领域，例如工业机器人、服务机器人等。

## 📄 摘要（原文）

> Data scarcity remains a fundamental barrier to achieving fully autonomous surgical robots. While large scale vision language action (VLA) models have shown impressive generalization in household and industrial manipulation by leveraging paired video action data from diverse domains, surgical robotics suffers from the paucity of datasets that include both visual observations and accurate robot kinematics. In contrast, vast corpora of surgical videos exist, but they lack corresponding action labels, preventing direct application of imitation learning or VLA training. In this work, we aim to alleviate this problem by learning policy models from SurgWorld, a world model designed for surgical physical AI. We curated the Surgical Action Text Alignment (SATA) dataset with detailed action description specifically for surgical robots. Then we built SurgeWorld based on the most advanced physical AI world model and SATA. It's able to generate diverse, generalizable and realistic surgery videos. We are also the first to use an inverse dynamics model to infer pseudokinematics from synthetic surgical videos, producing synthetic paired video action data. We demonstrate that a surgical VLA policy trained with these augmented data significantly outperforms models trained only on real demonstrations on a real surgical robot platform. Our approach offers a scalable path toward autonomous surgical skill acquisition by leveraging the abundance of unlabeled surgical video and generative world modeling, thus opening the door to generalizable and data efficient surgical robot policies.

