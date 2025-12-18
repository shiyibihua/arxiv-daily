---
layout: default
title: Measuring Epistemic Humility in Multimodal Large Language Models
---

# Measuring Epistemic Humility in Multimodal Large Language Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.09658" class="toolbar-btn" target="_blank">📄 arXiv: 2509.09658v1</a>
  <a href="https://arxiv.org/pdf/2509.09658.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.09658v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.09658v1', 'Measuring Epistemic Humility in Multimodal Large Language Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Bingkui Tong, Jiaer Xia, Sifeng Shang, Kaiyang Zhou

**分类**: cs.CV

**发布日期**: 2025-09-11

**🔗 代码/项目**: [GITHUB](https://github.com/maifoundations/HumbleBench)

---

## 💡 一句话要点

**HumbleBench：评估多模态大语言模型认知谦逊性的新基准**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多模态大语言模型` `认知谦逊性` `幻觉检测` `基准测试` `视觉问答`

## 📋 核心要点

1. 现有MLLM评估侧重识别准确率，忽略了模型识别错误答案（认知谦逊性）的能力，这在安全攸关场景中至关重要。
2. HumbleBench通过引入“以上皆非”选项，迫使模型不仅识别正确信息，还要判断所有选项是否都错误，从而评估认知谦逊性。
3. 实验评估了多种MLLM在HumbleBench上的表现，揭示了现有模型在认知谦逊性方面的不足，并为未来研究提供了方向。

## 📝 摘要（中文）

多模态大语言模型（MLLM）中的幻觉现象——模型生成的内容与输入图像不一致——在现实应用中构成重大风险，从视觉问答中的错误信息到决策中的不安全错误。现有的基准主要测试识别准确率，即评估模型是否能在干扰项中选择正确答案。这忽略了可信AI的一个同样关键的能力：识别何时提供的选项都不正确，这种行为反映了认知谦逊性。我们提出了HumbleBench，一个新的幻觉基准，旨在评估MLLM拒绝跨三种幻觉类型（对象、关系和属性）的看似合理但错误的答案的能力。HumbleBench构建于全景场景图数据集之上，我们利用细粒度的场景图注释来提取ground-truth实体和关系，并提示GPT-4-Turbo生成多项选择题，然后进行严格的人工过滤。每个问题都包含一个“以上皆非”选项，要求模型不仅要识别正确的视觉信息，还要识别何时没有提供有效的答案。我们在HumbleBench上评估了各种最先进的MLLM——包括通用模型和专门的推理模型——并与社区分享有价值的发现和见解。通过结合显式的错误选项拒绝，HumbleBench填补了当前评估套件中的一个关键空白，为安全关键设置中MLLM的可靠性提供了更真实的衡量标准。我们的代码和数据集已公开发布，可在https://github.com/maifoundations/HumbleBench访问。

## 🔬 方法详解

**问题定义**：论文旨在解决多模态大语言模型（MLLM）在视觉问答等任务中产生幻觉的问题，即生成与输入图像不一致的内容。现有评估方法主要关注模型识别正确答案的能力，而忽略了模型识别所有选项均为错误答案的能力，这在安全攸关场景下会造成潜在风险。

**核心思路**：论文的核心思路是构建一个专门的基准测试集，该测试集包含“以上皆非”选项，迫使模型不仅要识别正确的视觉信息，还要能够判断何时所有提供的答案都是无效的。通过这种方式，可以更全面地评估MLLM的认知谦逊性，即模型在不确定情况下拒绝错误答案的能力。

**技术框架**：HumbleBench的构建流程主要包括以下几个阶段：1) 基于全景场景图数据集，提取ground-truth实体和关系；2) 利用GPT-4-Turbo生成多项选择题，每个问题包含一个“以上皆非”选项；3) 进行严格的人工过滤，确保问题的质量和难度。评估时，将MLLM应用于HumbleBench数据集，并根据模型选择“以上皆非”选项的频率和准确性来评估其认知谦逊性。

**关键创新**：HumbleBench的关键创新在于其评估MLLM认知谦逊性的方法。与现有基准测试不同，HumbleBench通过引入“以上皆非”选项，迫使模型在不确定情况下做出判断，从而更真实地反映了模型在实际应用中的可靠性。这种评估方法填补了当前评估套件中的一个关键空白。

**关键设计**：HumbleBench使用了全景场景图数据集，保证了ground-truth信息的准确性。利用GPT-4-Turbo生成问题，提高了数据集的构建效率。人工过滤过程确保了问题的质量和难度，避免了简单或模棱两可的问题。 “以上皆非”选项的设计是评估认知谦逊性的关键，需要仔细考虑其措辞和含义，以避免误导模型。

## 📊 实验亮点

HumbleBench评估了多种最先进的MLLM，结果表明现有模型在认知谦逊性方面存在明显不足。例如，即使在明确包含“以上皆非”选项的情况下，模型仍然倾向于选择错误的答案。这些实验结果突出了HumbleBench的价值，并为未来研究提供了重要的参考。

## 🎯 应用场景

HumbleBench的研究成果可应用于提升多模态大语言模型在安全关键领域的可靠性，例如自动驾驶、医疗诊断和金融风控。通过提高模型识别错误信息的能力，可以减少因幻觉导致的错误决策，从而提高系统的安全性和可信度。该基准测试也有助于推动相关算法的改进和优化。

## 📄 摘要（原文）

> Hallucinations in multimodal large language models (MLLMs) -- where the model generates content inconsistent with the input image -- pose significant risks in real-world applications, from misinformation in visual question answering to unsafe errors in decision-making. Existing benchmarks primarily test recognition accuracy, i.e., evaluating whether models can select the correct answer among distractors. This overlooks an equally critical capability for trustworthy AI: recognizing when none of the provided options are correct, a behavior reflecting epistemic humility. We present HumbleBench, a new hallucination benchmark designed to evaluate MLLMs' ability to reject plausible but incorrect answers across three hallucination types: object, relation, and attribute. Built from a panoptic scene graph dataset, we leverage fine-grained scene graph annotations to extract ground-truth entities and relations, and prompt GPT-4-Turbo to generate multiple-choice questions, followed by a rigorous manual filtering process. Each question includes a "None of the above" option, requiring models not only to recognize correct visual information but also to identify when no provided answer is valid. We evaluate a variety of state-of-the-art MLLMs -- including both general-purpose and specialized reasoning models -- on HumbleBench and share valuable findings and insights with the community. By incorporating explicit false-option rejection, HumbleBench fills a key gap in current evaluation suites, providing a more realistic measure of MLLM reliability in safety-critical settings. Our code and dataset are released publicly and can be accessed at https://github.com/maifoundations/HumbleBench.

