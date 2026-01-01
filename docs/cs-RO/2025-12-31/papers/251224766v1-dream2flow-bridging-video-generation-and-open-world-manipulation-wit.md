---
layout: default
title: "Dream2Flow: Bridging Video Generation and Open-World Manipulation with 3D Object Flow"
---

# Dream2Flow: Bridging Video Generation and Open-World Manipulation with 3D Object Flow

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.24766" class="toolbar-btn" target="_blank">📄 arXiv: 2512.24766v1</a>
  <a href="https://arxiv.org/pdf/2512.24766.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.24766v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.24766v1', 'Dream2Flow: Bridging Video Generation and Open-World Manipulation with 3D Object Flow')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Karthik Dharmarajan, Wenlong Huang, Jiajun Wu, Li Fei-Fei, Ruohan Zhang

**分类**: cs.RO, cs.AI, cs.CV

**发布日期**: 2025-12-31

**备注**: Project website: https://dream2flow.github.io/

**🔗 代码/项目**: [PROJECT_PAGE](https://dream2flow.github.io/)

---

## 💡 一句话要点

**Dream2Flow：利用3D物体流桥接视频生成与开放世界操作**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `视频生成` `机器人操作` `3D物体流` `零样本学习` `轨迹优化`

## 📋 核心要点

1. 现有方法难以将生成视频中的物体运动转化为机器人可执行的底层动作，存在“具身差距”。
2. Dream2Flow通过3D物体流作为中间表示，将视频生成与机器人控制连接，实现零样本操作指导。
3. 实验表明，Dream2Flow能够操作各种类型的物体，并通过轨迹优化或强化学习生成可执行的机器人指令。

## 📝 摘要（中文）

生成式视频建模已成为一种引人注目的工具，可以对开放世界操作中合理的物理交互进行零样本推理。然而，将这种人为引导的运动转化为机器人系统所需的底层动作仍然是一个挑战。我们观察到，给定初始图像和任务指令，这些模型擅长合成合理的物体运动。因此，我们引入了Dream2Flow，一个通过3D物体流作为中间表示来桥接视频生成和机器人控制的框架。我们的方法从生成的视频中重建3D物体运动，并将操作定义为物体轨迹跟踪。通过将状态变化与实现这些变化的执行器分离，Dream2Flow克服了具身差距，并实现了从预训练视频模型到操作各种类别物体的零样本指导，包括刚性、铰接、可变形和颗粒状物体。通过轨迹优化或强化学习，Dream2Flow将重建的3D物体流转换为可执行的底层命令，而无需特定于任务的演示。仿真和真实世界的实验突出了3D物体流作为一种通用且可扩展的接口，用于将视频生成模型适配到开放世界机器人操作。

## 🔬 方法详解

**问题定义**：现有生成式视频模型擅长生成物体运动，但难以直接控制机器人执行这些运动，因为视频模型输出的是高层语义信息，而机器人需要底层控制指令。这种从高层语义到低层控制的转换存在“具身差距”，阻碍了视频生成模型在机器人操作中的应用。

**核心思路**：Dream2Flow的核心思路是将视频生成模型生成的物体运动信息提取出来，用3D物体流来表示，然后将机器人操作任务转化为对3D物体轨迹的跟踪问题。通过这种方式，将高层语义的物体运动与底层控制指令解耦，从而克服“具身差距”。

**技术框架**：Dream2Flow框架包含以下几个主要步骤：1) 给定初始图像和任务指令，使用预训练的视频生成模型生成视频；2) 从生成的视频中重建3D物体运动，得到3D物体流；3) 将机器人操作任务定义为对3D物体轨迹的跟踪问题；4) 使用轨迹优化或强化学习方法，将3D物体流转换为可执行的底层机器人控制指令。

**关键创新**：Dream2Flow的关键创新在于使用3D物体流作为视频生成和机器人控制之间的中间表示。这种表示方式能够有效地提取视频中的物体运动信息，并将高层语义的物体运动与底层控制指令解耦，从而克服“具身差距”，实现零样本机器人操作。

**关键设计**：Dream2Flow的关键设计包括：1) 使用现有的视频生成模型，无需重新训练；2) 使用现有的3D重建算法从视频中重建3D物体运动；3) 使用轨迹优化或强化学习方法将3D物体流转换为可执行的机器人控制指令。具体使用的轨迹优化算法和强化学习算法可以根据具体任务进行选择。

## 📊 实验亮点

Dream2Flow在仿真和真实世界环境中进行了实验验证。实验结果表明，Dream2Flow能够成功地操作各种类型的物体，包括刚性、铰接、可变形和颗粒状物体。与现有的方法相比，Dream2Flow无需特定于任务的演示，即可实现零样本机器人操作，具有更好的泛化能力和可扩展性。

## 🎯 应用场景

Dream2Flow具有广泛的应用前景，例如家庭服务机器人、工业自动化、医疗机器人等。它可以使机器人能够理解人类的指令，并根据指令操作各种物体，从而提高机器人的智能化水平和应用范围。未来，Dream2Flow可以与其他技术结合，例如自然语言处理、计算机视觉等，实现更复杂的机器人操作任务。

## 📄 摘要（原文）

> Generative video modeling has emerged as a compelling tool to zero-shot reason about plausible physical interactions for open-world manipulation. Yet, it remains a challenge to translate such human-led motions into the low-level actions demanded by robotic systems. We observe that given an initial image and task instruction, these models excel at synthesizing sensible object motions. Thus, we introduce Dream2Flow, a framework that bridges video generation and robotic control through 3D object flow as an intermediate representation. Our method reconstructs 3D object motions from generated videos and formulates manipulation as object trajectory tracking. By separating the state changes from the actuators that realize those changes, Dream2Flow overcomes the embodiment gap and enables zero-shot guidance from pre-trained video models to manipulate objects of diverse categories-including rigid, articulated, deformable, and granular. Through trajectory optimization or reinforcement learning, Dream2Flow converts reconstructed 3D object flow into executable low-level commands without task-specific demonstrations. Simulation and real-world experiments highlight 3D object flow as a general and scalable interface for adapting video generation models to open-world robotic manipulation. Videos and visualizations are available at https://dream2flow.github.io/.

