---
layout: default
title: Leveraging Large Language Models for Robot-Assisted Learning of Morphological Structures in Preschool Children with Language Vulnerabilities
---

# Leveraging Large Language Models for Robot-Assisted Learning of Morphological Structures in Preschool Children with Language Vulnerabilities

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.22287" class="toolbar-btn" target="_blank">📄 arXiv: 2509.22287v1</a>
  <a href="https://arxiv.org/pdf/2509.22287.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.22287v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.22287v1', 'Leveraging Large Language Models for Robot-Assisted Learning of Morphological Structures in Preschool Children with Language Vulnerabilities')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Stina Sundstedt, Mattias Wingren, Susanne Hägglund, Daniel Ventus

**分类**: cs.RO, cs.AI, cs.HC

**发布日期**: 2025-09-26

**备注**: 12 pages, 2 figures, Preprint of: Sundstedt, S., Wingren, M., Hägglund, S. & Ventus, D. (2025). Leveraging Large Language Models for Robot-Assisted Learning of Morphological Structures in Preschool Children with Language Vulnerabilities. In: Stephanidis, C., Antona, M., Ntoa, S. & Salvendy, G. (eds.), Communications in Computer and Information Science, vol. 2523, pp. 415-425. Springer

**期刊**: Communications in Computer and Information Science(2025). Stephanidis, C., Antona, M., Ntoa, S. & Salvendy, G. (eds.). p. 415-425 11 p. ( Communications in Computer and Information Science; vol. 2523)

**DOI**: [10.1007/978-3-031-94153-5_41](https://doi.org/10.1007/978-3-031-94153-5_41)

---

## 💡 一句话要点

**利用大型语言模型辅助机器人为语言障碍幼儿提供形态结构学习**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `机器人辅助学习` `大型语言模型` `形态结构学习` `语言障碍儿童` `会话机器人`

## 📋 核心要点

1. 现有方法依赖人工干预，对教育者语言能力要求高，且难以兼顾互动性和教学目标。
2. 利用大型语言模型，使机器人能够自动生成和传递特定的形态目标，辅助语言学习。
3. 设想机器人可作为儿童和专业人士的语言学习模型，支持多种语言的形态结构教学。

## 📝 摘要（中文）

针对存在语言障碍（如发展性语言障碍或移民相关的语言挑战）的学龄前儿童，通常需要加强其表达能力。基于内隐学习原则，语言治疗师（SLT）通常将目标形态结构（例如，第三人称-s）嵌入到日常互动或基于游戏的学习活动中。SLT建议教育工作者也这样做。这种方法需要精确的语言知识和实时生成各种形态形式（例如，“爸爸开车上班时会戴这些”）。当教育工作者或家长还必须让孩子们保持参与并管理游戏活动中的轮流时，这项任务变得更具挑战性。在TalBot项目中，我们的多专业团队开发了一个应用程序，其中Furhat会话机器人与孩子们玩单词检索游戏“Alias”，以提高语言技能。我们的应用程序目前使用大型语言模型（LLM）来管理游戏玩法、对话、情感反应和轮流。我们的下一步是进一步利用LLM的能力，以便机器人可以在游戏中生成和传递特定的形态目标。我们假设机器人在这项任务中的表现可能优于人类。这种方法的新颖之处在于，机器人最终可以作为儿童和专业人士的模型和导师，并且在这种情况下使用LLM能力将支持有语言障碍的儿童的基本沟通需求。我们的长期目标是创建一个强大的基于LLM的机器人辅助语言学习干预，能够教授不同语言的各种形态结构。

## 🔬 方法详解

**问题定义**：论文旨在解决语言障碍学龄前儿童在形态结构学习方面面临的挑战。现有方法，如由语言治疗师或教育者主导的教学，存在对教学者语言能力要求高、难以实时生成多样形态形式、以及难以兼顾儿童参与度和教学目标等痛点。

**核心思路**：论文的核心思路是利用大型语言模型（LLM）的强大生成能力，让机器人能够自动生成并传递特定的形态目标，从而辅助儿童进行语言学习。通过机器人与儿童进行互动游戏，将形态结构的学习融入到自然、有趣的环境中。

**技术框架**：TalBot项目的整体框架包含一个Furhat会话机器人，该机器人运行一个基于LLM的应用程序。该应用程序负责管理游戏玩法（如Alias游戏）、对话、情感反应和轮流。LLM是核心组件，负责生成包含特定形态结构的句子，并根据儿童的反应进行调整。

**关键创新**：该方法的主要创新在于将LLM应用于机器人辅助语言学习，特别是针对形态结构教学。与传统方法相比，机器人能够提供一致、可重复的教学，并且可以根据儿童的个体差异进行个性化调整。此外，机器人还可以作为教育者的模型，帮助他们更好地进行语言教学。

**关键设计**：目前论文尚未详细描述LLM的具体架构和训练细节。未来的研究方向可能包括：1) 设计合适的提示工程（Prompt Engineering），引导LLM生成符合教学目标的句子；2) 探索不同的损失函数，以优化LLM在形态结构生成方面的性能；3) 研究如何根据儿童的语言水平和学习进度，动态调整教学内容和难度。

## 📊 实验亮点

论文提出了一个利用大型语言模型辅助机器人进行语言教学的创新方法，旨在解决语言障碍儿童在形态结构学习中遇到的困难。虽然目前尚未提供具体的实验数据，但该研究为机器人辅助语言学习开辟了新的方向，并有望在未来的研究中验证其有效性。

## 🎯 应用场景

该研究成果可应用于特殊教育领域，为语言障碍儿童提供个性化的语言学习支持。同时，该技术也可推广到普通幼儿的语言启蒙教育中，提高语言学习效率。未来，基于LLM的机器人辅助语言学习系统有望成为一种重要的教育工具，减轻教育者的负担，提升教学质量。

## 📄 摘要（原文）

> Preschool children with language vulnerabilities -- such as developmental language disorders or immigration related language challenges -- often require support to strengthen their expressive language skills. Based on the principle of implicit learning, speech-language therapists (SLTs) typically embed target morphological structures (e.g., third person -s) into everyday interactions or game-based learning activities. Educators are recommended by SLTs to do the same. This approach demands precise linguistic knowledge and real-time production of various morphological forms (e.g., "Daddy wears these when he drives to work"). The task becomes even more demanding when educators or parent also must keep children engaged and manage turn-taking in a game-based activity. In the TalBot project our multiprofessional team have developed an application in which the Furhat conversational robot plays the word retrieval game "Alias" with children to improve language skills. Our application currently employs a large language model (LLM) to manage gameplay, dialogue, affective responses, and turn-taking. Our next step is to further leverage the capacity of LLMs so the robot can generate and deliver specific morphological targets during the game. We hypothesize that a robot could outperform humans at this task. Novel aspects of this approach are that the robot could ultimately serve as a model and tutor for both children and professionals and that using LLM capabilities in this context would support basic communication needs for children with language vulnerabilities. Our long-term goal is to create a robust LLM-based Robot-Assisted Language Learning intervention capable of teaching a variety of morphological structures across different languages.

