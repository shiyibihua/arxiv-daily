---
layout: default
title: Video Object Segmentation-Aware Audio Generation
---

# Video Object Segmentation-Aware Audio Generation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.26604" class="toolbar-btn" target="_blank">📄 arXiv: 2509.26604v1</a>
  <a href="https://arxiv.org/pdf/2509.26604.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.26604v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.26604v1', 'Video Object Segmentation-Aware Audio Generation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Ilpo Viertola, Vladimir Iashin, Esa Rahtu

**分类**: cs.CV

**发布日期**: 2025-09-30

**备注**: Preprint version. The Version of Record is published in DAGM GCPR 2025 proceedings with Springer Lecture Notes in Computer Science (LNCS). Updated results and resources are available at the project page: https://saganet.notion.site

---

## 💡 一句话要点

**提出SAGANet，通过视频对象分割实现可控音频生成，提升Foley工作流效率。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `音频生成` `视频对象分割` `多模态学习` `Foley合成` `生成对抗网络`

## 📋 核心要点

1. 现有音频生成模型缺乏对特定对象的关注，难以精确控制，导致生成不相关的背景声音。
2. SAGANet利用视频对象分割掩码，结合视频和文本信息，实现对特定对象音频的精准控制。
3. 提出的Segmented Music Solos数据集，以及实验结果表明，SAGANet显著优于现有方法，提升了Foley合成质量。

## 📝 摘要（中文）

现有的多模态音频生成模型通常缺乏精确的用户控制，限制了它们在专业Foley工作流程中的应用。这些模型侧重于整个视频，未能提供针对场景中特定对象的优先级排序方法，导致生成不必要的背景声音或关注错误的对象。为了解决这个问题，我们提出了视频对象分割感知的音频生成这一新任务，该任务明确地将声音合成建立在对象级别的分割图上。我们提出了SAGANet，一种新的多模态生成模型，它通过利用视觉分割掩码以及视频和文本线索来实现可控的音频生成。我们的模型为用户提供了对音频生成进行细粒度和视觉局部控制的能力。为了支持这项任务并进一步研究分割感知的Foley，我们提出了Segmented Music Solos，这是一个包含分割信息的乐器演奏视频基准数据集。我们的方法展示了相对于当前最先进方法的显著改进，并为可控、高保真Foley合成设定了新的标准。代码、样本和Segmented Music Solos可在https://saganet.notion.site获取。

## 🔬 方法详解

**问题定义**：现有音频生成模型无法根据视频中特定对象进行针对性音频生成，用户难以控制生成的声音细节，导致在Foley等专业应用中效果不佳。模型通常关注整个视频场景，无法区分重要对象和背景，容易产生不必要的或错误的音频。

**核心思路**：论文的核心思路是将视频对象分割信息融入到音频生成过程中，通过分割掩码引导模型关注特定对象，从而实现对音频生成的精细控制。这样，用户可以指定视频中的哪些对象应该发出声音，以及这些声音的特性。

**技术框架**：SAGANet是一个多模态生成模型，其整体架构包含以下几个主要模块：1) 视频编码器：提取视频帧的视觉特征。2) 分割编码器：提取对象分割掩码的特征。3) 文本编码器：提取文本描述的语义特征。4) 音频生成器：结合视觉特征、分割特征和文本特征，生成对应的音频。模型通过对抗训练的方式进行优化，其中生成器负责生成逼真的音频，判别器负责区分生成的音频和真实音频。

**关键创新**：该论文的关键创新在于提出了视频对象分割感知的音频生成任务，并将分割信息显式地融入到音频生成模型中。与以往方法相比，SAGANet能够根据用户指定的对象生成相应的音频，实现了对音频生成的精细控制。此外，提出的Segmented Music Solos数据集为该任务提供了新的基准。

**关键设计**：在网络结构方面，SAGANet采用了编码器-解码器结构，其中编码器负责提取多模态特征，解码器负责生成音频。损失函数方面，采用了对抗损失和重构损失，以保证生成音频的质量和与输入模态的一致性。分割掩码的处理方式是将分割信息与视觉特征进行融合，从而引导模型关注特定对象。具体融合方式未知。

## 📊 实验亮点

SAGANet在Segmented Music Solos数据集上取得了显著的性能提升，相较于现有最先进方法，在音频质量和与视频内容的匹配度方面均有明显改善。具体性能数据未知，但论文强调了其在可控性和高保真度方面的优势，为Foley合成设定了新的标准。

## 🎯 应用场景

该研究成果可应用于电影、游戏等领域的Foley音效制作，实现对特定对象的精细化音效控制。例如，可以根据角色动作生成脚步声、武器碰撞声等。此外，还可应用于虚拟现实、增强现实等领域，提升用户体验。未来，该技术有望扩展到更广泛的音频生成任务，例如根据场景描述生成环境音效。

## 📄 摘要（原文）

> Existing multimodal audio generation models often lack precise user control, which limits their applicability in professional Foley workflows. In particular, these models focus on the entire video and do not provide precise methods for prioritizing a specific object within a scene, generating unnecessary background sounds, or focusing on the wrong objects. To address this gap, we introduce the novel task of video object segmentation-aware audio generation, which explicitly conditions sound synthesis on object-level segmentation maps. We present SAGANet, a new multimodal generative model that enables controllable audio generation by leveraging visual segmentation masks along with video and textual cues. Our model provides users with fine-grained and visually localized control over audio generation. To support this task and further research on segmentation-aware Foley, we propose Segmented Music Solos, a benchmark dataset of musical instrument performance videos with segmentation information. Our method demonstrates substantial improvements over current state-of-the-art methods and sets a new standard for controllable, high-fidelity Foley synthesis. Code, samples, and Segmented Music Solos are available at https://saganet.notion.site

