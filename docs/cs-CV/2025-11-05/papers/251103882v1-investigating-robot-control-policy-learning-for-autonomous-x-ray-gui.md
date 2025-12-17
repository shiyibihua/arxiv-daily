---
layout: default
title: Investigating Robot Control Policy Learning for Autonomous X-ray-guided Spine Procedures
---

# Investigating Robot Control Policy Learning for Autonomous X-ray-guided Spine Procedures

<div class="paper-toolbar">
  <div class="toolbar-left">
    <a href="https://arxiv.org/abs/2511.03882" target="_blank" class="toolbar-btn">arXiv: 2511.03882v1</a>
    <a href="https://arxiv.org/pdf/2511.03882.pdf" target="_blank" class="toolbar-btn">PDF</a>
  </div>
  <div class="toolbar-right">
    <button class="toolbar-btn favorite-btn" data-arxiv-id="2511.03882v1" 
            onclick="toggleFavorite(this, '2511.03882v1', 'Investigating Robot Control Policy Learning for Autonomous X-ray-guided Spine Procedures')" title="收藏">
      ☆ 收藏
    </button>
    <button class="toolbar-btn share-btn" onclick="copyLink()" title="复制链接">
      🔗 分享
    </button>
  </div>
</div>


**作者**: Florence Klitzner, Blanca Inigo, Benjamin D. Killeen, Lalithkumar Seenivasan, Michelle Song, Axel Krieger, Mathias Unberath

**分类**: cs.CV, cs.AI, cs.LG, cs.RO

**发布日期**: 2025-11-05

---

## 💡 一句话要点

**提出基于模仿学习的机器人控制策略，用于X射线引导的脊柱手术**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱三：空间感知 (Perception & SLAM)**

**关键词**: `机器人控制` `模仿学习` `X射线引导` `脊柱手术` `计算机视觉`

## 📋 核心要点

1. X射线引导手术中，多视角X射线图像的复杂性给基于模仿学习的机器人控制策略带来了挑战。
2. 论文提出在逼真的模拟环境中，通过模仿学习训练机器人控制策略，实现基于X射线图像的套管自动对准。
3. 实验表明，该策略在模拟环境中具有较高的成功率和鲁棒性，并在真实X射线图像上展现出潜力。

## 📝 摘要（中文）

本文研究了基于模仿学习的机器人控制策略在X射线引导手术中的应用，特别是脊柱器械植入。由于多视角X射线图像的复杂性，该方法在该领域的应用尚不明确。本文针对双平面X射线引导下的套管插入，探讨了模仿策略学习的机会和挑战。为此，开发了一个高真实度的计算机模拟环境，用于大规模、自动化地模拟X射线引导的脊柱手术。通过模拟专家操作，创建了一个包含正确轨迹和相应双平面X射线序列的数据集。然后，训练模仿学习策略，仅基于视觉信息迭代对准套管，进行规划和开环控制。实验结果表明，该策略在68.5%的案例中首次尝试成功，并在不同椎体水平上保持安全的椎弓根内轨迹。该策略推广到包括骨折在内的复杂解剖结构，并对不同的初始化保持鲁棒性。在真实双平面X射线上的实验表明，该模型可以生成合理的轨迹，尽管仅在模拟环境中训练。初步结果令人鼓舞，但也发现了局限性，尤其是在入口点精度方面。完全闭环控制需要考虑如何提供足够频繁的反馈。通过更强大的先验知识和领域知识，此类模型可能为未来轻量级和无CT的机器人术中脊柱导航奠定基础。

## 🔬 方法详解

**问题定义**：论文旨在解决X射线引导的脊柱手术中，如何利用机器人实现精准、自主的器械植入。现有方法依赖于CT图像或人工操作，前者增加了辐射暴露，后者则依赖于医生的经验和技能。因此，需要一种轻量级、无CT且能自主操作的机器人控制方法。

**核心思路**：论文的核心思路是利用模仿学习，让机器人通过学习专家在模拟环境中的操作轨迹和对应的X射线图像，从而掌握在真实手术中进行器械对准的能力。这种方法避免了复杂的图像处理和三维重建，直接从X射线图像到控制指令，简化了控制流程。

**技术框架**：整体框架包括三个主要部分：1) 高真实度的脊柱手术模拟环境，用于生成训练数据；2) 专家操作轨迹和对应X射线图像的数据集；3) 基于模仿学习的机器人控制策略。该策略接收双平面X射线图像作为输入，输出机器人的控制指令，实现套管的迭代对准。采用开环控制，即一次性输出整个轨迹。

**关键创新**：最重要的创新点在于直接从X射线图像学习控制策略，避免了传统方法中复杂的三维重建和路径规划。此外，论文构建了一个高真实度的模拟环境，能够生成大规模、多样化的训练数据，从而提高策略的泛化能力。

**关键设计**：论文使用深度神经网络作为模仿学习策略的模型，具体网络结构未知。损失函数的设计目标是最小化机器人实际轨迹与专家轨迹之间的差异。模拟环境的关键参数包括X射线源的位置、角度、强度，以及脊柱的解剖结构、骨密度等。数据集包含不同椎体水平、不同病理情况（如骨折）下的专家操作轨迹和对应的X射线图像。

## 📊 实验亮点

该模仿学习策略在模拟环境中取得了显著成果，在68.5%的案例中首次尝试成功，并在不同椎体水平上保持安全的椎弓根内轨迹。该策略对复杂解剖结构（包括骨折）具有良好的泛化能力，并且对不同的初始化位置具有鲁棒性。在真实双平面X射线上的初步实验表明，该模型能够生成合理的轨迹，尽管仅在模拟环境中训练。

## 🎯 应用场景

该研究成果可应用于机器人辅助的脊柱微创手术，降低医生操作难度，提高手术精度和效率，减少患者的辐射暴露。未来，结合更强大的先验知识和领域知识，有望实现轻量级、无CT的机器人术中脊柱导航，为更广泛的骨科手术提供支持。

## 📄 摘要（原文）

> Imitation learning-based robot control policies are enjoying renewed interest in video-based robotics. However, it remains unclear whether this approach applies to X-ray-guided procedures, such as spine instrumentation. This is because interpretation of multi-view X-rays is complex. We examine opportunities and challenges for imitation policy learning in bi-plane-guided cannula insertion. We develop an in silico sandbox for scalable, automated simulation of X-ray-guided spine procedures with a high degree of realism. We curate a dataset of correct trajectories and corresponding bi-planar X-ray sequences that emulate the stepwise alignment of providers. We then train imitation learning policies for planning and open-loop control that iteratively align a cannula solely based on visual information. This precisely controlled setup offers insights into limitations and capabilities of this method. Our policy succeeded on the first attempt in 68.5% of cases, maintaining safe intra-pedicular trajectories across diverse vertebral levels. The policy generalized to complex anatomy, including fractures, and remained robust to varied initializations. Rollouts on real bi-planar X-rays further suggest that the model can produce plausible trajectories, despite training exclusively in simulation. While these preliminary results are promising, we also identify limitations, especially in entry point precision. Full closed-look control will require additional considerations around how to provide sufficiently frequent feedback. With more robust priors and domain knowledge, such models may provide a foundation for future efforts toward lightweight and CT-free robotic intra-operative spinal navigation.

