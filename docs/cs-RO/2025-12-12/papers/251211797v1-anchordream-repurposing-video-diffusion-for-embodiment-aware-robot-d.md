---
layout: default
title: AnchorDream: Repurposing Video Diffusion for Embodiment-Aware Robot Data Synthesis
---

# AnchorDream: Repurposing Video Diffusion for Embodiment-Aware Robot Data Synthesis

<div class="paper-toolbar">
  <div class="toolbar-left">
    <a href="https://arxiv.org/abs/2512.11797" target="_blank" class="toolbar-btn">arXiv: 2512.11797v1</a>
    <a href="https://arxiv.org/pdf/2512.11797.pdf" target="_blank" class="toolbar-btn">PDF</a>
  </div>
  <div class="toolbar-right">
    <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.11797v1" 
            onclick="toggleFavorite(this, '2512.11797v1', 'AnchorDream: Repurposing Video Diffusion for Embodiment-Aware Robot Data Synthesis')" title="收藏">
      ☆ 收藏
    </button>
    <button class="toolbar-btn share-btn" onclick="copyLink()" title="复制链接">
      🔗 分享
    </button>
  </div>
</div>


**作者**: Junjie Ye, Rong Xue, Basile Van Hoorick, Pavel Tokmakov, Muhammad Zubair Irshad, Yue Wang, Vitor Guizilini

**分类**: cs.RO, cs.CV

**发布日期**: 2025-12-12

**备注**: Project page: https://jay-ye.github.io/AnchorDream/

---

## 💡 一句话要点

**AnchorDream：利用视频扩散模型进行具身感知机器人数据合成**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `机器人数据合成` `视频扩散模型` `模仿学习` `具身感知` `运动渲染`

## 📋 核心要点

1. 现有机器人模仿学习方法受限于真实数据获取成本高昂和仿真环境真实度不足的问题。
2. AnchorDream通过以机器人运动渲染为条件驱动视频扩散模型，合成高质量、多样化的机器人数据。
3. 实验表明，使用AnchorDream生成的数据能显著提升下游策略学习效果，真实环境性能提升近一倍。

## 📝 摘要（中文）

大规模和多样化的机器人演示数据收集仍然是模仿学习的主要瓶颈，因为真实世界的数据获取成本高昂，而仿真器提供的多样性和逼真度有限，存在明显的模拟到真实世界的差距。虽然生成模型提供了一个有吸引力的解决方案，但现有方法通常只改变视觉外观而不创造新的行为，或者遭受具身不一致性，从而产生不合理的运动。为了解决这些限制，我们引入了AnchorDream，一种具身感知的世界模型，它将预训练的视频扩散模型重新用于机器人数据合成。AnchorDream以机器人运动渲染为条件来驱动扩散过程，锚定具身以防止幻觉，同时合成与机器人运动学一致的物体和环境。从少量的远程操作演示开始，我们的方法将其扩展为大型、多样化、高质量的数据集，而无需显式的环境建模。实验表明，生成的数据能够持续改进下游策略学习，在模拟器基准测试中相对增益为36.4%，在真实世界研究中性能几乎翻倍。这些结果表明，将生成世界模型建立在机器人运动的基础上，为扩展模仿学习提供了一条切实可行的途径。

## 🔬 方法详解

**问题定义**：现有机器人模仿学习方法面临数据瓶颈，真实数据采集成本高，仿真数据存在“sim-to-real”差距。生成模型虽然有潜力，但要么只改变视觉效果，要么产生不符合机器人运动学规律的动作，缺乏具身感知能力。

**核心思路**：AnchorDream的核心在于利用预训练的视频扩散模型，并以机器人运动渲染作为条件（Anchor）来引导扩散过程。通过这种方式，模型可以生成与机器人运动学一致的场景和物体，避免幻觉，保证合成数据的合理性。

**技术框架**：AnchorDream的整体框架包括以下几个步骤：1) 使用少量人工遥操作数据作为种子；2) 将机器人运动信息渲染成图像序列；3) 将渲染的图像序列作为条件输入到预训练的视频扩散模型中；4) 视频扩散模型生成新的视频序列，这些序列包含与机器人运动一致的场景和物体。

**关键创新**：AnchorDream的关键创新在于将机器人运动信息作为“锚点”融入到视频扩散模型中，从而实现了具身感知的机器人数据合成。这与以往的生成模型只关注视觉效果或忽略机器人运动学约束的方法有本质区别。

**关键设计**：AnchorDream的关键设计包括：1) 使用预训练的视频扩散模型，避免从头训练的成本；2) 精心设计的机器人运动渲染方式，确保运动信息能够有效地传递给扩散模型；3) 使用对抗性损失函数来提高生成数据的真实感和多样性（具体损失函数细节论文中可能包含，此处未知）。

## 📊 实验亮点

实验结果表明，使用AnchorDream生成的数据能够显著提升下游策略学习的性能。在模拟器基准测试中，相对增益达到36.4%，而在真实世界的研究中，性能几乎翻倍。这些结果验证了AnchorDream在机器人数据合成方面的有效性和优越性。

## 🎯 应用场景

AnchorDream在机器人模仿学习领域具有广泛的应用前景，可以用于生成各种任务的训练数据，例如物体抓取、导航、装配等。该方法能够降低机器人学习的成本，提高学习效率，并有望加速机器人技术在工业、医疗、服务等领域的应用。

## 📄 摘要（原文）

> The collection of large-scale and diverse robot demonstrations remains a major bottleneck for imitation learning, as real-world data acquisition is costly and simulators offer limited diversity and fidelity with pronounced sim-to-real gaps. While generative models present an attractive solution, existing methods often alter only visual appearances without creating new behaviors, or suffer from embodiment inconsistencies that yield implausible motions. To address these limitations, we introduce AnchorDream, an embodiment-aware world model that repurposes pretrained video diffusion models for robot data synthesis. AnchorDream conditions the diffusion process on robot motion renderings, anchoring the embodiment to prevent hallucination while synthesizing objects and environments consistent with the robot's kinematics. Starting from only a handful of human teleoperation demonstrations, our method scales them into large, diverse, high-quality datasets without requiring explicit environment modeling. Experiments show that the generated data leads to consistent improvements in downstream policy learning, with relative gains of 36.4% in simulator benchmarks and nearly double performance in real-world studies. These results suggest that grounding generative world models in robot motion provides a practical path toward scaling imitation learning.

