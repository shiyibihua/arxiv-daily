---
layout: default
title: "ProGuard: Towards Proactive Multimodal Safeguard"
---

# ProGuard: Towards Proactive Multimodal Safeguard

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.23573" class="toolbar-btn" target="_blank">📄 arXiv: 2512.23573v1</a>
  <a href="https://arxiv.org/pdf/2512.23573.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.23573v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.23573v1', 'ProGuard: Towards Proactive Multimodal Safeguard')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Shaohan Yu, Lijun Li, Chenyang Si, Lu Sheng, Jing Shao

**分类**: cs.CV

**发布日期**: 2025-12-29

---

## 💡 一句话要点

**提出ProGuard，一种主动式多模态安全防护方法，用于识别和描述生成模型中的OOD安全风险。**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多模态安全` `主动防御` `强化学习` `分布外检测` `视觉-语言模型`

## 📋 核心要点

1. 现有生成模型的安全性防御方法存在局限性，难以应对不断涌现的多模态安全风险，尤其是在分布外（OOD）场景下。
2. ProGuard通过构建模态平衡数据集和强化学习训练，实现了对OOD安全风险的主动识别和描述，无需模型调整。
3. 实验结果表明，ProGuard在OOD风险检测和描述方面显著优于现有开源模型，提升幅度分别达到52.6%和64.8%。

## 📝 摘要（中文）

生成模型的快速发展导致多模态安全风险不断涌现，暴露了现有防御方法的局限性。为了应对这些挑战，我们提出了ProGuard，一种视觉-语言主动防护方法，它能够识别和描述分布外(OOD)安全风险，而无需像传统被动方法那样进行模型调整。我们首先构建了一个包含87K样本的模态平衡数据集，每个样本都标注了二元安全标签和分层多模态安全分类体系下的风险类别，有效地缓解了模态偏差，并确保了文本、图像和文本-图像输入之间的一致审核。基于此数据集，我们完全通过强化学习(RL)训练视觉-语言基础模型，以实现高效简洁的推理。为了在受控环境中近似主动安全场景，我们进一步引入了OOD安全类别推断任务，并通过基于同义词库的相似性奖励来增强RL目标，鼓励模型为未见过的非安全类别生成简洁的描述。实验结果表明，ProGuard在二元安全分类方面达到了与闭源大型模型相当的性能，并在非安全内容分类方面显著优于现有的开源防护模型。最值得注意的是，ProGuard提供了强大的主动审核能力，将OOD风险检测提高了52.6%，OOD风险描述提高了64.8%。

## 🔬 方法详解

**问题定义**：论文旨在解决生成模型中日益增长的多模态安全风险，特别是分布外（OOD）的安全风险识别问题。现有的防御方法通常是被动的，需要针对特定风险进行模型调整，无法有效应对未知的安全威胁。此外，现有方法往往存在模态偏差，难以在文本、图像和文本-图像等不同模态之间保持一致的审核标准。

**核心思路**：ProGuard的核心思路是构建一个主动式的安全防护系统，使其能够在没有事先见过的情况下，识别和描述新的、分布外的安全风险。通过强化学习训练模型，使其能够高效简洁地进行推理，并利用同义词库的相似性奖励，鼓励模型生成对未知风险类别的准确描述。

**技术框架**：ProGuard的技术框架主要包括以下几个部分：1) 构建模态平衡数据集，包含文本、图像和文本-图像三种模态，并标注二元安全标签和分层风险类别。2) 使用强化学习训练视觉-语言基础模型，使其能够进行安全分类和风险描述。3) 引入OOD安全类别推断任务，模拟主动安全场景。4) 使用基于同义词库的相似性奖励来增强强化学习目标，鼓励模型生成对未知风险类别的简洁描述。

**关键创新**：ProGuard的关键创新在于其主动式的安全防护能力。与传统的被动防御方法不同，ProGuard能够在没有事先见过的情况下，识别和描述新的、分布外的安全风险。这得益于其基于强化学习的训练方法和基于同义词库的相似性奖励机制。

**关键设计**：ProGuard的关键设计包括：1) 模态平衡数据集的构建，确保了模型在不同模态之间的一致性。2) 强化学习目标的设计，包括安全分类奖励、风险描述奖励和相似性奖励。3) 基于同义词库的相似性奖励的计算方法，用于衡量模型生成的描述与真实风险类别之间的相似度。具体参数设置和网络结构等细节在论文中未详细说明，属于未知信息。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.23573v1/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.23573v1/x2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.23573v1/x3.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

ProGuard在二元安全分类方面达到了与闭源大型模型相当的性能，并在非安全内容分类方面显著优于现有的开源防护模型。最重要的是，ProGuard在OOD风险检测方面提高了52.6%，在OOD风险描述方面提高了64.8%，展示了强大的主动审核能力。

## 🎯 应用场景

ProGuard可应用于各种生成模型，例如文本生成、图像生成和多模态生成模型，以提高其安全性。该研究的实际价值在于能够有效识别和防御未知的安全风险，降低生成模型被恶意利用的风险。未来，ProGuard可以进一步扩展到更广泛的安全领域，例如网络安全和信息安全。

## 📄 摘要（原文）

> The rapid evolution of generative models has led to a continuous emergence of multimodal safety risks, exposing the limitations of existing defense methods. To address these challenges, we propose ProGuard, a vision-language proactive guard that identifies and describes out-of-distribution (OOD) safety risks without the need for model adjustments required by traditional reactive approaches. We first construct a modality-balanced dataset of 87K samples, each annotated with both binary safety labels and risk categories under a hierarchical multimodal safety taxonomy, effectively mitigating modality bias and ensuring consistent moderation across text, image, and text-image inputs. Based on this dataset, we train our vision-language base model purely through reinforcement learning (RL) to achieve efficient and concise reasoning. To approximate proactive safety scenarios in a controlled setting, we further introduce an OOD safety category inference task and augment the RL objective with a synonym-bank-based similarity reward that encourages the model to generate concise descriptions for unseen unsafe categories. Experimental results show that ProGuard achieves performance comparable to closed-source large models on binary safety classification, substantially outperforms existing open-source guard models on unsafe content categorization. Most notably, ProGuard delivers a strong proactive moderation ability, improving OOD risk detection by 52.6% and OOD risk description by 64.8%.

