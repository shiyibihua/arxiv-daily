---
layout: default
title: Grounded Vision-Language Interpreter for Integrated Task and Motion Planning
---

# Grounded Vision-Language Interpreter for Integrated Task and Motion Planning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.03270" class="toolbar-btn" target="_blank">📄 arXiv: 2506.03270v2</a>
  <a href="https://arxiv.org/pdf/2506.03270.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.03270v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.03270v2', 'Grounded Vision-Language Interpreter for Integrated Task and Motion Planning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jeremy Siburian, Keisuke Shirai, Cristian C. Beltran-Hernandez, Masashi Hamaya, Michael Görner, Atsushi Hashimoto

**分类**: cs.RO, cs.AI

**发布日期**: 2025-06-03 (更新: 2025-11-04)

**备注**: Project website: https://omron-sinicx.github.io/ViLaIn-TAMP/

---

## 💡 一句话要点

**提出ViLaIn-TAMP以解决机器人规划的安全性与可解释性问题**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `视觉-语言模型` `机器人规划` `混合规划框架` `可解释性` `安全性` `任务与运动规划` `纠正规划`

## 📋 核心要点

1. 现有的视觉-语言模型在机器人规划中缺乏安全性和可解释性，限制了其实际应用。
2. 本文提出的ViLaIn-TAMP框架结合了视觉-语言解释、任务与运动规划及纠正规划模块，旨在提高机器人行为的可验证性和可解释性。
3. 实验结果显示，ViLaIn-TAMP在成功率上比基线提高了18%，并且通过引入CP模块，成功率进一步提升了32%。

## 📝 摘要（中文）

随着视觉-语言模型的进步，语言引导的机器人规划得到了快速发展。然而，这些模型的黑箱特性往往缺乏安全保障和可解释性，限制了其在实际应用中的部署。相对而言，经典的符号规划方法提供了严格的安全验证，但在设置时需要大量专家知识。为了解决这一问题，本文提出了ViLaIn-TAMP，一个混合规划框架，旨在实现可验证、可解释和自主的机器人行为。该框架包括三个主要组件：视觉-语言解释器（ViLaIn）、模块化任务与运动规划（TAMP）系统，以及纠正规划（CP）模块。通过在烹饪领域设计具有挑战性的操作任务并进行评估，实验结果表明，ViLaIn-TAMP在平均成功率上比基线提高了18%，而添加CP模块后成功率提升了32%。

## 🔬 方法详解

**问题定义**：本文旨在解决现有视觉-语言模型在机器人规划中缺乏安全性和可解释性的问题。传统的符号规划方法虽然提供了安全验证，但需要大量的专家知识，导致实际应用受限。

**核心思路**：ViLaIn-TAMP框架通过结合视觉-语言解释器、模块化任务与运动规划系统及纠正规划模块，提供了一种新的解决方案，使得机器人能够在复杂环境中进行安全、可解释的自主规划。

**技术框架**：该框架由三个主要模块组成：1) 视觉-语言解释器（ViLaIn），将多模态输入转换为结构化问题规格；2) 模块化任务与运动规划（TAMP）系统，通过符号和几何约束推理将规格转化为可执行的轨迹序列；3) 纠正规划（CP）模块，接收失败尝试的反馈并将约束反馈给ViLaIn，以优化问题规格。

**关键创新**：ViLaIn-TAMP的主要创新在于其混合规划框架，能够在保证安全性和可解释性的同时，提升机器人自主行为的能力。这一设计与现有方法的本质区别在于其集成了反馈机制，允许动态调整规划过程。

**关键设计**：在设计中，ViLaIn模块采用了先进的多模态融合技术，TAMP系统则结合了符号推理与几何约束，CP模块则通过具体反馈不断优化规划结果。

## 📊 实验亮点

实验结果表明，ViLaIn-TAMP在平均成功率上比基线提高了18%，而引入纠正规划模块后，成功率进一步提升了32%。这些结果展示了该框架在复杂操作任务中的显著优势，验证了其有效性。

## 🎯 应用场景

该研究具有广泛的应用潜力，尤其是在复杂的机器人操作任务中，如家庭服务、工业自动化和医疗辅助等领域。通过提高机器人规划的安全性和可解释性，ViLaIn-TAMP能够在实际应用中更好地满足用户需求，推动智能机器人技术的进一步发展。

## 📄 摘要（原文）

> While recent advances in vision-language models have accelerated the development of language-guided robot planners, their black-box nature often lacks safety guarantees and interpretability crucial for real-world deployment. Conversely, classical symbolic planners offer rigorous safety verification but require significant expert knowledge for setup. To bridge the current gap, this paper proposes ViLaIn-TAMP, a hybrid planning framework for enabling verifiable, interpretable, and autonomous robot behaviors. ViLaIn-TAMP comprises three main components: (1) a Vision-Language Interpreter (ViLaIn) adapted from previous work that converts multimodal inputs into structured problem specifications, (2) a modular Task and Motion Planning (TAMP) system that grounds these specifications in actionable trajectory sequences through symbolic and geometric constraint reasoning, and (3) a corrective planning (CP) module which receives concrete feedback on failed solution attempts and feed them with constraints back to ViLaIn to refine the specification. We design challenging manipulation tasks in a cooking domain and evaluate our framework. Experimental results demonstrate that ViLaIn-TAMP outperforms a VLM-as-a-planner baseline by 18% in mean success rate, and that adding the CP module boosts mean success rate by 32%.

