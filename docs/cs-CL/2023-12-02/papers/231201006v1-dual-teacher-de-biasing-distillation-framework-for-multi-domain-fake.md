---
layout: default
title: Dual-Teacher De-biasing Distillation Framework for Multi-domain Fake News Detection
---

# Dual-Teacher De-biasing Distillation Framework for Multi-domain Fake News Detection

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2312.01006" class="toolbar-btn" target="_blank">📄 arXiv: 2312.01006v1</a>
  <a href="https://arxiv.org/pdf/2312.01006.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2312.01006v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2312.01006v1', 'Dual-Teacher De-biasing Distillation Framework for Multi-domain Fake News Detection')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jiayang Li, Xuan Feng, Tianlong Gu, Liang Chang

**分类**: cs.CL

**发布日期**: 2023-12-02

**备注**: ICDE 2024

---

## 💡 一句话要点

**提出双教师解偏蒸馏框架DTDBD，缓解多领域假新闻检测中的领域偏差问题。**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `假新闻检测` `领域偏差` `知识蒸馏` `对抗训练` `多领域学习`

## 📋 核心要点

1. 现有假新闻检测方法侧重于整体性能提升，忽略了数据不平衡导致的领域偏差问题。
2. DTDBD框架采用双教师结构，通过无偏教师和干净教师共同指导学生模型，缓解领域偏差并保持性能。
3. 实验结果表明，DTDBD在偏差指标上显著优于现有方法，同时保证了良好的检测性能。

## 📝 摘要（中文）

多领域假新闻检测旨在识别来自不同领域的各种新闻的真伪，这已变得紧迫而重要。然而，现有方法致力于提高假新闻检测的整体性能，忽略了不平衡数据导致对不同领域的区别对待，即领域偏差问题。为了解决这个问题，我们提出了双教师解偏蒸馏框架（DTDBD）来减轻不同领域之间的偏差。遵循知识蒸馏方法，DTDBD采用教师-学生结构，其中预训练的大型教师指导学生模型。特别地，DTDBD由一个无偏教师和一个干净教师组成，它们共同指导学生模型减轻领域偏差并保持性能。对于无偏教师，我们引入了一种对抗性解偏蒸馏损失，以指导学生模型学习无偏领域知识。对于干净教师，我们设计了领域知识蒸馏损失，有效地激励学生模型专注于表示领域特征，同时保持性能。此外，我们提出了一种基于动量的动态调整算法来权衡两位教师的影响。在中文和英文数据集上的大量实验表明，所提出的方法在偏差指标方面大大优于最先进的基线方法，同时保证了具有竞争力的性能。

## 🔬 方法详解

**问题定义**：多领域假新闻检测任务中，由于各领域数据量不平衡，模型容易产生领域偏差，导致在某些领域表现不佳。现有方法通常只关注整体性能，忽略了这种偏差带来的负面影响。

**核心思路**：利用知识蒸馏，通过两个教师模型分别提供无偏和干净的领域知识，指导学生模型学习。无偏教师负责消除领域偏差，干净教师负责保持整体性能。通过这种方式，学生模型可以同时学习到领域无关的知识和领域特定的特征。

**技术框架**：DTDBD框架包含一个学生模型和两个教师模型：无偏教师和干净教师。首先，使用预训练模型作为教师模型。然后，无偏教师通过对抗性解偏蒸馏损失，指导学生模型学习无偏领域知识。干净教师通过领域知识蒸馏损失，指导学生模型学习领域特征。最后，使用基于动量的动态调整算法，平衡两个教师的影响。

**关键创新**：核心创新在于双教师的解偏蒸馏框架。通过引入无偏教师和对抗性解偏蒸馏损失，显式地减少了模型中的领域偏差。同时，干净教师的存在保证了模型在整体性能上的竞争力。

**关键设计**：对抗性解偏蒸馏损失的设计是关键。该损失函数通过对抗训练，使学生模型学习到的特征尽可能与领域无关。领域知识蒸馏损失则鼓励学生模型学习领域特定的特征表示。基于动量的动态调整算法用于平衡两个教师的影响，其权重根据训练过程中的性能动态调整。

## 📊 实验亮点

在中文和英文数据集上的实验结果表明，DTDBD框架在偏差指标上显著优于现有方法。例如，在某个数据集上，DTDBD的偏差指标降低了XX%，同时保持了与最佳基线方法相当的整体性能。这表明DTDBD能够有效缓解领域偏差，提高假新闻检测的公平性。

## 🎯 应用场景

该研究成果可应用于各种在线新闻平台，以提高假新闻检测的准确性和公平性。通过减轻领域偏差，可以确保不同领域的新闻得到公正的评估，从而减少虚假信息传播，维护社会稳定。此外，该方法也可推广到其他存在领域偏差的分类任务中。

## 📄 摘要（原文）

> Multi-domain fake news detection aims to identify whether various news from different domains is real or fake and has become urgent and important. However, existing methods are dedicated to improving the overall performance of fake news detection, ignoring the fact that unbalanced data leads to disparate treatment for different domains, i.e., the domain bias problem. To solve this problem, we propose the Dual-Teacher De-biasing Distillation framework (DTDBD) to mitigate bias across different domains. Following the knowledge distillation methods, DTDBD adopts a teacher-student structure, where pre-trained large teachers instruct a student model. In particular, the DTDBD consists of an unbiased teacher and a clean teacher that jointly guide the student model in mitigating domain bias and maintaining performance. For the unbiased teacher, we introduce an adversarial de-biasing distillation loss to instruct the student model in learning unbiased domain knowledge. For the clean teacher, we design domain knowledge distillation loss, which effectively incentivizes the student model to focus on representing domain features while maintaining performance. Moreover, we present a momentum-based dynamic adjustment algorithm to trade off the effects of two teachers. Extensive experiments on Chinese and English datasets show that the proposed method substantially outperforms the state-of-the-art baseline methods in terms of bias metrics while guaranteeing competitive performance.

