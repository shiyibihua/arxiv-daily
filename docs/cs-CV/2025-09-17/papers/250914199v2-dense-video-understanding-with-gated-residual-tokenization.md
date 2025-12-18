---
layout: default
title: Dense Video Understanding with Gated Residual Tokenization
---

# Dense Video Understanding with Gated Residual Tokenization

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.14199" class="toolbar-btn" target="_blank">📄 arXiv: 2509.14199v2</a>
  <a href="https://arxiv.org/pdf/2509.14199.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.14199v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.14199v2', 'Dense Video Understanding with Gated Residual Tokenization')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Haichao Zhang, Wenhao Chai, Shwai He, Ang Li, Yun Fu

**分类**: cs.CV, cs.AI, cs.CL, cs.LG

**发布日期**: 2025-09-17 (更新: 2025-09-18)

---

## 💡 一句话要点

**提出门控残差Token化（GRT）框架，实现高效高帧率视频理解。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `视频理解` `高帧率视频` `Token化` `运动补偿` `语义分割` `大语言模型` `时序推理`

## 📋 核心要点

1. 现有视频理解模型依赖低帧率采样，忽略了视频中密集的时序信息，导致无法处理需要精细时间对齐的任务。
2. 提出门控残差Token化（GRT）框架，通过运动补偿和语义场景融合，减少Token化时间和Token冗余，实现高效的高帧率视频理解。
3. 在提出的DIVE基准测试上，GRT优于更大的VLLM基线，并表现出随帧率增加而性能提升的趋势，验证了其有效性。

## 📝 摘要（中文）

高时间分辨率对于捕捉视频理解中的细粒度细节至关重要。然而，当前的视频大语言模型（VLLM）和基准测试主要依赖于低帧率采样，例如均匀采样或关键帧选择，从而丢弃了密集的时序信息。这种折衷方案避免了对每一帧进行Token化的高成本，否则会导致冗余计算和随着视频长度增加的线性Token增长。虽然这种权衡适用于变化缓慢的内容，但它不适用于诸如讲座理解之类的任务，在这些任务中，信息几乎出现在每一帧中，并且需要精确的时间对齐。为了解决这一差距，我们引入了密集视频理解（DVU），它通过减少Token化时间和Token开销来实现高FPS视频理解。现有的基准测试也受到限制，因为它们的QA对侧重于粗略的内容更改。因此，我们提出了DIVE（密集信息视频评估），这是第一个为密集时序推理设计的基准测试。为了使DVU实用，我们提出了门控残差Token化（GRT），这是一个两阶段框架：（1）运动补偿的帧间门控Token化使用像素级运动估计来跳过Token化期间的静态区域，从而实现Token数量和计算的亚线性增长。（2）语义场景的帧内Token化合并融合场景内静态区域的Token，进一步减少冗余，同时保留动态语义。在DIVE上的实验表明，GRT优于更大的VLLM基线，并随着FPS的增加而积极扩展。这些结果突出了密集时序信息的重要性，并证明GRT能够实现高效、可扩展的高FPS视频理解。

## 🔬 方法详解

**问题定义**：现有视频理解方法为了降低计算成本，通常采用低帧率采样，忽略了视频中丰富的时序信息。这导致模型难以捕捉视频中的细微变化，无法胜任需要高时间分辨率的任务，例如讲座理解等。现有方法的痛点在于无法在计算效率和信息完整性之间取得平衡。

**核心思路**：GRT的核心思路是通过减少Token化过程中的冗余计算和Token数量，从而实现高效的高帧率视频理解。具体来说，它利用视频帧之间的运动信息和场景语义信息，跳过静态区域的Token化，并将相似的Token进行合并，从而降低计算复杂度和Token数量。这样既保留了视频中的关键信息，又避免了对每一帧都进行Token化带来的巨大开销。

**技术框架**：GRT是一个两阶段框架，包括：
1. **运动补偿的帧间门控Token化 (Motion-Compensated Inter-Gated Tokenization)**：利用像素级运动估计，识别并跳过视频帧之间的静态区域，只对运动区域进行Token化，从而减少Token数量。
2. **语义场景的帧内Token化合并 (Semantic-Scene Intra-Tokenization Merging)**：在同一场景内，将静态区域的Token进行合并，进一步减少Token冗余，同时保留动态语义信息。

**关键创新**：GRT的关键创新在于其门控残差Token化机制，它能够根据视频内容的动态程度自适应地调整Token化过程。与传统的均匀采样或关键帧选择方法相比，GRT能够更有效地保留视频中的关键信息，同时显著降低计算成本。这种方法实现了Token数量和计算量的亚线性增长，使其能够处理更长的视频序列。

**关键设计**：
* **运动估计**：采用像素级运动估计方法，例如光流法，来识别视频帧之间的运动区域。
* **门控机制**：使用门控机制来控制Token化的过程，只有当像素的运动幅度超过一定阈值时，才对其进行Token化。
* **语义场景分割**：使用语义分割模型将视频帧分割成不同的场景区域。
* **Token合并**：在同一场景内，使用聚类算法将相似的Token进行合并，例如K-means聚类。

## 📊 实验亮点

实验结果表明，GRT在DIVE基准测试上优于更大的VLLM基线。具体来说，GRT在QA任务上的准确率比现有方法提高了显著幅度，并且随着输入视频帧率的增加，GRT的性能也随之提升。这表明GRT能够有效地利用高帧率视频中的时序信息，实现更准确的视频理解。

## 🎯 应用场景

该研究成果可应用于多种视频理解场景，例如在线教育、智能监控、自动驾驶等。在在线教育中，可以用于理解讲座视频，自动生成笔记或摘要。在智能监控中，可以用于检测异常行为或事件。在自动驾驶中，可以用于理解交通场景，提高驾驶安全性。该研究的未来影响在于推动视频理解技术的发展，使其能够更好地服务于人们的生活。

## 📄 摘要（原文）

> High temporal resolution is essential for capturing fine-grained details in video understanding. However, current video large language models (VLLMs) and benchmarks mostly rely on low-frame-rate sampling, such as uniform sampling or keyframe selection, discarding dense temporal information. This compromise avoids the high cost of tokenizing every frame, which otherwise leads to redundant computation and linear token growth as video length increases. While this trade-off works for slowly changing content, it fails for tasks like lecture comprehension, where information appears in nearly every frame and requires precise temporal alignment. To address this gap, we introduce Dense Video Understanding (DVU), which enables high-FPS video comprehension by reducing both tokenization time and token overhead. Existing benchmarks are also limited, as their QA pairs focus on coarse content changes. We therefore propose DIVE (Dense Information Video Evaluation), the first benchmark designed for dense temporal reasoning. To make DVU practical, we present Gated Residual Tokenization (GRT), a two-stage framework: (1) Motion-Compensated Inter-Gated Tokenization uses pixel-level motion estimation to skip static regions during tokenization, achieving sub-linear growth in token count and compute. (2) Semantic-Scene Intra-Tokenization Merging fuses tokens across static regions within a scene, further reducing redundancy while preserving dynamic semantics. Experiments on DIVE show that GRT outperforms larger VLLM baselines and scales positively with FPS. These results highlight the importance of dense temporal information and demonstrate that GRT enables efficient, scalable high-FPS video understanding.

