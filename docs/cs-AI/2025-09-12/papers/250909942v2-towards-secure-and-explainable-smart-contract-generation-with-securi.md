---
layout: default
title: Towards Secure and Explainable Smart Contract Generation with Security-Aware Group Relative Policy Optimization
---

# Towards Secure and Explainable Smart Contract Generation with Security-Aware Group Relative Policy Optimization

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.09942" class="toolbar-btn" target="_blank">📄 arXiv: 2509.09942v2</a>
  <a href="https://arxiv.org/pdf/2509.09942.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.09942v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.09942v2', 'Towards Secure and Explainable Smart Contract Generation with Security-Aware Group Relative Policy Optimization')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Lei Yu, Jingyuan Zhang, Xin Wang, Jiajia Ma, Li Yang, Fengjun Zhang

**分类**: cs.CR, cs.AI, cs.SE

**发布日期**: 2025-09-12 (更新: 2025-10-12)

---

## 💡 一句话要点

**提出SmartCoder-R1，通过安全感知强化学习提升智能合约生成安全性和可解释性。**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `智能合约生成` `大型语言模型` `安全漏洞` `强化学习` `可解释性` `安全感知` `策略优化`

## 📋 核心要点

1. 现有大型语言模型在智能合约生成中缺乏透明推理，导致生成的代码存在严重安全漏洞，易造成经济损失。
2. SmartCoder-R1通过持续预训练、长链思维监督微调和安全感知组相对策略优化，提升智能合约生成安全性和可解释性。
3. 实验表明，SmartCoder-R1在多个关键指标上超越现有技术，FullRate指标比最强基线DeepSeek-R1相对提高了45.79%。

## 📝 摘要（中文）

智能合约自动化管理高价值资产，但漏洞可能导致灾难性的经济损失。大型语言模型(LLMs)在此问题上存在双重挑战：缺乏透明的推理过程，如同“黑盒”；生成代码存在严重的安全漏洞。为解决这些问题，我们提出了SmartCoder-R1（基于Qwen2.5-Coder-7B），一个用于安全且可解释的智能合约生成的新框架。它首先进行持续预训练(CPT)以专门化模型。然后，我们在7,998个专家验证的推理和代码样本上应用长链思维监督微调(L-CoT SFT)，以训练模型模仿人类安全分析。最后，为了直接缓解漏洞，我们采用安全感知组相对策略优化(S-GRPO)，这是一个强化学习阶段，通过优化编译成功、安全合规性和格式正确性的加权奖励信号来改进生成策略。在包含756个真实世界函数的基准测试中，与17个基线相比，SmartCoder-R1建立了新的技术水平，在五个关键指标上取得了最佳性能：ComPass为87.70%，VulRate为8.60%，SafeAval为80.16%，FuncRate为53.84%，FullRate为50.53%。这个FullRate比最强的基线DeepSeek-R1相对提高了45.79%。至关重要的是，其生成的推理在人工评估中也表现出色，在功能性(82.7%)、安全性(85.3%)和清晰度(90.7%)方面获得了高质量的评分。

## 🔬 方法详解

**问题定义**：论文旨在解决大型语言模型（LLMs）在智能合约生成中存在的安全漏洞和缺乏可解释性的问题。现有方法生成的智能合约代码容易出现安全漏洞，且LLM的推理过程不透明，难以审计和验证。

**核心思路**：论文的核心思路是通过结合监督学习和强化学习，训练一个能够生成安全、可解释的智能合约代码的模型。具体来说，首先通过监督学习模仿人类专家的安全分析过程，然后通过强化学习优化生成策略，直接降低代码中的漏洞。

**技术框架**：SmartCoder-R1框架包含三个主要阶段：
1. **持续预训练 (CPT)**：在Qwen2.5-Coder-7B模型基础上进行持续预训练，使其更适应智能合约代码的生成任务。
2. **长链思维监督微调 (L-CoT SFT)**：使用专家验证的推理和代码样本，训练模型模仿人类的安全分析过程，生成包含推理过程的代码。
3. **安全感知组相对策略优化 (S-GRPO)**：使用强化学习，根据编译成功、安全合规性和格式正确性等指标，优化模型的生成策略。

**关键创新**：论文的关键创新在于提出了安全感知组相对策略优化（S-GRPO）方法。S-GRPO通过强化学习直接优化智能合约的安全性，与传统的监督学习方法相比，能够更有效地降低代码中的漏洞。此外，L-CoT SFT 使得模型生成代码的同时，也输出了推理过程，增强了可解释性。

**关键设计**：S-GRPO的关键设计在于奖励函数的设计，奖励函数综合考虑了编译成功、安全合规性和格式正确性三个方面。具体来说，编译成功保证了代码的基本可用性，安全合规性通过静态分析工具检测代码中的漏洞，格式正确性则保证了代码的可读性。通过对这三个方面进行加权，S-GRPO能够有效地引导模型生成高质量的智能合约代码。具体的权重设置未知。

## 📊 实验亮点

SmartCoder-R1在包含756个真实世界函数的基准测试中，与17个基线模型相比，在五个关键指标上取得了最佳性能。其中，FullRate指标达到了50.53%，比最强的基线DeepSeek-R1相对提高了45.79%。此外，人工评估结果表明，SmartCoder-R1生成的代码在功能性、安全性和清晰度方面均获得了高质量的评分。

## 🎯 应用场景

该研究成果可应用于智能合约自动生成、安全审计和漏洞修复等领域。通过提高智能合约的安全性和可解释性，降低智能合约开发和部署的风险，促进区块链技术的广泛应用。未来，该技术有望应用于更复杂的智能合约场景，并与其他安全工具集成，构建更完善的智能合约安全生态。

## 📄 摘要（原文）

> Smart contracts automate the management of high-value assets, where vulnerabilities can lead to catastrophic financial losses. This challenge is amplified in Large Language Models (LLMs) by two interconnected failures: they operate as unauditable "black boxes" lacking a transparent reasoning process, and consequently, generate code riddled with critical security vulnerabilities. To address both issues, we propose SmartCoder-R1 (based on Qwen2.5-Coder-7B), a novel framework for secure and explainable smart contract generation. It begins with Continual Pre-training (CPT) to specialize the model. We then apply Long Chain-of-Thought Supervised Fine-Tuning (L-CoT SFT) on 7,998 expert-validated reasoning-and-code samples to train the model to emulate human security analysis. Finally, to directly mitigate vulnerabilities, we employ Security-Aware Group Relative Policy Optimization (S-GRPO), a reinforcement learning phase that refines the generation policy by optimizing a weighted reward signal for compilation success, security compliance, and format correctness. Evaluated against 17 baselines on a benchmark of 756 real-world functions, SmartCoder-R1 establishes a new state of the art, achieving top performance across five key metrics: a ComPass of 87.70%, a VulRate of 8.60%, a SafeAval of 80.16%, a FuncRate of 53.84%, and a FullRate of 50.53%. This FullRate marks a 45.79% relative improvement over the strongest baseline, DeepSeek-R1. Crucially, its generated reasoning also excels in human evaluations, achieving high-quality ratings for Functionality (82.7%), Security (85.3%), and Clarity (90.7%).

