---
layout: default
title: 3D Printable Soft Liquid Metal Sensors for Delicate Manipulation Tasks
---

# 3D Printable Soft Liquid Metal Sensors for Delicate Manipulation Tasks

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.17389" class="toolbar-btn" target="_blank">📄 arXiv: 2509.17389v1</a>
  <a href="https://arxiv.org/pdf/2509.17389.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.17389v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.17389v1', '3D Printable Soft Liquid Metal Sensors for Delicate Manipulation Tasks')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Lois Liow, Jonty Milford, Emre Uygun, Andre Farinha, Vinoth Viswanathan, Josh Pinskier, David Howard

**分类**: cs.RO

**发布日期**: 2025-09-22

**备注**: 8 pages, 4 figures

---

## 💡 一句话要点

**提出基于3D打印软体液态金属传感器的精细操作方法，用于脆弱物品操作**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `软体机器人` `3D打印` `液态金属传感器` `精细操作` `物理孪生体`

## 📋 核心要点

1. 现有方法难以安全地与脆弱样本交互，且缺乏足够的数据来训练操作策略，尤其是在珊瑚等生态保护领域。
2. 论文提出一种基于3D打印的软体液态金属传感器，能够高保真地复制复杂自然几何形状，实现精细操作的传感。
3. 实验表明，该传感器能够检测到低于0.5N的抓取力，并在自动珊瑚标记和机器人珊瑚养殖中展示了应用价值。

## 📝 摘要（中文）

本文提出了一种新颖的方法，用于打印自由形式、高度传感化的软体“物理孪生体”。该方法提供了一个自动化的设计流程，可以根据3D扫描或模型按需创建复杂且可定制的3D软传感结构。与现有技术相比，我们的软体液态金属传感器能够忠实地再现复杂的自然几何形状，并表现出优异的传感特性，适用于验证精细操作任务中的性能。我们展示了物理孪生体在“传感珊瑚”中的应用：高保真、3D打印的珊瑚复制品，无需活珊瑚实验，同时提高数据质量，为推进自主珊瑚处理和广泛的软操作提供了一种合乎伦理且可扩展的途径。通过广泛的台式操作和水下抓取实验，我们表明我们的传感珊瑚能够检测到低于0.5 N的抓取力，有效地捕捉珊瑚处理所需的精细交互和轻微接触力。最后，我们展示了我们的物理孪生体在两个演示中的价值：（i）用于实验室识别的自动珊瑚标记和（ii）机器人珊瑚养殖。像我们这样的传感物理孪生体可以提供比传统传感器更丰富的抓取反馈，为部署前处理脆弱物品提供实验验证。

## 🔬 方法详解

**问题定义**：目前在处理脆弱物品，如珊瑚时，面临两个主要问题。一是难以安全地与这些脆弱样本进行交互，避免造成损害。二是缺乏足够的数据来训练机器人进行精细操作，尤其是在强化学习等方法中，需要大量安全的数据采集。现有的传感器和操作方法难以同时满足这两个需求。

**核心思路**：论文的核心思路是利用3D打印技术，创建软体的、具有高灵敏度传感器的“物理孪生体”。这些物理孪生体可以复制真实物体的几何形状和物理特性，同时内置液态金属传感器，能够感知微小的接触力和压力。通过在物理孪生体上进行实验，可以安全地获取数据，训练机器人进行精细操作，而无需直接操作真实的脆弱物品。

**技术框架**：整体流程包括以下几个主要步骤：1. 对真实物体进行3D扫描或建模，获取其几何信息。2. 根据3D模型，设计软体物理孪生体的结构，包括传感器的布局和形状。3. 使用3D打印技术，将软体结构打印出来，并将液态金属注入到预留的通道中，形成传感器。4. 使用物理孪生体进行操作实验，获取传感数据。5. 利用传感数据训练机器人操作策略。

**关键创新**：最重要的技术创新点在于将3D打印技术与液态金属传感器相结合，创造出具有高保真度和高灵敏度的软体物理孪生体。与传统的刚性传感器相比，软体传感器能够更好地适应复杂物体的形状，并感知微小的力。与现有的软体传感器相比，该方法能够更精确地复制复杂几何形状，并实现定制化的传感器布局。

**关键设计**：论文中没有详细描述具体的参数设置、损失函数或网络结构，因为这取决于具体的应用场景和机器人操作策略。但是，关键的设计在于液态金属传感器的布局和形状，需要根据物体的几何形状和操作任务进行优化，以实现最佳的传感性能。此外，软体材料的选择也很重要，需要具有足够的柔韧性和强度，以承受操作过程中的力和变形。

## 📊 实验亮点

实验结果表明，该传感珊瑚能够检测到低于0.5 N的抓取力，有效地捕捉珊瑚处理所需的精细交互和轻微接触力。在自动珊瑚标记和机器人珊瑚养殖的演示中，展示了物理孪生体的实际应用价值。这些结果表明，该方法能够提供比传统传感器更丰富的抓取反馈，为部署前处理脆弱物品提供实验验证。

## 🎯 应用场景

该研究成果可广泛应用于需要精细操作的领域，例如：脆弱物品的处理、生物样本的采集和分析、医疗手术辅助、食品加工等。通过使用物理孪生体，可以安全地进行实验和数据采集，降低操作风险，提高操作效率。此外，该技术还可以用于机器人教育和培训，帮助学生和工程师更好地理解和掌握精细操作技术。

## 📄 摘要（原文）

> Robotics and automation are key enablers to increase throughput in ongoing conservation efforts across various threatened ecosystems. Cataloguing, digitisation, husbandry, and similar activities require the ability to interact with delicate, fragile samples without damaging them. Additionally, learning-based solutions to these tasks require the ability to safely acquire data to train manipulation policies through, e.g., reinforcement learning. To address these twin needs, we introduce a novel method to print free-form, highly sensorised soft 'physical twins'. We present an automated design workflow to create complex and customisable 3D soft sensing structures on demand from 3D scans or models. Compared to the state of the art, our soft liquid metal sensors faithfully recreate complex natural geometries and display excellent sensing properties suitable for validating performance in delicate manipulation tasks. We demonstrate the application of our physical twins as 'sensing corals': high-fidelity, 3D printed replicas of scanned corals that eliminate the need for live coral experimentation, whilst increasing data quality, offering an ethical and scalable pathway for advancing autonomous coral handling and soft manipulation broadly. Through extensive bench-top manipulation and underwater grasping experiments, we show that our sensing coral is able to detect grasps under 0.5 N, effectively capturing the delicate interactions and light contact forces required for coral handling. Finally, we showcase the value of our physical twins across two demonstrations: (i) automated coral labelling for lab identification and (ii) robotic coral aquaculture. Sensing physical twins such as ours can provide richer grasping feedback than conventional sensors providing experimental validation of prior to deployment in handling fragile and delicate items.

