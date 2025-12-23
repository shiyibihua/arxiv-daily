---
layout: default
title: Can AI Dream of Unseen Galaxies? Conditional Diffusion Model for Galaxy Morphology Augmentation
---

# Can AI Dream of Unseen Galaxies? Conditional Diffusion Model for Galaxy Morphology Augmentation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.16233" class="toolbar-btn" target="_blank">📄 arXiv: 2506.16233v1</a>
  <a href="https://arxiv.org/pdf/2506.16233.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.16233v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.16233v1', 'Can AI Dream of Unseen Galaxies? Conditional Diffusion Model for Galaxy Morphology Augmentation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Chenrui Ma, Zechang Sun, Tao Jing, Zheng Cai, Yuan-Sen Ting, Song Huang, Mingyu Li

**分类**: astro-ph.GA, cs.LG

**发布日期**: 2025-06-19

**备注**: We have submitted to AAS journals. See another independent work for further reference -- Category-based Galaxy Image Generation via Diffusion Models (Fan, Tang et al.). Comments are welcome

---

## 💡 一句话要点

**提出条件扩散模型以解决天文数据稀缺问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `条件扩散模型` `星系图像合成` `稀有对象检测` `机器学习` `天文学` `数据增强` `视觉特征识别`

## 📋 核心要点

1. 现有机器学习模型在大规模天文调查中泛化能力不足，尤其是对稀有天体的检测面临挑战。
2. 本文提出了一种条件扩散模型，通过合成星系图像来增强训练数据，从而提高模型的泛化能力。
3. 实验结果表明，合成图像的使用使标准形态分类的完整性和纯度提升了30%，稀有对象检测的实例数量也显著增加。

## 📝 摘要（中文）

观测天文学依赖于视觉特征识别来检测重要的天体物理现象。尽管机器学习在这一过程中日益自动化，但由于标注数据集的代表性有限，模型在大规模调查中常常难以泛化，尤其是对于稀有但科学价值高的对象。为此，本文提出了一种条件扩散模型，用于合成真实的星系图像，以增强机器学习训练数据。利用Galaxy Zoo 2数据集，模型生成多样化且高保真的星系图像，紧密符合指定的形态特征条件。此外，该模型还支持生成性外推，将良好标注的数据投射到未见领域，促进稀有对象的检测。将合成图像整合到机器学习流程中，标准形态分类的性能提升了多达30%。

## 🔬 方法详解

**问题定义**：本文旨在解决天文学中标注数据稀缺导致的机器学习模型泛化能力不足的问题。现有方法在处理稀有天体时，往往依赖于有限的视觉特征标注，导致检测效果不佳。

**核心思路**：提出的条件扩散模型通过合成高保真的星系图像，增强训练数据的多样性和代表性，从而提高模型在稀有对象检测中的性能。

**技术框架**：模型基于Galaxy Zoo 2数据集，包含志愿者标注的星系图像与特征对。模型的主要模块包括条件生成网络和图像合成模块，能够根据指定的形态特征生成相应的星系图像。

**关键创新**：本研究的创新点在于利用条件扩散模型进行图像合成，能够有效填补稀缺标注数据与广阔参数空间之间的空白，显著提高稀有对象的检测能力。

**关键设计**：模型设计中采用了特定的损失函数以确保生成图像的高保真度，并通过调节网络结构参数来优化生成效果。

## 📊 实验亮点

实验结果显示，使用合成图像后，标准形态分类的完整性和纯度提升了30%。在稀有对象检测方面，以早型星系为例，检测实例数量从352增加到872，显著优于基于视觉检查的先前研究。

## 🎯 应用场景

该研究的潜在应用领域包括天文学中的稀有天体检测、数据增强以及机器学习模型的训练。通过合成高质量的星系图像，能够有效提升模型的泛化能力，为未来的天文观测和研究提供更为丰富的数据支持，推动天文学的发展。

## 📄 摘要（原文）

> Observational astronomy relies on visual feature identification to detect critical astrophysical phenomena. While machine learning (ML) increasingly automates this process, models often struggle with generalization in large-scale surveys due to the limited representativeness of labeled datasets -- whether from simulations or human annotation -- a challenge pronounced for rare yet scientifically valuable objects. To address this, we propose a conditional diffusion model to synthesize realistic galaxy images for augmenting ML training data. Leveraging the Galaxy Zoo 2 dataset which contains visual feature -- galaxy image pairs from volunteer annotation, we demonstrate that our model generates diverse, high-fidelity galaxy images closely adhere to the specified morphological feature conditions. Moreover, this model enables generative extrapolation to project well-annotated data into unseen domains and advancing rare object detection. Integrating synthesized images into ML pipelines improves performance in standard morphology classification, boosting completeness and purity by up to 30\% across key metrics. For rare object detection, using early-type galaxies with prominent dust lane features ( $\sim$0.1\% in GZ2 dataset) as a test case, our approach doubled the number of detected instances from 352 to 872, compared to previous studies based on visual inspection. This study highlights the power of generative models to bridge gaps between scarce labeled data and the vast, uncharted parameter space of observational astronomy and sheds insight for future astrophysical foundation model developments. Our project homepage is available at https://galaxysd-webpage.streamlit.app/.

