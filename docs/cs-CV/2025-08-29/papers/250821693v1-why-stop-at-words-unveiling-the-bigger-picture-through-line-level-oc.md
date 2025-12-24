---
layout: default
title: Why Stop at Words? Unveiling the Bigger Picture through Line-Level OCR
---

# Why Stop at Words? Unveiling the Bigger Picture through Line-Level OCR

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.21693" class="toolbar-btn" target="_blank">📄 arXiv: 2508.21693v1</a>
  <a href="https://arxiv.org/pdf/2508.21693.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.21693v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.21693v1', 'Why Stop at Words? Unveiling the Bigger Picture through Line-Level OCR')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Shashank Vempati, Nishit Anand, Gaurav Talebailkar, Arpan Garai, Chetan Arora

**分类**: cs.CV, cs.AI, cs.CL, cs.LG

**发布日期**: 2025-08-29

**备注**: 11 pages. Project Website: https://nishitanand.github.io/line-level-ocr-website

**🔗 代码/项目**: [PROJECT_PAGE](https://nishitanand.github.io/line-level-ocr-website)

---

## 💡 一句话要点

**提出行级OCR以解决词级OCR的局限性**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `光学字符识别` `行级OCR` `文本检测` `语言模型` `文档数字化` `深度学习`

## 📋 核心要点

1. 现有的OCR方法在字符分割上容易出错，且缺乏上下文信息，限制了语言模型的有效利用。
2. 本文提出行级OCR，能够绕过单词检测中的错误，并提供更大的上下文信息，从而提高OCR的准确性和效率。
3. 实验结果表明，行级OCR的端到端准确性提高了5.4%，效率相比词级管道提升了4倍，显示出显著的改进。

## 📝 摘要（中文）

传统的光学字符识别（OCR）技术通过分割每个字符进行识别，这使得字符分割容易出错，并且缺乏利用语言模型的上下文。近年来，序列到序列翻译的进展使得现代技术首先检测单词，然后逐个输入到模型中，直接输出完整的字符序列。这种方法提高了语言模型的利用效率，绕过了容易出错的字符分割步骤。然而，这种转变使得准确性的瓶颈转移到了单词分割上。本文提出了一种从词级OCR到行级OCR的自然进展，能够绕过单词检测中的错误，并提供更大的句子上下文以更好地利用语言模型。实验结果显示，该技术不仅提高了OCR的准确性，还提高了效率。我们还贡献了一个包含251个英文页面图像及行级注释的精心策划的数据集。

## 🔬 方法详解

**问题定义**：本文旨在解决传统OCR方法在字符分割和单词检测中存在的错误，导致整体识别准确性下降的问题。现有方法在处理复杂文档时，容易受到字符和单词分割的影响。

**核心思路**：论文提出的行级OCR方法通过直接处理整行文本，避免了单词检测的错误，并利用更丰富的上下文信息来提升识别效果。这种方法的设计旨在提高OCR的整体准确性和效率。

**技术框架**：整体架构包括行级文本检测模块和字符识别模块。首先，系统检测文本行，然后对整行进行字符识别，最后输出完整的文本序列。

**关键创新**：最重要的创新点在于从词级OCR转向行级OCR，这一转变使得系统能够利用更大的上下文信息，显著减少了错误率，并提高了处理效率。

**关键设计**：在技术细节上，采用了优化的损失函数以适应行级识别的需求，并在网络结构中引入了适合行级文本特征提取的卷积层和循环神经网络（RNN）模块。

## 📊 实验亮点

实验结果显示，行级OCR的端到端准确性提高了5.4%，相比传统的词级OCR，效率提升了4倍。这些结果表明，行级OCR在处理文档图像时具有显著的优势，尤其是在复杂文本环境中。

## 🎯 应用场景

该研究的潜在应用领域包括文档数字化、自动化数据录入和信息提取等。行级OCR能够在处理复杂文档时提供更高的准确性和效率，未来可能在法律、医疗和金融等行业中发挥重要作用，提升信息处理的自动化水平。

## 📄 摘要（原文）

> Conventional optical character recognition (OCR) techniques segmented each character and then recognized. This made them prone to error in character segmentation, and devoid of context to exploit language models. Advances in sequence to sequence translation in last decade led to modern techniques first detecting words and then inputting one word at a time to a model to directly output full words as sequence of characters. This allowed better utilization of language models and bypass error-prone character segmentation step. We observe that the above transition in style has moved the bottleneck in accuracy to word segmentation. Hence, in this paper, we propose a natural and logical progression from word level OCR to line-level OCR. The proposal allows to bypass errors in word detection, and provides larger sentence context for better utilization of language models. We show that the proposed technique not only improves the accuracy but also efficiency of OCR. Despite our thorough literature survey, we did not find any public dataset to train and benchmark such shift from word to line-level OCR. Hence, we also contribute a meticulously curated dataset of 251 English page images with line-level annotations. Our experimentation revealed a notable end-to-end accuracy improvement of 5.4%, underscoring the potential benefits of transitioning towards line-level OCR, especially for document images. We also report a 4 times improvement in efficiency compared to word-based pipelines. With continuous improvements in large language models, our methodology also holds potential to exploit such advances. Project Website: https://nishitanand.github.io/line-level-ocr-website

