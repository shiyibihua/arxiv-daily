---
layout: default
title: Character-Level Perturbations Disrupt LLM Watermarks
---

# Character-Level Perturbations Disrupt LLM Watermarks

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.09112" class="toolbar-btn" target="_blank">📄 arXiv: 2509.09112v2</a>
  <a href="https://arxiv.org/pdf/2509.09112.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.09112v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.09112v2', 'Character-Level Perturbations Disrupt LLM Watermarks')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zhaoxi Zhang, Xiaomei Zhang, Yanjun Zhang, He Zhang, Shirui Pan, Bo Liu, Asif Qumer Gill, Leo Yu Zhang

**分类**: cs.CR, cs.AI

**发布日期**: 2025-09-11 (更新: 2025-09-14)

**备注**: accepted by Network and Distributed System Security (NDSS) Symposium 2026

**期刊**: Network and Distributed System Security (NDSS) Symposium 2026

**DOI**: [10.14722/ndss.2026.230138](https://doi.org/10.14722/ndss.2026.230138)

---

## 💡 一句话要点

**提出基于字符级扰动的LLM水印移除攻击，揭示现有水印方案的脆弱性**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `LLM水印` `水印移除攻击` `字符级扰动` `遗传算法` `对抗性攻击` `鲁棒性评估` `自然语言处理`

## 📋 核心要点

1. 现有LLM水印移除攻击方法次优，难以充分评估水印的脆弱性，需要更有效的攻击手段。
2. 提出基于字符级扰动的水印移除方法，通过影响token化过程，实现对多个token的同时攻击。
3. 实验表明，字符级扰动在限制条件下能有效移除水印，并提出自适应攻击以对抗潜在防御。

## 📝 摘要（中文）

大型语言模型（LLM）水印技术旨在将可检测的信号嵌入到生成的文本中，用于版权保护、滥用预防和内容检测。以往的研究评估水印鲁棒性时，通常使用次优的水印移除攻击方法，导致人们误以为有效移除水印需要较大的扰动或强大的攻击者。为了弥补这一差距，我们首先形式化了LLM水印的系统模型，并刻画了两种在访问水印检测器方面受限的现实威胁模型。然后，我们分析了不同类型的扰动在攻击范围上的差异，即它们可以通过单次编辑影响的token数量。我们观察到，字符级扰动（例如，拼写错误、交换、删除、同形字）可以通过扰乱token化过程同时影响多个token。我们证明，在最严格的威胁模型下，字符级扰动对于水印移除更为有效。我们进一步提出了基于遗传算法（GA）的引导移除攻击，该算法使用参考检测器进行优化。在对水印检测器的黑盒查询有限的实际威胁模型下，我们的方法表现出强大的移除性能。实验证实了字符级扰动的优越性以及GA在实际约束下移除水印的有效性。此外，我们认为在考虑潜在防御措施时存在对抗性困境：任何固定的防御措施都可以通过适当的扰动策略来绕过。受此原则的启发，我们提出了一种自适应的复合字符级攻击。实验结果表明，该方法可以有效地击败防御措施。我们的研究结果突出了现有LLM水印方案的重大漏洞，并强调了开发新的鲁棒机制的紧迫性。

## 🔬 方法详解

**问题定义**：现有LLM水印方案的鲁棒性评估不足，常用的水印移除攻击方法效果有限，无法充分揭示水印的脆弱性。现有方法通常需要较大的扰动或强大的攻击者，与实际应用场景不符。因此，需要研究更有效的、在资源受限条件下的水印移除攻击方法。

**核心思路**：利用字符级扰动对LLM的token化过程产生影响，从而实现对多个token的同时攻击。相比于token级别的扰动，字符级扰动可以在更小的改动幅度下，影响更多的token，从而更有效地移除水印。此外，利用遗传算法（GA）来指导扰动的选择，以优化水印移除的效果。

**技术框架**：该方法主要包含以下几个阶段：1) **系统模型形式化**：定义LLM水印的系统模型，包括水印嵌入、文本生成和水印检测等过程。2) **威胁模型刻画**：定义两种现实的威胁模型，限制攻击者对水印检测器的访问权限。3) **扰动分析**：分析不同类型扰动（字符级、token级）的攻击范围和效果。4) **攻击方法设计**：提出基于字符级扰动的攻击方法，包括基本的字符级扰动和基于遗传算法的引导攻击。5) **防御对抗**：提出自适应的复合字符级攻击，以对抗潜在的防御措施。

**关键创新**：该论文的关键创新在于：1) 提出了利用字符级扰动进行水印移除攻击的思想，相比于token级别的扰动，字符级扰动更有效。2) 提出了基于遗传算法的引导攻击方法，可以有效地优化扰动的选择，提高水印移除的效果。3) 提出了自适应的复合字符级攻击，可以对抗潜在的防御措施。

**关键设计**：1) **字符级扰动类型**：包括拼写错误、字符交换、字符删除、同形字替换等。2) **遗传算法**：使用遗传算法来搜索最优的扰动组合，目标是最小化水印检测器的置信度。遗传算法的关键参数包括种群大小、交叉概率、变异概率等。3) **自适应攻击**：根据防御措施的反馈，动态调整扰动策略，以提高攻击的成功率。

## 📊 实验亮点

实验结果表明，在限制条件下，字符级扰动比token级扰动更有效地移除水印。基于遗传算法的引导攻击方法在实际威胁模型下表现出强大的移除性能。自适应复合字符级攻击可以有效地击败潜在的防御措施。这些结果突出了现有LLM水印方案的脆弱性。

## 🎯 应用场景

该研究成果可应用于评估和改进现有LLM水印方案的鲁棒性，帮助开发者设计更安全可靠的水印技术。同时，该研究也提醒人们关注LLM生成内容的潜在风险，例如恶意内容伪造和版权侵犯，促进相关安全防护技术的发展。

## 📄 摘要（原文）

> Large Language Model (LLM) watermarking embeds detectable signals into generated text for copyright protection, misuse prevention, and content detection. While prior studies evaluate robustness using watermark removal attacks, these methods are often suboptimal, creating the misconception that effective removal requires large perturbations or powerful adversaries.
>   To bridge the gap, we first formalize the system model for LLM watermark, and characterize two realistic threat models constrained on limited access to the watermark detector. We then analyze how different types of perturbation vary in their attack range, i.e., the number of tokens they can affect with a single edit. We observe that character-level perturbations (e.g., typos, swaps, deletions, homoglyphs) can influence multiple tokens simultaneously by disrupting the tokenization process. We demonstrate that character-level perturbations are significantly more effective for watermark removal under the most restrictive threat model. We further propose guided removal attacks based on the Genetic Algorithm (GA) that uses a reference detector for optimization. Under a practical threat model with limited black-box queries to the watermark detector, our method demonstrates strong removal performance. Experiments confirm the superiority of character-level perturbations and the effectiveness of the GA in removing watermarks under realistic constraints. Additionally, we argue there is an adversarial dilemma when considering potential defenses: any fixed defense can be bypassed by a suitable perturbation strategy. Motivated by this principle, we propose an adaptive compound character-level attack. Experimental results show that this approach can effectively defeat the defenses. Our findings highlight significant vulnerabilities in existing LLM watermark schemes and underline the urgency for the development of new robust mechanisms.

