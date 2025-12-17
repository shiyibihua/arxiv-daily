---
layout: default
title: FoodLogAthl-218: Constructing a Real-World Food Image Dataset Using Dietary Management Applications
---

# FoodLogAthl-218: Constructing a Real-World Food Image Dataset Using Dietary Management Applications

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.14574" class="toolbar-btn" target="_blank">📄 arXiv: 2512.14574v1</a>
  <a href="https://arxiv.org/pdf/2512.14574.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.14574v1" onclick="toggleFavorite(this, '2512.14574v1', 'FoodLogAthl-218: Constructing a Real-World Food Image Dataset Using Dietary Management Applications')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Mitsuki Watanabe, Sosuke Amano, Kiyoharu Aizawa, Yoko Yamakata

**分类**: cs.CV, cs.MM

**发布日期**: 2025-12-16

**DOI**: [10.1145/3746027.3758276](https://doi.org/10.1145/3746027.3758276)

**🔗 代码/项目**: [HUGGINGFACE](https://huggingface.co/datasets/FoodLog)

---

## 💡 一句话要点

**FoodLogAthl-218：构建基于膳食管理应用采集的真实食物图像数据集**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `食物图像分类` `真实数据集` `膳食管理` `增量学习` `上下文感知` `多模态模型` `计算机视觉`

## 📋 核心要点

1. 现有食物图像数据集依赖网络爬取图像，与用户真实膳食照片存在差异，限制了膳食管理应用的性能。
2. FoodLogAthl-218数据集直接从膳食管理应用收集用户上传的真实照片，更贴近实际应用场景。
3. 论文提出了增量微调和上下文感知分类两个FoodLog特定任务，并使用大型多模态模型进行评估。

## 📝 摘要（中文）

本文提出了FoodLogAthl-218，一个基于膳食管理应用FoodLog Athl收集的真实食物图像数据集。该数据集包含218个食物类别的6925张图像，以及总计14349个边界框。每张图像都附带有丰富的元数据，包括用餐日期和时间、匿名用户ID以及膳食级别的上下文信息。与传统的基于网络爬取的、以预定义类别为导向的数据集不同，该数据集从用户提交的照片开始，然后进行标注，从而产生更大的类内多样性、膳食类型的自然频率分布以及未经滤镜处理的个人使用图像。除了标准的分类基准之外，本文还引入了两个FoodLog特定的任务：一个遵循用户日志时间流的增量微调协议，以及一个上下文感知的分类任务，其中每张图像包含多个菜肴，模型必须利用整体膳食上下文对每个菜肴进行分类。使用大型多模态模型（LMM）对这些任务进行了评估。该数据集已公开发布。

## 🔬 方法详解

**问题定义**：现有食物图像分类数据集主要依赖于网络爬取的图像，这些图像通常经过精心挑选和处理，与用户在日常生活中使用膳食管理应用拍摄的食物照片存在显著差异。这种差异导致在这些数据集上训练的模型在实际应用中表现不佳，无法准确识别用户拍摄的食物。

**核心思路**：本文的核心思路是直接从膳食管理应用中收集用户上传的真实食物照片，构建一个更贴近实际应用场景的数据集。通过这种方式，可以获得具有更大类内多样性、膳食类型的自然频率分布以及未经滤镜处理的图像，从而提高模型在实际应用中的泛化能力。

**技术框架**：该研究主要围绕FoodLogAthl-218数据集的构建和使用展开。数据集构建过程包括从FoodLog Athl应用收集用户上传的食物照片，然后对这些照片进行标注，包括食物类别和边界框。此外，还提供了丰富的元数据，如用餐日期和时间、匿名用户ID以及膳食级别的上下文信息。基于该数据集，提出了两个FoodLog特定的任务：增量微调和上下文感知分类。增量微调旨在模拟用户日志的时间流，逐步更新模型。上下文感知分类则要求模型利用整体膳食上下文对图像中的每个菜肴进行分类。

**关键创新**：该论文的关键创新在于数据集的构建方式。与传统的基于网络爬取的数据集不同，FoodLogAthl-218数据集直接从用户上传的真实照片开始，然后进行标注。这种方式能够更好地反映实际应用场景，并获得更具代表性的数据。此外，提出的增量微调和上下文感知分类任务也更贴近实际应用需求。

**关键设计**：在数据集构建方面，作者注重数据的多样性和真实性，尽量减少人工干预。在实验方面，作者使用了大型多模态模型（LMM）作为基线模型，并针对提出的两个FoodLog特定任务设计了相应的评估指标。具体的参数设置和网络结构等技术细节在论文中没有详细描述，属于模型选择和调优的范畴。

## 📊 实验亮点

论文构建了包含218个食物类别的大型真实食物图像数据集FoodLogAthl-218。此外，论文还提出了两个FoodLog特定的任务：增量微调和上下文感知分类，为后续研究提供了新的基准和方向。虽然论文中没有给出具体的性能数据，但强调了该数据集在实际应用中的优势。

## 🎯 应用场景

该研究成果可直接应用于膳食管理应用中，提升食物图像识别的准确性和鲁棒性，减轻用户手动记录膳食的负担。此外，该数据集也可用于训练更通用的食物图像分类模型，应用于餐饮推荐、营养分析等领域，具有重要的实际价值和广泛的应用前景。

## 📄 摘要（原文）

> Food image classification models are crucial for dietary management applications because they reduce the burden of manual meal logging. However, most publicly available datasets for training such models rely on web-crawled images, which often differ from users' real-world meal photos. In this work, we present FoodLogAthl-218, a food image dataset constructed from real-world meal records collected through the dietary management application FoodLog Athl. The dataset contains 6,925 images across 218 food categories, with a total of 14,349 bounding boxes. Rich metadata, including meal date and time, anonymized user IDs, and meal-level context, accompany each image. Unlike conventional datasets-where a predefined class set guides web-based image collection-our data begins with user-submitted photos, and labels are applied afterward. This yields greater intra-class diversity, a natural frequency distribution of meal types, and casual, unfiltered images intended for personal use rather than public sharing. In addition to (1) a standard classification benchmark, we introduce two FoodLog-specific tasks: (2) an incremental fine-tuning protocol that follows the temporal stream of users' logs, and (3) a context-aware classification task where each image contains multiple dishes, and the model must classify each dish by leveraging the overall meal context. We evaluate these tasks using large multimodal models (LMMs). The dataset is publicly available at https://huggingface.co/datasets/FoodLog/FoodLogAthl-218.

