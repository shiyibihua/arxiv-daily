---
layout: default
title: "MM-UAVBench: How Well Do Multimodal Large Language Models See, Think, and Plan in Low-Altitude UAV Scenarios?"
---

# MM-UAVBench: How Well Do Multimodal Large Language Models See, Think, and Plan in Low-Altitude UAV Scenarios?

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.23219" class="toolbar-btn" target="_blank">📄 arXiv: 2512.23219v1</a>
  <a href="https://arxiv.org/pdf/2512.23219.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.23219v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.23219v1', 'MM-UAVBench: How Well Do Multimodal Large Language Models See, Think, and Plan in Low-Altitude UAV Scenarios?')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Shiqi Dai, Zizhi Ma, Zhicong Luo, Xuesong Yang, Yibin Huang, Wanyue Zhang, Chi Chen, Zonghao Guo, Wang Xu, Yufei Sun, Maosong Sun

**分类**: cs.CV

**发布日期**: 2025-12-29

**备注**: 25 pages

---

## 💡 一句话要点

**提出MM-UAVBench，评估多模态大语言模型在低空无人机场景下的感知、认知和规划能力。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多模态大语言模型` `无人机` `低空场景` `基准测试` `感知` `认知` `规划` `空间推理`

## 📋 核心要点

1. 现有MLLM基准测试缺乏对低空无人机场景的针对性评估，无法有效反映模型在此类复杂环境下的性能。
2. MM-UAVBench通过构建包含感知、认知和规划三个维度的综合评估体系，系统地测试MLLM在低空无人机场景中的能力。
3. 实验结果表明，现有MLLM在低空场景中面临空间偏差和多视角理解等挑战，性能有待提升。

## 📝 摘要（中文）

多模态大语言模型(MLLMs)在各个领域展现了卓越的通用智能，但其在无人机(UAV)主导的低空应用中的潜力尚未得到充分探索。现有的MLLM基准测试很少涵盖低空场景的独特挑战，而与UAV相关的评估主要集中在定位或导航等特定任务上，缺乏对MLLM通用智能的统一评估。为了弥合这一差距，我们提出了MM-UAVBench，这是一个全面的基准，系统地评估了MLLM在低空UAV场景中的三个核心能力维度——感知、认知和规划。MM-UAVBench包含19个子任务，包含超过5.7K个手动标注的问题，所有问题都来自公共数据集收集的真实UAV数据。对16个开源和专有MLLM的大量实验表明，当前的模型难以适应低空场景的复杂视觉和认知需求。我们的分析进一步揭示了空间偏差和多视角理解等关键瓶颈，这些瓶颈阻碍了MLLM在UAV场景中的有效部署。我们希望MM-UAVBench能够促进未来对鲁棒且可靠的MLLM在实际UAV智能方面的研究。

## 🔬 方法详解

**问题定义**：论文旨在解决多模态大语言模型(MLLM)在低空无人机(UAV)场景下应用效果评估不足的问题。现有MLLM基准测试很少关注低空环境的特殊性，而UAV相关的研究又过于关注特定任务，缺乏对MLLM通用智能的全面评估。这导致我们难以了解现有MLLM在实际UAV应用中的潜力和局限性。

**核心思路**：论文的核心思路是构建一个专门针对低空UAV场景的综合性基准测试集MM-UAVBench。通过设计一系列涵盖感知、认知和规划三个核心能力维度的子任务，系统地评估MLLM在处理低空UAV数据时的表现。这种方法能够更全面地揭示MLLM在UAV应用中的优势和不足，为未来的研究提供指导。

**技术框架**：MM-UAVBench的整体框架包括数据收集、任务设计和模型评估三个主要阶段。首先，从公共数据集中收集真实的UAV图像和视频数据。然后，基于这些数据设计19个子任务，涵盖感知（例如目标检测、场景理解）、认知（例如推理、常识判断）和规划（例如路径规划、任务调度）三个维度。最后，使用这些子任务评估多个开源和专有的MLLM，并分析其性能瓶颈。

**关键创新**：MM-UAVBench的关键创新在于其针对低空UAV场景的特殊设计。与现有的通用MLLM基准测试不同，MM-UAVBench更加关注低空环境的复杂性和挑战，例如视角变化、光照变化和遮挡等。此外，MM-UAVBench还引入了规划任务，这在现有的MLLM基准测试中相对较少。

**关键设计**：MM-UAVBench包含19个子任务，每个子任务都包含多个手动标注的问题。这些问题旨在测试MLLM在不同方面的能力，例如识别不同类型的目标、理解场景中的关系、进行逻辑推理和制定合理的计划。为了确保评估的公平性和可靠性，论文作者对所有问题进行了仔细的审查和验证。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.23219v1/x4.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.23219v1/x1.png" alt="img_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.23219v1/x2.png" alt="img_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

在MM-UAVBench上对16个MLLM的实验结果表明，现有模型在低空UAV场景中表现不佳，尤其是在空间推理和多视角理解方面。例如，模型在处理视角变化较大的图像时，目标识别的准确率显著下降。这些结果揭示了现有MLLM在UAV应用中的局限性，为未来的研究指明了方向。

## 🎯 应用场景

该研究成果可应用于多种低空无人机应用场景，例如智能巡检、环境监测、灾害救援和物流配送等。通过评估和改进MLLM在这些场景下的性能，可以提高无人机的自主性和智能化水平，从而提升工作效率和安全性。未来，该基准测试集可以促进更多针对无人机应用的MLLM研究。

## 📄 摘要（原文）

> While Multimodal Large Language Models (MLLMs) have exhibited remarkable general intelligence across diverse domains, their potential in low-altitude applications dominated by Unmanned Aerial Vehicles (UAVs) remains largely underexplored. Existing MLLM benchmarks rarely cover the unique challenges of low-altitude scenarios, while UAV-related evaluations mainly focus on specific tasks such as localization or navigation, without a unified evaluation of MLLMs'general intelligence. To bridge this gap, we present MM-UAVBench, a comprehensive benchmark that systematically evaluates MLLMs across three core capability dimensions-perception, cognition, and planning-in low-altitude UAV scenarios. MM-UAVBench comprises 19 sub-tasks with over 5.7K manually annotated questions, all derived from real-world UAV data collected from public datasets. Extensive experiments on 16 open-source and proprietary MLLMs reveal that current models struggle to adapt to the complex visual and cognitive demands of low-altitude scenarios. Our analyses further uncover critical bottlenecks such as spatial bias and multi-view understanding that hinder the effective deployment of MLLMs in UAV scenarios. We hope MM-UAVBench will foster future research on robust and reliable MLLMs for real-world UAV intelligence.

