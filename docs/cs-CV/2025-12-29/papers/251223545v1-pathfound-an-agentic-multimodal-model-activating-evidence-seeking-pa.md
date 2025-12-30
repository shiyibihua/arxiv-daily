---
layout: default
title: "PathFound: An Agentic Multimodal Model Activating Evidence-seeking Pathological Diagnosis"
---

# PathFound: An Agentic Multimodal Model Activating Evidence-seeking Pathological Diagnosis

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.23545" class="toolbar-btn" target="_blank">📄 arXiv: 2512.23545v1</a>
  <a href="https://arxiv.org/pdf/2512.23545.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.23545v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.23545v1', 'PathFound: An Agentic Multimodal Model Activating Evidence-seeking Pathological Diagnosis')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Shengyi Hua, Jianfeng Wu, Tianle Shen, Kangzhe Hu, Zhongzhen Huang, Shujuan Ni, Zhihong Zhang, Yuan Li, Zhe Wang, Xiaofan Zhang

**分类**: cs.CV, cs.AI

**发布日期**: 2025-12-29

---

## 💡 一句话要点

**PathFound：一种主动证据搜寻的病理诊断多模态Agent模型**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `病理诊断` `多模态学习` `主动学习` `强化学习` `证据搜寻` `视觉-语言模型` `计算病理学`

## 📋 核心要点

1. 现有病理诊断模型缺乏主动证据搜寻能力，无法模拟医生通过多次观察和检查来完善诊断的过程。
2. PathFound通过集成视觉基础模型、视觉-语言模型和强化学习推理模型，模拟医生主动搜寻证据并改进诊断的流程。
3. 实验表明，PathFound在多个大型多模态模型中提高了诊断准确性，并在不同临床场景中达到了最先进的性能。

## 📝 摘要（中文）

近期的病理学基础模型在视觉表征学习和多模态交互方面取得了显著进展。然而，大多数模型仍然依赖于静态的推理范式，即对整张切片图像进行一次处理以产生预测，而没有在诊断模糊时进行重新评估或有针对性的证据获取。这与临床诊断工作流程形成对比，后者通过重复的切片观察和进一步的检查请求来完善假设。我们提出了PathFound，一种旨在支持病理诊断中证据搜寻推理的主动多模态模型。PathFound集成了病理视觉基础模型、视觉-语言模型和使用强化学习训练的推理模型，通过初始诊断、证据搜寻和最终决策阶段，执行主动的信息获取和诊断改进。在几个大型多模态模型中，采用这种策略始终提高了诊断准确性，表明证据搜寻工作流程在计算病理学中的有效性。在这些模型中，PathFound在不同的临床场景中实现了最先进的诊断性能，并展示了发现细微细节（如核特征和局部浸润）的强大潜力。

## 🔬 方法详解

**问题定义**：现有病理诊断模型主要采用静态推理范式，即对整张切片图像进行一次性处理并给出预测，缺乏主动证据搜寻和诊断迭代的能力。这种方式无法模拟病理医生在实际诊断过程中，根据初步诊断结果，有针对性地观察特定区域或请求额外检查以获取更多证据，从而提高诊断准确性的过程。因此，如何使模型具备主动证据搜寻能力，以模拟临床诊断流程，是本文要解决的核心问题。

**核心思路**：PathFound的核心思路是将病理诊断过程建模为一个Agent与环境交互的过程。Agent（模型）通过观察切片图像，进行初步诊断，并根据诊断结果决定下一步行动（例如，观察特定区域或请求额外检查）。环境（病理切片）根据Agent的行动提供新的信息，Agent根据新的信息更新诊断结果，并重复上述过程，直到最终做出诊断决策。这种主动证据搜寻的思路旨在模拟病理医生在实际诊断中的迭代过程，从而提高诊断准确性。

**技术框架**：PathFound的技术框架主要包含三个阶段：初始诊断阶段、证据搜寻阶段和最终决策阶段。在初始诊断阶段，模型利用病理视觉基础模型对整张切片图像进行初步分析，并给出初步诊断结果。在证据搜寻阶段，模型根据初步诊断结果，利用视觉-语言模型和推理模型，决定下一步需要观察的区域或需要进行的检查。模型通过与环境交互，获取新的信息，并更新诊断结果。在最终决策阶段，模型综合所有已获取的信息，给出最终的诊断决策。

**关键创新**：PathFound的关键创新在于将病理诊断过程建模为一个Agent与环境交互的过程，并利用强化学习训练推理模型，使其具备主动证据搜寻的能力。与现有方法相比，PathFound不再局限于对整张切片图像进行一次性处理，而是能够根据诊断结果，有针对性地获取更多信息，从而提高诊断准确性。此外，PathFound还集成了病理视觉基础模型和视觉-语言模型，使其能够更好地理解病理图像和文本信息。

**关键设计**：PathFound的关键设计包括：1) 使用强化学习训练推理模型，使其能够根据诊断结果，选择最优的证据搜寻策略。2) 设计合适的奖励函数，鼓励模型获取更多有用的信息，并做出准确的诊断决策。3) 集成病理视觉基础模型和视觉-语言模型，使其能够更好地理解病理图像和文本信息。具体的网络结构和参数设置在论文中有详细描述，此处不再赘述。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.23545v1/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.23545v1/x2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.23545v1/x3.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

PathFound在多个大型多模态模型中进行了评估，结果表明，采用证据搜寻策略能够显著提高诊断准确性。PathFound在不同的临床场景中实现了最先进的诊断性能，并展示了发现细微细节（如核特征和局部浸润）的强大潜力。具体的性能数据和对比基线在论文中有详细描述。

## 🎯 应用场景

PathFound具有广泛的应用前景，可用于辅助病理医生进行诊断，提高诊断效率和准确性。该模型可以应用于各种病理诊断场景，例如肿瘤诊断、感染诊断等。此外，PathFound还可以用于病理图像的自动分析和标注，从而加速病理研究的进展。未来，PathFound有望成为病理诊断领域的重要工具。

## 📄 摘要（原文）

> Recent pathological foundation models have substantially advanced visual representation learning and multimodal interaction. However, most models still rely on a static inference paradigm in which whole-slide images are processed once to produce predictions, without reassessment or targeted evidence acquisition under ambiguous diagnoses. This contrasts with clinical diagnostic workflows that refine hypotheses through repeated slide observations and further examination requests. We propose PathFound, an agentic multimodal model designed to support evidence-seeking inference in pathological diagnosis. PathFound integrates the power of pathological visual foundation models, vision-language models, and reasoning models trained with reinforcement learning to perform proactive information acquisition and diagnosis refinement by progressing through the initial diagnosis, evidence-seeking, and final decision stages. Across several large multimodal models, adopting this strategy consistently improves diagnostic accuracy, indicating the effectiveness of evidence-seeking workflows in computational pathology. Among these models, PathFound achieves state-of-the-art diagnostic performance across diverse clinical scenarios and demonstrates strong potential to discover subtle details, such as nuclear features and local invasions.

