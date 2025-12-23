---
layout: default
title: Self-supervised Learning of Echocardiographic Video Representations via Online Cluster Distillation
---

# Self-supervised Learning of Echocardiographic Video Representations via Online Cluster Distillation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.11777" class="toolbar-btn" target="_blank">📄 arXiv: 2506.11777v2</a>
  <a href="https://arxiv.org/pdf/2506.11777.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.11777v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.11777v2', 'Self-supervised Learning of Echocardiographic Video Representations via Online Cluster Distillation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Divyanshu Mishra, Mohammadreza Salehi, Pramit Saha, Olga Patey, Aris T. Papageorghiou, Yuki M. Asano, J. Alison Noble

**分类**: cs.CV, cs.AI, cs.CY, cs.LG

**发布日期**: 2025-06-13 (更新: 2025-11-14)

**🔗 代码/项目**: [GITHUB](https://github.com/mdivyanshu97/DISCOVR)

---

## 💡 一句话要点

**提出DISCOVR以解决心脏超声视频表示学习问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `自监督学习` `心脏超声` `视频表示学习` `聚类编码器` `蒸馏训练` `细粒度特征` `临床应用` `多模态学习`

## 📋 核心要点

1. 现有自监督学习方法在心脏超声领域面临高样本间相似性和低PSNR输入的挑战，导致性能受限。
2. 论文提出了DISCOVR框架，通过聚类视频编码器和在线图像编码器的结合，提升超声视频的表示学习能力。
3. 在六个心脏超声数据集上，DISCOVR在零样本和线性探测设置中超越了现有方法，表现出色。

## 📝 摘要（中文）

自监督学习（SSL）在自然图像和视频理解方面取得了重大进展，但在心脏超声等领域仍面临挑战，主要由于细微的解剖结构、复杂的时间动态以及缺乏领域特定的预训练模型。现有的SSL方法在高样本间相似性、对低PSNR输入的敏感性以及过度增强导致的临床相关特征失真方面表现不佳。本文提出了DISCOVR（跨模态视频表示的蒸馏图像监督），一个自监督的双分支框架，用于心脏超声视频表示学习。DISCOVR结合了一个基于聚类的视频编码器和一个在线图像编码器，通过语义聚类蒸馏损失将解剖知识从图像编码器转移到视频编码器，从而实现时序一致的表示，增强了细粒度的语义理解。经过在六个涵盖胎儿、儿童和成人群体的心脏超声数据集上的评估，DISCOVR在零样本和线性探测设置中超越了专门的视频异常检测方法和最先进的视频SSL基线，取得了优越的分割迁移和强大的下游任务表现，如LVEF预测。

## 🔬 方法详解

**问题定义**：本文旨在解决心脏超声视频表示学习中的自监督学习挑战，现有方法在处理高样本间相似性和低PSNR输入时效果不佳，且缺乏领域特定的预训练模型。

**核心思路**：论文提出的DISCOVR框架通过结合聚类视频编码器和在线图像编码器，利用语义聚类蒸馏损失将解剖知识从图像编码器转移到视频编码器，从而实现更好的时序一致性和细粒度语义理解。

**技术框架**：DISCOVR框架包括两个主要模块：聚类视频编码器和在线图像编码器。视频编码器负责建模时间动态，而图像编码器则提取细粒度空间语义。两个编码器通过蒸馏损失连接，形成一个自监督学习的闭环。

**关键创新**：DISCOVR的核心创新在于其双分支结构和语义聚类蒸馏损失，这使得视频编码器能够有效吸收图像编码器的解剖知识，从而克服了现有方法在超声视频表示学习中的局限性。

**关键设计**：在设计中，聚类视频编码器采用了时间序列建模技术，而在线图像编码器则使用了细粒度特征提取方法。蒸馏损失的设计确保了知识的有效转移，增强了模型的整体性能。具体参数设置和网络结构细节在论文中有详细描述。

## 📊 实验亮点

在六个心脏超声数据集的评估中，DISCOVR在零样本和线性探测设置中超越了专门的视频异常检测方法和最先进的视频SSL基线，表现出色，尤其在LVEF预测任务中取得了显著的性能提升。

## 🎯 应用场景

该研究的潜在应用领域包括心脏病学中的超声影像分析、临床决策支持系统以及医疗影像自动化处理。通过提升心脏超声视频的表示学习能力，DISCOVR有助于提高疾病诊断的准确性和效率，未来可能在临床实践中发挥重要作用。

## 📄 摘要（原文）

> Self-supervised learning (SSL) has achieved major advances in natural images and video understanding, but challenges remain in domains like echocardiography (heart ultrasound) due to subtle anatomical structures, complex temporal dynamics, and the current lack of domain-specific pre-trained models. Existing SSL approaches such as contrastive, masked modeling, and clustering-based methods struggle with high intersample similarity, sensitivity to low PSNR inputs common in ultrasound, or aggressive augmentations that distort clinically relevant features. We present DISCOVR (Distilled Image Supervision for Cross Modal Video Representation), a self-supervised dual branch framework for cardiac ultrasound video representation learning. DISCOVR combines a clustering-based video encoder that models temporal dynamics with an online image encoder that extracts fine-grained spatial semantics. These branches are connected through a semantic cluster distillation loss that transfers anatomical knowledge from the evolving image encoder to the video encoder, enabling temporally coherent representations enriched with fine-grained semantic understanding.Evaluated on six echocardiography datasets spanning fetal, pediatric, and adult populations, DISCOVR outperforms both specialized video anomaly detection methods and state-of-the-art video-SSL baselines in zero-shot and linear probing setups,achieving superior segmentation transfer and strong downstream performance on clinically relevant tasks such as LVEF prediction. Code available at: https://github.com/mdivyanshu97/DISCOVR

