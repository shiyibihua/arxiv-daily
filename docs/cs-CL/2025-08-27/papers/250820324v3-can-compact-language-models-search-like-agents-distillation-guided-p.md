---
layout: default
title: Can Compact Language Models Search Like Agents? Distillation-Guided Policy Optimization for Preserving Agentic RAG Capabilities
---

# Can Compact Language Models Search Like Agents? Distillation-Guided Policy Optimization for Preserving Agentic RAG Capabilities

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.20324" class="toolbar-btn" target="_blank">📄 arXiv: 2508.20324v3</a>
  <a href="https://arxiv.org/pdf/2508.20324.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.20324v3" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.20324v3', 'Can Compact Language Models Search Like Agents? Distillation-Guided Policy Optimization for Preserving Agentic RAG Capabilities')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Rikuto Kotoge, Mai Nishimura, Jiaxin Ma

**分类**: cs.CL

**发布日期**: 2025-08-27 (更新: 2025-10-11)

---

## 💡 一句话要点

**提出蒸馏引导策略优化以提升紧凑语言模型的智能搜索能力**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `强化学习` `蒸馏训练` `紧凑模型` `智能搜索` `策略优化` `RAG能力` `教师模型` `模型压缩`

## 📋 核心要点

1. 现有方法在将强化学习应用于紧凑模型时，面临初始性能差、奖励稀疏和训练不稳定等挑战。
2. 本文提出的蒸馏引导策略优化（DGPO）通过教师示范的冷启动和持续指导，提升紧凑模型的智能行为。
3. 实验结果显示，DGPO使紧凑模型实现了复杂的智能搜索行为，部分情况下超越了大型教师模型的表现。

## 📝 摘要（中文）

强化学习已成为从语言模型中引导智能RAG行为（如搜索和规划）的主要后训练方法。尽管在大型模型中取得了成功，但将强化学习应用于紧凑模型（如0.5-1B参数）面临独特挑战。紧凑模型的初始性能较差，导致稀疏奖励和不稳定训练。为克服这些困难，本文提出了蒸馏引导策略优化（DGPO），该方法利用教师示范的冷启动初始化和在策略优化过程中持续的教师指导。通过引入智能RAG能力（ARC）这一细粒度指标，分析推理、搜索协调和响应合成。实验表明，DGPO使紧凑模型能够实现复杂的智能搜索行为，甚至在某些情况下超越了大型教师模型。

## 🔬 方法详解

**问题定义**：本文旨在解决紧凑语言模型在应用强化学习时的性能不足问题，尤其是初始性能差和训练不稳定导致的稀疏奖励问题。

**核心思路**：提出蒸馏引导策略优化（DGPO），通过教师示范进行冷启动初始化，并在策略优化过程中提供持续的教师指导，以提升紧凑模型的智能行为。

**技术框架**：DGPO的整体架构包括两个主要阶段：首先是通过教师模型进行冷启动初始化，其次是利用教师模型的反馈进行策略优化，确保紧凑模型在学习过程中保持稳定性和有效性。

**关键创新**：DGPO的核心创新在于结合了教师示范与强化学习的优势，使得紧凑模型能够在资源受限的环境中实现智能RAG能力，显著提升了模型的搜索和推理能力。

**关键设计**：在DGPO中，设置了特定的损失函数以平衡教师指导与模型自主学习的关系，同时采用了适应性的学习率调整策略，以应对训练过程中的不稳定性。

## 📊 实验亮点

实验结果表明，DGPO使得紧凑模型在智能搜索行为上取得了显著提升，部分情况下其性能超过了大型教师模型，展示了在资源受限环境中实现复杂智能行为的可能性。

## 🎯 应用场景

该研究的潜在应用领域包括智能助手、自动化搜索引擎和资源受限的嵌入式系统。通过提升紧凑模型的智能搜索能力，能够在计算资源有限的环境中实现更高效的任务执行，具有重要的实际价值和广泛的应用前景。

## 📄 摘要（原文）

> Reinforcement Learning has emerged as a dominant post-training approach to elicit agentic RAG behaviors such as search and planning from language models. Despite its success with larger models, applying RL to compact models (e.g., 0.5--1B parameters) presents unique challenges. The compact models exhibit poor initial performance, resulting in sparse rewards and unstable training. To overcome these difficulties, we propose Distillation-Guided Policy Optimization (DGPO), which employs cold-start initialization from teacher demonstrations and continuous teacher guidance during policy optimization. To understand how compact models preserve agentic behavior, we introduce Agentic RAG Capabilities (ARC), a fine-grained metric analyzing reasoning, search coordination, and response synthesis. Comprehensive experiments demonstrate that DGPO enables compact models to achieve sophisticated agentic search behaviors, even outperforming the larger teacher model in some cases. DGPO makes agentic RAG feasible in computing resource-constrained environments.

