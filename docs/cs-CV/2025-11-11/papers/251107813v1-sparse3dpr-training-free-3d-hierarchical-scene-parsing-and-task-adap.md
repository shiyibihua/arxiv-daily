---
layout: default
title: Sparse3DPR: Training-Free 3D Hierarchical Scene Parsing and Task-Adaptive Subgraph Reasoning from Sparse RGB Views
---

# Sparse3DPR: Training-Free 3D Hierarchical Scene Parsing and Task-Adaptive Subgraph Reasoning from Sparse RGB Views

<div class="paper-toolbar">
  <div class="toolbar-left">
    <a href="https://arxiv.org/abs/2511.07813" target="_blank" class="toolbar-btn">arXiv: 2511.07813v1</a>
    <a href="https://arxiv.org/pdf/2511.07813.pdf" target="_blank" class="toolbar-btn">PDF</a>
  </div>
  <div class="toolbar-right">
    <button class="toolbar-btn favorite-btn" data-arxiv-id="2511.07813v1" 
            onclick="toggleFavorite(this, '2511.07813v1', 'Sparse3DPR: Training-Free 3D Hierarchical Scene Parsing and Task-Adaptive Subgraph Reasoning from Sparse RGB Views')" title="收藏">
      ☆ 收藏
    </button>
    <button class="toolbar-btn share-btn" onclick="copyLink()" title="复制链接">
      🔗 分享
    </button>
  </div>
</div>


**作者**: Haida Feng, Hao Wei, Zewen Xu, Haolin Wang, Chade Li, Yihong Wu

**分类**: cs.CV, cs.AI

**发布日期**: 2025-11-11

---

## 💡 一句话要点

**Sparse3DPR：一种基于稀疏RGB视图的无训练3D场景分层解析与任务自适应子图推理框架**

🎯 **匹配领域**: **支柱三：空间感知 (Perception & SLAM)**

**关键词**: `3D场景理解` `大型语言模型` `无训练学习` `场景图` `平面结构`

## 📋 核心要点

1. 现有基于大型语言模型的3D场景理解方法，尤其是无训练方法，在准确性和效率方面存在挑战，限制了实际部署。
2. Sparse3DPR通过引入分层平面增强场景图和任务自适应子图提取，提升了推理链的清晰度，并减少了上下文噪声。
3. 实验表明，Sparse3DPR在Space3D-Bench上显著提升了性能和效率，并在ScanQA上取得了与训练方法相当的结果。

## 📝 摘要（中文）

本文提出Sparse3DPR，一种新颖的无训练框架，用于开放式场景理解。该框架利用预训练大型语言模型（LLM）的推理能力，仅需稀疏视角的RGB输入。具体而言，我们引入了一种分层平面增强场景图，支持开放词汇表，并采用主要平面结构作为空间锚点，从而实现更清晰的推理链和更可靠的高级推断。此外，我们设计了一种任务自适应子图提取方法，以动态过滤与查询无关的信息，减少上下文噪声，提高3D场景推理的效率和准确性。实验结果表明，Sparse3DPR具有优越性，在Space3D-Bench上，EM@1指标提升了28.7%，速度提升了78.2%（与ConceptGraphs相比）。此外，Sparse3DPR在ScanQA上获得了与基于训练的方法相当的性能，并通过额外的真实世界实验证实了其鲁棒性和泛化能力。

## 🔬 方法详解

**问题定义**：现有基于LLM的无训练3D场景理解方法，虽然具有灵活性和泛化性，但在实际应用中面临准确率低和效率不足的问题。这些方法难以有效地从稀疏的RGB视图中提取关键信息，并进行可靠的推理。

**核心思路**：Sparse3DPR的核心在于利用预训练LLM的强大推理能力，并结合精心设计的场景图表示和任务自适应子图提取策略。通过将场景表示为分层、平面增强的图结构，并动态过滤无关信息，从而提高推理的准确性和效率。

**技术框架**：Sparse3DPR框架主要包含以下几个阶段：1) **场景图构建**：从稀疏RGB视图中提取平面结构，并构建分层场景图，其中平面作为空间锚点。2) **开放词汇表支持**：利用LLM支持开放词汇表，允许对场景中的对象和关系进行灵活的描述。3) **任务自适应子图提取**：根据用户查询，动态提取与任务相关的子图，减少上下文噪声。4) **LLM推理**：利用预训练LLM对提取的子图进行推理，生成最终的场景理解结果。

**关键创新**：Sparse3DPR的关键创新在于其分层平面增强场景图和任务自适应子图提取方法。传统的场景图表示可能缺乏明确的空间结构，而Sparse3DPR通过引入平面结构作为空间锚点，增强了推理链的清晰度。此外，任务自适应子图提取能够有效地过滤无关信息，提高推理效率和准确性。

**关键设计**：在场景图构建阶段，需要精确地提取场景中的平面结构，并将其作为节点添加到场景图中。子图提取策略需要根据不同的任务进行调整，以确保提取的子图包含足够的信息，同时避免引入过多的噪声。LLM的选择和prompt设计也会影响最终的推理结果。

## 📊 实验亮点

Sparse3DPR在Space3D-Bench数据集上取得了显著的性能提升，EM@1指标提高了28.7%，速度提高了78.2%（与ConceptGraphs相比）。此外，Sparse3DPR在ScanQA数据集上获得了与基于训练的方法相当的性能，同时在真实世界实验中表现出良好的鲁棒性和泛化能力。这些结果表明，Sparse3DPR是一种高效且准确的无训练3D场景理解框架。

## 🎯 应用场景

Sparse3DPR在机器人导航、智能家居、虚拟现实和增强现实等领域具有广泛的应用前景。它可以帮助机器人理解周围环境，进行自主导航；可以用于智能家居场景中的物体识别和交互；还可以为VR/AR应用提供更逼真的3D场景理解能力。该研究有望推动3D场景理解技术的发展，并促进其在各个领域的应用。

## 📄 摘要（原文）

> Recently, large language models (LLMs) have been explored widely for 3D scene understanding. Among them, training-free approaches are gaining attention for their flexibility and generalization over training-based methods. However, they typically struggle with accuracy and efficiency in practical deployment. To address the problems, we propose Sparse3DPR, a novel training-free framework for open-ended scene understanding, which leverages the reasoning capabilities of pre-trained LLMs and requires only sparse-view RGB inputs. Specifically, we introduce a hierarchical plane-enhanced scene graph that supports open vocabulary and adopts dominant planar structures as spatial anchors, which enables clearer reasoning chains and more reliable high-level inferences. Furthermore, we design a task-adaptive subgraph extraction method to filter query-irrelevant information dynamically, reducing contextual noise and improving 3D scene reasoning efficiency and accuracy. Experimental results demonstrate the superiority of Sparse3DPR, which achieves a 28.7% EM@1 improvement and a 78.2% speedup compared with ConceptGraphs on the Space3D-Bench. Moreover, Sparse3DPR obtains comparable performance to training-based methods on ScanQA, with additional real-world experiments confirming its robustness and generalization capability.

