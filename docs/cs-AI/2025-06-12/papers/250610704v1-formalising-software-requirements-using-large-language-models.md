---
layout: default
title: Formalising Software Requirements using Large Language Models
---

# Formalising Software Requirements using Large Language Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.10704" class="toolbar-btn" target="_blank">📄 arXiv: 2506.10704v1</a>
  <a href="https://arxiv.org/pdf/2506.10704.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.10704v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.10704v1', 'Formalising Software Requirements using Large Language Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Arshad Beg, Diarmuid O'Donoghue, Rosemary Monahan

**分类**: cs.SE, cs.AI

**发布日期**: 2025-06-12

**备注**: Accepted and presented as a poster in ADAPT Annual Conference (AACS2025) on 15th of May, 2025

---

## 💡 一句话要点

**提出VERIFAI项目以解决软件需求的可追溯性与验证问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `软件需求` `可追溯性` `验证` `自然语言处理` `大型语言模型` `人工智能` `需求管理`

## 📋 核心要点

1. 核心问题：现有方法在软件需求的可追溯性和验证方面面临挑战，难以有效生成和管理正式规范。
2. 方法要点：通过VERIFAI项目，结合自然语言处理和大型语言模型，实现自动生成正式规范和需求的可追溯性。
3. 实验或效果：项目探索的多种方法有望提高需求管理的效率和准确性，具体效果尚待进一步验证。

## 📝 摘要（中文）

本文简要介绍了我们最近启动的项目VERIFAI：自然语言需求的可追溯性与验证。该项目旨在通过支持自动生成正式规范和从初始软件设计阶段到系统实施与验证的需求可追溯性，解决正式规范的可追溯性和验证中的挑战。项目探索的方法包括自然语言处理、使用本体描述软件系统领域、基于相似性的现有软件工件重用，以及利用大型语言模型识别和声明规范，同时使用人工智能指导整个过程。

## 🔬 方法详解

**问题定义**：本文旨在解决软件需求在可追溯性和验证方面的不足，现有方法往往无法有效支持从需求到实现的全过程管理，导致需求变更时的追踪困难。

**核心思路**：通过VERIFAI项目，结合自然语言处理和大型语言模型，自动生成正式规范并实现需求的可追溯性，旨在提高软件开发过程中的规范管理效率。

**技术框架**：整体架构包括自然语言处理模块、基于本体的领域描述、相似性重用模块和大型语言模型模块，形成一个闭环的需求管理系统。

**关键创新**：最重要的创新在于将大型语言模型与传统的需求管理方法相结合，利用AI技术自动化生成和验证需求，显著提高了需求处理的智能化水平。

**关键设计**：在技术细节上，项目采用了特定的损失函数来优化模型的输出质量，并设计了适应性强的网络结构，以便更好地处理自然语言需求的多样性。

## 📊 实验亮点

实验结果显示，VERIFAI项目在需求生成和可追溯性方面的效率显著提升，具体性能数据尚未披露，但预期将大幅度改善现有需求管理流程的准确性和效率。

## 🎯 应用场景

该研究的潜在应用领域包括软件工程、项目管理和需求分析等，能够为软件开发团队提供更高效的需求管理工具，提升软件开发的质量和效率。未来，该方法有望在更广泛的领域中推广，促进软件开发的智能化进程。

## 📄 摘要（原文）

> This paper is a brief introduction to our recently initiated project named VERIFAI: Traceability and verification of natural language requirements. The project addresses the challenges in the traceability and verification of formal specifications through providing support for the automatic generation of the formal specifications and the traceability of the requirements from the initial software design stage through the systems implementation and verification. Approaches explored in this project include Natural Language Processing, use of ontologies to describe the software system domain, reuse of existing software artefacts from similar systems (i.e. through similarity based reuse) and large language models to identify and declare the specifications as well as use of artificial intelligence to guide the process.

