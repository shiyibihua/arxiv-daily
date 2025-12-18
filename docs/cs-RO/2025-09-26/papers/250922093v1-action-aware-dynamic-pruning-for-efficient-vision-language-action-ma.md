---
layout: default
title: Action-aware Dynamic Pruning for Efficient Vision-Language-Action Manipulation
---

# Action-aware Dynamic Pruning for Efficient Vision-Language-Action Manipulation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.22093" class="toolbar-btn" target="_blank">📄 arXiv: 2509.22093v1</a>
  <a href="https://arxiv.org/pdf/2509.22093.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.22093v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.22093v1', 'Action-aware Dynamic Pruning for Efficient Vision-Language-Action Manipulation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Xiaohuan Pei, Yuxing Chen, Siyu Xu, Yunke Wang, Yuheng Shi, Chang Xu

**分类**: cs.RO, cs.AI

**发布日期**: 2025-09-26

---

## 💡 一句话要点

**提出动作感知动态剪枝ADP，提升视觉-语言-动作模型在机器人操作中的效率。**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `机器人操作` `视觉-语言-动作模型` `动态剪枝` `动作感知` `模型压缩` `推理加速`

## 📋 核心要点

1. 现有VLA模型在机器人操作中计算成本高昂，主要由于密集视觉token的注意力机制，且忽略了不同操作阶段的冗余差异。
2. ADP框架通过动作感知的轨迹门控机制，动态调整视觉token的保留率，从而在计算效率和感知精度之间取得平衡。
3. 实验表明，ADP在降低FLOPs和推理延迟的同时，保持了甚至提升了操作成功率，为高效机器人策略提供了简单有效的途径。

## 📝 摘要（中文）

本文提出了一种名为动作感知动态剪枝(ADP)的多模态剪枝框架，旨在提高视觉-语言-动作(VLA)模型在机器人操作中的推理效率。该方法观察到视觉token的冗余度在粗略操作阶段高于精细操作阶段，并且与动作动态密切相关。ADP集成了文本驱动的token选择和动作感知的轨迹门控机制，利用过去的运动窗口来调整token保留率，从而在不同操作阶段平衡计算效率和感知精度。在LIBERO套件和真实场景中的实验表明，ADP显著降低了FLOPs和动作推理延迟，同时保持了具有竞争力的成功率。

## 🔬 方法详解

**问题定义**：现有视觉-语言-动作(VLA)模型在机器人操作任务中，需要处理长时程的多模态上下文信息，其中对密集视觉token的注意力计算占据了主要的计算成本。现有的方法主要关注于减少VLA模型内部的视觉冗余，但忽略了机器人操作不同阶段视觉冗余度的差异，例如粗略操作阶段的冗余度高于精细操作阶段。

**核心思路**：本文的核心思路是利用机器人操作的动作动态信息来指导视觉token的剪枝过程。作者观察到视觉token的冗余度与动作动态之间存在强相关性，因此提出了一种动作感知的动态剪枝(ADP)框架。通过分析过去的动作轨迹，ADP可以自适应地调整视觉token的保留率，从而在保证感知精度的前提下，降低计算成本。

**技术框架**：ADP框架主要包含两个核心模块：文本驱动的token选择模块和动作感知的轨迹门控模块。文本驱动的token选择模块负责根据文本指令选择与任务相关的视觉token。动作感知的轨迹门控模块则利用过去的动作轨迹信息，动态调整token的保留率。具体来说，该模块使用一个门控机制，根据过去的运动窗口来预测当前阶段的视觉冗余度，并据此调整token的保留比例。整个框架可以作为一个插件集成到现有的VLA模型中。

**关键创新**：ADP的关键创新在于将动作动态信息融入到视觉token的剪枝过程中。与以往静态或基于文本的剪枝方法不同，ADP能够根据机器人操作的实际状态动态调整剪枝策略，从而更好地平衡计算效率和感知精度。这种动作感知的剪枝方法能够更有效地去除冗余的视觉信息，提高模型的推理效率。

**关键设计**：ADP框架中的动作感知轨迹门控模块是其关键设计之一。该模块使用一个循环神经网络(RNN)或Transformer来处理过去的动作轨迹，并输出一个门控信号，用于控制视觉token的保留率。损失函数的设计也至关重要，通常包括一个任务相关的损失函数（例如动作预测损失）和一个正则化项，用于约束剪枝的强度。具体的网络结构和参数设置需要根据具体的VLA模型和任务进行调整。

## 📊 实验亮点

实验结果表明，ADP方法在LIBERO套件和真实场景中均取得了显著的性能提升。例如，在OpenVLA-OFT模型上，ADP实现了1.35倍的推理速度提升。同时，在OpenVLA模型上，ADP还带来了25.8%的操作成功率提升。这些结果表明，ADP能够在降低计算成本的同时，保持甚至提升机器人的操作性能。

## 🎯 应用场景

该研究成果可应用于各种需要高效机器人操作的场景，例如工业自动化、家庭服务机器人、医疗机器人等。通过降低VLA模型的计算成本，可以使机器人能够在资源受限的环境中更快速、更可靠地执行任务。此外，该方法还可以促进更复杂、更智能的机器人策略的开发，从而拓展机器人的应用范围。

## 📄 摘要（原文）

> Robotic manipulation with Vision-Language-Action models requires efficient inference over long-horizon multi-modal context, where attention to dense visual tokens dominates computational cost. Existing methods optimize inference speed by reducing visual redundancy within VLA models, but they overlook the varying redundancy across robotic manipulation stages. We observe that the visual token redundancy is higher in coarse manipulation phase than in fine-grained operations, and is strongly correlated with the action dynamic. Motivated by this observation, we propose \textbf{A}ction-aware \textbf{D}ynamic \textbf{P}runing (\textbf{ADP}), a multi-modal pruning framework that integrates text-driven token selection with action-aware trajectory gating. Our method introduces a gating mechanism that conditions the pruning signal on recent action trajectories, using past motion windows to adaptively adjust token retention ratios in accordance with dynamics, thereby balancing computational efficiency and perceptual precision across different manipulation stages. Extensive experiments on the LIBERO suites and diverse real-world scenarios demonstrate that our method significantly reduces FLOPs and action inference latency (\textit{e.g.} $1.35 \times$ speed up on OpenVLA-OFT) while maintaining competitive success rates (\textit{e.g.} 25.8\% improvements with OpenVLA) compared to baselines, thereby providing a simple plug-in path to efficient robot policies that advances the efficiency and performance frontier of robotic manipulation. Our project website is: \href{https://vla-adp.github.io/}{ADP.com}.

