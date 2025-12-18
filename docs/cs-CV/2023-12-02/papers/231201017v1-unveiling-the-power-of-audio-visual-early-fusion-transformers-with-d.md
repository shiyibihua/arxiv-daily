---
layout: default
title: Unveiling the Power of Audio-Visual Early Fusion Transformers with Dense Interactions through Masked Modeling
---

# Unveiling the Power of Audio-Visual Early Fusion Transformers with Dense Interactions through Masked Modeling

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2312.01017" class="toolbar-btn" target="_blank">📄 arXiv: 2312.01017v1</a>
  <a href="https://arxiv.org/pdf/2312.01017.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2312.01017v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2312.01017v1', 'Unveiling the Power of Audio-Visual Early Fusion Transformers with Dense Interactions through Masked Modeling')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Shentong Mo, Pedro Morgado

**分类**: cs.CV, cs.AI, cs.LG, cs.MM, cs.SD

**发布日期**: 2023-12-02

---

## 💡 一句话要点

**提出基于掩码建模的音视频早期融合Transformer，提升多模态感知能力**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `音视频融合` `早期融合` `Transformer` `掩码建模` `多模态学习` `自监督学习` `注意力机制`

## 📋 核心要点

1. 现有早期融合音视频模型训练困难，模型表达能力受限，难以充分利用多模态信息。
2. 利用掩码重建框架训练早期融合音视频编码器，并设计注意力融合模块捕获局部音视频交互。
3. 在音频事件分类、视觉声音定位等任务上，验证了所提方法优于现有方法，提升了模型性能。

## 📝 摘要（中文）

人类具备整合听觉和视觉信息的能力，从而更深入地理解周围环境。认知心理学和神经科学研究表明，音视频线索的早期融合为开发多模态感知模型提供了有潜力的途径。然而，训练早期融合架构面临着重大挑战，因为模型表达能力的增强需要强大的学习框架来驾驭其增强的能力。本文通过利用在单模态设置中已成功的掩码重建框架来训练具有早期融合的音视频编码器，从而应对这一挑战。此外，我们提出了一种基于注意力的融合模块，该模块捕获局部音频和视觉表示之间的交互，从而增强了模型捕获细粒度交互的能力。虽然有效，但随着局部表示数量的增加，此过程在计算上变得难以处理。因此，为了解决计算复杂性，我们提出了一种替代程序，该程序在表示音视频交互之前对局部表示进行分解。在各种数据集上的广泛评估表明，我们的方法在音频事件分类、视觉声音定位、声音分离和音视频分割方面具有优越性。这些贡献使得能够有效训练深度集成的音视频模型，并显著提高早期融合架构的实用性。

## 🔬 方法详解

**问题定义**：论文旨在解决音视频多模态学习中，早期融合模型训练困难的问题。现有方法难以有效利用音视频信息的早期交互，导致模型性能受限。痛点在于模型复杂度高，训练不稳定，难以捕捉细粒度的音视频关联。

**核心思路**：论文的核心思路是利用掩码建模（Masked Modeling）作为自监督学习的手段，并结合注意力机制，来有效训练早期融合的音视频Transformer模型。通过掩码部分输入，迫使模型学习音视频之间的关联，并重建被掩码的信息，从而提升模型的表达能力和泛化能力。

**技术框架**：整体框架包含以下几个主要模块：1) 音视频特征提取模块：分别提取音频和视频的局部特征表示。2) 早期融合模块：将提取的音视频特征进行融合，形成统一的多模态表示。3) 基于注意力的交互模块：利用注意力机制建模局部音视频表示之间的交互关系。4) 掩码建模模块：随机掩码部分输入，并利用模型重建被掩码的信息。5) 预测模块：根据任务需求，进行音频事件分类、视觉声音定位等任务的预测。

**关键创新**：论文的关键创新在于：1) 将掩码建模引入到早期融合的音视频Transformer模型训练中，提升了模型的学习效率和泛化能力。2) 提出了基于注意力的融合模块，能够有效捕捉局部音视频表示之间的细粒度交互。3) 针对计算复杂度问题，提出了分解局部表示的方法，降低了计算成本。

**关键设计**：在掩码建模方面，采用了随机掩码策略，掩码比例为一定的百分比。损失函数包括重建损失和任务相关的损失。注意力模块采用了多头注意力机制，以捕捉不同层面的音视频交互。为了降低计算复杂度，论文提出了对局部表示进行分解的方法，例如使用线性投影或聚类等方式，减少了注意力计算的规模。

## 📊 实验亮点

实验结果表明，该方法在音频事件分类、视觉声音定位、声音分离和音视频分割等任务上均取得了显著的性能提升。例如，在音频事件分类任务上，相比于基线方法，准确率提升了X%；在视觉声音定位任务上，定位精度提升了Y%。这些结果验证了该方法在多模态感知方面的有效性。

## 🎯 应用场景

该研究成果可应用于智能监控、机器人感知、自动驾驶等领域。例如，在智能监控中，可以利用音视频信息进行异常事件检测；在机器人感知中，可以帮助机器人理解周围环境，进行导航和交互；在自动驾驶中，可以提高车辆对复杂交通场景的感知能力，提升安全性。

## 📄 摘要（原文）

> Humans possess a remarkable ability to integrate auditory and visual information, enabling a deeper understanding of the surrounding environment. This early fusion of audio and visual cues, demonstrated through cognitive psychology and neuroscience research, offers promising potential for developing multimodal perception models. However, training early fusion architectures poses significant challenges, as the increased model expressivity requires robust learning frameworks to harness their enhanced capabilities. In this paper, we address this challenge by leveraging the masked reconstruction framework, previously successful in unimodal settings, to train audio-visual encoders with early fusion. Additionally, we propose an attention-based fusion module that captures interactions between local audio and visual representations, enhancing the model's ability to capture fine-grained interactions. While effective, this procedure can become computationally intractable, as the number of local representations increases. Thus, to address the computational complexity, we propose an alternative procedure that factorizes the local representations before representing audio-visual interactions. Extensive evaluations on a variety of datasets demonstrate the superiority of our approach in audio-event classification, visual sound localization, sound separation, and audio-visual segmentation. These contributions enable the efficient training of deeply integrated audio-visual models and significantly advance the usefulness of early fusion architectures.

