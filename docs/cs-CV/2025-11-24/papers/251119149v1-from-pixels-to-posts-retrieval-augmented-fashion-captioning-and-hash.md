---
layout: default
title: From Pixels to Posts: Retrieval-Augmented Fashion Captioning and Hashtag Generation
---

# From Pixels to Posts: Retrieval-Augmented Fashion Captioning and Hashtag Generation

<div class="paper-toolbar">
  <div class="toolbar-left">
    <a href="https://arxiv.org/abs/2511.19149" target="_blank" class="toolbar-btn">arXiv: 2511.19149v1</a>
    <a href="https://arxiv.org/pdf/2511.19149.pdf" target="_blank" class="toolbar-btn">PDF</a>
  </div>
  <div class="toolbar-right">
    <button class="toolbar-btn favorite-btn" data-arxiv-id="2511.19149v1" 
            onclick="toggleFavorite(this, '2511.19149v1', 'From Pixels to Posts: Retrieval-Augmented Fashion Captioning and Hashtag Generation')" title="收藏">
      ☆ 收藏
    </button>
    <button class="toolbar-btn share-btn" onclick="copyLink()" title="复制链接">
      🔗 分享
    </button>
  </div>
</div>


**作者**: Moazzam Umer Gondal, Hamad Ul Qudous, Daniya Siddiqui, Asma Ahmad Farhan

**分类**: cs.CV, cs.AI, cs.CL

**发布日期**: 2025-11-24

**备注**: Submitted to Expert Systems with Applications

---

## 💡 一句话要点

**提出检索增强的时尚描述与标签生成框架，提升属性保真度和领域泛化性。**

🎯 **匹配领域**: **支柱三：空间感知 (Perception & SLAM)**

**关键词**: `时尚图像描述` `检索增强生成` `多服装检测` `属性推理` `大型语言模型` `服装标签生成` `CLIP-FAISS` `领域泛化`

## 📋 核心要点

1. 现有端到端时尚图像描述模型在属性保真度和领域泛化方面存在不足，难以准确描述服装细节和风格。
2. 提出一种检索增强框架，利用多服装检测、属性推理和LLM提示，生成更准确、更具风格的时尚描述和标签。
3. 实验表明，该框架在属性覆盖率和事实基础方面优于基线模型BLIP，具有更好的泛化能力和可扩展性。

## 📝 摘要（中文）

本文提出了一种检索增强框架，用于自动生成时尚图像的描述和标签。该框架结合了多服装检测、属性推理和大型语言模型（LLM）提示。旨在为时尚图像生成视觉上有关联、描述性强且风格有趣的文本，克服了端到端描述器在属性保真度和领域泛化方面的局限性。该流程结合了基于YOLO的检测器进行多服装定位，k-means聚类提取主色调，以及基于结构化产品索引的CLIP-FAISS检索模块进行面料和性别属性推断。这些属性与检索到的风格示例一起，创建了一个事实证据包，用于引导LLM生成类似人类的描述和上下文丰富的标签。使用微调的BLIP模型作为有监督的基线模型进行比较。实验结果表明，YOLO检测器在九个服装类别中获得了0.71的平均精度均值（mAP@0.5）。RAG-LLM流程生成了富有表现力的属性对齐描述，并在标签生成中实现了0.80的平均属性覆盖率，在50%阈值下实现了完全覆盖，而BLIP提供了更高的词汇重叠和更低的泛化能力。检索增强方法表现出更好的事实基础、更少的幻觉，并且在各种服装领域具有巨大的可扩展部署潜力。这些结果证明了检索增强生成作为一种有效且可解释的范例，用于自动和视觉基础的时尚内容生成。

## 🔬 方法详解

**问题定义**：现有时尚图像描述方法，特别是端到端模型，难以保证生成描述的属性准确性，并且在不同服装领域泛化能力较弱。这些模型容易产生幻觉，无法准确捕捉图像中服装的细节和风格特征。

**核心思路**：本文的核心思路是利用检索增强生成（RAG）框架，通过检索与图像相关的属性和风格信息，为大型语言模型（LLM）提供更丰富的事实依据，从而引导LLM生成更准确、更具风格的描述和标签。这种方法旨在减少幻觉，提高属性保真度，并增强领域泛化能力。

**技术框架**：该框架包含以下主要模块：1) 基于YOLO的多服装检测器，用于定位图像中的各个服装；2) k-means聚类，用于提取服装的主色调；3) CLIP-FAISS检索模块，基于结构化产品索引推断服装的面料和性别属性；4) LLM，用于生成描述和标签，其输入包括检测到的服装、提取的属性和检索到的风格示例。整个流程首先对图像进行分析，提取相关信息，然后将这些信息作为提示输入LLM，最后由LLM生成最终的描述和标签。

**关键创新**：该方法最重要的创新点在于将检索增强生成应用于时尚图像描述和标签生成任务。通过检索与图像相关的属性和风格信息，该方法能够为LLM提供更丰富的事实依据，从而生成更准确、更具风格的描述和标签。与传统的端到端模型相比，该方法具有更好的属性保真度、更少的幻觉和更强的领域泛化能力。

**关键设计**：在CLIP-FAISS检索模块中，构建了一个结构化的产品索引，用于存储服装的属性信息。在LLM提示方面，设计了一个有效的事实证据包，包括检测到的服装、提取的属性和检索到的风格示例。此外，还对BLIP模型进行了微调，作为有监督的基线模型进行比较。

## 📊 实验亮点

实验结果表明，该框架在九个服装类别中获得了0.71的平均精度均值（mAP@0.5）。RAG-LLM流程生成了富有表现力的属性对齐描述，并在标签生成中实现了0.80的平均属性覆盖率，在50%阈值下实现了完全覆盖。与基线模型BLIP相比，该框架具有更好的属性保真度、更少的幻觉和更强的领域泛化能力。

## 🎯 应用场景

该研究成果可应用于电商平台、时尚博客、社交媒体等领域，自动生成商品描述和标签，提高商品曝光率和用户参与度。此外，该技术还可用于辅助时尚设计师进行风格分析和灵感挖掘，以及为消费者提供个性化的时尚推荐。

## 📄 摘要（原文）

> This paper introduces the retrieval-augmented framework for automatic fashion caption and hashtag generation, combining multi-garment detection, attribute reasoning, and Large Language Model (LLM) prompting. The system aims to produce visually grounded, descriptive, and stylistically interesting text for fashion imagery, overcoming the limitations of end-to-end captioners that have problems with attribute fidelity and domain generalization. The pipeline combines a YOLO-based detector for multi-garment localization, k-means clustering for dominant color extraction, and a CLIP-FAISS retrieval module for fabric and gender attribute inference based on a structured product index. These attributes, together with retrieved style examples, create a factual evidence pack that is used to guide an LLM to generate human-like captions and contextually rich hashtags. A fine-tuned BLIP model is used as a supervised baseline model for comparison. Experimental results show that the YOLO detector is able to obtain a mean Average Precision (mAP@0.5) of 0.71 for nine categories of garments. The RAG-LLM pipeline generates expressive attribute-aligned captions and achieves mean attribute coverage of 0.80 with full coverage at the 50% threshold in hashtag generation, whereas BLIP gives higher lexical overlap and lower generalization. The retrieval-augmented approach exhibits better factual grounding, less hallucination, and great potential for scalable deployment in various clothing domains. These results demonstrate the use of retrieval-augmented generation as an effective and interpretable paradigm for automated and visually grounded fashion content generation.

