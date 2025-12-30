---
layout: default
title: "Diffusion Knows Transparency: Repurposing Video Diffusion for Transparent Object Depth and Normal Estimation"
---

# Diffusion Knows Transparency: Repurposing Video Diffusion for Transparent Object Depth and Normal Estimation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.23705" class="toolbar-btn" target="_blank">📄 arXiv: 2512.23705v1</a>
  <a href="https://arxiv.org/pdf/2512.23705.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.23705v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.23705v1', 'Diffusion Knows Transparency: Repurposing Video Diffusion for Transparent Object Depth and Normal Estimation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Shaocong Xu, Songlin Wei, Qizhe Wei, Zheng Geng, Hong Li, Licheng Shen, Qianpu Sun, Shu Han, Bin Ma, Bohan Li, Chongjie Ye, Yuhang Zheng, Nan Wang, Saining Zhang, Hao Zhao

**分类**: cs.CV

**发布日期**: 2025-12-29

**备注**: Project Page: https://daniellli.github.io/projects/DKT/; Code: https://github.com/Daniellli/DKT; Dataset: https://huggingface.co/datasets/Daniellesry/TransPhy3D

---

## 💡 一句话要点

**利用视频扩散模型，DKT实现了透明物体深度和法向量的零样本SOTA估计**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱三：空间感知与语义 (Perception & Semantics)**

**关键词**: `透明物体感知` `深度估计` `法向量估计` `视频扩散模型` `零样本学习`

## 📋 核心要点

1. 传统方法在透明物体深度估计方面面临挑战，因为透明物体的折射、反射等特性违反了传统视觉算法的假设。
2. 该论文利用视频扩散模型已经能够生成逼真的透明效果的特性，通过训练将视频扩散模型转化为深度和法向量估计器。
3. 实验表明，该方法在真实和合成数据集上均取得了SOTA结果，并在抓取任务中提高了成功率，验证了方法的有效性。

## 📝 摘要（中文）

透明物体对感知系统来说一直是个难题，折射、反射和透射破坏了立体视觉、飞行时间相机以及纯粹判别式单目深度估计的假设，导致空洞和时间上不稳定的估计。本文的关键观察是，现代视频扩散模型已经合成了令人信服的透明现象，表明它们已经内化了光学规则。为此，作者构建了TransPhy3D，一个透明/反射场景的合成视频语料库，包含1.1万个使用Blender/Cycles渲染的序列。场景由丰富的静态资产和程序化资产组成，并配以玻璃/塑料/金属材料。使用基于物理的光线追踪和OptiX降噪渲染RGB +深度+法向量。从大型视频扩散模型出发，通过轻量级的LoRA适配器学习视频到视频的深度（和法向量）转换器。在训练过程中，将RGB和（带噪声的）深度潜在变量连接在DiT骨干网络中，并在TransPhy3D和现有的逐帧合成数据集上进行联合训练，从而为任意长度的输入视频产生时间一致的预测。由此产生的模型DKT在涉及透明度的真实和合成视频基准测试（ClearPose、DREDS和TransPhy3D-Test）上实现了零样本SOTA。它提高了精度和时间一致性，并且一个法向量变体在ClearPose上设置了最佳视频法向量估计结果。一个紧凑的1.3B版本以约0.17秒/帧的速度运行。集成到抓取堆栈中，DKT的深度提高了半透明、反射和漫反射表面的成功率，优于先前的估计器。总之，这些结果支持一个更广泛的论点：“扩散知道透明度。”生成视频先验可以被重新利用，高效且无标签地转化为鲁棒的、时间连贯的感知，用于具有挑战性的真实世界操作。

## 🔬 方法详解

**问题定义**：论文旨在解决透明和反射物体深度和法向量估计的问题。现有方法，如立体视觉、ToF传感器和单目深度估计，在处理透明物体时会失效，导致深度估计不准确、存在空洞以及时间上的不稳定性。这些方法无法很好地处理由于折射、反射和透射等现象引起的光线传播变化。

**核心思路**：论文的核心思路是利用视频扩散模型已经学习到的关于透明物体光学特性的先验知识。作者认为，如果扩散模型能够生成逼真的透明效果，那么它一定已经内化了相关的物理规则。因此，可以通过训练将视频扩散模型转化为深度和法向量估计器，从而解决透明物体的感知问题。

**技术框架**：整体框架包括以下几个主要步骤：1) 构建大规模合成数据集TransPhy3D，包含透明和反射场景的视频序列，并提供精确的深度和法向量标签。2) 基于大型视频扩散模型，使用LoRA适配器学习视频到视频的转换器，用于预测深度和法向量。3) 在训练过程中，将RGB图像和带噪声的深度潜在变量连接到DiT骨干网络中，并在TransPhy3D和现有数据集上进行联合训练，以提高模型的泛化能力和时间一致性。

**关键创新**：该论文的关键创新在于将视频扩散模型用于透明物体的深度和法向量估计。与传统方法不同，该方法不依赖于特定的几何或光度假设，而是利用扩散模型学习到的先验知识来推断透明物体的深度和法向量。此外，使用LoRA适配器可以高效地将大型扩散模型适应于新的任务。

**关键设计**：TransPhy3D数据集包含1.1万个视频序列，使用Blender/Cycles渲染，并使用OptiX降噪。训练过程中，使用LoRA适配器来微调视频扩散模型，并采用联合训练策略，结合TransPhy3D和现有数据集。损失函数包括深度和法向量的L1损失，以及时间一致性损失。模型使用DiT作为骨干网络，并使用RGB和深度潜在变量的连接作为输入。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.23705v1/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.23705v1/x2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.23705v1/x3.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

DKT在ClearPose、DREDS和TransPhy3D-Test等数据集上实现了零样本SOTA，显著提高了透明物体深度和法向量估计的准确性和时间一致性。在ClearPose数据集上，法向量估计结果达到了最佳水平。此外，一个紧凑的1.3B版本模型运行速度达到0.17秒/帧，具有实际应用价值。集成到抓取堆栈后，DKT显著提高了半透明、反射和漫反射表面的抓取成功率。

## 🎯 应用场景

该研究成果可应用于机器人抓取、自动驾驶、增强现实等领域。在机器人抓取中，准确的深度估计可以帮助机器人更好地识别和抓取透明或反射物体。在自动驾驶中，可以提高车辆对透明物体的感知能力，例如挡风玻璃、水面等。在增强现实中，可以更真实地渲染虚拟物体与真实透明物体的交互。

## 📄 摘要（原文）

> Transparent objects remain notoriously hard for perception systems: refraction, reflection and transmission break the assumptions behind stereo, ToF and purely discriminative monocular depth, causing holes and temporally unstable estimates. Our key observation is that modern video diffusion models already synthesize convincing transparent phenomena, suggesting they have internalized the optical rules. We build TransPhy3D, a synthetic video corpus of transparent/reflective scenes: 11k sequences rendered with Blender/Cycles. Scenes are assembled from a curated bank of category-rich static assets and shape-rich procedural assets paired with glass/plastic/metal materials. We render RGB + depth + normals with physically based ray tracing and OptiX denoising. Starting from a large video diffusion model, we learn a video-to-video translator for depth (and normals) via lightweight LoRA adapters. During training we concatenate RGB and (noisy) depth latents in the DiT backbone and co-train on TransPhy3D and existing frame-wise synthetic datasets, yielding temporally consistent predictions for arbitrary-length input videos. The resulting model, DKT, achieves zero-shot SOTA on real and synthetic video benchmarks involving transparency: ClearPose, DREDS (CatKnown/CatNovel), and TransPhy3D-Test. It improves accuracy and temporal consistency over strong image/video baselines, and a normal variant sets the best video normal estimation results on ClearPose. A compact 1.3B version runs at ~0.17 s/frame. Integrated into a grasping stack, DKT's depth boosts success rates across translucent, reflective and diffuse surfaces, outperforming prior estimators. Together, these results support a broader claim: "Diffusion knows transparency." Generative video priors can be repurposed, efficiently and label-free, into robust, temporally coherent perception for challenging real-world manipulation.

