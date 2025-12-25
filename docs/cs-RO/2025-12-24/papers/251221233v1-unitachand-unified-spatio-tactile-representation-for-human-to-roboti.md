---
layout: default
title: "UniTacHand: Unified Spatio-Tactile Representation for Human to Robotic Hand Skill Transfer"
---

# UniTacHand: Unified Spatio-Tactile Representation for Human to Robotic Hand Skill Transfer

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.21233" class="toolbar-btn" target="_blank">📄 arXiv: 2512.21233v1</a>
  <a href="https://arxiv.org/pdf/2512.21233.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.21233v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.21233v1', 'UniTacHand: Unified Spatio-Tactile Representation for Human to Robotic Hand Skill Transfer')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Chi Zhang, Penglin Cai, Haoqi Yuan, Chaoyi Xu, Zongqing Lu

**分类**: cs.RO

**发布日期**: 2025-12-24

---

## 💡 一句话要点

**UniTacHand：用于人-机器人手技能迁移的统一时空触觉表示**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱二：RL算法与架构 (RL & Architecture)** **支柱六：视频提取与匹配 (Video Extraction)** **支柱七：动作重定向 (Motion Retargeting)**

**关键词**: `触觉感知` `机器人灵巧操作` `人机协作` `迁移学习` `对比学习`

## 📋 核心要点

1. 机器人触觉数据获取成本高昂，阻碍了触觉感知在灵巧操作中的应用，尤其是在视觉受限场景。
2. UniTacHand通过将人手和机器人手的触觉信号投影到统一的MANO模型空间，并利用对比学习对齐，实现跨域迁移。
3. 实验表明，UniTacHand支持零样本策略迁移，且混合数据协同训练能提升性能和数据效率。

## 📝 摘要（中文）

触觉感知对于机器人手实现人类水平的灵巧操作至关重要，尤其是在视觉遮挡的情况下。然而，其应用常常受到大规模真实世界机器人触觉数据难以收集的限制。本研究提出使用触觉手套收集低成本的人类操作数据，用于基于触觉的机器人策略学习。人类和机器人触觉数据之间的不对齐使得从人类数据学习的策略难以迁移到机器人。为了弥合这一差距，我们提出了UniTacHand，一种统一的表示，用于对齐灵巧手捕获的机器人触觉信息与手套获得的人手触摸。首先，我们将来自人手和机器人手的触觉信号投影到MANO手模型的形态一致的2D表面空间上。这种统一标准化了异构数据结构，并固有地将触觉信号嵌入空间上下文。然后，我们引入了一种对比学习方法，将它们对齐到一个统一的潜在空间中，该空间仅在我们数据收集系统的10分钟配对数据上进行训练。我们的方法实现了从人类到真实机器人的零样本基于触觉的策略迁移，推广到预训练数据中未见过的对象。我们还证明，通过UniTacHand在混合数据（包括人类和机器人演示）上进行协同训练，与仅使用机器人数据相比，可以获得更好的性能和数据效率。UniTacHand为基于触觉的灵巧手的一般、可扩展和数据高效的学习铺平了道路。

## 🔬 方法详解

**问题定义**：现有机器人触觉数据难以获取，且人手和机器人手的触觉数据存在不对齐问题，导致难以将人类的灵巧操作技能迁移到机器人上。现有方法通常依赖于大量的机器人数据，成本高昂且泛化性差。

**核心思路**：UniTacHand的核心思路是将人手和机器人手的触觉信息映射到一个统一的、形态一致的表示空间，从而消除数据异构性。通过对比学习，进一步对齐不同来源的触觉特征，实现知识迁移。这样设计的原因在于，统一表示能够嵌入空间上下文，而对比学习能够学习到领域不变的特征。

**技术框架**：UniTacHand包含以下主要阶段：1) 数据收集：使用触觉手套收集人手操作数据，使用机器人手上的触觉传感器收集机器人操作数据。2) 触觉信号投影：将人手和机器人手的触觉信号投影到MANO手模型的2D表面空间上，形成统一的表示。3) 对比学习：使用对比学习方法，训练一个编码器，将统一表示映射到潜在空间，并对齐人手和机器人手的触觉特征。4) 策略迁移：将训练好的编码器用于机器人策略学习，实现从人类到机器人的零样本策略迁移。

**关键创新**：UniTacHand的关键创新在于提出了一个统一的时空触觉表示，能够有效地对齐人手和机器人手的触觉信息。与现有方法相比，UniTacHand不需要大量的机器人数据，而是利用低成本的人类数据进行训练，并通过对比学习实现跨域迁移。

**关键设计**：UniTacHand的关键设计包括：1) 使用MANO模型作为统一的2D表面空间，嵌入空间上下文。2) 使用对比学习损失函数，鼓励人手和机器人手的触觉特征在潜在空间中对齐。3) 使用少量配对数据进行对比学习训练，提高数据效率。具体的对比学习损失函数细节和网络结构未在摘要中详细说明，属于未知信息。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.21233v1/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.21233v1/x2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.21233v1/x3.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

UniTacHand实现了从人类到真实机器人的零样本触觉策略迁移，能够推广到预训练数据中未见过的物体。通过混合人类和机器人数据进行协同训练，与仅使用机器人数据相比，性能和数据效率均得到提升。具体提升幅度和性能数据在摘要中未给出，属于未知信息。

## 🎯 应用场景

UniTacHand可应用于各种需要灵巧操作的机器人任务，例如：工业自动化、医疗手术、家庭服务等。通过利用人类的知识和经验，可以降低机器人学习的成本和时间，提高机器人的智能化水平。该研究为触觉感知在机器人领域的应用开辟了新的方向，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> Tactile sensing is crucial for robotic hands to achieve human-level dexterous manipulation, especially in scenarios with visual occlusion. However, its application is often hindered by the difficulty of collecting large-scale real-world robotic tactile data. In this study, we propose to collect low-cost human manipulation data using haptic gloves for tactile-based robotic policy learning. The misalignment between human and robotic tactile data makes it challenging to transfer policies learned from human data to robots. To bridge this gap, we propose UniTacHand, a unified representation to align robotic tactile information captured by dexterous hands with human hand touch obtained from gloves. First, we project tactile signals from both human hands and robotic hands onto a morphologically consistent 2D surface space of the MANO hand model. This unification standardizes the heterogeneous data structures and inherently embeds the tactile signals with spatial context. Then, we introduce a contrastive learning method to align them into a unified latent space, trained on only 10 minutes of paired data from our data collection system. Our approach enables zero-shot tactile-based policy transfer from humans to a real robot, generalizing to objects unseen in the pre-training data. We also demonstrate that co-training on mixed data, including both human and robotic demonstrations via UniTacHand, yields better performance and data efficiency compared with using only robotic data. UniTacHand paves a path toward general, scalable, and data-efficient learning for tactile-based dexterous hands.

