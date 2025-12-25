---
layout: default
title: "Casting a SPELL: Sentence Pairing Exploration for LLM Limitation-breaking"
---

# Casting a SPELL: Sentence Pairing Exploration for LLM Limitation-breaking

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.21236" class="toolbar-btn" target="_blank">📄 arXiv: 2512.21236v1</a>
  <a href="https://arxiv.org/pdf/2512.21236.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.21236v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.21236v1', 'Casting a SPELL: Sentence Pairing Exploration for LLM Limitation-breaking')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yifan Huang, Xiaojun Jia, Wenbo Guo, Yuqiang Sun, Yihao Huang, Chong Wang, Yang Liu

**分类**: cs.CR, cs.AI, cs.SE

**发布日期**: 2025-12-24

**备注**: Accepted to FSE 2026

---

## 💡 一句话要点

**SPELL：通过句子配对探索LLM在恶意代码生成中的安全漏洞**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `恶意代码生成` `安全对齐` `越狱攻击` `提示工程`

## 📋 核心要点

1. 现有研究对LLM在恶意代码生成方面的安全漏洞探索不足，缺乏针对性的测试框架。
2. SPELL框架通过时分选择策略，智能组合句子构建越狱提示，探索并利用攻击模式。
3. 实验表明SPELL能有效攻击GPT-4.1等代码模型，并在实际AI开发工具中生成恶意代码。

## 📝 摘要（中文）

大型语言模型（LLMs）通过AI辅助编码工具彻底改变了软件开发，使编程经验有限的开发人员能够创建复杂的应用程序。然而，这种可访问性也延伸到了恶意行为者，他们可能利用这些强大的工具来生成有害软件。现有的越狱研究主要侧重于针对LLM的一般攻击场景，对恶意代码生成作为越狱目标的研究有限。为了解决这一差距，我们提出了SPELL，这是一个全面的测试框架，专门用于评估恶意代码生成中安全对齐的弱点。我们的框架采用了一种时分选择策略，通过智能地组合来自先验知识数据集的句子来系统地构建越狱提示，从而平衡了对新攻击模式的探索和对成功技术的利用。对三种先进代码模型（GPT-4.1、Claude-3.5和Qwen2.5-Coder）的广泛评估表明了SPELL的有效性，在八个恶意代码类别中分别实现了83.75%、19.38%和68.12%的攻击成功率。生成的提示成功地在Cursor等实际AI开发工具中生成了恶意代码，并且最先进的检测系统确认输出为恶意的比率超过73%。这些发现揭示了当前LLM实现中的重大安全漏洞，并为改进代码生成应用中的AI安全对齐提供了宝贵的见解。

## 🔬 方法详解

**问题定义**：论文旨在解决大型语言模型（LLMs）在恶意代码生成方面的安全对齐问题。现有的越狱研究主要关注通用攻击，缺乏对恶意代码生成这一特定场景的深入研究和有效评估方法。这使得LLMs容易被恶意利用，生成有害软件，对软件开发生态构成威胁。

**核心思路**：论文的核心思路是构建一个名为SPELL的测试框架，该框架通过系统地生成和评估越狱提示，来揭示LLMs在恶意代码生成方面的安全漏洞。SPELL采用时分选择策略，平衡了对新攻击模式的探索和对成功攻击技术的利用，从而更有效地发现LLMs的弱点。

**技术框架**：SPELL框架主要包含以下几个阶段：1) **先验知识数据集构建**：收集包含各种攻击意图的句子，构建知识库。2) **时分选择策略**：将时间划分为多个阶段，在不同阶段侧重于探索新的攻击模式或利用已知的有效模式。3) **提示生成**：根据时分选择策略，从知识库中选择句子，组合成越狱提示。4) **攻击评估**：将生成的提示输入到目标LLM，评估其生成恶意代码的成功率。5) **恶意代码检测**：使用现有的恶意代码检测系统，验证生成的代码是否确实具有恶意性。

**关键创新**：SPELL的关键创新在于其针对恶意代码生成场景设计的时分选择策略。该策略能够有效地平衡探索和利用，从而更全面地发现LLMs的安全漏洞。与传统的随机或基于规则的提示生成方法相比，SPELL能够更智能地生成有效的越狱提示。

**关键设计**：SPELL的时分选择策略是其核心设计。具体而言，在探索阶段，SPELL会随机选择句子进行组合，以发现新的攻击模式。在利用阶段，SPELL会优先选择之前成功生成恶意代码的句子，并尝试对其进行变异，以提高攻击成功率。此外，SPELL还使用了多种提示工程技巧，例如使用角色扮演、添加约束条件等，来提高提示的有效性。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.21236v1/figures/overview.png" alt="fig_0" loading="lazy">
</figure>
</div>

## 📊 实验亮点

SPELL框架在GPT-4.1、Claude-3.5和Qwen2.5-Coder三个先进代码模型上进行了广泛评估，分别实现了83.75%、19.38%和68.12%的攻击成功率。生成的提示成功地在Cursor等实际AI开发工具中生成了恶意代码，并且最先进的检测系统确认输出为恶意的比率超过73%。这些结果表明SPELL能够有效地揭示LLM在恶意代码生成方面的安全漏洞。

## 🎯 应用场景

该研究成果可应用于提升AI辅助代码工具的安全性，例如，通过SPELL框架发现的安全漏洞可以用于训练更鲁棒的LLM，从而防止恶意代码的生成。此外，该研究还可以帮助安全研究人员更好地理解LLM的安全风险，并开发更有效的防御机制。该研究对于保障软件开发生态的安全具有重要意义。

## 📄 摘要（原文）

> Large language models (LLMs) have revolutionized software development through AI-assisted coding tools, enabling developers with limited programming expertise to create sophisticated applications. However, this accessibility extends to malicious actors who may exploit these powerful tools to generate harmful software. Existing jailbreaking research primarily focuses on general attack scenarios against LLMs, with limited exploration of malicious code generation as a jailbreak target. To address this gap, we propose SPELL, a comprehensive testing framework specifically designed to evaluate the weakness of security alignment in malicious code generation. Our framework employs a time-division selection strategy that systematically constructs jailbreaking prompts by intelligently combining sentences from a prior knowledge dataset, balancing exploration of novel attack patterns with exploitation of successful techniques. Extensive evaluation across three advanced code models (GPT-4.1, Claude-3.5, and Qwen2.5-Coder) demonstrates SPELL's effectiveness, achieving attack success rates of 83.75%, 19.38%, and 68.12% respectively across eight malicious code categories. The generated prompts successfully produce malicious code in real-world AI development tools such as Cursor, with outputs confirmed as malicious by state-of-the-art detection systems at rates exceeding 73%. These findings reveal significant security gaps in current LLM implementations and provide valuable insights for improving AI safety alignment in code generation applications.

