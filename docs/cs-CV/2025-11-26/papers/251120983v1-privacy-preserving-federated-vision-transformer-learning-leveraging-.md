---
layout: default
title: Privacy-Preserving Federated Vision Transformer Learning Leveraging Lightweight Homomorphic Encryption in Medical AI
---

# Privacy-Preserving Federated Vision Transformer Learning Leveraging Lightweight Homomorphic Encryption in Medical AI

**arXiv**: [2511.20983v1](https://arxiv.org/abs/2511.20983) | [PDF](https://arxiv.org/pdf/2511.20983.pdf)

**作者**: Al Amin, Kamrul Hasan, Liang Hong, Sharif Ullah

**分类**: cs.CV, cs.CR

**发布日期**: 2025-11-26

**备注**: 7 pages, 4 figures

**期刊**: IEEE ICNC2026

---

## 💡 一句话要点

**提出基于同态加密的联邦Vision Transformer学习框架，保护医疗AI中的患者隐私。**

🎯 **匹配领域**: **支柱五：交互与反应 (Interaction & Reaction)**

**关键词**: `联邦学习` `同态加密` `Vision Transformer` `隐私保护` `医疗AI` `组织病理学` `模型反演攻击`

## 📋 核心要点

1. 传统联邦学习中的模型梯度易受重建攻击，可能暴露敏感医疗信息，HIPAA等法规禁止直接共享患者数据。
2. 论文提出一种结合Vision Transformers (ViT) 和同态加密 (HE) 的联邦学习框架，保护多机构组织病理学分类中的隐私。
3. 实验表明，该方法在保证隐私的同时，实现了通信量的显著减少，并在加密域和未加密域均取得了较高的分类精度。

## 📝 摘要（中文）

本文提出了一种保护隐私的联邦学习框架，该框架结合了Vision Transformers (ViT) 和同态加密 (HE)，用于安全的多机构组织病理学分类。该方法利用ViT的CLS token作为紧凑的768维特征表示，用于安全聚合，并在传输到服务器之前使用CKKS同态加密对这些token进行加密。实验表明，与梯度加密相比，加密CLS token实现了30倍的通信减少，同时保持了强大的隐私保证。在肺癌组织病理学分类的三客户端联邦设置中，梯度非常容易受到模型反演攻击（PSNR：52.26 dB，SSIM：0.999，NMI：0.741），从而可以实现近乎完美的图像重建。相比之下，所提出的CLS保护的HE方法可以防止此类攻击，同时可以直接在密文上进行加密推理，每次聚合轮次仅需要326 KB的加密数据传输。该框架在未加密域中实现了96.12％的全局分类精度，在加密域中实现了90.02％的全局分类精度。

## 🔬 方法详解

**问题定义**：论文旨在解决在医疗AI领域，利用联邦学习进行多机构协作训练时，如何保护患者隐私的问题。传统的联邦学习虽然避免了直接共享原始数据，但模型梯度仍然存在被攻击者利用进行数据重建的风险，这使得在医疗场景下的应用受到限制。现有方法的痛点在于，如何在保证模型性能的同时，提供更强的隐私保护。

**核心思路**：论文的核心思路是利用Vision Transformer (ViT) 的CLS token作为一种紧凑的特征表示，并使用同态加密 (HE) 对其进行加密，从而在联邦学习过程中保护隐私。CLS token包含了图像的全局信息，同时维度较低，适合进行加密。通过对CLS token进行同态加密，可以在服务器端进行加密数据的聚合和计算，而无需解密，从而防止了梯度泄露。

**技术框架**：该框架主要包含以下几个阶段：1) 客户端使用本地数据训练ViT模型，提取CLS token；2) 客户端使用CKKS同态加密算法对CLS token进行加密；3) 客户端将加密后的CLS token发送到服务器；4) 服务器对加密的CLS token进行聚合；5) 服务器将聚合后的加密CLS token发送回客户端；6) 客户端对加密的CLS token进行解密，并更新本地模型。

**关键创新**：该论文最重要的技术创新点在于，将ViT的CLS token与同态加密相结合，用于联邦学习中的隐私保护。与直接加密梯度相比，加密CLS token可以显著减少通信量，同时保持较强的隐私保护能力。此外，该方法支持在加密域进行推理，进一步增强了隐私性。

**关键设计**：论文使用了CKKS同态加密算法，该算法允许在加密数据上进行近似计算。CLS token的维度为768维。实验中使用了三个客户端进行联邦学习。损失函数使用了交叉熵损失函数。ViT模型的具体结构和参数设置未在摘要中详细说明，需要参考论文全文。

## 📊 实验亮点

实验结果表明，直接使用梯度进行联邦学习容易受到模型反演攻击，图像重建效果接近完美（PSNR: 52.26 dB, SSIM: 0.999, NMI: 0.741）。而提出的CLS保护的HE方法可以有效防止此类攻击，同时每次聚合轮次仅需传输326 KB的加密数据，并在未加密域和加密域分别实现了96.12%和90.02%的全局分类精度。

## 🎯 应用场景

该研究成果可应用于医疗影像分析、基因组学等领域，实现多家医疗机构在保护患者隐私的前提下进行协作研究，提升疾病诊断和治疗水平。该方法还可推广到其他对数据隐私有较高要求的联邦学习场景，例如金融风控、智能制造等。

## 📄 摘要（原文）

> Collaborative machine learning across healthcare institutions promises improved diagnostic accuracy by leveraging diverse datasets, yet privacy regulations such as HIPAA prohibit direct patient data sharing. While federated learning (FL) enables decentralized training without raw data exchange, recent studies show that model gradients in conventional FL remain vulnerable to reconstruction attacks, potentially exposing sensitive medical information. This paper presents a privacy-preserving federated learning framework combining Vision Transformers (ViT) with homomorphic encryption (HE) for secure multi-institutional histopathology classification. The approach leverages the ViT CLS token as a compact 768-dimensional feature representation for secure aggregation, encrypting these tokens using CKKS homomorphic encryption before transmission to the server. We demonstrate that encrypting CLS tokens achieves a 30-fold communication reduction compared to gradient encryption while maintaining strong privacy guarantees. Through evaluation on a three-client federated setup for lung cancer histopathology classification, we show that gradients are highly susceptible to model inversion attacks (PSNR: 52.26 dB, SSIM: 0.999, NMI: 0.741), enabling near-perfect image reconstruction. In contrast, the proposed CLS-protected HE approach prevents such attacks while enabling encrypted inference directly on ciphertexts, requiring only 326 KB of encrypted data transmission per aggregation round. The framework achieves 96.12 percent global classification accuracy in the unencrypted domain and 90.02 percent in the encrypted domain.

