---
layout: default
title: A Call to Action for a Secure-by-Design Generative AI Paradigm
---

# A Call to Action for a Secure-by-Design Generative AI Paradigm

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.00451" class="toolbar-btn" target="_blank">📄 arXiv: 2510.00451v1</a>
  <a href="https://arxiv.org/pdf/2510.00451.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.00451v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2510.00451v1', 'A Call to Action for a Secure-by-Design Generative AI Paradigm')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Dalal Alharthi, Ivan Roberto Kawaminami Garcia

**分类**: cs.CR, cs.AI, cs.LG, cs.MA

**发布日期**: 2025-10-01

---

## 💡 一句话要点

**提出PromptShield框架，通过本体驱动确保生成式AI的确定性和安全性**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `生成式AI安全` `提示注入攻击` `本体驱动` `语义验证` `安全设计` `大型语言模型` `确定性提示工程`

## 📋 核心要点

1. 大型语言模型易受提示注入等攻击，现有方法难以有效应对这些安全威胁。
2. PromptShield通过本体驱动的语义验证标准化用户输入，消除歧义，从而减轻对抗性操纵。
3. 实验表明，PromptShield显著提升了模型安全性和性能，在云日志分析中F1分数达到约94%。

## 📝 摘要（中文）

大型语言模型（LLM）的应用日益广泛，但其易受提示注入和其他对抗性攻击的脆弱性仍然是一个关键问题。本文倡导一种“安全设计”的AI范式，主动缓解LLM的漏洞并提高性能。为此，我们引入了PromptShield，这是一个本体驱动的框架，旨在确保确定性和安全的提示交互。它通过语义验证标准化用户输入，消除歧义并减轻对抗性操纵。为了评估PromptShield的安全性和性能，我们在一个基于代理的系统中进行了一项实验，该系统分析了Amazon Web Services（AWS）中的云日志，其中包含与恶意活动和异常相关的493个不同事件。通过模拟提示注入攻击并评估部署PromptShield的影响，我们的结果表明模型安全性和性能得到了显著提高，实现了约94%的精确率、召回率和F1分数。值得注意的是，基于本体的框架不仅减轻了对抗性威胁，还提高了系统的整体性能和可靠性。此外，PromptShield的模块化和适应性设计确保了其在云安全之外的适用性，使其成为保护各个领域生成式AI应用程序的强大解决方案。通过为AI安全标准奠定基础并为未来的政策制定提供信息，这项工作激发了关于确定性提示工程和基于本体的验证在确保LLM在高风险环境中安全和负责任部署中的关键作用的重要对话。

## 🔬 方法详解

**问题定义**：论文旨在解决大型语言模型（LLM）在面对提示注入等对抗性攻击时存在的安全漏洞问题。现有方法通常缺乏对用户输入的有效验证和标准化，导致LLM容易受到恶意操纵，从而影响其性能和可靠性。

**核心思路**：论文的核心思路是采用“安全设计”的AI范式，通过在LLM交互过程中引入本体驱动的语义验证机制，实现对用户输入的标准化和确定性控制。PromptShield框架旨在消除用户输入的歧义，减轻对抗性操纵，从而提高LLM的安全性和性能。

**技术框架**：PromptShield框架包含以下主要模块：1) 用户输入接收模块，负责接收用户的提示信息；2) 本体驱动的语义验证模块，利用预定义的本体知识库对用户输入进行语义分析和验证，确保输入的合法性和一致性；3) 提示标准化模块，将验证后的用户输入转换为符合LLM要求的标准格式；4) LLM推理模块，利用标准化后的提示信息进行推理和生成；5) 输出结果验证模块，对LLM的输出结果进行验证，确保其符合预期。

**关键创新**：PromptShield的关键创新在于其采用本体驱动的语义验证方法，实现了对用户输入的细粒度控制和标准化。与传统的基于规则或模式匹配的方法相比，PromptShield能够更好地理解用户输入的语义信息，从而更有效地识别和防御对抗性攻击。此外，PromptShield的模块化设计使其易于扩展和定制，可以应用于不同的LLM和应用场景。

**关键设计**：PromptShield的关键设计包括：1) 本体知识库的构建，需要根据具体的应用领域定义相关的概念、关系和规则；2) 语义验证算法的设计，需要考虑验证的准确性和效率；3) 提示标准化策略的制定，需要确保标准化后的提示信息能够被LLM正确理解和处理。论文中未明确给出具体的参数设置、损失函数或网络结构等技术细节，这部分内容可能属于商业机密或未公开的研究成果。

## 📊 实验亮点

实验结果表明，在模拟提示注入攻击的场景下，部署PromptShield后，基于代理的云日志分析系统在精确率、召回率和F1分数上均达到了约94%，相较于未部署PromptShield的系统，安全性和性能得到了显著提升。这验证了PromptShield在减轻对抗性威胁方面的有效性。

## 🎯 应用场景

PromptShield框架具有广泛的应用前景，可用于保护各种生成式AI应用，例如智能客服、内容生成、代码生成等。尤其在高风险领域，如金融、医疗等，PromptShield可以有效防止恶意攻击，确保AI系统的安全可靠运行。该研究为AI安全标准制定和政策发展提供了重要参考。

## 📄 摘要（原文）

> Large language models have gained widespread prominence, yet their vulnerability to prompt injection and other adversarial attacks remains a critical concern. This paper argues for a security-by-design AI paradigm that proactively mitigates LLM vulnerabilities while enhancing performance. To achieve this, we introduce PromptShield, an ontology-driven framework that ensures deterministic and secure prompt interactions. It standardizes user inputs through semantic validation, eliminating ambiguity and mitigating adversarial manipulation. To assess PromptShield's security and performance capabilities, we conducted an experiment on an agent-based system to analyze cloud logs within Amazon Web Services (AWS), containing 493 distinct events related to malicious activities and anomalies. By simulating prompt injection attacks and assessing the impact of deploying PromptShield, our results demonstrate a significant improvement in model security and performance, achieving precision, recall, and F1 scores of approximately 94%. Notably, the ontology-based framework not only mitigates adversarial threats but also enhances the overall performance and reliability of the system. Furthermore, PromptShield's modular and adaptable design ensures its applicability beyond cloud security, making it a robust solution for safeguarding generative AI applications across various domains. By laying the groundwork for AI safety standards and informing future policy development, this work stimulates a crucial dialogue on the pivotal role of deterministic prompt engineering and ontology-based validation in ensuring the safe and responsible deployment of LLMs in high-stakes environments.

