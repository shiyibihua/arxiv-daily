---
layout: default
title: Malicious Image Analysis via Vision-Language Segmentation Fusion: Detection, Element, and Location in One-shot
---

# Malicious Image Analysis via Vision-Language Segmentation Fusion: Detection, Element, and Location in One-shot

<div class="paper-toolbar">
  <div class="toolbar-left">
    <a href="https://arxiv.org/abs/2512.04599" target="_blank" class="toolbar-btn">arXiv: 2512.04599v1</a>
    <a href="https://arxiv.org/pdf/2512.04599.pdf" target="_blank" class="toolbar-btn">PDF</a>
  </div>
  <div class="toolbar-right">
    <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.04599v1" 
            onclick="toggleFavorite(this, '2512.04599v1', 'Malicious Image Analysis via Vision-Language Segmentation Fusion: Detection, Element, and Location in One-shot')" title="收藏">
      ☆ 收藏
    </button>
    <button class="toolbar-btn share-btn" onclick="copyLink()" title="复制链接">
      🔗 分享
    </button>
  </div>
</div>


**作者**: Sheng Hang, Chaoxiang He, Hongsheng Hu, Hanqing Hu, Bin Benjamin Zhu, Shi-Feng Sun, Dawu Gu, Shuo Wang

**分类**: cs.CV

**发布日期**: 2025-12-04

---

## 💡 一句话要点

**提出基于视觉-语言分割融合的恶意图像分析方法，实现一步到位的内容检测、元素识别和定位。**

🎯 **匹配领域**: **支柱三：空间感知 (Perception & SLAM)**

**关键词**: `恶意图像分析` `视觉-语言模型` `图像分割` `零样本学习` `内容审核` `对抗鲁棒性` `可解释性`

## 📋 核心要点

1. 现有恶意图像检测方法通常仅提供图像级别的NSFW标志，缺乏对有害元素及其位置的细粒度理解。
2. 该论文提出一种零样本的视觉-语言分割融合方法，能够一步到位地检测恶意内容、识别关键元素并精确定位。
3. 实验表明，该方法在恶意内容检测的召回率、精确率和分割成功率上均有显著提升，并具有较强的抗攻击鲁棒性。

## 📝 摘要（中文）

本文提出了一种零样本恶意图像分析流程，能够同时完成三个任务：(i) 检测图像是否包含有害内容；(ii) 识别图像中涉及的关键元素；(iii) 以像素级精度定位这些元素。该系统首先应用基础分割模型（SAM）生成候选对象掩码，并将其优化为更大的独立区域。然后，使用视觉-语言模型和开放词汇提示对每个区域进行恶意相关性评分；这些分数用于加权融合步骤，生成统一的恶意对象图。通过集成多个分割器，增强了流程对针对单一分割方法的自适应攻击的抵抗能力。在包含毒品、性、暴力和极端主义内容的新标注的790张图像数据集上进行评估，该方法达到了85.8%的元素级召回率，78.1%的精确率和92.1%的分割成功率，在可比精度下，比直接的零样本VLM定位提高了27.4%的召回率。针对旨在破坏SAM和VLM的PGD对抗扰动，该方法的精确率和召回率下降不超过10%，表现出很高的抗攻击鲁棒性。完整的流程在几秒钟内处理一张图像，无缝地插入现有的VLM工作流程，并构成了第一个用于细粒度、可解释的恶意图像审核的实用工具。

## 🔬 方法详解

**问题定义**：恶意图像分析旨在识别图像中存在的有害内容，并确定导致图像被判定为恶意的具体元素及其位置。现有方法通常只能给出图像级别的判断，无法提供细粒度的解释，且容易受到对抗攻击的影响。

**核心思路**：该论文的核心思路是利用视觉-语言模型的开放词汇能力，结合图像分割技术，实现对恶意图像中关键元素的定位和识别。通过融合多个分割器的结果，提高模型的鲁棒性。

**技术框架**：该方法主要包含以下几个阶段：1) 使用基础分割模型（SAM）生成候选对象掩码；2) 将掩码优化为更大的独立区域；3) 使用视觉-语言模型对每个区域进行恶意相关性评分；4) 根据评分进行融合，生成恶意对象图；5) 集成多个分割器的结果，提高鲁棒性。

**关键创新**：该方法最重要的创新点在于将视觉-语言模型与图像分割技术相结合，实现了零样本的细粒度恶意图像分析。通过融合多个分割器的结果，提高了模型的鲁棒性，使其能够抵抗针对单一分割方法的对抗攻击。

**关键设计**：该方法使用SAM作为基础分割模型，利用其强大的分割能力生成候选区域。使用视觉-语言模型进行评分时，采用开放词汇提示，允许模型识别各种类型的恶意元素。通过加权融合不同区域的评分，生成最终的恶意对象图。

## 📊 实验亮点

该方法在包含毒品、性、暴力和极端主义内容的数据集上取得了显著成果，元素级召回率达到85.8%，精确率达到78.1%，分割成功率达到92.1%。与直接的零样本VLM定位相比，召回率提高了27.4%。同时，该方法对PGD对抗扰动表现出较强的鲁棒性，精确率和召回率下降不超过10%。

## 🎯 应用场景

该研究成果可应用于内容审核、网络安全、智能监控等领域。例如，可以帮助社交媒体平台自动检测和过滤恶意图像，减少人工审核的工作量，提高审核效率。此外，该方法还可以用于识别和定位犯罪现场的证据，辅助案件侦破。

## 📄 摘要（原文）

> Detecting illicit visual content demands more than image-level NSFW flags; moderators must also know what objects make an image illegal and where those objects occur. We introduce a zero-shot pipeline that simultaneously (i) detects if an image contains harmful content, (ii) identifies each critical element involved, and (iii) localizes those elements with pixel-accurate masks - all in one pass. The system first applies foundation segmentation model (SAM) to generate candidate object masks and refines them into larger independent regions. Each region is scored for malicious relevance by a vision-language model using open-vocabulary prompts; these scores weight a fusion step that produces a consolidated malicious object map. An ensemble across multiple segmenters hardens the pipeline against adaptive attacks that target any single segmentation method. Evaluated on a newly-annotated 790-image dataset spanning drug, sexual, violent and extremist content, our method attains 85.8% element-level recall, 78.1% precision and a 92.1% segment-success rate - exceeding direct zero-shot VLM localization by 27.4% recall at comparable precision. Against PGD adversarial perturbations crafted to break SAM and VLM, our method's precision and recall decreased by no more than 10%, demonstrating high robustness against attacks. The full pipeline processes an image in seconds, plugs seamlessly into existing VLM workflows, and constitutes the first practical tool for fine-grained, explainable malicious-image moderation.

