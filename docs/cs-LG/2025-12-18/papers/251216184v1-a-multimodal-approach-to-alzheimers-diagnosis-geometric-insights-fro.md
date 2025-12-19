---
layout: default
title: A Multimodal Approach to Alzheimer's Diagnosis: Geometric Insights from Cube Copying and Cognitive Assessments
---

# A Multimodal Approach to Alzheimer's Diagnosis: Geometric Insights from Cube Copying and Cognitive Assessments

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.16184" class="toolbar-btn" target="_blank">📄 arXiv: 2512.16184v1</a>
  <a href="https://arxiv.org/pdf/2512.16184.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.16184v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.16184v1', 'A Multimodal Approach to Alzheimer\'s Diagnosis: Geometric Insights from Cube Copying and Cognitive Assessments')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jaeho Yang, Kijung Yoon

**分类**: cs.LG

**发布日期**: 2025-12-18

---

## 💡 一句话要点

**提出基于图神经网络的多模态融合方法，用于阿尔茨海默病早期诊断。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `阿尔茨海默病` `早期诊断` `图神经网络` `多模态融合` `立方体复制` `几何特征` `拓扑结构`

## 📋 核心要点

1. 阿尔茨海默病早期诊断困难，传统方法依赖复杂且昂贵的检测手段，缺乏便捷性。
2. 将手绘立方体转化为图结构，提取几何和拓扑特征，结合人口统计学信息进行多模态融合。
3. 实验表明，基于图的表示优于像素模型，多模态融合进一步提升性能，并具有良好的可解释性。

## 📝 摘要（中文）

阿尔茨海默病(AD)的早期且易于获得的检测仍然是一项关键的临床挑战，而立方体复制任务提供了一种简单但信息丰富的视觉空间功能评估方法。本研究提出了一种多模态框架，该框架将手绘立方体草图转换为图结构表示，以捕获几何和拓扑属性，并将这些特征与人口统计信息和神经心理测试(NPT)分数相结合，用于AD分类。立方体图被建模为图，其节点特征编码空间坐标、基于局部图元的拓扑结构和角度几何，这些特征使用图神经网络进行处理，并在后期融合模型中与年龄、教育程度和NPT特征融合。实验结果表明，基于图的表示提供了强大的单模态基线，并且大大优于基于像素的卷积模型，而多模态集成进一步提高了性能和对类不平衡的鲁棒性。基于SHAP的可解释性分析将特定的图元基序和几何扭曲识别为关键预测因子，这与AD中立方体图的紊乱的临床观察结果密切相关。总之，这些结果确立了基于图的立方体复制分析作为一种可解释、非侵入性和可扩展的阿尔茨海默病筛查方法。

## 🔬 方法详解

**问题定义**：阿尔茨海默病的早期诊断是临床上的一个难题。现有的诊断方法，例如脑部扫描和认知测试，通常成本高昂且耗时，难以大规模应用。手绘立方体复制任务虽然简单，但其蕴含的视觉空间信息尚未被充分利用，缺乏有效的量化分析方法。

**核心思路**：本研究的核心在于将手绘立方体图转化为图结构数据，从而能够利用图神经网络(GNN)提取其几何和拓扑特征。这种方法能够更有效地捕捉立方体图中的空间关系和结构信息，克服了传统像素级方法的局限性。同时，结合人口统计学信息和神经心理测试分数，实现多模态融合，提升诊断准确率。

**技术框架**：该框架主要包含以下几个阶段：1) **数据预处理**：将手绘立方体图转换为数字图像，并提取图像中的线条和节点。2) **图构建**：将提取的线条和节点构建成图结构，其中节点表示立方体的顶点，边表示立方体的棱。3) **特征提取**：提取节点的空间坐标、局部图元拓扑结构和角度几何等特征。4) **图神经网络处理**：使用GNN对图结构数据进行学习，提取高级特征表示。5) **多模态融合**：将GNN提取的特征与人口统计学信息和神经心理测试分数进行融合。6) **分类**：使用分类器对融合后的特征进行分类，判断患者是否患有阿尔茨海默病。

**关键创新**：该研究的关键创新在于：1) 将手绘立方体图转化为图结构数据，并利用GNN进行特征提取。2) 提出了一种多模态融合框架，结合了图像特征、人口统计学信息和神经心理测试分数。3) 通过SHAP分析，揭示了图元基序和几何扭曲等关键预测因子，提高了模型的可解释性。

**关键设计**：在图构建阶段，节点特征包括空间坐标、局部图元拓扑结构（例如，节点周围的三角形、四边形等）和角度几何（例如，节点连接的边的角度）。GNN采用多层图卷积网络，损失函数采用交叉熵损失函数。多模态融合采用后期融合策略，即将不同模态的特征进行拼接，然后输入到分类器中。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16184v1/Figure1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16184v1/Figure2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16184v1/Figure3.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

实验结果表明，基于图的表示方法在单模态情况下就优于基于像素的卷积模型。多模态融合后，性能进一步提升，并且对类不平衡问题具有更强的鲁棒性。SHAP分析揭示了特定的图元基序和几何扭曲是关键的预测因子，与临床观察结果一致，验证了该方法的有效性和可解释性。

## 🎯 应用场景

该研究成果可应用于阿尔茨海默病的早期筛查和诊断，尤其适用于资源有限的社区和医疗机构。通过简单的手绘立方体复制任务，结合智能算法分析，可以实现快速、便捷、低成本的初步诊断，为患者争取宝贵的治疗时间。未来，该方法有望推广到其他神经退行性疾病的辅助诊断中。

## 📄 摘要（原文）

> Early and accessible detection of Alzheimer's disease (AD) remains a critical clinical challenge, and cube-copying tasks offer a simple yet informative assessment of visuospatial function. This work proposes a multimodal framework that converts hand-drawn cube sketches into graph-structured representations capturing geometric and topological properties, and integrates these features with demographic information and neuropsychological test (NPT) scores for AD classification. Cube drawings are modeled as graphs with node features encoding spatial coordinates, local graphlet-based topology, and angular geometry, which are processed using graph neural networks and fused with age, education, and NPT features in a late-fusion model. Experimental results show that graph-based representations provide a strong unimodal baseline and substantially outperform pixel-based convolutional models, while multimodal integration further improves performance and robustness to class imbalance. SHAP-based interpretability analysis identifies specific graphlet motifs and geometric distortions as key predictors, closely aligning with clinical observations of disorganized cube drawings in AD. Together, these results establish graph-based analysis of cube copying as an interpretable, non-invasive, and scalable approach for Alzheimer's disease screening.

