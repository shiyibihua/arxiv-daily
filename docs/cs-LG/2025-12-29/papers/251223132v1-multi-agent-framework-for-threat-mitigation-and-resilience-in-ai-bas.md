---
layout: default
title: Multi-Agent Framework for Threat Mitigation and Resilience in AI-Based Systems
---

# Multi-Agent Framework for Threat Mitigation and Resilience in AI-Based Systems

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.23132" class="toolbar-btn" target="_blank">📄 arXiv: 2512.23132v1</a>
  <a href="https://arxiv.org/pdf/2512.23132.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.23132v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.23132v1', 'Multi-Agent Framework for Threat Mitigation and Resilience in AI-Based Systems')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Armstrong Foundjem, Lionel Nganyewou Tidjon, Leuson Da Silva, Foutse Khomh

**分类**: cs.CR, cs.LG, cs.MA

**发布日期**: 2025-12-29

**备注**: 56 pages, 18 Figures, 22 Tables, TOSEM

---

## 💡 一句话要点

**提出多智能体框架，用于缓解和增强人工智能系统的威胁抵御能力**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `机器学习安全` `威胁建模` `多智能体系统` `RAG系统` `大型语言模型` `知识图谱` `漏洞分析`

## 📋 核心要点

1. 现有网络安全方法缺乏针对机器学习模型（尤其是基础模型、多模态模型和RAG系统）的特定威胁建模。
2. 提出一种多智能体RAG系统，通过分析大量威胁数据，构建本体驱动的威胁图，关联TTP、漏洞和生命周期阶段。
3. 识别出商业LLM API模型窃取、参数记忆泄漏等未报告威胁，并揭示了主要TTP和高风险漏洞集群。

## 📝 摘要（中文）

机器学习正支撑着金融、医疗和关键基础设施中的基础模型，使其成为数据投毒、模型提取、提示注入、自动越狱和利用模型比较的偏好引导黑盒攻击的目标。更大的模型更容易受到内省驱动的越狱和跨模态操纵的影响。传统的网络安全缺乏针对基础模型、多模态和RAG系统的机器学习特定威胁建模。本研究旨在通过识别主要的TTP、漏洞和目标生命周期阶段来描述机器学习安全风险。我们从MITRE ATLAS（26个）、AI Incident Database（12个）和文献（55个）中提取了93个威胁，并分析了854个GitHub/Python存储库。一个多智能体RAG系统（ChatGPT-4o，温度0.4）挖掘了300多篇文章，构建了一个本体驱动的威胁图，将TTP、漏洞和阶段联系起来。我们识别出未报告的威胁，包括商业LLM API模型窃取、参数记忆泄漏和偏好引导的纯文本越狱。主要的TTP包括MASTERKEY风格的越狱、联邦投毒、扩散后门和偏好优化泄漏，主要影响预训练和推理。图分析揭示了具有较差补丁传播的库中的密集漏洞集群。结论是，自适应的、机器学习特定的安全框架，结合依赖卫生、威胁情报和监控，对于缓解整个机器学习生命周期中的供应链和推理风险至关重要。

## 🔬 方法详解

**问题定义**：论文旨在解决机器学习系统，特别是基于大型语言模型（LLM）的系统，在面对各种安全威胁时的脆弱性问题。现有的网络安全方法通常不足以应对机器学习模型特有的攻击方式，例如数据投毒、模型提取、提示注入和越狱攻击。这些攻击可能导致模型性能下降、敏感信息泄露甚至系统崩溃。

**核心思路**：论文的核心思路是构建一个多智能体框架，利用RAG（Retrieval-Augmented Generation）系统，从大量的威胁情报数据中提取、分析和关联威胁信息，从而构建一个全面的威胁图。该威胁图能够帮助安全专家识别潜在的攻击路径、漏洞和关键的攻击阶段，从而制定更有效的防御策略。

**技术框架**：该框架主要包含以下几个模块：1) **威胁数据收集模块**：从MITRE ATLAS、AI Incident Database和相关文献中收集威胁数据。2) **知识图谱构建模块**：利用多智能体RAG系统（ChatGPT-4o）从收集到的数据中提取实体（TTP、漏洞、阶段）和关系，构建本体驱动的威胁图。3) **威胁分析模块**：分析威胁图，识别主要的TTP、高风险漏洞集群和关键的攻击阶段。4) **安全策略生成模块**：基于威胁分析结果，生成针对性的安全策略，例如依赖项管理、威胁情报和监控。

**关键创新**：该论文的关键创新在于：1) **多智能体RAG系统**：利用多智能体系统自动化地从海量数据中提取和关联威胁信息，提高了威胁情报分析的效率和准确性。2) **本体驱动的威胁图**：构建了一个结构化的威胁知识库，能够清晰地展示威胁之间的关系和攻击路径。3) **识别未报告的威胁**：通过分析，识别出商业LLM API模型窃取、参数记忆泄漏等新型威胁。

**关键设计**：RAG系统使用ChatGPT-4o作为核心引擎，温度参数设置为0.4，以平衡生成结果的创造性和准确性。威胁图的构建基于预定义的本体，该本体定义了威胁相关的实体类型（TTP、漏洞、阶段）和关系类型。论文还重点关注了依赖项管理，强调了及时更新和修补漏洞的重要性。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.23132v1/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.23132v1/x2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.23132v1/x3.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

实验结果表明，该框架能够识别出未报告的威胁，例如商业LLM API模型窃取和参数记忆泄漏。通过分析威胁图，发现主要的TTP包括MASTERKEY风格的越狱、联邦投毒和扩散后门。此外，还识别出具有较差补丁传播的库中的密集漏洞集群，为安全专家提供了有价值的威胁情报。

## 🎯 应用场景

该研究成果可应用于提高人工智能系统的安全性，尤其是在金融、医疗和关键基础设施等领域。通过构建全面的威胁图和制定针对性的安全策略，可以有效降低机器学习模型遭受攻击的风险，保护敏感数据和系统安全。该研究还有助于开发更安全的LLM应用，并促进人工智能技术的可靠应用。

## 📄 摘要（原文）

> Machine learning (ML) underpins foundation models in finance, healthcare, and critical infrastructure, making them targets for data poisoning, model extraction, prompt injection, automated jailbreaking, and preference-guided black-box attacks that exploit model comparisons. Larger models can be more vulnerable to introspection-driven jailbreaks and cross-modal manipulation. Traditional cybersecurity lacks ML-specific threat modeling for foundation, multimodal, and RAG systems. Objective: Characterize ML security risks by identifying dominant TTPs, vulnerabilities, and targeted lifecycle stages. Methods: We extract 93 threats from MITRE ATLAS (26), AI Incident Database (12), and literature (55), and analyze 854 GitHub/Python repositories. A multi-agent RAG system (ChatGPT-4o, temp 0.4) mines 300+ articles to build an ontology-driven threat graph linking TTPs, vulnerabilities, and stages. Results: We identify unreported threats including commercial LLM API model stealing, parameter memorization leakage, and preference-guided text-only jailbreaks. Dominant TTPs include MASTERKEY-style jailbreaking, federated poisoning, diffusion backdoors, and preference optimization leakage, mainly impacting pre-training and inference. Graph analysis reveals dense vulnerability clusters in libraries with poor patch propagation. Conclusion: Adaptive, ML-specific security frameworks, combining dependency hygiene, threat intelligence, and monitoring, are essential to mitigate supply-chain and inference risks across the ML lifecycle.

