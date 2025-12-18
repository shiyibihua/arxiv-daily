---
layout: default
title: An Open Benchmark Dataset for GeoAI Foundation Models for Oil Palm Mapping in Indonesia
---

# An Open Benchmark Dataset for GeoAI Foundation Models for Oil Palm Mapping in Indonesia

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.08303" class="toolbar-btn" target="_blank">📄 arXiv: 2509.08303v1</a>
  <a href="https://arxiv.org/pdf/2509.08303.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.08303v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.08303v1', 'An Open Benchmark Dataset for GeoAI Foundation Models for Oil Palm Mapping in Indonesia')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: M. Warizmi Wafiq, Peter Cutter, Ate Poortinga, Daniel Marc G. dela Torre, Karis Tenneson, Vanna Teck, Enikoe Bihari, Chanarun Saisaward, Weraphong Suaruang, Andrea McMahon, Andi Vika Faradiba Muin, Karno B. Batiran, Chairil A, Nurul Qomar, Arya Arismaya Metananda, David Ganz, David Saah

**分类**: cs.CV

**发布日期**: 2025-09-10

---

## 💡 一句话要点

**发布印尼油棕榈测绘GeoAI基础模型开放基准数据集，助力可持续发展。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `油棕榈测绘` `地理空间数据集` `遥感图像分析` `土地覆盖分类` `深度学习` `印尼` `可持续发展` `开放数据`

## 📋 核心要点

1. 印尼油棕榈种植是森林砍伐的主要原因之一，需要更精确的测绘来支持可持续发展和监管。
2. 论文提出了一个开放获取的印尼油棕榈种植园地理空间数据集，包含高质量的专家标注和分层类型学。
3. 该数据集适用于训练和评估传统的卷积神经网络和新型地理空间基础模型，旨在提高土地覆盖类型测绘的准确性。

## 📝 摘要（中文）

本文介绍了一个印尼油棕榈种植园及相关土地覆盖类型的开放获取地理空间数据集。该数据集通过专家标注2020年至2024年的高分辨率卫星图像生成，提供了覆盖不同农业生态区域的、基于多边形的、全覆盖的标注。数据集包含一个分层类型学，区分了油棕榈的种植阶段以及类似的多年生作物。通过多位专家共识和实地验证确保了数据质量。该数据集采用全覆盖数字化方式创建，适用于训练和评估传统卷积神经网络以及新型地理空间基础模型。该数据集以CC-BY许可发布，填补了遥感训练数据的一个关键空白，旨在提高土地覆盖类型测绘的准确性。通过支持对油棕榈扩张的透明监测，该资源有助于实现全球减少森林砍伐的目标，并遵循FAIR数据原则。

## 🔬 方法详解

**问题定义**：论文旨在解决印尼油棕榈种植园精确测绘的问题，现有方法缺乏高质量、大规模、开放获取的标注数据集，限制了遥感图像分析和土地覆盖类型测绘的精度。缺乏统一的标准和分层类型学也使得不同种植阶段和相似作物的区分变得困难。

**核心思路**：论文的核心思路是通过专家标注高分辨率卫星图像，构建一个大规模、高质量、开放获取的油棕榈种植园数据集。通过多位专家共识和实地验证确保数据质量，并采用分层类型学来区分油棕榈的不同种植阶段和相似作物，从而提高测绘精度。

**技术框架**：该数据集的构建流程主要包括以下几个阶段：1) 数据收集：收集2020年至2024年印尼不同农业生态区域的高分辨率卫星图像；2) 专家标注：由领域专家对图像进行多边形标注，标注油棕榈种植园及相关土地覆盖类型；3) 质量控制：通过多位专家共识和实地验证，确保标注的准确性和一致性；4) 数据发布：以CC-BY许可发布数据集，供研究人员和从业者使用。

**关键创新**：该论文的关键创新在于构建了一个大规模、高质量、开放获取的印尼油棕榈种植园地理空间数据集，填补了遥感训练数据的一个关键空白。该数据集采用分层类型学，区分了油棕榈的不同种植阶段和相似作物，提高了测绘精度。此外，数据集的构建过程遵循FAIR数据原则，促进了数据的可查找性、可访问性、互操作性和可重用性。

**关键设计**：数据集采用多边形标注，标注对象包括油棕榈种植园及相关土地覆盖类型。分层类型学包括油棕榈的不同种植阶段（如幼苗期、成熟期）以及与油棕榈相似的多年生作物。质量控制采用多位专家共识和实地验证相结合的方式，确保标注的准确性和一致性。数据集以GeoTIFF和Shapefile等常用格式发布，方便用户使用。

## 📊 实验亮点

该数据集是印尼油棕榈种植园首个大规模、开放获取的地理空间数据集，包含高质量的专家标注和分层类型学。通过在不同农业生态区域进行全覆盖数字化，该数据集适用于训练和评估传统的卷积神经网络和新型地理空间基础模型，有望显著提高土地覆盖类型测绘的准确性。

## 🎯 应用场景

该数据集可广泛应用于油棕榈种植园监测、土地利用规划、森林砍伐评估、可持续农业发展等领域。通过训练和评估遥感图像分析模型，可以实现对油棕榈种植面积和分布的精确测绘，为政府、企业和研究机构提供决策支持，促进可持续发展和环境保护。

## 📄 摘要（原文）

> Oil palm cultivation remains one of the leading causes of deforestation in Indonesia. To better track and address this challenge, detailed and reliable mapping is needed to support sustainability efforts and emerging regulatory frameworks. We present an open-access geospatial dataset of oil palm plantations and related land cover types in Indonesia, produced through expert labeling of high-resolution satellite imagery from 2020 to 2024. The dataset provides polygon-based, wall-to-wall annotations across a range of agro-ecological zones and includes a hierarchical typology that distinguishes oil palm planting stages as well as similar perennial crops. Quality was ensured through multi-interpreter consensus and field validation. The dataset was created using wall-to-wall digitization over large grids, making it suitable for training and benchmarking both conventional convolutional neural networks and newer geospatial foundation models. Released under a CC-BY license, it fills a key gap in training data for remote sensing and aims to improve the accuracy of land cover types mapping. By supporting transparent monitoring of oil palm expansion, the resource contributes to global deforestation reduction goals and follows FAIR data principles.

