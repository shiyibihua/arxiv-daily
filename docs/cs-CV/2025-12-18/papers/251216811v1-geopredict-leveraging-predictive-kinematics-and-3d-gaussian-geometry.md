---
layout: default
title: GeoPredict: Leveraging Predictive Kinematics and 3D Gaussian Geometry for Precise VLA Manipulation
---

# GeoPredict: Leveraging Predictive Kinematics and 3D Gaussian Geometry for Precise VLA Manipulation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.16811" class="toolbar-btn" target="_blank">📄 arXiv: 2512.16811v1</a>
  <a href="https://arxiv.org/pdf/2512.16811.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.16811v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.16811v1', 'GeoPredict: Leveraging Predictive Kinematics and 3D Gaussian Geometry for Precise VLA Manipulation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jingjing Qian, Boyao Han, Chen Shi, Lei Xiao, Long Yang, Shaoshuai Shi, Li Jiang

**分类**: cs.CV, cs.RO

**发布日期**: 2025-12-18

---

## 💡 一句话要点

**GeoPredict：利用预测运动学和3D高斯几何实现精确的VLA操作**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `视觉语言动作模型` `机器人操作` `3D几何推理` `运动学预测` `高斯几何` `深度渲染`

## 📋 核心要点

1. 现有VLA模型在精确3D推理任务中表现不足，缺乏对环境几何信息的有效利用。
2. GeoPredict通过预测机器人手臂的运动轨迹和工作空间几何形状，为VLA模型引入了几何先验。
3. 实验表明，GeoPredict在几何密集型和空间要求高的场景中，显著优于现有的VLA基线方法。

## 📝 摘要（中文）

视觉-语言-动作(VLA)模型在机器人操作中表现出强大的泛化能力，但很大程度上是反应式的和以2D为中心的，这使得它们在需要精确3D推理的任务中不可靠。我们提出了GeoPredict，一个几何感知的VLA框架，它用预测运动学和几何先验来增强连续动作策略。GeoPredict引入了一个轨迹级模块，该模块编码运动历史并预测机器人手臂的多步3D关键点轨迹，以及一个预测性3D高斯几何模块，该模块预测工作空间几何形状，并通过沿未来关键点轨迹的跟踪引导细化。这些预测模块仅作为训练时的监督，通过基于深度的渲染实现，而推理只需要轻量级的额外查询token，无需调用任何3D解码。在RoboCasa Human-50、LIBERO和真实世界操作任务上的实验表明，GeoPredict始终优于强大的VLA基线，尤其是在几何密集型和空间要求高的场景中。

## 🔬 方法详解

**问题定义**：现有的视觉-语言-动作(VLA)模型在机器人操作任务中，尤其是在需要精确3D推理的场景下，存在不足。它们通常是反应式的，并且主要依赖于2D视觉信息，缺乏对机器人运动学和环境几何信息的有效利用，导致操作精度不高。

**核心思路**：GeoPredict的核心思路是在训练阶段引入预测性的运动学和几何先验知识，从而提升VLA模型对3D环境的理解和操作能力。通过预测机器人手臂的关键点轨迹以及工作空间的3D几何形状，为模型提供更丰富的上下文信息，指导其生成更精确的动作。

**技术框架**：GeoPredict框架包含一个轨迹级模块和一个预测性3D高斯几何模块。轨迹级模块负责编码机器人手臂的运动历史，并预测未来多步的关键点轨迹。预测性3D高斯几何模块则预测工作空间的几何形状，并根据预测的关键点轨迹进行细化。这两个模块在训练阶段通过深度渲染提供监督信号，而在推理阶段仅需少量额外的查询token，无需进行复杂的3D解码。

**关键创新**：GeoPredict的关键创新在于将预测性的运动学和几何先验知识融入到VLA模型的训练过程中。通过预测未来轨迹和几何形状，模型能够更好地理解3D环境，从而生成更精确的动作。此外，该方法在推理阶段避免了复杂的3D解码，保持了模型的轻量级和高效性。

**关键设计**：GeoPredict使用深度渲染技术将预测的3D关键点轨迹和几何形状转化为深度图，作为训练的监督信号。轨迹级模块可能采用循环神经网络（RNN）或Transformer等结构来编码运动历史并预测未来轨迹。预测性3D高斯几何模块可能使用高斯混合模型或其他概率模型来表示工作空间的几何形状。损失函数的设计需要考虑轨迹预测的准确性和几何形状预测的逼真度。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16811v1/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16811v1/x2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16811v1/x3.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

GeoPredict在RoboCasa Human-50、LIBERO和真实世界操作任务上进行了评估，实验结果表明，GeoPredict始终优于强大的VLA基线。尤其是在几何密集型和空间要求高的场景中，GeoPredict的性能提升更为显著，证明了其在精确3D操作方面的优势。

## 🎯 应用场景

GeoPredict具有广泛的应用前景，可用于提升机器人操作的精度和可靠性，尤其是在需要精细操作和复杂环境理解的场景中，例如：医疗手术机器人、精密装配、家庭服务机器人等。该研究有助于推动机器人技术在更广泛领域的应用，并提高机器人的智能化水平。

## 📄 摘要（原文）

> Vision-Language-Action (VLA) models achieve strong generalization in robotic manipulation but remain largely reactive and 2D-centric, making them unreliable in tasks that require precise 3D reasoning. We propose GeoPredict, a geometry-aware VLA framework that augments a continuous-action policy with predictive kinematic and geometric priors. GeoPredict introduces a trajectory-level module that encodes motion history and predicts multi-step 3D keypoint trajectories of robot arms, and a predictive 3D Gaussian geometry module that forecasts workspace geometry with track-guided refinement along future keypoint trajectories. These predictive modules serve exclusively as training-time supervision through depth-based rendering, while inference requires only lightweight additional query tokens without invoking any 3D decoding. Experiments on RoboCasa Human-50, LIBERO, and real-world manipulation tasks show that GeoPredict consistently outperforms strong VLA baselines, especially in geometry-intensive and spatially demanding scenarios.

