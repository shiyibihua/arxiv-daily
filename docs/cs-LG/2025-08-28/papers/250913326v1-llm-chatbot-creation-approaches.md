---
layout: default
title: LLM Chatbot-Creation Approaches
---

# LLM Chatbot-Creation Approaches

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.13326" class="toolbar-btn" target="_blank">📄 arXiv: 2509.13326v1</a>
  <a href="https://arxiv.org/pdf/2509.13326.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.13326v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.13326v1', 'LLM Chatbot-Creation Approaches')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Hemil Mehta, Tanvi Raut, Kohav Yadav, Edward F. Gehringer

**分类**: cs.HC, cs.LG

**发布日期**: 2025-08-28

**备注**: Forthcoming in Frontiers in Education (FIE 2025), Nashville, Tennessee, USA, Nov 2-5, 2025

---

## 💡 一句话要点

**比较低代码平台与定制编码解决方案以开发教育聊天机器人**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `教育聊天机器人` `低代码平台` `定制编码` `大型语言模型` `用户体验` `技术性能` `可扩展性`

## 📋 核心要点

1. 现有的聊天机器人开发方法在定制化和扩展性方面存在不足，难以满足教育领域的多样化需求。
2. 论文提出通过比较低代码平台与定制编码解决方案，探索适合教育环境的聊天机器人开发策略。
3. 研究发现低代码平台便于快速原型开发，但定制编码系统在控制和灵活性方面表现更佳，适合复杂应用。

## 📝 摘要（中文）

本研究探讨了在教育背景下开发课程聊天机器人的方法，比较了低代码平台与定制编码解决方案。随着大型语言模型（LLMs）的兴起，基于LLM的聊天机器人被逐步整合进教学工作流程中，以实现任务自动化、提供帮助和可扩展支持。选择最佳开发策略需要在易用性、定制化、数据隐私和可扩展性之间取得平衡。研究表明，低代码平台如AnythingLLM和Botpress虽然能够快速原型开发，但在定制化和扩展性方面存在局限，而定制编码系统则提供了更多控制，但需要较高的技术专长。该研究为根据机构目标和资源选择合适的开发策略提供了框架。未来的工作将集中在结合低代码可访问性与模块化定制的混合解决方案上，并纳入多模态输入以支持智能辅导系统。

## 🔬 方法详解

**问题定义**：本研究旨在解决教育领域中聊天机器人开发的最佳策略选择问题，现有方法在定制化和扩展性上存在痛点。

**核心思路**：通过比较低代码平台与定制编码解决方案，评估两者在技术性能、可扩展性和用户体验方面的差异，以指导教育机构选择合适的开发方式。

**技术框架**：研究采用了Prompt工程、检索增强生成（RAG）和个性化技术，构建了多个聊天机器人原型，并对其进行评估。主要模块包括用户交互、数据处理和反馈机制。

**关键创新**：本研究的创新点在于系统性比较低代码与定制编码的开发方式，揭示了两者在适应性反馈和对话连续性方面的实现效果，提供了选择框架。

**关键设计**：在技术细节上，研究使用了LangChain、FAISS和FastAPI等工具，设置了适当的参数以优化聊天机器人的响应时间和用户体验。

## 📊 实验亮点

实验结果表明，低代码平台在原型开发速度上具有明显优势，但在定制化和扩展性方面不及定制编码系统。定制编码系统在用户体验和技术性能上表现更佳，能够实现更复杂的功能和更高的用户满意度。

## 🎯 应用场景

该研究的潜在应用领域包括教育技术、在线学习平台和智能辅导系统。通过提供灵活的聊天机器人开发策略，教育机构能够更好地满足学生的个性化学习需求，提升教学效果。

## 📄 摘要（原文）

> This full research-to-practice paper explores approaches for developing course chatbots by comparing low-code platforms and custom-coded solutions in educational contexts. With the rise of Large Language Models (LLMs) like GPT-4 and LLaMA, LLM-based chatbots are being integrated into teaching workflows to automate tasks, provide assistance, and offer scalable support. However, selecting the optimal development strategy requires balancing ease of use, customization, data privacy, and scalability. This study compares two development approaches: low-code platforms like AnythingLLM and Botpress, with custom-coded solutions using LangChain, FAISS, and FastAPI. The research uses Prompt engineering, Retrieval-augmented generation (RAG), and personalization to evaluate chatbot prototypes across technical performance, scalability, and user experience. Findings indicate that while low-code platforms enable rapid prototyping, they face limitations in customization and scaling, while custom-coded systems offer more control but require significant technical expertise. Both approaches successfully implement key research principles such as adaptive feedback loops and conversational continuity. The study provides a framework for selecting the appropriate development strategy based on institutional goals and resources. Future work will focus on hybrid solutions that combine low-code accessibility with modular customization and incorporate multimodal input for intelligent tutoring systems.

