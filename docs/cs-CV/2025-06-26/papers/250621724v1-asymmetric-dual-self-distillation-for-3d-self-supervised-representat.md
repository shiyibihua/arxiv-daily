---
layout: default
title: Asymmetric Dual Self-Distillation for 3D Self-Supervised Representation Learning
---

# Asymmetric Dual Self-Distillation for 3D Self-Supervised Representation Learning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.21724" class="toolbar-btn" target="_blank">📄 arXiv: 2506.21724v1</a>
  <a href="https://arxiv.org/pdf/2506.21724.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.21724v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.21724v1', 'Asymmetric Dual Self-Distillation for 3D Self-Supervised Representation Learning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Remco F. Leijenaar, Hamidreza Kasaei

**分类**: cs.CV

**发布日期**: 2025-06-26

**备注**: for associated source code, see https://github.com/RFLeijenaar/AsymDSD

---

## 💡 一句话要点

**提出不对称双重自蒸馏框架以解决3D自监督表示学习问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `3D表示学习` `自监督学习` `蒸馏训练` `点云处理` `深度学习`

## 📋 核心要点

1. 现有的自监督3D学习方法在捕捉高层语义时受到重建目标的限制，尤其是在缺乏标注数据的情况下。
2. 论文提出的AsymDSD框架通过在潜在空间进行预测，结合掩蔽建模和不变性学习，克服了现有方法的不足。
3. AsymDSD在ScanObjectNN数据集上取得了90.53%的准确率，经过930k形状的预训练后进一步提升至93.72%，显著优于以往方法。

## 📝 摘要（中文）

从无结构的3D点云中学习语义丰富的表示仍然是计算机视觉中的一个核心挑战，尤其是在缺乏大规模标注数据集的情况下。尽管掩蔽点建模（MPM）在自监督3D学习中被广泛使用，但其基于重建的目标可能限制了其捕捉高层语义的能力。我们提出了AsymDSD，一个不对称双重自蒸馏框架，通过在潜在空间而非输入空间进行预测，统一了掩蔽建模和不变性学习。AsymDSD基于联合嵌入架构，并引入了几个关键设计选择：高效的不对称设置、禁用掩蔽查询之间的注意力以防止形状泄漏、多掩蔽采样以及点云的多裁剪适配。AsymDSD在ScanObjectNN上达到了90.53%的最新结果，并在930k形状的预训练下进一步提升至93.72%，超越了之前的方法。

## 🔬 方法详解

**问题定义**：本论文旨在解决从无结构3D点云中学习语义表示的挑战。现有方法如掩蔽点建模（MPM）在重建目标上存在局限，难以有效捕捉高层语义信息。

**核心思路**：论文提出的AsymDSD框架通过在潜在空间进行预测，结合掩蔽建模与不变性学习，旨在提升语义表示的质量和有效性。这样的设计使得模型能够更好地理解和捕捉3D形状的语义特征。

**技术框架**：AsymDSD采用联合嵌入架构，主要模块包括不对称设置、掩蔽查询之间的注意力禁用、多掩蔽采样和点云的多裁剪适配。这些模块共同作用，提升了模型的学习能力。

**关键创新**：AsymDSD的核心创新在于其不对称双重自蒸馏机制，通过在潜在空间进行预测而非输入空间，显著提高了模型对高层语义的捕捉能力。这一设计与传统的重建目标方法形成了本质区别。

**关键设计**：在设计中，AsymDSD采用了高效的不对称设置，禁用了掩蔽查询之间的注意力以防止形状信息泄漏，同时引入了多掩蔽采样和多裁剪适配技术，以增强模型的鲁棒性和适应性。具体的损失函数和网络结构细节在论文中进行了详细描述。

## 📊 实验亮点

AsymDSD在ScanObjectNN数据集上取得了90.53%的准确率，并在930k形状的预训练后进一步提升至93.72%。这一结果显著超越了之前的方法，展示了其在3D自监督表示学习中的优越性能。

## 🎯 应用场景

该研究的潜在应用领域包括自动驾驶、机器人导航和虚拟现实等场景，能够帮助系统更好地理解和处理3D环境中的信息。通过提升3D表示学习的效果，未来可能推动相关技术在智能城市、增强现实等领域的广泛应用，具有重要的实际价值。

## 📄 摘要（原文）

> Learning semantically meaningful representations from unstructured 3D point clouds remains a central challenge in computer vision, especially in the absence of large-scale labeled datasets. While masked point modeling (MPM) is widely used in self-supervised 3D learning, its reconstruction-based objective can limit its ability to capture high-level semantics. We propose AsymDSD, an Asymmetric Dual Self-Distillation framework that unifies masked modeling and invariance learning through prediction in the latent space rather than the input space. AsymDSD builds on a joint embedding architecture and introduces several key design choices: an efficient asymmetric setup, disabling attention between masked queries to prevent shape leakage, multi-mask sampling, and a point cloud adaptation of multi-crop. AsymDSD achieves state-of-the-art results on ScanObjectNN (90.53%) and further improves to 93.72% when pretrained on 930k shapes, surpassing prior methods.

