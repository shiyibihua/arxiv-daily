---
layout: default
title: Automated Detection of Pre-training Text in Black-box LLMs
---

# Automated Detection of Pre-training Text in Black-box LLMs

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.19399" class="toolbar-btn" target="_blank">📄 arXiv: 2506.19399v1</a>
  <a href="https://arxiv.org/pdf/2506.19399.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.19399v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.19399v1', 'Automated Detection of Pre-training Text in Black-box LLMs')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Ruihan Hu, Yu-Ming Shang, Jiankun Peng, Wei Luo, Yazhe Wang, Xi Zhang

**分类**: cs.CL, cs.AI

**发布日期**: 2025-06-24

**备注**: 13 pages

---

## 💡 一句话要点

**提出VeilProbe以解决黑箱LLM预训练文本检测问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `黑箱模型` `预训练文本` `数据隐私` `自动化检测` `机器学习` `序列到序列模型` `版权保护`

## 📋 核心要点

1. 现有方法依赖于模型的隐藏信息，无法在黑箱环境中有效检测预训练文本，且需要大量人工设计问题。
2. 本文提出VeilProbe框架，利用序列到序列映射模型自动推断输入与输出之间的映射特征，减少人工干预。
3. 在三个数据集上的评估显示，VeilProbe在黑箱环境中表现优越，成功缓解了过拟合问题。

## 📝 摘要（中文）

检测给定文本是否属于大型语言模型（LLMs）的预训练数据对于确保数据隐私和版权保护至关重要。现有方法依赖于模型的隐藏信息，无法在黑箱环境中有效工作。为了解决这一问题，本文提出了VeilProbe，这是第一个在黑箱环境中无需人工干预自动检测LLMs预训练文本的框架。VeilProbe利用序列到序列映射模型推断输入文本与LLM生成的输出后缀之间的潜在映射特征，并通过关键token扰动获得更具区分性的成员特征。此外，考虑到真实场景中训练文本样本有限，本文引入了一种基于原型的成员分类器以缓解过拟合问题。对三个广泛使用的数据集进行的广泛评估表明，该框架在黑箱环境中有效且优越。

## 🔬 方法详解

**问题定义**：本文旨在解决在黑箱环境中检测大型语言模型预训练文本的具体问题。现有方法依赖于模型的隐藏信息，无法在仅有输入和输出文本的情况下有效工作，且往往需要大量人工设计的问题和指令。

**核心思路**：VeilProbe框架的核心思路是利用序列到序列映射模型自动推断输入文本与LLM生成的输出后缀之间的潜在映射特征，从而实现无需人工干预的预训练文本检测。

**技术框架**：VeilProbe的整体架构包括输入文本处理、序列到序列映射模型推断、关键token扰动和基于原型的成员分类器四个主要模块。首先，输入文本通过模型生成输出后缀，然后推断潜在映射特征，接着进行token扰动以增强特征的可区分性，最后使用原型分类器进行成员资格判断。

**关键创新**：VeilProbe的最大创新在于其在黑箱环境中实现了自动化的预训练文本检测，避免了传统方法对隐藏信息的依赖，并且减少了人工干预的需求。

**关键设计**：在设计中，VeilProbe采用了序列到序列模型进行特征推断，并通过关键token扰动来增强特征的区分能力。此外，基于原型的成员分类器被引入以应对训练样本有限导致的过拟合问题。具体的参数设置和损失函数设计在实验部分进行了详细描述。

## 📊 实验亮点

在三个广泛使用的数据集上的实验结果表明，VeilProbe框架在黑箱环境中显著优于现有方法，成功提高了预训练文本检测的准确性和效率。具体性能数据展示了在不同数据集上检测准确率的提升幅度，验证了该方法的有效性。

## 🎯 应用场景

该研究的潜在应用领域包括数据隐私保护、版权管理和模型安全性评估等。通过自动化检测LLM的预训练文本，能够有效防止数据泄露和版权侵权，具有重要的实际价值和社会影响。未来，该技术可能会在更多的黑箱模型检测和数据安全领域得到广泛应用。

## 📄 摘要（原文）

> Detecting whether a given text is a member of the pre-training data of Large Language Models (LLMs) is crucial for ensuring data privacy and copyright protection. Most existing methods rely on the LLM's hidden information (e.g., model parameters or token probabilities), making them ineffective in the black-box setting, where only input and output texts are accessible. Although some methods have been proposed for the black-box setting, they rely on massive manual efforts such as designing complicated questions or instructions. To address these issues, we propose VeilProbe, the first framework for automatically detecting LLMs' pre-training texts in a black-box setting without human intervention. VeilProbe utilizes a sequence-to-sequence mapping model to infer the latent mapping feature between the input text and the corresponding output suffix generated by the LLM. Then it performs the key token perturbations to obtain more distinguishable membership features. Additionally, considering real-world scenarios where the ground-truth training text samples are limited, a prototype-based membership classifier is introduced to alleviate the overfitting issue. Extensive evaluations on three widely used datasets demonstrate that our framework is effective and superior in the black-box setting.

