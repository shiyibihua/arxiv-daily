---
layout: default
title: DeepSeek performs better than other Large Language Models in Dental Cases
---

# DeepSeek performs better than other Large Language Models in Dental Cases

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.02036" class="toolbar-btn" target="_blank">📄 arXiv: 2509.02036v1</a>
  <a href="https://arxiv.org/pdf/2509.02036.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.02036v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.02036v1', 'DeepSeek performs better than other Large Language Models in Dental Cases')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Hexian Zhang, Xinyu Yan, Yanqi Yang, Lijian Jin, Ping Yang, Junwen Wang

**分类**: cs.CL, cs.AI

**发布日期**: 2025-09-02

**备注**: Abstract word count: 171; Total word count: 3130; Total number of tables: 2; Total number of figures: 3; Number of references: 32

---

## 💡 一句话要点

**DeepSeek在大语言模型牙科病例分析中表现优于其他模型**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `牙科病例分析` `纵向数据` `医疗保健` `DeepSeek` `临床决策支持` `模型评估` `自然语言处理`

## 📋 核心要点

1. 现有大型语言模型在解读纵向患者叙述方面存在不足，尤其是在医疗保健领域。
2. 该研究利用牙科病例数据，评估了多个LLM在分析纵向牙周病例摘要方面的能力。
3. 实验结果表明，DeepSeek模型在忠实性和专家评分方面均优于其他模型，成为案例分析的领先LLM。

## 📝 摘要（中文）

大型语言模型（LLM）在医疗保健领域具有变革潜力，但其解读纵向患者叙述的能力尚未得到充分探索。牙科拥有丰富的结构化临床数据，为严格评估LLM的推理能力提供了独特的机会。虽然已经存在一些商业LLM，但今年早些时候备受关注的DeepSeek也加入了竞争。本研究评估了四种最先进的LLM（GPT-4o、Gemini 2.0 Flash、Copilot和DeepSeek V3）通过开放式临床任务分析纵向牙科病例摘要的能力。使用34个标准化的纵向牙周病例（包括258个问答对），我们通过自动指标和持牌牙医的盲法评估来评估模型性能。DeepSeek表现最佳，展示出卓越的忠实性（中位数得分=0.528 vs. 0.367-0.457）和更高的专家评分（中位数=4.5/5 vs. 4.0/5），且没有显著降低可读性。我们的研究将DeepSeek定位为案例分析领域领先的LLM，支持将其整合为医学教育和研究的辅助工具，并强调其作为领域特定代理的潜力。

## 🔬 方法详解

**问题定义**：论文旨在评估和比较不同大型语言模型在牙科纵向病例分析中的表现。现有方法，即其他LLM，在处理此类任务时，可能存在忠实性不足、专家评分较低等问题，无法充分满足医疗领域对准确性和可靠性的要求。

**核心思路**：论文的核心思路是通过构建标准化的纵向牙周病例数据集，并设计开放式临床任务，来系统地评估不同LLM的性能。通过自动指标和专家盲法评估，客观地比较各模型的忠实性、可读性和专家评分，从而找出最适合牙科病例分析的LLM。

**技术框架**：该研究的技术框架主要包括以下几个阶段：1) 构建标准化的纵向牙周病例数据集，包含258个问答对；2) 选择四种最先进的LLM（GPT-4o、Gemini 2.0 Flash、Copilot和DeepSeek V3）进行评估；3) 设计开放式临床任务，要求模型分析病例摘要并回答相关问题；4) 使用自动指标（如忠实性得分）和专家盲法评估来评估模型性能；5) 对比分析各模型的表现，找出最佳模型。

**关键创新**：该研究的关键创新在于：1) 首次系统地评估了多个LLM在牙科纵向病例分析中的表现；2) 采用了标准化的病例数据集和开放式临床任务，使得评估更加客观和可比；3) 结合了自动指标和专家评估，全面地评估了模型的性能。

**关键设计**：研究中使用了34个标准化的纵向牙周病例，每个病例包含多个问答对，以模拟真实的临床场景。评估指标包括忠实性得分（衡量模型回答与病例信息的匹配程度）、可读性得分（衡量模型回答的流畅性和易懂性）和专家评分（由持牌牙医进行盲法评估）。具体参数设置和损失函数等技术细节在论文中可能未详细描述，属于未知信息。

## 📊 实验亮点

实验结果表明，DeepSeek模型在牙科纵向病例分析中表现最佳，其忠实性中位数得分达到0.528，显著高于其他模型（0.367-0.457）。同时，DeepSeek的专家评分中位数也达到4.5/5，高于其他模型的4.0/5。这些数据表明，DeepSeek在处理牙科病例分析任务时具有更高的准确性和可靠性。

## 🎯 应用场景

该研究成果可应用于医学教育和研究领域，DeepSeek模型可作为辅助工具，帮助学生和研究人员更好地理解和分析牙科病例。此外，该模型还具有作为领域特定代理的潜力，可以为牙科医生提供决策支持，提高诊断和治疗的效率和准确性。未来，该研究可以扩展到其他医学领域，为更广泛的医疗保健应用提供支持。

## 📄 摘要（原文）

> Large language models (LLMs) hold transformative potential in healthcare, yet their capacity to interpret longitudinal patient narratives remains inadequately explored. Dentistry, with its rich repository of structured clinical data, presents a unique opportunity to rigorously assess LLMs' reasoning abilities. While several commercial LLMs already exist, DeepSeek, a model that gained significant attention earlier this year, has also joined the competition. This study evaluated four state-of-the-art LLMs (GPT-4o, Gemini 2.0 Flash, Copilot, and DeepSeek V3) on their ability to analyze longitudinal dental case vignettes through open-ended clinical tasks. Using 34 standardized longitudinal periodontal cases (comprising 258 question-answer pairs), we assessed model performance via automated metrics and blinded evaluations by licensed dentists. DeepSeek emerged as the top performer, demonstrating superior faithfulness (median score = 0.528 vs. 0.367-0.457) and higher expert ratings (median = 4.5/5 vs. 4.0/5), without significantly compromising readability. Our study positions DeepSeek as the leading LLM for case analysis, endorses its integration as an adjunct tool in both medical education and research, and highlights its potential as a domain-specific agent.

