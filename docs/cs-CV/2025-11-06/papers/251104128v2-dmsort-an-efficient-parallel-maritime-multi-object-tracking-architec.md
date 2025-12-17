---
layout: default
title: DMSORT: An efficient parallel maritime multi-object tracking architecture for unmanned vessel platforms
---

# DMSORT: An efficient parallel maritime multi-object tracking architecture for unmanned vessel platforms

**arXiv**: [2511.04128v2](https://arxiv.org/abs/2511.04128) | [PDF](https://arxiv.org/pdf/2511.04128.pdf)

**作者**: Shengyu Tang, Zeyuan Lu, Jiazhi Dong, Changdong Yu, Xiaoyu Wang, Yaohui Lyu, Weihao Xia

**分类**: cs.CV, cs.AI

**发布日期**: 2025-11-06 (更新: 2025-11-16)

**备注**: This version clarifies several citation formatting inconsistencies caused by a technical issue in the reference management software used during manuscript preparation. All scientific data, experiments, and conclusions remain fully valid and unaffected. The clarification is provided to maintain transparency and consistency in the scholarly record

**DOI**: [10.1016/j.oceaneng.2025.123045](https://doi.org/10.1016/j.oceaneng.2025.123045)

**🔗 代码/项目**: [GITHUB](https://github.com/BiscuitsLzy/DMSORT-An-efficient-parallel-maritime-multi-object-tracking-architecture-)

---

## 💡 一句话要点

**DMSORT：一种高效的并行海事多目标跟踪架构，适用于无人船平台**

🎯 **匹配领域**: **支柱三：空间感知 (Perception & SLAM)**

**关键词**: `多目标跟踪` `无人船` `海事环境` `运动补偿` `深度学习`

## 📋 核心要点

1. 复杂海事环境下的相机运动和视觉退化对多目标跟踪（MOT）构成挑战，现有方法难以兼顾精度与速度。
2. DMSORT采用双分支并行跟踪器，分别处理目标检测与重识别以及动态相机运动估计，实现运动补偿。
3. 实验表明，DMSORT在新加坡海事数据集上达到SOTA性能，并在保持高一致性的同时，运行速度最快。

## 📝 摘要（中文）

为了确保船舶安全航行和有效海事监视，通过稳健的多目标跟踪（MOT）对海洋环境进行精确感知至关重要。然而，复杂的海事环境经常导致相机运动和随后的视觉退化，给MOT带来重大挑战。为了应对这一挑战，我们提出了一种高效的双分支海事SORT（DMSORT）方法用于海事MOT。该框架的核心是一个具有仿射补偿的并行跟踪器，它结合了一个目标检测和重识别（ReID）分支，以及一个用于动态相机运动估计的专用分支。具体来说，一个可逆柱状检测网络（RCDN）被集成到检测模块中，以利用多层次的视觉特征进行鲁棒的目标检测。此外，设计了一个轻量级的基于Transformer的外观提取器（Li-TAE）来捕获全局上下文信息并生成鲁棒的外观特征。另一个分支通过构建投影变换来解耦平台引起的运动和目标固有的运动，在卡尔曼滤波器中应用平台运动补偿，从而稳定真实的目标轨迹。最后，一个聚类优化的特征融合模块有效地结合了运动和外观线索，以确保在噪声、遮挡和漂移下的身份一致性。在新加坡海事数据集上的大量评估表明，DMSORT实现了最先进的性能。值得注意的是，DMSORT在现有的基于ReID的MOT框架中实现了最快的运行时间，同时保持了高身份一致性和对抖动和遮挡的鲁棒性。

## 🔬 方法详解

**问题定义**：论文旨在解决复杂海事环境下，由于相机运动和视觉退化导致的多目标跟踪（MOT）问题。现有方法难以在精度、速度和鲁棒性之间取得平衡，尤其是在存在噪声、遮挡和漂移的情况下，目标身份容易丢失。

**核心思路**：DMSORT的核心思路是将MOT任务分解为两个并行分支：一个分支负责目标检测和重识别（ReID），提取目标的视觉特征；另一个分支负责估计和补偿由平台运动引起的相机运动。通过这种方式，可以有效地解耦平台运动和目标自身运动，从而提高跟踪的准确性和鲁棒性。

**技术框架**：DMSORT的整体架构是一个双分支并行跟踪器。主要包含以下模块：1) Reversible Columnar Detection Network (RCDN)：用于目标检测，提取多层次视觉特征。2) Lightweight Transformer-based Appearance Extractor (Li-TAE)：用于提取目标的全局上下文外观特征。3) 运动估计分支：通过构建投影变换估计平台运动。4) 卡尔曼滤波器：结合运动估计结果进行平台运动补偿，稳定目标轨迹。5) 聚类优化的特征融合模块：融合运动和外观特征，确保身份一致性。

**关键创新**：DMSORT的关键创新在于其双分支并行跟踪架构和运动补偿机制。通过并行处理视觉特征和运动信息，可以更有效地应对复杂海事环境中的挑战。此外，RCDN和Li-TAE的设计也提高了目标检测和外观特征提取的鲁棒性。

**关键设计**：RCDN采用可逆柱状结构，可以更有效地利用多层次视觉特征。Li-TAE采用轻量级Transformer结构，可以在保证性能的同时降低计算复杂度。运动估计分支通过构建投影变换来估计平台运动，并将其应用于卡尔曼滤波器中进行运动补偿。聚类优化的特征融合模块采用自适应权重，根据不同情况调整运动和外观特征的贡献。

## 📊 实验亮点

DMSORT在新加坡海事数据集上取得了最先进的性能，在MOTA、IDF1等指标上均优于现有方法。值得注意的是，DMSORT在保持高身份一致性和对抖动和遮挡的鲁棒性的同时，实现了最快的运行速度，使其更适合于实时应用。

## 🎯 应用场景

DMSORT可广泛应用于无人船、自主水面舰艇等平台，实现自主导航、环境感知和目标监视。该研究成果有助于提升海上交通安全、海洋资源管理和海上安防能力，具有重要的实际应用价值和广阔的发展前景。

## 📄 摘要（原文）

> Accurate perception of the marine environment through robust multi-object tracking (MOT) is essential for ensuring safe vessel navigation and effective maritime surveillance. However, the complicated maritime environment often causes camera motion and subsequent visual degradation, posing significant challenges to MOT. To address this challenge, we propose an efficient Dual-branch Maritime SORT (DMSORT) method for maritime MOT. The core of the framework is a parallel tracker with affine compensation, which incorporates an object detection and re-identification (ReID) branch, along with a dedicated branch for dynamic camera motion estimation. Specifically, a Reversible Columnar Detection Network (RCDN) is integrated into the detection module to leverage multi-level visual features for robust object detection. Furthermore, a lightweight Transformer-based appearance extractor (Li-TAE) is designed to capture global contextual information and generate robust appearance features. Another branch decouples platform-induced and target-intrinsic motion by constructing a projective transformation, applying platform-motion compensation within the Kalman filter, and thereby stabilizing true object trajectories. Finally, a clustering-optimized feature fusion module effectively combines motion and appearance cues to ensure identity consistency under noise, occlusion, and drift. Extensive evaluations on the Singapore Maritime Dataset demonstrate that DMSORT achieves state-of-the-art performance. Notably, DMSORT attains the fastest runtime among existing ReID-based MOT frameworks while maintaining high identity consistency and robustness to jitter and occlusion. Code is available at: https://github.com/BiscuitsLzy/DMSORT-An-efficient-parallel-maritime-multi-object-tracking-architecture-.

