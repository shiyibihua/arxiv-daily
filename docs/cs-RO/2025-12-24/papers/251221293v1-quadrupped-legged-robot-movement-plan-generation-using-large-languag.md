---
layout: default
title: Quadrupped-Legged Robot Movement Plan Generation using Large Language Model
---

# Quadrupped-Legged Robot Movement Plan Generation using Large Language Model

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.21293" class="toolbar-btn" target="_blank">📄 arXiv: 2512.21293v1</a>
  <a href="https://arxiv.org/pdf/2512.21293.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.21293v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.21293v1', 'Quadrupped-Legged Robot Movement Plan Generation using Large Language Model')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Muhtadin, Vincentius Gusti Putu A. B. M., Ahmad Zaini, Mauridhi Hery Purnomo, I Ketut Eddy Purnama, Chastine Fatichah

**分类**: cs.RO, cs.HC

**发布日期**: 2025-12-24

---

## 💡 一句话要点

**提出基于大语言模型的四足机器人自然语言运动规划方法**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `四足机器人` `大语言模型` `自然语言控制` `运动规划` `ROS导航`

## 📋 核心要点

1. 传统四足机器人控制接口门槛高，需要专业技术知识才能有效操作。
2. 利用大语言模型，将自然语言指令转化为机器人可执行的运动规划，降低操作难度。
3. 实验表明，该系统在室内环境中具有较高的成功率，验证了其可行性。

## 📝 摘要（中文）

本文提出了一种新颖的控制框架，该框架集成了大型语言模型（LLM），以实现直观的、基于自然语言的四足机器人导航。为了克服DeepRobotics Jueying Lite 3平台的板载计算约束，该系统采用了一种分布式架构，将高级指令处理卸载到外部服务器。系统利用实时传感器融合（激光雷达、IMU和里程计）将LLM生成的计划转化为可执行的ROS导航命令。在结构化的室内环境中，针对四个不同的场景（从单房间任务到复杂的跨区域导航）进行了实验验证。结果表明，该系统具有鲁棒性，在所有场景中的总体成功率超过90％，验证了基于卸载LLM的规划在现实环境中自主部署四足机器人的可行性。

## 🔬 方法详解

**问题定义**：传统四足机器人的控制依赖于复杂的控制接口，需要操作者具备专业的机器人学知识。这使得非专业人士难以有效操控四足机器人，限制了其应用范围。现有方法难以实现自然语言指令到机器人运动规划的直接转换。

**核心思路**：本文的核心思路是利用大型语言模型（LLM）的强大自然语言理解和生成能力，将用户输入的自然语言指令转化为机器人可以理解和执行的运动规划。通过将计算密集型的LLM处理卸载到外部服务器，解决了四足机器人板载计算资源有限的问题。

**技术框架**：该系统采用分布式架构，主要包含以下几个模块：1) 自然语言指令输入模块；2) LLM指令处理模块（在外部服务器上运行），负责将自然语言指令转化为高层运动规划；3) 传感器融合模块，利用激光雷达、IMU和里程计数据进行环境感知和定位；4) ROS导航命令生成模块，将LLM生成的高层运动规划转化为可执行的ROS导航命令；5) 四足机器人运动控制模块，负责执行ROS导航命令，控制机器人运动。

**关键创新**：该方法最重要的创新点在于将大型语言模型应用于四足机器人的运动规划，实现了自然语言控制。与传统的基于规则或优化的运动规划方法相比，该方法更加灵活和易于使用。此外，通过将LLM处理卸载到外部服务器，解决了机器人板载计算资源有限的问题。

**关键设计**：论文中没有详细描述LLM的具体选择和训练细节，以及ROS导航命令生成的具体算法。传感器融合模块的具体实现方式也未详细说明。这些是未来研究可以深入探索的方向。论文提到了DeepRobotics Jueying Lite 3平台，但没有给出具体的参数设置。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.21293v1/images/fig.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.21293v1/x1.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.21293v1/images/website.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

实验结果表明，该系统在结构化室内环境中，针对四个不同的场景（从单房间任务到复杂的跨区域导航），总体成功率超过90％。这验证了基于卸载LLM的规划在现实环境中自主部署四足机器人的可行性，展示了其良好的鲁棒性和实用性。

## 🎯 应用场景

该研究成果可应用于搜救、巡检、物流等领域。通过自然语言控制，非专业人员也能轻松操控四足机器人完成复杂任务，降低了使用门槛。未来，该技术有望在家庭服务、医疗辅助等领域发挥重要作用，提升机器人的智能化水平和服务能力。

## 📄 摘要（原文）

> Traditional control interfaces for quadruped robots often impose a high barrier to entry, requiring specialized technical knowledge for effective operation. To address this, this paper presents a novel control framework that integrates Large Language Models (LLMs) to enable intuitive, natural language-based navigation. We propose a distributed architecture where high-level instruction processing is offloaded to an external server to overcome the onboard computational constraints of the DeepRobotics Jueying Lite 3 platform. The system grounds LLM-generated plans into executable ROS navigation commands using real-time sensor fusion (LiDAR, IMU, and Odometry). Experimental validation was conducted in a structured indoor environment across four distinct scenarios, ranging from single-room tasks to complex cross-zone navigation. The results demonstrate the system's robustness, achieving an aggregate success rate of over 90\% across all scenarios, validating the feasibility of offloaded LLM-based planning for autonomous quadruped deployment in real-world settings.

