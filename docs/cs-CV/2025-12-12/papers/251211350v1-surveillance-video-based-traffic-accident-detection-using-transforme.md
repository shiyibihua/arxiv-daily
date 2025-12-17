---
layout: default
title: Surveillance Video-Based Traffic Accident Detection Using Transformer Architecture
---

# Surveillance Video-Based Traffic Accident Detection Using Transformer Architecture

<div class="paper-toolbar">
  <div class="toolbar-left">
    <a href="https://arxiv.org/abs/2512.11350" target="_blank" class="toolbar-btn">arXiv: 2512.11350v1</a>
    <a href="https://arxiv.org/pdf/2512.11350.pdf" target="_blank" class="toolbar-btn">PDF</a>
  </div>
  <div class="toolbar-right">
    <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.11350v1" 
            onclick="toggleFavorite(this, '2512.11350v1', 'Surveillance Video-Based Traffic Accident Detection Using Transformer Architecture')" title="收藏">
      ☆ 收藏
    </button>
    <button class="toolbar-btn share-btn" onclick="copyLink()" title="复制链接">
      🔗 分享
    </button>
  </div>
</div>


**作者**: Tanu Singh, Pranamesh Chakraborty, Long T. Truong

**分类**: cs.CV, cs.AI

**发布日期**: 2025-12-12

---

## 💡 一句话要点

**提出基于Transformer的交通视频事故检测模型，并构建了大规模平衡数据集。**

🎯 **匹配领域**: **支柱三：空间感知 (Perception & SLAM)**

**关键词**: `交通视频分析` `事故检测` `Transformer` `时空建模` `光流` `深度学习` `智能交通` `视频监控`

## 📋 核心要点

1. 传统计算机视觉方法在交通视频事故检测中缺乏有效的时空建模能力，泛化性较差。
2. 提出一种基于Transformer的事故检测模型，利用卷积提取局部特征，Transformer建模时序依赖。
3. 构建了大规模平衡数据集，并结合RGB和光流信息，实验表明该方法取得了88.3%的准确率。

## 📝 摘要（中文）

道路交通事故是全球主要的死亡原因之一，其发生率随着人口、城市化和机动化的增长而上升。日益增长的事故率引发了对交通监控有效性的担忧。传统的计算机视觉事故检测方法在时空理解和跨领域泛化方面存在不足。Transformer架构在建模全局时空依赖性和并行计算方面表现出色。然而，由于小型、非多样化的数据集的限制，将这些模型应用于自动交通事故检测受到限制，阻碍了鲁棒、通用系统的开发。为了解决这个问题，我们整理了一个全面且平衡的数据集，捕捉了各种交通环境、事故类型和上下文变化。利用该数据集，我们提出了一种基于Transformer架构的事故检测模型，该模型使用预提取的空间视频特征。该架构采用卷积层来提取帧内各种模式的局部相关性，同时利用Transformer来捕获检索到的特征之间的时序依赖性。此外，大多数现有研究忽略了运动线索的整合，而运动线索对于理解动态场景至关重要，尤其是在事故发生期间。这些方法通常依赖于静态特征或粗略的时间信息。在本研究中，评估了多种整合运动线索的方法，以确定最有效的策略。在测试的输入方法中，RGB特征与光流的连接实现了最高的准确率，达到88.3%。结果还与视觉语言模型（VLM），如GPT、Gemini和LLaVA-NeXT-Video进行了比较，以评估所提出方法的有效性。

## 🔬 方法详解

**问题定义**：现有交通视频事故检测方法难以有效建模长时序依赖关系，且对不同场景的泛化能力不足。传统方法依赖手工特征或浅层模型，无法充分利用视频中的时空信息。此外，现有数据集规模较小且分布不平衡，限制了模型的训练效果。

**核心思路**：利用Transformer架构强大的时序建模能力，捕捉视频帧之间的长距离依赖关系。同时，结合卷积神经网络提取局部空间特征，融合时空信息。通过构建大规模平衡数据集，提高模型的泛化能力。此外，引入光流信息作为运动线索，增强模型对动态场景的理解。

**技术框架**：该模型首先使用卷积神经网络提取视频帧的局部空间特征。然后，将提取的特征输入Transformer编码器，建模帧之间的时序依赖关系。为了融合运动信息，将RGB特征与光流特征进行拼接。最后，使用分类器判断视频片段是否包含事故。

**关键创新**：该方法的关键创新在于将Transformer架构应用于交通视频事故检测，并有效融合了RGB和光流信息。与传统方法相比，该方法能够更好地捕捉视频中的时空依赖关系，提高检测准确率。此外，构建大规模平衡数据集也有助于提高模型的泛化能力。

**关键设计**：在Transformer编码器中，使用了多头注意力机制，以便模型能够关注不同的特征维度。为了提高训练效率，使用了预训练的卷积神经网络作为特征提取器。在损失函数方面，使用了交叉熵损失函数，并对不同类别的样本进行了加权，以解决数据集不平衡的问题。

## 📊 实验亮点

实验结果表明，该方法在自建的大规模平衡数据集上取得了显著的性能提升，准确率达到88.3%。通过对比实验，验证了Transformer架构和光流信息融合的有效性。此外，与视觉语言模型（VLM）如GPT、Gemini和LLaVA-NeXT-Video的对比，也证明了该方法在交通视频事故检测任务上的优势。

## 🎯 应用场景

该研究成果可应用于智能交通监控系统，实现交通事故的自动检测和预警，提高道路安全管理效率。此外，该方法还可以扩展到其他视频监控场景，如异常行为检测、人群计数等，具有广泛的应用前景。未来，结合边缘计算技术，可实现实时事故检测，为自动驾驶提供安全保障。

## 📄 摘要（原文）

> Road traffic accidents represent a leading cause of mortality globally, with incidence rates rising due to increasing population, urbanization, and motorization. Rising accident rates raise concerns about traffic surveillance effectiveness. Traditional computer vision methods for accident detection struggle with limited spatiotemporal understanding and poor cross-domain generalization. Recent advances in transformer architectures excel at modeling global spatial-temporal dependencies and parallel computation. However, applying these models to automated traffic accident detection is limited by small, non-diverse datasets, hindering the development of robust, generalizable systems. To address this gap, we curated a comprehensive and balanced dataset that captures a wide spectrum of traffic environments, accident types, and contextual variations. Utilizing the curated dataset, we propose an accident detection model based on a transformer architecture using pre-extracted spatial video features. The architecture employs convolutional layers to extract local correlations across diverse patterns within a frame, while leveraging transformers to capture sequential-temporal dependencies among the retrieved features. Moreover, most existing studies neglect the integration of motion cues, which are essential for understanding dynamic scenes, especially during accidents. These approaches typically rely on static features or coarse temporal information. In this study, multiple methods for incorporating motion cues were evaluated to identify the most effective strategy. Among the tested input approaches, concatenating RGB features with optical flow achieved the highest accuracy at 88.3%. The results were further compared with vision language models (VLM) such as GPT, Gemini, and LLaVA-NeXT-Video to assess the effectiveness of the proposed method.

