---
layout: default
title: Vision-Language-Action Models for Autonomous Driving: Past, Present, and Future
---

# Vision-Language-Action Models for Autonomous Driving: Past, Present, and Future

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.16760" class="toolbar-btn" target="_blank">📄 arXiv: 2512.16760v1</a>
  <a href="https://arxiv.org/pdf/2512.16760.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.16760v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.16760v1', 'Vision-Language-Action Models for Autonomous Driving: Past, Present, and Future')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Tianshuai Hu, Xiaolu Liu, Song Wang, Yiyao Zhu, Ao Liang, Lingdong Kong, Guoyang Zhao, Zeying Gong, Jun Cen, Zhiyu Huang, Xiaoshuai Hao, Linfeng Li, Hang Song, Xiangtai Li, Jun Ma, Shaojie Shen, Jianke Zhu, Dacheng Tao, Ziwei Liu, Junwei Liang

**分类**: cs.RO

**发布日期**: 2025-12-18

**备注**: Preprint; 40 pages, 7 figures, 9 tables; GitHub at https://github.com/worldbench/awesome-vla-for-ad

---

## 💡 一句话要点

**综述性论文：面向自动驾驶的视觉-语言-动作模型研究进展与未来展望**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `自动驾驶` `视觉语言动作模型` `多模态学习` `大型语言模型` `端到端学习` `双系统架构` `综述`

## 📋 核心要点

1. 传统自动驾驶依赖“感知-决策-行动”模块化流程，易受感知误差影响，且难以处理复杂场景。
2. 视觉-语言-动作（VLA）模型通过整合视觉、语言和动作，实现更可解释和通用的驾驶策略。
3. 论文综述了VLA在自动驾驶中的应用，分析了端到端和双系统两种范例，并指出了未来研究方向。

## 📝 摘要（中文）

自动驾驶长期以来依赖于模块化的“感知-决策-行动”流程，但手工设计的接口和基于规则的组件在复杂或长尾场景中经常失效。其级联设计进一步传播感知误差，降低下游规划和控制的性能。视觉-动作（VA）模型通过学习从视觉输入到动作的直接映射来解决一些局限性，但它们仍然不透明，对分布偏移敏感，并且缺乏结构化推理或指令遵循能力。大型语言模型（LLM）和多模态学习的最新进展推动了视觉-语言-动作（VLA）框架的出现，该框架将感知与基于语言的决策相结合。通过统一视觉理解、语言推理和可操作的输出，VLA为更可解释、更通用和更符合人类习惯的驾驶策略提供了一条途径。本文对新兴的自动驾驶VLA领域进行了结构化描述，追溯了从早期VA方法到现代VLA框架的演变，并将现有方法组织成两种主要范例：端到端VLA和双系统VLA。总结了用于评估VLA驾驶系统的代表性数据集和基准，并强调了关键挑战和开放方向，包括鲁棒性、可解释性和指令保真度。总的来说，这项工作旨在为推进与人类兼容的自动驾驶系统奠定连贯的基础。

## 🔬 方法详解

**问题定义**：传统自动驾驶系统依赖于模块化的“感知-决策-行动”流程，这些流程存在多个问题。首先，手工设计的接口和规则在复杂或长尾场景中容易失效。其次，级联的设计会导致感知误差向下游传播，影响规划和控制的准确性。此外，早期的视觉-动作（VA）模型虽然能够直接从视觉输入映射到动作，但缺乏可解释性，对数据分布的变化非常敏感，并且缺乏结构化的推理能力和指令遵循能力。

**核心思路**：论文的核心思路是利用大型语言模型（LLM）和多模态学习的最新进展，构建视觉-语言-动作（VLA）框架，将视觉感知与基于语言的决策相结合。通过统一视觉理解、语言推理和可执行的动作输出，VLA旨在实现更可解释、更通用、更符合人类习惯的自动驾驶策略。这种方法的核心在于利用语言作为桥梁，连接视觉感知和动作执行，从而提高系统的鲁棒性和泛化能力。

**技术框架**：论文将现有的VLA方法组织成两种主要的范例：端到端VLA和双系统VLA。端到端VLA将感知、推理和规划整合到一个单一的模型中，直接从视觉输入生成动作。双系统VLA则将慢速的推理（通过视觉语言模型）与快速、安全关键的执行（通过规划器）分离。在这些范例中，又进一步区分了文本动作生成器与数值动作生成器，以及显式指导机制与隐式指导机制。

**关键创新**：论文的关键创新在于对自动驾驶领域的VLA模型进行了系统的分类和分析，并提出了端到端VLA和双系统VLA两种主要范例。这种分类方法有助于研究人员更好地理解不同VLA模型的优缺点，并为未来的研究方向提供了指导。此外，论文还强调了VLA模型在可解释性、通用性和指令保真度方面的优势，这些优势是传统自动驾驶系统所不具备的。

**关键设计**：论文没有涉及具体的模型设计细节，而侧重于对现有VLA框架的综述和分类。因此，没有具体的参数设置、损失函数或网络结构等技术细节可以描述。论文主要关注的是不同VLA框架的整体架构和流程，以及它们在自动驾驶任务中的应用。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16760v1/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16760v1/x2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16760v1/figures/fig3.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

该论文是一篇综述性文章，没有具体的实验结果。其亮点在于对现有VLA模型进行了系统的分类和分析，提出了端到端VLA和双系统VLA两种主要范例，并指出了未来研究的关键挑战和开放方向，例如鲁棒性、可解释性和指令保真度。该综述为研究人员提供了一个全面的VLA模型发展概况，并为未来的研究方向提供了指导。

## 🎯 应用场景

该研究对自动驾驶领域具有重要的应用价值。VLA模型能够提升自动驾驶系统的可解释性、通用性和鲁棒性，使其在复杂和未知的环境中更好地运行。未来的发展方向包括提高VLA模型的指令遵循能力、增强其对长尾场景的处理能力，以及实现更安全可靠的自动驾驶系统。这项研究也将推动人机交互在自动驾驶领域的应用，使车辆能够更好地理解和响应人类的指令。

## 📄 摘要（原文）

> Autonomous driving has long relied on modular "Perception-Decision-Action" pipelines, where hand-crafted interfaces and rule-based components often break down in complex or long-tailed scenarios. Their cascaded design further propagates perception errors, degrading downstream planning and control. Vision-Action (VA) models address some limitations by learning direct mappings from visual inputs to actions, but they remain opaque, sensitive to distribution shifts, and lack structured reasoning or instruction-following capabilities. Recent progress in Large Language Models (LLMs) and multimodal learning has motivated the emergence of Vision-Language-Action (VLA) frameworks, which integrate perception with language-grounded decision making. By unifying visual understanding, linguistic reasoning, and actionable outputs, VLAs offer a pathway toward more interpretable, generalizable, and human-aligned driving policies. This work provides a structured characterization of the emerging VLA landscape for autonomous driving. We trace the evolution from early VA approaches to modern VLA frameworks and organize existing methods into two principal paradigms: End-to-End VLA, which integrates perception, reasoning, and planning within a single model, and Dual-System VLA, which separates slow deliberation (via VLMs) from fast, safety-critical execution (via planners). Within these paradigms, we further distinguish subclasses such as textual vs. numerical action generators and explicit vs. implicit guidance mechanisms. We also summarize representative datasets and benchmarks for evaluating VLA-based driving systems and highlight key challenges and open directions, including robustness, interpretability, and instruction fidelity. Overall, this work aims to establish a coherent foundation for advancing human-compatible autonomous driving systems.

