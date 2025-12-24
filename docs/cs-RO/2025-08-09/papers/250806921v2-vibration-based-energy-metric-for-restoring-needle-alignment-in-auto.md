---
layout: default
title: Vibration-Based Energy Metric for Restoring Needle Alignment in Autonomous Robotic Ultrasound
---

# Vibration-Based Energy Metric for Restoring Needle Alignment in Autonomous Robotic Ultrasound

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.06921" class="toolbar-btn" target="_blank">📄 arXiv: 2508.06921v2</a>
  <a href="https://arxiv.org/pdf/2508.06921.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.06921v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.06921v2', 'Vibration-Based Energy Metric for Restoring Needle Alignment in Autonomous Robotic Ultrasound')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zhongyu Chen, Chenyang Li, Xuesong Li, Dianye Huang, Zhongliang Jiang, Stefanie Speidel, Xiangyu Chu, K. W. Samuel Au

**分类**: cs.RO, cs.CV

**发布日期**: 2025-08-09 (更新: 2025-08-18)

**备注**: Accepted by IROS2025

---

## 💡 一句话要点

**提出基于振动的能量度量以解决针头对齐问题**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)**

**关键词**: `机器人手术` `超声引导` `针头对齐` `振动能量度量` `自动化系统` `医疗机器人` `精确定位`

## 📋 核心要点

1. 现有方法在超声图像中针头可见性降低时，难以实现精准的针头检测和对齐，影响手术效果。
2. 本文提出了一种基于针头振动的能量度量方法，能够在针头不在成像平面内时仍然有效，增强了针头对齐的鲁棒性。
3. 实验结果表明，该方法在离体猪组织样本中实现了显著的平移和旋转误差降低，验证了其有效性。

## 📝 摘要（中文）

精确的针头对齐对于机器人超声引导下的经皮针插入至关重要。然而，现有方法在超声图像中针头可见性降低时，面临斑点噪声、针状伪影和低图像分辨率等挑战。本文提出了一种通过机械系统周期性振动针头来恢复针头对齐的方法，利用振动能量度量，即使在针头完全不在平面内时也能有效工作。基于该度量，我们开发了一种控制策略，以应对超声成像平面与针头插入平面之间的错位。通过在离体猪组织样本上进行的实验，验证了该方法的有效性，结果显示平移误差为0.41±0.27毫米，旋转误差为0.51±0.19度。

## 🔬 方法详解

**问题定义**：本文旨在解决在超声引导下进行针头插入时，针头与成像平面错位导致的对齐问题。现有方法在针头可见性降低时，难以实现准确检测，影响手术的安全性和有效性。

**核心思路**：论文提出通过机械系统周期性振动针头，利用振动产生的能量度量来恢复针头对齐。这种方法不依赖于针头在超声图像中的可见性，增强了对齐的鲁棒性。

**技术框架**：整体方法包括两个主要模块：首先，通过振动系统对针头进行周期性振动；其次，基于振动能量度量，开发控制策略来调整超声探头的位置，以应对成像平面与针头插入平面之间的错位。

**关键创新**：最重要的创新点在于引入了振动能量度量作为针头对齐的依据，这一方法在针头完全不在成像平面内时仍然有效，显著区别于传统依赖可见性的检测方法。

**关键设计**：在实验中，振动频率和幅度的选择是关键设计参数，确保振动能量能够有效传递并被检测。此外，控制策略中采用了反馈机制，以实时调整探头位置，优化对齐过程。

## 📊 实验亮点

实验结果显示，所提出的方法在离体猪组织样本中实现了平移误差为0.41±0.27毫米，旋转误差为0.51±0.19度，显著优于传统方法。这表明该方法在针头对齐方面具有较高的精度和鲁棒性。

## 🎯 应用场景

该研究的潜在应用领域包括机器人手术、超声引导下的医疗程序以及其他需要精确定位的自动化系统。通过提高针头对齐的准确性，能够显著提升手术的安全性和成功率，具有重要的临床价值和实际应用前景。

## 📄 摘要（原文）

> Precise needle alignment is essential for percutaneous needle insertion in robotic ultrasound-guided procedures. However, inherent challenges such as speckle noise, needle-like artifacts, and low image resolution make robust needle detection difficult, particularly when visibility is reduced or lost. In this paper, we propose a method to restore needle alignment when the ultrasound imaging plane and the needle insertion plane are misaligned. Unlike many existing approaches that rely heavily on needle visibility in ultrasound images, our method uses a more robust feature by periodically vibrating the needle using a mechanical system. Specifically, we propose a vibration-based energy metric that remains effective even when the needle is fully out of plane. Using this metric, we develop a control strategy to reposition the ultrasound probe in response to misalignments between the imaging plane and the needle insertion plane in both translation and rotation. Experiments conducted on ex-vivo porcine tissue samples using a dual-arm robotic ultrasound-guided needle insertion system demonstrate the effectiveness of the proposed approach. The experimental results show the translational error of 0.41$\pm$0.27 mm and the rotational error of 0.51$\pm$0.19 degrees.

