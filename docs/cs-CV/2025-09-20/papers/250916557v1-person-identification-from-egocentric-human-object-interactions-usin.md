---
layout: default
title: Person Identification from Egocentric Human-Object Interactions using 3D Hand Pose
---

# Person Identification from Egocentric Human-Object Interactions using 3D Hand Pose

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.16557" class="toolbar-btn" target="_blank">📄 arXiv: 2509.16557v1</a>
  <a href="https://arxiv.org/pdf/2509.16557.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.16557v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.16557v1', 'Person Identification from Egocentric Human-Object Interactions using 3D Hand Pose')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Muhammad Hamza, Danish Hamid, Muhammad Tahir Akram

**分类**: cs.CV, cs.ET, cs.HC, cs.LG

**发布日期**: 2025-09-20

**备注**: 21 pages, 8 figures, 7 tables. Preprint of a manuscript submitted to CCF Transactions on Pervasive Computing and Interaction (Springer), currently under review

---

## 💡 一句话要点

**I2S框架：利用3D手部姿态进行人-物交互的用户身份识别**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱五：交互与反应 (Interaction & Reaction)** **支柱六：视频提取与匹配 (Video Extraction)**

**关键词**: `人-物交互识别` `3D手部姿态` `用户身份识别` `增强现实` `特征工程` `深度学习` `轻量级模型`

## 📋 核心要点

1. 现有增强现实辅助技术在人机交互环境中面临用户身份识别的挑战，需要更精准和非侵入式的解决方案。
2. I2S框架通过分析3D手部姿态和人-物交互，实现用户身份的无干扰识别，提升了系统的安全性和个性化体验。
3. 实验结果表明，I2S框架在用户识别方面取得了97.52%的F1分数，模型轻量且推理速度快，适合实时应用。

## 📝 摘要（中文）

本研究提出I2S（Interact2Sign），一个多阶段框架，旨在通过人-物交互识别进行无干扰的用户身份识别，利用以自我为中心的视频中的3D手部姿态分析。I2S利用从3D手部姿态中提取的手工特征，并执行顺序特征增强：首先识别物体类别，然后进行HOI识别，最后进行用户身份识别。对3D手部姿态进行了全面的特征提取和描述过程，将提取的特征组织成语义上有意义的类别：空间、频率、运动学、方向，以及本研究中引入的新型描述符，即手间空间包络（IHSE）。进行了广泛的消融研究，以确定最有效的特征组合。在从ARCTIC和H2O数据集衍生的双手物体操作数据集上评估，最佳配置在用户身份识别方面实现了97.52%的平均F1分数。I2S展示了最先进的性能，同时保持了小于4 MB的轻量级模型大小和0.1秒的快速推理时间。这些特性使所提出的框架非常适合在安全关键的基于AR的系统中进行实时、设备上的身份验证。

## 🔬 方法详解

**问题定义**：论文旨在解决增强现实（AR）环境中，特别是高风险人机交互场景（如飞机驾驶舱、航空航天维护、外科手术）中，如何准确、非侵入式地进行用户身份识别的问题。现有方法可能依赖于繁琐的身份验证流程或侵入式的生物特征识别，影响用户体验和工作效率。

**核心思路**：论文的核心思路是利用用户与物体交互时的3D手部姿态信息，通过分析手部动作、物体类型以及交互模式，来推断用户的身份。这种方法无需用户主动配合，具有非侵入性和自然性的优点。

**技术框架**：I2S框架是一个多阶段流程，首先从以自我为中心的视频中提取3D手部姿态信息。然后，进行顺序特征增强，包括：1) 物体类别识别；2) 人-物交互（HOI）识别；3) 用户身份识别。框架的核心在于对3D手部姿态进行特征提取和描述，并将提取的特征组织成语义上有意义的类别，如空间、频率、运动学、方向等。

**关键创新**：论文的关键创新在于提出了Inter-Hand Spatial Envelope (IHSE) 描述符，用于捕捉双手之间的空间关系。此外，论文还通过消融研究，确定了最有效的特征组合，实现了高性能的用户身份识别。

**关键设计**：论文详细描述了3D手部姿态的特征提取过程，包括空间特征（如手部关键点坐标）、频率特征（如手部运动速度的傅里叶变换）、运动学特征（如关节角度）、方向特征（如手部朝向）以及IHSE。通过消融实验，确定了最佳的特征组合和权重。模型大小被控制在4MB以下，推理时间为0.1秒，保证了实时性。

## 📊 实验亮点

I2S框架在基于ARCTIC和H2O数据集的双手物体操作数据集上进行了评估，实现了97.52%的平均F1分数，超越了现有技术水平。同时，该模型保持了小于4MB的轻量级大小和0.1秒的快速推理时间，使其非常适合在资源受限的设备上进行实时部署。

## 🎯 应用场景

该研究成果可应用于多种增强现实辅助系统，例如在飞机驾驶舱中自动识别飞行员身份并加载个性化设置，在航空航天维护中辅助技术人员进行操作指导，以及在外科手术中验证医护人员身份并提供定制化信息。该技术有助于提高工作效率、减少人为错误，并增强系统的安全性。

## 📄 摘要（原文）

> Human-Object Interaction Recognition (HOIR) and user identification play a crucial role in advancing augmented reality (AR)-based personalized assistive technologies. These systems are increasingly being deployed in high-stakes, human-centric environments such as aircraft cockpits, aerospace maintenance, and surgical procedures. This research introduces I2S (Interact2Sign), a multi stage framework designed for unobtrusive user identification through human object interaction recognition, leveraging 3D hand pose analysis in egocentric videos. I2S utilizes handcrafted features extracted from 3D hand poses and per forms sequential feature augmentation: first identifying the object class, followed by HOI recognition, and ultimately, user identification. A comprehensive feature extraction and description process was carried out for 3D hand poses, organizing the extracted features into semantically meaningful categories: Spatial, Frequency, Kinematic, Orientation, and a novel descriptor introduced in this work, the Inter-Hand Spatial Envelope (IHSE). Extensive ablation studies were conducted to determine the most effective combination of features. The optimal configuration achieved an impressive average F1-score of 97.52% for user identification, evaluated on a bimanual object manipulation dataset derived from the ARCTIC and H2O datasets. I2S demonstrates state-of-the-art performance while maintaining a lightweight model size of under 4 MB and a fast inference time of 0.1 seconds. These characteristics make the proposed framework highly suitable for real-time, on-device authentication in security-critical, AR-based systems.

