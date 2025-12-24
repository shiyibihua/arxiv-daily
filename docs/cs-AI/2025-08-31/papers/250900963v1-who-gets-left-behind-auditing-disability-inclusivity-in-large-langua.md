---
layout: default
title: Who Gets Left Behind? Auditing Disability Inclusivity in Large Language Models
---

# Who Gets Left Behind? Auditing Disability Inclusivity in Large Language Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.00963" class="toolbar-btn" target="_blank">📄 arXiv: 2509.00963v1</a>
  <a href="https://arxiv.org/pdf/2509.00963.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.00963v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.00963v1', 'Who Gets Left Behind? Auditing Disability Inclusivity in Large Language Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Deepika Dash, Yeshil Bangera, Mithil Bangera, Gouthami Vadithya, Srikant Panda

**分类**: cs.CY, cs.AI

**发布日期**: 2025-08-31

---

## 💡 一句话要点

**提出无障碍审计基准以解决大型语言模型的包容性问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `无障碍技术` `大型语言模型` `包容性审计` `残疾支持` `模型评估`

## 📋 核心要点

1. 现有大型语言模型在无障碍指导中存在明显的包容性差距，许多残疾群体未能获得有效支持。
2. 论文提出了一种系统的审计框架，通过人类验证的无障碍问题基准，评估模型在不同残疾类别的覆盖情况。
3. 实验结果表明，尽管视觉、听觉和运动残疾的支持较为充分，但其他类别如心理健康等仍显著不足，亟需改进。

## 📝 摘要（中文）

大型语言模型（LLMs）在无障碍指导中越来越多地被使用，但许多残疾群体仍未得到充分服务。为了解决这一差距，本文提出了一种与分类法对齐的人类验证的通用无障碍问题基准，旨在系统性审计不同残疾的包容性。该基准从问题级覆盖、残疾级覆盖和深度三个维度评估模型。对17个专有和开放权重模型的应用显示，视觉、听觉和运动残疾的覆盖较好，而言语、遗传/发育、感官认知和心理健康等类别则服务不足。这些发现揭示了当前LLM无障碍指导中被忽视的群体，并强调了可操作的改进措施，如基于分类法的提示/训练和联合审计的评估。

## 🔬 方法详解

**问题定义**：本文旨在解决大型语言模型在无障碍指导中对不同残疾群体的服务不足问题。现有方法未能全面覆盖所有残疾类型，导致部分群体被忽视。

**核心思路**：论文提出了一种与分类法对齐的无障碍问题基准，系统性地审计模型在不同残疾类别的包容性，确保各类残疾群体都能得到有效支持。

**技术框架**：整体架构包括三个主要模块：问题级覆盖评估、残疾级覆盖评估和深度评估。每个模块针对不同维度进行分析，确保全面审计。

**关键创新**：最重要的创新在于提出了一个系统化的审计框架，能够同时评估模型的广度、平衡性和深度，与现有方法相比，提供了更全面的评估视角。

**关键设计**：在设计中，采用了人类验证的无障碍问题集，确保问题的有效性和相关性，同时在评估中引入了多维度的覆盖指标，以便更好地反映模型的实际表现。

## 📊 实验亮点

实验结果显示，17个模型在视觉、听觉和运动残疾的支持上表现较好，但在言语、遗传/发育、感官认知和心理健康等类别的支持上存在显著不足。这一发现强调了当前无障碍指导中的包容性缺口，呼吁对模型进行更全面的审计和改进。

## 🎯 应用场景

该研究的潜在应用领域包括无障碍技术开发、教育和公共服务等。通过提升大型语言模型的包容性，可以更好地服务于不同残疾群体，推动社会的全面包容与公平。未来，研究成果有望影响政策制定和技术标准，促进无障碍设计的普及。

## 📄 摘要（原文）

> Large Language Models (LLMs) are increasingly used for accessibility guidance, yet many disability groups remain underserved by their advice. To address this gap, we present taxonomy aligned benchmark1 of human validated, general purpose accessibility questions, designed to systematically audit inclusivity across disabilities. Our benchmark evaluates models along three dimensions: Question-Level Coverage (breadth within answers), Disability-Level Coverage (balance across nine disability categories), and Depth (specificity of support). Applying this framework to 17 proprietary and open-weight models reveals persistent inclusivity gaps: Vision, Hearing, and Mobility are frequently addressed, while Speech, Genetic/Developmental, Sensory-Cognitive, and Mental Health remain under served. Depth is similarly concentrated in a few categories but sparse elsewhere. These findings reveal who gets left behind in current LLM accessibility guidance and highlight actionable levers: taxonomy-aware prompting/training and evaluations that jointly audit breadth, balance, and depth.

