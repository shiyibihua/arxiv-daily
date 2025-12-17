---
layout: default
title: ReIDMamba: Learning Discriminative Features with Visual State Space Model for Person Re-Identification
---

# ReIDMamba: Learning Discriminative Features with Visual State Space Model for Person Re-Identification

**arXiv**: [2511.07948v1](https://arxiv.org/abs/2511.07948) | [PDF](https://arxiv.org/pdf/2511.07948.pdf)

**作者**: Hongyang Gu, Qisong Yang, Lei Pu, Siming Han, Yao Ding

**分类**: cs.CV

**发布日期**: 2025-11-11

**备注**: 11 pages, 8 figures. Accepted to IEEE Transactions on Multimedia (TMM). Accepted Manuscript version uploaded

**🔗 代码/项目**: [GITHUB](https://github.com/GuHY777/ReIDMamba)

---

## 💡 一句话要点

**提出ReIDMamba，利用视觉状态空间模型学习判别性特征，实现高效行人重识别**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `行人重识别` `Mamba` `状态空间模型` `多粒度特征` `Triplet正则化`

## 📋 核心要点

1. 现有基于Transformer的ReID方法面临着计算和内存需求随输入序列长度呈二次方增长的可扩展性问题。
2. ReIDMamba采用纯Mamba架构，通过多粒度特征提取和排序感知的Triplet正则化来学习鲁棒的判别性特征。
3. ReIDMamba在五个行人ReID基准上取得了SOTA性能，且参数量仅为TransReID的三分之一，并降低了GPU内存占用。

## 📝 摘要（中文）

提取鲁棒的判别性特征是行人重识别（ReID）中的关键挑战。虽然基于Transformer的方法成功地解决了卷积神经网络（CNN）的一些局限性，例如其局部处理特性以及卷积和下采样操作导致的信息丢失，但由于内存和计算需求随输入序列长度呈二次方增长，它们仍然面临可扩展性问题。为了克服这一点，我们提出了一个纯粹基于Mamba的行人ReID框架，名为ReIDMamba。具体来说，我们设计了一个基于Mamba的强大基线，通过引入多个类别token来有效地利用细粒度的判别性全局特征。为了进一步增强Mamba中鲁棒特征的学习，我们精心设计了两种新颖的技术。首先，多粒度特征提取器（MGFE）模块采用多分支架构和类别token融合，有效地形成多粒度特征，增强了判别能力和细粒度覆盖。其次，引入了排序感知的Triplet正则化（RATR）来减少来自多个分支的特征冗余，通过结合类内和类间多样性约束来增强多粒度特征的多样性，从而确保行人特征的鲁棒性。据我们所知，这是第一个将纯Mamba驱动的方法集成到ReID研究中的工作。我们提出的ReIDMamba模型仅有TransReID三分之一的参数，同时具有更低的GPU内存使用量和更快的推理吞吐量。实验结果表明，ReIDMamba具有卓越和有希望的性能，在五个行人ReID基准上实现了最先进的性能。

## 🔬 方法详解

**问题定义**：行人重识别旨在跨不同的摄像头视角识别同一行人。现有基于Transformer的方法虽然在建模全局关系方面表现出色，但计算复杂度高，难以扩展到高分辨率图像。CNN方法则受限于局部感受野，难以捕捉全局上下文信息。因此，如何在保证性能的同时降低计算成本，是行人重识别领域的一个重要挑战。

**核心思路**：ReIDMamba的核心思路是利用Mamba架构的线性复杂度来克服Transformer的计算瓶颈，同时设计多粒度特征提取模块和排序感知的Triplet正则化来增强特征的判别性和鲁棒性。通过Mamba的全局建模能力和精心设计的特征提取策略，ReIDMamba能够在保持高性能的同时显著降低计算成本。

**技术框架**：ReIDMamba的整体框架包括：1) 输入图像经过一个初始的特征提取层；2) 提取的特征输入到多个Mamba块中进行全局特征建模；3) 多粒度特征提取器（MGFE）模块从Mamba块的输出中提取多粒度特征；4) 排序感知的Triplet正则化（RATR）用于优化特征表示；5) 最后，使用分类器进行身份预测。

**关键创新**：ReIDMamba的关键创新在于：1) 首次将纯Mamba架构引入行人重识别领域，利用其线性复杂度优势；2) 提出了多粒度特征提取器（MGFE），通过多分支结构和类别token融合，增强特征的判别能力和细粒度覆盖；3) 引入了排序感知的Triplet正则化（RATR），减少特征冗余，增强特征多样性。与现有方法相比，ReIDMamba在计算效率和特征表达能力上都具有优势。

**关键设计**：MGFE模块采用多分支结构，每个分支提取不同尺度的特征。类别token被用于融合不同分支的特征，从而形成多粒度表示。RATR损失函数结合了类内和类间多样性约束，鼓励模型学习更具区分性的特征。具体的损失函数设计和网络结构参数设置在论文中有详细描述。

## 📊 实验亮点

ReIDMamba在五个行人ReID基准数据集上取得了SOTA性能。例如，在Market-1501数据集上，Rank-1准确率达到了新的高度。更重要的是，ReIDMamba的参数量仅为TransReID的三分之一，同时降低了GPU内存占用，并提高了推理速度。这些结果表明，ReIDMamba在性能和效率方面都具有显著优势。

## 🎯 应用场景

ReIDMamba在智能安防、智慧城市等领域具有广泛的应用前景。例如，可以用于在大型商场、机场等公共场所进行行人追踪和身份识别，提高安全性和管理效率。此外，该方法还可以应用于智能零售、人流分析等领域，为商业决策提供数据支持。未来，ReIDMamba有望进一步扩展到其他视觉识别任务中。

## 📄 摘要（原文）

> Extracting robust discriminative features is a critical challenge in person re-identification (ReID). While Transformer-based methods have successfully addressed some limitations of convolutional neural networks (CNNs), such as their local processing nature and information loss resulting from convolution and downsampling operations, they still face the scalability issue due to the quadratic increase in memory and computational requirements with the length of the input sequence. To overcome this, we propose a pure Mamba-based person ReID framework named ReIDMamba. Specifically, we have designed a Mamba-based strong baseline that effectively leverages fine-grained, discriminative global features by introducing multiple class tokens. To further enhance robust features learning within Mamba, we have carefully designed two novel techniques. First, the multi-granularity feature extractor (MGFE) module, designed with a multi-branch architecture and class token fusion, effectively forms multi-granularity features, enhancing both discrimination ability and fine-grained coverage. Second, the ranking-aware triplet regularization (RATR) is introduced to reduce redundancy in features from multiple branches, enhancing the diversity of multi-granularity features by incorporating both intra-class and inter-class diversity constraints, thus ensuring the robustness of person features. To our knowledge, this is the pioneering work that integrates a purely Mamba-driven approach into ReID research. Our proposed ReIDMamba model boasts only one-third the parameters of TransReID, along with lower GPU memory usage and faster inference throughput. Experimental results demonstrate ReIDMamba's superior and promising performance, achieving state-of-the-art performance on five person ReID benchmarks. Code is available at https://github.com/GuHY777/ReIDMamba.

