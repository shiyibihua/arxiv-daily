---
layout: default
title: What Do They Fix? LLM-Aided Categorization of Security Patches for Critical Memory Bugs
---

# What Do They Fix? LLM-Aided Categorization of Security Patches for Critical Memory Bugs

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.22796" class="toolbar-btn" target="_blank">📄 arXiv: 2509.22796v1</a>
  <a href="https://arxiv.org/pdf/2509.22796.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.22796v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.22796v1', 'What Do They Fix? LLM-Aided Categorization of Security Patches for Critical Memory Bugs')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Xingyu Li, Juefei Pu, Yifan Wu, Xiaochen Zou, Shitong Zhu, Xiaochen Zou, Shitong Zhu, Qiushi Wu, Zheng Zhang, Joshua Hsu, Yue Dong, Zhiyun Qian, Kangjie Lu, Trent Jaeger, Michael De Lucia, Srikanth V. Krishnamurthy

**分类**: cs.CR, cs.LG

**发布日期**: 2025-09-26

---

## 💡 一句话要点

**DUALLM：利用LLM辅助识别Linux内核中关键内存漏洞的安全补丁**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `Linux内核` `安全补丁` `漏洞分类` `大型语言模型` `越界访问` `释放后使用` `软件安全` `自然语言处理`

## 📋 核心要点

1. 现有细粒度补丁分类方法在覆盖范围和准确性上存在局限，难以有效识别Linux内核中的安全关键补丁，特别是OOB和UAF漏洞。
2. DUALLM利用大型语言模型和微调的小型语言模型，结合提交信息、代码差异和上下文，构建双方法管道进行补丁分类。
3. DUALLM在识别OOB和UAF漏洞补丁方面达到了87.4%的准确率和0.875的F1分数，显著优于现有方法，并成功发现了多个未公开的漏洞。

## 📝 摘要（中文）

开源软件项目是现代软件生态系统的基础，其中Linux内核因其普遍性和复杂性而成为一个关键典范。尽管安全补丁不断集成到Linux主线内核中，但下游维护人员通常会延迟采用，从而造成漏洞窗口。造成这种滞后的一个关键原因是难以识别安全关键补丁，特别是那些解决可利用漏洞的补丁，例如越界（OOB）访问和释放后使用（UAF）错误。由于有意保持沉默的错误修复、不完整或缺失的CVE分配、CVE发布延迟以及最近对Linux内核的CVE分配标准的更改，这一挑战更加严峻。虽然存在细粒度的补丁分类方法，但它们在覆盖范围和准确性方面都存在局限性。在这项工作中，我们发现了以前未探索的机会，可以显着改进细粒度的补丁分类。具体来说，通过利用提交标题/消息和差异以及适当的代码上下文中的线索，我们开发了DUALLM，这是一种双方法管道，集成了两种基于大型语言模型（LLM）和微调的小型语言模型的方法。DUALLM实现了87.4%的准确率和0.875的F1分数，显着优于之前的解决方案。值得注意的是，DUALLM成功地将5,140个最近的Linux内核补丁中的111个识别为解决了OOB或UAF漏洞，其中90个真阳性已通过手动验证确认（许多在补丁描述中没有明确的指示）。此外，我们为两个已识别的错误（一个UAF和一个OOB）构建了概念验证，包括一个开发用于进行先前未知的控制流劫持，作为分类正确性的进一步证据。

## 🔬 方法详解

**问题定义**：论文旨在解决Linux内核安全补丁分类问题，特别是识别修复了越界（OOB）访问和释放后使用（UAF）等关键内存漏洞的补丁。现有方法存在覆盖率和准确率不足的问题，难以有效识别这些安全关键补丁，导致漏洞修复延迟。

**核心思路**：论文的核心思路是结合大型语言模型（LLM）和小语言模型（SLM）的优势，利用补丁的提交信息（标题、消息）和代码差异（diff）作为线索，并结合代码上下文，实现更准确的补丁分类。通过双重验证机制，提高识别准确率。

**技术框架**：DUALLM采用双方法管道，包含以下主要阶段：
1. **数据预处理**：提取补丁的提交信息、代码差异和相关代码上下文。
2. **LLM分类器**：使用大型语言模型（如GPT-3）对补丁进行初步分类，利用其强大的语义理解能力。
3. **SLM分类器**：使用微调的小型语言模型（如BERT）对补丁进行二次分类，利用其在特定任务上的高效性。
4. **结果融合**：结合LLM和SLM的分类结果，通过一定的策略（如投票或加权平均）得到最终分类结果。
5. **人工验证**：对识别出的可疑补丁进行人工验证，确认其是否真正修复了OOB或UAF漏洞。

**关键创新**：DUALLM的关键创新在于：
1. **双方法融合**：结合LLM的语义理解能力和SLM的特定任务效率，提高分类准确率。
2. **多源信息利用**：同时利用提交信息、代码差异和代码上下文，提供更全面的分类依据。
3. **人工验证闭环**：通过人工验证确认分类结果，并用于改进模型性能。

**关键设计**：
1. **LLM选择**：选择具有强大语义理解能力的大型语言模型，如GPT-3。
2. **SLM选择与微调**：选择适合文本分类的小型语言模型，如BERT，并使用标注数据进行微调。
3. **特征工程**：设计有效的特征提取方法，将提交信息、代码差异和代码上下文转换为模型可用的输入。
4. **融合策略**：设计合理的融合策略，平衡LLM和SLM的分类结果。

## 📊 实验亮点

DUALLM在5,140个Linux内核补丁中成功识别出111个OOB或UAF漏洞补丁，准确率达到87.4%，F1分数为0.875，显著优于现有方法。通过人工验证，确认了90个真阳性结果，并为其中两个漏洞构建了概念验证，证明了分类的有效性。

## 🎯 应用场景

该研究成果可应用于自动化安全补丁识别和优先级排序，帮助Linux内核维护者和下游发行版更快地发现和应用关键安全补丁，缩短漏洞窗口期。此外，该方法也可推广到其他开源软件项目，提升整体软件安全水平，降低安全风险。

## 📄 摘要（原文）

> Open-source software projects are foundational to modern software ecosystems, with the Linux kernel standing out as a critical exemplar due to its ubiquity and complexity. Although security patches are continuously integrated into the Linux mainline kernel, downstream maintainers often delay their adoption, creating windows of vulnerability. A key reason for this lag is the difficulty in identifying security-critical patches, particularly those addressing exploitable vulnerabilities such as out-of-bounds (OOB) accesses and use-after-free (UAF) bugs. This challenge is exacerbated by intentionally silent bug fixes, incomplete or missing CVE assignments, delays in CVE issuance, and recent changes to the CVE assignment criteria for the Linux kernel. While fine-grained patch classification approaches exist, they exhibit limitations in both coverage and accuracy. In this work, we identify previously unexplored opportunities to significantly improve fine-grained patch classification. Specifically, by leveraging cues from commit titles/messages and diffs alongside appropriate code context, we develop DUALLM, a dual-method pipeline that integrates two approaches based on a Large Language Model (LLM) and a fine-tuned small language model. DUALLM achieves 87.4% accuracy and an F1-score of 0.875, significantly outperforming prior solutions. Notably, DUALLM successfully identified 111 of 5,140 recent Linux kernel patches as addressing OOB or UAF vulnerabilities, with 90 true positives confirmed by manual verification (many do not have clear indications in patch descriptions). Moreover, we constructed proof-of-concepts for two identified bugs (one UAF and one OOB), including one developed to conduct a previously unknown control-flow hijack as further evidence of the correctness of the classification.

