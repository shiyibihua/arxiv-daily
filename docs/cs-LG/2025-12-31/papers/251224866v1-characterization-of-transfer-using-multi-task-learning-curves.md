---
layout: default
title: Characterization of Transfer Using Multi-task Learning Curves
---

# Characterization of Transfer Using Multi-task Learning Curves

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.24866" class="toolbar-btn" target="_blank">📄 arXiv: 2512.24866v1</a>
  <a href="https://arxiv.org/pdf/2512.24866.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.24866v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.24866v1', 'Characterization of Transfer Using Multi-task Learning Curves')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: András Millinghoffer, Bence Bolgár, Péter Antal

**分类**: cs.LG

**发布日期**: 2025-12-31

---

## 💡 一句话要点

**提出基于多任务学习曲线的迁移学习表征方法，用于刻画数据集扰动下的迁移效应。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `迁移学习` `多任务学习` `学习曲线` `数据集扰动` `任务亲和性`

## 📋 核心要点

1. 现有方法主要通过梯度更新扰动模型来研究迁移学习，忽略了数据集扰动带来的影响。
2. 论文提出利用多任务学习曲线，通过改变样本数量来扰动数据集，从而更本质地刻画迁移效应。
3. 实验结果表明，该方法能更好地捕捉多任务学习效果，并能有效区分基础模型中的成对和上下文迁移效应。

## 📝 摘要（中文）

迁移效应在训练过程中（使用固定数据集）和归纳推理过程中（使用累积数据）均会显现。本文假设，通过包含更多样本来扰动数据集，而不是通过梯度更新来扰动模型，能够提供对迁移效应的互补且更根本的表征。为了捕捉这种现象，我们使用多任务学习曲线对迁移效应进行定量建模，该曲线近似于不同样本大小下的归纳性能。我们描述了一种有效的方法来近似多任务学习曲线，类似于训练期间应用的任务亲和性分组方法。我们比较了迁移的统计和计算方法，表明前者计算成本高得多，但功率更好，适用性更广。使用基准药物-靶标相互作用数据集进行评估。我们的结果表明，学习曲线可以更好地捕捉多任务学习的效果，并且它们的多任务扩展可以描绘基础模型中的成对和上下文迁移效应。

## 🔬 方法详解

**问题定义**：现有研究迁移学习的方法主要集中在模型参数的调整和优化上，例如通过梯度更新来适应新的任务。然而，数据集本身的变化，例如样本数量的增加，也会对迁移学习的效果产生显著影响。现有方法缺乏对这种数据集扰动影响的有效建模和分析，限制了我们对迁移学习本质的理解。

**核心思路**：本文的核心思路是利用多任务学习曲线来刻画数据集扰动下的迁移效应。具体来说，通过构建不同样本数量下的学习曲线，可以观察到模型在不同数据规模下的性能变化。这些学习曲线能够反映出任务之间的相关性和迁移潜力，从而为迁移学习提供更全面的表征。这种方法将数据集的变化视为一种扰动，并分析其对模型性能的影响，从而提供了一种互补的视角。

**技术框架**：该方法主要包含以下几个步骤：1) 构建多任务学习场景，即定义多个相关的学习任务。2) 对于每个任务，构建不同样本数量下的数据集。3) 在每个数据集上训练模型，并记录模型的性能指标（例如准确率、损失值）。4) 将模型的性能指标与样本数量绘制成学习曲线。5) 分析学习曲线的形状、趋势和相互关系，从而推断任务之间的迁移效应。该框架类似于任务亲和性分组方法，但应用于学习曲线而非模型训练。

**关键创新**：该方法的关键创新在于将学习曲线的概念引入到迁移学习的分析中。传统的迁移学习研究主要关注模型参数的调整，而忽略了数据集本身的影响。通过分析学习曲线，可以更全面地了解迁移学习的本质，并为迁移学习策略的设计提供更有效的指导。此外，该方法还提供了一种定量分析迁移效应的手段，可以用于比较不同任务之间的相关性和迁移潜力。

**关键设计**：在构建学习曲线时，需要选择合适的性能指标来衡量模型的性能。常用的性能指标包括准确率、精确率、召回率、F1值等。此外，还需要选择合适的样本数量范围，以确保学习曲线能够充分反映模型的性能变化。在分析学习曲线时，可以采用统计方法或机器学习方法来提取关键特征，例如学习曲线的斜率、截距、面积等。这些特征可以用于描述任务之间的相关性和迁移潜力。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.24866v1/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.24866v1/kiba244_tasks__10f_comp-vs-scaff.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.24866v1/kiba244_tasks__10f_scaff_single-vs-all.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

论文使用药物-靶标相互作用数据集进行评估，结果表明，学习曲线能够更好地捕捉多任务学习的效果，并且它们的多任务扩展可以描绘基础模型中的成对和上下文迁移效应。该方法能够有效区分不同任务之间的相关性和迁移潜力，为迁移学习策略的设计提供了更有效的指导。

## 🎯 应用场景

该研究成果可应用于药物发现、图像识别、自然语言处理等领域。例如，在药物发现中，可以利用该方法分析不同靶标之间的相关性，从而加速新药的研发过程。在图像识别中，可以利用该方法分析不同图像类别之间的相关性，从而提高图像识别的准确率。此外，该方法还可以用于评估预训练模型在不同下游任务上的迁移能力，为模型选择和微调提供指导。

## 📄 摘要（原文）

> Transfer effects manifest themselves both during training using a fixed data set and in inductive inference using accumulating data. We hypothesize that perturbing the data set by including more samples, instead of perturbing the model by gradient updates, provides a complementary and more fundamental characterization of transfer effects. To capture this phenomenon, we quantitatively model transfer effects using multi-task learning curves approximating the inductive performance over varying sample sizes. We describe an efficient method to approximate multi-task learning curves analogous to the Task Affinity Grouping method applied during training. We compare the statistical and computational approaches to transfer, which indicates considerably higher compute costs for the previous but better power and broader applicability. Evaluations are performed using a benchmark drug-target interaction data set. Our results show that learning curves can better capture the effects of multi-task learning and their multi-task extensions can delineate pairwise and contextual transfer effects in foundation models.

