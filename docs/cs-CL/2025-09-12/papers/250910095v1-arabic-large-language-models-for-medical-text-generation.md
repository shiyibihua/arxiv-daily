---
layout: default
title: Arabic Large Language Models for Medical Text Generation
---

# Arabic Large Language Models for Medical Text Generation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.10095" class="toolbar-btn" target="_blank">📄 arXiv: 2509.10095v1</a>
  <a href="https://arxiv.org/pdf/2509.10095.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.10095v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.10095v1', 'Arabic Large Language Models for Medical Text Generation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Abdulrahman Allam, Seif Ahmed, Ali Hamdi, Ammar Mohammed

**分类**: cs.CL

**发布日期**: 2025-09-12

**备注**: Published in 2025 4th International Conference on Computer Technologies (ICCTech)

---

## 💡 一句话要点

**提出并微调阿拉伯语大型语言模型，用于生成医疗文本，辅助医院管理系统。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `阿拉伯语` `大型语言模型` `医疗文本生成` `微调` `医院管理系统`

## 📋 核心要点

1. 现有医院管理系统在处理不规则输入和欠代表性语言时，缺乏准确、实时的医疗建议能力。
2. 通过微调大型语言模型，构建阿拉伯语医疗文本生成系统，为患者提供医疗建议、诊断和治疗方案。
3. 实验结果表明，微调后的Mistral-7B模型在BERT Score指标上优于其他模型，验证了系统的有效性。

## 📝 摘要（中文）

本研究旨在通过微调大型语言模型（LLM）来解决医院管理系统（HMS）面临的挑战，如拥挤、资源有限和紧急医疗保健可用性差等问题。现有方法缺乏提供准确、实时医疗建议的能力，尤其是在处理不规则输入和代表性不足的语言时。该研究提出了一种针对阿拉伯语医疗文本生成的LLM微调方法，旨在根据用户输入为患者提供准确的医疗建议、诊断、药物推荐和治疗方案。研究收集了来自社交媒体平台的独特数据集，捕捉了患者与医生之间的真实医疗对话，并对包含多种阿拉伯语方言的数据集进行了清洗和预处理。通过微调Mistral-7B-Instruct-v0.2、LLaMA-2-7B和GPT-2 Medium等先进的生成模型，优化了系统生成可靠医疗文本的能力。评估结果表明，微调后的Mistral-7B模型优于其他模型，其BERT Score在精确率、召回率和F1分数上的平均值分别为68.5%、69.08%和68.5%。对比基准测试和定性评估验证了系统针对非正式输入生成连贯且相关的医疗回复的能力。该研究强调了生成式人工智能在推进HMS方面的潜力，为全球医疗保健挑战提供了一种可扩展且适应性强的解决方案，尤其是在语言和文化多样的环境中。

## 🔬 方法详解

**问题定义**：论文旨在解决现有医院管理系统在处理阿拉伯语医疗信息时，缺乏准确和实时的医疗建议能力的问题。现有方法难以处理非正式的患者输入，并且在阿拉伯语这种欠代表性语言上的表现不佳。这导致患者难以获得及时的医疗指导，尤其是在资源有限的情况下。

**核心思路**：论文的核心思路是利用大型语言模型（LLMs）强大的生成能力，通过在真实的阿拉伯语医疗对话数据集上进行微调，使模型能够理解并生成准确、相关的医疗建议。这种方法旨在弥合现有系统在语言理解和生成方面的差距，从而为患者提供更好的医疗服务。

**技术框架**：该研究的技术框架主要包括以下几个阶段：1) 数据收集：从社交媒体平台收集真实的患者与医生之间的阿拉伯语医疗对话数据。2) 数据预处理：对收集到的数据进行清洗、标准化和方言处理，以提高数据质量。3) 模型选择与微调：选择预训练的LLMs（如Mistral-7B-Instruct-v0.2、LLaMA-2-7B和GPT-2 Medium），并在预处理后的数据集上进行微调。4) 模型评估：使用BERT Score等指标对微调后的模型进行评估，并进行对比基准测试和定性评估。

**关键创新**：该研究的关键创新在于针对阿拉伯语医疗文本生成，对大型语言模型进行了微调。这使得模型能够更好地理解和生成阿拉伯语医疗信息，从而为阿拉伯语地区的患者提供更好的医疗服务。此外，该研究还构建了一个包含真实患者与医生对话的阿拉伯语医疗数据集，为后续研究提供了宝贵资源。

**关键设计**：在模型微调过程中，研究人员使用了标准的语言模型训练方法，例如交叉熵损失函数。具体参数设置（如学习率、batch size等）未知，但论文强调了对Mistral-7B-Instruct-v0.2、LLaMA-2-7B和GPT-2 Medium等模型的微调，并使用BERT Score进行评估。

## 📊 实验亮点

实验结果表明，经过微调的Mistral-7B模型在阿拉伯语医疗文本生成任务中表现最佳，其BERT Score在精确率、召回率和F1分数上分别达到68.5%、69.08%和68.5%。该模型优于其他基线模型，证明了该方法在生成准确和相关的阿拉伯语医疗建议方面的有效性。

## 🎯 应用场景

该研究成果可应用于智能医疗助手、在线医疗咨询平台和医院管理系统，为患者提供个性化的医疗建议和诊断，尤其是在阿拉伯语地区。该技术有助于缓解医疗资源紧张，提高医疗服务效率，并为医疗专业人员提供辅助决策支持。未来，该技术有望扩展到其他低资源语言，促进全球医疗服务的普及。

## 📄 摘要（原文）

> Efficient hospital management systems (HMS) are critical worldwide to address challenges such as overcrowding, limited resources, and poor availability of urgent health care. Existing methods often lack the ability to provide accurate, real-time medical advice, particularly for irregular inputs and underrepresented languages. To overcome these limitations, this study proposes an approach that fine-tunes large language models (LLMs) for Arabic medical text generation. The system is designed to assist patients by providing accurate medical advice, diagnoses, drug recommendations, and treatment plans based on user input. The research methodology required the collection of a unique dataset from social media platforms, capturing real-world medical conversations between patients and doctors. The dataset, which includes patient complaints together with medical advice, was properly cleaned and preprocessed to account for multiple Arabic dialects. Fine-tuning state-of-the-art generative models, such as Mistral-7B-Instruct-v0.2, LLaMA-2-7B, and GPT-2 Medium, optimized the system's ability to generate reliable medical text. Results from evaluations indicate that the fine-tuned Mistral-7B model outperformed the other models, achieving average BERT (Bidirectional Encoder Representations from Transformers) Score values in precision, recall, and F1-scores of 68.5\%, 69.08\%, and 68.5\%, respectively. Comparative benchmarking and qualitative assessments validate the system's ability to produce coherent and relevant medical replies to informal input. This study highlights the potential of generative artificial intelligence (AI) in advancing HMS, offering a scalable and adaptable solution for global healthcare challenges, especially in linguistically and culturally diverse environments.

