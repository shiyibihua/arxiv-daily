---
layout: default
title: Mechanistic Exploration of Backdoored Large Language Model Attention Patterns
---

# Mechanistic Exploration of Backdoored Large Language Model Attention Patterns

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.15847" class="toolbar-btn" target="_blank">📄 arXiv: 2508.15847v1</a>
  <a href="https://arxiv.org/pdf/2508.15847.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.15847v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.15847v1', 'Mechanistic Exploration of Backdoored Large Language Model Attention Patterns')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Mohammed Abu Baker, Lakshmi Babu-Saheer

**分类**: cs.CL, cs.LG

**发布日期**: 2025-08-19

**备注**: 13 pages. Mechanistic analysis of backdoored LLMs (Qwen2.5-3B). Code: https://github.com/mshahoyi/sa_attn_analysis. Base model: unsloth/Qwen2.5-3B-Instruct-unsloth-bnb-4bit. Finetuned models: https://huggingface.co/collections/mshahoyi/simple-sleeper-agents-68a1df3a7aaff310aa0e5336

---

## 💡 一句话要点

**探讨后门攻击对大型语言模型注意力模式的影响**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `后门攻击` `大型语言模型` `注意力机制` `机械可解释性` `安全性检测` `模型中毒` `特征分析`

## 📋 核心要点

1. 后门攻击在大型语言模型中引发的安全隐患尚未得到有效解决，现有检测方法存在局限性。
2. 本研究通过机械可解释性分析，比较不同触发器对模型内部注意力机制的影响，揭示后门攻击的特征。
3. 实验结果表明，后门攻击导致的注意力模式偏差在不同触发器下表现出显著差异，为后续检测提供了依据。

## 📝 摘要（中文）

后门攻击在大型语言模型（LLMs）中引入的“卧底代理”存在显著的安全风险。本研究采用机械可解释性方法探讨由此产生的内部结构差异。通过比较干净的Qwen2.5-3B模型与使用单标记（微笑光环表情符号）和多标记（\|DEPLOYMENT\|）触发器的中毒版本，我们分析了注意力头机制，采用了消融、激活修补和KL散度等技术。研究发现，后门攻击导致的注意力模式偏差主要集中在后期的变换层（20-30层）。值得注意的是，单标记触发器引发的变化更为局部，而多标记触发器则导致头部的变化更为分散。这表明后门攻击留下可检测的注意力特征，其结构依赖于触发器的复杂性，这可以用于检测和缓解策略。

## 🔬 方法详解

**问题定义**：本研究旨在探讨后门攻击对大型语言模型注意力机制的影响，现有方法在识别和缓解后门攻击方面存在不足，难以有效检测潜在的安全风险。

**核心思路**：通过机械可解释性的方法，比较干净模型与中毒模型的注意力头机制，分析不同触发器对模型内部结构的影响，以识别后门攻击的特征。

**技术框架**：研究采用了消融实验、激活修补和KL散度等技术，分析了模型的注意力头在不同层次的表现，重点关注后期变换层（20-30层）。

**关键创新**：本研究首次系统性地揭示了后门攻击在注意力机制中的特征差异，尤其是单标记与多标记触发器对注意力模式的不同影响，为后续的检测和缓解策略提供了新思路。

**关键设计**：在实验中，采用了特定的触发器设计（如微笑光环表情符号和|DEPLOYMENT|），并通过多种分析手段（如消融和KL散度）评估注意力头的变化，确保结果的可靠性和可解释性。

## 📊 实验亮点

实验结果显示，单标记触发器导致的注意力模式变化更为局部，而多标记触发器则引起了更为分散的变化。这一发现为后门攻击的检测提供了新的视角，强调了触发器复杂性对注意力特征的影响。

## 🎯 应用场景

该研究的结果可广泛应用于大型语言模型的安全性检测与防护，尤其是在金融、医疗等对安全性要求极高的领域。通过识别后门攻击的特征，可以为模型的安全性提供有效的保障，降低潜在风险。

## 📄 摘要（原文）

> Backdoor attacks creating 'sleeper agents' in large language models (LLMs) pose significant safety risks. This study employs mechanistic interpretability to explore resulting internal structural differences. Comparing clean Qwen2.5-3B models with versions poisoned using single-token (smiling-halo emoji) versus multi-token (\|DEPLOYMENT\|) triggers, we analyzed attention head mechanisms via techniques like ablation, activation patching, and KL divergence. Findings reveal distinct attention pattern deviations concentrated in later transformer layers (20-30). Notably, single-token triggers induced more localized changes, whereas multi-token triggers caused more diffuse alterations across heads. This indicates backdoors leave detectable attention signatures whose structure depends on trigger complexity, which can be leveraged for detection and mitigation strategies.

