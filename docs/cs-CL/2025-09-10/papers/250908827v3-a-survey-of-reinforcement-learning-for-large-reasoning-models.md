---
layout: default
title: A Survey of Reinforcement Learning for Large Reasoning Models
---

# A Survey of Reinforcement Learning for Large Reasoning Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.08827" class="toolbar-btn" target="_blank">📄 arXiv: 2509.08827v3</a>
  <a href="https://arxiv.org/pdf/2509.08827.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.08827v3" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.08827v3', 'A Survey of Reinforcement Learning for Large Reasoning Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Kaiyan Zhang, Yuxin Zuo, Bingxiang He, Youbang Sun, Runze Liu, Che Jiang, Yuchen Fan, Kai Tian, Guoli Jia, Pengfei Li, Yu Fu, Xingtai Lv, Yuchen Zhang, Sihang Zeng, Shang Qu, Haozhan Li, Shijie Wang, Yuru Wang, Xinwei Long, Fangfu Liu, Xiang Xu, Jiaze Ma, Xuekai Zhu, Ermo Hua, Yihao Liu, Zonglin Li, Huayu Chen, Xiaoye Qu, Yafu Li, Weize Chen, Zhenzhao Yuan, Junqi Gao, Dong Li, Zhiyuan Ma, Ganqu Cui, Zhiyuan Liu, Biqing Qi, Ning Ding, Bowen Zhou

**分类**: cs.CL, cs.AI, cs.LG

**发布日期**: 2025-09-10 (更新: 2025-10-09)

**备注**: Fixed typos; added missing and recent citations (117 -> 120 pages)

**🔗 代码/项目**: [GITHUB](https://github.com/TsinghuaC3I/Awesome-RL-for-LRMs)

---

## 💡 一句话要点

**综述：强化学习驱动的大型推理模型研究进展**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `强化学习` `大型语言模型` `推理能力` `综述` `深度学习`

## 📋 核心要点

1. 现有大型语言模型在复杂推理任务中面临挑战，需要更有效的训练方法。
2. 利用强化学习（RL）训练LLM，使其具备更强的推理能力，是解决该问题的核心思路。
3. 该综述全面回顾了RL在LLM推理能力提升方面的研究进展，并展望了未来发展方向。

## 📝 摘要（中文）

本文综述了近年来强化学习（RL）在增强大型语言模型（LLM）推理能力方面的最新进展。RL在提升LLM能力方面取得了显著成功，尤其是在解决数学和编程等复杂逻辑任务方面。因此，RL已成为将LLM转化为大型推理模型（LRM）的基础方法。随着该领域的快速发展，进一步扩展RL以应用于LRM不仅面临计算资源方面的挑战，还在算法设计、训练数据和基础设施方面面临基础性挑战。为此，重新审视该领域的发展历程，重新评估其发展轨迹，并探索增强RL可扩展性的策略以实现人工超智能（ASI）正当其时。特别是，我们研究了将RL应用于LLM和LRM以提高推理能力的研究，尤其是在DeepSeek-R1发布之后，包括基础组件、核心问题、训练资源和下游应用，以识别这个快速发展领域的未来机遇和方向。我们希望这篇综述能够促进未来对更广泛推理模型的RL研究。

## 🔬 方法详解

**问题定义**：论文旨在解决如何利用强化学习（RL）提升大型语言模型（LLM）的推理能力的问题。现有方法在处理复杂逻辑任务，如数学和编程时，仍存在不足，需要更有效的训练策略和算法设计。此外，随着模型规模的增大，计算资源、训练数据和基础设施也成为限制RL应用于LRM的瓶颈。

**核心思路**：论文的核心思路是综述当前利用RL提升LLM推理能力的研究进展，并分析其面临的挑战和未来的发展方向。通过对现有方法的梳理和总结，为后续研究提供参考，并促进RL在更广泛推理模型中的应用。

**技术框架**：该论文是一篇综述，其技术框架主要体现在对现有研究的分类和总结上。它涵盖了RL应用于LLM推理的基础组件、核心问题、训练资源和下游应用等方面。通过对这些方面的分析，论文试图构建一个完整的RL for LRM的知识体系。

**关键创新**：该论文的关键创新在于对RL在LLM推理领域应用的全面综述和未来方向的展望。它不仅总结了现有方法的优点和不足，还指出了未来研究可能面临的挑战和机遇，为后续研究提供了重要的参考价值。

**关键设计**：该论文的关键设计在于其对现有研究的分类和组织方式。它从基础组件、核心问题、训练资源和下游应用等多个维度对RL for LRM的研究进行了梳理，使得读者能够更清晰地了解该领域的发展现状和未来趋势。

## 📊 实验亮点

该综述重点关注了DeepSeek-R1发布后，RL在LLM推理能力提升方面的研究进展，涵盖了基础组件、核心问题、训练资源和下游应用等多个方面。通过对现有研究的梳理和总结，为后续研究提供了重要的参考价值，并指出了未来研究可能面临的挑战和机遇。

## 🎯 应用场景

该研究对开发具有更强推理能力的人工智能系统具有重要意义。潜在应用领域包括智能助手、自动化编程、科学研究等。通过提升LLM的推理能力，可以使其更好地理解和解决复杂问题，从而在各个领域发挥更大的作用。

## 📄 摘要（原文）

> In this paper, we survey recent advances in Reinforcement Learning (RL) for reasoning with Large Language Models (LLMs). RL has achieved remarkable success in advancing the frontier of LLM capabilities, particularly in addressing complex logical tasks such as mathematics and coding. As a result, RL has emerged as a foundational methodology for transforming LLMs into LRMs. With the rapid progress of the field, further scaling of RL for LRMs now faces foundational challenges not only in computational resources but also in algorithm design, training data, and infrastructure. To this end, it is timely to revisit the development of this domain, reassess its trajectory, and explore strategies to enhance the scalability of RL toward Artificial SuperIntelligence (ASI). In particular, we examine research applying RL to LLMs and LRMs for reasoning abilities, especially since the release of DeepSeek-R1, including foundational components, core problems, training resources, and downstream applications, to identify future opportunities and directions for this rapidly evolving area. We hope this review will promote future research on RL for broader reasoning models. Github: https://github.com/TsinghuaC3I/Awesome-RL-for-LRMs

