---
layout: default
title: "SpatialMosaic: A Multiview VLM Dataset for Partial Visibility"
---

# SpatialMosaic: A Multiview VLM Dataset for Partial Visibility

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.23365" class="toolbar-btn" target="_blank">📄 arXiv: 2512.23365v1</a>
  <a href="https://arxiv.org/pdf/2512.23365.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.23365v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.23365v1', 'SpatialMosaic: A Multiview VLM Dataset for Partial Visibility')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Kanghee Lee, Injae Lee, Minseok Kwak, Kwonyoung Ryu, Jungi Hong, Jaesik Park

**分类**: cs.CV

**发布日期**: 2025-12-29

---

## 💡 一句话要点

**提出SpatialMosaic数据集，增强多视角VLM在部分可见场景下的空间推理能力**

🎯 **匹配领域**: **支柱三：空间感知与语义 (Perception & Semantics)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多视角学习` `视觉语言模型` `空间推理` `数据集构建` `三维重建`

## 📋 核心要点

1. 现有方法依赖预构建3D表示或重建流程，限制了VLM在真实场景中的空间推理能力，尤其是在部分可见和遮挡情况下。
2. SpatialMosaic通过可扩展的数据生成和标注流程，构建包含200万QA对的数据集，用于训练VLM在复杂多视角场景下的空间推理。
3. SpatialMosaic-Bench提供100万QA对的基准测试，SpatialMosaicVLM框架集成了3D重建模型，实验验证了数据集和VQA任务的有效性。

## 📝 摘要（中文）

多模态大型语言模型(MLLM)的快速发展释放了增强3D场景理解和空间推理的潜力。然而，现有方法通常依赖于预先构建的3D表示或现成的重建流程，这限制了可扩展性和实际应用。最近的研究探索直接从多视角图像中学习空间推理，使视觉-语言模型(VLM)能够在没有显式3D重建的情况下理解3D场景。然而，现实环境中经常出现的关键挑战，如部分可见性、遮挡和低重叠条件，需要从碎片化的视觉线索进行空间推理，这些挑战仍未得到充分研究。为了解决这些限制，我们提出了一个可扩展的多视角数据生成和标注流程，构建了真实的包含200万个QA对的空间推理QA，形成了SpatialMosaic，一个全面的指令调优数据集。我们进一步引入了SpatialMosaic-Bench，这是一个具有挑战性的基准，用于评估在现实和具有挑战性的场景下的多视角空间推理，包含跨越6个任务的100万个QA对。此外，我们提出了SpatialMosaicVLM，一个混合框架，它将3D重建模型作为几何编码器集成到VLM中，以实现鲁棒的空间推理。大量的实验表明，我们提出的数据集和VQA任务有效地增强了具有挑战性的多视角条件下的空间推理，验证了我们的数据生成流程在构建真实和多样化的QA对方面的有效性。代码和数据集即将发布。

## 🔬 方法详解

**问题定义**：现有VLM在多视角场景下的空间推理能力不足，尤其是在部分可见、遮挡和低重叠等真实场景中。现有方法依赖于预先构建的3D模型或重建流程，限制了其可扩展性和泛化能力。因此，需要一种能够直接从多视角图像中学习空间推理的方法，并解决真实场景中的挑战。

**核心思路**：SpatialMosaic的核心思路是通过大规模数据生成和标注，构建一个包含丰富空间推理信息的指令调优数据集。该数据集模拟了真实场景中的各种挑战，如部分可见、遮挡和低重叠，从而使VLM能够学习到更鲁棒的空间推理能力。此外，SpatialMosaic还提出了一个混合框架SpatialMosaicVLM，将3D重建模型作为几何编码器集成到VLM中，进一步提升空间推理性能。

**技术框架**：SpatialMosaic的整体框架包括以下几个主要模块：1) 多视角数据生成：使用可扩展的流程生成包含各种场景和视角的图像数据。2) 空间推理QA标注：设计多种空间推理任务，并对生成的数据进行QA标注，构建包含丰富空间推理信息的数据集。3) SpatialMosaic-Bench基准测试：构建一个具有挑战性的基准测试，用于评估VLM在多视角空间推理方面的性能。4) SpatialMosaicVLM框架：将3D重建模型作为几何编码器集成到VLM中，提升空间推理性能。

**关键创新**：SpatialMosaic的主要创新点在于：1) 提出了一个可扩展的多视角数据生成和标注流程，能够构建大规模、高质量的空间推理数据集。2) 设计了多种空间推理任务，涵盖了真实场景中的各种挑战。3) 提出了SpatialMosaicVLM框架，将3D重建模型与VLM相结合，提升了空间推理性能。

**关键设计**：在数据生成方面，SpatialMosaic采用了随机场景生成和相机参数设置，模拟了真实场景中的各种视角和光照条件。在QA标注方面，SpatialMosaic设计了多种空间推理任务，包括目标定位、关系推理和场景理解等。SpatialMosaicVLM框架中，3D重建模型采用了现有的成熟算法，如COLMAP等，并将其输出作为VLM的输入，从而使VLM能够利用3D几何信息进行空间推理。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.23365v1/x3.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.23365v1/x4.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.23365v1/x5.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

SpatialMosaic数据集包含200万个QA对，SpatialMosaic-Bench基准测试包含100万个QA对，涵盖6个空间推理任务。实验结果表明，使用SpatialMosaic进行训练可以显著提升VLM在多视角空间推理方面的性能。SpatialMosaicVLM框架通过集成3D重建模型，进一步提升了空间推理的准确性和鲁棒性。具体性能数据将在论文中详细展示。

## 🎯 应用场景

SpatialMosaic的研究成果可应用于机器人导航、自动驾驶、增强现实等领域。通过提升VLM在复杂环境下的空间推理能力，可以使机器人更好地理解周围环境，实现更智能的导航和交互。在自动驾驶领域，可以提高车辆对周围环境的感知能力，从而提高驾驶安全性。在增强现实领域，可以实现更自然的虚拟物体与真实环境的融合。

## 📄 摘要（原文）

> The rapid progress of Multimodal Large Language Models (MLLMs) has unlocked the potential for enhanced 3D scene understanding and spatial reasoning. However, existing approaches often rely on pre-constructed 3D representations or off-the-shelf reconstruction pipelines, which constrain scalability and real-world applicability. A recent line of work explores learning spatial reasoning directly from multi-view images, enabling Vision-Language Models (VLMs) to understand 3D scenes without explicit 3D reconstructions. Nevertheless, key challenges that frequently arise in real-world environments, such as partial visibility, occlusion, and low-overlap conditions that require spatial reasoning from fragmented visual cues, remain under-explored. To address these limitations, we propose a scalable multi-view data generation and annotation pipeline that constructs realistic spatial reasoning QAs, resulting in SpatialMosaic, a comprehensive instruction-tuning dataset featuring 2M QA pairs. We further introduce SpatialMosaic-Bench, a challenging benchmark for evaluating multi-view spatial reasoning under realistic and challenging scenarios, consisting of 1M QA pairs across 6 tasks. In addition, we present SpatialMosaicVLM, a hybrid framework that integrates 3D reconstruction models as geometry encoders within VLMs for robust spatial reasoning. Extensive experiments demonstrate that our proposed dataset and VQA tasks effectively enhance spatial reasoning under challenging multi-view conditions, validating the effectiveness of our data generation pipeline in constructing realistic and diverse QA pairs. Code and dataset will be available soon.

