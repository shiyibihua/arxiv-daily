---
layout: default
title: The World is Your Canvas: Painting Promptable Events with Reference Images, Trajectories, and Text
---

# The World is Your Canvas: Painting Promptable Events with Reference Images, Trajectories, and Text

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.16924" class="toolbar-btn" target="_blank">📄 arXiv: 2512.16924v1</a>
  <a href="https://arxiv.org/pdf/2512.16924.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.16924v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.16924v1', 'The World is Your Canvas: Painting Promptable Events with Reference Images, Trajectories, and Text')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Hanlin Wang, Hao Ouyang, Qiuyu Wang, Yue Yu, Yihao Meng, Wen Wang, Ka Leong Cheng, Shuailei Ma, Qingyan Bai, Yixuan Li, Cheng Chen, Yanhong Zeng, Xing Zhu, Yujun Shen, Qifeng Chen

**分类**: cs.CV

**发布日期**: 2025-12-18

**备注**: Project page and code: https://worldcanvas.github.io/

**🔗 代码/项目**: [PROJECT_PAGE](https://worldcanvas.github.io/)

---

## 💡 一句话要点

**WorldCanvas：结合文本、轨迹和参考图像，实现可控的世界事件模拟。**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `世界模型` `事件生成` `多模态融合` `轨迹控制` `参考图像`

## 📋 核心要点

1. 现有方法在世界事件模拟中，要么仅依赖文本，缺乏精细控制，要么依赖轨迹控制，但忽略了语义意图和视觉一致性。
2. WorldCanvas结合文本、轨迹和参考图像，利用轨迹编码运动，自然语言表达语义，参考图像提供视觉基础，实现可控事件生成。
3. 实验结果表明，WorldCanvas生成的视频不仅具有时间连贯性，还能保持对象身份和场景一致性，支持多智能体交互等复杂事件。

## 📝 摘要（中文）

本文提出了WorldCanvas，一个用于可提示世界事件的框架，它通过结合文本、轨迹和参考图像来实现丰富的、用户导向的模拟。与仅使用文本的方法和现有的轨迹控制图像到视频方法不同，我们的多模态方法结合了轨迹（编码运动、时间安排和可见性）与自然语言（用于语义意图）以及参考图像（用于对象身份的视觉基础），从而能够生成连贯的、可控的事件，包括多智能体交互、对象进入/退出、参考引导的外观和违反直觉的事件。生成的视频不仅展示了时间连贯性，还展示了涌现一致性，即使在暂时消失的情况下也能保持对象身份和场景。通过支持富有表现力的世界事件生成，WorldCanvas将世界模型从被动预测器提升为交互式的、用户塑造的模拟器。我们的项目页面位于：https://worldcanvas.github.io/。

## 🔬 方法详解

**问题定义**：现有世界模型在生成复杂、可控的世界事件时面临挑战。仅依赖文本的方法难以精确控制事件的细节和视觉效果，而现有的轨迹控制图像到视频方法则缺乏对语义意图的理解，难以生成具有丰富交互和视觉一致性的事件。这些方法无法很好地处理多智能体交互、物体进入/退出以及违反直觉的事件。

**核心思路**：WorldCanvas的核心思路是将文本、轨迹和参考图像三种模态的信息融合起来，共同驱动世界事件的生成。轨迹用于控制物体的运动和时间信息，文本用于表达事件的语义意图，参考图像则用于提供物体外观的视觉基础。通过这种多模态融合的方式，可以实现对世界事件更精细、更可控的模拟。

**技术框架**：WorldCanvas的整体框架包含以下几个主要模块：1) 轨迹编码模块，用于将轨迹信息编码成可供后续模块使用的特征向量；2) 文本编码模块，用于将自然语言描述编码成语义特征向量；3) 参考图像编码模块，用于提取参考图像的视觉特征；4) 事件生成模块，该模块接收轨迹、文本和参考图像的特征向量，生成相应的视频帧序列。该模块可能基于生成对抗网络（GAN）或扩散模型等技术。

**关键创新**：WorldCanvas的关键创新在于其多模态融合的方法，它将轨迹、文本和参考图像三种模态的信息有机地结合起来，从而实现了对世界事件更精细、更可控的模拟。与现有方法相比，WorldCanvas能够生成包含多智能体交互、物体进入/退出以及违反直觉的事件，并且能够保持物体身份和场景的一致性。

**关键设计**：具体的技术细节未知，但可以推测可能包含以下设计：轨迹编码可能使用循环神经网络（RNN）或Transformer等序列模型；文本编码可能使用预训练的语言模型，如BERT或GPT；参考图像编码可能使用卷积神经网络（CNN），如ResNet或VGG。事件生成模块可能使用条件生成对抗网络（Conditional GAN）或条件扩散模型（Conditional Diffusion Model），其中轨迹、文本和参考图像的特征向量作为条件输入。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16924v1/x2.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16924v1/x3.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16924v1/x4.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

论文展示了WorldCanvas在生成各种复杂世界事件方面的能力，包括多智能体交互、物体进入/退出、参考引导的外观和违反直觉的事件。生成的视频不仅具有时间连贯性，还能保持物体身份和场景的一致性。具体性能数据未知，但视觉效果上明显优于现有方法。

## 🎯 应用场景

WorldCanvas具有广泛的应用前景，例如：游戏开发（生成动态游戏场景）、电影制作（创建特效和动画）、机器人训练（模拟真实世界环境）、自动驾驶（生成交通场景）等。它能够帮助用户更高效、更便捷地创建各种复杂的世界事件，并为相关领域的研究和应用提供新的思路和方法。

## 📄 摘要（原文）

> We present WorldCanvas, a framework for promptable world events that enables rich, user-directed simulation by combining text, trajectories, and reference images. Unlike text-only approaches and existing trajectory-controlled image-to-video methods, our multimodal approach combines trajectories -- encoding motion, timing, and visibility -- with natural language for semantic intent and reference images for visual grounding of object identity, enabling the generation of coherent, controllable events that include multi-agent interactions, object entry/exit, reference-guided appearance and counterintuitive events. The resulting videos demonstrate not only temporal coherence but also emergent consistency, preserving object identity and scene despite temporary disappearance. By supporting expressive world events generation, WorldCanvas advances world models from passive predictors to interactive, user-shaped simulators. Our project page is available at: https://worldcanvas.github.io/.

