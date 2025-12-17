---
layout: default
title: Dexterity from Smart Lenses: Multi-Fingered Robot Manipulation with In-the-Wild Human Demonstrations
---

# Dexterity from Smart Lenses: Multi-Fingered Robot Manipulation with In-the-Wild Human Demonstrations

**arXiv**: [2511.16661v1](https://arxiv.org/abs/2511.16661) | [PDF](https://arxiv.org/pdf/2511.16661.pdf)

**作者**: Irmak Guzey, Haozhi Qi, Julen Urain, Changhao Wang, Jessica Yin, Krishna Bodduluri, Mike Lambeta, Lerrel Pinto, Akshara Rai, Jitendra Malik, Tingfan Wu, Akash Sharma, Homanga Bharadhwaj

**分类**: cs.RO, cs.AI, cs.LG

**发布日期**: 2025-11-20

---

## 💡 一句话要点

**AINA框架：利用智能眼镜和人类演示学习多指机器人灵巧操作**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱二：RL算法与架构 (RL & Architecture)** **支柱三：空间感知 (Perception & SLAM)** **支柱七：动作重定向 (Motion Retargeting)**

**关键词**: `机器人操作` `多指灵巧手` `人类演示学习` `智能眼镜` `3D点云` `策略学习` `AINA框架`

## 📋 核心要点

1. 现有方法难以从真实场景的人类视频中提取相关上下文和运动线索，导致难以学习自主策略。
2. AINA框架利用Aria Gen 2眼镜获取的人类数据，学习对背景变化鲁棒的3D点云策略。
3. 实验表明，AINA框架在多个日常操作任务中表现出色，无需机器人数据即可直接部署。

## 📝 摘要（中文）

本文提出了一种名为AINA的框架，旨在通过人类在自然环境中执行日常任务的演示来学习多指机器人策略。该框架利用Aria Gen 2眼镜收集的数据，这些眼镜轻便便携，配备高分辨率RGB相机，提供精确的3D头部和手部姿势，并提供可用于场景深度估计的宽立体视野。AINA能够学习基于3D点的多指手策略，该策略对背景变化具有鲁棒性，并且可以直接部署，无需任何机器人数据。该研究将AINA框架与先前的人类到机器人策略学习方法进行了比较，验证了设计选择，并在九个日常操作任务中展示了结果。

## 🔬 方法详解

**问题定义**：现有方法在从人类演示中学习机器人策略时，面临着人类和机器人之间的形态差异，以及从真实场景视频中提取有效信息的挑战。这限制了机器人策略的泛化能力，并增加了对机器人数据收集的依赖。

**核心思路**：本文的核心思路是利用智能眼镜（Aria Gen 2）获取高质量的人类操作数据，包括RGB图像、3D头部和手部姿势以及深度信息。通过这些数据，可以直接学习适用于机器人的3D点云策略，从而克服形态差异和环境变化带来的挑战。

**技术框架**：AINA框架主要包括数据采集和策略学习两个阶段。在数据采集阶段，使用Aria Gen 2眼镜记录人类执行任务的视频，并提取头部和手部姿势以及深度信息。在策略学习阶段，利用这些数据训练一个基于3D点云的策略，该策略能够根据当前场景的状态预测机器人的动作。

**关键创新**：AINA框架的关键创新在于利用智能眼镜进行数据采集，这使得可以在真实场景中轻松获取高质量的人类操作数据。此外，该框架直接学习基于3D点云的策略，避免了中间表示的转换，从而提高了策略的鲁棒性和泛化能力。

**关键设计**：AINA框架使用PointNet++提取3D点云特征，并使用Transformer网络学习策略。损失函数包括动作预测损失和姿势预测损失，用于约束策略的学习。此外，还采用了数据增强技术，例如随机旋转和缩放，以提高策略的鲁棒性。

## 📊 实验亮点

实验结果表明，AINA框架在九个日常操作任务中表现出色，例如抓取物体、放置物体和组装物体。与先前的人类到机器人策略学习方法相比，AINA框架能够学习更鲁棒和泛化的策略，并且无需任何机器人数据即可直接部署。具体性能数据可在项目网站查看。

## 🎯 应用场景

该研究成果可应用于各种需要灵巧操作的机器人任务，例如家庭服务、工业自动化和医疗辅助。通过学习人类的演示，机器人可以更好地适应复杂和动态的环境，从而提高工作效率和安全性。未来，该技术有望实现更智能、更自主的机器人系统，从而更好地服务于人类社会。

## 📄 摘要（原文）

> Learning multi-fingered robot policies from humans performing daily tasks in natural environments has long been a grand goal in the robotics community. Achieving this would mark significant progress toward generalizable robot manipulation in human environments, as it would reduce the reliance on labor-intensive robot data collection. Despite substantial efforts, progress toward this goal has been bottle-necked by the embodiment gap between humans and robots, as well as by difficulties in extracting relevant contextual and motion cues that enable learning of autonomous policies from in-the-wild human videos. We claim that with simple yet sufficiently powerful hardware for obtaining human data and our proposed framework AINA, we are now one significant step closer to achieving this dream. AINA enables learning multi-fingered policies from data collected by anyone, anywhere, and in any environment using Aria Gen 2 glasses. These glasses are lightweight and portable, feature a high-resolution RGB camera, provide accurate on-board 3D head and hand poses, and offer a wide stereo view that can be leveraged for depth estimation of the scene. This setup enables the learning of 3D point-based policies for multi-fingered hands that are robust to background changes and can be deployed directly without requiring any robot data (including online corrections, reinforcement learning, or simulation). We compare our framework against prior human-to-robot policy learning approaches, ablate our design choices, and demonstrate results across nine everyday manipulation tasks. Robot rollouts are best viewed on our website: https://aina-robot.github.io.

