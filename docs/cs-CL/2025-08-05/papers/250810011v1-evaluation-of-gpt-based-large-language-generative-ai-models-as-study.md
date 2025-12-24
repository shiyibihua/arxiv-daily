---
layout: default
title: Evaluation of GPT-based large language generative AI models as study aids for the national licensure examination for registered dietitians in Japan
---

# Evaluation of GPT-based large language generative AI models as study aids for the national licensure examination for registered dietitians in Japan

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.10011" class="toolbar-btn" target="_blank">📄 arXiv: 2508.10011v1</a>
  <a href="https://arxiv.org/pdf/2508.10011.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.10011v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.10011v1', 'Evaluation of GPT-based large language generative AI models as study aids for the national licensure examination for registered dietitians in Japan')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yuta Nagamori, Mikoto Kosai, Yuji Kawai, Haruka Marumo, Misaki Shibuya, Tatsuya Negishi, Masaki Imanishi, Yasumasa Ikeda, Koichiro Tsuchiya, Asuka Sawai, Licht Miyamoto

**分类**: cs.CL

**发布日期**: 2025-08-05

---

## 💡 一句话要点

**评估基于GPT的大语言生成AI模型作为日本注册营养师考试的学习辅助工具**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `生成式人工智能` `大型语言模型` `营养教育` `学习辅助工具` `模型评估` `提示工程` `考试准备`

## 📋 核心要点

1. 现有的生成AI模型在营养教育领域的应用尚未得到充分验证，尤其是在日本注册营养师考试中表现不佳。
2. 本研究通过使用日本国家注册营养师考试的问题，评估了基于GPT的生成AI模型作为学习辅助工具的有效性。
3. 实验结果显示，Bing-Precise和Bing-Creative模型的表现优于其他模型，但整体准确性和一致性仍需改进。

## 📝 摘要（中文）

基于大型语言模型（LLM）的生成式人工智能（AI），如ChatGPT，在医学和教育等多个专业领域取得了显著进展。然而，它们在营养教育，特别是日本注册营养师国家执照考试中的表现仍未得到充分探讨。本研究旨在评估当前基于LLM的生成AI模型作为营养学生学习辅助工具的潜力。研究使用了日本国家注册营养师考试的问题作为ChatGPT和三个Bing模型（Precise、Creative、Balanced）的提示。结果表明，Bing-Precise（66.2%）和Bing-Creative（61.4%）超过了及格线，而其他模型的表现则不尽如人意。尽管某些生成AI模型略微超过了及格线，但整体准确性和答案一致性仍然不理想，显示出在答案稳定性方面的局限性。

## 🔬 方法详解

**问题定义**：本研究旨在解决基于生成AI的学习辅助工具在日本注册营养师考试中的有效性不足的问题。现有方法在准确性和答案一致性方面存在明显的短板。

**核心思路**：通过使用国家考试问题作为提示，评估不同生成AI模型的表现，并探索提示工程对模型性能的影响。

**技术框架**：研究使用了ChatGPT和三个Bing模型（Precise、Creative、Balanced），每个问题在独立会话中输入，分析模型的准确性、一致性和响应时间。

**关键创新**：本研究首次系统评估了生成AI模型在特定专业领域（营养教育）中的应用，揭示了模型在答案一致性和稳定性方面的局限性。

**关键设计**：实验中进行了额外的提示工程，包括角色分配，测试其对模型表现的潜在提升，发现仅在提供正确答案和解释时有轻微改善。整体上，模型在不同学科领域的表现差异明显。

## 📊 实验亮点

实验结果显示，Bing-Precise模型以66.2%的准确率和Bing-Creative模型以61.4%的准确率超过了60%的及格线，而ChatGPT和Bing-Balanced模型的表现则明显低于此标准，分别为42.8%和43.3%。这表明尽管某些模型表现良好，但整体准确性和一致性仍需显著提升。

## 🎯 应用场景

该研究为生成AI在营养教育领域的应用提供了重要的实证基础，未来可为营养师执照考试的学习辅助工具开发提供指导。随着技术的进步，生成AI有潜力成为教育领域的重要支持工具，提升学习效率和效果。

## 📄 摘要（原文）

> Generative artificial intelligence (AI) based on large language models (LLMs), such as ChatGPT, has demonstrated remarkable progress across various professional fields, including medicine and education. However, their performance in nutritional education, especially in Japanese national licensure examination for registered dietitians, remains underexplored. This study aimed to evaluate the potential of current LLM-based generative AI models as study aids for nutrition students. Questions from the Japanese national examination for registered dietitians were used as prompts for ChatGPT and three Bing models (Precise, Creative, Balanced), based on GPT-3.5 and GPT-4. Each question was entered into independent sessions, and model responses were analyzed for accuracy, consistency, and response time. Additional prompt engineering, including role assignment, was tested to assess potential performance improvements. Bing-Precise (66.2%) and Bing-Creative (61.4%) surpassed the passing threshold (60%), while Bing-Balanced (43.3%) and ChatGPT (42.8%) did not. Bing-Precise and Bing-Creative generally outperformed others across subject fields except Nutrition Education, where all models underperformed. None of the models consistently provided the same correct responses across repeated attempts, highlighting limitations in answer stability. ChatGPT showed greater consistency in response patterns but lower accuracy. Prompt engineering had minimal effect, except for modest improvement when correct answers and explanations were explicitly provided. While some generative AI models marginally exceeded the passing threshold, overall accuracy and answer consistency remained suboptimal. Moreover, all the models demonstrated notable limitations in answer consistency and robustness. Further advancements are needed to ensure reliable and stable AI-based study aids for dietitian licensure preparation.

