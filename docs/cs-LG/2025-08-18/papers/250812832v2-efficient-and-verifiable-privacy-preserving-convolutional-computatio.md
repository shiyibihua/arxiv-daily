---
layout: default
title: Efficient and Verifiable Privacy-Preserving Convolutional Computation for CNN Inference with Untrusted Clouds
---

# Efficient and Verifiable Privacy-Preserving Convolutional Computation for CNN Inference with Untrusted Clouds

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.12832" class="toolbar-btn" target="_blank">📄 arXiv: 2508.12832v2</a>
  <a href="https://arxiv.org/pdf/2508.12832.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.12832v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.12832v2', 'Efficient and Verifiable Privacy-Preserving Convolutional Computation for CNN Inference with Untrusted Clouds')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jinyu Lu, Xinrong Sun, Yunting Tao, Tong Ji, Fanyu Kong, Guoqiang Yang

**分类**: cs.CR, cs.LG

**发布日期**: 2025-08-18 (更新: 2025-08-19)

**备注**: Conference link: [ICIC 2025](http://www.ic-icc.cn/2025/index.php) will provide further details

**期刊**: International Conference On Intelligent Computing 2025, Ningbo, China, July 26-29, 2025, Volume I, pp. 866-881

---

## 💡 一句话要点

**提出高效可验证的隐私保护卷积计算方案以解决云计算中的隐私泄露问题**

🎯 **匹配领域**: **支柱五：交互与反应 (Interaction & Reaction)**

**关键词**: `隐私保护` `卷积神经网络` `云计算` `同态加密` `机器学习服务` `结果验证` `高效计算`

## 📋 核心要点

1. 现有的CNN隐私保护方案在确保数据机密性方面有效，但在卷积操作的效率上存在瓶颈，影响了实际应用。
2. 本文提出了一种新颖的可验证隐私保护方案，专门针对CNN卷积层，能够高效地进行加密和解密，支持资源受限客户端的安全计算。
3. 实验结果表明，该方案在10个数据集和多种CNN模型上实现了26倍至87倍的速度提升，同时保持了模型的准确性。

## 📝 摘要（中文）

卷积神经网络（CNN）在资源受限场景中的广泛应用推动了机器学习即服务（MLaaS）系统的发展。然而，客户端发送到不可信云服务器的数据往往包含敏感信息，容易导致隐私泄露。现有的CNN隐私保护方案虽然通过同态加密和秘密共享确保数据机密性，但在卷积操作中面临效率瓶颈。本文提出了一种新颖的可验证隐私保护方案，专门针对CNN卷积层，能够实现高效的加密和解密，使资源受限的客户端能够安全地将计算任务卸载到不可信的云服务器。此外，我们还提出了一种验证机制，能够以至少$1-rac{1}{	ext{\|Z\|} }$的成功概率检测结果的正确性。通过在10个数据集和多种CNN模型上的广泛实验，我们的方案在保持准确性的同时，实现了比原始明文模型快26倍至87倍的速度提升。

## 🔬 方法详解

**问题定义**：本文旨在解决在不可信云环境中进行CNN推理时的隐私泄露问题。现有方法虽然能保护数据机密性，但在卷积操作的效率上存在显著瓶颈。

**核心思路**：我们提出了一种新颖的可验证隐私保护方案，专门针对CNN的卷积层设计，能够实现高效的加密和解密过程，从而使资源受限的客户端能够安全地将计算任务卸载到云服务器。

**技术框架**：该方案包括数据加密、卷积计算、结果验证等主要模块。首先，客户端对输入数据进行加密，然后将加密数据发送到云服务器进行卷积计算，最后通过验证机制确保计算结果的正确性。

**关键创新**：本研究的核心创新在于提出了一种高效的卷积计算加密方案，并结合了结果验证机制，显著提高了计算效率与安全性。这与现有方法的本质区别在于同时解决了隐私保护与计算效率的问题。

**关键设计**：在设计中，我们采用了特定的加密算法和优化的卷积计算策略，确保在保证安全性的同时，最大限度地提升计算速度。

## 📊 实验亮点

实验结果显示，所提出的隐私保护方案在10个数据集和多种CNN模型上实现了26倍至87倍的速度提升，相较于原始明文模型，且在保持模型准确性的同时，验证机制的成功概率达到至少$1-rac{1}{	ext{\|Z\|} }$，显示出良好的实用性和有效性。

## 🎯 应用场景

该研究的潜在应用领域包括医疗数据分析、金融数据处理和智能监控等需要保护用户隐私的场景。通过安全地将计算任务卸载到云端，用户可以在不泄露敏感信息的情况下，利用云计算的强大能力进行数据分析。这一方案的实际价值在于提升了隐私保护的同时，确保了计算效率，具有广泛的应用前景。

## 📄 摘要（原文）

> The widespread adoption of convolutional neural networks (CNNs) in resource-constrained scenarios has driven the development of Machine Learning as a Service (MLaaS) system. However, this approach is susceptible to privacy leakage, as the data sent from the client to the untrusted cloud server often contains sensitive information. Existing CNN privacy-preserving schemes, while effective in ensuring data confidentiality through homomorphic encryption and secret sharing, face efficiency bottlenecks, particularly in convolution operations. In this paper, we propose a novel verifiable privacy-preserving scheme tailored for CNN convolutional layers. Our scheme enables efficient encryption and decryption, allowing resource-constrained clients to securely offload computations to the untrusted cloud server. Additionally, we present a verification mechanism capable of detecting the correctness of the results with a success probability of at least $1-\frac{1}{\left\|Z\right\|}$. Extensive experiments conducted on 10 datasets and various CNN models demonstrate that our scheme achieves speedups ranging $26 \times$ ~ $\ 87\times$ compared to the original plaintext model while maintaining accuracy.

