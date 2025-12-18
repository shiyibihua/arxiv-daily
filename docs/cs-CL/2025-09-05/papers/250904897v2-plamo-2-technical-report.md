---
layout: default
title: PLaMo 2 Technical Report
---

# PLaMo 2 Technical Report

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.04897" class="toolbar-btn" target="_blank">📄 arXiv: 2509.04897v2</a>
  <a href="https://arxiv.org/pdf/2509.04897.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.04897v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.04897v2', 'PLaMo 2 Technical Report')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Preferred Networks, :, Kaizaburo Chubachi, Yasuhiro Fujita, Shinichi Hemmi, Yuta Hirokawa, Kentaro Imajo, Toshiki Kataoka, Goro Kobayashi, Kenichi Maehashi, Calvin Metzger, Hiroaki Mikami, Shogo Murai, Daisuke Nishino, Kento Nozawa, Toru Ogawa, Shintarou Okada, Daisuke Okanohara, Shunta Saito, Shotaro Sano, Shuji Suzuki, Kuniyuki Takahashi, Daisuke Tanaka, Avinash Ummadisingu, Hanqin Wang, Sixue Wang, Tianqi Xu

**分类**: cs.CL, cs.AI, cs.LG

**发布日期**: 2025-09-05 (更新: 2025-09-25)

---

## 💡 一句话要点

**PLaMo 2：面向日语的混合架构大型语言模型，性能媲美千亿级模型。**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `日语NLP` `混合架构` `结构化剪枝` `合成数据` `指令微调` `模型优化`

## 📋 核心要点

1. 现有日语大型语言模型面临数据稀缺和计算成本高昂的挑战，限制了模型性能和可扩展性。
2. PLaMo 2通过混合架构、合成数据增强、权重重用和结构化剪枝等技术，有效提升模型性能并降低计算成本。
3. 实验结果表明，PLaMo 2的8B模型性能可与之前的100B模型媲美，并在日语基准测试中超越同等规模的开源模型。

## 📝 摘要（中文）

本报告介绍了PLaMo 2，一系列以日语为中心的大型语言模型，采用基于Samba的混合架构，通过持续预训练过渡到全注意力机制，以支持32K token的上下文长度。训练利用了广泛的合成语料库来克服数据稀缺问题，并通过权重重用和结构化剪枝实现计算效率。这种高效的剪枝方法产生了一个8B模型，其性能与我们之前的100B模型相当。后训练使用监督微调（SFT）和直接偏好优化（DPO）的流程进一步优化模型，并由合成日语指令数据和模型合并技术增强。PLaMo 2模型使用vLLM进行优化推理，并使用量化技术以最小的精度损失，在日语基准测试中取得了最先进的结果，在指令遵循、语言流畅性和日语特定知识方面优于类似规模的开源模型。

## 🔬 方法详解

**问题定义**：现有日语大型语言模型面临数据稀缺的问题，导致模型在日语特定知识和语言流畅性方面表现不足。同时，训练和部署大型模型需要巨大的计算资源，限制了模型的实际应用。

**核心思路**：PLaMo 2的核心思路是利用合成数据增强来弥补数据稀缺，并采用混合架构和高效剪枝技术来降低计算成本。通过持续预训练，模型能够更好地适应长上下文，提升性能。

**技术框架**：PLaMo 2的训练流程包括以下几个主要阶段：1) 基于Samba的混合架构预训练，逐步过渡到全注意力机制；2) 利用合成日语语料进行数据增强；3) 通过权重重用和结构化剪枝降低模型规模；4) 使用监督微调（SFT）和直接偏好优化（DPO）进行后训练，提升指令遵循能力。

**关键创新**：PLaMo 2的关键创新在于其混合架构和高效剪枝方法。混合架构允许模型在计算效率和性能之间取得平衡，而结构化剪枝则可以在不显著降低模型性能的前提下，大幅减少模型参数量。此外，合成数据的有效利用也是一个重要创新。

**关键设计**：PLaMo 2采用了32K token的上下文长度，并通过持续预训练来支持长上下文。在剪枝方面，采用了结构化剪枝方法，保留了模型的重要连接。后训练阶段，使用了合成日语指令数据和模型合并技术，进一步提升模型性能。具体参数设置和损失函数等细节未在摘要中详细说明，属于未知信息。

## 📊 实验亮点

PLaMo 2的8B模型在日语基准测试中取得了最先进的结果，其性能与之前的100B模型相当。在指令遵循、语言流畅性和日语特定知识方面，PLaMo 2优于同等规模的开源模型。这些结果表明，通过混合架构、合成数据增强和高效剪枝等技术，可以在显著降低计算成本的同时，保持甚至提升模型性能。

## 🎯 应用场景

PLaMo 2可广泛应用于日语自然语言处理任务，如机器翻译、文本生成、对话系统、信息检索等。其高效的性能和较小的模型规模使其更易于部署在资源受限的环境中，例如移动设备和边缘计算平台。该研究有望推动日语自然语言处理技术的发展，并促进相关应用的普及。

## 📄 摘要（原文）

> In this report, we introduce PLaMo 2, a series of Japanese-focused large language models featuring a hybrid Samba-based architecture that transitions to full attention via continual pre-training to support 32K token contexts. Training leverages extensive synthetic corpora to overcome data scarcity, while computational efficiency is achieved through weight reuse and structured pruning. This efficient pruning methodology produces an 8B model that achieves performance comparable to our previous 100B model. Post-training further refines the models using a pipeline of supervised fine-tuning (SFT) and direct preference optimization (DPO), enhanced by synthetic Japanese instruction data and model merging techniques. Optimized for inference using vLLM and quantization with minimal accuracy loss, the PLaMo 2 models achieve state-of-the-art results on Japanese benchmarks, outperforming similarly-sized open models in instruction-following, language fluency, and Japanese-specific knowledge.

