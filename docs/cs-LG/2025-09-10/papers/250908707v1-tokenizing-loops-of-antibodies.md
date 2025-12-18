---
layout: default
title: Tokenizing Loops of Antibodies
---

# Tokenizing Loops of Antibodies

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.08707" class="toolbar-btn" target="_blank">📄 arXiv: 2509.08707v1</a>
  <a href="https://arxiv.org/pdf/2509.08707.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.08707v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.08707v1', 'Tokenizing Loops of Antibodies')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Ada Fang, Robert G. Alberstein, Simon Kelow, Frédéric A. Dreyer

**分类**: q-bio.BM, cs.LG

**发布日期**: 2025-09-10

**备注**: 21 pages, 7 figures, 10 tables, code available at https://github.com/prescient-design/igloo

---

## 💡 一句话要点

**提出Igloo抗体环区Tokenizer，提升蛋白语言模型性能并促进抗体设计**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `抗体工程` `互补决定区` `环结构预测` `蛋白质语言模型` `对比学习` `抗体设计` `多模态学习`

## 📋 核心要点

1. 现有抗体CDR结构分类方法覆盖率低，难以融入蛋白基础模型。
2. Igloo通过对比学习编码环区主链二面角和序列信息，实现高效检索。
3. Igloo提升了蛋白语言模型在抗体结合亲和力预测和环区生成方面的性能。

## 📝 摘要（中文）

抗体的互补决定区（CDR）是环状结构，对抗体与抗原的相互作用至关重要，并且对于新型生物制剂的设计具有重要意义。自20世纪80年代以来，将CDR结构的多样性分类为规范簇已经能够识别抗体的关键结构基序。然而，现有方法覆盖范围有限，并且不能容易地整合到蛋白质基础模型中。本文介绍了一种多模态抗体环Tokenizer，Igloo，它编码主链二面角和序列。Igloo使用对比学习目标进行训练，以将具有相似主链二面角的环在潜在空间中映射得更近。Igloo可以有效地从结构抗体数据库中检索最匹配的环结构，在识别相似的H3环方面优于现有方法5.9%。Igloo将token分配给所有环，解决了规范簇的覆盖范围有限的问题，同时保留了恢复规范环构象的能力。为了展示Igloo token的多功能性，我们展示了它们可以与IglooLM和IglooALM一起整合到蛋白质语言模型中。在预测重链变体的结合亲和力方面，IglooLM在10个抗体-抗原靶标中的8个上优于基础蛋白质语言模型。此外，它与现有的最先进的基于序列和多模态的蛋白质语言模型相当，与参数多7倍的模型相比，性能相当。IglooALM采样抗体环，这些抗体环在序列上是多样的，并且在结构上比最先进的抗体反向折叠模型更一致。Igloo证明了引入抗体环的多模态token对于编码抗体环的多样化景观、改进蛋白质基础模型以及用于抗体CDR设计的益处。

## 🔬 方法详解

**问题定义**：抗体互补决定区（CDR）环结构对抗体功能至关重要，但现有方法在对这些环结构进行分类和编码时存在局限性。具体来说，现有方法（如canonical clusters）覆盖范围有限，无法处理所有可能的环结构，并且难以直接整合到现代蛋白质基础模型中，阻碍了抗体设计和优化。

**核心思路**：Igloo的核心思路是将抗体环结构（包括其序列和三维结构信息）编码成token，类似于自然语言处理中的词嵌入。通过学习一个潜在空间，使得结构相似的环在潜在空间中距离更近。这种方法旨在克服现有方法覆盖范围有限的问题，并为将环结构信息融入蛋白质语言模型提供一种有效途径。

**技术框架**：Igloo是一个多模态抗体环Tokenizer，其主要流程包括：1) 数据准备：收集包含抗体环序列和结构信息的数据库；2) 特征提取：提取环的主链二面角和序列信息；3) 模型训练：使用对比学习目标训练模型，使得结构相似的环在潜在空间中距离更近；4) Token分配：将环映射到潜在空间，并根据其在潜在空间中的位置分配token。训练完成后，Igloo可以用于检索相似环结构，并生成用于蛋白质语言模型的token。

**关键创新**：Igloo的关键创新在于其多模态编码方式和对比学习训练方法。与仅依赖序列或结构信息的方法不同，Igloo同时考虑了环的序列和三维结构信息，从而能够更准确地捕捉环的结构特征。此外，对比学习方法使得Igloo能够学习到一个能够区分不同环结构的潜在空间，从而实现更有效的环结构检索和token分配。

**关键设计**：Igloo使用对比学习损失函数，旨在最小化结构相似环之间的距离，同时最大化结构不相似环之间的距离。具体的网络结构未知，但可以推测其包含编码序列和二面角的模块，并将它们融合到一个共享的潜在空间中。具体的参数设置和超参数优化细节未知。

## 📊 实验亮点

Igloo在识别相似H3环方面优于现有方法5.9%。在预测重链变体的结合亲和力方面，IglooLM在10个抗体-抗原靶标中的8个上优于基础蛋白质语言模型，并且与参数多7倍的现有最先进模型性能相当。IglooALM生成的抗体环在序列上更加多样，在结构上更加一致。

## 🎯 应用场景

Igloo在抗体工程和药物发现领域具有广泛的应用前景。它可以用于抗体人源化、亲和力成熟、新型抗体设计等任务。通过将Igloo token整合到蛋白质语言模型中，可以提高模型在抗体相关任务上的性能，例如抗体结合亲和力预测和抗体结构预测。此外，Igloo还可以用于构建抗体结构数据库，并实现高效的抗体结构检索。

## 📄 摘要（原文）

> The complementarity-determining regions of antibodies are loop structures that are key to their interactions with antigens, and of high importance to the design of novel biologics. Since the 1980s, categorizing the diversity of CDR structures into canonical clusters has enabled the identification of key structural motifs of antibodies. However, existing approaches have limited coverage and cannot be readily incorporated into protein foundation models. Here we introduce ImmunoGlobulin LOOp Tokenizer, Igloo, a multimodal antibody loop tokenizer that encodes backbone dihedral angles and sequence. Igloo is trained using a contrastive learning objective to map loops with similar backbone dihedral angles closer together in latent space. Igloo can efficiently retrieve the closest matching loop structures from a structural antibody database, outperforming existing methods on identifying similar H3 loops by 5.9\%. Igloo assigns tokens to all loops, addressing the limited coverage issue of canonical clusters, while retaining the ability to recover canonical loop conformations. To demonstrate the versatility of Igloo tokens, we show that they can be incorporated into protein language models with IglooLM and IglooALM. On predicting binding affinity of heavy chain variants, IglooLM outperforms the base protein language model on 8 out of 10 antibody-antigen targets. Additionally, it is on par with existing state-of-the-art sequence-based and multimodal protein language models, performing comparably to models with $7\times$ more parameters. IglooALM samples antibody loops which are diverse in sequence and more consistent in structure than state-of-the-art antibody inverse folding models. Igloo demonstrates the benefit of introducing multimodal tokens for antibody loops for encoding the diverse landscape of antibody loops, improving protein foundation models, and for antibody CDR design.

