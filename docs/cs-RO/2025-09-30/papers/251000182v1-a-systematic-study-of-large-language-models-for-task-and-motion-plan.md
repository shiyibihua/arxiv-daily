---
layout: default
title: A Systematic Study of Large Language Models for Task and Motion Planning With PDDLStream
---

# A Systematic Study of Large Language Models for Task and Motion Planning With PDDLStream

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.00182" class="toolbar-btn" target="_blank">📄 arXiv: 2510.00182v1</a>
  <a href="https://arxiv.org/pdf/2510.00182.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.00182v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2510.00182v1', 'A Systematic Study of Large Language Models for Task and Motion Planning With PDDLStream')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jorge Mendez-Mendez

**分类**: cs.RO, cs.AI

**发布日期**: 2025-09-30

---

## 💡 一句话要点

**提出基于LLM的TAMP系统以解决复杂机器人任务规划问题**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `任务规划` `运动规划` `机器人技术` `Gemini算法` `形式推理` `自主决策`

## 📋 核心要点

1. 现有方法在将大型语言模型与任务和运动规划结合时，面临规划能力覆盖范围不清晰的挑战。
2. 论文提出通过开发16种算法，利用Gemini 2.5 Flash替代TAMP的关键组件，以提高规划效率。
3. 实验结果表明，Gemini基础的规划器成功率较低且规划时间较长，非推理LLM变体在大多数情况下表现更佳。

## 📝 摘要（中文）

本研究探讨了大型语言模型（LLMs）在复杂机器人任务和运动规划中的应用，尤其是其规划能力的局限性。尽管LLMs在某些问题上表现出规划能力，但其在机器人任务中的适用范围尚不明确。为此，研究者们开发了16种算法，利用Gemini 2.5 Flash替代关键的任务和运动规划（TAMP）组件。通过对4950个问题的零样本实验，结果显示Gemini基础的规划器在成功率和规划时间上均低于传统工程方法。提供几何细节反而增加了任务规划错误，而非推理的LLM变体在大多数情况下优于推理变体，因为TAMP系统能够引导LLM纠正错误。

## 🔬 方法详解

**问题定义**：本研究旨在解决大型语言模型在复杂机器人任务和运动规划中的应用局限性，尤其是其规划能力在不同任务中的适用性尚不明确。现有方法在集成LLMs与TAMP时，面临设计复杂性和性能不足的问题。

**核心思路**：论文的核心思路是通过开发16种基于Gemini 2.5 Flash的算法，替代TAMP中的关键组件，以探索LLMs在任务规划中的潜力。此设计旨在结合LLMs的语义知识与TAMP的形式推理能力。

**技术框架**：整体架构包括数据输入、LLM处理、任务规划和结果输出四个主要模块。首先，输入数据被传递给LLM进行语义理解，然后通过Gemini算法进行任务规划，最后输出规划结果。

**关键创新**：最重要的技术创新在于将Gemini 2.5 Flash集成到TAMP系统中，提供了一种新的方法来评估LLMs在任务规划中的有效性。这与传统的工程方法相比，提供了更灵活的规划能力。

**关键设计**：在算法设计中，关键参数包括几何细节的提供与否、LLM的推理能力选择等。研究发现，几何细节的引入反而增加了任务规划错误，而非推理的LLM变体在效率上优于推理变体。

## 📊 实验亮点

实验结果显示，基于Gemini的规划器在4950个问题中表现出较低的成功率和较高的规划时间，具体成功率低于传统方法。非推理的LLM变体在大多数情况下表现优于推理变体，表明在任务规划中，快速反应的模型更具优势。

## 🎯 应用场景

该研究的潜在应用领域包括自主机器人、智能制造和人机协作等场景。通过提高机器人在复杂环境中的任务规划能力，能够显著提升其自主决策和执行能力，进而推动智能机器人技术的发展与应用。未来，研究成果可能会影响机器人领域的标准化和智能化进程。

## 📄 摘要（原文）

> Using large language models (LLMs) to solve complex robotics problems requires understanding their planning capabilities. Yet while we know that LLMs can plan on some problems, the extent to which these planning capabilities cover the space of robotics tasks is unclear. One promising direction is to integrate the semantic knowledge of LLMs with the formal reasoning of task and motion planning (TAMP). However, the myriad of choices for how to integrate LLMs within TAMP complicates the design of such systems. We develop 16 algorithms that use Gemini 2.5 Flash to substitute key TAMP components. Our zero-shot experiments across 4,950 problems and three domains reveal that the Gemini-based planners exhibit lower success rates and higher planning times than their engineered counterparts. We show that providing geometric details increases the number of task-planning errors compared to pure PDDL descriptions, and that (faster) non-reasoning LLM variants outperform (slower) reasoning variants in most cases, since the TAMP system can direct the LLM to correct its mistakes.

