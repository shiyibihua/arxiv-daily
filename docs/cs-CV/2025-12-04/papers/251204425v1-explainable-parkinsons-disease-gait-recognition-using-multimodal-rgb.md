---
layout: default
title: Explainable Parkinsons Disease Gait Recognition Using Multimodal RGB-D Fusion and Large Language Models
---

# Explainable Parkinsons Disease Gait Recognition Using Multimodal RGB-D Fusion and Large Language Models

<div class="paper-toolbar">
  <div class="toolbar-left">
    <a href="https://arxiv.org/abs/2512.04425" target="_blank" class="toolbar-btn">arXiv: 2512.04425v1</a>
    <a href="https://arxiv.org/pdf/2512.04425.pdf" target="_blank" class="toolbar-btn">PDF</a>
  </div>
  <div class="toolbar-right">
    <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.04425v1" 
            onclick="toggleFavorite(this, '2512.04425v1', 'Explainable Parkinsons Disease Gait Recognition Using Multimodal RGB-D Fusion and Large Language Models')" title="收藏">
      ☆ 收藏
    </button>
    <button class="toolbar-btn share-btn" onclick="copyLink()" title="复制链接">
      🔗 分享
    </button>
  </div>
</div>


**作者**: Manar Alnaasan, Md Selim Sarowar, Sungho Kim

**分类**: cs.CV, cs.AI

**发布日期**: 2025-12-04

**🔗 代码/项目**: [GITHUB](https://github.com/manaralnaasan/RGB-D_parkinson-LLM)

---

## 💡 一句话要点

**提出基于RGB-D融合和LLM的可解释帕金森步态识别框架**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)**

**关键词**: `帕金森病` `步态识别` `RGB-D融合` `多模态学习` `大型语言模型` `可解释性` `YOLOv11`

## 📋 核心要点

1. 现有帕金森步态识别方法通常依赖单一模态输入，鲁棒性较差，且缺乏临床透明度。
2. 该论文提出一种基于RGB-D融合和大型语言模型(LLM)的可解释步态识别框架，提升识别精度和可解释性。
3. 实验结果表明，该框架在识别精度、鲁棒性和视觉-语言推理方面均优于单输入基线。

## 📝 摘要（中文）

本研究提出了一种可解释的多模态框架，该框架集成了RGB和深度(RGB-D)数据，用于识别真实条件下的帕金森病(PD)步态模式。该系统采用基于双YOLOv11的编码器进行特定模态的特征提取，然后使用多尺度局部-全局提取(MLGE)模块和跨空间颈融合机制来增强时空表示。这种设计能够捕捉到细粒度的肢体运动(如手臂摆动减少)和整体步态动态(如步幅短或转弯困难)，即使在低光照或衣物遮挡等具有挑战性的场景中也是如此。为了确保可解释性，引入了一个冻结的大型语言模型(LLM)，将融合的视觉嵌入和结构化元数据转换为具有临床意义的文本解释。在多模态步态数据集上的实验评估表明，与单输入基线相比，所提出的RGB-D融合框架实现了更高的识别精度、对环境变化的更强鲁棒性以及清晰的视觉-语言推理。通过将多模态特征学习与基于语言的可解释性相结合，本研究弥合了视觉识别和临床理解之间的差距，为可靠且可解释的帕金森病步态分析提供了一种新颖的视觉-语言范例。

## 🔬 方法详解

**问题定义**：帕金森病早期检测依赖于准确且可解释的步态分析。然而，现有方法主要依赖单一模态数据，在复杂环境下鲁棒性不足，且缺乏临床医生能够理解的解释性，限制了其在实际临床应用中的价值。

**核心思路**：该论文的核心思路是利用RGB-D多模态数据融合，结合深度学习模型提取步态特征，并通过大型语言模型(LLM)将这些特征转化为临床可理解的文本解释，从而提高识别精度和可解释性。多模态融合可以提供更全面的步态信息，LLM则负责将复杂的视觉信息转化为易于理解的临床语言。

**技术框架**：该框架主要包含以下几个模块：1) 基于双YOLOv11的编码器，分别处理RGB和Depth数据，提取模态特定的特征；2) 多尺度局部-全局提取(MLGE)模块，用于捕捉细粒度的肢体运动和整体步态动态；3) 跨空间颈融合机制，用于融合RGB和Depth特征；4) 冻结的LLM，将融合的视觉嵌入和结构化元数据转换为临床可理解的文本解释。

**关键创新**：该论文的关键创新在于：1) 提出了一种RGB-D多模态融合的步态识别框架，能够有效利用不同模态的信息；2) 引入了LLM，实现了步态识别结果的临床可解释性，弥合了视觉识别和临床理解之间的差距；3) 设计了MLGE模块和跨空间颈融合机制，增强了时空特征表示能力。

**关键设计**：论文使用了YOLOv11作为基础检测器，并针对RGB和Depth数据分别训练。MLGE模块的具体结构和参数设置未知。跨空间颈融合机制的实现细节未知。LLM采用冻结的方式，避免了在小数据集上微调可能导致的过拟合问题。损失函数和训练策略的具体细节未知。

## 📊 实验亮点

该研究在多模态步态数据集上进行了实验评估，结果表明，所提出的RGB-D融合框架相比于单输入基线，实现了更高的识别精度和对环境变化的更强鲁棒性。同时，通过LLM生成的文本解释，提供了清晰的视觉-语言推理，增强了模型的可解释性。具体的性能提升数据未知。

## 🎯 应用场景

该研究成果可应用于帕金森病早期筛查、病情评估和康复治疗监测。通过提供准确且可解释的步态分析结果，辅助医生进行诊断和治疗方案制定，提高患者的生活质量。未来可扩展到其他神经系统疾病的步态分析，具有广阔的应用前景。

## 📄 摘要（原文）

> Accurate and interpretable gait analysis plays a crucial role in the early detection of Parkinsons disease (PD),yet most existing approaches remain limited by single-modality inputs, low robustness, and a lack of clinical transparency. This paper presents an explainable multimodal framework that integrates RGB and Depth (RGB-D) data to recognize Parkinsonian gait patterns under realistic conditions. The proposed system employs dual YOLOv11-based encoders for modality-specific feature extraction, followed by a Multi-Scale Local-Global Extraction (MLGE) module and a Cross-Spatial Neck Fusion mechanism to enhance spatial-temporal representation. This design captures both fine-grained limb motion (e.g., reduced arm swing) and overall gait dynamics (e.g., short stride or turning difficulty), even in challenging scenarios such as low lighting or occlusion caused by clothing. To ensure interpretability, a frozen Large Language Model (LLM) is incorporated to translate fused visual embeddings and structured metadata into clinically meaningful textual explanations. Experimental evaluations on multimodal gait datasets demonstrate that the proposed RGB-D fusion framework achieves higher recognition accuracy, improved robustness to environmental variations, and clear visual-linguistic reasoning compared with single-input baselines. By combining multimodal feature learning with language-based interpretability, this study bridges the gap between visual recognition and clinical understanding, offering a novel vision-language paradigm for reliable and explainable Parkinsons disease gait analysis. Code:https://github.com/manaralnaasan/RGB-D_parkinson-LLM

