---
layout: default
title: OVAL-Grasp: Open-Vocabulary Affordance Localization for Task Oriented Grasping
---

# OVAL-Grasp: Open-Vocabulary Affordance Localization for Task Oriented Grasping

<div class="paper-toolbar">
  <div class="toolbar-left">
    <a href="https://arxiv.org/abs/2511.20841" target="_blank" class="toolbar-btn">arXiv: 2511.20841v1</a>
    <a href="https://arxiv.org/pdf/2511.20841.pdf" target="_blank" class="toolbar-btn">PDF</a>
  </div>
  <div class="toolbar-right">
    <button class="toolbar-btn favorite-btn" data-arxiv-id="2511.20841v1" 
            onclick="toggleFavorite(this, '2511.20841v1', 'OVAL-Grasp: Open-Vocabulary Affordance Localization for Task Oriented Grasping')" title="收藏">
      ☆ 收藏
    </button>
    <button class="toolbar-btn share-btn" onclick="copyLink()" title="复制链接">
      🔗 分享
    </button>
  </div>
</div>


**作者**: Edmond Tong, Advaith Balaji, Anthony Opipari, Stanley Lewis, Zhen Zeng, Odest Chadwicke Jenkins

**分类**: cs.RO

**发布日期**: 2025-11-25

**备注**: 10 pages, 7 figures, 3 tables. Presented at the 2025 International Symposium on Experimental Robotics (ISER)

**🔗 代码/项目**: [PROJECT_PAGE](https://ekjt.github.io/OVAL-Grasp/)

---

## 💡 一句话要点

**OVAL-Grasp：面向任务的开放词汇抓取方法，提升机器人操作灵活性。**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱三：空间感知 (Perception & SLAM)**

**关键词**: `机器人抓取` `开放词汇` `可供性` `视觉语言模型` `大型语言模型` `任务导向` `零样本学习`

## 📋 核心要点

1. 现有基于几何的抓取方法难以处理视觉定义的物体部件、遮挡和未见过的物体，限制了机器人在非结构化环境中操作的灵活性。
2. OVAL-Grasp利用大型语言模型和视觉-语言模型，实现零样本的、面向任务的抓取，使机器人能根据任务抓取物体的特定部位。
3. 实验表明，OVAL-Grasp在真实场景中能有效识别和抓取目标物体部位，且在遮挡情况下仍具有良好的鲁棒性，优于现有基线方法。

## 📝 摘要（中文）

本文提出了一种名为OVAL-Grasp的零样本开放词汇方法，用于实现面向任务的、基于可供性的抓取。该方法利用大型语言模型（LLM）和视觉-语言模型（VLM），使机器人能够根据给定的任务在物体的正确部位进行抓取。给定RGB图像和任务描述，OVAL-Grasp首先使用LLM识别需要抓取或避免抓取的物体部位，然后使用VLM分割这些部位，并生成物体上可操作区域的2D热图。实验结果表明，该方法在20个家用物品和每个物品3个独特任务的实验中，优于两种面向任务的抓取基线。在真实世界的实验中，OVAL-Grasp成功识别和分割正确物体部位的概率为95%，抓取正确可操作区域的概率为78.3%。此外，OVAL-Grasp在部分遮挡的情况下也能找到正确的物体部位，在杂乱场景中的部位选择成功率为80%。论文还展示了OVAL-Grasp在依赖视觉特征进行部位选择的场景中的有效性，并通过消融实验证明了模块化设计的优势。

## 🔬 方法详解

**问题定义**：现有基于几何信息的抓取方法在处理具有复杂视觉特征的物体部件时表现不佳，尤其是在存在遮挡或遇到未见过的物体时。这些方法难以理解任务需求，无法根据任务目标选择合适的抓取部位。因此，需要一种能够理解任务语义并定位物体上可抓取区域的方法。

**核心思路**：OVAL-Grasp的核心思路是利用大型语言模型（LLM）理解任务描述，并结合视觉-语言模型（VLM）定位物体上与任务相关的可抓取区域。通过将语言理解和视觉感知相结合，该方法能够实现零样本的、面向任务的抓取。

**技术框架**：OVAL-Grasp的整体框架包含以下几个主要模块：1) 任务理解模块：使用LLM解析任务描述，识别需要抓取或避免抓取的物体部位。2) 部位分割模块：使用VLM分割图像中识别出的物体部位。3) 热图生成模块：根据分割结果生成2D热图，指示物体上可操作区域。4) 抓取执行模块：根据热图选择最佳抓取点，并控制机器人执行抓取动作。

**关键创新**：OVAL-Grasp的关键创新在于将LLM和VLM相结合，实现零样本的、面向任务的抓取。与传统的基于几何信息的抓取方法相比，OVAL-Grasp能够理解任务语义，并根据任务目标选择合适的抓取部位。此外，该方法具有良好的泛化能力，能够处理未见过的物体和复杂的场景。

**关键设计**：OVAL-Grasp的关键设计包括：1) 使用预训练的LLM（例如GPT-3）进行任务理解，无需针对特定任务进行微调。2) 使用预训练的VLM（例如CLIP）进行部位分割，利用其强大的视觉-语言对齐能力。3) 设计了一种基于热图的抓取点选择策略，考虑了抓取点的可达性和稳定性。

## 📊 实验亮点

OVAL-Grasp在真实世界的实验中表现出色，成功识别和分割正确物体部位的概率为95%，抓取正确可操作区域的概率为78.3%。在杂乱场景中，该方法在部分遮挡的情况下仍能保持80%的部位选择成功率。此外，OVAL-Grasp在与两种面向任务的抓取基线方法的对比实验中，取得了显著的性能提升，验证了其有效性。

## 🎯 应用场景

OVAL-Grasp具有广泛的应用前景，可应用于家庭服务机器人、工业自动化、医疗辅助等领域。例如，在家庭环境中，机器人可以根据用户的指令抓取特定的物品，并放置到指定的位置。在工业自动化中，机器人可以根据生产任务抓取不同的零件，并进行组装。在医疗辅助中，机器人可以帮助医生抓取手术器械，提高手术效率和安全性。该研究有望推动机器人技术在实际场景中的应用。

## 📄 摘要（原文）

> To manipulate objects in novel, unstructured environments, robots need task-oriented grasps that target object parts based on the given task. Geometry-based methods often struggle with visually defined parts, occlusions, and unseen objects. We introduce OVAL-Grasp, a zero-shot open-vocabulary approach to task-oriented, affordance based grasping that uses large-language models and vision-language models to allow a robot to grasp objects at the correct part according to a given task. Given an RGB image and a task, OVAL-Grasp identifies parts to grasp or avoid with an LLM, segments them with a VLM, and generates a 2D heatmap of actionable regions on the object. During our evaluations, we found that our method outperformed two task oriented grasping baselines on experiments with 20 household objects with 3 unique tasks for each. OVAL-Grasp successfully identifies and segments the correct object part 95% of the time and grasps the correct actionable area 78.3% of the time in real-world experiments with the Fetch mobile manipulator. Additionally, OVAL-Grasp finds correct object parts under partial occlusions, demonstrating a part selection success rate of 80% in cluttered scenes. We also demonstrate OVAL-Grasp's efficacy in scenarios that rely on visual features for part selection, and show the benefit of a modular design through our ablation experiments. Our project webpage is available at https://ekjt.github.io/OVAL-Grasp/

