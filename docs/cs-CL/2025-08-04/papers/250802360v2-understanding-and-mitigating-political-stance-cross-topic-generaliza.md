---
layout: default
title: Understanding and Mitigating Political Stance Cross-topic Generalization in Large Language Models
---

# Understanding and Mitigating Political Stance Cross-topic Generalization in Large Language Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.02360" class="toolbar-btn" target="_blank">📄 arXiv: 2508.02360v2</a>
  <a href="https://arxiv.org/pdf/2508.02360.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.02360v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.02360v2', 'Understanding and Mitigating Political Stance Cross-topic Generalization in Large Language Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jiayi Zhang, Shu Yang, Junchao Wu, Derek F. Wong, Di Wang

**分类**: cs.CL

**发布日期**: 2025-08-04 (更新: 2025-11-16)

---

## 💡 一句话要点

**提出PNLAC与InhibitFT以解决政治立场跨主题泛化问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `政治立场` `跨主题泛化` `大型语言模型` `神经元识别` `微调方法` `激活对比` `抑制微调` `模型鲁棒性`

## 📋 核心要点

1. 现有方法在政治主题微调时，导致模型在无关主题上的立场出现意外变化，缺乏对内部机制的深入理解。
2. 论文提出PNLAC方法，通过激活对比识别政治神经元，并引入InhibitFT抑制微调策略，以减轻跨主题泛化问题。
3. 实验结果显示，InhibitFT方法平均减少了20%的跨主题立场泛化，同时仅需抑制5%的神经元即可实现有效减轻。

## 📝 摘要（中文）

对大型语言模型进行政治主题微调会显著影响其在多个议题上的政治立场，并无意中影响与之无关的主题。尽管已有研究提出了这一问题，但对这些立场的内部表征及导致意外跨主题泛化的机制仍缺乏理解。本文从神经元层面系统探讨了这一现象的内部机制，并提出了通过激活对比的政治神经元定位（PNLAC）方法，识别出两种不同类型的政治神经元。基于这些发现，本文引入了一种基于抑制的微调方法（InhibitFT），有效减轻了跨主题立场泛化。实验结果表明，所识别的神经元类型在多个模型和数据集上具有鲁棒性，InhibitFT平均减少了20%的跨主题立场泛化，同时保持了主题特定性能。

## 🔬 方法详解

**问题定义**：本文旨在解决大型语言模型在政治主题微调后，导致的跨主题立场泛化问题。现有方法未能有效识别和控制这种现象的内部机制，导致模型在无关主题上的表现受到影响。

**核心思路**：论文提出的核心思路是通过激活对比方法（PNLAC）识别政治神经元，并利用抑制微调（InhibitFT）策略来减轻跨主题立场泛化。这样的设计旨在精准定位影响模型立场的神经元类型，从而实现有效的干预。

**技术框架**：整体架构包括两个主要模块：首先是政治神经元的识别模块，通过激活对比实验识别出一般政治神经元和主题特定神经元；其次是抑制微调模块，通过选择性抑制部分神经元来减轻跨主题泛化。

**关键创新**：最重要的技术创新在于提出了PNLAC方法，能够有效识别不同类型的政治神经元，并通过InhibitFT方法实现了跨主题立场泛化的显著减轻。这与现有方法的本质区别在于，前者关注神经元层面的干预，而后者通常只关注模型整体性能。

**关键设计**：在实验中，选择性抑制5%的神经元被证明足以有效减轻跨主题立场泛化。此外，损失函数和网络结构的设计也经过精心调整，以确保在减轻泛化的同时保持主题特定的性能。

## 📊 实验亮点

实验结果表明，InhibitFT方法在多个模型和数据集上平均减少了20%的跨主题立场泛化，且仅需抑制5%的神经元即可实现有效干预。这一结果显示了所提出方法的有效性和鲁棒性，为大型语言模型的微调提供了新的方向。

## 🎯 应用场景

该研究的潜在应用领域包括社交媒体内容生成、政治舆论分析和信息推荐系统等。通过有效控制模型的政治立场，能够提高模型在多样化主题上的表现，减少偏见传播，促进更公正的信息交流。未来，该方法可能为其他领域的模型微调提供新的思路和方法。

## 📄 摘要（原文）

> Fine-tuning Large Language Models on a political topic will significantly manipulate their political stance on various issues and unintentionally affect their stance on unrelated topics. While previous studies have proposed this issue, there is still a lack of understanding regarding the internal representations of these stances and the mechanisms that lead to unintended cross-topic generalization. In this paper, we systematically explore the internal mechanisms underlying this phenomenon from a neuron-level perspective and how to mitigate the cross-topic generalization of political fine-tuning. Firstly, we propose Political Neuron Localization through Activation Contrasting (PNLAC) to identify two distinct types of political neurons: general political neurons, which govern stance across multiple political topics, and topic-specific neurons} that affect the model's political stance on individual topics. We find the existence of these political neuron types across four models and datasets through activation patching experiments. Leveraging these insights, we introduce InhibitFT, an inhibition-based fine-tuning method, effectively mitigating the cross-topic stance generalization. Experimental results demonstrate the robustness of identified neuron types across various models and datasets, and show that InhibitFT significantly reduces the cross-topic stance generalization by 20% on average, while preserving topic-specific performance. Moreover, we demonstrate that selectively inhibiting only 5% of neurons is sufficient to effectively mitigate the cross-topic stance generalization.

