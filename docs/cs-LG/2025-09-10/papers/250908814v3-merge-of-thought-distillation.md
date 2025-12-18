---
layout: default
title: Merge-of-Thought Distillation
---

# Merge-of-Thought Distillation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.08814" class="toolbar-btn" target="_blank">📄 arXiv: 2509.08814v3</a>
  <a href="https://arxiv.org/pdf/2509.08814.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.08814v3" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.08814v3', 'Merge-of-Thought Distillation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zhanming Shen, Zeyu Qin, Zenan Huang, Hao Chen, Jiaqi Hu, Yihong Zhuang, Guoshan Lu, Gang Chen, Junbo Zhao

**分类**: cs.LG, cs.AI, cs.CL

**发布日期**: 2025-09-10 (更新: 2025-10-16)

---

## 💡 一句话要点

**提出Merge-of-Thought Distillation，解决长链CoT模型蒸馏中多教师冲突问题。**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `思维链蒸馏` `多教师学习` `模型融合` `知识蒸馏` `长链推理` `权重合并` `共识推理`

## 📋 核心要点

1. 现有CoT模型蒸馏依赖单一教师，忽略了多教师CoT语料库的潜力，导致学生模型性能受限。
2. 提出Merge-of-Thought Distillation (MoT)，通过交替微调和权重合并，融合多教师的推理能力。
3. 实验表明，MoT在数学推理上超越了多个强大模型，并提升了通用推理能力，降低了灾难性遗忘。

## 📝 摘要（中文）

针对长链思维（CoT）模型的高效推理蒸馏日益受到单一oracle教师假设的限制，而实际中存在多个候选教师和不断增长的CoT语料库。本文重新审视了教师选择问题，发现不同的学生有不同的“最佳教师”，甚至对于同一个学生，最佳教师也可能因数据集而异。因此，为了将多个教师的推理能力统一到一个学生中，以克服不同教师监督之间的冲突，我们提出了Merge-of-Thought Distillation（MoT），这是一个轻量级框架，在特定于教师的监督微调分支和由此产生的学生变体的权重空间合并之间交替进行。在竞赛数学基准测试中，仅使用约200个CoT样本，将MoT应用于Qwen3-14B学生模型，就超越了包括Deepseek-R1、Qwen3-32B和OpenAI-O1在内的强大模型，实现了显著的性能提升。此外，MoT始终优于最佳单教师蒸馏，在提高数学之外的通用推理能力的同时，减少了灾难性遗忘，并对分布偏移和同级教师表现出鲁棒性。最后，我们证明了MoT通过消除特定于教师的归纳偏差和教师间的冲突，同时重复加强对共识推理特征的学习，从而拥有共识CoT。这些结果表明，MoT是一种简单有效的途径，可以将来自不同教师的长CoT能力高效地提炼到紧凑的学生模型中。

## 🔬 方法详解

**问题定义**：现有长链思维（CoT）模型的知识蒸馏方法通常依赖于单一的“oracle”教师模型。然而，实际情况是存在多个CoT教师模型，并且这些教师模型之间可能存在推理上的冲突。简单地选择一个教师进行蒸馏可能会导致学生模型继承该教师的特定偏差，而忽略了其他教师的优点。因此，如何有效地利用多个教师的知识，克服教师间的冲突，提升学生模型的推理能力是一个关键问题。

**核心思路**：MoT的核心思路是通过交替进行教师特定微调和权重空间合并，从而将多个教师的推理能力融合到学生模型中。这种方法允许学生模型学习每个教师的独特视角，并通过权重合并来消除教师间的冲突，最终获得一个具有共识推理能力的模型。

**技术框架**：MoT框架包含以下主要步骤：1) 初始化学生模型；2) 对每个教师，使用其CoT数据对学生模型进行微调，得到多个特定于教师的学生模型变体；3) 将这些学生模型变体的权重进行合并，得到一个融合了多教师知识的学生模型；4) 重复步骤2和3，直到模型收敛。

**关键创新**：MoT的关键创新在于其交替微调和权重合并的策略。这种策略允许学生模型在学习每个教师的独特知识的同时，通过权重合并来消除教师间的冲突，从而获得更鲁棒和泛化的推理能力。与传统的单教师蒸馏方法相比，MoT能够更好地利用多教师的优势，提升学生模型的性能。

**关键设计**：MoT的关键设计包括：1) 教师特定微调的学习率和训练轮数；2) 权重合并的策略，例如简单的平均或更复杂的加权平均；3) 损失函数的设计，例如使用交叉熵损失或知识蒸馏损失；4) 学生模型的选择，例如选择一个与教师模型结构相似的模型或一个更小的模型。

## 📊 实验亮点

实验结果表明，在竞赛数学基准测试中，仅使用约200个CoT样本，将MoT应用于Qwen3-14B学生模型，就超越了Deepseek-R1、Qwen3-32B和OpenAI-O1等强大模型。MoT还优于最佳单教师蒸馏，提升了通用推理能力，减少了灾难性遗忘，并对分布偏移和同级教师表现出鲁棒性。

## 🎯 应用场景

MoT可应用于各种需要长链推理的场景，如数学问题求解、代码生成、知识图谱推理等。通过将多个专家模型的知识提炼到一个紧凑的学生模型中，可以降低部署成本，提高推理效率，并提升模型的鲁棒性和泛化能力。该方法在教育、金融、医疗等领域具有广泛的应用前景。

## 📄 摘要（原文）

> Efficient reasoning distillation for long chain-of-thought (CoT) models is increasingly constrained by the assumption of a single oracle teacher, despite the practical availability of multiple candidate teachers and growing CoT corpora. We revisit teacher selection and observe that different students have different "best teachers," and even for the same student, the best teacher can vary across datasets. Therefore, to unify multiple teachers' reasoning abilities into a student to overcome conflicts among various teachers' supervision, we propose Merge-of-Thought Distillation (MoT), a lightweight framework that alternates between teacher-specific supervised fine-tuning branches and weight-space merging of the resulting student variants. On competition math benchmarks, using only about 200 CoT samples, applying MoT to a Qwen3-14B student surpasses strong models including Deepseek-R1, Qwen3-32B, and OpenAI-O1, demonstrating substantial gains. Besides, MoT consistently outperforms the best single-teacher distillation, improves general reasoning beyond mathematics while reducing catastrophic forgetting, and shows robustness to distribution-shifted and peer-level teachers. Finally, we have demonstrated MoT possesses consensus CoT by eliminating teacher-specific inductive biases and inter-teacher conflicts while repeatedly reinforcing the learning of consensus reasoning features. These results position MoT as a simple, effective route to efficiently distilling long CoT capabilities from diverse teachers into compact students.

