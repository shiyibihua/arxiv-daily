---
layout: default
title: PuffyBot: An Untethered Shape Morphing Robot for Multi-environment Locomotion
---

# PuffyBot: An Untethered Shape Morphing Robot for Multi-environment Locomotion

<div class="paper-toolbar">
  <div class="toolbar-left">
    <a href="https://arxiv.org/abs/2511.09885" target="_blank" class="toolbar-btn">arXiv: 2511.09885v1</a>
    <a href="https://arxiv.org/pdf/2511.09885.pdf" target="_blank" class="toolbar-btn">PDF</a>
  </div>
  <div class="toolbar-right">
    <button class="toolbar-btn favorite-btn" data-arxiv-id="2511.09885v1" 
            onclick="toggleFavorite(this, '2511.09885v1', 'PuffyBot: An Untethered Shape Morphing Robot for Multi-environment Locomotion')" title="收藏">
      ☆ 收藏
    </button>
    <button class="toolbar-btn share-btn" onclick="copyLink()" title="复制链接">
      🔗 分享
    </button>
  </div>
</div>


**作者**: Shashwat Singh, Zilin Si, Zeynep Temel

**分类**: cs.RO

**发布日期**: 2025-11-13

**备注**: 8 pages, 10 figures, IEEE RoboSoft 2026

---

## 💡 一句话要点

**PuffyBot：一种用于多环境运动的无束缚变形机器人**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)**

**关键词**: `变形机器人` `多环境运动` `剪式升降机构` `浮力调节` `水下机器人`

## 📋 核心要点

1. 现有机器人难以兼顾陆地和水下环境的运动需求，形态固定导致效率低下。
2. PuffyBot通过剪式升降机构实现体积和肢体角度的变形，适应不同环境。
3. 实验验证了PuffyBot在陆地、水下和水面等多种环境下的运动能力。

## 📝 摘要（中文）

本文介绍了一种名为PuffyBot的无束缚变形机器人，其灵感来源于两栖动物在陆地和水生环境中适应形态和运动的能力。该机器人能够改变自身形态以适应多种环境。PuffyBot的设计利用线性致动器驱动的剪式升降机构作为主要结构，实现形状变形，体积变化范围为255.00 cm3到423.75 cm3，从而调节浮力，抵消机器人330克质量产生的3.237牛顿的向下力。剪式升降机构集成了曲柄连杆机构，可将伺服驱动的肢体调整90度，从而在爬行和游泳模式之间实现无缝过渡。机器人完全防水，使用热塑性聚氨酯（TPU）织物以确保在水生环境中的功能。PuffyBot可在1000毫安时的板载电池支持下无束缚运行两小时。实验结果表明，该机器人能够进行多环境运动，包括陆地爬行、水下地面爬行、水面游泳以及用于水下沉没或重新浮出水面的双模式浮力调节。这些发现表明，形状变形技术具有创造适用于各种环境的多功能且节能的机器人平台的潜力。

## 🔬 方法详解

**问题定义**：现有机器人通常针对特定环境设计，难以在陆地和水下等多种环境中高效运动。固定形态限制了其适应性和能量效率。因此，需要一种能够根据环境改变自身形态的机器人，以实现多环境运动能力。

**核心思路**：PuffyBot的核心思路是模仿两栖动物的形态适应性，通过改变自身体积和肢体角度来适应不同的运动环境。通过体积变化调节浮力，适应水下环境；通过肢体角度变化，切换爬行和游泳模式。

**技术框架**：PuffyBot的整体架构包括：1) 剪式升降机构：作为主要结构，实现体积变化；2) 线性致动器：驱动剪式升降机构；3) 曲柄连杆机构：与剪式升降机构集成，调整肢体角度；4) 伺服电机：驱动肢体运动；5) 防水外壳：采用TPU材料，保证水下功能；6) 板载电池：提供无束缚运行的电力。

**关键创新**：PuffyBot的关键创新在于将剪式升降机构与曲柄连杆机构相结合，实现了体积和肢体角度的协同变形。这种设计使得机器人能够在陆地和水下环境中无缝切换运动模式，并根据需要调节浮力。与传统机器人相比，PuffyBot具有更强的环境适应性和能量效率。

**关键设计**：剪式升降机构的设计参数决定了机器人的体积变化范围，线性致动器的选择需要考虑推力和速度。曲柄连杆机构的设计需要保证肢体能够旋转90度。TPU材料的选择需要考虑防水性和柔韧性。电池容量的选择需要平衡续航时间和机器人重量。

## 📊 实验亮点

实验结果表明，PuffyBot能够在陆地、水下地面和水面等多种环境下运动。其体积变化范围为255.00 cm3到423.75 cm3，能够抵消3.237牛顿的向下力。在1000毫安时电池的支持下，PuffyBot可以无束缚运行两小时。这些结果验证了PuffyBot的多环境运动能力和能源效率。

## 🎯 应用场景

PuffyBot具有广泛的应用前景，包括水下勘探、环境监测、搜救行动等。其多环境适应性使其能够在复杂和未知的环境中执行任务，例如在水下管道检查、海洋生物研究、灾难现场搜寻等。未来，可以通过改进其控制算法和传感器系统，进一步提高其自主性和智能化水平。

## 📄 摘要（原文）

> Amphibians adapt their morphologies and motions to accommodate movement in both terrestrial and aquatic environments. Inspired by these biological features, we present PuffyBot, an untethered shape morphing robot capable of changing its body morphology to navigate multiple environments. Our robot design leverages a scissor-lift mechanism driven by a linear actuator as its primary structure to achieve shape morphing. The transformation enables a volume change from 255.00 cm3 to 423.75 cm3, modulating the buoyant force to counteract a downward force of 3.237 N due to 330 g mass of the robot. A bell-crank linkage is integrated with the scissor-lift mechanism, which adjusts the servo-actuated limbs by 90 degrees, allowing a seamless transition between crawling and swimming modes. The robot is fully waterproof, using thermoplastic polyurethane (TPU) fabric to ensure functionality in aquatic environments. The robot can operate untethered for two hours with an onboard battery of 1000 mA h. Our experimental results demonstrate multi-environment locomotion, including crawling on the land, crawling on the underwater floor, swimming on the water surface, and bimodal buoyancy adjustment to submerge underwater or resurface. These findings show the potential of shape morphing to create versatile and energy efficient robotic platforms suitable for diverse environments.

