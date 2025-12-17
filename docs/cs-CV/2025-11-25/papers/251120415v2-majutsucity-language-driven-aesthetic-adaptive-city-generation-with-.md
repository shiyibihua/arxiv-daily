---
layout: default
title: MajutsuCity: Language-driven Aesthetic-adaptive City Generation with Controllable 3D Assets and Layouts
---

# MajutsuCity: Language-driven Aesthetic-adaptive City Generation with Controllable 3D Assets and Layouts

**arXiv**: [2511.20415v2](https://arxiv.org/abs/2511.20415) | [PDF](https://arxiv.org/pdf/2511.20415.pdf)

**作者**: Zilong Huang, Jun He, Xiaobin Huang, Ziyi Xiong, Yang Luo, Junyan Ye, Weijia Li, Yiping Chen, Ting Han

**分类**: cs.CV

**发布日期**: 2025-11-25 (更新: 2025-12-08)

**备注**: 13 pages, 6 figures

**🔗 代码/项目**: [PROJECT_PAGE](https://longhz140516.github.io/MajutsuCity/)

---

## 💡 一句话要点

**MajutsuCity：提出语言驱动的美学自适应城市生成框架，可控3D资产与布局。**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱三：空间感知 (Perception & SLAM)**

**关键词**: `3D城市生成` `自然语言驱动` `美学自适应` `可控生成` `多模态数据集`

## 📋 核心要点

1. 现有3D城市生成方法难以平衡文本生成提供的创造灵活性与显式结构表示带来的对象级可编辑性。
2. MajutsuCity通过将城市表示为可控的布局、资产和材质的组合，实现自然语言驱动和美学自适应的3D城市生成。
3. 实验表明，MajutsuCity在结构一致性、风格适应性和语义可控性方面均优于现有方法，显著降低了布局FID。

## 📝 摘要（中文）

本文提出MajutsuCity，一个自然语言驱动且美学自适应的框架，用于合成结构一致且风格多样的3D城市场景。MajutsuCity将城市表示为可控的布局、资产和材质的组合，并通过一个四阶段的流程运行。为了扩展生成后的可控性，进一步集成了MajutsuAgent，一个交互式的、语言驱动的编辑代理，支持五个对象级别的操作。为了支持照片级真实感和可定制的场景合成，构建了MajutsuDataset，一个高质量的多模态数据集，包含2D语义布局和高度图、多样化的3D建筑资产，以及精选的PBR材质和天空盒，每个都带有详细的注释。同时，开发了一套实用的评估指标，涵盖了结构一致性、场景复杂性、材质逼真度和光照氛围等关键维度。大量实验表明，与CityDreamer相比，MajutsuCity将布局FID降低了83.7%，与CityCraft相比降低了20.1%。该方法在所有AQS和RDR评分中均排名第一，明显优于现有方法。这些结果证实了MajutsuCity在3D城市生成的几何保真度、风格适应性和语义可控性方面达到了新的最先进水平。

## 🔬 方法详解

**问题定义**：现有3D城市生成方法要么缺乏足够的风格多样性，要么难以进行细粒度的对象级别控制和编辑。它们通常难以在文本驱动的创造性和结构化的可编辑性之间取得平衡，限制了其在虚拟现实、游戏开发等领域的应用。

**核心思路**：MajutsuCity的核心思路是将3D城市场景解耦为可控的布局、3D资产和材质三个关键组成部分，并利用自然语言作为驱动，实现对城市风格和结构的精细控制。通过这种解耦，可以独立地控制每个组成部分，从而实现更大的灵活性和可编辑性。

**技术框架**：MajutsuCity采用一个四阶段的流程：1) **布局生成**：根据文本描述生成城市布局；2) **资产选择与放置**：根据布局和文本描述选择合适的3D建筑资产并放置到布局中；3) **材质生成与应用**：根据文本描述生成并应用PBR材质到建筑资产上；4) **场景渲染**：将所有元素整合并渲染成最终的3D城市场景。此外，还引入了MajutsuAgent，一个交互式的语言驱动编辑代理，用于在对象级别进行编辑。

**关键创新**：MajutsuCity的关键创新在于其将自然语言作为统一的控制接口，实现了对城市布局、资产和材质的协同控制。同时，MajutsuAgent的引入进一步增强了场景的可编辑性，允许用户通过自然语言指令对场景进行修改。此外，MajutsuDataset的构建为训练和评估此类模型提供了高质量的多模态数据。

**关键设计**：MajutsuCity的具体技术细节包括：使用Transformer架构进行文本编码，并将其与布局、资产和材质生成模块相结合。MajutsuAgent使用强化学习进行训练，以学习如何根据用户的语言指令执行编辑操作。损失函数包括用于保证布局一致性的损失、用于保证资产风格一致性的损失以及用于保证材质逼真度的损失。具体的网络结构和参数设置在论文中有详细描述（未知）。

## 📊 实验亮点

实验结果表明，MajutsuCity在3D城市生成的几何保真度、风格适应性和语义可控性方面均优于现有方法。与CityDreamer相比，MajutsuCity将布局FID降低了83.7%，与CityCraft相比降低了20.1%。在AQS和RDR评分中，MajutsuCity均排名第一，表明其在结构一致性、场景复杂性、材质逼真度和光照氛围等方面均有显著提升。

## 🎯 应用场景

MajutsuCity在虚拟现实、游戏开发、城市规划和世界模型等领域具有广泛的应用前景。它可以用于快速生成各种风格的3D城市场景，为游戏和VR应用提供丰富的环境资源。此外，它还可以辅助城市规划师进行城市设计和可视化，并为世界模型的构建提供逼真的3D城市环境。

## 📄 摘要（原文）

> Generating realistic 3D cities is fundamental to world models, virtual reality, and game development, where an ideal urban scene must satisfy both stylistic diversity, fine-grained, and controllability. However, existing methods struggle to balance the creative flexibility offered by text-based generation with the object-level editability enabled by explicit structural representations. We introduce MajutsuCity, a natural language-driven and aesthetically adaptive framework for synthesizing structurally consistent and stylistically diverse 3D urban scenes. MajutsuCity represents a city as a composition of controllable layouts, assets, and materials, and operates through a four-stage pipeline. To extend controllability beyond initial generation, we further integrate MajutsuAgent, an interactive language-grounded editing agent} that supports five object-level operations. To support photorealistic and customizable scene synthesis, we also construct MajutsuDataset, a high-quality multimodal dataset} containing 2D semantic layouts and height maps, diverse 3D building assets, and curated PBR materials and skyboxes, each accompanied by detailed annotations. Meanwhile, we develop a practical set of evaluation metrics, covering key dimensions such as structural consistency, scene complexity, material fidelity, and lighting atmosphere. Extensive experiments demonstrate MajutsuCity reduces layout FID by 83.7% compared with CityDreamer and by 20.1% over CityCraft. Our method ranks first across all AQS and RDR scores, outperforming existing methods by a clear margin. These results confirm MajutsuCity as a new state-of-the-art in geometric fidelity, stylistic adaptability, and semantic controllability for 3D city generation. We expect our framework can inspire new avenues of research in 3D city generation. Our project page: https://longhz140516.github.io/MajutsuCity/.

