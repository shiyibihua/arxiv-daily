---
layout: default
title: "GenZ: Foundational models as latent variable generators within traditional statistical models"
---

# GenZ: Foundational models as latent variable generators within traditional statistical models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.24834" class="toolbar-btn" target="_blank">📄 arXiv: 2512.24834v1</a>
  <a href="https://arxiv.org/pdf/2512.24834.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.24834v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.24834v1', 'GenZ: Foundational models as latent variable generators within traditional statistical models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Marko Jojic, Nebojsa Jojic

**分类**: cs.AI

**发布日期**: 2025-12-31

---

## 💡 一句话要点

**GenZ：融合统计模型与大模型的隐变量生成框架，提升预测精度。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `隐变量模型` `基础模型` `统计建模` `语义特征` `房价预测` `协同过滤` `冷启动` `EM算法`

## 📋 核心要点

1. 现有大型语言模型在特定数据集预测任务中，无法有效捕捉数据集特有的模式。
2. GenZ通过迭代对比统计建模误差识别的项目组，发现可解释的语义特征，并用其指导预测。
3. 实验表明，GenZ在房价预测和电影推荐任务上显著优于现有方法，并能发现数据集特有模式。

## 📝 摘要（中文）

本文提出GenZ，一种混合模型，通过可解释的语义特征桥接基础模型和统计建模。大型语言模型虽然拥有广泛的领域知识，但通常无法捕捉对预测任务至关重要的数据集特定模式。我们的方法通过迭代过程发现语义特征描述来解决这个问题，该过程对比通过统计建模误差识别的项目组，而不是仅仅依赖于基础模型的领域理解。我们将其公式化为广义EM算法，该算法联合优化语义特征描述符和统计模型参数。该方法提示一个冻结的基础模型根据发现的特征对项目进行分类，将这些判断视为潜在二元特征的噪声观测，这些特征通过学习的统计关系预测实值目标。我们在两个领域展示了该方法：房价预测（享乐回归）和电影推荐的冷启动协同过滤。在房价方面，我们的模型使用从多模态列表数据中发现的语义特征实现了12%的中位数相对误差，大大优于依赖于LLM一般领域知识的GPT-5基线（38%误差）。对于Netflix电影嵌入，我们的模型仅从语义描述预测协同过滤表示，余弦相似度为0.59——匹配了通过传统协同过滤需要大约4000个用户评分才能达到的性能。发现的特征揭示了数据集特定的模式（例如，预测当地房地产市场的建筑细节，预测用户偏好的特许经营会员资格），这些模式与模型单独的领域知识不同。

## 🔬 方法详解

**问题定义**：论文旨在解决大型语言模型（LLM）在特定数据集上进行预测时，无法有效利用数据集自身蕴含的特定模式的问题。现有方法过度依赖LLM的通用领域知识，忽略了数据集内部的细粒度信息，导致预测精度下降。例如，在房价预测中，LLM可能知道房屋的一般特征，但难以捕捉特定区域的建筑风格对房价的影响。

**核心思路**：GenZ的核心思路是将LLM作为一种隐变量生成器，通过统计建模误差来引导LLM发现数据集特有的语义特征。这些特征作为隐变量，连接LLM的领域知识和统计模型的预测能力，从而实现更精确的预测。这种方法避免了直接依赖LLM的通用知识，而是让LLM专注于提取数据集相关的特征。

**技术框架**：GenZ的整体框架是一个广义EM算法。首先，使用统计模型进行初步预测，并识别预测误差较大的样本组。然后，利用这些样本组的差异，提示LLM生成语义特征描述。接着，将这些特征描述作为隐变量，通过学习统计关系来预测目标值。最后，迭代优化语义特征描述和统计模型参数，直至收敛。主要模块包括：统计建模模块、语义特征发现模块（基于LLM）和联合优化模块。

**关键创新**：GenZ的关键创新在于将LLM与传统的统计建模方法相结合，并利用统计建模误差来引导LLM发现数据集特有的语义特征。与现有方法相比，GenZ不是直接使用LLM进行预测，而是将LLM作为一种特征提取器，提取出的特征再用于统计建模。这种方法能够更好地利用数据集自身的信息，提高预测精度。

**关键设计**：GenZ的关键设计包括：1) 使用广义EM算法进行联合优化，确保语义特征和统计模型参数能够协同优化。2) 设计合适的prompt，引导LLM生成有意义的语义特征描述。3) 将LLM的输出视为隐变量的噪声观测，并通过学习统计关系来降低噪声的影响。4) 使用冻结的LLM，避免了微调LLM带来的计算成本和过拟合风险。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.24834v1/1_bathroom.jpg" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.24834v1/x1.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.24834v1/x2.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

GenZ在房价预测任务上，使用发现的语义特征实现了12%的中位数相对误差，显著优于GPT-5基线（38%误差）。在Netflix电影嵌入任务上，GenZ仅从语义描述预测协同过滤表示，余弦相似度达到0.59，与需要约4000个用户评分的传统协同过滤方法性能相当。这些结果表明，GenZ能够有效利用数据集特有的模式，提高预测精度。

## 🎯 应用场景

GenZ具有广泛的应用前景，可应用于各种需要利用领域知识和数据集特定模式的预测任务。例如，在金融领域，可以用于预测股票价格或信用风险；在医疗领域，可以用于诊断疾病或预测患者预后；在推荐系统领域，可以用于冷启动推荐或个性化推荐。GenZ的实际价值在于提高预测精度，并发现数据集中的隐藏模式，为决策提供更可靠的依据。

## 📄 摘要（原文）

> We present GenZ, a hybrid model that bridges foundational models and statistical modeling through interpretable semantic features. While large language models possess broad domain knowledge, they often fail to capture dataset-specific patterns critical for prediction tasks. Our approach addresses this by discovering semantic feature descriptions through an iterative process that contrasts groups of items identified via statistical modeling errors, rather than relying solely on the foundational model's domain understanding. We formulate this as a generalized EM algorithm that jointly optimizes semantic feature descriptors and statistical model parameters. The method prompts a frozen foundational model to classify items based on discovered features, treating these judgments as noisy observations of latent binary features that predict real-valued targets through learned statistical relationships. We demonstrate the approach on two domains: house price prediction (hedonic regression) and cold-start collaborative filtering for movie recommendations. On house prices, our model achieves 12\% median relative error using discovered semantic features from multimodal listing data, substantially outperforming a GPT-5 baseline (38\% error) that relies on the LLM's general domain knowledge. For Netflix movie embeddings, our model predicts collaborative filtering representations with 0.59 cosine similarity purely from semantic descriptions -- matching the performance that would require approximately 4000 user ratings through traditional collaborative filtering. The discovered features reveal dataset-specific patterns (e.g., architectural details predicting local housing markets, franchise membership predicting user preferences) that diverge from the model's domain knowledge alone.

