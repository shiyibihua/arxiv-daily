---
layout: default
title: Compressor-VLA: Instruction-Guided Visual Token Compression for Efficient Robotic Manipulation
---

# Compressor-VLA: Instruction-Guided Visual Token Compression for Efficient Robotic Manipulation

**arXiv**: [2511.18950v1](https://arxiv.org/abs/2511.18950) | [PDF](https://arxiv.org/pdf/2511.18950.pdf)

**作者**: Juntao Gao, Feiyang Ye, Jing Zhang, Wenjing Qian

**分类**: cs.RO, cs.CV, cs.LG

**发布日期**: 2025-11-24

**备注**: 11 pages, 5 figures

---

## 💡 一句话要点

**提出Compressor-VLA，通过指令引导的视觉Token压缩提升机器人操作效率。**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)**

**关键词**: `机器人操作` `视觉语言动作模型` `Token压缩` `指令引导` `具身智能`

## 📋 核心要点

1. VLA模型计算开销大，冗余视觉Token处理是实时机器人部署的瓶颈，传统Token剪枝方法难以保留任务关键信息。
2. Compressor-VLA通过指令调节，动态压缩视觉Token，同时保留全局上下文和精细空间信息，实现高效任务导向的视觉信息处理。
3. 实验表明，Compressor-VLA在LIBERO基准测试中表现出色，显著降低了FLOPs和Token数量，并在真实机器人上验证了其有效性。

## 📝 摘要（中文）

视觉-语言-动作(VLA)模型已成为具身智能领域的重要范式。然而，处理冗余视觉Token所带来的巨大计算开销仍然是实时机器人部署的关键瓶颈。虽然标准的Token剪枝技术可以缓解这个问题，但这些与任务无关的方法难以保留任务关键的视觉信息。为了解决这个问题，同时保留整体上下文和精细细节以实现精确动作，我们提出Compressor-VLA，这是一种新颖的混合指令条件Token压缩框架，专为VLA模型中视觉信息的有效、面向任务的压缩而设计。所提出的Compressor-VLA框架由两个Token压缩模块组成：语义任务压缩器(STC)，用于提取整体的、与任务相关的上下文；以及空间细化压缩器(SRC)，用于保留精细的空间细节。这种压缩由自然语言指令动态调节，从而允许自适应地浓缩与任务相关的视觉信息。实验结果表明，Compressor-VLA在LIBERO基准测试中实现了具有竞争力的成功率，同时与基线相比，FLOPs减少了59%，视觉Token数量减少了3倍以上。在双臂机器人平台上的真实机器人部署验证了该模型的sim-to-real可迁移性和实际适用性。此外，定性分析表明，我们的指令引导动态地将模型的感知焦点转移到与任务相关的对象上，从而验证了我们方法的有效性。

## 🔬 方法详解

**问题定义**：论文旨在解决视觉-语言-动作(VLA)模型在机器人操作中计算开销过大的问题。现有Token剪枝方法无法有效区分任务相关的关键视觉信息，导致性能下降。因此，需要一种能够根据任务指令自适应压缩视觉Token，同时保留重要信息的方案。

**核心思路**：核心思路是利用自然语言指令引导视觉Token的压缩过程，使模型能够动态地关注与任务相关的视觉信息。通过这种方式，模型可以有效地去除冗余信息，同时保留执行任务所需的关键上下文和细节。这种指令引导的压缩方法能够提升模型的效率和性能。

**技术框架**：Compressor-VLA框架包含两个主要的Token压缩模块：语义任务压缩器(STC)和空间细化压缩器(SRC)。STC负责提取整体的、与任务相关的上下文信息，而SRC负责保留精细的空间细节。自然语言指令作为这两个模块的输入，动态地调节压缩过程。整个框架的目标是生成一个压缩后的视觉表示，该表示既包含全局的任务上下文，又包含局部的重要细节。

**关键创新**：关键创新在于指令引导的混合Token压缩方法。与传统的任务无关的Token剪枝方法不同，Compressor-VLA能够根据自然语言指令动态地调整压缩策略，从而更好地保留任务相关的视觉信息。这种方法能够显著提升VLA模型在机器人操作任务中的效率和性能。

**关键设计**：STC和SRC的具体网络结构未知，但关键在于它们都以自然语言指令作为输入，并利用指令信息来指导Token的压缩过程。损失函数的设计也至关重要，需要确保压缩后的视觉表示能够保留足够的任务相关信息，以便模型能够成功执行机器人操作任务。具体的参数设置和网络结构细节在论文中可能有所描述，但此处信息不足，无法详细说明。

## 📊 实验亮点

Compressor-VLA在LIBERO基准测试中取得了显著的性能提升，与基线模型相比，FLOPs降低了59%，视觉Token数量减少了3倍以上，同时保持了具有竞争力的成功率。真实机器人部署验证了该模型的sim-to-real可迁移性和实际应用价值。定性分析表明，指令引导能够有效地引导模型关注任务相关的对象。

## 🎯 应用场景

该研究成果可广泛应用于各种机器人操作任务，例如家庭服务机器人、工业自动化机器人和医疗机器人等。通过降低计算开销，可以使VLA模型在资源受限的平台上运行，从而实现更智能、更高效的机器人操作。此外，该方法还可以促进机器人与人类的自然交互，提升用户体验。

## 📄 摘要（原文）

> Vision-Language-Action (VLA) models have emerged as a powerful paradigm in Embodied AI. However, the significant computational overhead of processing redundant visual tokens remains a critical bottleneck for real-time robotic deployment. While standard token pruning techniques can alleviate this, these task-agnostic methods struggle to preserve task-critical visual information. To address this challenge, simultaneously preserving both the holistic context and fine-grained details for precise action, we propose Compressor-VLA, a novel hybrid instruction-conditioned token compression framework designed for efficient, task-oriented compression of visual information in VLA models. The proposed Compressor-VLA framework consists of two token compression modules: a Semantic Task Compressor (STC) that distills holistic, task-relevant context, and a Spatial Refinement Compressor (SRC) that preserves fine-grained spatial details. This compression is dynamically modulated by the natural language instruction, allowing for the adaptive condensation of task-relevant visual information. Experimentally, extensive evaluations demonstrate that Compressor-VLA achieves a competitive success rate on the LIBERO benchmark while reducing FLOPs by 59% and the visual token count by over 3x compared to its baseline. The real-robot deployments on a dual-arm robot platform validate the model's sim-to-real transferability and practical applicability. Moreover, qualitative analyses reveal that our instruction guidance dynamically steers the model's perceptual focus toward task-relevant objects, thereby validating the effectiveness of our approach.

