---
layout: default
title: World Modeling with Probabilistic Structure Integration
---

# World Modeling with Probabilistic Structure Integration

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.09737" class="toolbar-btn" target="_blank">📄 arXiv: 2509.09737v1</a>
  <a href="https://arxiv.org/pdf/2509.09737.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.09737v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.09737v1', 'World Modeling with Probabilistic Structure Integration')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Klemen Kotar, Wanhee Lee, Rahul Venkatesh, Honglin Chen, Daniel Bear, Jared Watrous, Simon Kim, Khai Loong Aw, Lilian Naing Chen, Stefan Stojanov, Kevin Feigelis, Imran Thobani, Alex Durango, Khaled Jedoui, Atlas Kazemian, Dan Yamins

**分类**: cs.CV, cs.AI, cs.LG

**发布日期**: 2025-09-10

---

## 💡 一句话要点

**提出概率结构集成（PSI），用于学习可控且灵活提示的世界模型。**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱三：空间感知与语义 (Perception & Semantics)**

**关键词**: `世界模型` `概率图模型` `因果推断` `结构化学习` `视频理解` `自监督学习` `序列模型`

## 📋 核心要点

1. 现有世界模型在可控性和灵活性方面存在不足，难以有效利用数据中的潜在结构。
2. PSI通过概率预测、结构提取和集成循环，将提取的中间结构作为新的token类型融入训练，增强模型能力。
3. 在1.4万亿token的视频数据上训练的PSI，在视频预测、光流估计、深度估计和对象分割等方面表现出色。

## 📝 摘要（中文）

本文提出了一种名为概率结构集成（PSI）的系统，用于从数据中学习具有丰富可控性和灵活提示性的世界模型。PSI包含一个三步循环：1）概率预测，构建数据的概率图模型Psi，形式为随机访问自回归序列模型。Psi支持完整的学习条件分布集，描述数据中任何变量对任何其他变量集的依赖关系。2）结构提取，展示了如何通过对Psi进行因果推断，以零样本方式提取数据中潜在的低维属性，对应于各种有意义的“中间结构”。3）集成，通过将这些结构转换为新的token类型，然后不断地将其混合回训练数据中作为条件信号和预测目标，从而完成循环。每个循环都增强了Psi的能力，使其能够更好地建模底层数据，并创建新的控制句柄——类似于LLM的通用提示语言。我们在1.4万亿个互联网视频数据token上训练了一个Psi实例；我们使用它来执行各种有用的视频预测和理解推断；我们提取了最先进的光流、自监督深度和对象分割；并且我们使用这些结构来支持预测改进的完整循环。

## 🔬 方法详解

**问题定义**：现有世界模型难以充分利用数据中蕴含的丰富结构信息，导致可控性和灵活性受限。例如，难以根据用户指定的中间层特征（如光流、深度信息）进行条件生成或预测，也难以有效地进行零样本迁移。

**核心思路**：PSI的核心在于通过概率图模型学习数据中变量之间的依赖关系，并利用因果推断提取有意义的中间结构。这些结构随后被转化为新的token类型，并集成回训练过程中，从而增强模型对数据底层结构的理解和利用能力。这种循环式的结构集成方法使得模型能够不断学习和改进，最终实现更强的可控性和灵活性。

**技术框架**：PSI包含三个主要步骤：
1. **概率预测**：构建数据的概率图模型Psi，采用随机访问自回归序列模型实现，能够学习任意变量间的条件依赖关系。
2. **结构提取**：通过对Psi进行因果推断，提取数据中潜在的低维属性，这些属性对应于有意义的中间结构，如光流、深度信息等。
3. **集成**：将提取的中间结构转换为新的token类型，并将其作为条件信号和预测目标，循环地集成回训练数据中。

**关键创新**：PSI的关键创新在于其循环式的结构集成方法。通过不断地提取和集成中间结构，模型能够逐步学习数据的底层结构，并将其转化为可控的提示信号。这种方法类似于LLM的通用提示语言，使得模型能够根据用户指定的中间层特征进行条件生成和预测，从而实现更强的可控性和灵活性。与现有方法相比，PSI能够以零样本的方式提取中间结构，无需额外的监督信息。

**关键设计**：PSI使用随机访问自回归序列模型作为概率图模型Psi的实现方式，这使得模型能够灵活地访问和预测数据中的任意变量。在结构提取阶段，采用因果推断方法来识别数据中潜在的因果关系，并提取相应的中间结构。在集成阶段，需要仔细设计新的token类型，并调整训练策略，以确保模型能够有效地利用这些新的token类型。

## 📊 实验亮点

PSI在1.4万亿token的互联网视频数据上进行了训练，实验结果表明，PSI能够提取最先进的光流、自监督深度和对象分割等中间结构。通过将这些结构集成回训练过程中，PSI能够显著提高视频预测的准确性和可控性。具体性能数据未知，但论文强调了PSI在多个任务上达到了state-of-the-art的水平。

## 🎯 应用场景

PSI具有广泛的应用前景，例如视频编辑、游戏AI、机器人控制等领域。通过提取和利用视频中的中间结构，PSI可以实现更逼真的视频生成、更智能的机器人导航和更高效的视频分析。此外，PSI还可以应用于其他类型的数据，例如图像、文本等，从而构建更强大的通用世界模型。

## 📄 摘要（原文）

> We present Probabilistic Structure Integration (PSI), a system for learning richly controllable and flexibly promptable world models from data. PSI consists of a three-step cycle. The first step, Probabilistic prediction, involves building a probabilistic graphical model Psi of the data, in the form of a random-access autoregressive sequence model. Psi supports a complete set of learned conditional distributions describing the dependence of any variables in the data on any other set of variables. In step 2, Structure extraction, we show how to extract underlying low-dimensional properties in the data, corresponding to a diverse set of meaningful "intermediate structures", in a zero-shot fashion via causal inference on Psi. Step 3, Integration, completes the cycle by converting these structures into new token types that are then continually mixed back into the training diet as conditioning signals and prediction targets. Each such cycle augments the capabilities of Psi, both allowing it to model the underlying data better, and creating new control handles -- akin to an LLM-like universal prompting language. We train an instance of Psi on 1.4 trillion tokens of internet video data; we use it to perform a variety of useful video prediction and understanding inferences; we extract state-of-the-art optical flow, self-supervised depth and object segmentation; and we use these structures to support a full cycle of predictive improvements.

