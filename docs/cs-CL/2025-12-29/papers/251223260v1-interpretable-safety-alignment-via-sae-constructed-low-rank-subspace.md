---
layout: default
title: Interpretable Safety Alignment via SAE-Constructed Low-Rank Subspace Adaptation
---

# Interpretable Safety Alignment via SAE-Constructed Low-Rank Subspace Adaptation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.23260" class="toolbar-btn" target="_blank">📄 arXiv: 2512.23260v1</a>
  <a href="https://arxiv.org/pdf/2512.23260.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.23260v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.23260v1', 'Interpretable Safety Alignment via SAE-Constructed Low-Rank Subspace Adaptation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Dianyun Wang, Qingsen Ma, Yuhu Shang, Zhifeng Lu, Lechen Ning, Zhenbo Xu, Huijia Wu, Zhaofeng He

**分类**: cs.CL, cs.AI, cs.LG

**发布日期**: 2025-12-29

---

## 💡 一句话要点

**提出基于稀疏自编码器构建低秩子空间适配的安全对齐方法**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `低秩适配` `参数高效微调` `稀疏自编码器` `可解释性` `安全对齐`

## 📋 核心要点

1. 现有低秩适配方法缺乏可解释性，其低秩子空间以黑盒方式学习，难以直接控制。
2. 利用预训练稀疏自编码器识别解耦特征空间中的任务相关特征，构建显式可解释的低秩子空间。
3. 实验表明，该方法在安全对齐方面优于全微调，接近RLHF方法，同时仅更新少量参数。

## 📝 摘要（中文）

参数高效微调已成为将大型语言模型适配到下游任务的主流范式。诸如LoRA之类的低秩适配方法假设任务相关的权重更新存在于一个低秩子空间中，然而，这个子空间是以黑盒方式从数据中隐式学习的，不提供可解释性或直接控制。我们假设这种困难源于多义性——单个维度编码多个纠缠的概念。为了解决这个问题，我们利用预训练的稀疏自编码器（SAE）来识别解耦特征空间中的任务相关特征，然后构建一个显式的、可解释的低秩子空间来指导适配器初始化。我们提供了理论分析，证明在单义性假设下，基于SAE的子空间识别可以实现任意小的恢复误差，而多义空间中的直接识别会遭受不可约的误差下限。在安全对齐方面，我们的方法实现了高达99.6%的安全率——超过完全微调7.4个百分点，并接近基于RLHF的方法——同时仅更新0.19-0.24%的参数。至关重要的是，我们的方法通过SAE特征的语义基础，提供了对学习到的对齐子空间的可解释的见解。我们的工作表明，将机制可解释性融入微调过程可以同时提高性能和透明度。

## 🔬 方法详解

**问题定义**：现有低秩适配方法（如LoRA）在微调大型语言模型时，虽然参数效率高，但学习到的低秩子空间缺乏可解释性，难以理解和控制模型行为。这种黑盒特性限制了模型在安全对齐等任务中的应用，因为无法直接干预或验证模型的决策过程。现有方法难以应对特征空间的多义性问题，即单个维度可能编码多个纠缠的概念，导致子空间识别的误差较高。

**核心思路**：论文的核心思路是利用预训练的稀疏自编码器（SAE）来解耦特征空间，将多义特征分解为单义特征。通过在解耦后的特征空间中识别任务相关的特征，可以构建一个更清晰、更可解释的低秩子空间，用于指导适配器的初始化。这种方法旨在将机制可解释性融入微调过程，从而提高模型的性能和透明度。

**技术框架**：该方法主要包含以下几个阶段：1) 使用预训练的稀疏自编码器（SAE）对模型的中间层特征进行编码，得到解耦的特征表示。2) 在解耦后的特征空间中，识别与特定任务（如安全对齐）相关的特征。这可以通过分析SAE激活与任务目标之间的相关性来实现。3) 基于识别出的任务相关特征，构建一个低秩子空间。这个子空间可以被视为一个适配器，用于在微调过程中调整模型的权重。4) 使用构建的低秩子空间初始化适配器，并进行微调。

**关键创新**：该方法最重要的技术创新点在于将稀疏自编码器（SAE）引入到低秩适配框架中，用于解耦特征空间并提高可解释性。与传统的低秩适配方法相比，该方法能够显式地识别和控制任务相关的特征，从而实现更精确、更可控的微调。此外，该方法还提供了理论分析，证明在单义性假设下，基于SAE的子空间识别可以实现任意小的恢复误差。

**关键设计**：SAE的训练目标是最小化重构误差，同时鼓励稀疏激活。这可以通过添加L1正则化项来实现。低秩子空间的构建方式取决于具体的任务和特征空间。一种常见的方法是选择与任务目标相关性最高的SAE激活对应的特征向量，并将它们作为子空间的基向量。适配器的初始化可以使用这些基向量的线性组合。损失函数通常包括任务相关的损失项（如交叉熵损失）和一个正则化项，用于防止过拟合。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.23260v1/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.23260v1/x2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.23260v1/x3.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

该方法在安全对齐任务上取得了显著的性能提升，安全率高达99.6%，超过全微调7.4个百分点，并接近基于RLHF的方法。同时，该方法仅更新0.19-0.24%的参数，具有很高的参数效率。此外，该方法还提供了对学习到的对齐子空间的可解释的见解，通过SAE特征的语义基础，可以理解模型是如何进行安全对齐的。

## 🎯 应用场景

该研究成果可应用于安全关键型大型语言模型的对齐，例如，在自动驾驶、医疗诊断等领域，确保模型输出的安全性、可靠性和可解释性。此外，该方法还可推广到其他需要可控微调的场景，例如，个性化推荐、内容生成等。通过提高模型的可解释性，可以增强用户对模型的信任，并促进其更广泛的应用。

## 📄 摘要（原文）

> Parameter-efficient fine-tuning has become the dominant paradigm for adapting large language models to downstream tasks. Low-rank adaptation methods such as LoRA operate under the assumption that task-relevant weight updates reside in a low-rank subspace, yet this subspace is learned implicitly from data in a black-box manner, offering no interpretability or direct control. We hypothesize that this difficulty stems from polysemanticity--individual dimensions encoding multiple entangled concepts. To address this, we leverage pre-trained Sparse Autoencoders (SAEs) to identify task-relevant features in a disentangled feature space, then construct an explicit, interpretable low-rank subspace to guide adapter initialization. We provide theoretical analysis proving that under monosemanticity assumptions, SAE-based subspace identification achieves arbitrarily small recovery error, while direct identification in polysemantic space suffers an irreducible error floor. On safety alignment, our method achieves up to 99.6% safety rate--exceeding full fine-tuning by 7.4 percentage points and approaching RLHF-based methods--while updating only 0.19-0.24% of parameters. Crucially, our method provides interpretable insights into the learned alignment subspace through the semantic grounding of SAE features. Our work demonstrates that incorporating mechanistic interpretability into the fine-tuning process can simultaneously improve both performance and transparency.

