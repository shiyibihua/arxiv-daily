---
layout: default
title: Latent Refinement via Flow Matching for Training-free Linear Inverse Problem Solving
---

# Latent Refinement via Flow Matching for Training-free Linear Inverse Problem Solving

**arXiv**: [2511.06138v1](https://arxiv.org/abs/2511.06138) | [PDF](https://arxiv.org/pdf/2511.06138.pdf)

**作者**: Hossein Askari, Yadan Luo, Hongfu Sun, Fred Roosta

**分类**: cs.CV

**发布日期**: 2025-11-08

**备注**: 37 pages, 16 figures,

**🔗 代码/项目**: [GITHUB](https://github.com/hosseinaskari-cs/LFlow)

---

## 💡 一句话要点

**提出LFlow：基于Flow Matching的免训练线性逆问题隐空间优化方法**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `Flow Matching` `线性逆问题` `隐空间模型` `免训练` `图像重建`

## 📋 核心要点

1. 现有基于Flow的逆问题求解器直接在像素空间操作，计算资源需求大，难以扩展到高分辨率图像。
2. LFlow利用Flow Matching在隐空间进行ODE采样，提高了效率，并能沿最优路径进行优化。
3. LFlow引入了基于最优向量场的后验协方差，实现了更有效的Flow引导，提升了重建质量。

## 📝 摘要（中文）

本文提出LFlow（Latent Refinement via Flows），一个免训练框架，用于通过预训练的隐空间Flow先验解决线性逆问题。LFlow利用Flow Matching的效率，在隐空间沿最优路径执行ODE采样。这种隐空间公式允许我们引入一个理论上合理的后验协方差，该协方差源自最优向量场，从而实现有效的Flow引导。实验结果表明，在大多数任务中，我们提出的方法在重建质量方面优于最先进的隐空间扩散模型求解器。

## 🔬 方法详解

**问题定义**：论文旨在解决线性逆问题，即从观测数据中恢复原始信号或图像。现有的基于Flow的逆问题求解器主要存在两个痛点：一是直接在像素空间操作，计算成本高昂，难以处理高分辨率图像；二是采用的引导策略对先验信息利用不足，导致后验覆盖率下降。

**核心思路**：LFlow的核心思路是将逆问题求解过程转移到预训练的隐空间中进行。通过在隐空间中进行Flow Matching，可以利用预训练模型的先验知识，同时降低计算复杂度。此外，论文还提出了一种基于最优向量场的后验协方差，用于更有效地引导Flow的采样过程。

**技术框架**：LFlow的整体框架包括以下几个主要步骤：1) 将观测数据通过逆问题的算子映射到隐空间；2) 利用预训练的Flow模型在隐空间中进行ODE采样，从噪声出发逐步恢复潜在的原始信号；3) 在采样过程中，利用基于最优向量场的后验协方差进行Flow引导，确保采样轨迹与生成轨迹对齐；4) 将恢复的隐空间表示解码回像素空间，得到最终的重建结果。

**关键创新**：LFlow的关键创新在于：1) 将Flow Matching应用于隐空间，降低了计算成本，提高了效率；2) 提出了一种基于最优向量场的后验协方差，用于更有效地引导Flow的采样过程，提高了重建质量和后验覆盖率；3) 提出了一个免训练的框架，无需针对特定逆问题进行训练，具有更好的泛化能力。

**关键设计**：论文的关键设计包括：1) 使用预训练的Flow模型作为隐空间先验；2) 基于Flow Matching构建隐空间ODE；3) 推导并使用基于最优向量场的后验协方差进行Flow引导。具体的参数设置和网络结构取决于所使用的预训练Flow模型。

## 📊 实验亮点

实验结果表明，LFlow在图像去噪、图像修复等任务中，重建质量优于现有的隐空间扩散模型求解器。例如，在特定任务上，LFlow的PSNR指标比最先进的方法提升了X dB（具体数值需参考论文）。此外，LFlow的免训练特性使其具有更强的实用性。

## 🎯 应用场景

LFlow具有广泛的应用前景，包括图像去噪、图像修复、超分辨率重建、医学图像重建等线性逆问题。该方法无需针对特定任务进行训练，具有良好的泛化能力，可以快速应用于各种实际场景。未来，LFlow有望在计算成像、遥感图像处理等领域发挥重要作用。

## 📄 摘要（原文）

> Recent advances in inverse problem solving have increasingly adopted flow priors over diffusion models due to their ability to construct straight probability paths from noise to data, thereby enhancing efficiency in both training and inference. However, current flow-based inverse solvers face two primary limitations: (i) they operate directly in pixel space, which demands heavy computational resources for training and restricts scalability to high-resolution images, and (ii) they employ guidance strategies with prior-agnostic posterior covariances, which can weaken alignment with the generative trajectory and degrade posterior coverage. In this paper, we propose LFlow (Latent Refinement via Flows), a training-free framework for solving linear inverse problems via pretrained latent flow priors. LFlow leverages the efficiency of flow matching to perform ODE sampling in latent space along an optimal path. This latent formulation further allows us to introduce a theoretically grounded posterior covariance, derived from the optimal vector field, enabling effective flow guidance. Experimental results demonstrate that our proposed method outperforms state-of-the-art latent diffusion solvers in reconstruction quality across most tasks. The code will be publicly available at https://github.com/hosseinaskari-cs/LFlow .

