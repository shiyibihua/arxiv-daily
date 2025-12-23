---
layout: default
title: Spatiotemporal Contrastive Learning for Cross-View Video Localization in Unstructured Off-road Terrains
---

# Spatiotemporal Contrastive Learning for Cross-View Video Localization in Unstructured Off-road Terrains

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.05250" class="toolbar-btn" target="_blank">📄 arXiv: 2506.05250v1</a>
  <a href="https://arxiv.org/pdf/2506.05250.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.05250v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.05250v1', 'Spatiotemporal Contrastive Learning for Cross-View Video Localization in Unstructured Off-road Terrains')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zhiyun Deng, Dongmyeong Lee, Amanda Adkins, Jesse Quattrociocchi, Christian Ellis, Joydeep Biswas

**分类**: cs.CV, cs.RO

**发布日期**: 2025-06-05

---

## 💡 一句话要点

**提出MoViX以解决GPS缺失下的越野视频定位问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱八：物理动画 (Physics-based Animation)**

**关键词**: `越野定位` `自监督学习` `跨视角匹配` `多假设跟踪` `计算机视觉`

## 📋 核心要点

1. 现有方法在GPS缺失的越野环境中，因重复植被和季节变化导致的感知模糊性，定位精度受到严重影响。
2. 本文提出MoViX框架，通过自监督学习实现视角和季节不变的表示，增强方向感知和样本选择策略。
3. 在TartanDrive 2.0数据集上，MoViX在未见区域内93%的时间定位误差在25米以内，100%在50米以内，超越了现有基线。

## 📝 摘要（中文）

在GPS无法使用的越野环境中，3自由度定位面临重复植被和非结构化地形带来的感知模糊性，以及季节变化导致场景外观显著改变的问题。为此，本文提出了MoViX，一个自监督的跨视角视频定位框架，旨在学习视角和季节不变的表示，同时保持方向感知以实现准确定位。MoViX采用姿态依赖的正样本采样策略和时间对齐的困难负样本挖掘，增强方向区分能力。实验表明，MoViX在未见区域的定位精度显著优于现有方法。

## 🔬 方法详解

**问题定义**：本文旨在解决在GPS缺失的越野环境中，因重复植被和季节变化导致的3自由度定位问题。现有方法在这些条件下表现不佳，难以实现准确定位。

**核心思路**：MoViX框架通过自监督学习，学习视角和季节不变的表示，同时保持方向感知。采用姿态依赖的正样本采样和时间对齐的困难负样本挖掘，增强方向区分能力，避免依赖季节线索。

**技术框架**：MoViX的整体架构包括一个运动信息驱动的帧采样器、轻量级的时间聚合器和一个学习的跨视角匹配模块。该框架在推理阶段结合Monte Carlo定位方法，进行多假设跟踪。

**关键创新**：最重要的创新在于引入了姿态依赖的正样本采样和时间对齐的困难负样本挖掘策略，这与传统方法相比，显著提升了方向感知和定位精度。

**关键设计**：在参数设置上，采用了熵引导的温度缩放方法，以增强多假设跟踪的鲁棒性。网络结构上，轻量级的时间聚合器强调几何对齐的观测，降低模糊样本的权重。

## 📊 实验亮点

在TartanDrive 2.0数据集上，MoViX在未见区域内93%的时间定位误差在25米以内，100%在50米以内，显著优于现有基线方法，且无需针对特定环境进行调优。这一结果展示了其在复杂环境下的强大适应性和准确性。

## 🎯 应用场景

该研究的潜在应用领域包括自动驾驶、无人机导航和机器人探索等场景，尤其是在GPS信号弱或缺失的环境中。通过提高越野环境下的定位精度，MoViX能够为自主系统提供更可靠的导航能力，进而推动相关技术的发展与应用。

## 📄 摘要（原文）

> Robust cross-view 3-DoF localization in GPS-denied, off-road environments remains challenging due to (1) perceptual ambiguities from repetitive vegetation and unstructured terrain, and (2) seasonal shifts that significantly alter scene appearance, hindering alignment with outdated satellite imagery. To address this, we introduce MoViX, a self-supervised cross-view video localization framework that learns viewpoint- and season-invariant representations while preserving directional awareness essential for accurate localization. MoViX employs a pose-dependent positive sampling strategy to enhance directional discrimination and temporally aligned hard negative mining to discourage shortcut learning from seasonal cues. A motion-informed frame sampler selects spatially diverse frames, and a lightweight temporal aggregator emphasizes geometrically aligned observations while downweighting ambiguous ones. At inference, MoViX runs within a Monte Carlo Localization framework, using a learned cross-view matching module in place of handcrafted models. Entropy-guided temperature scaling enables robust multi-hypothesis tracking and confident convergence under visual ambiguity. We evaluate MoViX on the TartanDrive 2.0 dataset, training on under 30 minutes of data and testing over 12.29 km. Despite outdated satellite imagery, MoViX localizes within 25 meters of ground truth 93% of the time, and within 50 meters 100% of the time in unseen regions, outperforming state-of-the-art baselines without environment-specific tuning. We further demonstrate generalization on a real-world off-road dataset from a geographically distinct site with a different robot platform.

