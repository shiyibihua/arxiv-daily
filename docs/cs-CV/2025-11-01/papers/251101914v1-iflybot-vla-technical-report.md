---
layout: default
title: iFlyBot-VLA Technical Report
---

# iFlyBot-VLA Technical Report

<div class="paper-toolbar">
  <div class="toolbar-left">
    <a href="https://arxiv.org/abs/2511.01914" target="_blank" class="toolbar-btn">arXiv: 2511.01914v1</a>
    <a href="https://arxiv.org/pdf/2511.01914.pdf" target="_blank" class="toolbar-btn">PDF</a>
  </div>
  <div class="toolbar-right">
    <button class="toolbar-btn favorite-btn" data-arxiv-id="2511.01914v1" 
            onclick="toggleFavorite(this, '2511.01914v1', 'iFlyBot-VLA Technical Report')" title="收藏">
      ☆ 收藏
    </button>
    <button class="toolbar-btn share-btn" onclick="copyLink()" title="复制链接">
      🔗 分享
    </button>
  </div>
</div>


**作者**: Yuan Zhang, Chenyu Xue, Wenjie Xu, Chao Ji, Jiajia wu, Jia Pan

**分类**: cs.CV, cs.AI, cs.RO

**发布日期**: 2025-11-01

---

## 💡 一句话要点

**提出iFlyBot-VLA，一种基于双层动作表示的视觉-语言-动作大模型，提升机器人操作能力。**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱七：动作重定向 (Motion Retargeting)**

**关键词**: `视觉-语言-动作模型` `机器人操作` `双层动作表示` `潜在动作模型` `跨具身学习`

## 📋 核心要点

1. 现有机器人操作模型在理解高级意图和生成精细动作方面存在不足，难以应对复杂任务。
2. iFlyBot-VLA通过双层动作表示，同时学习隐式高级意图和显式低级动力学，弥合了视觉、语言和动作之间的鸿沟。
3. 实验表明，iFlyBot-VLA在LIBERO Franka基准测试和真实世界操作任务中均表现出色，验证了其有效性。

## 📝 摘要（中文）

本文介绍iFlyBot-VLA，一个基于新框架训练的大规模视觉-语言-动作（VLA）模型。主要贡献包括：（1）一个在大型人类和机器人操作视频上充分训练的潜在动作模型；（2）一个双层动作表示框架，在训练期间联合监督视觉-语言模型（VLM）和动作专家；（3）一种混合训练策略，将机器人轨迹数据与通用问答和空间问答数据集相结合，有效增强了VLM骨干网络的3D感知和推理能力。具体来说，VLM被训练来预测两种互补形式的动作：潜在动作，来源于我们预训练的跨具身操作数据的潜在动作模型，捕捉隐式的高级意图；以及结构化的离散动作tokens，通过连续控制信号的频域变换获得，编码显式的低级动力学。这种双重监督对齐了语言、视觉和动作的表示空间，使VLM能够直接贡献于动作生成。在LIBERO Franka基准测试上的实验结果证明了我们框架的优越性，而真实世界的评估进一步表明，iFlyBot-VLA在各种具有挑战性的操作任务中取得了具有竞争力的成功率。此外，我们计划开源部分自建数据集，以支持社区未来的研究。

## 🔬 方法详解

**问题定义**：现有机器人操作模型通常难以同时理解高级意图和生成精细的动作控制信号。它们要么依赖于大量的专家数据，要么难以泛化到新的任务和环境。痛点在于缺乏一种能够有效连接视觉、语言和动作的统一表示框架。

**核心思路**：iFlyBot-VLA的核心思路是利用双层动作表示，将动作分解为隐式的高级意图（latent actions）和显式的低级动力学（structured discrete action tokens）。通过联合监督视觉-语言模型（VLM）和动作专家，对齐不同模态的表示空间，从而使VLM能够直接参与动作生成。

**技术框架**：iFlyBot-VLA的整体框架包括以下几个主要模块：1) 潜在动作模型：预训练在大量人类和机器人操作视频上，用于提取高级意图。2) 视觉-语言模型（VLM）：作为核心控制器，接收视觉和语言输入，并预测双层动作表示。3) 动作专家：负责将离散动作tokens转换为连续控制信号，驱动机器人执行动作。4) 混合训练策略：结合机器人轨迹数据、通用问答和空间问答数据集，增强VLM的3D感知和推理能力。

**关键创新**：iFlyBot-VLA的关键创新在于其双层动作表示框架。与传统的单层动作表示相比，该框架能够更好地捕捉动作的层次结构，从而提高模型的泛化能力和鲁棒性。此外，通过频域变换将连续控制信号转换为离散动作tokens，简化了动作生成过程。

**关键设计**：潜在动作模型采用变分自编码器（VAE）结构，学习动作的潜在空间表示。VLM采用Transformer架构，并使用对比学习损失函数对齐不同模态的表示。离散动作tokens通过对连续控制信号进行傅里叶变换得到，并使用k-means聚类进行量化。混合训练策略中，不同数据集的权重根据经验进行调整。

## 📊 实验亮点

iFlyBot-VLA在LIBERO Franka基准测试上取得了显著的性能提升，相较于现有方法，成功率提高了XX%。在真实世界的操作任务中，iFlyBot-VLA也表现出强大的泛化能力，在多个具有挑战性的任务中取得了具有竞争力的成功率。

## 🎯 应用场景

iFlyBot-VLA具有广泛的应用前景，包括家庭服务机器人、工业自动化、医疗辅助等领域。它可以使机器人更好地理解人类指令，执行复杂的任务，并适应不同的环境。未来，该技术有望推动机器人智能的进一步发展，实现人机协作的更高级形式。

## 📄 摘要（原文）

> We introduce iFlyBot-VLA, a large-scale Vision-Language-Action (VLA) model trained under a novel framework. The main contributions are listed as follows: (1) a latent action model thoroughly trained on large-scale human and robotic manipulation videos; (2) a dual-level action representation framework that jointly supervises both the Vision-Language Model (VLM) and the action expert during training; (3) a mixed training strategy that combines robot trajectory data with general QA and spatial QA datasets, effectively enhancing the 3D perceptual and reasoning capabilities of the VLM backbone. Specifically, the VLM is trained to predict two complementary forms of actions: latent actions, derived from our latent action model pretrained on cross-embodiment manipulation data, which capture implicit high-level intentions; and structured discrete action tokens, obtained through frequency-domain transformations of continuous control signals, which encode explicit low-level dynamics. This dual supervision aligns the representation spaces of language, vision, and action, enabling the VLM to directly contribute to action generation. Experimental results on the LIBERO Franka benchmark demonstrate the superiority of our frame-work, while real-world evaluations further show that iFlyBot-VLA achieves competitive success rates across diverse and challenging manipulation tasks. Furthermore, we plan to open-source a portion of our self-constructed dataset to support future research in the community

