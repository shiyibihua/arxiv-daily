---
layout: default
title: LISN: Language-Instructed Social Navigation with VLM-based Controller Modulating
---

# LISN: Language-Instructed Social Navigation with VLM-based Controller Modulating

<div class="paper-toolbar">
  <div class="toolbar-left">
    <a href="https://arxiv.org/abs/2512.09920" target="_blank" class="toolbar-btn">arXiv: 2512.09920v1</a>
    <a href="https://arxiv.org/pdf/2512.09920.pdf" target="_blank" class="toolbar-btn">PDF</a>
  </div>
  <div class="toolbar-right">
    <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.09920v1" 
            onclick="toggleFavorite(this, '2512.09920v1', 'LISN: Language-Instructed Social Navigation with VLM-based Controller Modulating')" title="收藏">
      ☆ 收藏
    </button>
    <button class="toolbar-btn share-btn" onclick="copyLink()" title="复制链接">
      🔗 分享
    </button>
  </div>
</div>


**作者**: Junting Chen, Yunchuan Li, Panfeng Jiang, Jiacheng Du, Zixuan Chen, Chenrui Tie, Jiajun Deng, Lin Shao

**分类**: cs.RO, cs.AI, cs.CV

**发布日期**: 2025-12-10

**备注**: 8 pages

**🔗 代码/项目**: [PROJECT_PAGE](https://social-nav.github.io/LISN-project/)

---

## 💡 一句话要点

**提出LISN-Bench与Social-Nav-Modulator，实现基于语言指令的社交导航。**

🎯 **匹配领域**: **支柱三：空间感知 (Perception & SLAM)**

**关键词**: `社交导航` `语言指令` `视觉语言模型` `机器人控制` `人机交互`

## 📋 核心要点

1. 现有社交导航方法主要关注路径效率和避撞，忽略了机器人理解并执行人类语言指令的能力。
2. 论文提出Social-Nav-Modulator，利用视觉语言模型（VLM）调节代价地图和控制器参数，实现语言指导下的社交导航。
3. 实验表明，该方法在语言指导的社交导航任务中显著优于现有方法，尤其在复杂场景下提升明显。

## 📝 摘要（中文）

本文提出了一种基于语言指令的社交导航方法，旨在实现人机共存。现有社交导航研究主要关注路径效率和行人避撞，但忽略了机器人遵循用户指令、符合任务目标和社交规范的能力。为此，本文构建了LISN-Bench，这是一个基于Rosnav-Arena 3.0的模拟基准，首次将指令跟随和场景理解融入到社交导航中。此外，本文提出了Social-Nav-Modulator，这是一个快-慢分层系统，其中VLM智能体调节代价地图和控制器参数。这种解耦降低了对高频VLM推理的依赖，同时提高了动态避障和感知适应性。实验结果表明，该方法平均成功率为91.3%，比最具竞争力的基线高出63%，尤其在人群跟随和避开禁行区域等挑战性任务中表现突出。

## 🔬 方法详解

**问题定义**：现有社交导航方法主要关注路径效率和行人避撞，缺乏对人类指令的理解和执行能力。这导致机器人在复杂社交环境中难以与人类自然交互，无法完成需要理解人类意图的任务。现有方法的痛点在于缺乏有效的机制将语言信息融入到导航决策中。

**核心思路**：论文的核心思路是利用视觉语言模型（VLM）的强大语义理解能力，将人类的语言指令转化为机器人可以理解的代价地图和控制器参数。通过VLM对环境和指令进行理解，动态调整机器人的行为，使其能够更好地遵循指令并符合社交规范。

**技术框架**：Social-Nav-Modulator采用快-慢分层系统。慢速VLM环路负责处理语言指令和场景理解，生成代价地图和控制器参数的调制信息。快速底层控制环路则根据调制后的参数进行实时的路径规划和运动控制。这种分层结构降低了对VLM推理频率的要求，提高了系统的实时性和鲁棒性。整体流程为：接收语言指令 -> VLM理解指令和场景 -> 生成调制信息 -> 调制代价地图和控制器参数 -> 底层控制器执行导航。

**关键创新**：最重要的技术创新点在于将VLM引入到社交导航中，并设计了一种有效的调制机制，将VLM的语义理解能力转化为机器人的导航行为。与现有方法相比，该方法能够更好地理解和执行人类指令，从而实现更自然、更符合社交规范的导航。

**关键设计**：VLM使用预训练的视觉语言模型，例如CLIP或类似模型。代价地图的调制方式可以是直接修改代价地图的值，也可以是调整代价函数的权重。控制器参数的调制可以包括速度、加速度、避障距离等参数。损失函数的设计需要考虑指令的完成度、路径的效率以及社交规范的遵守程度。具体参数设置和网络结构在论文中可能包含更多细节，但摘要中未明确指出。

## 📊 实验亮点

实验结果表明，Social-Nav-Modulator在LISN-Bench上的平均成功率达到91.3%，比最具竞争力的基线高出63%。尤其是在人群跟随和避开禁行区域等挑战性任务中，性能提升更为显著。这表明该方法能够有效地理解和执行人类指令，并在复杂社交环境中实现更可靠的导航。

## 🎯 应用场景

该研究成果可应用于服务机器人、自动驾驶、智能家居等领域。例如，服务机器人可以在商场或医院等复杂环境中，根据用户的语言指令引导用户到达指定地点，并避开禁行区域。自动驾驶汽车可以根据乘客的指令选择行驶路线，并遵守交通规则和社交规范。智能家居系统可以根据用户的语音指令控制机器人的行为，例如让机器人清理特定区域或跟随用户移动。

## 📄 摘要（原文）

> Towards human-robot coexistence, socially aware navigation is significant for mobile robots. Yet existing studies on this area focus mainly on path efficiency and pedestrian collision avoidance, which are essential but represent only a fraction of social navigation. Beyond these basics, robots must also comply with user instructions, aligning their actions to task goals and social norms expressed by humans. In this work, we present LISN-Bench, the first simulation-based benchmark for language-instructed social navigation. Built on Rosnav-Arena 3.0, it is the first standardized social navigation benchmark to incorporate instruction following and scene understanding across diverse contexts. To address this task, we further propose Social-Nav-Modulator, a fast-slow hierarchical system where a VLM agent modulates costmaps and controller parameters. Decoupling low-level action generation from the slower VLM loop reduces reliance on high-frequency VLM inference while improving dynamic avoidance and perception adaptability. Our method achieves an average success rate of 91.3%, which is greater than 63% than the most competitive baseline, with most of the improvements observed in challenging tasks such as following a person in a crowd and navigating while strictly avoiding instruction-forbidden regions. The project website is at: https://social-nav.github.io/LISN-project/

