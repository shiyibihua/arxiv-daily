---
layout: default
title: MVSMamba: Multi-View Stereo with State Space Model
---

# MVSMamba: Multi-View Stereo with State Space Model

**arXiv**: [2511.01315v1](https://arxiv.org/abs/2511.01315) | [PDF](https://arxiv.org/pdf/2511.01315.pdf)

**作者**: Jianfei Jiang, Qiankun Liu, Hongyuan Liu, Haochen Yu, Liyong Wang, Jiansheng Chen, Huimin Ma

**分类**: cs.CV

**发布日期**: 2025-11-03

**备注**: Accepted by NeurIPS 2025

**🔗 代码/项目**: [GITHUB](https://github.com/JianfeiJ/MVSMamba)

---

## 💡 一句话要点

**MVSMamba：利用状态空间模型实现高效多视角立体视觉重建**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱六：视频提取与匹配 (Video Extraction & Matching)**

**关键词**: `多视角立体视觉` `状态空间模型` `Mamba架构` `三维重建` `深度图估计`

## 📋 核心要点

1. 现有基于Transformer的MVS方法计算复杂度高，难以平衡性能和效率。
2. MVSMamba利用Mamba架构的线性复杂度和全局建模能力，设计动态Mamba模块，实现高效特征聚合。
3. 实验结果表明，MVSMamba在DTU和Tanks-and-Temples数据集上超越现有SOTA方法，兼顾性能与效率。

## 📝 摘要（中文）

本文提出了一种基于Mamba架构的多视角立体视觉(MVS)网络MVSMamba，旨在解决现有基于Transformer的MVS方法计算复杂度高的问题。MVSMamba利用Mamba架构的全局建模能力和线性复杂度，实现了高效的全局特征聚合，且计算开销极小。为了充分发挥Mamba在MVS中的潜力，本文设计了一种基于参考视图中心动态扫描策略的动态Mamba模块(DM-module)，该模块能够：（1）实现从参考视图到源视图的高效的视图内和视图间特征交互；（2）生成全向多视图特征表示；（3）进行多尺度全局特征聚合。大量的实验结果表明，MVSMamba在DTU数据集和Tanks-and-Temples基准测试中优于最先进的MVS方法，并在性能和效率方面均表现出色。源代码已在https://github.com/JianfeiJ/MVSMamba公开。

## 🔬 方法详解

**问题定义**：现有的基于学习的多视角立体视觉(MVS)方法依赖于精确的特征匹配，而鲁棒的特征表示是关键。Transformer-based MVS方法虽然能够捕获长距离依赖，但其二次方复杂度限制了性能和效率的平衡。因此，如何降低计算复杂度，同时保持全局建模能力，是MVS领域的一个重要挑战。

**核心思路**：本文的核心思路是利用Mamba架构的线性复杂度和全局建模能力，替代Transformer在MVS网络中的作用。Mamba架构基于状态空间模型(SSM)，能够以线性复杂度建模长序列依赖关系，从而降低计算负担。此外，通过设计动态Mamba模块，能够更好地适应MVS任务的特点，提升特征表示能力。

**技术框架**：MVSMamba的整体框架包括特征提取、动态Mamba模块和深度图估计三个主要阶段。首先，使用传统的特征金字塔网络提取局部特征。然后，将提取的特征输入到动态Mamba模块中，进行全局特征聚合和视图间特征交互。最后，利用聚合后的特征进行深度图估计。动态Mamba模块是MVSMamba的核心组成部分，它基于参考视图中心动态扫描策略，实现高效的特征交互和全局建模。

**关键创新**：MVSMamba的关键创新在于将Mamba架构引入MVS领域，并设计了动态Mamba模块。动态Mamba模块通过参考视图中心动态扫描策略，实现了高效的视图内和视图间特征交互，生成全向多视图特征表示，并进行多尺度全局特征聚合。与传统的Transformer-based MVS方法相比，MVSMamba在计算复杂度上具有显著优势，同时保持了良好的性能。

**关键设计**：动态Mamba模块的关键设计包括：(1) 参考视图中心动态扫描策略：以参考视图为中心，动态调整扫描方向和范围，实现高效的特征交互。(2) 多尺度特征聚合：利用不同尺度的特征进行全局建模，提升特征表示能力。(3) 损失函数：采用深度图回归常用的损失函数，如L1损失或Huber损失。

## 📊 实验亮点

实验结果表明，MVSMamba在DTU数据集和Tanks-and-Temples基准测试中均取得了优异的性能。在DTU数据集上，MVSMamba的精度和完整性指标均优于现有SOTA方法。在Tanks-and-Temples基准测试中，MVSMamba在保持较高精度的同时，显著降低了计算时间，展现了其在效率方面的优势。

## 🎯 应用场景

MVSMamba在三维重建领域具有广泛的应用前景，例如：自动驾驶中的环境感知、机器人导航、虚拟现实/增强现实、城市建模、文物数字化等。该研究成果能够提升三维重建的效率和精度，为相关应用提供更可靠的数据支持，并推动相关领域的发展。

## 📄 摘要（原文）

> Robust feature representations are essential for learning-based Multi-View Stereo (MVS), which relies on accurate feature matching. Recent MVS methods leverage Transformers to capture long-range dependencies based on local features extracted by conventional feature pyramid networks. However, the quadratic complexity of Transformer-based MVS methods poses challenges to balance performance and efficiency. Motivated by the global modeling capability and linear complexity of the Mamba architecture, we propose MVSMamba, the first Mamba-based MVS network. MVSMamba enables efficient global feature aggregation with minimal computational overhead. To fully exploit Mamba's potential in MVS, we propose a Dynamic Mamba module (DM-module) based on a novel reference-centered dynamic scanning strategy, which enables: (1) Efficient intra- and inter-view feature interaction from the reference to source views, (2) Omnidirectional multi-view feature representations, and (3) Multi-scale global feature aggregation. Extensive experimental results demonstrate MVSMamba outperforms state-of-the-art MVS methods on the DTU dataset and the Tanks-and-Temples benchmark with both superior performance and efficiency. The source code is available at https://github.com/JianfeiJ/MVSMamba.

