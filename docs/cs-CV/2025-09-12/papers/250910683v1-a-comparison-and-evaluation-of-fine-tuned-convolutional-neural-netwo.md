---
layout: default
title: A Comparison and Evaluation of Fine-tuned Convolutional Neural Networks to Large Language Models for Image Classification and Segmentation of Brain Tumors on MRI
---

# A Comparison and Evaluation of Fine-tuned Convolutional Neural Networks to Large Language Models for Image Classification and Segmentation of Brain Tumors on MRI

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.10683" class="toolbar-btn" target="_blank">📄 arXiv: 2509.10683v1</a>
  <a href="https://arxiv.org/pdf/2509.10683.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.10683v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.10683v1', 'A Comparison and Evaluation of Fine-tuned Convolutional Neural Networks to Large Language Models for Image Classification and Segmentation of Brain Tumors on MRI')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Felicia Liu, Jay J. Yoo, Farzad Khalvati

**分类**: cs.CV, cs.AI

**发布日期**: 2025-09-12

---

## 💡 一句话要点

**对比微调LLM与CNN在脑肿瘤MRI图像分类与分割任务中的性能**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `卷积神经网络` `脑肿瘤` `医学图像分割` `医学图像分类`

## 📋 核心要点

1. 现有LLM在医学图像任务中应用潜力未知，缺乏与传统CNN的直接对比。
2. 本文探索LLM在脑肿瘤分类与分割任务中的性能，并与3D CNN进行对比评估。
3. 实验表明，CNN在脑肿瘤分类和分割任务中优于LLM，LLM空间理解能力有限。

## 📝 摘要（中文）

大型语言模型(LLMs)在基于文本的医疗保健任务中表现出强大的性能。然而，它们在基于图像的应用中的效用仍有待探索。本文研究了LLMs在医学成像任务中的有效性，特别是胶质瘤分类和分割，并将它们的性能与传统的卷积神经网络(CNNs)进行了比较。使用BraTS 2020多模态脑部MRI数据集，我们评估了一个通用视觉-语言LLM (LLaMA 3.2 Instruct)在微调前后的性能，并将其性能与定制的3D CNN进行了基准测试。对于胶质瘤分类(低级别vs.高级别)，CNN达到了80%的准确率和平衡的精确率和召回率。通用LLM达到了76%的准确率，但特异性仅为18%，经常错误分类低级别肿瘤。微调将特异性提高到55%，但整体性能下降(例如，准确率降至72%)。对于分割，实现了三种方法——中心点、边界框和多边形提取。CNNs准确地定位了胶质瘤，尽管有时会遗漏小肿瘤。相比之下，LLMs始终将预测聚集在图像中心附近，无法区分胶质瘤的大小、位置或放置。微调改进了输出格式，但未能有意义地提高空间准确性。边界多边形方法产生了随机的、非结构化的输出。总的来说，CNNs在两项任务中都优于LLMs。LLMs显示出有限的空间理解能力，并且微调带来的改进很小，表明它们目前的形式不太适合基于图像的任务。可能需要更严格的微调或替代训练策略，LLMs才能在医学领域实现更好的性能、鲁棒性和实用性。

## 🔬 方法详解

**问题定义**：论文旨在评估大型语言模型（LLMs）在医学图像处理任务中的有效性，具体问题是脑肿瘤的分类和分割。现有方法，即传统的卷积神经网络（CNNs），虽然在这些任务中表现良好，但缺乏对上下文信息的理解能力，并且需要针对特定任务进行专门设计。LLMs在自然语言处理领域展现出强大的上下文理解和泛化能力，但其在医学图像领域的应用潜力尚未充分挖掘。

**核心思路**：论文的核心思路是将LLMs应用于医学图像处理任务，并将其性能与传统的CNNs进行比较。通过微调LLMs，使其适应医学图像的特点，并评估其在脑肿瘤分类和分割任务中的表现。这种方法旨在探索LLMs在医学图像领域的潜力，并为未来的研究提供参考。

**技术框架**：论文的技术框架主要包括以下几个部分：1）使用BraTS 2020数据集，该数据集包含多模态脑部MRI图像；2）选择LLaMA 3.2 Instruct作为LLM模型，并进行微调；3）构建定制的3D CNN模型作为基线；4）对于分类任务，比较LLM和CNN的准确率、精确率和召回率；5）对于分割任务，采用中心点、边界框和多边形提取三种方法，评估LLM和CNN的分割效果。

**关键创新**：论文的关键创新在于首次将通用视觉-语言LLM（LLaMA 3.2 Instruct）应用于脑肿瘤的分类和分割任务，并与传统的3D CNN进行了全面的比较。此外，论文还探索了不同的分割方法，并评估了微调对LLM性能的影响。

**关键设计**：在实验中，LLM使用了LLaMA 3.2 Instruct模型，并使用BraTS 2020数据集进行了微调。对于分割任务，采用了三种不同的方法：中心点预测、边界框预测和多边形提取。对于CNN模型，使用了定制的3D CNN架构，并针对BraTS 2020数据集进行了训练。损失函数和优化器等技术细节未在摘要中明确提及，属于未知信息。

## 📊 实验亮点

实验结果表明，在脑肿瘤分类任务中，CNN达到了80%的准确率，而未经微调的LLM准确率为76%，但特异性仅为18%。微调后，LLM的特异性提高到55%，但整体准确率下降到72%。在分割任务中，CNN能够准确地定位胶质瘤，而LLM的预测结果始终聚集在图像中心附近，无法有效区分肿瘤的大小和位置。总体而言，CNN在两项任务中均优于LLM。

## 🎯 应用场景

该研究成果可应用于医学影像辅助诊断领域，通过结合LLM的上下文理解能力和CNN的图像处理能力，有望提高脑肿瘤等疾病的诊断准确率和效率。未来，该方法可扩展到其他医学影像任务，为临床医生提供更全面的辅助决策支持。

## 📄 摘要（原文）

> Large Language Models (LLMs) have shown strong performance in text-based healthcare tasks. However, their utility in image-based applications remains unexplored. We investigate the effectiveness of LLMs for medical imaging tasks, specifically glioma classification and segmentation, and compare their performance to that of traditional convolutional neural networks (CNNs). Using the BraTS 2020 dataset of multi-modal brain MRIs, we evaluated a general-purpose vision-language LLM (LLaMA 3.2 Instruct) both before and after fine-tuning, and benchmarked its performance against custom 3D CNNs. For glioma classification (Low-Grade vs. High-Grade), the CNN achieved 80% accuracy and balanced precision and recall. The general LLM reached 76% accuracy but suffered from a specificity of only 18%, often misclassifying Low-Grade tumors. Fine-tuning improved specificity to 55%, but overall performance declined (e.g., accuracy dropped to 72%). For segmentation, three methods - center point, bounding box, and polygon extraction, were implemented. CNNs accurately localized gliomas, though small tumors were sometimes missed. In contrast, LLMs consistently clustered predictions near the image center, with no distinction of glioma size, location, or placement. Fine-tuning improved output formatting but failed to meaningfully enhance spatial accuracy. The bounding polygon method yielded random, unstructured outputs. Overall, CNNs outperformed LLMs in both tasks. LLMs showed limited spatial understanding and minimal improvement from fine-tuning, indicating that, in their current form, they are not well-suited for image-based tasks. More rigorous fine-tuning or alternative training strategies may be needed for LLMs to achieve better performance, robustness, and utility in the medical space.

