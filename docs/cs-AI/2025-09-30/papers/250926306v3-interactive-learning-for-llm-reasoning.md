---
layout: default
title: Interactive Learning for LLM Reasoning
---

# Interactive Learning for LLM Reasoning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.26306" class="toolbar-btn" target="_blank">📄 arXiv: 2509.26306v3</a>
  <a href="https://arxiv.org/pdf/2509.26306.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.26306v3" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.26306v3', 'Interactive Learning for LLM Reasoning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Hehai Lin, Shilei Cao, Sudong Wang, Haotian Wu, Minzhi Li, Linyi Yang, Juepeng Zheng, Chengwei Qin

**分类**: cs.AI

**发布日期**: 2025-09-30 (更新: 2025-10-02)

**备注**: The code is available at https://github.com/linhh29/Interactive-Learning-for-LLM-Reasoning

---

## 💡 一句话要点

**提出ILR框架，通过交互式学习提升LLM独立推理能力**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `多智能体学习` `交互式学习` `推理能力` `动态交互`

## 📋 核心要点

1. 现有方法在推理时需重新执行多智能体系统，与人类独立推理的认知不符，限制了LLM能力的迁移。
2. ILR框架通过动态交互和感知校准，使LLM在交互式学习后，能够独立解决问题，提升推理能力。
3. 实验表明，ILR在数学和编码基准测试中优于单智能体学习，最高提升5%，并增强了LLM的鲁棒性。

## 📝 摘要（中文）

现有的多智能体学习方法通过交互式训练环境来促进多个大型语言模型（LLM）之间的协作，从而构建更强大的多智能体系统（MAS）。然而，在推理过程中，它们需要重新执行MAS才能获得最终解决方案，这与人类通过与他人互动来增强推理能力并在未来独立解决问题的认知不同。为了研究多智能体交互是否可以增强LLM的独立问题解决能力，我们引入了ILR，一种用于MAS的新型协同学习框架，它集成了两个关键组件：动态交互和感知校准。具体来说，动态交互首先根据问题的难度和模型的能力自适应地选择合作或竞争策略。然后，LLM通过Idea3（思想共享、思想分析和思想融合）交换信息，这是一种旨在模仿人类讨论的创新交互范式，然后在得出各自的最终答案。在感知校准中，ILR采用群体相对策略优化（GRPO）来训练LLM，同时将一个LLM的奖励分布特征整合到另一个LLM的奖励函数中，从而增强多智能体交互的凝聚力。我们在两个不同规模的模型系列的三个LLM上验证了ILR，评估了五个数学基准和一个编码基准的性能。实验结果表明，ILR始终优于单智能体学习，与最强的基线相比，性能提升高达5%。我们进一步发现，Idea3可以增强更强大的LLM在多智能体推理过程中的鲁棒性，并且与纯粹的合作或竞争策略相比，动态交互类型可以促进多智能体学习。

## 🔬 方法详解

**问题定义**：现有方法，特别是多智能体学习方法，在提升LLM推理能力时，依赖于推理阶段的多智能体协作。这意味着在实际应用中，每次需要解决问题时，都需要重新构建和执行整个多智能体系统。这与人类的学习方式不同，人类可以通过与他人交流学习，最终独立解决问题。因此，如何让LLM通过交互式学习，提升其独立推理能力，是本文要解决的核心问题。

**核心思路**：ILR的核心思路是通过模拟人类的讨论和学习过程，让LLM在交互式环境中学习，并最终具备独立解决问题的能力。具体来说，ILR包含动态交互和感知校准两个关键组件。动态交互允许LLM根据问题难度和自身能力选择合作或竞争策略，而感知校准则通过群体相对策略优化，增强多智能体之间的协作凝聚力。

**技术框架**：ILR框架主要包含以下几个阶段：1) **动态交互选择**：根据问题难度和模型能力，自适应选择合作或竞争策略。2) **Idea3交互**：LLM之间通过Idea3（思想共享、思想分析和思想融合）进行信息交换，模拟人类讨论过程。3) **独立推理**：LLM基于交互信息，独立得出最终答案。4) **感知校准**：使用Group Relative Policy Optimization (GRPO) 训练LLM，将一个LLM的奖励分布特征整合到另一个LLM的奖励函数中。

**关键创新**：ILR的关键创新在于：1) **动态交互**：根据问题难度和模型能力自适应选择交互策略，更灵活有效。2) **Idea3交互范式**：模拟人类讨论过程，促进LLM之间的信息交换和知识融合。3) **感知校准**：通过GRPO增强多智能体交互的凝聚力，提升学习效果。与现有方法相比，ILR更注重提升LLM的独立推理能力，而非仅仅依赖于推理阶段的多智能体协作。

**关键设计**：Idea3交互范式包含三个阶段：思想共享（Idea Sharing）、思想分析（Idea Analysis）和思想融合（Idea Fusion）。在思想共享阶段，LLM分享各自的初步想法。在思想分析阶段，LLM分析彼此的想法，找出优点和不足。在思想融合阶段，LLM将彼此的想法融合，形成更完善的解决方案。GRPO通过调整奖励函数，使得LLM在训练过程中更加关注群体表现，从而增强多智能体之间的协作。

## 📊 实验亮点

实验结果表明，ILR在五个数学基准测试和一个编码基准测试中，均优于单智能体学习方法，最高提升达5%。此外，实验还发现，Idea3交互范式可以增强更强大的LLM在多智能体推理过程中的鲁棒性，并且动态交互类型可以促进多智能体学习，效果优于纯粹的合作或竞争策略。

## 🎯 应用场景

ILR框架可应用于各种需要LLM进行复杂推理和决策的场景，例如智能客服、金融分析、医疗诊断等。通过交互式学习，LLM可以更好地理解问题，并给出更准确、更可靠的答案。此外，ILR还可以用于提升LLM在特定领域的专业知识和技能，使其更好地服务于各行各业。

## 📄 摘要（原文）

> Existing multi-agent learning approaches have developed interactive training environments to explicitly promote collaboration among multiple Large Language Models (LLMs), thereby constructing stronger multi-agent systems (MAS). However, during inference, they require re-executing the MAS to obtain final solutions, which diverges from human cognition that individuals can enhance their reasoning capabilities through interactions with others and resolve questions independently in the future. To investigate whether multi-agent interaction can enhance LLMs' independent problem-solving ability, we introduce ILR, a novel co-learning framework for MAS that integrates two key components: Dynamic Interaction and Perception Calibration. Specifically, Dynamic Interaction first adaptively selects either cooperative or competitive strategies depending on question difficulty and model ability. LLMs then exchange information through Idea3 (Idea Sharing, Idea Analysis, and Idea Fusion), an innovative interaction paradigm designed to mimic human discussion, before deriving their respective final answers. In Perception Calibration, ILR employs Group Relative Policy Optimization (GRPO) to train LLMs while integrating one LLM's reward distribution characteristics into another's reward function, thereby enhancing the cohesion of multi-agent interactions. We validate ILR on three LLMs across two model families of varying scales, evaluating performance on five mathematical benchmarks and one coding benchmark. Experimental results show that ILR consistently outperforms single-agent learning, yielding an improvement of up to 5% over the strongest baseline. We further discover that Idea3 can enhance the robustness of stronger LLMs during multi-agent inference, and dynamic interaction types can boost multi-agent learning compared to pure cooperative or competitive strategies.

