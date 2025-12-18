---
layout: default
title: A Foundation Model for Chest X-ray Interpretation with Grounded Reasoning via Online Reinforcement Learning
---

# A Foundation Model for Chest X-ray Interpretation with Grounded Reasoning via Online Reinforcement Learning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.03906" class="toolbar-btn" target="_blank">📄 arXiv: 2509.03906v1</a>
  <a href="https://arxiv.org/pdf/2509.03906.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.03906v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.03906v1', 'A Foundation Model for Chest X-ray Interpretation with Grounded Reasoning via Online Reinforcement Learning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Qika Lin, Yifan Zhu, Bin Pu, Ling Huang, Haoran Luo, Jingying Ma, Zhen Peng, Tianzhe Zhao, Fangzhi Xu, Jian Zhang, Kai He, Zhonghong Ou, Swapnil Mishra, Mengling Feng

**分类**: cs.AI

**发布日期**: 2025-09-04

**备注**: 15 pages

---

## 💡 一句话要点

**DeepMedix-R1：基于在线强化学习的胸部X光片可解释性基础模型**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `医学影像` `胸部X光片` `基础模型` `可解释性` `强化学习` `视觉问答` `报告生成`

## 📋 核心要点

1. 现有医学基础模型缺乏透明推理过程和局部可解释性，限制了其临床应用。
2. DeepMedix-R1通过顺序训练流程，结合微调、合成推理和在线强化学习，实现可解释的胸部X光片分析。
3. 实验表明，DeepMedix-R1在报告生成和视觉问答任务中显著优于现有模型，并具有更高的临床合理性。

## 📝 摘要（中文）

随着人工智能技术的快速发展，医学基础模型（FMs）展现出巨大的潜力。然而，当前的医学FMs通常以黑盒方式生成答案，缺乏透明的推理过程和局部可解释性，这阻碍了它们在临床中的实际部署。为此，我们推出了DeepMedix-R1，一个用于胸部X光片（CXR）解释的整体医学FM。它利用一个顺序训练流程：首先在精选的CXR指令数据上进行微调，以具备基本的CXR解释能力，然后暴露于高质量的合成推理样本以实现冷启动推理，最后通过在线强化学习进行优化，以提高基础推理质量和生成性能。因此，该模型为每个查询生成答案和与图像局部区域相关的推理步骤。定量评估表明，在报告生成（例如，比LLaVA-Rad和MedGemma分别提高14.54%和31.32%）和视觉问答（例如，比MedGemma和CheXagent分别提高57.75%和23.06%）任务中，性能得到了显著提升。为了方便稳健的评估，我们提出了Report Arena，一个使用高级语言模型评估答案质量的基准框架，进一步突出了DeepMedix-R1的优越性。专家对生成的推理步骤的审查表明，与已建立的Qwen2.5-VL-7B模型相比，DeepMedix-R1具有更高的可解释性和临床合理性（总体偏好为0.7416 vs. 0.2584）。总的来说，我们的工作推动了医学FM朝着整体、透明和临床可操作的CXR解释建模方向发展。

## 🔬 方法详解

**问题定义**：论文旨在解决医学基础模型在胸部X光片判读中缺乏透明推理过程和局部可解释性的问题。现有方法通常是黑盒模型，无法提供支持诊断的依据，阻碍了其在临床实践中的应用。医生需要了解模型做出判断的原因，以便验证和信任模型的输出。

**核心思路**：论文的核心思路是通过一个多阶段的训练流程，使模型不仅能给出诊断结果，还能提供与图像局部区域相关的推理步骤。这种设计旨在提高模型的可解释性，并使医生能够验证模型的推理过程。通过在线强化学习，模型可以不断学习和优化其推理策略，从而提高诊断的准确性和可靠性。

**技术框架**：DeepMedix-R1的整体框架包含三个主要阶段：1) 在精选的胸部X光片指令数据上进行微调，使模型具备基本的胸部X光片判读能力；2) 使用高质量的合成推理样本进行训练，使模型能够进行冷启动推理；3) 通过在线强化学习，根据奖励信号优化模型的推理过程和生成性能。该框架旨在逐步提升模型的能力，使其能够生成准确且可解释的诊断报告。

**关键创新**：该论文的关键创新在于将在线强化学习应用于医学基础模型，以提高其推理能力和可解释性。与传统的监督学习方法不同，在线强化学习允许模型在与环境交互的过程中不断学习和优化其策略。此外，该论文还提出了一个名为Report Arena的基准框架，用于评估模型生成的报告的质量。

**关键设计**：在在线强化学习阶段，论文设计了一个奖励函数，用于评估模型生成的推理步骤的质量。该奖励函数考虑了推理步骤与图像局部区域的相关性、推理步骤的逻辑一致性以及最终诊断结果的准确性。此外，论文还使用了Transformer架构作为模型的基础，并针对胸部X光片判读任务进行了优化。

## 📊 实验亮点

DeepMedix-R1在报告生成任务中，相较于LLaVA-Rad和MedGemma，分别取得了14.54%和31.32%的性能提升。在视觉问答任务中，相较于MedGemma和CheXagent，分别取得了57.75%和23.06%的性能提升。专家评估表明，DeepMedix-R1生成的推理步骤具有更高的可解释性和临床合理性（0.7416 vs. 0.2584）。

## 🎯 应用场景

DeepMedix-R1可应用于辅助医生进行胸部X光片诊断，提高诊断效率和准确性。其可解释的推理过程有助于医生验证诊断结果，增强对模型的信任。未来，该模型有望扩展到其他医学影像领域，为临床决策提供更全面的支持。

## 📄 摘要（原文）

> Medical foundation models (FMs) have shown tremendous promise amid the rapid advancements in artificial intelligence (AI) technologies. However, current medical FMs typically generate answers in a black-box manner, lacking transparent reasoning processes and locally grounded interpretability, which hinders their practical clinical deployments. To this end, we introduce DeepMedix-R1, a holistic medical FM for chest X-ray (CXR) interpretation. It leverages a sequential training pipeline: initially fine-tuned on curated CXR instruction data to equip with fundamental CXR interpretation capabilities, then exposed to high-quality synthetic reasoning samples to enable cold-start reasoning, and finally refined via online reinforcement learning to enhance both grounded reasoning quality and generation performance. Thus, the model produces both an answer and reasoning steps tied to the image's local regions for each query. Quantitative evaluation demonstrates substantial improvements in report generation (e.g., 14.54% and 31.32% over LLaVA-Rad and MedGemma) and visual question answering (e.g., 57.75% and 23.06% over MedGemma and CheXagent) tasks. To facilitate robust assessment, we propose Report Arena, a benchmarking framework using advanced language models to evaluate answer quality, further highlighting the superiority of DeepMedix-R1. Expert review of generated reasoning steps reveals greater interpretability and clinical plausibility compared to the established Qwen2.5-VL-7B model (0.7416 vs. 0.2584 overall preference). Collectively, our work advances medical FM development toward holistic, transparent, and clinically actionable modeling for CXR interpretation.

