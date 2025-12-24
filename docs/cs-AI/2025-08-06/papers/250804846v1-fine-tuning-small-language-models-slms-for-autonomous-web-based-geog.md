---
layout: default
title: Fine-Tuning Small Language Models (SLMs) for Autonomous Web-based Geographical Information Systems (AWebGIS)
---

# Fine-Tuning Small Language Models (SLMs) for Autonomous Web-based Geographical Information Systems (AWebGIS)

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.04846" class="toolbar-btn" target="_blank">📄 arXiv: 2508.04846v1</a>
  <a href="https://arxiv.org/pdf/2508.04846.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.04846v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.04846v1', 'Fine-Tuning Small Language Models (SLMs) for Autonomous Web-based Geographical Information Systems (AWebGIS)')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Mahdi Nazari Ashani, Ali Asghar Alesheikh, Saba Kazemi, Kimya Kheirkhah, Yasin Mohammadi, Fatemeh Rezaie, Amir Mahdi Manafi, Hedieh Zarkesh

**分类**: cs.AI, cs.CL, cs.LG

**发布日期**: 2025-08-06

---

## 💡 一句话要点

**提出基于小型语言模型的自主网络地理信息系统解决方案**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `自主系统` `地理信息` `小型语言模型` `自然语言处理` `客户端计算` `隐私保护` `模型微调`

## 📋 核心要点

1. 现有的AWebGIS解决方案依赖云端大型语言模型，存在隐私和可扩展性问题。
2. 论文提出了一种基于微调小型语言模型的完全自主离线方法，能够在客户端浏览器中执行。
3. 实验结果显示，该方法在准确性上优于其他方法，精确匹配率达到0.93，ROUGE得分为0.98。

## 📝 摘要（中文）

自主网络地理信息系统（AWebGIS）旨在通过自然语言输入执行地理空间操作，实现直观、智能和免提的交互。然而，现有解决方案多依赖于云端大型语言模型（LLMs），这需要持续的互联网连接，并因集中式服务器处理而引发用户隐私和可扩展性问题。本研究比较了三种实现AWebGIS的方法：使用云端LLMs的全自动在线方法、使用经典机器学习分类器的半自动离线方法，以及基于微调小型语言模型（SLM）的完全自主离线方法。结果表明，基于SLM的第三种方法在准确性上表现最佳，精确匹配准确率为0.93，Levenshtein相似度为0.99，ROUGE-1和ROUGE-L得分均为0.98。这种客户端计算策略减轻了后端服务器的负担，展示了浏览器可执行模型在AWebGIS解决方案中的可行性。

## 🔬 方法详解

**问题定义**：本论文旨在解决现有自主网络地理信息系统在隐私和可扩展性方面的不足，尤其是依赖云端大型语言模型所带来的问题。

**核心思路**：论文提出了一种基于微调小型语言模型（SLM）的完全自主离线方法，允许用户在本地浏览器中处理地理信息请求，从而避免了对云端服务的依赖。

**技术框架**：整体架构包括数据输入模块、SLM模型推理模块和结果输出模块。用户通过自然语言输入地理信息请求，模型在本地进行处理并返回结果。

**关键创新**：最重要的创新在于将小型语言模型微调应用于地理信息系统，显著提高了处理准确性，并减少了对后端服务器的依赖。

**关键设计**：在模型微调过程中，采用了特定的损失函数和优化算法，以确保模型在地理信息处理任务中的高效性和准确性。

## 📊 实验亮点

实验结果显示，基于微调小型语言模型的方案在准确性上优于其他方法，精确匹配率达到0.93，Levenshtein相似度为0.99，ROUGE-1和ROUGE-L得分均为0.98，展现了显著的性能提升。

## 🎯 应用场景

该研究的潜在应用领域包括智能城市管理、环境监测和旅游导航等。通过实现自主的地理信息系统，用户能够在没有网络连接的情况下，快速获取所需的地理信息，提升了系统的实用性和用户体验。

## 📄 摘要（原文）

> Autonomous web-based geographical information systems (AWebGIS) aim to perform geospatial operations from natural language input, providing intuitive, intelligent, and hands-free interaction. However, most current solutions rely on cloud-based large language models (LLMs), which require continuous internet access and raise users' privacy and scalability issues due to centralized server processing. This study compares three approaches to enabling AWebGIS: (1) a fully-automated online method using cloud-based LLMs (e.g., Cohere); (2) a semi-automated offline method using classical machine learning classifiers such as support vector machine and random forest; and (3) a fully autonomous offline (client-side) method based on a fine-tuned small language model (SLM), specifically T5-small model, executed in the client's web browser. The third approach, which leverages SLMs, achieved the highest accuracy among all methods, with an exact matching accuracy of 0.93, Levenshtein similarity of 0.99, and recall-oriented understudy for gisting evaluation ROUGE-1 and ROUGE-L scores of 0.98. Crucially, this client-side computation strategy reduces the load on backend servers by offloading processing to the user's device, eliminating the need for server-based inference. These results highlight the feasibility of browser-executable models for AWebGIS solutions.

