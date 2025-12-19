---
layout: default
title: OS-Oracle: A Comprehensive Framework for Cross-Platform GUI Critic Models
---

# OS-Oracle: A Comprehensive Framework for Cross-Platform GUI Critic Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.16295" class="toolbar-btn" target="_blank">📄 arXiv: 2512.16295v1</a>
  <a href="https://arxiv.org/pdf/2512.16295.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.16295v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.16295v1', 'OS-Oracle: A Comprehensive Framework for Cross-Platform GUI Critic Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zhenyu Wu, Jingjing Xie, Zehao Li, Bowen Yang, Qiushi Sun, Zhaoyang Liu, Zhoumianze Liu, Yu Qiao, Xiangyu Yue, Zun Wang, Zichen Ding

**分类**: cs.AI

**发布日期**: 2025-12-18

**🔗 代码/项目**: [GITHUB](https://github.com/numbmelon/OS-Oracle)

---

## 💡 一句话要点

**提出OS-Oracle框架，用于跨平台GUI智能体的决策评估与优化**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)**

**关键词**: `GUI智能体` `决策评估` `Critic模型` `跨平台` `数据合成`

## 📋 核心要点

1. 现有计算机使用智能体在GUI操作中面临步级决策可靠性问题，长流程任务易出错。
2. OS-Oracle通过构建数据管道、设计训练范式和建立评估基准来解决GUI智能体的决策评估问题。
3. OS-Oracle-7B在OS-Critic Bench上达到SOTA，并提升了UI-TARS-1.5-7B等智能体的性能。

## 📝 摘要（中文）

随着VLM驱动的计算机使用智能体(CUA)在图形用户界面(GUI)导航和操作方面能力不断增强，可靠的步级决策已成为实际部署的关键瓶颈。在长流程任务中，错误会迅速累积，不可逆操作可能导致意外后果，因此需要评估每次操作的critic模型。然而，缺乏多样化、高质量的GUI反馈数据和用于计算机使用中步级评估的公共critic基准阻碍了critic模型的有效性。为了弥合这些差距，我们引入了OS-Oracle，它做出了三个核心贡献：(1)用于合成跨平台GUI critic数据的可扩展数据管道；(2)结合监督微调(SFT)和一致性保持的组相对策略优化(CP-GRPO)的两阶段训练范式；(3)OS-Critic Bench，一个用于评估移动、Web和桌面平台上的critic模型性能的整体基准。利用此框架，我们整理了一个包含31万个critic样本的高质量数据集。由此产生的critic模型OS-Oracle-7B在OS-Critic Bench上实现了开源VLM中的最先进性能，并在移动领域超越了专有模型。此外，当作为pre-critic时，OS-Oracle-7B提高了原生GUI智能体（如UI-TARS-1.5-7B）在OSWorld和AndroidWorld环境中的性能。代码已开源。

## 🔬 方法详解

**问题定义**：论文旨在解决计算机使用智能体（CUAs）在图形用户界面（GUI）交互中，由于缺乏可靠的步级决策能力而导致的错误累积问题。现有方法缺乏高质量的GUI反馈数据和统一的评估基准，难以训练和评估有效的critic模型，从而限制了CUAs在实际应用中的部署。

**核心思路**：论文的核心思路是构建一个全面的框架，包括数据生成、模型训练和性能评估三个方面，以提升GUI智能体的决策能力。通过合成高质量的跨平台GUI critic数据，设计有效的训练范式，并建立统一的评估基准，从而训练出能够准确评估每一步操作的critic模型。

**技术框架**：OS-Oracle框架包含三个主要组成部分：1) 可扩展的数据管道，用于合成跨平台GUI critic数据；2) 两阶段训练范式，包括监督微调（SFT）和一致性保持的组相对策略优化（CP-GRPO）；3) OS-Critic Bench，一个用于评估critic模型性能的综合基准，涵盖移动、Web和桌面平台。数据管道负责生成训练数据，两阶段训练范式用于训练critic模型，OS-Critic Bench用于评估模型的性能。

**关键创新**：论文的关键创新在于构建了一个完整的、可扩展的框架，用于解决GUI智能体的决策评估问题。具体包括：1) 提出了一个可扩展的数据管道，能够合成高质量的跨平台GUI critic数据，解决了数据稀缺的问题；2) 设计了一种两阶段训练范式，结合了监督微调和一致性保持的组相对策略优化，提高了模型的训练效率和性能；3) 构建了一个综合的评估基准OS-Critic Bench，能够全面评估critic模型在不同平台上的性能。

**关键设计**：在数据生成方面，论文设计了自动化的数据收集和标注流程，以保证数据的质量和多样性。在模型训练方面，论文采用了两阶段训练范式，首先使用监督微调（SFT）对模型进行预训练，然后使用一致性保持的组相对策略优化（CP-GRPO）对模型进行微调，以提高模型的泛化能力。在评估方面，论文构建了OS-Critic Bench，包含多个任务和评估指标，能够全面评估critic模型的性能。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16295v1/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16295v1/x2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16295v1/x3.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

OS-Oracle-7B在OS-Critic Bench上实现了开源VLM中的SOTA性能，并在移动领域超越了专有模型。作为pre-critic，OS-Oracle-7B显著提升了UI-TARS-1.5-7B等原生GUI智能体在OSWorld和AndroidWorld环境中的性能。这些结果表明OS-Oracle框架在提升GUI智能体决策能力方面的有效性。

## 🎯 应用场景

OS-Oracle框架可应用于各种需要GUI交互的智能体系统中，例如自动化测试、智能助手、机器人流程自动化（RPA）等。通过提升智能体的决策能力，可以减少错误操作，提高工作效率，并降低人工干预的需求。该研究的成果有助于推动计算机使用智能体在实际场景中的广泛应用。

## 📄 摘要（原文）

> With VLM-powered computer-using agents (CUAs) becoming increasingly capable at graphical user interface (GUI) navigation and manipulation, reliable step-level decision-making has emerged as a key bottleneck for real-world deployment. In long-horizon workflows, errors accumulate quickly and irreversible actions can cause unintended consequences, motivating critic models that assess each action before execution. While critic models offer a promising solution, their effectiveness is hindered by the lack of diverse, high-quality GUI feedback data and public critic benchmarks for step-level evaluation in computer use. To bridge these gaps, we introduce OS-Oracle that makes three core contributions: (1) a scalable data pipeline for synthesizing cross-platform GUI critic data; (2) a two-stage training paradigm combining supervised fine-tuning (SFT) and consistency-preserving group relative policy optimization (CP-GRPO); (3) OS-Critic Bench, a holistic benchmark for evaluating critic model performance across Mobile, Web, and Desktop platforms. Leveraging this framework, we curate a high-quality dataset containing 310k critic samples. The resulting critic model, OS-Oracle-7B, achieves state-of-the-art performance among open-source VLMs on OS-Critic Bench, and surpasses proprietary models on the mobile domain. Furthermore, when serving as a pre-critic, OS-Oracle-7B improves the performance of native GUI agents such as UI-TARS-1.5-7B in OSWorld and AndroidWorld environments. The code is open-sourced at https://github.com/numbmelon/OS-Oracle.

