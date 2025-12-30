---
layout: default
title: SE-MLP Model for Predicting Prior Acceleration Features in Penetration Signals
---

# SE-MLP Model for Predicting Prior Acceleration Features in Penetration Signals

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.23131" class="toolbar-btn" target="_blank">📄 arXiv: 2512.23131v1</a>
  <a href="https://arxiv.org/pdf/2512.23131.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.23131v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.23131v1', 'SE-MLP Model for Predicting Prior Acceleration Features in Penetration Signals')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yankang Li, Changsheng Li

**分类**: cs.LG

**发布日期**: 2025-12-29

**备注**: 23 pages, 10 figures, 6 tables

---

## 💡 一句话要点

**提出SE-MLP模型，用于快速预测侵彻信号中的先验加速度特征，解决传统方法计算耗时问题。**

🎯 **匹配领域**: **支柱四：生成式动作 (Generative Motion)** **支柱八：物理动画 (Physics-based Animation)**

**关键词**: `侵彻信号预测` `加速度特征` `多层感知机` `通道注意力机制` `残差连接` `深度学习` `物理参数建模`

## 📋 核心要点

1. 准确识别侵彻过程依赖于侵彻加速度的先验特征值，但传统方法需要耗时的仿真周期和高昂的计算成本。
2. 论文提出SE-MLP模型，通过集成通道注意力机制和残差连接，实现对加速度特征值的快速预测。
3. 实验结果表明，SE-MLP在预测精度、泛化性和稳定性方面优于传统MLP、XGBoost和Transformer模型。

## 📝 摘要（中文）

本文提出了一种名为挤压激励多层感知机（SE-MLP）的模型，该模型集成了通道注意力机制和残差连接，旨在快速预测加速度特征值。该模型以不同工况下的物理参数作为输入，输出分层加速度特征，从而建立物理参数与侵彻特性之间的非线性映射。与传统MLP、XGBoost和Transformer模型的对比实验表明，SE-MLP在预测精度、泛化性和稳定性方面表现更优。消融研究进一步证实了通道注意力模块和残差结构对性能提升的显著贡献。数值模拟和射程恢复测试表明，预测和测量得到的加速度峰值和脉冲宽度之间的差异保持在可接受的工程容差范围内。这些结果验证了该方法的可行性和工程适用性，并为快速生成侵彻引信的先验特征值提供了实践基础。

## 🔬 方法详解

**问题定义**：论文旨在解决侵彻过程中加速度特征值预测耗时的问题。传统的获取方式依赖于长时间的仿真和高昂的计算，这限制了对侵彻过程的快速分析和优化。现有方法的痛点在于计算效率低，难以满足实时性要求。

**核心思路**：论文的核心思路是利用深度学习模型学习物理参数与加速度特征之间的非线性映射关系，从而实现对加速度特征值的快速预测。通过构建一个高效的预测模型，避免了耗时的仿真过程，提高了计算效率。

**技术框架**：SE-MLP模型的整体架构是一个多层感知机，其输入是不同工况下的物理参数，输出是分层加速度特征。模型主要包含以下模块：输入层、多层感知机层、挤压激励（Squeeze-and-Excitation）模块、残差连接和输出层。挤压激励模块用于学习通道之间的依赖关系，提升特征表达能力。残差连接用于缓解梯度消失问题，提高模型训练的稳定性。

**关键创新**：最重要的技术创新点在于将通道注意力机制（挤压激励模块）和残差连接集成到多层感知机中。与传统的MLP相比，SE-MLP能够更好地捕捉通道之间的依赖关系，并缓解梯度消失问题，从而提高预测精度和泛化能力。

**关键设计**：SE-MLP的关键设计包括：1) 挤压激励模块的参数设置，例如压缩比例的选择；2) 残差连接的连接方式，例如直接连接或通过卷积层连接；3) 损失函数的选择，例如均方误差或Huber损失；4) 网络层数的选择，需要根据具体问题进行调整。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.23131v1/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.23131v1/x2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.23131v1/x3.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

实验结果表明，SE-MLP模型在预测精度、泛化性和稳定性方面优于传统MLP、XGBoost和Transformer模型。消融研究证实了通道注意力模块和残差结构对性能提升的显著贡献。数值模拟和射程恢复测试表明，预测和测量得到的加速度峰值和脉冲宽度之间的差异保持在可接受的工程容差范围内，验证了该方法的工程适用性。

## 🎯 应用场景

该研究成果可应用于侵彻引信的快速设计和优化，提高武器系统的研发效率。此外，该方法还可以扩展到其他需要快速预测先验特征值的工程领域，例如材料设计、结构优化等。通过建立物理参数与性能指标之间的快速预测模型，可以加速设计迭代过程，降低研发成本。

## 📄 摘要（原文）

> Accurate identification of the penetration process relies heavily on prior feature values of penetration acceleration. However, these feature values are typically obtained through long simulation cycles and expensive computations. To overcome this limitation, this paper proposes a multi-layer Perceptron architecture, termed squeeze and excitation multi-layer perceptron (SE-MLP), which integrates a channel attention mechanism with residual connections to enable rapid prediction of acceleration feature values. Using physical parameters under different working conditions as inputs, the model outputs layer-wise acceleration features, thereby establishing a nonlinear mapping between physical parameters and penetration characteristics. Comparative experiments against conventional MLP, XGBoost, and Transformer models demonstrate that SE-MLP achieves superior prediction accuracy, generalization, and stability. Ablation studies further confirm that both the channel attention module and residual structure contribute significantly to performance gains. Numerical simulations and range recovery tests show that the discrepancies between predicted and measured acceleration peaks and pulse widths remain within acceptable engineering tolerances. These results validate the feasibility and engineering applicability of the proposed method and provide a practical basis for rapidly generating prior feature values for penetration fuzes.

