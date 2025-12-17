---
layout: default
title: Enhancing Geo-localization for Crowdsourced Flood Imagery via LLM-Guided Attention
---

# Enhancing Geo-localization for Crowdsourced Flood Imagery via LLM-Guided Attention

**arXiv**: [2512.11811v2](https://arxiv.org/abs/2512.11811) | [PDF](https://arxiv.org/pdf/2512.11811.pdf)

**作者**: Fengyi Xu, Jun Ma, Waishan Qiu, Cui Guo, Jack C. P. Cheng

**分类**: cs.CL, cs.AI, cs.CV, cs.CY

**发布日期**: 2025-11-25 (更新: 2025-12-16)

**备注**: Updated author list to include additional contributor. Revised title and improved methodology section based on collaborative feedback

---

## 💡 一句话要点

**VPR-AttLLM：利用LLM引导的注意力增强众包洪水图像的地理定位**

🎯 **匹配领域**: **支柱三：空间感知 (Perception & SLAM)**

**关键词**: `视觉位置识别` `地理定位` `大型语言模型` `注意力机制` `众包图像`

## 📋 核心要点

1. 现有视觉位置识别模型在处理众包图像时，由于视觉失真和跨源域偏移，性能显著下降，难以满足应急响应需求。
2. VPR-AttLLM利用大型语言模型的语义推理和地理知识，通过注意力机制引导描述符增强，提升VPR模型在复杂场景下的检索能力。
3. 实验表明，VPR-AttLLM在多个数据集上均能有效提升现有VPR模型的召回性能，在真实洪水图像上提升高达8%。

## 📝 摘要（中文）

本文提出了一种名为VPR-AttLLM的模型无关框架，该框架通过注意力引导的描述符增强，将大型语言模型（LLM）的语义推理和地理知识集成到现有的视觉位置识别（VPR）流程中。通过利用LLM识别城市环境中具有位置信息的区域并抑制视觉噪声，VPR-AttLLM提高了检索性能，而无需模型重新训练或额外数据。在扩展的基准测试（包括用真实社交媒体洪水图像丰富的SF-XL、既定查询集上的合成洪水场景和Mapillary照片）以及捕获形态各异城市景观的新HK-URBAN数据集上进行了全面评估。将VPR-AttLLM与三种最先进的VPR模型（CosPlace、EigenPlaces和SALAD）集成，始终如一地提高了召回性能，相对增益通常在1-3%之间，在最具挑战性的真实洪水图像上达到8%。除了可衡量的检索准确率提升外，本研究还为视觉检索系统中LLM引导的多模态融合建立了一种通用范例。通过将城市感知理论的原则嵌入到注意力机制中，VPR-AttLLM将类人空间推理与现代VPR架构联系起来。其即插即用设计、强大的跨源鲁棒性和可解释性突出了其在可扩展城市监测和众包危机图像快速地理定位方面的潜力。

## 🔬 方法详解

**问题定义**：论文旨在解决众包图像地理定位问题，特别是针对社交媒体上缺乏可靠地理元数据的洪水图像。现有视觉位置识别（VPR）方法在处理此类图像时，由于图像质量差、视角变化大、光照条件恶劣等因素，导致性能显著下降，难以满足应急响应的需求。

**核心思路**：论文的核心思路是利用大型语言模型（LLM）的语义理解和地理知识，引导VPR模型关注图像中与位置信息相关的区域，并抑制噪声干扰。通过这种方式，可以增强VPR模型对图像特征的提取能力，提高地理定位的准确性。

**技术框架**：VPR-AttLLM是一个模型无关的框架，可以与现有的VPR模型集成。其主要流程包括：1) 使用LLM分析图像，识别图像中与位置信息相关的区域；2) 基于LLM的分析结果，生成注意力权重，用于增强VPR模型的图像描述符；3) 使用增强后的描述符进行视觉位置检索。

**关键创新**：该方法最重要的创新点在于将LLM的语义理解能力融入到VPR任务中，通过注意力机制引导模型关注图像中与位置信息相关的区域。这种方法有效地利用了LLM的知识，提高了VPR模型在复杂场景下的鲁棒性和准确性。与现有方法相比，VPR-AttLLM无需重新训练VPR模型或收集额外的数据，具有更强的通用性和实用性。

**关键设计**：VPR-AttLLM的关键设计包括：1) 使用预训练的LLM（如GPT-3）进行图像分析，提取图像中的语义信息和地理知识；2) 设计注意力机制，根据LLM的分析结果，对图像的不同区域赋予不同的权重；3) 将注意力权重与VPR模型的图像描述符进行融合，生成增强后的描述符。具体的参数设置和网络结构取决于所使用的VPR模型。

## 📊 实验亮点

实验结果表明，VPR-AttLLM能够显著提升现有VPR模型的性能。在SF-XL数据集上，与CosPlace、EigenPlaces和SALAD等基线模型相比，VPR-AttLLM的召回率分别提升了1-3%。在最具挑战性的真实洪水图像上，VPR-AttLLM的召回率提升高达8%。此外，VPR-AttLLM在HK-URBAN数据集上也表现出良好的性能，证明了其在不同城市景观下的泛化能力。

## 🎯 应用场景

该研究成果可应用于城市应急管理、灾害监测、智能交通等领域。通过快速准确地定位众包图像，可以帮助应急响应人员及时了解灾情，制定合理的救援方案。此外，该方法还可以用于城市规划、环境监测等领域，为城市管理提供更全面的信息支持。未来，该技术有望应用于更广泛的视觉检索任务，提升多模态信息融合的能力。

## 📄 摘要（原文）

> Crowdsourced street-view imagery from social media provides real-time visual evidence of urban flooding and other crisis events, yet it often lacks reliable geographic metadata for emergency response. Existing image geo-localization approaches, also known as Visual Place Recognition (VPR) models, exhibit substantial performance degradation when applied to such imagery due to visual distortions and domain shifts in cross-source scenarios. This paper presents VPR-AttLLM, a model-agnostic framework that integrates the semantic reasoning and geo-knowledge of Large Language Models (LLMs) into established VPR pipelines through attention-guided descriptor enhancement. By leveraging LLMs to identify location-informative regions within the city context and suppress visual noise, VPR-AttLLM improves retrieval performance without requiring model retraining or additional data. Comprehensive evaluations are conducted on extended benchmarks including SF-XL enriched with real social-media flood images, synthetic flooding scenarios over established query sets and Mapillary photos, and a new HK-URBAN dataset capturing morphologically distinct cityscapes. Integrating VPR-AttLLM with three state-of-the-art VPR models-CosPlace, EigenPlaces, and SALAD-consistently improves recall performance, yielding relative gains typically between 1-3% and reaching up to 8% on the most challenging real flood imagery. Beyond measurable gains in retrieval accuracy, this study establishes a generalizable paradigm for LLM-guided multimodal fusion in visual retrieval systems. By embedding principles from urban perception theory into attention mechanisms, VPR-AttLLM bridges human-like spatial reasoning with modern VPR architectures. Its plug-and-play design, strong cross-source robustness, and interpretability highlight its potential for scalable urban monitoring and rapid geo-localization of crowdsourced crisis imagery.

