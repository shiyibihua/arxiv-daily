---
layout: default
title: A systematic review of trial-matching pipelines using large language models
---

# A systematic review of trial-matching pipelines using large language models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.19327" class="toolbar-btn" target="_blank">📄 arXiv: 2509.19327v1</a>
  <a href="https://arxiv.org/pdf/2509.19327.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.19327v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.19327v1', 'A systematic review of trial-matching pipelines using large language models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Braxton A. Morrison, Madhumita Sushil, Jacob S. Young

**分类**: cs.CL, cs.AI

**发布日期**: 2025-09-13

**备注**: 28 pages, 3 figures

---

## 💡 一句话要点

**利用大型语言模型进行临床试验匹配的系统性综述研究**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `临床试验匹配` `大型语言模型` `自然语言处理` `GPT-4` `系统性综述`

## 📋 核心要点

1. 人工临床试验匹配耗时且易错，阻碍新疗法的发现和患者招募。
2. 本研究系统性地综述了基于大型语言模型（LLM）的临床试验匹配方法，旨在提高匹配效率和准确性。
3. 研究发现GPT-4在匹配和资格提取方面表现优异，但同时也指出了数据、成本和伦理等方面的挑战。

## 📝 摘要（中文）

将患者与临床试验选项进行匹配对于发现新的治疗方法至关重要，尤其是在肿瘤学领域。然而，手动匹配既费力又容易出错，导致招募延迟。包含大型语言模型（LLM）的流程提供了一个有希望的解决方案。本研究对2020年至2025年间发表于三个学术数据库和一个预印本服务器的研究进行了系统性综述，识别了基于LLM的临床试验匹配方法。在126篇独特的文章中，有31篇符合纳入标准。综述的研究集中于仅患者-标准匹配（n=4）、仅患者-试验匹配（n=10）、仅试验-患者匹配（n=2）、仅二元资格分类（n=1）或组合任务（n=14）。16项研究使用了合成数据；14项研究使用了真实患者数据；1项研究同时使用了两者。数据集和评估指标的差异限制了跨研究的可比性。在直接比较的研究中，GPT-4模型在匹配和资格提取方面始终优于其他模型，甚至是经过微调的模型，尽管成本更高。有希望的策略包括使用GPT-4o模型等专有LLM进行零样本提示、高级检索方法，以及在将大型模型纳入医院基础设施不可行时，对较小的开源模型进行微调以保护数据隐私。关键挑战包括访问足够大的真实世界数据集，以及与部署相关的挑战，如降低成本、减轻幻觉风险、数据泄露和偏见。本综述总结了LLM在临床试验匹配中的应用进展，强调了有希望的方向和关键限制。标准化的指标、更真实的测试集以及对成本效益和公平性的关注对于更广泛的部署至关重要。

## 🔬 方法详解

**问题定义**：临床试验匹配旨在为患者找到合适的临床试验，传统方法依赖人工，效率低且容易出错。现有方法的痛点在于数据获取困难、匹配规则复杂、以及缺乏标准化的评估体系，导致匹配结果的准确性和可信度不高。

**核心思路**：利用大型语言模型（LLM）强大的自然语言理解和生成能力，自动提取患者信息和试验标准，并进行智能匹配。核心在于将临床试验匹配问题转化为自然语言处理任务，例如文本分类、信息抽取和语义相似度计算。

**技术框架**：整体流程通常包括以下几个阶段：1) 数据预处理：清洗和标准化患者病历和临床试验方案；2) 特征提取：利用LLM提取患者特征和试验入选/排除标准；3) 匹配：基于提取的特征，使用LLM进行患者与试验的匹配，输出匹配结果和置信度；4) 评估：使用标准化的指标评估匹配结果的准确性和效率。

**关键创新**：本研究的关键创新在于系统性地综述了LLM在临床试验匹配中的应用，并指出了现有方法的局限性和未来发展方向。强调了GPT-4等大型模型在匹配和资格提取方面的优越性能，以及零样本提示和微调等策略的有效性。

**关键设计**：研究中涉及的关键设计包括：1) 如何设计有效的提示（prompt）来引导LLM进行信息抽取和匹配；2) 如何选择合适的LLM模型，例如GPT-4或开源模型；3) 如何构建标准化的评估指标，例如准确率、召回率和F1值；4) 如何解决数据隐私和安全问题，例如使用合成数据或进行联邦学习。

## 📊 实验亮点

研究表明，GPT-4模型在临床试验匹配和资格提取方面表现突出，优于其他模型，即使是经过微调的模型。零样本提示和高级检索方法也被证明是有效的策略。然而，研究也强调了数据获取、成本控制和伦理问题是实际应用中的关键挑战。

## 🎯 应用场景

该研究成果可应用于医疗机构、制药公司和研究机构，以提高临床试验招募效率，加速新药研发进程。通过自动化匹配，可以减少人工干预，降低成本，并为患者提供更多个性化的治疗选择。未来，该技术有望与电子病历系统集成，实现临床试验的智能化管理。

## 📄 摘要（原文）

> Matching patients to clinical trial options is critical for identifying novel treatments, especially in oncology. However, manual matching is labor-intensive and error-prone, leading to recruitment delays. Pipelines incorporating large language models (LLMs) offer a promising solution. We conducted a systematic review of studies published between 2020 and 2025 from three academic databases and one preprint server, identifying LLM-based approaches to clinical trial matching. Of 126 unique articles, 31 met inclusion criteria. Reviewed studies focused on matching patient-to-criterion only (n=4), patient-to-trial only (n=10), trial-to-patient only (n=2), binary eligibility classification only (n=1) or combined tasks (n=14). Sixteen used synthetic data; fourteen used real patient data; one used both. Variability in datasets and evaluation metrics limited cross-study comparability. In studies with direct comparisons, the GPT-4 model consistently outperformed other models, even finely-tuned ones, in matching and eligibility extraction, albeit at higher cost. Promising strategies included zero-shot prompting with proprietary LLMs like the GPT-4o model, advanced retrieval methods, and fine-tuning smaller, open-source models for data privacy when incorporation of large models into hospital infrastructure is infeasible. Key challenges include accessing sufficiently large real-world data sets, and deployment-associated challenges such as reducing cost, mitigating risk of hallucinations, data leakage, and bias. This review synthesizes progress in applying LLMs to clinical trial matching, highlighting promising directions and key limitations. Standardized metrics, more realistic test sets, and attention to cost-efficiency and fairness will be critical for broader deployment.

