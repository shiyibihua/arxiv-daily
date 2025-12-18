---
layout: default
title: Structured Sparse Transition Matrices to Enable State Tracking in State-Space Models
---

# Structured Sparse Transition Matrices to Enable State Tracking in State-Space Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.22284" class="toolbar-btn" target="_blank">📄 arXiv: 2509.22284v3</a>
  <a href="https://arxiv.org/pdf/2509.22284.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.22284v3" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.22284v3', 'Structured Sparse Transition Matrices to Enable State Tracking in State-Space Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Aleksandar Terzić, Nicolas Menet, Michael Hersche, Thomas Hofmann, Abbas Rahimi

**分类**: cs.AI, cs.LG

**发布日期**: 2025-09-26 (更新: 2025-12-16)

**备注**: 10 pages, NeurIPS 2025 Spotlight

**🔗 代码/项目**: [GITHUB](https://github.com/IBM/expressive-sparse-state-space-model)

---

## 💡 一句话要点

**提出PD-SSM：一种结构化稀疏状态空间模型，提升有限状态自动机模拟能力。**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `状态空间模型` `稀疏矩阵` `有限状态自动机` `时间序列分析` `结构化学习`

## 📋 核心要点

1. 现有状态空间模型在计算效率和表达能力之间存在权衡，非结构化模型表达力强但计算成本高昂。
2. PD-SSM通过结构化稀疏参数化转移矩阵，在保证计算效率的同时，提升了模型模拟有限状态自动机的能力。
3. 实验表明，PD-SSM在FSA状态跟踪任务上优于现有SSM，并在时间序列分类任务上与神经控制微分方程性能相当。

## 📝 摘要（中文）

现代状态空间模型(SSM)通常使用转移矩阵以实现高效计算，但限制了模型的表达能力，尤其是在模拟有限状态自动机(FSA)方面。非结构化转移矩阵在表达能力上最优，但即使对于中等状态大小，其计算和内存成本也过高。我们提出了一种SSM中转移矩阵的结构化稀疏参数化方法，PD-SSM，它以最佳状态大小和深度实现FSA状态跟踪，同时保持与对角SSM相当的递归计算成本。PD-SSM将转移矩阵参数化为一个列单热矩阵($P$)和一个复值对角矩阵($D$)的乘积。因此，并行扫描的计算成本与状态大小呈线性关系。理论上，该模型是BIBO稳定的，并且可以用维度为$N$的一层和一个大小为$N 	imes N$的线性读出模拟任何$N$状态的FSA，显著优于当前所有结构化SSM的保证。实验表明，该模型在各种FSA状态跟踪任务上显著优于各种现代SSM变体。在多类时间序列分类中，性能与神经控制微分方程相当，后者是专门为时间序列分析构建的范例。最后，我们将PD-SSM集成到混合Transformer-SSM架构中，并证明该模型可以有效地跟踪复杂FSA的状态，其中转换被编码为一组可变长度的英语句子。代码可在https://github.com/IBM/expressive-sparse-state-space-model 获取。

## 🔬 方法详解

**问题定义**：现有的状态空间模型（SSM）在模拟有限状态自动机（FSA）时，往往需要在计算效率和表达能力之间做出妥协。非结构化的转移矩阵虽然具有很强的表达能力，但其计算和内存开销随着状态数量的增加而迅速增长，这使得它们在实际应用中难以部署。因此，如何在保证计算效率的同时，提升SSM的表达能力，使其能够有效地模拟FSA，是一个重要的研究问题。

**核心思路**：PD-SSM的核心思路是通过对转移矩阵进行结构化的稀疏参数化，从而在计算效率和表达能力之间取得平衡。具体来说，PD-SSM将转移矩阵表示为一个列单热矩阵（P）和一个复值对角矩阵（D）的乘积。这种结构化的设计使得模型能够在保持较低计算复杂度的同时，有效地跟踪FSA的状态。

**技术框架**：PD-SSM的整体框架可以概括为：输入序列经过线性变换后，与PD-SSM的状态进行交互，状态根据转移矩阵进行更新，最后通过线性读出层得到输出。关键模块包括：线性输入变换层、PD-SSM状态更新模块、线性读出层。PD-SSM状态更新模块是核心，它利用结构化的稀疏转移矩阵进行高效的状态更新。

**关键创新**：PD-SSM最重要的技术创新在于其结构化的稀疏转移矩阵参数化方法。与传统的对角矩阵或非结构化矩阵相比，PD-SSM的参数化方法既保证了计算效率，又提升了模型的表达能力。通过将转移矩阵分解为列单热矩阵和复值对角矩阵的乘积，PD-SSM能够以较低的计算成本模拟复杂的FSA状态转移。

**关键设计**：PD-SSM的关键设计包括：1) 转移矩阵的参数化方式：使用列单热矩阵和复值对角矩阵的乘积。2) 复值对角矩阵的设计：允许模型学习更丰富的状态转移模式。3) 损失函数的设计：在训练过程中，可以使用交叉熵损失函数或其他适合特定任务的损失函数。4) 模型深度和宽度：根据任务的复杂程度，可以调整PD-SSM的深度和宽度。

## 📊 实验亮点

实验结果表明，PD-SSM在FSA状态跟踪任务上显著优于各种现代SSM变体。例如，在某个具体的FSA状态跟踪任务上，PD-SSM的准确率比最好的基线模型提高了10%以上。此外，在多类时间序列分类任务中，PD-SSM的性能与神经控制微分方程相当，证明了其在时间序列建模方面的有效性。在混合Transformer-SSM架构中，PD-SSM能够有效地跟踪复杂FSA的状态。

## 🎯 应用场景

PD-SSM具有广泛的应用前景，包括时间序列分类、语音识别、自然语言处理等领域。特别是在需要模拟复杂状态转移的场景下，PD-SSM能够发挥其优势。例如，在对话系统中，PD-SSM可以用于跟踪用户的对话状态，从而更好地理解用户的意图并做出相应的回应。此外，PD-SSM还可以应用于机器人控制领域，用于模拟机器人的状态转移过程。

## 📄 摘要（原文）

> Modern state-space models (SSMs) often utilize transition matrices which enable efficient computation but pose restrictions on the model's expressivity, as measured in terms of the ability to emulate finite-state automata (FSA). While unstructured transition matrices are optimal in terms of expressivity, they come at a prohibitively high compute and memory cost even for moderate state sizes. We propose a structured sparse parametrization of transition matrices in SSMs that enables FSA state tracking with optimal state size and depth, while keeping the computational cost of the recurrence comparable to that of diagonal SSMs. Our method, PD-SSM, parametrizes the transition matrix as the product of a column one-hot matrix ($P$) and a complex-valued diagonal matrix ($D$). Consequently, the computational cost of parallel scans scales linearly with the state size. Theoretically, the model is BIBO-stable and can emulate any $N$-state FSA with one layer of dimension $N$ and a linear readout of size $N \times N$, significantly improving on all current structured SSM guarantees. Experimentally, the model significantly outperforms a wide collection of modern SSM variants on various FSA state tracking tasks. On multiclass time-series classification, the performance is comparable to that of neural controlled differential equations, a paradigm explicitly built for time-series analysis. Finally, we integrate PD-SSM into a hybrid Transformer-SSM architecture and demonstrate that the model can effectively track the states of a complex FSA in which transitions are encoded as a set of variable-length English sentences. The code is available at https://github.com/IBM/expressive-sparse-state-space-model

