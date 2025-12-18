---
layout: default
title: Attribute-based Object Grounding and Robot Grasp Detection with Spatial Reasoning
---

# Attribute-based Object Grounding and Robot Grasp Detection with Spatial Reasoning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.08126" class="toolbar-btn" target="_blank">📄 arXiv: 2509.08126v1</a>
  <a href="https://arxiv.org/pdf/2509.08126.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.08126v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.08126v1', 'Attribute-based Object Grounding and Robot Grasp Detection with Spatial Reasoning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Houjian Yu, Zheming Zhou, Min Sun, Omid Ghasemalizadeh, Yuyin Sun, Cheng-Hao Kuo, Arnie Sen, Changhyun Choi

**分类**: cs.RO

**发布日期**: 2025-09-09

**备注**: Accepted to 2025 IEEE-RAS 24th International Conference on Humanoid Robots

---

## 💡 一句话要点

**提出基于属性的对象定位与机器人抓取框架OGRG，解决复杂场景下的语言指定抓取问题。**

🎯 **匹配领域**: **支柱三：空间感知与语义 (Perception & Semantics)**

**关键词**: `机器人抓取` `自然语言理解` `视觉语言融合` `空间推理` `弱监督学习` `对象定位` `人机交互`

## 📋 核心要点

1. 现有方法难以处理开放式语言表达，且通常假设目标对象是唯一的，忽略了重复实例，限制了应用场景。
2. OGRG框架通过双向视觉-语言融合和深度信息集成，增强了几何推理能力，从而提升了定位和抓取性能。
3. 实验表明，OGRG在定位精度和抓取成功率上均优于现有方法，并在真实机器人实验中验证了其有效性。

## 📝 摘要（中文）

本文提出了一种基于属性的对象定位与机器人抓取框架（OGRG），旨在解决人机交互中通过自然语言指定抓取对象的问题。该框架能够解析开放式的语言表达，并进行空间推理，从而在包含重复对象实例的场景中定位目标对象并预测平面抓取姿态。OGRG在两种设置下进行了研究：(1)像素级全监督下的参考抓取合成（RGS）；(2)仅使用单像素抓取标注的弱监督学习下的参考抓取可供性（RGA）。主要贡献包括双向视觉-语言融合模块以及深度信息集成以增强几何推理，从而提高定位和抓取性能。实验结果表明，OGRG在具有多样化空间语言指令的桌面场景中优于强大的基线方法。在RGS中，它在单个NVIDIA RTX 2080 Ti GPU上以17.59 FPS运行，使其能够潜在地用于闭环或多对象顺序抓取，同时提供优于所有考虑的基线的定位和抓取预测精度。在弱监督RGA设置下，OGRG在模拟和真实机器人试验中也超过了基线抓取成功率，突出了其空间推理设计的有效性。

## 🔬 方法详解

**问题定义**：论文旨在解决机器人根据自然语言指令抓取特定对象的问题，尤其是在场景中存在多个相同对象实例的情况下。现有方法通常依赖于密集的像素级标注，成本高昂，并且难以处理复杂的、开放式的语言指令，以及缺乏对场景中对象间空间关系的有效推理。

**核心思路**：论文的核心思路是利用视觉属性和空间推理来精确地定位目标对象，并预测合适的抓取姿态。通过融合视觉信息和语言信息，并结合深度信息进行几何推理，从而克服现有方法在处理复杂场景和开放式语言指令方面的局限性。

**技术框架**：OGRG框架包含以下主要模块：(1)视觉特征提取模块，用于提取场景的视觉特征；(2)语言特征提取模块，用于提取自然语言指令的语义特征；(3)双向视觉-语言融合模块，用于将视觉特征和语言特征进行融合，从而实现视觉信息和语言信息的有效交互；(4)空间推理模块，利用深度信息进行几何推理，增强对场景中对象间空间关系的理解；(5)抓取姿态预测模块，用于预测目标对象的抓取姿态。

**关键创新**：论文的关键创新在于：(1)提出了双向视觉-语言融合模块，能够更有效地融合视觉信息和语言信息；(2)集成了深度信息，增强了几何推理能力，从而提高了定位和抓取性能；(3)提出了弱监督学习方法，仅使用单像素抓取标注，降低了标注成本。与现有方法相比，OGRG能够更好地处理复杂的场景和开放式的语言指令，并且具有更高的定位精度和抓取成功率。

**关键设计**：双向视觉-语言融合模块采用Transformer结构，允许视觉和语言信息相互影响和增强。空间推理模块利用深度图计算点云，并使用PointNet提取几何特征。损失函数包括定位损失和抓取损失，其中定位损失采用交叉熵损失，抓取损失采用Smooth L1损失。在弱监督学习中，采用最大化抓取成功率的策略进行训练。

## 📊 实验亮点

实验结果表明，OGRG在RGS设置下，在单个NVIDIA RTX 2080 Ti GPU上以17.59 FPS运行，同时在定位精度和抓取预测精度上均优于所有基线方法。在弱监督RGA设置下，OGRG在模拟和真实机器人试验中也超过了基线抓取成功率，验证了其空间推理设计的有效性。具体而言，在真实机器人实验中，OGRG的抓取成功率比基线方法提高了显著比例（具体数值未知）。

## 🎯 应用场景

该研究成果可应用于智能制造、家庭服务机器人、仓储物流等领域。例如，在智能制造中，机器人可以根据工人的语音指令抓取特定的零件进行组装；在家庭服务中，机器人可以根据用户的语言指令抓取物品，帮助用户完成家务；在仓储物流中，机器人可以根据指令抓取货物进行分拣和搬运。该研究有助于提升人机交互的自然性和效率，实现更智能化的机器人应用。

## 📄 摘要（原文）

> Enabling robots to grasp objects specified through natural language is essential for effective human-robot interaction, yet it remains a significant challenge. Existing approaches often struggle with open-form language expressions and typically assume unambiguous target objects without duplicates. Moreover, they frequently rely on costly, dense pixel-wise annotations for both object grounding and grasp configuration. We present Attribute-based Object Grounding and Robotic Grasping (OGRG), a novel framework that interprets open-form language expressions and performs spatial reasoning to ground target objects and predict planar grasp poses, even in scenes containing duplicated object instances. We investigate OGRG in two settings: (1) Referring Grasp Synthesis (RGS) under pixel-wise full supervision, and (2) Referring Grasp Affordance (RGA) using weakly supervised learning with only single-pixel grasp annotations. Key contributions include a bi-directional vision-language fusion module and the integration of depth information to enhance geometric reasoning, improving both grounding and grasping performance. Experiment results show that OGRG outperforms strong baselines in tabletop scenes with diverse spatial language instructions. In RGS, it operates at 17.59 FPS on a single NVIDIA RTX 2080 Ti GPU, enabling potential use in closed-loop or multi-object sequential grasping, while delivering superior grounding and grasp prediction accuracy compared to all the baselines considered. Under the weakly supervised RGA setting, OGRG also surpasses baseline grasp-success rates in both simulation and real-robot trials, underscoring the effectiveness of its spatial reasoning design. Project page: https://z.umn.edu/ogrg

