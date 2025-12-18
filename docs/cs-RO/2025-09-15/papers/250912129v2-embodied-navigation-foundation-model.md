---
layout: default
title: Embodied Navigation Foundation Model
---

# Embodied Navigation Foundation Model

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.12129" class="toolbar-btn" target="_blank">📄 arXiv: 2509.12129v2</a>
  <a href="https://arxiv.org/pdf/2509.12129.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.12129v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.12129v2', 'Embodied Navigation Foundation Model')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jiazhao Zhang, Anqi Li, Yunpeng Qi, Minghan Li, Jiahang Liu, Shaoan Wang, Haoran Liu, Gengze Zhou, Yuze Wu, Xingxing Li, Yuxin Fan, Wenjun Li, Zhibo Chen, Fei Gao, Qi Wu, Zhizheng Zhang, He Wang

**分类**: cs.RO

**发布日期**: 2025-09-15 (更新: 2025-09-16)

**备注**: Project Page: https://pku-epic.github.io/NavFoM-Web/

---

## 💡 一句话要点

**提出跨具身、跨任务的导航基础模型NavFoM，提升具身智能导航的泛化能力。**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱七：动作重定向 (Motion Retargeting)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `具身智能` `导航基础模型` `跨具身` `跨任务` `视觉语言导航` `Transformer` `多模态学习`

## 📋 核心要点

1. 现有视觉语言模型在具身导航中的泛化能力受限于特定任务和具身架构，难以适应复杂环境。
2. NavFoM通过统一架构处理多模态输入，并引入标识符token嵌入相机视图和时间上下文信息，提升泛化性。
3. 实验表明，NavFoM在多个导航任务和具身机器人上取得了领先性能，无需任务特定微调，并验证了实际应用潜力。

## 📝 摘要（中文）

本文提出了一种跨具身和跨任务的导航基础模型(NavFoM)，该模型在包含四足机器人、无人机、轮式机器人和车辆的八百万导航样本上进行训练，涵盖了视觉语言导航、物体搜索、目标跟踪和自动驾驶等多种任务。NavFoM采用统一的架构，处理来自不同相机配置和导航范围的多模态导航输入。为了适应不同的相机设置和时间范围，NavFoM集成了标识符token，嵌入了具身机器人的相机视图信息和任务的时间上下文。此外，为了满足实际部署的需求，NavFoM在有限的token长度预算下，使用动态调整的采样策略来控制所有观察token。在公共基准上的大量评估表明，我们的模型在多个导航任务和具身机器人上实现了最先进或极具竞争力的性能，而无需特定于任务的微调。额外的真实世界实验进一步证实了该方法的强大泛化能力和实际适用性。

## 🔬 方法详解

**问题定义**：现有具身导航方法，特别是基于视觉语言模型的方法，在泛化能力上存在局限性。它们通常针对特定任务和特定的具身机器人架构进行优化，难以适应不同类型的机器人（如四足机器人、无人机、轮式机器人等）和不同的导航任务（如视觉语言导航、物体搜索、目标跟踪等）。这种缺乏通用性的问题限制了具身智能在实际场景中的应用。

**核心思路**：NavFoM的核心思路是构建一个通用的导航基础模型，通过大规模的多样化数据训练，使其能够适应不同的具身机器人和导航任务。该模型采用统一的架构来处理来自不同相机配置和导航范围的多模态导航输入，并通过引入标识符token来嵌入相机视图信息和任务的时间上下文，从而提高模型的泛化能力。

**技术框架**：NavFoM的整体架构包含以下几个主要模块：1) 多模态输入处理模块：负责处理来自不同传感器（如摄像头、激光雷达等）的输入数据，并将其转换为统一的表示形式。2) 标识符Token嵌入模块：将相机视图信息和任务的时间上下文编码为标识符token，并将其与输入数据融合。3) Transformer编码器：使用Transformer编码器对融合后的数据进行编码，提取特征。4) 动态Token采样模块：在有限的token长度预算下，动态调整采样策略，选择重要的观察token。5) 导航策略输出模块：根据编码后的特征，输出导航策略。

**关键创新**：NavFoM的关键创新在于以下几个方面：1) 跨具身和跨任务的统一架构：能够处理不同类型的机器人和导航任务。2) 标识符token嵌入：能够嵌入相机视图信息和任务的时间上下文，提高模型的泛化能力。3) 动态Token采样：能够在有限的token长度预算下，选择重要的观察token，提高模型的效率。

**关键设计**：NavFoM的关键设计包括：1) 使用Transformer作为核心编码器，以捕捉输入数据之间的长距离依赖关系。2) 设计了专门的标识符token，用于编码相机视图信息和任务的时间上下文。3) 采用动态Token采样策略，根据token的重要性动态调整采样概率。4) 使用大规模的多样化数据集进行训练，以提高模型的泛化能力。

## 📊 实验亮点

NavFoM在多个公共基准测试中取得了最先进或极具竞争力的性能，无需针对特定任务进行微调。例如，在视觉语言导航任务中，NavFoM的性能超过了现有最佳方法。此外，真实世界的实验也验证了NavFoM的泛化能力和实际应用潜力，证明了其在复杂环境中的有效性。

## 🎯 应用场景

NavFoM具有广泛的应用前景，可应用于自动驾驶、物流配送、家庭服务机器人、安防巡检等领域。通过预训练的NavFoM，可以快速部署到新的机器人平台和导航任务中，降低开发成本，加速具身智能的落地。未来，可以进一步探索NavFoM在更复杂环境和任务中的应用，例如灾难救援、医疗辅助等。

## 📄 摘要（原文）

> Navigation is a fundamental capability in embodied AI, representing the intelligence required to perceive and interact within physical environments following language instructions. Despite significant progress in large Vision-Language Models (VLMs), which exhibit remarkable zero-shot performance on general vision-language tasks, their generalization ability in embodied navigation remains largely confined to narrow task settings and embodiment-specific architectures. In this work, we introduce a cross-embodiment and cross-task Navigation Foundation Model (NavFoM), trained on eight million navigation samples that encompass quadrupeds, drones, wheeled robots, and vehicles, and spanning diverse tasks such as vision-and-language navigation, object searching, target tracking, and autonomous driving. NavFoM employs a unified architecture that processes multimodal navigation inputs from varying camera configurations and navigation horizons. To accommodate diverse camera setups and temporal horizons, NavFoM incorporates identifier tokens that embed camera view information of embodiments and the temporal context of tasks. Furthermore, to meet the demands of real-world deployment, NavFoM controls all observation tokens using a dynamically adjusted sampling strategy under a limited token length budget. Extensive evaluations on public benchmarks demonstrate that our model achieves state-of-the-art or highly competitive performance across multiple navigation tasks and embodiments without requiring task-specific fine-tuning. Additional real-world experiments further confirm the strong generalization capability and practical applicability of our approach.

