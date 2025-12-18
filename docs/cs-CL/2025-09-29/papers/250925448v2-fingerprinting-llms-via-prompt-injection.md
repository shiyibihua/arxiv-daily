---
layout: default
title: Fingerprinting LLMs via Prompt Injection
---

# Fingerprinting LLMs via Prompt Injection

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.25448" class="toolbar-btn" target="_blank">📄 arXiv: 2509.25448v2</a>
  <a href="https://arxiv.org/pdf/2509.25448.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.25448v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.25448v2', 'Fingerprinting LLMs via Prompt Injection')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yuepeng Hu, Zhengyuan Jiang, Mengyuan Li, Osama Ahmed, Zhicong Huang, Cheng Hong, Neil Gong

**分类**: cs.CR, cs.CL

**发布日期**: 2025-09-29 (更新: 2025-10-01)

---

## 💡 一句话要点

**LLMPrint：利用Prompt注入为LLM构建鲁棒指纹，实现模型溯源**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `模型溯源` `Prompt注入` `模型指纹` `后处理鲁棒性`

## 📋 核心要点

1. 现有LLM溯源方法依赖于预先嵌入水印或使用随机prompt，前者无法应用于已发布模型，后者对后处理鲁棒性差。
2. LLMPrint利用prompt注入漏洞，通过优化prompt来诱导模型产生特定的token偏好，以此构建对后处理鲁棒的指纹。
3. 实验表明，LLMPrint在多种模型和后处理变体上实现了高真阳性率和低假阳性率，验证了其有效性。

## 📝 摘要（中文）

大型语言模型（LLM）发布后通常会经过后处理，如后训练或量化，这使得确定一个模型是否源自另一个模型变得困难。现有的溯源检测方法存在两个主要限制：（1）它们在发布前将信号嵌入到基础模型中，这对于已发布的模型是不可行的；（2）它们使用手工制作或随机提示比较模型之间的输出，这对于后处理不具有鲁棒性。本文提出了LLMPrint，一种新颖的检测框架，通过利用LLM固有的Prompt注入漏洞来构建指纹。核心思想是通过优化指纹提示来强制执行一致的token偏好，从而获得对基础模型独特且对后处理具有鲁棒性的指纹。进一步开发了一种适用于灰盒和黑盒设置的统一验证程序，并具有统计保证。在五个基础模型和大约700个后训练或量化变体上评估了LLMPrint。结果表明，LLMPrint实现了高真阳性率，同时保持假阳性率接近于零。

## 🔬 方法详解

**问题定义**：论文旨在解决大型语言模型（LLM）溯源问题，即判断一个经过后处理（如量化、微调）的模型是否衍生自某个已知的原始模型。现有方法的痛点在于，要么需要预先在原始模型中嵌入水印（不适用于已发布模型），要么使用随机或手工设计的prompt进行比对，但这些prompt对后处理的鲁棒性较差，容易受到干扰。

**核心思路**：论文的核心思路是利用LLM对prompt注入的脆弱性，通过精心设计的prompt，诱导模型产生特定的、具有区分性的token偏好。这些token偏好可以作为模型的“指纹”，即使经过后处理，这些指纹仍然相对稳定。通过比较不同模型的指纹，可以判断它们是否具有相同的来源。

**技术框架**：LLMPrint框架包含两个主要阶段：指纹生成阶段和指纹验证阶段。在指纹生成阶段，针对每个基础模型，通过优化算法生成一组特定的prompt，这些prompt能够诱导模型产生特定的token序列。在指纹验证阶段，对于待验证的模型，使用相同的prompt，观察其产生的token序列，并与基础模型的指纹进行比对，从而判断其是否衍生自该基础模型。该框架同时支持灰盒和黑盒场景。

**关键创新**：最重要的技术创新点在于利用prompt注入漏洞来构建模型的指纹。与传统的水印方法不同，LLMPrint不需要预先修改模型，因此可以应用于已发布的模型。与随机prompt方法不同，LLMPrint通过优化prompt来最大化token偏好的一致性，从而提高指纹的鲁棒性。

**关键设计**：指纹生成阶段的关键在于prompt的优化算法。论文采用了一种基于梯度下降的优化方法，目标是找到一组prompt，使得模型在这些prompt下产生特定token序列的概率最大化。此外，论文还设计了一种统计验证方法，用于评估两个模型指纹之间的相似度，并给出统计显著性保证。

## 📊 实验亮点

LLMPrint在五个基础模型和约700个后处理变体上进行了评估，实现了接近100%的真阳性率，同时保持假阳性率接近于零。实验结果表明，LLMPrint对量化和后训练等后处理方法具有很强的鲁棒性，能够有效识别衍生模型。

## 🎯 应用场景

LLMPrint可用于检测恶意模型抄袭、验证模型来源、防止未经授权的模型修改和分发。在模型安全和知识产权保护方面具有重要应用价值。未来可扩展到更广泛的AI模型溯源和安全审计领域，促进AI技术的健康发展。

## 📄 摘要（原文）

> Large language models (LLMs) are often modified after release through post-processing such as post-training or quantization, which makes it challenging to determine whether one model is derived from another. Existing provenance detection methods have two main limitations: (1) they embed signals into the base model before release, which is infeasible for already published models, or (2) they compare outputs across models using hand-crafted or random prompts, which are not robust to post-processing. In this work, we propose LLMPrint, a novel detection framework that constructs fingerprints by exploiting LLMs' inherent vulnerability to prompt injection. Our key insight is that by optimizing fingerprint prompts to enforce consistent token preferences, we can obtain fingerprints that are both unique to the base model and robust to post-processing. We further develop a unified verification procedure that applies to both gray-box and black-box settings, with statistical guarantees. We evaluate LLMPrint on five base models and around 700 post-trained or quantized variants. Our results show that LLMPrint achieves high true positive rates while keeping false positive rates near zero.

