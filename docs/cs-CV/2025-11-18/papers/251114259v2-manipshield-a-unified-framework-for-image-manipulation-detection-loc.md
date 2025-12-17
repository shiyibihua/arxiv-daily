---
layout: default
title: ManipShield: A Unified Framework for Image Manipulation Detection, Localization and Explanation
---

# ManipShield: A Unified Framework for Image Manipulation Detection, Localization and Explanation

<div class="paper-toolbar">
  <div class="toolbar-left">
    <a href="https://arxiv.org/abs/2511.14259" target="_blank" class="toolbar-btn">arXiv: 2511.14259v2</a>
    <a href="https://arxiv.org/pdf/2511.14259.pdf" target="_blank" class="toolbar-btn">PDF</a>
  </div>
  <div class="toolbar-right">
    <button class="toolbar-btn favorite-btn" data-arxiv-id="2511.14259v2" 
            onclick="toggleFavorite(this, '2511.14259v2', 'ManipShield: A Unified Framework for Image Manipulation Detection, Localization and Explanation')" title="收藏">
      ☆ 收藏
    </button>
    <button class="toolbar-btn share-btn" onclick="copyLink()" title="复制链接">
      🔗 分享
    </button>
  </div>
</div>


**作者**: Zitong Xu, Huiyu Duan, Xiaoyu Wang, Zhaolin Cai, Kaiwei Zhang, Qiang Hu, Jing Liu, Xiongkuo Min, Guangtao Zhai

**分类**: cs.CV

**发布日期**: 2025-11-18 (更新: 2025-11-25)

---

## 💡 一句话要点

**提出ManipShield，一个统一的图像篡改检测、定位和解释框架，并构建大规模基准测试集ManipBench。**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱三：空间感知 (Perception & SLAM)**

**关键词**: `图像篡改检测` `多模态大语言模型` `对比学习` `LoRA微调` `可解释性` `ManipBench` `图像定位` `数字取证`

## 📋 核心要点

1. 现有图像篡改检测方法在内容多样性、模型覆盖和可解释性方面存在不足，限制了其泛化能力。
2. 提出ManipShield，利用多模态大语言模型，通过对比LoRA微调和任务特定解码器，实现篡改检测、定位和解释的统一。
3. 在ManipBench和公共数据集上的实验表明，ManipShield达到了SOTA性能，并对未见过的篡改模型具有良好的泛化性。

## 📝 摘要（中文）

随着生成模型的快速发展，强大的图像编辑方法能够实现多样且高度逼真的图像篡改，这给篡改检测带来了新的挑战，远超传统的深度伪造技术。现有的图像篡改检测和定位(IMDL)基准测试在内容多样性、生成模型覆盖范围和可解释性方面存在局限性，阻碍了当前篡改检测方法的泛化和解释能力。为了解决这些限制，我们引入了ManipBench，这是一个专注于AI编辑图像的大规模图像篡改检测和定位基准。ManipBench包含超过45万张由25个最先进的图像编辑模型生成的篡改图像，涵盖12个篡改类别，其中10万张图像还标注了边界框、判断线索和文本解释，以支持可解释的检测。基于ManipBench，我们提出了ManipShield，这是一个基于多模态大型语言模型(MLLM)的一体化模型，它利用对比LoRA微调和特定任务解码器来实现统一的图像篡改检测、定位和解释。在ManipBench和多个公共数据集上的大量实验表明，ManipShield实现了最先进的性能，并对未见过的篡改模型表现出强大的泛化能力。ManipBench和ManipShield将在发表后发布。

## 🔬 方法详解

**问题定义**：现有图像篡改检测方法难以应对新型AI编辑工具生成的高度逼真篡改图像，且缺乏足够的内容多样性和可解释性，导致泛化能力不足。现有的数据集也难以覆盖各种篡改类型和生成模型，限制了算法的训练和评估。

**核心思路**：利用多模态大语言模型（MLLM）的强大能力，将图像篡改检测、定位和解释统一到一个框架中。通过对比学习增强模型对篡改区域的感知能力，并利用LoRA进行高效微调，使其适应特定的篡改检测任务。任务特定的解码器则负责输出检测结果、定位信息和解释文本。

**技术框架**：ManipShield的核心是一个多模态大语言模型，输入包括图像和文本提示。整体流程包括：1) 图像编码器提取图像特征；2) 文本编码器处理文本提示；3) 多模态融合模块将图像和文本特征融合；4) 对比LoRA微调模块，增强模型对篡改区域的感知；5) 任务特定解码器，分别用于篡改检测、定位和解释。

**关键创新**：ManipShield的关键创新在于将图像篡改检测、定位和解释统一到一个基于MLLM的框架中，并利用对比LoRA微调来提高模型对篡改区域的敏感性。与传统的图像篡改检测方法相比，ManipShield能够提供更全面的信息，包括篡改类型、位置和原因，从而提高检测的可信度和可解释性。

**关键设计**：对比LoRA微调模块使用对比损失函数，鼓励模型区分原始图像和篡改图像。任务特定解码器包括：1) 分类器，用于判断图像是否被篡改；2) 回归器，用于预测篡改区域的边界框；3) 文本生成器，用于生成篡改解释文本。具体网络结构和参数设置在论文中有详细描述。

## 📊 实验亮点

ManipShield在ManipBench和多个公共数据集上取得了SOTA性能，证明了其有效性和泛化能力。实验结果表明，ManipShield能够准确检测和定位各种类型的图像篡改，并提供有意义的解释。与现有方法相比，ManipShield在检测精度、定位准确性和解释质量方面均有显著提升。

## 🎯 应用场景

ManipShield可应用于数字取证、社交媒体内容审核、新闻真实性验证等领域。它可以帮助识别和定位被篡改的图像，防止虚假信息的传播，维护网络安全和信息安全。未来，该技术可以进一步扩展到视频篡改检测，并与其他安全技术相结合，构建更强大的安全防护体系。

## 📄 摘要（原文）

> With the rapid advancement of generative models, powerful image editing methods now enable diverse and highly realistic image manipulations that far surpass traditional deepfake techniques, posing new challenges for manipulation detection. Existing image manipulation detection and localization (IMDL) benchmarks suffer from limited content diversity, narrow generative-model coverage, and insufficient interpretability, which hinders the generalization and explanation capabilities of current manipulation detection methods. To address these limitations, we introduce \textbf{ManipBench}, a large-scale benchmark for image manipulation detection and localization focusing on AI-edited images. ManipBench contains over 450K manipulated images produced by 25 state-of-the-art image editing models across 12 manipulation categories, among which 100K images are further annotated with bounding boxes, judgment cues, and textual explanations to support interpretable detection. Building upon ManipBench, we propose \textbf{ManipShield}, an all-in-one model based on a Multimodal Large Language Model (MLLM) that leverages contrastive LoRA fine-tuning and task-specific decoders to achieve unified image manipulation detection, localization, and explanation. Extensive experiments on ManipBench and several public datasets demonstrate that ManipShield achieves state-of-the-art performance and exhibits strong generality to unseen manipulation models. Both ManipBench and ManipShield will be released upon publication.

