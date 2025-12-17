---
layout: default
title: Benchmarking individual tree segmentation using multispectral airborne laser scanning data: the FGI-EMIT dataset
---

# Benchmarking individual tree segmentation using multispectral airborne laser scanning data: the FGI-EMIT dataset

**arXiv**: [2511.00653v1](https://arxiv.org/abs/2511.00653) | [PDF](https://arxiv.org/pdf/2511.00653.pdf)

**作者**: Lassi Ruoppa, Tarmo Hietala, Verneri Seppänen, Josef Taher, Teemu Hakala, Xiaowei Yu, Antero Kukko, Harri Kaartinen, Juha Hyyppä

**分类**: cs.CV

**发布日期**: 2025-11-01

**备注**: 39 pages, 9 figures

---

## 💡 一句话要点

**FGI-EMIT：多光谱激光雷达树木分割基准数据集与深度学习方法性能评估**

🎯 **匹配领域**: **支柱三：空间感知 (Perception & SLAM)**

**关键词**: `个体树木分割` `多光谱激光雷达` `点云处理` `深度学习` `森林遥感` `基准数据集` `FGI-EMIT`

## 📋 核心要点

1. 个体树木分割是森林资源调查、碳监测和生物多样性评估的基础，传统方法受限于几何信息，缺乏大规模多光谱数据支持。
2. 本文构建了大规模多光谱激光雷达数据集FGI-EMIT，并对多种无监督和深度学习方法进行了基准测试。
3. 实验结果表明，深度学习方法显著优于传统方法，尤其在林下树木分割方面，但对多光谱信息的利用仍有提升空间。

## 📝 摘要（中文）

本文介绍了FGI-EMIT，这是一个用于个体树木分割（ITS）的首个大规模多光谱机载激光扫描基准数据集。该数据集包含532、905和1550纳米波长的数据，由1561棵手工标注的树木组成，特别关注了小型林下树木。研究使用FGI-EMIT全面评估了四种传统的无监督算法和四种有监督的深度学习（DL）方法。无监督方法的超参数通过贝叶斯方法优化，而DL模型则从头开始训练。在无监督方法中，Treeiso达到了最高的测试集F1分数52.7%。总体而言，DL方法表现明显更好，其中最佳模型ForestFormer3D的F1分数为73.3%。在林下树木的分割上，ForestFormer3D比Treeiso高出25.9个百分点。消融研究表明，当前的基于DL的方法通常无法有效利用多光谱反射信息，尽管单通道反射率可以略微提高准确性，尤其是在林下树木方面。点云密度分析表明，即使在低至10个点/平方米的密度下，DL方法也始终优于无监督算法。

## 🔬 方法详解

**问题定义**：个体树木分割（ITS）旨在从点云数据中准确识别和分割出单棵树木。现有方法，特别是传统的无监督算法，在处理复杂森林环境（如林下树木）时精度有限。此外，缺乏大规模多光谱激光雷达数据限制了算法的开发和评估，阻碍了利用多光谱信息提升分割性能的研究。

**核心思路**：本文的核心思路是构建一个大规模、高质量的多光谱激光雷达数据集FGI-EMIT，并利用该数据集对现有的无监督和深度学习ITS算法进行全面基准测试。通过对比不同算法的性能，揭示现有方法的优缺点，并为未来算法的开发提供指导。同时，研究还探讨了多光谱信息在ITS中的作用。

**技术框架**：研究主要分为三个阶段：1) 数据集构建：采集并手工标注包含多光谱信息的激光雷达点云数据，构建FGI-EMIT数据集。2) 算法基准测试：选择四种无监督算法和四种深度学习算法，在FGI-EMIT数据集上进行训练和测试。无监督算法的超参数通过贝叶斯优化方法进行优化。3) 性能分析：对比不同算法的分割精度（F1-score），分析多光谱信息和点云密度对分割性能的影响。

**关键创新**：该研究的关键创新在于构建了首个大规模多光谱机载激光扫描基准数据集FGI-EMIT，为个体树木分割算法的研究提供了重要的数据资源。此外，研究还系统地评估了现有无监督和深度学习算法在多光谱数据上的性能，并分析了多光谱信息对分割精度的影响。

**关键设计**：在数据集构建方面，特别关注了小型林下树木的标注，以提高数据集的代表性。在算法选择方面，选择了具有代表性的无监督算法（如Treeiso）和深度学习算法（如ForestFormer3D）。在实验设置方面，采用了贝叶斯优化方法来优化无监督算法的超参数，并从头开始训练深度学习模型，以保证公平性。消融实验用于评估多光谱信息的作用。

## 📊 实验亮点

实验结果表明，深度学习方法在个体树木分割任务中显著优于传统无监督算法。最佳模型ForestFormer3D在FGI-EMIT数据集上取得了73.3%的F1-score，相比于最佳无监督方法Treeiso的52.7%有显著提升。尤其在林下树木的分割上，ForestFormer3D比Treeiso高出25.9个百分点。消融实验表明，现有深度学习方法对多光谱信息的利用效率仍有提升空间。

## 🎯 应用场景

该研究成果可广泛应用于森林资源调查、碳储量估算、生物多样性监测等领域。高质量的个体树木分割结果能够为精准林业管理提供支持，例如优化采伐计划、评估森林健康状况等。FGI-EMIT数据集的发布将促进相关算法的开发和改进，推动森林遥感技术的进步。

## 📄 摘要（原文）

> Individual tree segmentation (ITS) from LiDAR point clouds is fundamental for applications such as forest inventory, carbon monitoring and biodiversity assessment. Traditionally, ITS has been achieved with unsupervised geometry-based algorithms, while more recent advances have shifted toward supervised deep learning (DL). In the past, progress in method development was hindered by the lack of large-scale benchmark datasets, and the availability of novel data formats, particularly multispectral (MS) LiDAR, remains limited to this day, despite evidence that MS reflectance can improve the accuracy of ITS. This study introduces FGI-EMIT, the first large-scale MS airborne laser scanning benchmark dataset for ITS. Captured at wavelengths 532, 905, and 1,550 nm, the dataset consists of 1,561 manually annotated trees, with a particular focus on small understory trees. Using FGI-EMIT, we comprehensively benchmarked four conventional unsupervised algorithms and four supervised DL approaches. Hyperparameters of unsupervised methods were optimized using a Bayesian approach, while DL models were trained from scratch. Among the unsupervised methods, Treeiso achieved the highest test set F1-score of 52.7%. The DL approaches performed significantly better overall, with the best model, ForestFormer3D, attaining an F1-score of 73.3%. The most significant difference was observed in understory trees, where ForestFormer3D exceeded Treeiso by 25.9 percentage points. An ablation study demonstrated that current DL-based approaches generally fail to leverage MS reflectance information when it is provided as additional input features, although single channel reflectance can improve accuracy marginally, especially for understory trees. A performance analysis across point densities further showed that DL methods consistently remain superior to unsupervised algorithms, even at densities as low as 10 points/m$^2$.

