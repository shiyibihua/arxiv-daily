---
layout: default
title: Augmenting Large Language Models with Static Code Analysis for Automated Code Quality Improvements
---

# Augmenting Large Language Models with Static Code Analysis for Automated Code Quality Improvements

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.10330" class="toolbar-btn" target="_blank">📄 arXiv: 2506.10330v1</a>
  <a href="https://arxiv.org/pdf/2506.10330.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.10330v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.10330v1', 'Augmenting Large Language Models with Static Code Analysis for Automated Code Quality Improvements')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Seyed Moein Abtahi, Akramul Azim

**分类**: cs.SE, cs.AI

**发布日期**: 2025-06-12

**备注**: Accepted at FORGE 2025

---

## 💡 一句话要点

**通过静态代码分析增强大型语言模型以自动改善代码质量**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `静态代码分析` `自动化修复` `代码质量` `软件开发` `迭代提示工程` `检索增强生成`

## 📋 核心要点

1. 核心问题：现有代码质量检测方法在检测准确性和自动修复能力上存在不足，导致开发效率低下。
2. 方法要点：本研究提出将大型语言模型与静态代码分析框架结合，利用迭代提示工程和RAG技术实现自动化代码修订。
3. 实验或效果：实验结果显示，结合上述方法后，代码问题显著减少，提升了代码质量和开发效率。

## 📝 摘要（中文）

本研究通过将大型语言模型（LLMs）如OpenAI的GPT-3.5 Turbo和GPT-4o整合到软件开发工作流程中，探讨了代码问题检测和修复自动化。静态代码分析框架能够检测大型软件项目中的缺陷、漏洞和代码异味。提取并组织每个问题的详细信息，以便利用LLMs进行自动化代码修订。采用迭代的提示工程过程，确保提示结构化以产生准确且符合项目要求的输出。实现了检索增强生成（RAG）以提高修订的相关性和精确性，使LLM能够访问和整合实时外部知识。通过定制的“代码比较应用”解决了LLM幻觉问题，识别并纠正错误更改。后续使用静态代码分析框架的扫描显示代码问题显著减少，证明了结合LLMs、静态分析和RAG以提高代码质量的有效性。

## 🔬 方法详解

**问题定义**：本论文旨在解决软件开发中代码质量检测和修复的自动化问题。现有方法在准确性和效率上存在不足，导致开发人员需要花费大量时间进行手动修复。

**核心思路**：论文的核心思路是将大型语言模型与静态代码分析结合，通过自动化的方式提高代码质量。通过迭代的提示工程，确保生成的修订建议符合项目需求，从而减少人工干预。

**技术框架**：整体架构包括静态代码分析框架、LLM生成模块和代码比较应用。静态分析框架负责检测代码问题，LLM生成模块用于生成修订建议，而代码比较应用则用于验证和纠正生成的建议。

**关键创新**：最重要的技术创新在于将RAG技术与LLM结合，增强了模型的实时知识获取能力，并通过定制的代码比较应用解决了LLM幻觉问题，确保生成的修订是准确的。

**关键设计**：在设计中，采用了迭代的提示工程方法，确保提示的结构化和针对性。同时，代码比较应用的设计使得在应用修订前能够有效识别和纠正错误，提升了整体系统的可靠性。

## 📊 实验亮点

实验结果表明，结合静态代码分析和大型语言模型后，代码问题减少了显著比例，具体数据未提供。通过RAG技术的应用，修订的相关性和准确性得到了提升，验证了该方法在实际开发中的有效性。

## 🎯 应用场景

该研究的潜在应用领域包括软件开发、代码审查和质量保证等。通过自动化代码修复，能够显著提高开发效率，减少人力成本，并提升软件产品的整体质量。未来，该方法可能在更广泛的编程语言和开发环境中得到应用，推动软件工程的智能化进程。

## 📄 摘要（原文）

> This study examined code issue detection and revision automation by integrating Large Language Models (LLMs) such as OpenAI's GPT-3.5 Turbo and GPT-4o into software development workflows. A static code analysis framework detects issues such as bugs, vulnerabilities, and code smells within a large-scale software project. Detailed information on each issue was extracted and organized to facilitate automated code revision using LLMs. An iterative prompt engineering process is applied to ensure that prompts are structured to produce accurate and organized outputs aligned with the project requirements. Retrieval-augmented generation (RAG) is implemented to enhance the relevance and precision of the revisions, enabling LLM to access and integrate real-time external knowledge. The issue of LLM hallucinations - where the model generates plausible but incorrect outputs - is addressed by a custom-built "Code Comparison App," which identifies and corrects erroneous changes before applying them to the codebase. Subsequent scans using the static code analysis framework revealed a significant reduction in code issues, demonstrating the effectiveness of combining LLMs, static analysis, and RAG to improve code quality, streamline the software development process, and reduce time and resource expenditure.

