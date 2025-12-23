---
layout: default
title: Object Navigation with Structure-Semantic Reasoning-Based Multi-level Map and Multimodal Decision-Making LLM
---

# Object Navigation with Structure-Semantic Reasoning-Based Multi-level Map and Multimodal Decision-Making LLM

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.05896" class="toolbar-btn" target="_blank">📄 arXiv: 2506.05896v1</a>
  <a href="https://arxiv.org/pdf/2506.05896.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.05896v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.05896v1', 'Object Navigation with Structure-Semantic Reasoning-Based Multi-level Map and Multimodal Decision-Making LLM')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Chongshang Yan, Jiaxuan He, Delun Li, Yi Yang, Wenjie Song

**分类**: cs.RO, cs.AI, cs.CV

**发布日期**: 2025-06-06

**备注**: 16 pages, 11 figures

---

## 💡 一句话要点

**提出基于结构-语义推理的多层次地图与多模态决策的主动物体导航框架**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `零样本物体导航` `环境属性图` `多层次推理` `路径优化` `智能机器人`

## 📋 核心要点

1. 现有的零样本物体导航方法在处理未知环境和语义新目标时，性能显著下降，主要由于忽视高维隐式场景信息。
2. 本文提出的框架结合环境属性图（EAM）和多层次推理模块（MHR），通过推理和预测环境信息来提升导航效率。
3. 实验结果显示，EAM在MP3D数据集上的场景映射准确率为64.5%，在HM3D和MP3D基准上的SPL分别提升了21.4%和46.0%。

## 📝 摘要（中文）

在未知开放环境中进行零样本物体导航（ZSON）时，由于忽视高维隐式场景信息和长距离目标搜索任务，性能常显著下降。为此，本文提出了一种主动物体导航框架，结合环境属性图（EAM）和多层次推理模块（MHR），以提高成功率和效率。EAM通过SBERT推理已观察环境，并利用扩散模型预测未观察环境，利用人类空间规律来建立物体与房间的关联。MHR则基于EAM进行前沿探索决策，避免在长距离场景中的迂回路径，从而提升路径效率。实验结果表明，EAM模块在MP3D数据集上的场景映射准确率达到64.5%，而导航任务在HM3D和MP3D基准上的成功路径长度（SPL）分别为28.4%和26.3%，相较于基线方法分别提升了21.4%和46.0%。

## 🔬 方法详解

**问题定义**：本文旨在解决在未知开放环境中进行零样本物体导航时，因忽视高维隐式场景信息和长距离目标搜索导致的性能下降问题。

**核心思路**：提出的主动物体导航框架通过环境属性图（EAM）和多层次推理模块（MHR）来增强导航的成功率和效率，利用环境推理和决策制定来优化路径。

**技术框架**：框架主要包括两个模块：环境属性图（EAM）用于推理和预测环境信息，和多层次推理模块（MHR）用于决策制定，整体流程为环境观察、属性推理、路径规划。

**关键创新**：EAM模块通过SBERT和扩散模型结合人类空间规律进行环境推理，MHR模块则通过前沿探索决策避免迂回路径，这些创新显著提升了导航效率。

**关键设计**：在EAM中，使用SBERT进行环境推理，扩散模型用于未观察环境的预测，MHR模块设计了有效的决策机制以优化路径选择，具体参数和损失函数的设置在实验中进行了详细调优。

## 📊 实验亮点

实验结果表明，EAM模块在MP3D数据集上的场景映射准确率达到64.5%，而在HM3D和MP3D基准上的成功路径长度（SPL）分别为28.4%和26.3%，相较于基线方法分别提升了21.4%和46.0%，显示出显著的性能改进。

## 🎯 应用场景

该研究的潜在应用领域包括智能机器人、自动驾驶、虚拟现实等，能够在复杂和未知环境中实现高效的物体导航，具有重要的实际价值和广泛的未来影响。通过提升导航效率，能够推动相关领域的技术进步与应用落地。

## 📄 摘要（原文）

> The zero-shot object navigation (ZSON) in unknown open-ended environments coupled with semantically novel target often suffers from the significant decline in performance due to the neglect of high-dimensional implicit scene information and the long-range target searching task. To address this, we proposed an active object navigation framework with Environmental Attributes Map (EAM) and MLLM Hierarchical Reasoning module (MHR) to improve its success rate and efficiency. EAM is constructed by reasoning observed environments with SBERT and predicting unobserved ones with Diffusion, utilizing human space regularities that underlie object-room correlations and area adjacencies. MHR is inspired by EAM to perform frontier exploration decision-making, avoiding the circuitous trajectories in long-range scenarios to improve path efficiency. Experimental results demonstrate that the EAM module achieves 64.5\% scene mapping accuracy on MP3D dataset, while the navigation task attains SPLs of 28.4\% and 26.3\% on HM3D and MP3D benchmarks respectively - representing absolute improvements of 21.4\% and 46.0\% over baseline methods.

