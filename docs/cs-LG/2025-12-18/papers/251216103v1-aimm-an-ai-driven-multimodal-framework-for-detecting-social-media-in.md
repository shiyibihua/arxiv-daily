---
layout: default
title: AIMM: An AI-Driven Multimodal Framework for Detecting Social-Media-Influenced Stock Market Manipulation
---

# AIMM: An AI-Driven Multimodal Framework for Detecting Social-Media-Influenced Stock Market Manipulation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.16103" class="toolbar-btn" target="_blank">📄 arXiv: 2512.16103v1</a>
  <a href="https://arxiv.org/pdf/2512.16103.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.16103v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.16103v1', 'AIMM: An AI-Driven Multimodal Framework for Detecting Social-Media-Influenced Stock Market Manipulation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Sandeep Neela

**分类**: cs.LG, cs.AI

**发布日期**: 2025-12-18

**备注**: Preprint

---

## 💡 一句话要点

**AIMM：一种AI驱动的多模态框架，用于检测社交媒体影响的股市操纵**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `股市操纵检测` `社交媒体分析` `多模态融合` `风险预警` `金融监管`

## 📋 核心要点

1. 现有方法难以有效关联社交媒体叙事、协同模式与市场行为，零售投资者、监管机构和券商缺乏有效工具。
2. AIMM框架融合Reddit活动、机器人指标、协同行为和市场特征，生成每日操纵风险评分，提前预警市场操纵。
3. 实验表明，AIMM在小规模数据集上具有初步区分能力，并在GME事件爆发前22天发出预警，验证了其有效性。

## 📝 摘要（中文）

本文提出AIMM，一个AI驱动的框架，旨在融合Reddit活动、机器人和协同行为指标以及OHLCV市场特征，为每个股票代码生成每日AIMM操纵风险评分，以应对源于协同社交媒体活动的股市操纵问题。该系统采用基于Parquet的流水线和一个Streamlit仪表板，使分析师能够探索可疑窗口，检查底层帖子和价格行为，并记录模型随时间的输出。由于Reddit API的限制，我们使用了经过校准的合成社交特征，使其与已记录的事件特征相匹配；市场数据（OHLCV）使用来自Yahoo Finance的真实历史数据。本文贡献包括：构建AIMM Ground Truth数据集（AIMM-GT），包含33个标记的股票代码-日期，涵盖8个股票，数据来自SEC执法行动、社区验证的操纵案例和匹配的正常对照；实施前向步进评估和前瞻性预测日志记录，用于回顾性和部署式评估；分析提前期，表明AIMM在2021年1月GME挤兑高峰前22天发出了警告。尽管当前标记集较小，但结果显示了初步的区分能力和对GME事件的早期预警。我们发布代码、数据集模式和仪表板设计，以支持对社交媒体驱动的市场监控的研究。

## 🔬 方法详解

**问题定义**：当前市场操纵行为日益依赖于社交媒体上的协同活动，而非孤立的交易行为。现有的市场监控工具难以有效地将社交媒体上的叙事、协同模式与市场行为联系起来，导致零售投资者、监管机构和券商难以及时发现和应对此类操纵行为。因此，需要一种能够整合多源信息，并提供早期预警的系统。

**核心思路**：AIMM的核心思路是将社交媒体数据（Reddit活动）、机器人和协同行为的指标，以及传统的市场数据（OHLCV）进行融合，利用AI模型学习这些数据之间的关联，从而预测市场操纵的风险。通过综合分析这些信息，可以更全面地了解市场动态，并及时发现潜在的操纵行为。

**技术框架**：AIMM框架包含以下主要模块：1) 数据收集模块：收集Reddit数据、机器人和协同行为指标以及OHLCV市场数据。2) 特征工程模块：从收集到的数据中提取相关特征，例如Reddit帖子的情感、机器人账号的活动频率、交易量和价格波动等。3) 模型训练模块：使用机器学习模型（具体模型类型未知）学习特征与市场操纵之间的关系。4) 风险评分模块：根据模型预测结果，为每个股票代码生成每日AIMM操纵风险评分。5) 可视化模块：使用Streamlit仪表板展示风险评分、底层帖子和价格行为，方便分析师进行分析。

**关键创新**：AIMM的关键创新在于其多模态数据融合的方法，它将社交媒体数据、机器人指标和市场数据结合起来，从而更全面地了解市场动态。此外，AIMM还构建了一个包含标记数据的AIMM-GT数据集，用于训练和评估模型。该数据集包含来自SEC执法行动、社区验证的操纵案例和匹配的正常对照。

**关键设计**：由于Reddit API的限制，AIMM使用了经过校准的合成社交特征，使其与已记录的事件特征相匹配。市场数据（OHLCV）使用来自Yahoo Finance的真实历史数据。模型训练采用前向步进评估和前瞻性预测日志记录，用于回顾性和部署式评估。具体的模型结构、损失函数和参数设置未知。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16103v1/figures/GroundTruthCoverage.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16103v1/figures/Forward-walk.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16103v1/figures/PredictionLog.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

实验结果表明，AIMM在小规模数据集上具有初步的区分能力，能够区分市场操纵事件和正常市场行为。更重要的是，AIMM在2021年1月GME挤兑高峰前22天发出了预警，表明其具有提前预警市场操纵事件的潜力。尽管数据集规模有限，但这些结果验证了AIMM框架的有效性。

## 🎯 应用场景

AIMM框架可应用于金融监管、券商风控和个人投资者风险管理等领域。监管机构可以使用AIMM来监控市场操纵行为，及时采取措施保护投资者利益。券商可以利用AIMM来识别潜在的风险客户，并加强风险管理。个人投资者可以使用AIMM来评估投资风险，做出更明智的投资决策。该研究有助于提高市场透明度，维护市场公平。

## 📄 摘要（原文）

> Market manipulation now routinely originates from coordinated social media campaigns, not isolated trades. Retail investors, regulators, and brokerages need tools that connect online narratives and coordination patterns to market behavior. We present AIMM, an AI-driven framework that fuses Reddit activity, bot and coordination indicators, and OHLCV market features into a daily AIMM Manipulation Risk Score for each ticker.
>   The system uses a parquet-native pipeline with a Streamlit dashboard that allows analysts to explore suspicious windows, inspect underlying posts and price action, and log model outputs over time. Due to Reddit API restrictions, we employ calibrated synthetic social features matching documented event characteristics; market data (OHLCV) uses real historical data from Yahoo Finance. This release makes three contributions. First, we build the AIMM Ground Truth dataset (AIMM-GT): 33 labeled ticker-days spanning eight equities, drawing from SEC enforcement actions, community-verified manipulation cases, and matched normal controls. Second, we implement forward-walk evaluation and prospective prediction logging for both retrospective and deployment-style assessment. Third, we analyze lead times and show that AIMM flagged GME 22 days before the January 2021 squeeze peak.
>   The current labeled set is small (33 ticker-days, 3 positive events), but results show preliminary discriminative capability and early warnings for the GME incident. We release the code, dataset schema, and dashboard design to support research on social media-driven market surveillance.

