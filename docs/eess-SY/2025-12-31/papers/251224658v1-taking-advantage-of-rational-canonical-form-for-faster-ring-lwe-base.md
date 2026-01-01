---
layout: default
title: Taking Advantage of Rational Canonical Form for Faster Ring-LWE based Encrypted Controller with Recursive Multiplication
---

# Taking Advantage of Rational Canonical Form for Faster Ring-LWE based Encrypted Controller with Recursive Multiplication

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.24658" class="toolbar-btn" target="_blank">📄 arXiv: 2512.24658v1</a>
  <a href="https://arxiv.org/pdf/2512.24658.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.24658v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.24658v1', 'Taking Advantage of Rational Canonical Form for Faster Ring-LWE based Encrypted Controller with Recursive Multiplication')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Donghyeon Song, Yeongjun Jang, Joowon Lee, Junsoo Kim

**分类**: eess.SY

**发布日期**: 2025-12-31

**备注**: 8 pages, 1 figures, presented at 2025 IEEE Conference on Decision and Control

---

## 💡 一句话要点

**利用有理标准型加速基于Ring-LWE的加密控制器递归乘法**

🎯 **匹配领域**: **支柱五：交互与反应 (Interaction & Reaction)**

**关键词**: `加密控制` `Ring-LWE` `同态加密` `有理标准型` `递归乘法`

## 📋 核心要点

1. 现有加密控制器在递归乘法中计算复杂度高，效率受限。
2. 将状态矩阵转换为有理标准型，利用其稀疏性减少加密和计算量。
3. 提出一种打包输入输出矩阵的新方法，进一步减少同态运算次数，提升效率。

## 📝 摘要（中文）

本文旨在为基于Ring-LWE的密码系统上执行递归乘法的加密线性动态控制器提供一种高效的实现方案。通过采用系统理论方法，我们显著降低了时间和空间复杂度，特别是递归乘法所需的同态运算次数。与加密给定控制器的整个状态矩阵不同，我们将状态矩阵转换为其有理标准型，其稀疏和循环结构使得仅需加密和计算其非平凡列。此外，我们提出了一种新颖的方法来将输入和输出矩阵“打包”成单个多项式，从而减少同态运算的次数。仿真结果表明，所提出的设计能够实现非常快速的加密控制器实现。

## 🔬 方法详解

**问题定义**：论文旨在解决基于Ring-LWE的加密线性动态控制器中，递归乘法计算复杂度高、效率低下的问题。现有方法通常直接加密整个状态矩阵，导致大量的同态运算，时间和空间复杂度都很高。

**核心思路**：论文的核心思路是将控制器的状态矩阵转换为有理标准型。有理标准型具有稀疏和循环的结构，这意味着只需要加密和计算矩阵的非平凡列，从而显著减少了计算量。此外，通过将输入和输出矩阵打包成单个多项式，进一步减少了同态运算的次数。

**技术框架**：该方法主要包含以下几个阶段：1) 将控制器的状态矩阵转换为有理标准型；2) 仅加密有理标准型的非平凡列；3) 将输入和输出矩阵打包成单个多项式；4) 在加密域中执行递归乘法；5) 解密结果。整体框架旨在利用有理标准型的特性来优化加密控制器的性能。

**关键创新**：论文的关键创新在于两个方面：一是将有理标准型应用于加密控制器，利用其稀疏性降低计算复杂度；二是提出了一种新的打包方法，将输入和输出矩阵打包成单个多项式，进一步减少同态运算的次数。与现有方法直接加密整个状态矩阵相比，该方法在计算效率上具有显著优势。

**关键设计**：论文的关键设计包括：选择合适的Ring-LWE参数以保证安全性和性能；设计高效的打包和解包算法，以减少打包过程中的计算开销；优化同态乘法运算，例如使用Number Theoretic Transform (NTT) 等技术加速多项式乘法。

## 📊 实验亮点

仿真结果表明，该设计能够实现非常快速的加密控制器实现。通过将状态矩阵转换为有理标准型并采用新的打包方法，显著减少了同态运算的次数，从而提高了加密控制器的计算效率。具体的性能数据和与现有方法的对比结果（例如加速比）在论文中进行了详细展示。

## 🎯 应用场景

该研究成果可应用于对安全性要求较高的控制系统中，例如无人机控制、机器人控制、智能电网等。通过加密控制器，可以防止恶意攻击者篡改控制策略，保障系统的安全稳定运行。该方法在保护隐私的同时，实现了控制系统的功能，具有重要的实际应用价值。

## 📄 摘要（原文）

> This paper aims to provide an efficient implementation of encrypted linear dynamic controllers that perform recursive multiplications on a Ring-Learning With Errors (Ring-LWE) based cryptosystem. By adopting a system-theoretical approach, we significantly reduce both time and space complexities, particularly the number of homomorphic operations required for recursive multiplications. Rather than encrypting the entire state matrix of a given controller, the state matrix is transformed into its rational canonical form, whose sparse and circulant structure enables that encryption and computation are required only on its nontrivial columns. Furthermore, we propose a novel method to ``pack'' each of the input and the output matrices into a single polynomial, thereby reducing the number of homomorphic operations. Simulation results demonstrate that the proposed design enables a remarkably fast implementation of encrypted controllers.

