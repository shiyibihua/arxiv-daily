---
layout: default
title: Pretraining Large Language Models with NVFP4
---

# Pretraining Large Language Models with NVFP4

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.25149" class="toolbar-btn" target="_blank">📄 arXiv: 2509.25149v1</a>
  <a href="https://arxiv.org/pdf/2509.25149.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.25149v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.25149v1', 'Pretraining Large Language Models with NVFP4')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: NVIDIA, Felix Abecassis, Anjulie Agrusa, Dong Ahn, Jonah Alben, Stefania Alborghetti, Michael Andersch, Sivakumar Arayandi, Alexis Bjorlin, Aaron Blakeman, Evan Briones, Ian Buck, Bryan Catanzaro, Jinhang Choi, Mike Chrzanowski, Eric Chung, Victor Cui, Steve Dai, Bita Darvish Rouhani, Carlo del Mundo, Deena Donia, Burc Eryilmaz, Henry Estela, Abhinav Goel, Oleg Goncharov, Yugi Guvvala, Robert Hesse, Russell Hewett, Herbert Hum, Ujval Kapasi, Brucek Khailany, Mikail Khona, Nick Knight, Alex Kondratenko, Ronny Krashinsky, Ben Lanir, Simon Layton, Michael Lightstone, Daniel Lo, Paulius Micikevicius, Asit Mishra, Tim Moon, Deepak Narayanan, Chao Ni, Abhijit Paithankar, Satish Pasumarthi, Ankit Patel, Mostofa Patwary, Ashwin Poojary, Gargi Prasad, Sweta Priyadarshi, Yigong Qin, Xiaowei Ren, Oleg Rybakov, Charbel Sakr, Sanjeev Satheesh, Stas Sergienko, Pasha Shamis, Kirthi Shankar, Nishant Sharma, Mohammad Shoeybi, Michael Siu, Misha Smelyanskiy, Darko Stosic, Dusan Stosic, Bor-Yiing Su, Frank Sun, Nima Tajbakhsh, Shelby Thomas, Przemek Tredak, Evgeny Tsykunov, Gandhi Vaithilingam, Aditya Vavre, Rangharajan Venkatesan, Roger Waleffe, Qiyu Wan, Hexin Wang, Mengdi Wang, Lizzie Wei, Hao Wu, Evan Wu, Keith Wyss, Ning Xu, Jinze Xue, Charlene Yang, Yujia Zhai, Ruoxi Zhang, Jingyang Zhu, Zhongbo Zhu

**分类**: cs.CL, cs.AI, cs.LG

**发布日期**: 2025-09-29

---

## 💡 一句话要点

**提出NVFP4训练方法，实现4-bit精度下大规模语言模型的稳定高效预训练。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大规模语言模型` `低精度训练` `NVFP4` `量化` `随机哈达玛变换` `预训练` `FP4`

## 📋 核心要点

1. 当前大规模语言模型训练需要巨大的计算资源，提高预训练效率对于构建更强大的LLM至关重要。
2. 论文提出NVFP4训练方法，通过随机哈达玛变换、二维量化、随机舍入和选择性高精度层等技术，实现稳定训练。
3. 实验结果表明，使用NVFP4训练的120亿参数模型在训练损失和下游任务准确性上与FP8基线相当。

## 📝 摘要（中文）

本文提出了一种使用NVFP4格式进行大规模语言模型（LLM）稳定且精确训练的新方法。该方法集成了随机哈达玛变换（RHT）以限制块级异常值，采用二维量化方案以确保前向和后向传播的一致性表示，利用随机舍入进行无偏梯度估计，并结合选择性的高精度层。通过在10万亿tokens上训练一个120亿参数的模型验证了该方法，这是迄今为止公开记录的最长的4-bit精度训练运行。结果表明，使用基于NVFP4的预训练技术训练的模型，其训练损失和下游任务准确性与FP8基线相当。这些发现表明，NVFP4与本文提出的训练方法相结合，代表了窄精度LLM训练算法的一个重大进步。

## 🔬 方法详解

**问题定义**：现有大规模语言模型（LLM）的训练需要消耗大量的计算资源和能源。虽然8-bit浮点（FP8）训练已被广泛采用，但进一步降低精度到4-bit浮点（FP4）可以显著提高计算速度和资源利用率。然而，这种极低的量化精度给训练的稳定性、收敛性和实现带来了挑战，尤其是在大规模模型和长序列训练中。

**核心思路**：论文的核心思路是通过一系列技术手段来克服4-bit量化带来的训练不稳定问题，从而实现大规模语言模型在NVFP4格式下的稳定训练。这些技术包括限制异常值、保持前后向传播一致性、减少梯度估计偏差以及在关键层保持高精度。通过这些方法，可以在保证模型性能的同时，显著降低计算成本。

**技术框架**：整体框架包括以下几个主要模块：1) **随机哈达玛变换（RHT）**：用于限制块级异常值，防止梯度爆炸。2) **二维量化方案**：确保前向和后向传播过程中表示的一致性，提高训练稳定性。3) **随机舍入**：用于无偏梯度估计，减少量化误差带来的影响。4) **选择性高精度层**：在对精度要求较高的层（例如，某些注意力层）使用更高的精度，以保持模型的表达能力。

**关键创新**：最重要的技术创新点在于将随机哈达玛变换、二维量化、随机舍入和选择性高精度层结合起来，形成一个完整的NVFP4训练方案。这种方案能够有效地解决4-bit量化带来的训练不稳定问题，使得大规模语言模型能够在极低的精度下进行有效训练。与现有方法相比，该方法能够在保证模型性能的同时，显著降低计算成本。

**关键设计**：1) **随机哈达玛变换的参数设置**：需要仔细调整哈达玛变换的参数，以确保能够有效地限制异常值，同时避免过度平滑。2) **二维量化方案的具体实现**：需要选择合适的量化范围和量化步长，以平衡量化误差和计算效率。3) **随机舍入的实现方式**：需要保证随机舍入的概率分布是均匀的，以实现无偏梯度估计。4) **选择性高精度层的选择策略**：需要根据模型的具体结构和任务特点，选择对精度要求较高的层使用更高的精度。

## 📊 实验亮点

实验结果表明，使用NVFP4训练的120亿参数模型在10万亿tokens上进行训练后，其训练损失和下游任务准确性与FP8基线模型相当。这证明了NVFP4训练方法在保持模型性能的同时，显著降低了计算成本，为更高效的LLM训练提供了新的途径。

## 🎯 应用场景

该研究成果可广泛应用于大规模语言模型的预训练，降低训练成本，加速模型迭代。尤其在资源受限的环境下，如边缘计算设备或小型研究团队，NVFP4训练方法能有效提升LLM的训练效率和可部署性，推动AI技术的普及。

## 📄 摘要（原文）

> Large Language Models (LLMs) today are powerful problem solvers across many domains, and they continue to get stronger as they scale in model size, training set size, and training set quality, as shown by extensive research and experimentation across the industry. Training a frontier model today requires on the order of tens to hundreds of yottaflops, which is a massive investment of time, compute, and energy. Improving pretraining efficiency is therefore essential to enable the next generation of even more capable LLMs. While 8-bit floating point (FP8) training is now widely adopted, transitioning to even narrower precision, such as 4-bit floating point (FP4), could unlock additional improvements in computational speed and resource utilization. However, quantization at this level poses challenges to training stability, convergence, and implementation, notably for large-scale models trained on long token horizons.
>   In this study, we introduce a novel approach for stable and accurate training of large language models (LLMs) using the NVFP4 format. Our method integrates Random Hadamard transforms (RHT) to bound block-level outliers, employs a two-dimensional quantization scheme for consistent representations across both the forward and backward passes, utilizes stochastic rounding for unbiased gradient estimation, and incorporates selective high-precision layers. We validate our approach by training a 12-billion-parameter model on 10 trillion tokens -- the longest publicly documented training run in 4-bit precision to date. Our results show that the model trained with our NVFP4-based pretraining technique achieves training loss and downstream task accuracies comparable to an FP8 baseline. These findings highlight that NVFP4, when combined with our training approach, represents a major step forward in narrow-precision LLM training algorithms.

