---
layout: default
title: A Systematic Review of Poisoning Attacks Against Large Language Models
---

# A Systematic Review of Poisoning Attacks Against Large Language Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.06518" class="toolbar-btn" target="_blank">📄 arXiv: 2506.06518v1</a>
  <a href="https://arxiv.org/pdf/2506.06518.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.06518v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.06518v1', 'A Systematic Review of Poisoning Attacks Against Large Language Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Neil Fendley, Edward W. Staley, Joshua Carney, William Redman, Marie Chau, Nathan Drenkow

**分类**: cs.CR, cs.LG

**发布日期**: 2025-06-06

**备注**: 28 Pages including number

---

## 💡 一句话要点

**提出系统性框架以应对大型语言模型的中毒攻击问题**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `中毒攻击` `安全风险` `系统回顾` `威胁模型` `自然语言处理` `信息安全`

## 📋 核心要点

1. 现有文献中的LLM中毒攻击框架和术语不够完善，无法适应生成性模型的特性。
2. 提出一个全面的中毒威胁模型，能够对多种LLM中毒攻击进行分类和分析。
3. 通过对已发表文献的系统回顾，明确了中毒攻击的安全隐患和术语的一致性问题。

## 📝 摘要（中文）

随着预训练大型语言模型（LLMs）及其训练数据集的广泛应用，关于其安全风险的关注显著增加。其中，中毒攻击是一种安全威胁，攻击者通过修改LLM训练过程中的某些部分，使得模型产生恶意行为。当前针对LLM中毒攻击的框架和术语主要源自早期的分类中毒文献，无法完全适应生成性LLM的环境。本文系统回顾了已发表的LLM中毒攻击，旨在澄清安全隐患并解决文献中的术语不一致问题。我们提出了一个全面的中毒威胁模型，以分类各种LLM中毒攻击，并定义了四种中毒攻击规格和六个中毒度量指标，以衡量攻击的关键特征。

## 🔬 方法详解

**问题定义**：本文旨在解决当前LLM中毒攻击研究中框架和术语不一致的问题，现有方法无法有效应对生成性模型的特性。

**核心思路**：提出一个全面的中毒威胁模型，涵盖四种中毒攻击规格和六个中毒度量指标，以便更好地理解和分类LLM中毒攻击。

**技术框架**：该框架包括对中毒攻击的四个关键维度的讨论：概念中毒、隐蔽中毒、持久中毒和针对特定任务的中毒，旨在全面分析当前的安全风险。

**关键创新**：最重要的创新在于提出了适用于生成性LLM的中毒威胁模型，填补了现有文献的空白，并提供了系统化的分类方法。

**关键设计**：模型中定义的四种中毒攻击规格和六个度量指标，能够有效衡量攻击的特征和影响，确保对中毒攻击的全面理解。

## 📊 实验亮点

通过系统回顾，本文明确了LLM中毒攻击的四个关键维度，并提出了一个全面的中毒威胁模型。这一模型不仅有助于分类和理解中毒攻击，还为未来的研究提供了重要的参考框架。

## 🎯 应用场景

该研究的潜在应用领域包括自然语言处理、信息安全和模型训练等。通过提供一个系统化的中毒攻击框架，研究者和开发者可以更好地识别和防范LLM中的安全风险，从而提升模型的安全性和可靠性。

## 📄 摘要（原文）

> With the widespread availability of pretrained Large Language Models (LLMs) and their training datasets, concerns about the security risks associated with their usage has increased significantly. One of these security risks is the threat of LLM poisoning attacks where an attacker modifies some part of the LLM training process to cause the LLM to behave in a malicious way. As an emerging area of research, the current frameworks and terminology for LLM poisoning attacks are derived from earlier classification poisoning literature and are not fully equipped for generative LLM settings. We conduct a systematic review of published LLM poisoning attacks to clarify the security implications and address inconsistencies in terminology across the literature. We propose a comprehensive poisoning threat model applicable to categorize a wide range of LLM poisoning attacks. The poisoning threat model includes four poisoning attack specifications that define the logistics and manipulation strategies of an attack as well as six poisoning metrics used to measure key characteristics of an attack. Under our proposed framework, we organize our discussion of published LLM poisoning literature along four critical dimensions of LLM poisoning attacks: concept poisons, stealthy poisons, persistent poisons, and poisons for unique tasks, to better understand the current landscape of security risks.

