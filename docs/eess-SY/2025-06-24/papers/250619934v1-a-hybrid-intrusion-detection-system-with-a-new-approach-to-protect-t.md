---
layout: default
title: A Hybrid Intrusion Detection System with a New Approach to Protect the Cybersecurity of Cloud Computing
---

# A Hybrid Intrusion Detection System with a New Approach to Protect the Cybersecurity of Cloud Computing

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.19934" class="toolbar-btn" target="_blank">📄 arXiv: 2506.19934v1</a>
  <a href="https://arxiv.org/pdf/2506.19934.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.19934v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.19934v1', 'A Hybrid Intrusion Detection System with a New Approach to Protect the Cybersecurity of Cloud Computing')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Maryam Mahdi Al-Husseini

**分类**: cs.CR, eess.SY

**发布日期**: 2025-06-24

**备注**: 1. Acknowledgment for: Supervisor: Prof. Dr. Alireza Rouhi Advisor: Prof. Dr. Einollah Pira 2. Thesis of MSc. degree for Azarbaijan Shahid Madani University Faculty of Information Technology and Computer Engineering 3. Number of pages: 103 4. Number of Figures: 66

---

## 💡 一句话要点

**提出混合入侵检测系统以保护云计算的网络安全**

🎯 **匹配领域**: **支柱五：交互与反应 (Interaction & Reaction)**

**关键词**: `混合入侵检测` `云计算安全` `特征选择` `能量谷优化器` `监督学习` `网络攻击防护` `数据集评估`

## 📋 核心要点

1. 现有的入侵检测系统在复杂性、维度和性能方面存在不足，无法有效应对云计算环境中的安全威胁。
2. 本文提出了一种新的混合入侵检测系统（HyIDS），通过能量谷优化器（EVO）进行特征选择，并结合监督学习模型进行分类。
3. 实验结果表明，所提方法在多个数据集上均表现出色，准确率和检测率均高于传统方法，尤其是在CIC_DDoS2019数据集上达到了99.13%的准确率。

## 📝 摘要（中文）

网络安全是云计算领域面临的主要挑战之一。随着智能设备在云计算环境中的广泛应用，安全威胁变得愈发重要。入侵检测系统的使用可以缓解这些系统的脆弱性，混合入侵检测系统相比传统系统提供了更好的保护。本文提出了一种新的混合入侵检测系统（HyIDS），利用能量谷优化器（EVO）选择最佳特征集，并通过监督学习模型进行分类。研究通过CIC_DDoS2019、CSE_CIC_DDoS2018和NSL-KDD数据集对该方法进行了评估，结果显示EVO在特征选择上优于灰狼优化器（GWO），并在多个数据集上实现了高达99.78%的准确率。

## 🔬 方法详解

**问题定义**：本文旨在解决云计算环境中入侵检测系统的安全性问题，现有方法在复杂性和性能上存在不足，难以有效应对多样化的网络攻击。

**核心思路**：提出了一种混合入侵检测系统（HyIDS），通过能量谷优化器（EVO）选择最优特征集，结合监督学习模型进行分类，从而提高检测准确率和效率。

**技术框架**：该系统主要包括特征选择模块（使用EVO）、分类模块（使用监督学习模型）和评估模块（通过多个数据集进行性能评估）。

**关键创新**：引入了能量谷优化器（EVO）作为特征选择的优化器，相比于传统的灰狼优化器（GWO），EVO在特征选择上表现出更好的性能，显著提升了混合入侵检测系统的效果。

**关键设计**：在特征选择过程中，EVO通过优化特征集来减少维度，提高分类器的性能，采用的损失函数和参数设置经过多次实验验证，以确保系统的稳定性和准确性。

## 📊 实验亮点

实验结果显示，所提出的D_TreeEVO模型在CIC_DDoS2019数据集上达到了99.13%的准确率和98.941%的检测率，而在CSE_CIC_DDoS2018数据集上准确率更是高达99.78%。与NSL-KDD数据集相比，准确率为99.50%，检测率为99.48%，显示出显著的性能提升。

## 🎯 应用场景

该研究的潜在应用领域包括云计算服务提供商、数据中心和企业网络安全防护。通过提高入侵检测的准确性和效率，能够有效保护用户数据和隐私，降低网络攻击带来的风险，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> Cybersecurity is one of the foremost challenges facing the world of cloud computing. Recently, the widespread adoption of smart devices in cloud computing environments that provide Internet-based services has become prevalent. Therefore, it is essential to consider the security threats in these environments. The use of intrusion detection systems can mitigate the vulnerabilities of these systems. Furthermore, hybrid intrusion detection systems can provide better protection compared to conventional intrusion detection systems. These systems manage issues related to complexity, dimensionality, and performance. This research aims to propose a Hybrid Intrusion Detection System (HyIDS) that identifies and mitigates initial threats. The main innovation of this research is the introduction of a new method for hybrid intrusion detection systems (HyIDS). For this purpose, an Energy-Valley Optimizer (EVO) is used to select an optimal feature set, which is then classified using supervised machine learning models. The proposed approach is evaluated using the CIC_DDoS2019, CSE_CIC_DDoS2018, and NSL-KDD datasets. For evaluation and testing, the proposed system has been run for a total of 32 times. The results of the proposed approach are compared with the Grey Wolf Optimizer (GWO). With the CIC_DDoS2019 dataset, the D_TreeEVO model achieves an accuracy of 99.13% and a detection rate of 98.941%. Furthermore, this result reaches 99.78% for the CSE_CIC_DDoS2018 dataset. In comparison to NSL-KDD, it has an accuracy of 99.50% and a detection rate (DT) of 99.48%. For feature selection, EVO outperforms GWO. The results of this research indicate that EVO yields better results as an optimizer for HyIDS performance.

