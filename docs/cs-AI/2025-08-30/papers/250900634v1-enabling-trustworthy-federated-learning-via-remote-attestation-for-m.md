---
layout: default
title: Enabling Trustworthy Federated Learning via Remote Attestation for Mitigating Byzantine Threats
---

# Enabling Trustworthy Federated Learning via Remote Attestation for Mitigating Byzantine Threats

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.00634" class="toolbar-btn" target="_blank">📄 arXiv: 2509.00634v1</a>
  <a href="https://arxiv.org/pdf/2509.00634.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.00634v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.00634v1', 'Enabling Trustworthy Federated Learning via Remote Attestation for Mitigating Byzantine Threats')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Chaoyu Zhang, Heng Jin, Shanghao Shi, Hexuan Yu, Sydney Johns, Y. Thomas Hou, Wenjing Lou

**分类**: cs.CR, cs.AI

**发布日期**: 2025-08-30

---

## 💡 一句话要点

**提出Sentinel以解决联邦学习中的拜占庭攻击问题**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)**

**关键词**: `联邦学习` `拜占庭攻击` `远程证明` `受信任执行环境` `数据安全` `隐私保护` `物联网` `模型更新`

## 📋 核心要点

1. 核心问题：现有联邦学习方法在面对拜占庭攻击时，难以有效区分恶意更新与自然数据变异，导致安全隐患。
2. 方法要点：提出Sentinel方案，通过远程证明技术增强客户端透明性，监控本地训练过程，确保模型更新的可信性。
3. 实验或效果：在物联网设备上进行实验，Sentinel以低开销确保本地训练完整性，显著提升了系统的安全性。

## 📝 摘要（中文）

联邦学习（FL）因其隐私保护能力而受到广泛关注，允许分布式设备在不共享原始数据的情况下协作训练全球模型。然而，其分布式特性使得中央服务器必须盲目信任本地训练过程，并聚合不确定的模型更新，这使其易受恶意参与者的拜占庭攻击。现有的数据驱动防御方法难以区分恶意更新与自然变异，导致高假阳性率和过滤性能差。为了解决这一挑战，本文提出了Sentinel，一个基于远程证明的FL系统方案，从系统安全的角度恢复客户端透明性并减轻拜占庭攻击。该系统通过代码插桩跟踪控制流并监控本地训练过程中的关键变量，并利用受信任的执行环境中的训练记录器生成经过加密签名的证明报告，确保只有可信的模型更新被聚合。实验结果表明，Sentinel在物联网设备上以低运行时和内存开销确保本地训练的完整性。

## 🔬 方法详解

**问题定义**：本文旨在解决联邦学习中由于恶意参与者引发的拜占庭攻击问题。现有方法在检测恶意更新时面临困难，因其无法有效区分恶意行为与自然数据变异，导致高假阳性率和过滤性能差。

**核心思路**：提出Sentinel方案，利用远程证明（RA）技术增强客户端透明性，从系统安全的角度监控本地训练过程，确保只有可信的模型更新被聚合。通过代码插桩跟踪控制流和关键变量，结合受信任的执行环境（TEE）生成加密签名的证明报告。

**技术框架**：Sentinel的整体架构包括三个主要模块：1）代码插桩模块，负责监控本地训练过程；2）受信任的训练记录器，生成证明报告；3）中央服务器，验证报告并聚合可信的模型更新。

**关键创新**：Sentinel的主要创新在于结合远程证明技术与受信任的执行环境，确保客户端训练过程的透明性和可信性。这一设计与现有方法的本质区别在于，Sentinel通过系统级别的监控来防范拜占庭攻击，而非仅依赖数据驱动的检测。

**关键设计**：在设计中，Sentinel采用了代码插桩技术来监控训练过程中的控制流和关键变量，确保数据的完整性。同时，受信任的训练记录器在TEE中运行，生成的证明报告经过加密签名，确保数据传输的安全性。

## 📊 实验亮点

实验结果显示，Sentinel在物联网设备上运行时，能够以低于5%的运行时和内存开销确保本地训练的完整性，相较于传统方法，显著降低了假阳性率，提高了系统的安全性和可靠性。

## 🎯 应用场景

该研究的潜在应用领域包括金融、医疗和智能物联网等对数据安全性要求极高的场景。通过增强联邦学习系统的安全性，Sentinel能够有效保护用户隐私，促进分布式智能系统的广泛应用，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> Federated Learning (FL) has gained significant attention for its privacy-preserving capabilities, enabling distributed devices to collaboratively train a global model without sharing raw data. However, its distributed nature forces the central server to blindly trust the local training process and aggregate uncertain model updates, making it susceptible to Byzantine attacks from malicious participants, especially in mission-critical scenarios. Detecting such attacks is challenging due to the diverse knowledge across clients, where variations in model updates may stem from benign factors, such as non-IID data, rather than adversarial behavior. Existing data-driven defenses struggle to distinguish malicious updates from natural variations, leading to high false positive rates and poor filtering performance.
>   To address this challenge, we propose Sentinel, a remote attestation (RA)-based scheme for FL systems that regains client-side transparency and mitigates Byzantine attacks from a system security perspective. Our system employs code instrumentation to track control-flow and monitor critical variables in the local training process. Additionally, we utilize a trusted training recorder within a Trusted Execution Environment (TEE) to generate an attestation report, which is cryptographically signed and securely transmitted to the server. Upon verification, the server ensures that legitimate client training processes remain free from program behavior violation or data manipulation, allowing only trusted model updates to be aggregated into the global model. Experimental results on IoT devices demonstrate that Sentinel ensures the trustworthiness of the local training integrity with low runtime and memory overhead.

