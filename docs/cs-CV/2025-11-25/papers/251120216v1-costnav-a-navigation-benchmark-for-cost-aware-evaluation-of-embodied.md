---
layout: default
title: CostNav: A Navigation Benchmark for Cost-Aware Evaluation of Embodied Agents
---

# CostNav: A Navigation Benchmark for Cost-Aware Evaluation of Embodied Agents

<div class="paper-toolbar">
  <div class="toolbar-left">
    <a href="https://arxiv.org/abs/2511.20216" target="_blank" class="toolbar-btn">arXiv: 2511.20216v1</a>
    <a href="https://arxiv.org/pdf/2511.20216.pdf" target="_blank" class="toolbar-btn">PDF</a>
  </div>
  <div class="toolbar-right">
    <button class="toolbar-btn favorite-btn" data-arxiv-id="2511.20216v1" 
            onclick="toggleFavorite(this, '2511.20216v1', 'CostNav: A Navigation Benchmark for Cost-Aware Evaluation of Embodied Agents')" title="收藏">
      ☆ 收藏
    </button>
    <button class="toolbar-btn share-btn" onclick="copyLink()" title="复制链接">
      🔗 分享
    </button>
  </div>
</div>


**作者**: Haebin Seong, Sungmin Kim, Minchan Kim, Yongjun Cho, Myunchul Joe, Suhwan Choi, Jaeyoon Jung, Jiyong Youn, Yoonshik Kim, Samwoo Seong, Yubeen Park, Youngjae Yu, Yunsung Lee

**分类**: cs.AI, cs.CE, cs.CV, cs.LG, cs.RO

**发布日期**: 2025-11-25

---

## 💡 一句话要点

**提出CostNav以解决导航任务经济可行性评估问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱三：空间感知 (Perception & SLAM)**

**关键词**: `导航基准` `经济可行性` `自主配送` `成本分析` `碰撞避免` `具身代理` `服务水平协议` `智能物流`

## 📋 核心要点

1. 现有导航基准未能考虑经济可行性，限制了自主配送机器人的商业应用。
2. 论文提出CostNav，通过综合成本-收益分析，评估具身代理的经济效益，填补导航研究与商业部署之间的空白。
3. 实验结果显示，基线模型在服务水平协议合规率上仅为43.0%，且每次运行存在显著亏损，强调了碰撞避免的重要性。

## 📝 摘要（中文）

现有导航基准主要关注任务成功率，而忽视了经济可行性，这对自主配送机器人商业部署至关重要。我们提出了CostNav，一个微导航经济测试平台，通过全面的成本-收益分析评估具身代理，模型涵盖硬件、训练、能源、维护成本及交付收入等经济生命周期。CostNav首次定量揭示了导航研究指标与商业可行性之间的差距，表明优化任务成功与优化经济部署之间存在根本差异。我们的成本模型基于行业数据，模拟结果显示基线模型的服务水平协议合规率为43.0%，但每次运行亏损30.009美元，且没有有限的盈亏平衡点，主要由于碰撞引起的维护成本占比高达99.7%。

## 🔬 方法详解

**问题定义**：论文旨在解决现有导航基准未考虑经济可行性的问题，现有方法主要关注任务成功率，导致商业部署受限。

**核心思路**：CostNav通过建立一个微导航经济测试平台，综合考虑硬件、训练、能源和维护等成本，提供全面的经济分析，以评估具身代理的商业可行性。

**技术框架**：整体架构包括成本模型、经济生命周期模拟和服务水平协议评估。模型使用行业数据源的参数，模拟从缩小规模到实际交付的过程。

**关键创新**：CostNav是首个定量揭示导航研究指标与商业可行性之间差距的工作，强调了优化任务成功与经济部署之间的根本区别。

**关键设计**：成本模型基于行业数据，考虑了能源费率和交付服务定价，特别关注碰撞引起的维护成本，确保模型的现实性和实用性。

## 📊 实验亮点

实验结果表明，基线模型在服务水平协议合规率上仅为43.0%，每次运行亏损30.009美元，且没有有限的盈亏平衡点。这一结果突显了碰撞避免在成本控制中的关键作用，为后续研究提供了重要的优化方向。

## 🎯 应用场景

该研究的潜在应用领域包括自主配送机器人、智能物流系统和城市交通管理等。通过提供经济可行性评估，CostNav能够帮助企业在导航技术的选择和优化上做出数据驱动的决策，从而提升商业效率和降低运营成本。未来，CostNav可能推动更多基于经济效益的导航算法开发，促进智能交通系统的商业化进程。

## 📄 摘要（原文）

> Existing navigation benchmarks focus on task success metrics while overlooking economic viability -- critical for commercial deployment of autonomous delivery robots. We introduce \emph{CostNav}, a \textbf{Micro-Navigation Economic Testbed} that evaluates embodied agents through comprehensive cost-revenue analysis aligned with real-world business operations. CostNav models the complete economic lifecycle including hardware, training, energy, maintenance costs, and delivery revenue with service-level agreements, using industry-derived parameters. \textbf{To our knowledge, CostNav is the first work to quantitatively expose the gap between navigation research metrics and commercial viability}, revealing that optimizing for task success fundamentally differs from optimizing for economic deployment. Our cost model uses parameters derived from industry data sources (energy rates, delivery service pricing), and we project from a reduced-scale simulation to realistic deliveries. Under this projection, the baseline achieves 43.0\% SLA compliance but is \emph{not} commercially viable: yielding a loss of \$30.009 per run with no finite break-even point, because operating costs are dominated by collision-induced maintenance, which accounts for 99.7\% of per-run costs and highlights collision avoidance as a key optimization target. We demonstrate a learning-based on-device navigation baseline and establish a foundation for evaluating rule-based navigation, imitation learning, and cost-aware RL training. CostNav bridges the gap between navigation research and commercial deployment, enabling data-driven decisions about economic trade-offs across navigation paradigms.

