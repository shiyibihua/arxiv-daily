---
layout: default
title: A Vision-Language Pre-training Model-Guided Approach for Mitigating Backdoor Attacks in Federated Learning
---

# A Vision-Language Pre-training Model-Guided Approach for Mitigating Backdoor Attacks in Federated Learning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.10315" class="toolbar-btn" target="_blank">📄 arXiv: 2508.10315v2</a>
  <a href="https://arxiv.org/pdf/2508.10315.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.10315v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.10315v2', 'A Vision-Language Pre-training Model-Guided Approach for Mitigating Backdoor Attacks in Federated Learning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Keke Gai, Dongjue Wang, Jing Yu, Liehuang Zhu, Qi Wu

**分类**: cs.LG, cs.AI

**发布日期**: 2025-08-14 (更新: 2025-10-13)

---

## 💡 一句话要点

**提出CLIP-Fed以解决联邦学习中的后门攻击问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `联邦学习` `后门攻击` `视觉-语言模型` `零样本学习` `数据增强` `隐私保护`

## 📋 核心要点

1. 现有方法在异构客户端数据分布下，难以有效防御后门攻击，同时又需兼顾隐私保护。
2. 本文提出的CLIP-Fed框架，利用视觉-语言预训练模型的零样本学习能力，集成了预聚合和后聚合防御策略。
3. 实验结果显示，CLIP-Fed在多个数据集上显著降低了攻击成功率，并提高了主要任务的准确率。

## 📝 摘要（中文）

在联邦学习中，针对异构客户端数据分布的后门攻击防御面临有效性与隐私保护之间的平衡挑战。本文提出了一种名为CLIP-Fed的框架，利用视觉-语言预训练模型的零样本学习能力，克服了非独立同分布（Non-IID）对防御效果的限制。CLIP-Fed通过集成预聚合和后聚合防御策略，确保了后门样本引起的类原型偏差被消除。实验结果表明，CLIP-Fed在CIFAR-10和CIFAR-10-LT数据集上分别实现了攻击成功率的平均降低2.03%和1.35%，同时提高了主要任务的准确率7.92%和0.48%。

## 🔬 方法详解

**问题定义**：本文旨在解决联邦学习中后门攻击防御的有效性与隐私保护之间的矛盾。现有方法多依赖于同质客户端数据分布或干净的服务器数据集，限制了其在异构环境下的应用。

**核心思路**：CLIP-Fed框架利用视觉-语言预训练模型的零样本学习能力，通过对抗后门样本引起的类原型偏差，提升防御效果。该设计旨在消除触发模式与目标标签之间的相关性。

**技术框架**：CLIP-Fed的整体架构包括数据增强、预聚合和后聚合防御策略。首先，通过多模态大语言模型和频率分析构建和增强服务器数据集，然后应用原型对比损失和Kullback-Leibler散度进行模型对齐。

**关键创新**：CLIP-Fed的主要创新在于结合了视觉-语言模型的零样本学习能力与多模态数据增强，克服了非独立同分布对防御效果的限制。与现有方法相比，CLIP-Fed在防御效果和隐私保护上实现了更好的平衡。

**关键设计**：在损失函数设计上，采用了原型对比损失和Kullback-Leibler散度，以确保后门样本对类原型的影响被有效抑制。同时，数据增强过程不依赖于客户端样本，增强了隐私保护。

## 📊 实验亮点

CLIP-Fed在CIFAR-10和CIFAR-10-LT数据集上，分别实现了攻击成功率的平均降低2.03%和1.35%，同时提高了主要任务的准确率7.92%和0.48%。这些结果表明，CLIP-Fed在防御后门攻击方面的有效性显著优于现有方法。

## 🎯 应用场景

该研究的潜在应用领域包括安全的联邦学习系统，尤其是在医疗、金融等对隐私要求高的行业。CLIP-Fed的防御机制能够有效抵御后门攻击，确保模型的安全性和可靠性，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> Defending backdoor attacks in Federated Learning (FL) under heterogeneous client data distributions encounters limitations balancing effectiveness and privacy-preserving, while most existing methods highly rely on the assumption of homogeneous client data distributions or the availability of a clean serve dataset. In this paper, we propose an FL backdoor defense framework, named CLIP-Fed, that utilizes the zero-shot learning capabilities of vision-language pre-training models. Our scheme overcomes the limitations of Non-IID imposed on defense effectiveness by integrating pre-aggregation and post-aggregation defense strategies. CLIP-Fed aligns the knowledge of the global model and CLIP on the augmented dataset using prototype contrastive loss and Kullback-Leibler divergence, so that class prototype deviations caused by backdoor samples are ensured and the correlation between trigger patterns and target labels is eliminated. In order to balance privacy-preserving and coverage enhancement of the dataset against diverse triggers, we further construct and augment the server dataset via using the multimodal large language model and frequency analysis without any client samples. Extensive experiments on representative datasets evidence the effectiveness of CLIP-Fed. Comparing to other existing methods, CLIP-Fed achieves an average reduction in Attack Success Rate, {\em i.e.}, 2.03\% on CIFAR-10 and 1.35\% on CIFAR-10-LT, while improving average Main Task Accuracy by 7.92\% and 0.48\%, respectively. Our codes are available at https://anonymous.4open.science/r/CLIP-Fed.

