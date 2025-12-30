---
layout: default
title: "Single LLM Debate, MoLaCE: Mixture of Latent Concept Experts Against Confirmation Bias"
---

# Single LLM Debate, MoLaCE: Mixture of Latent Concept Experts Against Confirmation Bias

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.23518" class="toolbar-btn" target="_blank">📄 arXiv: 2512.23518v1</a>
  <a href="https://arxiv.org/pdf/2512.23518.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.23518v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.23518v1', 'Single LLM Debate, MoLaCE: Mixture of Latent Concept Experts Against Confirmation Bias')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Hazel Kim, Philip Torr

**分类**: cs.CL

**发布日期**: 2025-12-29

---

## 💡 一句话要点

**提出MoLaCE，通过混合潜在概念专家解决LLM中的确认偏差问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `确认偏差` `多智能体辩论` `潜在概念` `模型鲁棒性`

## 📋 核心要点

1. 大型语言模型容易受到确认偏差的影响，即倾向于支持与初始假设一致的信息，忽略其他可能性。
2. MoLaCE通过混合多个“潜在概念专家”来解决此问题，每个专家代表不同的激活强度，从而影响模型响应。
3. 实验表明，MoLaCE能有效减少确认偏差，提高模型鲁棒性，且计算成本远低于多智能体辩论。

## 📝 摘要（中文）

大型语言模型（LLMs）极易受到输入确认偏差的影响。当提示暗示了偏好的答案时，模型通常会强化这种偏差，而不是探索替代方案。这种现象尚未得到充分研究，但它已经在基础模型中造成了危害，并且在多智能体辩论中构成了更大的风险，在多智能体辩论中，回声室效应会强化偏差而不是纠正偏差。我们引入了潜在概念专家混合（MoLaCE），这是一个轻量级的推理时框架，通过混合实例化为不同激活强度的专家来解决确认偏差，这些专家作用于塑造模型响应的潜在概念。我们的关键见解是，由于语言的组合性质，不同措辞的提示以提示特定的方式重新加权潜在概念，从而影响事实的正确性，因此不能将单个固定的干预措施普遍应用于所有输入。这种设计使单个LLM能够在内部模拟辩论的好处，同时保持计算效率和可扩展性。它还可以集成到多智能体辩论框架中，以实现视角多样化并减少相关的错误。我们通过实验表明，它始终如一地减少了确认偏差，提高了鲁棒性，并且在仅需少量计算的情况下匹配或超过了多智能体辩论。

## 🔬 方法详解

**问题定义**：论文旨在解决大型语言模型（LLMs）中普遍存在的确认偏差问题。当用户提供的prompt带有倾向性时，LLM往往会强化这种偏差，而无法给出客观、全面的回答。现有的多智能体辩论方法虽然可以缓解这个问题，但计算成本高昂，难以扩展。

**核心思路**：论文的核心思想是，利用语言的组合性质，不同措辞的prompt会以不同的方式激活LLM内部的“潜在概念”。通过混合这些潜在概念的专家，可以模拟多智能体辩论的效果，从而减少确认偏差。MoLaCE的关键在于，它不是采用固定的干预措施，而是根据不同的prompt动态调整潜在概念的权重。

**技术框架**：MoLaCE框架主要包含以下几个步骤：1) 提取prompt中的潜在概念；2) 为每个潜在概念实例化一个“专家”，每个专家代表不同的激活强度；3) 根据prompt的特性，动态调整每个专家的权重；4) 将所有专家的输出混合，得到最终的答案。这个过程在单个LLM内部完成，无需多个LLM之间的交互。

**关键创新**：MoLaCE最重要的创新点在于，它将多智能体辩论的思想融入到单个LLM中，通过混合潜在概念专家来模拟辩论过程。与传统的多智能体辩论方法相比，MoLaCE大大降低了计算成本，提高了效率。此外，MoLaCE能够根据不同的prompt动态调整潜在概念的权重，从而更好地适应不同的输入。

**关键设计**：MoLaCE的关键设计包括：1) 如何提取prompt中的潜在概念（具体方法未知）；2) 如何定义和实例化“专家”（具体实现未知）；3) 如何根据prompt的特性动态调整专家的权重（具体算法未知）；4) 如何混合不同专家的输出（例如，加权平均）。论文中可能使用了特定的损失函数来训练MoLaCE，以鼓励模型学习到更客观、全面的知识。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.23518v1/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.23518v1/figures/latent_corr_phi.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.23518v1/figures/alpha_layers_llama.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

实验结果表明，MoLaCE能够显著减少LLM中的确认偏差，提高模型在各种任务上的鲁棒性。在某些任务上，MoLaCE的性能甚至超过了传统的多智能体辩论方法，同时计算成本大大降低。具体的性能数据和提升幅度在论文中详细给出（具体数值未知）。

## 🎯 应用场景

MoLaCE可应用于各种需要减少确认偏差的场景，例如问答系统、搜索引擎、内容生成等。通过提高LLM的客观性和鲁棒性，MoLaCE可以帮助用户获取更准确、全面的信息，避免受到误导。未来，MoLaCE还可以与其他技术结合，例如知识图谱、信息检索等，进一步提升LLM的性能。

## 📄 摘要（原文）

> Large language models (LLMs) are highly vulnerable to input confirmation bias. When a prompt implies a preferred answer, models often reinforce that bias rather than explore alternatives. This phenomenon remains underexplored, yet it is already harmful in base models and poses an even greater risk in multi-agent debate, where echo chambers reinforce bias instead of correction. We introduce Mixture of Latent Concept Experts (MoLaCE), a lightweight inference-time framework that addresses confirmation bias by mixing experts instantiated as different activation strengths over latent concepts that shape model responses. Our key insight is that, due to the compositional nature of language, differently phrased prompts reweight latent concepts in prompt-specific ways that affect factual correctness, so no single fixed intervention can be applied universally across inputs. This design enables a single LLM to emulate the benefits of debate internally while remaining computationally efficient and scalable. It can also be integrated into multi-agent debate frameworks to diversify perspectives and reduce correlated errors. We empirically show that it consistently reduces confirmation bias, improves robustness, and matches or surpasses multi-agent debate while requiring only a fraction of the computation.

