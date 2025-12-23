---
layout: default
title: Midplane based 3D single pass unbiased segment-to-segment contact interaction using penalty method
---

# Midplane based 3D single pass unbiased segment-to-segment contact interaction using penalty method

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.04841" class="toolbar-btn" target="_blank">📄 arXiv: 2506.04841v1</a>
  <a href="https://arxiv.org/pdf/2506.04841.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.04841v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.04841v1', 'Midplane based 3D single pass unbiased segment-to-segment contact interaction using penalty method')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Indrajeet Sahu, Nik Petrinic

**分类**: cs.GR, math-ph

**发布日期**: 2025-06-05

---

## 💡 一句话要点

**提出无偏接触交互方法以解决接触面处理问题**

🎯 **匹配领域**: **支柱四：生成式动作 (Generative Motion)**

**关键词**: `接触交互` `无偏处理` `中平面方法` `接触力评估` `几何配置分析` `动态碰撞` `自接触问题` `材料科学`

## 📋 核心要点

1. 现有方法通常需要将接触表面指定为主从关系，限制了其灵活性和适用性。
2. 本文提出了一种基于中平面的接触交互方法，通过惩罚机制处理接触力，避免了主从表面的划分。
3. 实验结果表明，该方法在接触斑点测试、两梁弯曲、赫兹接触和扁平冲击测试中表现出色，准确性与有限元方法相当。

## 📝 摘要（中文）

本研究提出了一种接触交互方法，旨在无偏地处理接触表面，而无需将表面指定为主表面或从表面。通过相对于中平面的单次评估，保持接触力的平衡。接触力基于对相对表面真实重叠的惩罚，文中详细描述了离散接触段的积分过程。通过对不同几何配置的细致分析，验证了该方法在平面、曲面和尖角接触中的准确性和鲁棒性，显示出其在一般接触问题中的广泛适用性。

## 🔬 方法详解

**问题定义**：本研究旨在解决传统接触处理方法中主从表面划分的局限性，现有方法在处理复杂接触时常常面临准确性和灵活性不足的问题。

**核心思路**：提出了一种基于中平面的接触交互方法，通过对接触力的惩罚机制来处理相对表面的重叠，确保接触力的平衡和准确评估。

**技术框架**：整体流程包括接触面几何配置的分析、接触力的计算与积分、以及与解析解的对比验证，主要模块涵盖接触力评估、几何配置分析和结果验证。

**关键创新**：该方法的核心创新在于无偏接触处理，避免了传统方法的主从表面划分，能够更灵活地处理各种接触情况。

**关键设计**：在参数设置上，采用适当的惩罚因子和网格细化策略，以确保接触力的准确传递和收敛性，损失函数设计上强调接触力的平衡与真实重叠的惩罚。

## 📊 实验亮点

实验结果显示，该方法在接触斑点测试中实现了接触压力的均匀传递，准确性与有限元方法相当。通过网格细化和高惩罚因子的设置，方法能够收敛至解析解，展示了在平面、曲面及尖角接触中的高效性和准确性。

## 🎯 应用场景

该研究的潜在应用领域包括工程结构分析、材料科学以及机器人技术等，能够有效处理复杂接触问题，提高模拟精度和效率。未来，该方法有望在动态碰撞分析和自接触问题中发挥更大作用，推动相关领域的发展。

## 📄 摘要（原文）

> This work introduces a contact interaction methodology for an unbiased treatment of contacting surfaces without assigning surfaces as master and slave. The contact tractions between interacting discrete segments are evaluated with respect to a midplane in a single pass, inherently maintaining the equilibrium of tractions. These tractions are based on the penalisation of true interpenetration between opposite surfaces, and the procedure of their integral for discrete contacting segments is described in this paper. A meticulous examination of the different possible geometric configurations of interacting 3D segments is presented to develop visual understanding and better traction evaluation accuracy. The accuracy and robustness of the proposed method are validated against the analytical solutions of the contact patch test, two-beam bending, Hertzian contact, and flat punch test, thus proving the capability to reproduce contact between flat surfaces, curved surfaces, and sharp corners in contact, respectively. The method passes the contact patch test with the uniform transmission of contact pressure matching the accuracy levels of finite elements. It converges towards the analytical solution with mesh refinement and a suitably high penalty factor. The effectiveness of the proposed algorithm also extends to self-contact problems and has been tested for self-contact between flat and curved surfaces with inelastic material. Dynamic problems of elastic and inelastic collisions between bars, as well as oblique collisions of cylinders, are also presented. The ability of the algorithm to resolve contacts between flat and curved surfaces for nonconformal meshes with high accuracy demonstrates its versatility in general contact problems.

