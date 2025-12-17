---
layout: default
title: OmniTrack++: Omnidirectional Multi-Object Tracking by Learning Large-FoV Trajectory Feedback
---

# OmniTrack++: Omnidirectional Multi-Object Tracking by Learning Large-FoV Trajectory Feedback

<div class="paper-toolbar">
  <div class="toolbar-left">
    <a href="https://arxiv.org/abs/2511.00510" target="_blank" class="toolbar-btn">arXiv: 2511.00510v1</a>
    <a href="https://arxiv.org/pdf/2511.00510.pdf" target="_blank" class="toolbar-btn">PDF</a>
  </div>
  <div class="toolbar-right">
    <button class="toolbar-btn favorite-btn" data-arxiv-id="2511.00510v1" 
            onclick="toggleFavorite(this, '2511.00510v1', 'OmniTrack++: Omnidirectional Multi-Object Tracking by Learning Large-FoV Trajectory Feedback')" title="收藏">
      ☆ 收藏
    </button>
    <button class="toolbar-btn share-btn" onclick="copyLink()" title="复制链接">
      🔗 分享
    </button>
  </div>
</div>


**作者**: Kai Luo, Hao Shi, Kunyu Peng, Fei Teng, Sheng Wu, Kaiwei Wang, Kailun Yang

**分类**: cs.CV, cs.RO, eess.IV

**发布日期**: 2025-11-01

**备注**: Extended version of CVPR 2025 paper arXiv:2503.04565. Datasets and code will be made publicly available at https://github.com/xifen523/OmniTrack

**🔗 代码/项目**: [GITHUB](https://github.com/xifen523/OmniTrack)

---

## 💡 一句话要点

**OmniTrack++：通过学习大视场轨迹反馈实现全向多目标跟踪**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱三：空间感知 (Perception & SLAM)**

**关键词**: `全景多目标跟踪` `轨迹反馈` `全向视觉` `机器人感知` `目标关联`

## 📋 核心要点

1. 全景图像多目标跟踪面临360°视场、分辨率稀释和视角相关失真等挑战，传统方法难以有效应对。
2. OmniTrack++采用反馈驱动框架，利用轨迹线索逐步优化感知，解决全景失真、大搜索空间和身份模糊问题。
3. 在JRDB和EmboTrack数据集上，OmniTrack++显著超越现有技术，HOTA指标分别提升了25.5%和43.07%。

## 📝 摘要（中文）

本文研究全景图像中的多目标跟踪（MOT）问题，它带来了独特的挑战，包括360°视场（FoV）、分辨率稀释和严重的视角相关失真。为窄视场针孔相机设计的传统MOT方法在这些条件下表现不佳。为了解决全景失真、大搜索空间和360°视场下的身份模糊问题，OmniTrack++采用了一种反馈驱动的框架，通过轨迹线索逐步优化感知。DynamicSSM模块首先稳定全景特征，隐式地减轻几何失真。在归一化表示的基础上，FlexiTrack Instances使用轨迹信息反馈进行灵活的定位和可靠的短期关联。为了确保长期鲁棒性，ExpertTrack Memory通过混合专家设计整合外观线索，从而从碎片化的轨迹中恢复并减少身份漂移。最后，Tracklet Management模块根据场景动态自适应地在端到端和跟踪检测模式之间切换，为全景MOT提供了一个平衡且可扩展的解决方案。为了支持严格的评估，我们建立了EmboTrack基准，这是一个全面的全景MOT数据集，包括用四足机器人捕获的QuadTrack和用双足轮腿机器人收集的BipTrack。这些数据集涵盖了广角环境和不同的运动模式，为真实世界的全景感知提供了一个具有挑战性的测试平台。在JRDB和EmboTrack上的大量实验表明，OmniTrack++实现了最先进的性能，在JRDB上实现了+25.5%的HOTA提升，在QuadTrack上实现了+43.07%的HOTA提升，超过了原始的OmniTrack。

## 🔬 方法详解

**问题定义**：论文旨在解决全景图像下的多目标跟踪问题，现有方法在处理全景图像时，由于其360°视场、分辨率稀释和严重的视角相关失真等特性，导致跟踪精度和鲁棒性显著下降。传统方法难以有效处理全景图像带来的大搜索空间和目标身份模糊问题。

**核心思路**：论文的核心思路是采用反馈驱动的框架，利用轨迹信息逐步优化感知结果。通过轨迹线索，可以更准确地进行目标定位和关联，从而提高跟踪的准确性和鲁棒性。这种反馈机制能够有效缓解全景图像带来的几何失真和身份模糊问题。

**技术框架**：OmniTrack++的整体框架包含以下几个主要模块：1) DynamicSSM模块，用于稳定全景特征，减轻几何失真；2) FlexiTrack Instances模块，利用轨迹信息反馈进行灵活的定位和可靠的短期关联；3) ExpertTrack Memory模块，通过混合专家设计整合外观线索，实现长期鲁棒性；4) Tracklet Management模块，根据场景动态自适应地在端到端和跟踪检测模式之间切换。

**关键创新**：OmniTrack++的关键创新在于其反馈驱动的跟踪框架以及各个模块的设计。DynamicSSM模块通过稳定全景特征来减轻几何失真，FlexiTrack Instances模块利用轨迹信息进行灵活定位，ExpertTrack Memory模块通过混合专家设计实现长期鲁棒性。这些模块的协同工作使得OmniTrack++能够有效应对全景图像带来的挑战。与现有方法相比，OmniTrack++更注重利用轨迹信息进行反馈和优化，从而提高了跟踪的准确性和鲁棒性。

**关键设计**：DynamicSSM模块的具体实现细节（例如，所使用的具体网络结构和损失函数）以及ExpertTrack Memory模块中混合专家的具体数量和选择策略等关键参数设置在论文中可能有所描述，但具体细节未知。Tracklet Management模块中切换端到端和跟踪检测模式的具体策略也需要进一步研究论文才能明确。

## 📊 实验亮点

OmniTrack++在JRDB和EmboTrack数据集上取得了显著的性能提升。在JRDB数据集上，HOTA指标提升了25.5%，在QuadTrack数据集上，HOTA指标提升了43.07%，超过了原始的OmniTrack和其他现有方法。这些结果表明，OmniTrack++在全景多目标跟踪方面具有显著的优势。

## 🎯 应用场景

OmniTrack++在机器人导航、自动驾驶、安防监控等领域具有广泛的应用前景。全景多目标跟踪技术可以帮助机器人或车辆更好地理解周围环境，实现更安全、更智能的导航。在安防监控领域，该技术可以用于人群监控、异常行为检测等任务，提高监控效率和准确性。未来，该技术有望应用于更多需要全方位感知和理解的场景。

## 📄 摘要（原文）

> This paper investigates Multi-Object Tracking (MOT) in panoramic imagery, which introduces unique challenges including a 360° Field of View (FoV), resolution dilution, and severe view-dependent distortions. Conventional MOT methods designed for narrow-FoV pinhole cameras generalize unsatisfactorily under these conditions. To address panoramic distortion, large search space, and identity ambiguity under a 360° FoV, OmniTrack++ adopts a feedback-driven framework that progressively refines perception with trajectory cues. A DynamicSSM block first stabilizes panoramic features, implicitly alleviating geometric distortion. On top of normalized representations, FlexiTrack Instances use trajectory-informed feedback for flexible localization and reliable short-term association. To ensure long-term robustness, an ExpertTrack Memory consolidates appearance cues via a Mixture-of-Experts design, enabling recovery from fragmented tracks and reducing identity drift. Finally, a Tracklet Management module adaptively switches between end-to-end and tracking-by-detection modes according to scene dynamics, offering a balanced and scalable solution for panoramic MOT. To support rigorous evaluation, we establish the EmboTrack benchmark, a comprehensive dataset for panoramic MOT that includes QuadTrack, captured with a quadruped robot, and BipTrack, collected with a bipedal wheel-legged robot. Together, these datasets span wide-angle environments and diverse motion patterns, providing a challenging testbed for real-world panoramic perception. Extensive experiments on JRDB and EmboTrack demonstrate that OmniTrack++ achieves state-of-the-art performance, yielding substantial HOTA improvements of +25.5% on JRDB and +43.07% on QuadTrack over the original OmniTrack. Datasets and code will be made publicly available at https://github.com/xifen523/OmniTrack.

