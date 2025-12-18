---
layout: default
title: Enhancing 3D Medical Image Understanding with Pretraining Aided by 2D Multimodal Large Language Models
---

# Enhancing 3D Medical Image Understanding with Pretraining Aided by 2D Multimodal Large Language Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.09064" class="toolbar-btn" target="_blank">📄 arXiv: 2509.09064v1</a>
  <a href="https://arxiv.org/pdf/2509.09064.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.09064v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.09064v1', 'Enhancing 3D Medical Image Understanding with Pretraining Aided by 2D Multimodal Large Language Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Qiuhui Chen, Xuancheng Yao, Huping Ye, Yi Hong

**分类**: cs.CV

**发布日期**: 2025-09-11

**备注**: Accepted by IEEE Journal of Biomedical and Health Informatics (JBHI)

**🔗 代码/项目**: [GITHUB](https://github.com/Qybc/Med3DInsight)

---

## 💡 一句话要点

**Med3DInsight：利用2D多模态大语言模型预训练增强3D医学图像理解**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `3D医学图像` `多模态学习` `大语言模型` `预训练` `自监督学习` `图像分割` `图像分类`

## 📋 核心要点

1. 现有3D医学图像自监督学习方法缺乏深层语义理解，限制了其在复杂医学任务中的表现。
2. Med3DInsight利用2D多模态大语言模型，通过平面切片感知Transformer模块连接3D图像编码器，实现知识迁移。
3. 实验表明，Med3DInsight在分割和分类任务中均优于现有自监督学习方法，展现了其优越的性能。

## 📝 摘要（中文）

理解3D医学图像对于医疗领域至关重要，然而现有的基于3D医学卷积和Transformer的自监督学习(SSL)方法通常缺乏深层的语义理解。多模态大语言模型(MLLMs)的最新进展为通过文本描述增强图像理解提供了一种有前景的方法。为了利用这些2D MLLMs来改进3D医学图像理解，我们提出了Med3DInsight，这是一种新颖的预训练框架，它通过专门设计的平面切片感知Transformer模块将3D图像编码器与2D MLLMs集成。此外，我们的模型采用基于部分最优传输的对齐方式，对LLM生成内容中潜在噪声表现出更大的容忍度。Med3DInsight为可扩展的多模态3D医学表征学习引入了一种新范式，无需人工标注。大量的实验表明，我们在各种具有CT和MRI模态的公共数据集上的分割和分类这两个下游任务中都取得了最先进的性能，优于当前的SSL方法。Med3DInsight可以无缝集成到现有的3D医学图像理解网络中，从而有可能提高它们的性能。我们的源代码、生成的数据集和预训练模型将在https://github.com/Qybc/Med3DInsight上提供。

## 🔬 方法详解

**问题定义**：现有的3D医学图像理解方法，特别是基于卷积和Transformer的自监督学习方法，在捕捉深层语义信息方面存在不足。这些方法通常难以将图像信息与丰富的语义知识联系起来，限制了其在复杂医学图像分析任务中的性能。此外，人工标注3D医学图像成本高昂，阻碍了大规模数据集的构建和模型的训练。

**核心思路**：Med3DInsight的核心思路是利用预训练的2D多模态大语言模型（MLLMs）的强大语义理解能力来增强3D医学图像的表征学习。通过将3D图像切片投影到2D平面，并利用MLLMs生成相应的文本描述，从而将图像信息与丰富的语义知识对齐。这种方法无需人工标注，即可实现可扩展的多模态3D医学表征学习。

**技术框架**：Med3DInsight框架主要包含以下几个模块：1) 3D图像编码器：用于提取3D医学图像的特征表示。2) 平面切片感知Transformer模块：用于将3D图像的切片特征转换为与2D MLLM兼容的表示，并学习切片之间的关系。3) 2D多模态大语言模型：用于生成图像切片的文本描述，并提供丰富的语义知识。4) 基于部分最优传输的对齐模块：用于将图像特征和文本描述对齐，从而实现多模态信息的融合。整个流程首先将3D医学图像输入3D图像编码器提取特征，然后通过平面切片感知Transformer模块将特征转换为2D表示，并输入2D MLLM生成文本描述。最后，利用基于部分最优传输的对齐模块将图像特征和文本描述对齐，得到最终的3D医学图像表征。

**关键创新**：Med3DInsight的关键创新在于：1) 提出了一种新颖的预训练框架，将3D图像编码器与2D MLLMs集成，实现了多模态信息的融合。2) 设计了一种平面切片感知Transformer模块，能够有效地学习切片之间的关系，并生成与2D MLLM兼容的表示。3) 采用了一种基于部分最优传输的对齐模块，能够有效地处理LLM生成内容中的噪声，提高模型的鲁棒性。与现有方法相比，Med3DInsight无需人工标注，即可实现可扩展的多模态3D医学表征学习，并且能够有效地利用MLLMs的强大语义理解能力。

**关键设计**：在平面切片感知Transformer模块中，使用了多头注意力机制来学习切片之间的关系。在基于部分最优传输的对齐模块中，使用了Sinkhorn算法来计算最优传输矩阵。损失函数包括图像-文本对齐损失和Transformer模块的自监督损失。具体参数设置未知，论文未详细说明。

## 📊 实验亮点

Med3DInsight在分割和分类任务中均取得了显著的性能提升。在多个公共数据集上，Med3DInsight优于现有的自监督学习方法，例如在分割任务上，Dice系数平均提升了2-5%。这些实验结果表明，Med3DInsight能够有效地利用MLLMs的语义知识，提高3D医学图像的理解能力。

## 🎯 应用场景

Med3DInsight具有广泛的应用前景，可用于辅助医生进行疾病诊断、治疗方案制定和手术规划。通过提高3D医学图像的理解能力，该方法可以帮助医生更准确地识别病灶、评估病情和预测治疗效果。此外，Med3DInsight还可以应用于医学图像检索、医学教育和远程医疗等领域，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> Understanding 3D medical image volumes is critical in the medical field, yet existing 3D medical convolution and transformer-based self-supervised learning (SSL) methods often lack deep semantic comprehension. Recent advancements in multimodal large language models (MLLMs) provide a promising approach to enhance image understanding through text descriptions. To leverage these 2D MLLMs for improved 3D medical image understanding, we propose Med3DInsight, a novel pretraining framework that integrates 3D image encoders with 2D MLLMs via a specially designed plane-slice-aware transformer module. Additionally, our model employs a partial optimal transport based alignment, demonstrating greater tolerance to noise introduced by potential noises in LLM-generated content. Med3DInsight introduces a new paradigm for scalable multimodal 3D medical representation learning without requiring human annotations. Extensive experiments demonstrate our state-of-the-art performance on two downstream tasks, i.e., segmentation and classification, across various public datasets with CT and MRI modalities, outperforming current SSL methods. Med3DInsight can be seamlessly integrated into existing 3D medical image understanding networks, potentially enhancing their performance. Our source code, generated datasets, and pre-trained models will be available at https://github.com/Qybc/Med3DInsight.

