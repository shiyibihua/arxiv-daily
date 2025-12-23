---
layout: default
title: Effective Red-Teaming of Policy-Adherent Agents
---

# Effective Red-Teaming of Policy-Adherent Agents

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.09600" class="toolbar-btn" target="_blank">📄 arXiv: 2506.09600v3</a>
  <a href="https://arxiv.org/pdf/2506.09600.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.09600v3" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.09600v3', 'Effective Red-Teaming of Policy-Adherent Agents')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Itay Nakash, George Kour, Koren Lazar, Matan Vetzler, Guy Uziel, Ateret Anaby-Tavor

**分类**: cs.MA, cs.AI, cs.CL, cs.CR

**发布日期**: 2025-06-11 (更新: 2025-08-23)

---

## 💡 一句话要点

**提出CRAFT以增强政策遵循代理的安全性**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)**

**关键词**: `政策遵循代理` `恶意用户` `红队系统` `劝说策略` `鲁棒性评估` `客户服务` `安全防护`

## 📋 核心要点

1. 现有方法在确保政策遵循代理的安全性方面面临挑战，尤其是在恶意用户的操控下。
2. 本文提出CRAFT系统，通过政策意识的劝说策略来增强代理的防御能力，针对恶意用户的攻击进行有效应对。
3. 实验结果表明，CRAFT在客户服务场景中显著优于传统的越狱方法，展示了更强的鲁棒性和防御能力。

## 📝 摘要（中文）

基于任务导向的大型语言模型（LLM）代理在严格政策领域的应用日益增多，如退款资格或取消规则。确保代理始终遵循这些规则并适当地拒绝任何违反请求的挑战日益突出。为此，本文提出了一种新型威胁模型，专注于利用政策遵循代理的恶意用户。我们提出CRAFT，一个多代理红队系统，利用政策意识的劝说策略来削弱客户服务场景中的政策遵循代理，超越传统的越狱方法。基于现有的tau-bench基准，我们引入了tau-break，一个补充基准，用于严格评估代理对操控性用户行为的鲁棒性。最后，我们评估了几种简单但有效的防御策略，尽管这些措施提供了一定的保护，但仍显不足，强调了需要更强的研究驱动的保护措施来防止对政策遵循代理的攻击。

## 🔬 方法详解

**问题定义**：本文旨在解决政策遵循代理在面对恶意用户时的脆弱性，现有方法未能有效防止用户利用代理的政策漏洞进行操控。

**核心思路**：论文提出CRAFT系统，利用多代理红队策略，通过政策意识的劝说手段来模拟恶意用户的攻击，从而评估和增强代理的鲁棒性。

**技术框架**：CRAFT系统由多个代理组成，模拟不同类型的用户行为，采用政策意识的劝说策略进行交互，评估代理的反应和适应能力。

**关键创新**：CRAFT的创新在于其针对政策遵循代理的特定威胁模型，利用劝说策略而非传统的越狱方法，提供了一种新的评估和防御框架。

**关键设计**：在设计中，CRAFT系统采用了多种策略组合，结合了用户行为模拟、策略评估和防御机制，确保了系统在多种攻击场景下的有效性。具体参数和损失函数的设置尚未详细披露。

## 📊 实验亮点

实验结果显示，CRAFT系统在客户服务场景中显著优于传统的越狱方法，提升了代理的鲁棒性和防御能力，具体性能数据尚未披露，但强调了对抗恶意用户的有效性。

## 🎯 应用场景

该研究的潜在应用领域包括客户服务、金融服务和任何需要遵循严格政策的自动化系统。通过增强政策遵循代理的安全性，能够有效防止恶意用户的操控，提升用户体验和系统的可靠性，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> Task-oriented LLM-based agents are increasingly used in domains with strict policies, such as refund eligibility or cancellation rules. The challenge lies in ensuring that the agent consistently adheres to these rules and policies, appropriately refusing any request that would violate them, while still maintaining a helpful and natural interaction. This calls for the development of tailored design and evaluation methodologies to ensure agent resilience against malicious user behavior. We propose a novel threat model that focuses on adversarial users aiming to exploit policy-adherent agents for personal benefit. To address this, we present CRAFT, a multi-agent red-teaming system that leverages policy-aware persuasive strategies to undermine a policy-adherent agent in a customer-service scenario, outperforming conventional jailbreak methods such as DAN prompts, emotional manipulation, and coercive. Building upon the existing tau-bench benchmark, we introduce tau-break, a complementary benchmark designed to rigorously assess the agent's robustness against manipulative user behavior. Finally, we evaluate several straightforward yet effective defense strategies. While these measures provide some protection, they fall short, highlighting the need for stronger, research-driven safeguards to protect policy-adherent agents from adversarial attacks

