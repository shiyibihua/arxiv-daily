---
layout: default
title: A Multimodal LLM Approach for Visual Question Answering on Multiparametric 3D Brain MRI
---

# A Multimodal LLM Approach for Visual Question Answering on Multiparametric 3D Brain MRI

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.25889" class="toolbar-btn" target="_blank">📄 arXiv: 2509.25889v2</a>
  <a href="https://arxiv.org/pdf/2509.25889.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.25889v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.25889v2', 'A Multimodal LLM Approach for Visual Question Answering on Multiparametric 3D Brain MRI')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Arvind Murari Vepa, Yannan Yu, Jingru Gan, Anthony Cuturrufo, Weikai Li, Wei Wang, Fabien Scalzo, Yizhou Sun

**分类**: cs.CV, cs.CL

**发布日期**: 2025-09-30 (更新: 2025-10-01)

**备注**: 23 pages, 3 figures

---

## 💡 一句话要点

**提出mpLLM，用于多参数3D脑部MRI的视觉问答，提升医学诊断效率。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多模态学习` `视觉问答` `医学影像` `3D MRI` `混合专家模型` `深度学习` `医学诊断`

## 📋 核心要点

1. 现有医学VQA方法缺乏对多模态3D MRI数据的有效处理，限制了诊断的准确性和效率。
2. mpLLM通过分层混合专家架构，融合模态级和token级信息，实现对多模态3D MRI数据的有效理解。
3. 实验表明，mpLLM在多个mpMRI数据集上优于现有医学VLM基线，平均提升5.3%。

## 📝 摘要（中文）

本文提出了一种名为mpLLM的提示条件分层混合专家(MoE)架构，用于多参数3D脑部MRI(mpMRI)的视觉问答。mpLLM通过模态级和token级投影专家进行路由，融合多个相互关联的3D模态，从而实现高效训练，无需图像-报告预训练。为了解决有限的图像-文本配对监督问题，mpLLM集成了一种合成视觉问答(VQA)协议，该协议从分割注释生成医学相关的VQA，并与医学专家合作进行临床验证。在多个mpMRI数据集上，mpLLM的性能平均超过了强大的医学VLM基线5.3%。本研究的主要贡献包括：(1)首个经过临床验证的3D脑部mpMRI的VQA数据集，(2)一种处理多个相互关联的3D模态的新型多模态LLM，以及(3)强大的实验结果，证明了该方法的医学实用性。消融实验突出了模态级和token级专家以及提示条件路由的重要性。

## 🔬 方法详解

**问题定义**：论文旨在解决多参数3D脑部MRI（mpMRI）的视觉问答（VQA）问题。现有的医学VQA方法通常难以有效处理多模态3D MRI数据，并且缺乏足够的图像-文本配对监督，导致模型性能受限。此外，现有方法可能无法充分利用不同模态之间的关联性，从而影响诊断的准确性。

**核心思路**：论文的核心思路是利用一个提示条件分层混合专家（MoE）架构，即mpLLM，来融合多个相互关联的3D模态。通过模态级和token级投影专家进行路由，mpLLM能够更有效地学习不同模态之间的关系，并利用合成VQA数据来弥补有限的图像-文本配对监督。

**技术框架**：mpLLM的整体架构是一个分层MoE模型，包含以下主要模块：1) 多模态3D MRI输入；2) 模态级专家，用于处理不同模态的特征；3) token级专家，用于融合不同模态的token信息；4) 提示条件路由机制，根据问题提示动态选择专家；5) VQA预测模块，生成答案。

**关键创新**：论文的关键创新在于：1) 提出了一个针对多模态3D MRI数据的分层MoE架构，能够有效融合不同模态的信息；2) 引入了合成VQA协议，利用分割注释生成医学相关的VQA数据，缓解了数据稀缺问题；3) 提出了提示条件路由机制，能够根据问题动态选择专家，提高模型的适应性。

**关键设计**：mpLLM的关键设计包括：1) 使用3D卷积神经网络提取MRI图像特征；2) 设计了模态级和token级专家网络，用于处理不同模态和token的信息；3) 采用了交叉熵损失函数进行VQA任务的训练；4) 使用了临床专家进行验证，确保模型的医学实用性。

## 📊 实验亮点

mpLLM在多个mpMRI数据集上取得了显著的性能提升，平均超过了强大的医学VLM基线5.3%。消融实验表明，模态级和token级专家以及提示条件路由对模型性能至关重要。此外，该研究还构建了首个经过临床验证的3D脑部mpMRI的VQA数据集，为后续研究提供了宝贵资源。

## 🎯 应用场景

该研究成果可应用于医学影像辅助诊断，帮助医生更准确、高效地分析脑部MRI图像，从而提高诊断效率和准确性。此外，该方法还可以扩展到其他医学影像模态和疾病的诊断，具有广泛的应用前景。未来，结合患者的临床信息，可以实现更个性化的诊断和治疗方案。

## 📄 摘要（原文）

> We introduce mpLLM, a prompt-conditioned hierarchical mixture-of-experts (MoE) architecture for visual question answering over multi-parametric 3D brain MRI (mpMRI). mpLLM routes across modality-level and token-level projection experts to fuse multiple interrelated 3D modalities, enabling efficient training without image-report pretraining. To address limited image-text paired supervision, mpLLM integrates a synthetic visual question answering (VQA) protocol that generates medically relevant VQA from segmentation annotations, and we collaborate with medical experts for clinical validation. mpLLM outperforms strong medical VLM baselines by 5.3% on average across multiple mpMRI datasets. Our study features three main contributions: (1) the first clinically validated VQA dataset for 3D brain mpMRI, (2) a novel multimodal LLM that handles multiple interrelated 3D modalities, and (3) strong empirical results that demonstrate the medical utility of our methodology. Ablations highlight the importance of modality-level and token-level experts and prompt-conditioned routing.

