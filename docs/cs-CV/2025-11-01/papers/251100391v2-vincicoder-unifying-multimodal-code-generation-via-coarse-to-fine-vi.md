---
layout: default
title: VinciCoder: Unifying Multimodal Code Generation via Coarse-to-fine Visual Reinforcement Learning
---

# VinciCoder: Unifying Multimodal Code Generation via Coarse-to-fine Visual Reinforcement Learning

<div class="paper-toolbar">
  <div class="toolbar-left">
    <a href="https://arxiv.org/abs/2511.00391" target="_blank" class="toolbar-btn">arXiv: 2511.00391v2</a>
    <a href="https://arxiv.org/pdf/2511.00391.pdf" target="_blank" class="toolbar-btn">PDF</a>
  </div>
  <div class="toolbar-right">
    <button class="toolbar-btn favorite-btn" data-arxiv-id="2511.00391v2" 
            onclick="toggleFavorite(this, '2511.00391v2', 'VinciCoder: Unifying Multimodal Code Generation via Coarse-to-fine Visual Reinforcement Learning')" title="收藏">
      ☆ 收藏
    </button>
    <button class="toolbar-btn share-btn" onclick="copyLink()" title="复制链接">
      🔗 分享
    </button>
  </div>
</div>


**作者**: Xuanle Zhao, Deyang Jiang, Zhixiong Zeng, Lei Chen, Haibo Qiu, Jing Huang, Yufeng Zhong, Liming Zheng, Yilin Cao, Lin Ma

**分类**: cs.CV

**发布日期**: 2025-11-01 (更新: 2025-11-27)

**备注**: 15 pages, 11 figures

**🔗 代码/项目**: [GITHUB](https://github.com/DocTron-hub/VinciCoder)

---

## 💡 一句话要点

**VinciCoder：通过粗到细视觉强化学习统一多模态代码生成**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `多模态代码生成` `视觉强化学习` `粗到细学习` `视觉-语言模型` `代码智能`

## 📋 核心要点

1. 现有视觉-语言模型在多模态代码生成中依赖单任务训练，缺乏通用视觉代码智能。
2. VinciCoder通过两阶段训练框架，结合监督微调和粗到细的视觉强化学习来提升性能。
3. 实验表明，VinciCoder在多个基准测试中超越了现有开源模型，验证了方法的有效性。

## 📝 摘要（中文）

多模态代码生成已引起研究界的广泛关注。尽管最近的视觉-语言模型（VLMs）在诸如图表到代码生成等特定任务上取得了显著成功，但它们对单任务训练方案的依赖阻碍了通用视觉代码智能的发展。本文提出了VinciCoder，一个统一的多模态代码生成模型，通过两阶段训练框架解决了这一限制。首先，构建了一个大规模的监督微调（SFT）语料库，包含160万个图像-代码对，用于直接代码生成和基于视觉的代码改进任务。其次，引入了一种视觉强化学习（ViRL）策略，该策略采用粗到细的奖励机制，通过计算局部和全局图像块之间的视觉相似性来提高视觉保真度。在各种多模态代码生成基准上的大量实验表明，VinciCoder实现了最先进的性能，超越了最近的开源模型。消融研究进一步验证了我们提出的粗到细ViRL策略的有效性。数据、代码和模型可在https://github.com/DocTron-hub/VinciCoder获取。

## 🔬 方法详解

**问题定义**：论文旨在解决多模态代码生成任务中，现有视觉-语言模型（VLMs）泛化能力不足的问题。现有方法通常针对特定任务进行训练，缺乏在不同视觉输入和代码生成任务之间的迁移能力，限制了其通用性和实用性。

**核心思路**：VinciCoder的核心思路是通过一个统一的模型框架，结合监督学习和强化学习，提升模型在不同多模态代码生成任务上的性能和泛化能力。通过粗到细的视觉强化学习，使模型能够更好地理解图像内容，并生成与之对应的代码。

**技术框架**：VinciCoder的训练框架包含两个主要阶段：1) 监督微调（SFT）：使用大规模图像-代码对数据集对模型进行预训练，使其具备初步的代码生成能力。2) 视觉强化学习（ViRL）：利用强化学习策略，通过奖励机制引导模型生成更符合视觉信息的代码。ViRL采用粗到细的奖励机制，分别从全局和局部图像块的视觉相似性来评估生成代码的质量。

**关键创新**：VinciCoder的关键创新在于其粗到细的视觉强化学习（ViRL）策略。传统的强化学习方法通常只关注整体的奖励，而忽略了图像的局部细节。VinciCoder通过分别计算全局和局部图像块的视觉相似性，能够更精细地评估生成代码的质量，从而提高视觉保真度。

**关键设计**：在ViRL阶段，奖励函数的设计至关重要。VinciCoder的奖励函数包含两部分：全局视觉相似性奖励和局部视觉相似性奖励。全局视觉相似性奖励衡量生成代码对应的图像与原始图像的整体相似度，局部视觉相似性奖励则关注图像的局部细节。通过调整两部分奖励的权重，可以控制模型对全局和局部信息的关注程度。具体的网络结构细节和参数设置在论文中有详细描述。

## 📊 实验亮点

VinciCoder在多个多模态代码生成基准测试中取得了state-of-the-art的性能，显著超越了现有的开源模型。消融实验表明，粗到细的视觉强化学习策略对性能提升起到了关键作用。具体性能数据和对比基线可在论文中查阅。

## 🎯 应用场景

VinciCoder具有广泛的应用前景，包括自动化图表生成、UI界面代码生成、图像描述生成代码等。该技术可以应用于软件开发、数据可视化、自动化报告生成等领域，提高开发效率和降低开发成本。未来，VinciCoder有望成为通用视觉代码智能的基础模型，赋能更多智能应用。

## 📄 摘要（原文）

> Multimodal code generation has garnered significant interest within the research community. Despite the notable success of recent vision-language models (VLMs) on specialized tasks like chart-to-code generation, their reliance on single-task training regimens fosters a narrow paradigm that hinders the development of generalized \textbf{VI}sio\textbf{N} \textbf{C}ode \textbf{I}ntelligence. In this work, we introduce \textbf{VinciCoder}, a unified multimodal code generation model that addresses this limitation via a two-stage training framework. We begin by constructing a large-scale Supervised Finetuning (SFT) corpus comprising 1.6M image-code pairs for tasks involving direct code generation and visual-based code refinement. Subsequently, we introduce a Visual Reinforcement Learning (ViRL) strategy, which employs a coarse-to-fine reward mechanism to improve visual fidelity by calculating visual similarity across local and global image patches. Extensive experiments on diverse multimodal code generation benchmarks demonstrate that VinciCoder achieves state-of-the-art performance, surpassing recent open-source models. The ablation study further validates the effectiveness of our proposed coarse-to-fine ViRL strategy. The data, code and model is available at https://github.com/DocTron-hub/VinciCoder.

