---
layout: default
title: Backdoor Attacks on Prompt-Driven Video Segmentation Foundation Models
---

# Backdoor Attacks on Prompt-Driven Video Segmentation Foundation Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.22046" class="toolbar-btn" target="_blank">📄 arXiv: 2512.22046v1</a>
  <a href="https://arxiv.org/pdf/2512.22046.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.22046v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.22046v1', 'Backdoor Attacks on Prompt-Driven Video Segmentation Foundation Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zongmin Zhang, Zhen Sun, Yifan Liao, Wenhan Dong, Xinlei He, Xingshuo Han, Shengmin Xu, Xinyi Huang

**分类**: cs.CV, cs.CR

**发布日期**: 2025-12-26

---

## 💡 一句话要点

**提出BadVSFM，针对Prompt驱动的视频分割基础模型的后门攻击框架。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `后门攻击` `视频分割基础模型` `Prompt驱动` `对抗性攻击` `深度学习安全`

## 📋 核心要点

1. 现有的视频分割基础模型易受后门攻击威胁，但直接应用传统后门攻击方法效果不佳。
2. BadVSFM通过两阶段策略，分别操控图像编码器和掩码解码器，实现对VSFM的有效后门攻击。
3. 实验证明BadVSFM在保持分割质量的同时，实现了高攻击成功率，且能有效绕过现有防御手段。

## 📝 摘要（中文）

Prompt驱动的视频分割基础模型(VSFM)，如SAM2，正被广泛应用于自动驾驶和数字病理等领域，引发了对后门攻击的担忧。令人惊讶的是，我们发现直接将经典后门攻击(如BadNet)迁移到VSFM几乎无效，攻击成功率低于5%。为了理解这一点，我们研究了编码器梯度和注意力图，观察到传统训练保持了干净样本和触发样本的梯度基本对齐，并且注意力仍然集中在真实对象上，从而阻止了编码器学习到与触发器相关的独特表示。为了解决这个挑战，我们提出了BadVSFM，这是第一个专门为prompt驱动的VSFM量身定制的后门框架。BadVSFM使用两阶段策略：(1)引导图像编码器，使触发帧映射到指定的目标嵌入，而干净帧保持与干净参考编码器对齐；(2)训练掩码解码器，使得在各种prompt类型下，触发帧-prompt对产生共享的目标掩码，而干净输出保持接近参考解码器。在两个数据集和五个VSFM上的大量实验表明，BadVSFM在各种触发器和prompt下实现了强大且可控的后门效果，同时保持了干净分割质量。对损失、阶段、目标、触发器设置和中毒率的消融研究表明，该方法对合理的超参数变化具有鲁棒性，并证实了两阶段设计的必要性。最后，梯度冲突分析和注意力可视化表明，BadVSFM分离了触发和干净表示，并将注意力转移到触发区域，而四种代表性的防御方法仍然基本无效，揭示了当前VSFM中一个未被充分探索的漏洞。

## 🔬 方法详解

**问题定义**：论文旨在解决Prompt驱动的视频分割基础模型(VSFM)的后门攻击问题。现有方法，例如直接应用图像领域的后门攻击方法（如BadNet），在VSFM上效果不佳，攻击成功率很低。这是因为VSFM的训练方式使得触发样本和干净样本在编码器中梯度对齐，注意力机制也倾向于关注真实物体，导致触发器无法被有效学习。

**核心思路**：BadVSFM的核心思路是通过两阶段训练，分别操控图像编码器和掩码解码器，从而在VSFM中植入后门。第一阶段，引导图像编码器将触发帧映射到指定的目标嵌入，同时保持干净帧的表示不变。第二阶段，训练掩码解码器，使得触发帧与任意prompt组合都能生成预设的目标掩码。

**技术框架**：BadVSFM包含两个主要阶段：编码器操控阶段和解码器训练阶段。在编码器操控阶段，使用对比学习损失，促使触发帧的编码向量接近目标向量，同时使用参考编码器保持干净样本的表示。在解码器训练阶段，使用交叉熵损失和参考解码器，使得触发帧与任意prompt组合都能生成目标掩码，同时保持干净样本的分割结果。

**关键创新**：BadVSFM的关键创新在于其两阶段训练策略，该策略能够有效分离触发样本和干净样本的表示，并引导模型将注意力转移到触发区域。与直接应用传统后门攻击方法相比，BadVSFM能够更有效地控制后门行为，并提高攻击成功率。

**关键设计**：在编码器操控阶段，使用了对比学习损失，具体形式为InfoNCE损失，用于拉近触发帧的编码向量和目标向量。同时，使用L2损失约束干净样本的编码向量与参考编码器的输出。在解码器训练阶段，使用了交叉熵损失，用于训练解码器生成目标掩码。此外，还使用了L2损失约束干净样本的分割结果与参考解码器的输出。目标向量的选择和触发器的设计也是关键的技术细节。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.22046v1/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.22046v1/x2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.22046v1/x3.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

实验结果表明，BadVSFM在两个数据集和五个VSFM上实现了强大的后门攻击效果，攻击成功率远高于直接应用传统后门攻击方法。消融实验验证了两阶段设计的必要性，并表明该方法对超参数变化具有鲁棒性。梯度冲突分析和注意力可视化表明，BadVSFM能够有效分离触发和干净表示，并将注意力转移到触发区域。此外，实验还表明，四种代表性的防御方法对BadVSFM基本无效。

## 🎯 应用场景

该研究成果可应用于评估和增强视频分割基础模型在安全领域的鲁棒性。通过模拟后门攻击，可以更好地理解模型的脆弱性，并开发相应的防御机制。此外，该研究也为开发更安全的视频分析系统提供了理论基础，例如在自动驾驶、医疗影像分析等关键领域。

## 📄 摘要（原文）

> Prompt-driven Video Segmentation Foundation Models (VSFMs) such as SAM2 are increasingly deployed in applications like autonomous driving and digital pathology, raising concerns about backdoor threats. Surprisingly, we find that directly transferring classic backdoor attacks (e.g., BadNet) to VSFMs is almost ineffective, with ASR below 5\%. To understand this, we study encoder gradients and attention maps and observe that conventional training keeps gradients for clean and triggered samples largely aligned, while attention still focuses on the true object, preventing the encoder from learning a distinct trigger-related representation. To address this challenge, we propose BadVSFM, the first backdoor framework tailored to prompt-driven VSFMs. BadVSFM uses a two-stage strategy: (1) steer the image encoder so triggered frames map to a designated target embedding while clean frames remain aligned with a clean reference encoder; (2) train the mask decoder so that, across prompt types, triggered frame-prompt pairs produce a shared target mask, while clean outputs stay close to a reference decoder. Extensive experiments on two datasets and five VSFMs show that BadVSFM achieves strong, controllable backdoor effects under diverse triggers and prompts while preserving clean segmentation quality. Ablations over losses, stages, targets, trigger settings, and poisoning rates demonstrate robustness to reasonable hyperparameter changes and confirm the necessity of the two-stage design. Finally, gradient-conflict analysis and attention visualizations show that BadVSFM separates triggered and clean representations and shifts attention to trigger regions, while four representative defenses remain largely ineffective, revealing an underexplored vulnerability in current VSFMs.

