---
layout: default
title: ChessMamba: Structure-Aware Interleaving of State Spaces for Change Detection in Remote Sensing Images
---

# ChessMamba: Structure-Aware Interleaving of State Spaces for Change Detection in Remote Sensing Images

<div class="paper-toolbar">
  <div class="toolbar-left">
    <a href="https://arxiv.org/abs/2511.19882" target="_blank" class="toolbar-btn">arXiv: 2511.19882v1</a>
    <a href="https://arxiv.org/pdf/2511.19882.pdf" target="_blank" class="toolbar-btn">PDF</a>
  </div>
  <div class="toolbar-right">
    <button class="toolbar-btn favorite-btn" data-arxiv-id="2511.19882v1" 
            onclick="toggleFavorite(this, '2511.19882v1', 'ChessMamba: Structure-Aware Interleaving of State Spaces for Change Detection in Remote Sensing Images')" title="收藏">
      ☆ 收藏
    </button>
    <button class="toolbar-btn share-btn" onclick="copyLink()" title="复制链接">
      🔗 分享
    </button>
  </div>
</div>


**作者**: Lei Ding, Tong Liu, Xuanguang Liu, Xiangyun Liu, Haitao Guo, Jun Lu

**分类**: cs.CV

**发布日期**: 2025-11-25

---

## 💡 一句话要点

**ChessMamba：一种结构感知的状态空间交错方法，用于遥感图像变化检测**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱三：空间感知 (Perception & SLAM)**

**关键词**: `遥感图像` `变化检测` `状态空间模型` `多时相分析` `结构感知` `特征融合` `深度学习`

## 📋 核心要点

1. 现有基于Transformer或状态空间模型的变化检测方法，在处理多时相遥感图像时，容易破坏局部结构一致性，影响变化定位的准确性。
2. ChessMamba通过棋盘交错和蛇形扫描，将多时相特征整合为统一序列，并利用多扩张卷积进行结构感知融合，从而实现更鲁棒的变化检测。
3. 在二元CD、语义CD和多模态建筑物损伤评估等任务上，ChessMamba均优于现有方法，证明了其有效融合异构特征的能力。

## 📝 摘要（中文）

多时相遥感图像中的变化检测（CD）由于异质性和时空错位，给细粒度识别带来了重大挑战。然而，现有的基于视觉Transformer或状态空间模型的方法通常会破坏时间序列化过程中的局部结构一致性，从而模糊了错位下的判别线索，并阻碍了可靠的变化定位。为了解决这个问题，我们引入了ChessMamba，这是一个结构感知的框架，利用交错的状态空间建模，对多时相输入进行稳健的CD。ChessMamba集成了SpatialMamba编码器和一个轻量级的跨源交互模块，具有两个关键创新：(i) 具有蛇形扫描顺序的棋盘交错，将多时相特征序列化为单个前向传递中的统一序列，从而缩短了交互路径，并能够直接比较以进行准确的变化定位；(ii) 通过多扩张卷积进行结构感知融合，有选择地捕获每个单时相内的中心和角邻域上下文。在包括二元CD、语义CD和多模态建筑物损伤评估在内的三个CD任务上的综合评估表明，ChessMamba有效地融合了异构特征，并且相对于最先进的方法实现了显着的精度提升。

## 🔬 方法详解

**问题定义**：论文旨在解决多时相遥感图像变化检测中，由于异质性和时空错位导致现有方法难以保持局部结构一致性的问题。现有方法，如基于视觉Transformer或状态空间模型的方法，在时间序列化过程中破坏了局部结构，影响了变化定位的准确性。

**核心思路**：论文的核心思路是利用一种结构感知的状态空间交错方法，即ChessMamba，来更好地融合多时相特征，并保持局部结构信息。通过棋盘交错和蛇形扫描，将多时相特征整合为一个统一的序列，从而缩短交互路径，便于直接比较。

**技术框架**：ChessMamba框架主要包含SpatialMamba编码器和一个轻量级的跨源交互模块。SpatialMamba编码器用于提取多时相图像的特征，跨源交互模块则负责融合这些特征。框架的关键步骤包括：1) 使用SpatialMamba提取特征；2) 通过棋盘交错和蛇形扫描将多时相特征序列化；3) 使用多扩张卷积进行结构感知融合。

**关键创新**：论文的关键创新在于提出了棋盘交错和蛇形扫描的序列化方法，以及多扩张卷积的结构感知融合策略。棋盘交错和蛇形扫描能够有效地将多时相特征整合为一个统一的序列，同时保持空间结构信息。多扩张卷积则能够有选择地捕获中心和角邻域上下文，从而更好地融合特征。与现有方法相比，ChessMamba更注重保持局部结构一致性，从而提高了变化检测的准确性。

**关键设计**：论文中，棋盘交错的具体实现方式是按照棋盘格的模式，将不同时相的特征交错排列。蛇形扫描则用于确定特征序列化的顺序，以保证相邻特征在空间上的连续性。多扩张卷积使用了不同的扩张率，以捕获不同尺度的邻域信息。损失函数方面，论文可能采用了交叉熵损失或Dice损失等常用的分割损失函数，具体细节需要在代码中进一步确认。

## 📊 实验亮点

实验结果表明，ChessMamba在二元CD、语义CD和多模态建筑物损伤评估等三个CD任务上均取得了显著的性能提升。例如，在建筑物损伤评估任务中，ChessMamba相较于现有方法，精度提升了X%（具体数值需要在论文中查找）。这些结果证明了ChessMamba在融合异构特征和保持局部结构一致性方面的优势。

## 🎯 应用场景

该研究成果可广泛应用于遥感图像分析领域，例如城市变化监测、自然灾害评估、土地利用变化分析等。通过更准确地检测地物变化，可以为政府决策、环境保护和资源管理提供有力支持，具有重要的实际应用价值和社会意义。

## 📄 摘要（原文）

> Change detection (CD) in multitemporal remote sensing imagery presents significant challenges for fine-grained recognition, owing to heterogeneity and spatiotemporal misalignment. However, existing methodologies based on vision transformers or state-space models typically disrupt local structural consistency during temporal serialization, obscuring discriminative cues under misalignment and hindering reliable change localization. To address this, we introduce ChessMamba, a structure-aware framework leveraging interleaved state-space modeling for robust CD with multi-temporal inputs. ChessMamba integrates a SpatialMamba encoder with a lightweight cross-source interaction module, featuring two key innovations: (i) Chessboard interleaving with snake scanning order, which serializes multi-temporal features into a unified sequence within a single forward pass, thereby shortening interaction paths and enabling direct comparison for accurate change localization; and (ii) Structure-aware fusion via multi-dilated convolutions, selectively capturing center-and-corner neighborhood contexts within each mono-temporal. Comprehensive evaluations on three CD tasks, including binary CD, semantic CD and multimodal building damage assessment, demonstrate that ChessMamba effectively fuses heterogeneous features and achieves substantial accuracy improvements over state-of-the-art methods.The relevant code will be available at: github.com/DingLei14/ChessMamba.

