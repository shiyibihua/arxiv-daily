---
layout: default
title: A Systematic Approach to Predict the Impact of Cybersecurity Vulnerabilities Using LLMs
---

# A Systematic Approach to Predict the Impact of Cybersecurity Vulnerabilities Using LLMs

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.18439" class="toolbar-btn" target="_blank">📄 arXiv: 2508.18439v2</a>
  <a href="https://arxiv.org/pdf/2508.18439.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.18439v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.18439v2', 'A Systematic Approach to Predict the Impact of Cybersecurity Vulnerabilities Using LLMs')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Anders Mølmen Høst, Pierre Lison, Leon Moonen

**分类**: cs.CR, cs.AI, cs.CL, cs.SE

**发布日期**: 2025-08-25 (更新: 2025-10-19)

**备注**: Accepted for publication in the 24th IEEE International Conference on Trust, Security and Privacy in Computing and Communications (TrustCom 2025)

---

## 💡 一句话要点

**提出TRIAGE以自动预测网络安全漏洞影响**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `网络安全` `漏洞影响` `CVE` `ATT&CK技术` `大型语言模型` `自动化映射` `上下文学习`

## 📋 核心要点

1. 现有漏洞数据库缺乏对CVE在现实世界中影响的详细信息，手动链接工作繁琐且耗时。
2. 论文提出TRIAGE，通过大型语言模型自动将CVE映射到ATT&CK技术，结合规则推理与数据驱动推断。
3. 实验结果表明，基于上下文学习的模块优于单一映射方法，混合方法提高了召回率，GPT-4o-mini表现优于Llama3.3-70B。

## 📝 摘要（中文）

漏洞数据库如国家漏洞数据库（NVD）提供了常见漏洞和暴露（CVE）的详细描述，但通常缺乏其在现实世界中的影响信息，例如对手可能利用的战术、技术和程序（TTP）。手动将CVE与相应的TTP链接是一项具有挑战性且耗时的任务，尤其是每年发布的新漏洞数量庞大。因此，自动化支持显得尤为重要。本文提出了TRIAGE，一种基于大型语言模型（LLMs）的双重自动化方法，将CVE映射到ATT&CK知识库中的相关技术。我们的评估显示，基于上下文学习的模块在映射效果上优于单一方法，且混合方法提高了利用技术的召回率。总体结果表明，LLMs可以有效预测网络安全漏洞的影响，TRIAGE使CVE到ATT&CK的映射过程更加高效。

## 🔬 方法详解

**问题定义**：本文旨在解决现有漏洞数据库缺乏对CVE实际影响的详细描述的问题，手动链接CVE与TTP的过程既繁琐又耗时，尤其是在新漏洞数量不断增加的背景下。

**核心思路**：TRIAGE的核心思路是利用大型语言模型（LLMs）自动化映射过程，通过结合基于规则的推理与数据驱动的推断，提升映射的效率与准确性。

**技术框架**：TRIAGE的整体架构包括两个主要模块：首先，使用LLM根据MITRE的CVE映射方法生成初步技术列表；其次，利用另一个LLM模块进行上下文学习，进一步映射CVE到相关技术。

**关键创新**：该研究的主要创新在于将上下文学习与规则推理相结合，显著提高了对利用技术的召回率，且在性能上超越了传统的单一映射方法。

**关键设计**：在模型设计上，采用了基于LLM的两阶段映射流程，第一阶段生成初步列表，第二阶段进行上下文学习，具体参数设置和损失函数未详细披露，需进一步研究。

## 📊 实验亮点

实验结果显示，基于上下文学习的模块在映射效果上优于单一方法，混合方法提高了对利用技术的召回率。具体而言，GPT-4o-mini在此任务中的表现优于Llama3.3-70B，表明LLMs在自动化漏洞影响预测中的有效性。

## 🎯 应用场景

该研究的潜在应用领域包括网络安全评估、漏洞管理和自动化安全工具的开发。通过提高CVE与ATT&CK技术的映射效率，TRIAGE可以帮助安全团队更快速地识别和应对潜在威胁，提升整体安全防护能力。

## 📄 摘要（原文）

> Vulnerability databases, such as the National Vulnerability Database (NVD), offer detailed descriptions of Common Vulnerabilities and Exposures (CVEs), but often lack information on their real-world impact, such as the tactics, techniques, and procedures (TTPs) that adversaries may use to exploit the vulnerability. However, manually linking CVEs to their corresponding TTPs is a challenging and time-consuming task, and the high volume of new vulnerabilities published annually makes automated support desirable.
>   This paper introduces TRIAGE, a two-pronged automated approach that uses Large Language Models (LLMs) to map CVEs to relevant techniques from the ATT&CK knowledge base. We first prompt an LLM with instructions based on MITRE's CVE Mapping Methodology to predict an initial list of techniques. This list is then combined with the results from a second LLM-based module that uses in-context learning to map a CVE to relevant techniques. This hybrid approach strategically combines rule-based reasoning with data-driven inference. Our evaluation reveals that in-context learning outperforms the individual mapping methods, and the hybrid approach improves recall of exploitation techniques. We also find that GPT-4o-mini performs better than Llama3.3-70B on this task. Overall, our results show that LLMs can be used to automatically predict the impact of cybersecurity vulnerabilities and TRIAGE makes the process of mapping CVEs to ATT&CK more efficient. A replication package is available for download from https://doi.org/10.5281/zenodo.17341503.
>   Keywords: vulnerability impact, CVE, ATT&CK techniques, large language models, automated mapping.

