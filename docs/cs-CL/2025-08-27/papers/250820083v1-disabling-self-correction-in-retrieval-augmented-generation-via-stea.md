---
layout: default
title: Disabling Self-Correction in Retrieval-Augmented Generation via Stealthy Retriever Poisoning
---

# Disabling Self-Correction in Retrieval-Augmented Generation via Stealthy Retriever Poisoning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.20083" class="toolbar-btn" target="_blank">📄 arXiv: 2508.20083v1</a>
  <a href="https://arxiv.org/pdf/2508.20083.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.20083v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.20083v1', 'Disabling Self-Correction in Retrieval-Augmented Generation via Stealthy Retriever Poisoning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yanbo Dai, Zhenlan Ji, Zongjie Li, Kuan Li, Shuai Wang

**分类**: cs.CR, cs.CL

**发布日期**: 2025-08-27

---

## 💡 一句话要点

**提出DisarmRAG以解决RAG系统自我纠错能力的挑战**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `检索增强生成` `自我纠错能力` `毒化攻击` `对比学习` `模型编辑` `安全性测试` `对抗性攻击`

## 📋 核心要点

1. 现有RAG系统的自我纠错能力（SCA）使得攻击者难以通过毒化知识库实现预期的输出。
2. 本文提出DisarmRAG，通过破坏检索器本身来抑制SCA，从而实现攻击者选择的输出。
3. 实验结果表明，DisarmRAG在多种防御提示下的攻击成功率超过90%，显示出其有效性和隐蔽性。

## 📝 摘要（中文）

检索增强生成（RAG）已成为提高大型语言模型（LLMs）可靠性的标准方法。以往研究表明，通过毒化知识库可以误导RAG系统生成攻击者选择的输出。然而，本论文发现现代LLMs的强大自我纠错能力（SCA）可以减轻此类攻击。为此，本文提出了一种新的毒化范式DisarmRAG，旨在破坏检索器本身以抑制SCA并强制生成攻击者选择的输出。通过对检索器进行局部和隐蔽的编辑，确保其仅对特定受害查询返回恶意指令，同时保持良性检索行为。实验结果显示，DisarmRAG在六个LLMs和三个QA基准上表现出色，攻击成功率超过90%。

## 🔬 方法详解

**问题定义**：本文旨在解决RAG系统中自我纠错能力（SCA）对攻击者的防御效果。现有的毒化方法主要针对知识库，未能有效应对SCA的挑战。

**核心思路**：论文提出DisarmRAG，通过直接毒化检索器来抑制SCA，使得攻击者能够嵌入恶意指令，从而绕过自我纠错机制。

**技术框架**：整体架构包括毒化检索器的对比学习模型编辑技术，确保检索器在特定查询下返回恶意指令，同时保持正常的检索行为。该框架还包含迭代共同优化机制，以发现能够绕过防御的强健指令。

**关键创新**：DisarmRAG的创新在于其针对检索器的毒化方法，与以往主要针对知识库的毒化策略本质不同，能够有效抑制SCA。

**关键设计**：在模型编辑过程中，采用对比学习方法进行局部编辑，确保恶意指令仅在特定上下文中生效，同时设计了适应性强的损失函数以优化指令的鲁棒性。

## 📊 实验亮点

实验结果显示，DisarmRAG在六个大型语言模型上实现了近乎完美的恶意指令检索，攻击成功率在多种防御提示下超过90%。此外，经过编辑的检索器在多种检测方法下仍保持隐蔽性，突显了其有效性。

## 🎯 应用场景

该研究的潜在应用领域包括安全性测试、恶意软件检测和对抗性攻击防御等。通过深入理解RAG系统的脆弱性，可以为未来的AI系统设计更强的防御机制，提升其安全性和可靠性。

## 📄 摘要（原文）

> Retrieval-Augmented Generation (RAG) has become a standard approach for improving the reliability of large language models (LLMs). Prior work demonstrates the vulnerability of RAG systems by misleading them into generating attacker-chosen outputs through poisoning the knowledge base. However, this paper uncovers that such attacks could be mitigated by the strong \textit{self-correction ability (SCA)} of modern LLMs, which can reject false context once properly configured. This SCA poses a significant challenge for attackers aiming to manipulate RAG systems.
>   In contrast to previous poisoning methods, which primarily target the knowledge base, we introduce \textsc{DisarmRAG}, a new poisoning paradigm that compromises the retriever itself to suppress the SCA and enforce attacker-chosen outputs. This compromisation enables the attacker to straightforwardly embed anti-SCA instructions into the context provided to the generator, thereby bypassing the SCA. To this end, we present a contrastive-learning-based model editing technique that performs localized and stealthy edits, ensuring the retriever returns a malicious instruction only for specific victim queries while preserving benign retrieval behavior. To further strengthen the attack, we design an iterative co-optimization framework that automatically discovers robust instructions capable of bypassing prompt-based defenses. We extensively evaluate DisarmRAG across six LLMs and three QA benchmarks. Our results show near-perfect retrieval of malicious instructions, which successfully suppress SCA and achieve attack success rates exceeding 90\% under diverse defensive prompts. Also, the edited retriever remains stealthy under several detection methods, highlighting the urgent need for retriever-centric defenses.

