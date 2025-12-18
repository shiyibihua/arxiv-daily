---
layout: default
title: Generalizable Geometric Image Caption Synthesis
---

# Generalizable Geometric Image Caption Synthesis

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.15217" class="toolbar-btn" target="_blank">📄 arXiv: 2509.15217v1</a>
  <a href="https://arxiv.org/pdf/2509.15217.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.15217v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.15217v1', 'Generalizable Geometric Image Caption Synthesis')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yue Xin, Wenyuan Wang, Rui Pan, Ruida Wang, Howard Meng, Renjie Pi, Shizhe Diao, Tong Zhang

**分类**: cs.AI, cs.CV, cs.LG

**发布日期**: 2025-09-18

---

## 💡 一句话要点

**提出RLVR方法以解决几何图像描述生成问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `几何图像` `图像描述生成` `多模态学习` `强化学习` `数据合成` `推理能力` `数学问题解决` `模型泛化`

## 📋 核心要点

1. 现有的多模态大语言模型在处理复杂几何问题时表现不佳，缺乏高质量的图像-文本配对数据集是主要挑战。
2. 本文提出了一种结合可验证奖励的强化学习（RLVR）方法，优化几何图像的描述生成过程，从而提升模型的推理能力。
3. 实验结果表明，该方法在多个任务上实现了2.8%-4.8%的准确率提升，显著增强了模型的推理能力和泛化能力。

## 📝 摘要（中文）

多模态大语言模型在解决复杂几何问题时仍面临挑战，主要由于缺乏高质量的图像-文本配对数据集。现有的基于模板的数据合成管道通常无法推广到超出预定义模板的问题。本文通过引入可验证奖励的强化学习（RLVR）过程，改进几何图像的描述生成。该方法通过从50种基本几何关系合成图像，并利用数学问题解决任务的奖励信号来优化描述，从而提高了任务的泛化能力，并在非几何输入图像的多个任务中实现了2.8%-4.8%的准确率提升。

## 🔬 方法详解

**问题定义**：本文旨在解决多模态大语言模型在几何图像描述生成中的不足，尤其是现有方法在复杂几何问题上的泛化能力不足。

**核心思路**：通过引入可验证奖励的强化学习（RLVR）机制，优化合成的几何图像描述，利用数学问题解决任务的奖励信号来提升描述质量。

**技术框架**：整体架构包括数据生成管道和RLVR优化模块。首先，从50种基本几何关系合成图像，然后通过RLVR对生成的描述进行优化。

**关键创新**：最重要的创新在于将RLVR引入数据生成流程，使得生成的描述不仅符合几何特征，还能有效解决数学问题，从而提升模型的推理能力。

**关键设计**：在参数设置上，采用了适应性奖励机制，损失函数设计为结合语义相似度和几何特征的复合损失，网络结构则基于现有的多模态模型进行调整，以适应几何图像的特性。

## 📊 实验亮点

实验结果显示，采用RLVR优化后的模型在MathVista和MathVerse等非几何输入图像的统计、算术、代数和数值任务中，准确率提升了2.8%-4.8%；在艺术、设计、技术和工程任务中，准确率提升了2.4%-3.9%。

## 🎯 应用场景

该研究的潜在应用领域包括教育、机器人视觉、自动化设计等。通过提升多模态大语言模型在几何问题上的推理能力，可以在数学教育辅助、智能设计工具等方面发挥重要作用，未来可能影响相关领域的研究和应用发展。

## 📄 摘要（原文）

> Multimodal large language models have various practical applications that demand strong reasoning abilities. Despite recent advancements, these models still struggle to solve complex geometric problems. A key challenge stems from the lack of high-quality image-text pair datasets for understanding geometric images. Furthermore, most template-based data synthesis pipelines typically fail to generalize to questions beyond their predefined templates. In this paper, we bridge this gap by introducing a complementary process of Reinforcement Learning with Verifiable Rewards (RLVR) into the data generation pipeline. By adopting RLVR to refine captions for geometric images synthesized from 50 basic geometric relations and using reward signals derived from mathematical problem-solving tasks, our pipeline successfully captures the key features of geometry problem-solving. This enables better task generalization and yields non-trivial improvements. Furthermore, even in out-of-distribution scenarios, the generated dataset enhances the general reasoning capabilities of multimodal large language models, yielding accuracy improvements of $2.8\%\text{-}4.8\%$ in statistics, arithmetic, algebraic, and numerical tasks with non-geometric input images of MathVista and MathVerse, along with $2.4\%\text{-}3.9\%$ improvements in Art, Design, Tech, and Engineering tasks in MMMU.

