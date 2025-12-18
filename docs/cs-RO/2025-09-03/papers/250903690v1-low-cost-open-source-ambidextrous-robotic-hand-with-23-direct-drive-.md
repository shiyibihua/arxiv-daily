---
layout: default
title: Low-Cost Open-Source Ambidextrous Robotic Hand with 23 Direct-Drive servos for American Sign Language Alphabet
---

# Low-Cost Open-Source Ambidextrous Robotic Hand with 23 Direct-Drive servos for American Sign Language Alphabet

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.03690" class="toolbar-btn" target="_blank">📄 arXiv: 2509.03690v1</a>
  <a href="https://arxiv.org/pdf/2509.03690.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.03690v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.03690v1', 'Low-Cost Open-Source Ambidextrous Robotic Hand with 23 Direct-Drive servos for American Sign Language Alphabet')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Kelvin Daniel Gonzalez Amador

**分类**: cs.RO

**发布日期**: 2025-09-03

**备注**: 9 pages, 8 figures, 4 tables. Submitted as preprint

---

## 💡 一句话要点

**VulcanV3：低成本开源灵巧手，通过23个直驱舵机实现美国手语字母**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)**

**关键词**: `机器人手语` `灵巧手` `开源硬件` `3D打印` `直驱舵机` `美国手语` `辅助机器人`

## 📋 核心要点

1. 现有机器人手语解决方案成本高昂且功能有限，难以满足聋人社群的交流需求。
2. VulcanV3采用低成本3D打印和直驱舵机，设计为灵巧手，能够准确复现完整的美国手语字母表。
3. 实验结果表明，VulcanV3能准确再现52个ASL手势，用户研究识别准确率高达98.78%。

## 📝 摘要（中文）

本研究提出了VulcanV3，一种低成本、开源、3D打印的灵巧机械手，能够复现完整的美国手语（ASL）字母表（左右手配置共52个手势）。该系统采用23个直驱舵机，实现精确的手指和手腕运动，由带有双PCA9685模块的Arduino Mega控制。与大多数很少采用直驱驱动的人形上肢系统不同，VulcanV3通过可逆设计实现了完整的ASL覆盖。所有CAD文件和代码均以宽松的开源许可发布，以方便复制。实证测试证实了所有52个ASL手形的准确再现，参与者研究（n = 33）实现了96.97%的识别准确率，在视频演示后提高到98.78%。VulcanV3通过在一个开放共享的平台上结合经济性、完整的ASL覆盖和灵巧性，推进了辅助机器人技术，为可访问的通信技术和包容性创新做出了贡献。

## 🔬 方法详解

**问题定义**：现有机器人手语系统通常价格昂贵，且在手语表达的完整性和灵活性方面存在局限性。许多系统难以覆盖整个美国手语字母表，并且缺乏左右手通用的设计。此外，闭源设计限制了其可访问性和可定制性。

**核心思路**：VulcanV3的核心思路是利用低成本的3D打印技术和现成的直驱舵机，构建一个经济实惠、功能全面且开源的灵巧手。通过精心设计的机械结构和控制算法，实现对美国手语字母表的完整覆盖，并提供左右手通用的设计，增强系统的实用性和可扩展性。

**技术框架**：VulcanV3系统主要由以下几个部分组成：1）机械手本体：采用3D打印技术制造，包含手指、手掌和手腕等结构。2）驱动系统：使用23个直驱舵机控制手指和手腕的运动。3）控制系统：基于Arduino Mega和PCA9685模块，实现对舵机的精确控制。4）软件系统：包含手语手势的运动规划和控制算法，以及用户界面。

**关键创新**：VulcanV3的关键创新在于其低成本、开源和灵巧的设计。与传统机器人手语系统相比，VulcanV3显著降低了成本，并通过开源设计促进了社区的参与和改进。此外，直驱舵机的使用提高了运动的精度和响应速度，使得系统能够更准确地复现复杂的手语手势。左右手通用的设计也增强了系统的灵活性和适用性。

**关键设计**：VulcanV3的关键设计包括：1）采用模块化设计，方便组装和维护。2）优化机械结构，提高手指的灵活性和抓取能力。3）设计精确的运动规划算法，实现手语手势的平滑过渡。4）使用PID控制算法，提高舵机的控制精度。5）开源所有CAD文件和代码，方便用户进行定制和扩展。

## 📊 实验亮点

VulcanV3的实验结果表明，该系统能够准确再现所有52个美国手语字母表手势。用户研究表明，参与者对手语手势的识别准确率高达96.97%，在观看视频演示后，准确率进一步提高到98.78%。这些结果表明，VulcanV3在手语交流方面具有很高的实用价值。

## 🎯 应用场景

VulcanV3具有广泛的应用前景，可用于辅助聋哑人进行交流，例如在教育、医疗和公共服务等领域。此外，该系统还可以作为机器人研究和开发的平台，用于探索更复杂的人机交互和手势识别技术。开源的设计也促进了其在康复机器人、远程操作等领域的应用。

## 📄 摘要（原文）

> Accessible communication through sign language is vital for deaf communities, 1 yet robotic solutions are often costly and limited. This study presents VulcanV3, a low- 2 cost, open-source, 3D-printed ambidextrous robotic hand capable of reproducing the full 3 American Sign Language (ASL) alphabet (52 signs for right- and left-hand configurations). 4 The system employs 23 direct-drive servo actuators for precise finger and wrist movements, 5 controlled by an Arduino Mega with dual PCA9685 modules. Unlike most humanoid upper- 6 limb systems, which rarely employ direct-drive actuation, VulcanV3 achieves complete ASL 7 coverage with a reversible design. All CAD files and code are released under permissive 8 open-source licenses to enable replication. Empirical tests confirmed accurate reproduction 9 of all 52 ASL handshapes, while a participant study (n = 33) achieved 96.97% recognition 10 accuracy, improving to 98.78% after video demonstration. VulcanV3 advances assistive 11 robotics by combining affordability, full ASL coverage, and ambidexterity in an openly 12 shared platform, contributing to accessible communication technologies and inclusive 13 innovation.

