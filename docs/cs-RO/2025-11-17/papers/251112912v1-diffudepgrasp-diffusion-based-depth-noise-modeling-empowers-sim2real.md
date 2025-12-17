---
layout: default
title: DiffuDepGrasp: Diffusion-based Depth Noise Modeling Empowers Sim2Real Robotic Grasping
---

# DiffuDepGrasp: Diffusion-based Depth Noise Modeling Empowers Sim2Real Robotic Grasping

<div class="paper-toolbar">
  <div class="toolbar-left">
    <a href="https://arxiv.org/abs/2511.12912" target="_blank" class="toolbar-btn">arXiv: 2511.12912v1</a>
    <a href="https://arxiv.org/pdf/2511.12912.pdf" target="_blank" class="toolbar-btn">PDF</a>
  </div>
  <div class="toolbar-right">
    <button class="toolbar-btn favorite-btn" data-arxiv-id="2511.12912v1" 
            onclick="toggleFavorite(this, '2511.12912v1', 'DiffuDepGrasp: Diffusion-based Depth Noise Modeling Empowers Sim2Real Robotic Grasping')" title="收藏">
      ☆ 收藏
    </button>
    <button class="toolbar-btn share-btn" onclick="copyLink()" title="复制链接">
      🔗 分享
    </button>
  </div>
</div>


**作者**: Yingting Zhou, Wenbo Cui, Weiheng Liu, Guixing Chen, Haoran Li, Dongbin Zhao

**分类**: cs.RO

**发布日期**: 2025-11-17

**🔗 代码/项目**: [PROJECT_PAGE](https://diffudepgrasp.github.io/)

---

## 💡 一句话要点

**DiffuDepGrasp：基于扩散模型的深度噪声建模实现Sim2Real机器人抓取**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)**

**关键词**: `机器人抓取` `Sim2Real` `扩散模型` `深度噪声建模` `零样本迁移`

## 📋 核心要点

1. 现有基于深度信息的端到端策略在Sim2Real迁移中受阻于真实深度图中的空洞和噪声，导致数据效率低下。
2. DiffuDepGrasp通过扩散深度生成器学习传感器噪声，并将其注入到仿真深度图中，从而弥合Sim2Real差距。
3. 实验表明，DiffuDepGrasp在零样本迁移设置下，对12个对象的抓取成功率达到95.7%，并具有良好的泛化能力。

## 📝 摘要（中文）

本文提出DiffuDepGrasp，一个高效的sim2real框架，通过纯仿真训练实现零样本迁移。该框架的核心创新是扩散深度生成器，它通过两个协同模块合成具有传感器真实噪声的几何上干净的仿真深度图。扩散深度模块利用时间几何先验，实现条件扩散模型的样本高效训练，捕捉复杂的传感器噪声分布。噪声嫁接模块在注入感知伪影时保持度量精度。DiffuDepGrasp在部署期间仅需原始深度输入，消除了计算开销，并在12个对象的抓取任务中实现了95.7%的平均成功率，具有零样本迁移能力和对未见物体的强大泛化能力。

## 🔬 方法详解

**问题定义**：现有方法在仿真环境中训练机器人抓取策略，然后迁移到真实机器人上。然而，真实深度传感器数据存在噪声、空洞等问题，导致Sim2Real性能下降。现有的噪声注入方法通常数据效率低，且难以模拟真实的传感器噪声分布，而利用预训练模型的方法则引入了额外的计算开销。

**核心思路**：DiffuDepGrasp的核心思路是通过学习真实深度传感器的噪声分布，并在仿真环境中生成带有真实噪声的深度图，从而使仿真环境更接近真实环境。这样，在仿真环境中训练的策略可以直接迁移到真实机器人上，实现零样本迁移。

**技术框架**：DiffuDepGrasp包含两个主要模块：扩散深度模块和噪声嫁接模块。扩散深度模块利用时间几何先验，训练一个条件扩散模型，学习真实深度传感器的噪声分布。噪声嫁接模块将学习到的噪声注入到仿真深度图中，同时保持度量精度。整个流程在仿真环境中进行，真实环境中只需要原始深度输入。

**关键创新**：DiffuDepGrasp的关键创新在于使用扩散模型学习深度传感器的噪声分布，并将其注入到仿真深度图中。与传统的噪声注入方法相比，扩散模型能够更准确地捕捉复杂的传感器噪声分布，从而提高Sim2Real迁移的性能。此外，该方法不需要额外的计算开销，可以直接部署在真实机器人上。

**关键设计**：扩散深度模块使用时间几何先验作为条件，指导扩散模型的训练。噪声嫁接模块使用特定的损失函数，确保在注入噪声的同时保持度量精度。具体的网络结构和参数设置在论文中有详细描述。

## 📊 实验亮点

DiffuDepGrasp在12个对象的抓取任务中实现了95.7%的平均成功率，显著优于现有的Sim2Real方法。该方法具有零样本迁移能力，可以直接将仿真环境中训练的策略部署到真实机器人上，无需额外的微调。此外，DiffuDepGrasp对未见物体具有良好的泛化能力，能够适应不同的抓取场景。

## 🎯 应用场景

DiffuDepGrasp可应用于各种需要机器人抓取的场景，如工业自动化、物流分拣、家庭服务等。该方法能够提高机器人抓取的鲁棒性和泛化能力，降低部署成本，加速机器人技术的应用和普及。未来，该方法可以扩展到其他类型的传感器数据，如RGB图像、点云等，进一步提高Sim2Real迁移的性能。

## 📄 摘要（原文）

> Transferring the depth-based end-to-end policy trained in simulation to physical robots can yield an efficient and robust grasping policy, yet sensor artifacts in real depth maps like voids and noise establish a significant sim2real gap that critically impedes policy transfer. Training-time strategies like procedural noise injection or learned mappings suffer from data inefficiency due to unrealistic noise simulation, which is often ineffective for grasping tasks that require fine manipulation or dependency on paired datasets heavily. Furthermore, leveraging foundation models to reduce the sim2real gap via intermediate representations fails to mitigate the domain shift fully and adds computational overhead during deployment. This work confronts dual challenges of data inefficiency and deployment complexity. We propose DiffuDepGrasp, a deploy-efficient sim2real framework enabling zero-shot transfer through simulation-exclusive policy training. Its core innovation, the Diffusion Depth Generator, synthesizes geometrically pristine simulation depth with learned sensor-realistic noise via two synergistic modules. The first Diffusion Depth Module leverages temporal geometric priors to enable sample-efficient training of a conditional diffusion model that captures complex sensor noise distributions, while the second Noise Grafting Module preserves metric accuracy during perceptual artifact injection. With only raw depth inputs during deployment, DiffuDepGrasp eliminates computational overhead and achieves a 95.7% average success rate on 12-object grasping with zero-shot transfer and strong generalization to unseen objects.Project website: https://diffudepgrasp.github.io/.

