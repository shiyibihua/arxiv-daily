---
layout: default
title: On the Performance of LLMs for Real Estate Appraisal
---

# On the Performance of LLMs for Real Estate Appraisal

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.11812" class="toolbar-btn" target="_blank">📄 arXiv: 2506.11812v1</a>
  <a href="https://arxiv.org/pdf/2506.11812.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.11812v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.11812v1', 'On the Performance of LLMs for Real Estate Appraisal')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Margot Geerts, Manon Reusens, Bart Baesens, Seppe vanden Broucke, Jochen De Weerdt

**分类**: cs.AI, cs.CL, cs.LG

**发布日期**: 2025-06-13

**备注**: Accepted at ECML-PKDD 2025

**DOI**: [10.1007/978-3-032-06118-8_12](https://doi.org/10.1007/978-3-032-06118-8_12)

---

## 💡 一句话要点

**利用大语言模型提升房地产评估的透明度与可解释性**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大语言模型` `房地产评估` `可解释性` `上下文学习` `数据分析` `信息不对称` `机器学习`

## 📋 核心要点

1. 房地产市场存在信息不对称，传统评估方法难以满足透明性和可解释性的需求。
2. 本研究提出利用大语言模型，通过优化上下文学习策略生成房价估算，提升评估的可接近性和可解释性。
3. 实验结果显示，LLMs在利用享乐变量方面表现出色，尽管在空间推理和价格区间自信度上仍有待改进。

## 📝 摘要（中文）

房地产市场对全球经济至关重要，但存在显著的信息不对称。本研究探讨了大语言模型（LLMs）如何通过优化的上下文学习（ICL）策略，生成竞争性和可解释的房价估算，从而使房地产洞察更为普及。我们系统评估了多种国际住房数据集上的领先LLMs，比较了零-shot、few-shot、市场报告增强和混合提示技术。结果表明，LLMs有效利用了诸如房产大小和设施等享乐变量，生成有意义的估算。尽管传统机器学习模型在纯预测准确性上依然强劲，LLMs则提供了更为可访问、互动和可解释的替代方案。尽管自我解释需要谨慎解读，我们发现LLMs的预测解释与最先进模型一致，确认了其可信性。基于特征相似性和地理接近性精心选择的上下文示例显著提升了LLM的性能，但LLMs在价格区间的过度自信和有限的空间推理方面仍存在挑战。我们的研究为结构化预测任务提供了实用指导，强调了LLMs在房地产评估中提高透明度的潜力，并为利益相关者提供了可操作的洞察。

## 🔬 方法详解

**问题定义**：本研究旨在解决房地产评估中的信息不对称问题，现有方法在透明性和可解释性方面存在不足，难以为用户提供清晰的房价估算依据。

**核心思路**：论文的核心思路是利用大语言模型（LLMs）生成房价估算，通过优化的上下文学习策略，使得评估结果更具可解释性和互动性。

**技术框架**：整体架构包括数据收集、模型训练和评估三个主要阶段。首先，收集多种国际住房数据集，然后对不同的LLMs进行训练和评估，比较不同的提示技术对模型性能的影响。

**关键创新**：最重要的技术创新在于通过优化上下文示例的选择，提升LLMs在房价估算中的表现，尤其是在特征相似性和地理接近性方面的应用。与传统机器学习方法相比，LLMs提供了更为可解释和互动的评估方式。

**关键设计**：在参数设置上，研究中采用了多种提示技术，包括零-shot、few-shot和市场报告增强等，损失函数和网络结构则基于现有的LLM架构进行调整，以适应房地产评估的特定需求。

## 📊 实验亮点

实验结果表明，LLMs在利用享乐变量生成房价估算方面表现优异，尽管在空间推理和价格区间的自信度上存在不足。与传统机器学习模型相比，LLMs在可解释性和互动性上有显著提升，展示了其在房地产评估中的应用潜力。

## 🎯 应用场景

该研究的潜在应用领域包括房地产评估、市场分析和投资决策等。通过提高评估的透明度和可解释性，LLMs能够为房地产行业的利益相关者提供更为可靠的决策支持，未来可能推动房地产市场的数字化转型。

## 📄 摘要（原文）

> The real estate market is vital to global economies but suffers from significant information asymmetry. This study examines how Large Language Models (LLMs) can democratize access to real estate insights by generating competitive and interpretable house price estimates through optimized In-Context Learning (ICL) strategies. We systematically evaluate leading LLMs on diverse international housing datasets, comparing zero-shot, few-shot, market report-enhanced, and hybrid prompting techniques. Our results show that LLMs effectively leverage hedonic variables, such as property size and amenities, to produce meaningful estimates. While traditional machine learning models remain strong for pure predictive accuracy, LLMs offer a more accessible, interactive and interpretable alternative. Although self-explanations require cautious interpretation, we find that LLMs explain their predictions in agreement with state-of-the-art models, confirming their trustworthiness. Carefully selected in-context examples based on feature similarity and geographic proximity, significantly enhance LLM performance, yet LLMs struggle with overconfidence in price intervals and limited spatial reasoning. We offer practical guidance for structured prediction tasks through prompt optimization. Our findings highlight LLMs' potential to improve transparency in real estate appraisal and provide actionable insights for stakeholders.

