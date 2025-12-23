---
layout: default
title: Detection Method for Prompt Injection by Integrating Pre-trained Model and Heuristic Feature Engineering
---

# Detection Method for Prompt Injection by Integrating Pre-trained Model and Heuristic Feature Engineering

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.06384" class="toolbar-btn" target="_blank">📄 arXiv: 2506.06384v1</a>
  <a href="https://arxiv.org/pdf/2506.06384.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.06384v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.06384v1', 'Detection Method for Prompt Injection by Integrating Pre-trained Model and Heuristic Feature Engineering')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yi Ji, Runzhi Li, Baolei Mao

**分类**: cs.CL, cs.AI

**发布日期**: 2025-06-05

**备注**: Accepted by KSEM2025 AI & Sec Workshop

---

## 💡 一句话要点

**提出DMPI-PMHFE以解决提示注入攻击检测问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `提示注入攻击` `大型语言模型` `特征融合` `安全防护` `深度学习`

## 📋 核心要点

1. 现有的提示注入攻击检测方法在有效性和通用性之间存在显著的权衡，难以适应多种大型语言模型。
2. 本文提出DMPI-PMHFE框架，通过结合预训练模型和启发式特征工程，提升提示注入攻击的检测能力。
3. 实验结果显示，DMPI-PMHFE在多个基准数据集上表现优异，显著提高了检测的准确性和召回率。

## 📝 摘要（中文）

随着大型语言模型（LLMs）的广泛应用，提示注入攻击成为了一种显著的安全威胁。现有的防御机制常常在有效性和通用性之间面临重要的权衡，迫切需要高效的提示注入检测方法。为此，本文提出了DMPI-PMHFE，一个双通道特征融合检测框架，结合了预训练语言模型与启发式特征工程，旨在检测提示注入攻击。该框架使用DeBERTa-v3-base作为特征提取器，将输入文本转换为富含上下文信息的语义向量，同时基于已知攻击模式设计启发式规则提取攻击中常见的显式结构特征。两个通道的特征融合后，通过全连接神经网络进行最终预测。实验结果表明，DMPI-PMHFE在准确率、召回率和F1分数上均优于现有方法，并显著降低了主流LLMs（如GLM-4、LLaMA 3、Qwen 2.5和GPT-4o）的攻击成功率。

## 🔬 方法详解

**问题定义**：本文旨在解决提示注入攻击的检测问题，现有方法在不同大型语言模型上的有效性和通用性不足，导致攻击检测能力有限。

**核心思路**：论文提出的DMPI-PMHFE框架通过双通道特征融合，结合预训练语言模型和启发式特征工程，旨在提高检测的准确性和适用性。

**技术框架**：该框架包括两个主要模块：一是使用DeBERTa-v3-base提取输入文本的语义特征，二是基于已知攻击模式设计启发式规则提取结构特征。两个通道的特征经过融合后，输入全连接神经网络进行最终预测。

**关键创新**：DMPI-PMHFE的创新在于其双通道特征融合策略，克服了单一依赖DeBERTa提取特征的局限性，增强了对不同攻击模式的检测能力。

**关键设计**：在技术细节上，框架采用了特定的损失函数和网络结构，以优化特征融合效果，确保最终预测的准确性和鲁棒性。具体参数设置和网络结构细节在实验部分进行了详细描述。

## 📊 实验亮点

实验结果表明，DMPI-PMHFE在多个基准数据集上显著优于现有方法，准确率、召回率和F1分数均有明显提升，尤其在主流LLMs（如GLM-4、LLaMA 3、Qwen 2.5和GPT-4o）上，攻击成功率大幅降低，展现出良好的实际应用效果。

## 🎯 应用场景

该研究的潜在应用领域包括网络安全、自然语言处理和人工智能系统的安全防护。通过有效检测提示注入攻击，能够提升大型语言模型的安全性，保护用户数据和系统完整性，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> With the widespread adoption of Large Language Models (LLMs), prompt injection attacks have emerged as a significant security threat. Existing defense mechanisms often face critical trade-offs between effectiveness and generalizability. This highlights the urgent need for efficient prompt injection detection methods that are applicable across a wide range of LLMs. To address this challenge, we propose DMPI-PMHFE, a dual-channel feature fusion detection framework. It integrates a pretrained language model with heuristic feature engineering to detect prompt injection attacks. Specifically, the framework employs DeBERTa-v3-base as a feature extractor to transform input text into semantic vectors enriched with contextual information. In parallel, we design heuristic rules based on known attack patterns to extract explicit structural features commonly observed in attacks. Features from both channels are subsequently fused and passed through a fully connected neural network to produce the final prediction. This dual-channel approach mitigates the limitations of relying only on DeBERTa to extract features. Experimental results on diverse benchmark datasets demonstrate that DMPI-PMHFE outperforms existing methods in terms of accuracy, recall, and F1-score. Furthermore, when deployed actually, it significantly reduces attack success rates across mainstream LLMs, including GLM-4, LLaMA 3, Qwen 2.5, and GPT-4o.

