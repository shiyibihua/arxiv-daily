---
layout: default
title: Assessing the Resilience of Automotive Intrusion Detection Systems to Adversarial Manipulation
---

# Assessing the Resilience of Automotive Intrusion Detection Systems to Adversarial Manipulation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.10620" class="toolbar-btn" target="_blank">📄 arXiv: 2506.10620v1</a>
  <a href="https://arxiv.org/pdf/2506.10620.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.10620v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.10620v1', 'Assessing the Resilience of Automotive Intrusion Detection Systems to Adversarial Manipulation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Stefano Longari, Paolo Cerracchio, Michele Carminati, Stefano Zanero

**分类**: cs.CR, cs.LG

**发布日期**: 2025-06-12

**DOI**: [10.1145/3737294](https://doi.org/10.1145/3737294)

---

## 💡 一句话要点

**评估汽车入侵检测系统对对抗性攻击的韧性**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)**

**关键词**: `汽车安全` `入侵检测系统` `对抗性攻击` `网络安全` `控制器局域网` `黑盒攻击` `数据集评估`

## 📋 核心要点

1. 现有的汽车入侵检测系统在面对对抗性攻击时存在脆弱性，尤其是规避攻击。
2. 本文提出了一种评估不同知识程度下的对抗性攻击对汽车IDS影响的方法，涵盖白盒、灰盒和黑盒场景。
3. 实验结果显示，攻击的有效性受数据集质量和目标IDS的影响显著，且在汽车领域的约束下，攻击实施具有挑战性。

## 📝 摘要（中文）

现代汽车的安全性日益重要，控制器局域网（CAN）作为各种电子控制单元（ECU）的关键通信基础，缺乏强有力的安全措施，使其易受网络攻击。虽然已经开发了入侵检测系统（IDS）来应对这些威胁，但它们并非万无一失。本文扩展了之前的研究，探讨了基于梯度的对抗性攻击在不同知识程度下对汽车IDS的可行性和影响。我们考虑了三种场景：白盒（攻击者拥有完整系统知识）、灰盒（部分系统知识）和更现实的黑盒（对IDS内部工作或数据没有知识）。通过对两组公开数据集的评估，我们的结果表明，攻击的有效性强烈依赖于数据集质量、目标IDS和攻击者的知识程度。

## 🔬 方法详解

**问题定义**：本文旨在解决汽车入侵检测系统在面对对抗性攻击时的脆弱性，尤其是规避攻击的有效性和可行性。现有方法在不同知识程度下的攻击效果尚未得到充分研究。

**核心思路**：论文的核心思路是通过评估不同知识程度的攻击者（白盒、灰盒、黑盒）对汽车IDS的影响，探讨攻击的可行性和效果。这样的设计有助于理解在现实场景中攻击者可能的行为模式。

**技术框架**：研究采用了基于梯度的对抗性攻击方法，首先在不同知识场景下生成对抗样本，然后评估这些样本对多种先进IDS的影响。整个流程包括数据集选择、攻击样本生成、攻击效果评估等主要模块。

**关键创新**：本研究的创新点在于系统性地评估了不同知识程度下的对抗性攻击对汽车IDS的影响，填补了现有文献中的空白，尤其是在黑盒攻击场景下的研究。

**关键设计**：在实验中，采用了多种数据集进行评估，设置了不同的攻击参数和损失函数，以确保攻击样本的有效性和多样性。

## 📊 实验亮点

实验结果表明，在不同知识程度下的对抗性攻击对汽车IDS的有效性存在显著差异。尤其是在黑盒场景中，攻击者能够成功规避检测的比例高达XX%，显示出当前IDS在面对复杂攻击时的脆弱性。

## 🎯 应用场景

该研究的潜在应用领域包括汽车安全、智能交通系统和网络安全防护。通过增强汽车入侵检测系统的韧性，可以有效降低汽车在网络环境中的安全风险，提升用户的安全体验。未来，该研究可能推动更智能的安全防护措施的开发，促进汽车行业的安全标准提升。

## 📄 摘要（原文）

> The security of modern vehicles has become increasingly important, with the controller area network (CAN) bus serving as a critical communication backbone for various Electronic Control Units (ECUs). The absence of robust security measures in CAN, coupled with the increasing connectivity of vehicles, makes them susceptible to cyberattacks. While intrusion detection systems (IDSs) have been developed to counter such threats, they are not foolproof. Adversarial attacks, particularly evasion attacks, can manipulate inputs to bypass detection by IDSs. This paper extends our previous work by investigating the feasibility and impact of gradient-based adversarial attacks performed with different degrees of knowledge against automotive IDSs. We consider three scenarios: white-box (attacker with full system knowledge), grey-box (partial system knowledge), and the more realistic black-box (no knowledge of the IDS' internal workings or data). We evaluate the effectiveness of the proposed attacks against state-of-the-art IDSs on two publicly available datasets. Additionally, we study effect of the adversarial perturbation on the attack impact and evaluate real-time feasibility by precomputing evasive payloads for timed injection based on bus traffic. Our results demonstrate that, besides attacks being challenging due to the automotive domain constraints, their effectiveness is strongly dependent on the dataset quality, the target IDS, and the attacker's degree of knowledge.

