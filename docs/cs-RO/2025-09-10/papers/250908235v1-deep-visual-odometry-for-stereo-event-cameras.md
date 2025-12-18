---
layout: default
title: Deep Visual Odometry for Stereo Event Cameras
---

# Deep Visual Odometry for Stereo Event Cameras

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.08235" class="toolbar-btn" target="_blank">📄 arXiv: 2509.08235v1</a>
  <a href="https://arxiv.org/pdf/2509.08235.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.08235v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.08235v1', 'Deep Visual Odometry for Stereo Event Cameras')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Sheng Zhong, Junkai Niu, Yi Zhou

**分类**: cs.RO

**发布日期**: 2025-09-10

---

## 💡 一句话要点

**提出Stereo-DEVO，一种用于立体事件相机的深度视觉里程计，提升了在HDR环境下的位姿估计精度。**

🎯 **匹配领域**: **支柱三：空间感知与语义 (Perception & Semantics)**

**关键词**: `事件相机` `视觉里程计` `深度学习` `立体视觉` `位姿估计`

## 📋 核心要点

1. 现有事件相机视觉里程计在低光照HDR环境下，由于动态范围巨大和信噪比时空变化，数据关联不可靠。
2. Stereo-DEVO利用深度学习，通过静态立体关联进行稀疏深度估计，并结合紧耦合BA优化，提升位姿估计精度。
3. 该系统能实时处理VGA分辨率事件数据，并在真实世界数据集和HDR场景中表现出优于现有方法的性能。

## 📝 摘要（中文）

本文提出了一种基于学习的立体事件视觉里程计（Stereo-DEVO），旨在解决事件相机在运动模糊和高动态范围（HDR）光照条件下状态估计任务的挑战。现有基于手工数据关联的事件视觉里程计在低光照HDR条件下表现不稳定。Stereo-DEVO基于深度事件视觉里程计（DEVO），引入了一种新颖高效的静态立体关联策略，用于稀疏深度估计，几乎没有额外的计算负担。通过将其集成到紧耦合的捆绑调整（BA）优化方案中，并受益于循环网络通过基于体素的事件表示执行精确光流估计以建立可靠的patch关联的能力，该系统实现了高精度的度量尺度位姿估计。与DEVO的离线性能相比，该系统可以实时处理VGA分辨率的事件数据。在多个公共真实世界数据集和自采集数据上的广泛评估证明了该系统的通用性，与最先进的基于事件的VO方法相比，表现出卓越的性能。更重要的是，该系统即使在大型夜间HDR场景中也能实现稳定的位姿估计。

## 🔬 方法详解

**问题定义**：论文旨在解决事件相机在复杂光照条件（尤其是低光照HDR环境）下，传统视觉里程计方法因数据关联不可靠而导致的位姿估计精度下降问题。现有方法依赖手工设计的特征和关联策略，难以适应事件相机数据固有的噪声和动态范围变化。

**核心思路**：论文的核心思路是利用深度学习方法，特别是循环神经网络，学习事件数据中的光流信息，并结合立体视觉的几何约束，实现更鲁棒和精确的位姿估计。通过学习到的光流信息，建立事件patch之间的可靠关联，克服了手工特征的局限性。

**技术框架**：Stereo-DEVO系统主要包含以下几个模块：1) 事件数据体素化表示：将事件流转换为体素网格；2) 基于循环神经网络的光流估计：利用RNN学习体素网格中的光流信息；3) 静态立体关联：利用立体相机信息进行稀疏深度估计；4) 紧耦合捆绑调整（BA）：将光流估计和深度估计结果融合到BA优化框架中，实现位姿估计。

**关键创新**：该论文的关键创新在于：1) 提出了一种高效的静态立体关联策略，用于稀疏深度估计，计算负担小；2) 将深度学习的光流估计与立体视觉几何约束相结合，提高了位姿估计的鲁棒性和精度；3) 系统能够实时处理VGA分辨率的事件数据，具有实际应用价值。

**关键设计**：在网络结构方面，使用了循环神经网络（RNN）来学习事件数据中的时序信息，从而进行光流估计。损失函数方面，可能使用了光流一致性损失、深度一致性损失等，以约束光流和深度估计的准确性。静态立体关联的具体实现方式（例如，如何选择用于关联的事件）以及BA优化框架的具体参数设置（例如，权重分配）是影响系统性能的关键设计细节。

## 📊 实验亮点

Stereo-DEVO在多个公开数据集和自采集数据集上进行了评估，实验结果表明，该系统在位姿估计精度方面优于现有的基于事件的视觉里程计方法。更重要的是，该系统在大型夜间HDR场景中实现了稳定的位姿估计，证明了其在复杂光照条件下的鲁棒性。此外，该系统能够实时处理VGA分辨率的事件数据，具有实际应用价值。

## 🎯 应用场景

该研究成果可应用于机器人导航、自动驾驶、无人机等领域，尤其是在光照条件恶劣或动态范围高的场景下，例如夜间或隧道等环境。Stereo-DEVO能够提供更稳定和精确的位姿估计，从而提高机器人的自主性和可靠性。未来，该技术有望进一步扩展到增强现实、虚拟现实等领域。

## 📄 摘要（原文）

> Event-based cameras are bio-inspired sensors with pixels that independently and asynchronously respond to brightness changes at microsecond resolution, offering the potential to handle state estimation tasks involving motion blur and high dynamic range (HDR) illumination conditions. However, the versatility of event-based visual odometry (VO) relying on handcrafted data association (either direct or indirect methods) is still unreliable, especially in field robot applications under low-light HDR conditions, where the dynamic range can be enormous and the signal-to-noise ratio is spatially-and-temporally varying. Leveraging deep neural networks offers new possibilities for overcoming these challenges. In this paper, we propose a learning-based stereo event visual odometry. Building upon Deep Event Visual Odometry (DEVO), our system (called Stereo-DEVO) introduces a novel and efficient static-stereo association strategy for sparse depth estimation with almost no additional computational burden. By integrating it into a tightly coupled bundle adjustment (BA) optimization scheme, and benefiting from the recurrent network's ability to perform accurate optical flow estimation through voxel-based event representations to establish reliable patch associations, our system achieves high-precision pose estimation in metric scale. In contrast to the offline performance of DEVO, our system can process event data of \zs{Video Graphics Array} (VGA) resolution in real time. Extensive evaluations on multiple public real-world datasets and self-collected data justify our system's versatility, demonstrating superior performance compared to state-of-the-art event-based VO methods. More importantly, our system achieves stable pose estimation even in large-scale nighttime HDR scenarios.

