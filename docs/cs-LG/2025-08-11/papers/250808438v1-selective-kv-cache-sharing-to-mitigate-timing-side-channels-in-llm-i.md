---
layout: default
title: Selective KV-Cache Sharing to Mitigate Timing Side-Channels in LLM Inference
---

# Selective KV-Cache Sharing to Mitigate Timing Side-Channels in LLM Inference

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.08438" class="toolbar-btn" target="_blank">📄 arXiv: 2508.08438v1</a>
  <a href="https://arxiv.org/pdf/2508.08438.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.08438v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.08438v1', 'Selective KV-Cache Sharing to Mitigate Timing Side-Channels in LLM Inference')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Kexin Chu, Zecheng Lin, Dawei Xiang, Zixu Shen, Jianchang Su, Cheng Chu, Yiwei Yang, Wenhui Zhang, Wenfei Wu, Wei Zhang

**分类**: cs.CR, cs.LG, cs.OS

**发布日期**: 2025-08-11

**备注**: 17 pages,17 figures

---

## 💡 一句话要点

**提出SafeKV以解决LLM推理中的时序侧信道攻击问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `KV缓存共享` `时序侧信道攻击` `隐私保护` `大型语言模型` `性能优化` `信息泄露防护` `高吞吐量部署`

## 📋 核心要点

1. 现有的全球KV缓存共享方法在加速LLM推理的同时，暴露了时序侧信道攻击的风险，导致敏感信息泄露。
2. 本文提出SafeKV框架，通过选择性共享非敏感缓存条目，保护敏感信息，同时提升性能。
3. 实验结果表明，SafeKV能有效减轻94%-97%的攻击，TTFT提升40.58%，吞吐量提高至2.66倍，显著优于现有方法。

## 📝 摘要（中文）

全球KV缓存共享已成为加速大型语言模型（LLM）推理的关键优化。然而，这种方法暴露了新的时序侧信道攻击风险，使得攻击者能够通过共享缓存条目推断敏感用户输入。现有的防御措施如用户隔离虽然能消除泄漏，但在首次令牌时间（TTFT）上性能下降高达38.9%，不适合高吞吐量部署。为此，本文提出了SafeKV（安全灵活的KV缓存共享），一个隐私意识的KV缓存管理框架，选择性地共享非敏感条目，同时将敏感内容限制在私有缓存中。SafeKV通过三大组件实现其目标：混合多层检测管道、统一的基数树索引和基于熵的访问监控。评估结果显示，SafeKV能减轻94%-97%的时序侧信道攻击，相比用户隔离方法，TTFT提升高达40.58%，吞吐量提高至2.66倍。

## 🔬 方法详解

**问题定义**：本文解决的是大型语言模型推理中的时序侧信道攻击问题，现有的用户隔离方法虽然能防止信息泄露，但在性能上存在显著下降。

**核心思路**：SafeKV框架的核心思想是通过选择性共享非敏感缓存条目，来平衡隐私保护与性能提升，避免了全面隔离带来的性能损失。

**技术框架**：SafeKV由三个主要模块组成：混合多层检测管道、统一的基数树索引和基于熵的访问监控。检测管道负责识别敏感信息，基数树索引管理不同内存层次的缓存条目，访问监控则用于检测信息泄露。

**关键创新**：SafeKV的创新在于其选择性共享机制，能够在不牺牲性能的前提下，显著降低时序侧信道攻击的风险。这一机制与传统的用户隔离方法形成鲜明对比。

**关键设计**：在设计中，SafeKV采用了混合检测策略，结合规则匹配和上下文感知验证，同时使用统一的基数树索引来高效管理缓存条目，确保了高效的内存使用和快速访问。通过熵监控，进一步降低了信息泄露的风险。

## 📊 实验亮点

实验结果显示，SafeKV能够有效减轻94%-97%的时序侧信道攻击，相比于用户隔离方法，TTFT提升高达40.58%，吞吐量提高至2.66倍，显著降低了缓存引起的TTFT开销，从50.41%降至11.74%。

## 🎯 应用场景

SafeKV框架具有广泛的应用潜力，尤其在需要处理敏感信息的高吞吐量场景中，如金融、医疗和在线服务等领域。通过提升隐私保护能力和系统性能，SafeKV能够为这些领域的LLM推理提供更安全的解决方案，推动智能应用的发展。

## 📄 摘要（原文）

> Global KV-cache sharing has emerged as a key optimization for accelerating large language model (LLM) inference. However, it exposes a new class of timing side-channel attacks, enabling adversaries to infer sensitive user inputs via shared cache entries. Existing defenses, such as per-user isolation, eliminate leakage but degrade performance by up to 38.9% in time-to-first-token (TTFT), making them impractical for high-throughput deployment. To address this gap, we introduce SafeKV (Secure and Flexible KV Cache Sharing), a privacy-aware KV-cache management framework that selectively shares non-sensitive entries while confining sensitive content to private caches. SafeKV comprises three components: (i) a hybrid, multi-tier detection pipeline that integrates rule-based pattern matching, a general-purpose privacy detector, and context-aware validation; (ii) a unified radix-tree index that manages public and private entries across heterogeneous memory tiers (HBM, DRAM, SSD); and (iii) entropy-based access monitoring to detect and mitigate residual information leakage. Our evaluation shows that SafeKV mitigates 94% - 97% of timing-based side-channel attacks. Compared to per-user isolation method, SafeKV improves TTFT by up to 40.58% and throughput by up to 2.66X across diverse LLMs and workloads. SafeKV reduces cache-induced TTFT overhead from 50.41% to 11.74% on Qwen3-235B. By combining fine-grained privacy control with high cache reuse efficiency, SafeKV reclaims the performance advantages of global sharing while providing robust runtime privacy guarantees for LLM inference.

