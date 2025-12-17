---
layout: default
title: Mind-to-Face: Neural-Driven Photorealistic Avatar Synthesis via EEG Decoding
---

# Mind-to-Face: Neural-Driven Photorealistic Avatar Synthesis via EEG Decoding

<div class="paper-toolbar">
  <div class="toolbar-left">
    <a href="https://arxiv.org/abs/2512.04313" target="_blank" class="toolbar-btn">arXiv: 2512.04313v1</a>
    <a href="https://arxiv.org/pdf/2512.04313.pdf" target="_blank" class="toolbar-btn">PDF</a>
  </div>
  <div class="toolbar-right">
    <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.04313v1" 
            onclick="toggleFavorite(this, '2512.04313v1', 'Mind-to-Face: Neural-Driven Photorealistic Avatar Synthesis via EEG Decoding')" title="收藏">
      ☆ 收藏
    </button>
    <button class="toolbar-btn share-btn" onclick="copyLink()" title="复制链接">
      🔗 分享
    </button>
  </div>
</div>


**作者**: Haolin Xiong, Tianwen Fu, Pratusha Bhuvana Prasad, Yunxuan Cai, Haiwei Chen, Wenbin Teng, Hanyuan Xiao, Yajie Zhao

**分类**: cs.CV

**发布日期**: 2025-12-03

**备注**: 16 pages, 11 figures

---

## 💡 一句话要点

**Mind-to-Face：首个基于脑电信号解码的逼真人脸Avatar生成框架**

🎯 **匹配领域**: **支柱三：空间感知 (Perception & SLAM)**

**关键词**: `脑机接口` `人脸Avatar` `脑电信号解码` `3D高斯溅射` `情感识别`

## 📋 核心要点

1. 现有Avatar系统严重依赖视觉线索，在面部被遮挡或情绪内敛时失效，无法准确捕捉内在情感。
2. Mind-to-Face通过CNN-Transformer将脑电信号解码为高精度3D面部模型，并使用3D高斯溅射渲染逼真Avatar。
3. 实验证明，仅使用脑电信号即可预测个体化的动态面部表情，包括细微的情绪反应，效果显著。

## 📝 摘要（中文）

本文提出Mind-to-Face，是首个将非侵入式脑电图(EEG)信号直接解码为高保真面部表情的框架。我们构建了一个双模态记录系统，在诱发情绪的刺激下，同步获取EEG和多视角面部视频，从而为神经-视觉学习提供精确的监督。我们的模型使用CNN-Transformer编码器将EEG信号映射到密集的3D位置图，能够采样超过65k个顶点，捕捉精细的几何结构和微妙的情绪动态，并通过改进的3D高斯溅射渲染管线生成逼真且视角一致的结果。通过广泛的评估，我们证明仅凭EEG就能可靠地预测动态的、个体化的面部表情，包括微妙的情绪反应，表明神经信号包含比之前认为的更丰富的情感和几何信息。Mind-to-Face为神经驱动的Avatar建立了一个新的范例，能够在沉浸式环境中实现个性化的、情感感知的远程呈现和认知交互。

## 🔬 方法详解

**问题定义**：现有的人脸Avatar生成系统主要依赖于视觉信息，例如面部图像或视频。当面部被遮挡，或者人们试图隐藏自己的情绪时，这些系统就无法准确地捕捉到真实的情感表达。因此，如何仅通过非侵入式神经信号（如脑电图EEG）来驱动逼真的人脸Avatar，是一个具有挑战性的问题。

**核心思路**：本文的核心思路是将脑电信号直接映射到高精度的3D面部模型，并利用3D高斯溅射技术进行渲染，从而生成逼真的人脸Avatar。这种方法避免了对视觉信息的依赖，可以直接反映个体的情绪状态和内在想法。通过建立EEG信号与面部表情之间的直接联系，可以实现更加自然和个性化的Avatar控制。

**技术框架**：Mind-to-Face框架主要包含以下几个模块：1) **双模态数据采集**：同步记录EEG信号和多视角面部视频，用于训练模型。2) **CNN-Transformer编码器**：将EEG信号编码为高维特征向量。3) **3D位置图生成器**：将特征向量映射到密集的3D位置图，该位置图包含超过65k个顶点，能够捕捉精细的面部几何结构。4) **3D高斯溅射渲染管线**：将3D位置图渲染成逼真且视角一致的人脸图像。

**关键创新**：该论文的关键创新在于：1) **首次提出基于EEG信号直接生成逼真人脸Avatar的框架**，突破了传统方法对视觉信息的依赖。2) **利用CNN-Transformer结构有效提取EEG信号中的情感和几何信息**。3) **采用改进的3D高斯溅射渲染管线，实现了高质量的Avatar渲染效果**。

**关键设计**：在网络结构方面，采用了CNN-Transformer混合结构，CNN用于提取局部特征，Transformer用于捕捉全局依赖关系。损失函数方面，使用了L1损失和感知损失，以保证生成的人脸图像的逼真度和细节。在3D高斯溅射渲染管线中，对高斯分布的参数进行了优化，以提高渲染质量和效率。

## 📊 实验亮点

实验结果表明，Mind-to-Face能够仅凭EEG信号可靠地预测动态的、个体化的面部表情，包括微妙的情绪反应。与基线方法相比，Mind-to-Face在面部表情识别的准确性和Avatar渲染的逼真度方面均取得了显著提升。具体而言，在主观评估中，用户普遍认为Mind-to-Face生成的Avatar更加自然和富有表现力。

## 🎯 应用场景

Mind-to-Face技术在多个领域具有广泛的应用前景。例如，在远程呈现和虚拟会议中，可以使用户的Avatar能够真实地反映其情绪状态，从而增强沟通的自然性和有效性。在游戏和娱乐领域，可以创建更加个性化和沉浸式的角色体验。此外，该技术还可以应用于神经反馈治疗和认知康复，帮助患者更好地了解和控制自己的情绪。

## 📄 摘要（原文）

> Current expressive avatar systems rely heavily on visual cues, failing when faces are occluded or when emotions remain internal. We present Mind-to-Face, the first framework that decodes non-invasive electroencephalogram (EEG) signals directly into high-fidelity facial expressions. We build a dual-modality recording setup to obtain synchronized EEG and multi-view facial video during emotion-eliciting stimuli, enabling precise supervision for neural-to-visual learning. Our model uses a CNN-Transformer encoder to map EEG signals into dense 3D position maps, capable of sampling over 65k vertices, capturing fine-scale geometry and subtle emotional dynamics, and renders them through a modified 3D Gaussian Splatting pipeline for photorealistic, view-consistent results. Through extensive evaluation, we show that EEG alone can reliably predict dynamic, subject-specific facial expressions, including subtle emotional responses, demonstrating that neural signals contain far richer affective and geometric information than previously assumed. Mind-to-Face establishes a new paradigm for neural-driven avatars, enabling personalized, emotion-aware telepresence and cognitive interaction in immersive environments.

