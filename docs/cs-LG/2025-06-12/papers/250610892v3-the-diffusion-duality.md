---
layout: default
title: The Diffusion Duality
---

# The Diffusion Duality

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.10892" class="toolbar-btn" target="_blank">📄 arXiv: 2506.10892v3</a>
  <a href="https://arxiv.org/pdf/2506.10892.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.10892v3" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.10892v3', 'The Diffusion Duality')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Subham Sekhar Sahoo, Justin Deschenaux, Aaron Gokaslan, Guanghan Wang, Justin Chiu, Volodymyr Kuleshov

**分类**: cs.LG, cs.AI, cs.CL

**发布日期**: 2025-06-12 (更新: 2025-12-19)

**备注**: ICML 2025. We provide the code at: https://github.com/s-sahoo/duo [v3] includes improved theory, clearer presentation, and a new future work section

**🔗 代码/项目**: [PROJECT_PAGE](http://s-sahoo.github.io/duo)

---

## 💡 一句话要点

**提出Duo方法以缩小离散扩散模型与自回归模型的性能差距**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `离散扩散模型` `高斯扩散` `课程学习` `一致性蒸馏` `文本生成` `自然语言处理`

## 📋 核心要点

1. 现有的均匀状态离散扩散模型在文本生成速度上有优势，但通常性能不及自回归模型和掩蔽扩散模型。
2. 论文提出的方法Duo通过借用高斯扩散的技术，采用课程学习和离散一致性蒸馏来提升模型性能和采样效率。
3. 实验结果表明，使用课程学习的模型在多个基准测试中表现优于自回归模型，且采样速度提升了两个数量级。

## 📝 摘要（中文）

均匀状态离散扩散模型因其自我纠正能力而在快速文本生成中展现出潜力，但通常不及自回归模型和掩蔽扩散模型。本文通过一个关键见解缩小了这一性能差距：均匀状态扩散过程自然源于基础的高斯扩散。我们的方法Duo借用高斯扩散的强大技术，提升了训练和采样效率。首先，我们引入了基于高斯过程的课程学习策略，使训练速度加倍并降低方差。经过课程学习训练的模型在7个基准测试中的3个上超越了自回归模型的零-shot困惑度。其次，我们提出了离散一致性蒸馏，将一致性蒸馏从连续设置适应到离散设置，从而加速了扩散语言模型的采样速度。

## 🔬 方法详解

**问题定义**：本文旨在解决均匀状态离散扩散模型在文本生成中性能不足的问题，尤其是与自回归模型和掩蔽扩散模型的比较中表现不佳。

**核心思路**：通过将高斯扩散的技术应用于离散扩散模型，提出Duo方法，利用课程学习和一致性蒸馏来提高训练和采样效率。

**技术框架**：Duo方法的整体架构包括两个主要模块：首先是基于高斯过程的课程学习策略，其次是离散一致性蒸馏。课程学习通过逐步引导模型学习，减少训练中的方差；一致性蒸馏则加速了生成过程。

**关键创新**：最重要的创新在于将高斯扩散的技术有效转移到离散扩散模型中，尤其是课程学习和一致性蒸馏的结合，使得模型在零-shot任务中超越传统自回归模型。

**关键设计**：在课程学习中，模型的训练速度加倍，且通过调整损失函数和网络结构，优化了模型的学习过程。离散一致性蒸馏则通过减少生成步骤，显著提升了采样速度。

## 📊 实验亮点

实验结果显示，采用课程学习的模型在7个基准测试中的3个上超越了自回归模型，且在采样速度上提升了两个数量级，显著提高了生成效率和质量。

## 🎯 应用场景

该研究的潜在应用领域包括自然语言处理中的文本生成、对话系统以及其他需要快速生成文本的场景。Duo方法的高效性和准确性使其在实际应用中具有重要价值，未来可能推动相关技术的广泛应用和发展。

## 📄 摘要（原文）

> Uniform-state discrete diffusion models hold the promise of fast text generation due to their inherent ability to self-correct. However, they are typically outperformed by autoregressive models and masked diffusion models. In this work, we narrow this performance gap by leveraging a key insight: Uniform-state diffusion processes naturally emerge from an underlying Gaussian diffusion. Our method, Duo, transfers powerful techniques from Gaussian diffusion to improve both training and sampling. First, we introduce a curriculum learning strategy guided by the Gaussian process, doubling training speed by reducing variance. Models trained with curriculum learning surpass autoregressive models in zero-shot perplexity on 3 of 7 benchmarks. Second, we present Discrete Consistency Distillation, which adapts consistency distillation from the continuous to the discrete setting. This algorithm unlocks few-step generation in diffusion language models by accelerating sampling by two orders of magnitude. We provide the code, model checkpoints, and video tutorials on the project page: http://s-sahoo.github.io/duo

