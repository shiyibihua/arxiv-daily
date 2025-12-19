---
layout: default
title: Hearing to Translate: The Effectiveness of Speech Modality Integration into LLMs
---

# Hearing to Translate: The Effectiveness of Speech Modality Integration into LLMs

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.16378" class="toolbar-btn" target="_blank">📄 arXiv: 2512.16378v1</a>
  <a href="https://arxiv.org/pdf/2512.16378.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.16378v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.16378v1', 'Hearing to Translate: The Effectiveness of Speech Modality Integration into LLMs')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Sara Papi, Javier Garcia Gilabert, Zachary Hopton, Vilém Zouhar, Carlos Escolano, Gerard I. Gállego, Jorge Iranzo-Sánchez, Ahrii Kim, Dominik Macháček, Patricia Schmidtova, Maike Züfle

**分类**: cs.CL, cs.AI, cs.SD

**发布日期**: 2025-12-18

**备注**: Project available at https://github.com/sarapapi/hearing2translate

---

## 💡 一句话要点

**首个SpeechLLM综合评测：对比端到端与级联架构语音翻译性能**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `语音翻译` `SpeechLLM` `级联系统` `端到端模型` `基准测试`

## 📋 核心要点

1. 现有端到端SpeechLLM语音翻译能力有待考量，缺乏与传统级联架构的系统性对比。
2. 提出Hearing to Translate测试套件，全面评估SpeechLLM与级联系统的语音翻译性能。
3. 实验表明级联系统总体更可靠，SpeechLLM仅在特定场景媲美，集成LLM至关重要。

## 📝 摘要（中文）

随着大型语言模型(LLMs)超越文本领域，将语音作为原生模态集成催生了SpeechLLMs，旨在直接翻译口语，从而绕过传统的基于转录的流程。然而，这种集成是否能提高语音到文本的翻译质量，优于已建立的级联架构，仍然是一个悬而未决的问题。我们提出了Hearing to Translate，这是第一个综合测试套件，严格地将5个最先进的SpeechLLMs与16个强大的直接和级联系统进行基准测试，这些系统将领先的语音基础模型(SFM)与多语言LLMs相结合。我们的分析跨越16个基准、13个语言对和9个具有挑战性的条件，包括口齿不清、嘈杂和长篇语音。通过这项广泛的评估，我们发现级联系统仍然是最可靠的，而当前的SpeechLLMs仅在选定的设置中与级联系统相匹配，并且SFM落后于两者，这突出了集成LLM（无论是在模型内部还是在pipeline中）对于高质量语音翻译至关重要。

## 🔬 方法详解

**问题定义**：论文旨在评估端到端SpeechLLM在语音翻译任务中的有效性，并将其与传统的级联系统进行比较。现有端到端SpeechLLM的性能优势尚不明确，缺乏在各种场景下的全面评估，尤其是在处理口语中的噪声、口齿不清和长篇语音等挑战性条件时。

**核心思路**：论文的核心思路是通过构建一个全面的测试套件，在多种语言对和具有挑战性的条件下，对最先进的SpeechLLM和级联系统进行严格的基准测试。通过对比不同架构的性能，揭示SpeechLLM的优势和局限性，并确定影响语音翻译质量的关键因素。

**技术框架**：论文构建了名为Hearing to Translate的测试框架，包含以下几个关键组成部分：1) 收集并整理了16个语音翻译基准数据集，涵盖13个语言对和9种具有挑战性的条件；2) 选择了5个最先进的SpeechLLM作为评估对象；3) 构建了16个强大的直接和级联系统作为对比基线，这些系统结合了领先的语音基础模型(SFM)和多语言LLM；4) 使用标准的语音翻译评估指标（如BLEU）对所有系统在各个基准上进行评估。

**关键创新**：论文的主要创新在于构建了首个全面评估SpeechLLM语音翻译能力的测试套件。该测试套件不仅涵盖了多种语言对和具有挑战性的条件，还对比了端到端SpeechLLM与传统的级联系统，为研究人员提供了一个统一的评估平台，促进了语音翻译领域的发展。此外，论文还深入分析了不同架构的优势和局限性，为未来的模型设计提供了指导。

**关键设计**：论文的关键设计包括：1) 选择了具有代表性的SpeechLLM，包括直接翻译模型和基于转录的模型；2) 构建了强大的级联系统，充分利用了现有的语音识别和机器翻译技术；3) 采用了多种评估指标，包括BLEU、TER等，以全面评估翻译质量；4) 针对不同的挑战性条件，设计了相应的评估方案，例如，通过添加噪声来模拟嘈杂环境，通过引入口齿不清的语音来评估模型的鲁棒性。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16378v1/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16378v1/x2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16378v1/figs/pearmut_screenshot_1.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

实验结果表明，在大多数情况下，级联系统在语音翻译任务中表现更可靠，尤其是在处理具有挑战性的语音条件时。当前的SpeechLLM仅在特定设置下与级联系统性能相当。语音基础模型(SFM)的性能落后于两者，表明集成LLM对于高质量语音翻译至关重要。这些发现为未来的语音翻译系统设计提供了重要的指导。

## 🎯 应用场景

该研究成果可应用于实时语音翻译、多语言会议、语音助手等领域。通过优化SpeechLLM或级联系统，可以提升跨语言交流的效率和准确性，促进全球范围内的信息共享和文化交流。未来的研究可以进一步探索如何提高SpeechLLM在噪声环境和口语化场景下的鲁棒性，并将其应用于更多实际场景。

## 📄 摘要（原文）

> As Large Language Models (LLMs) expand beyond text, integrating speech as a native modality has given rise to SpeechLLMs, which aim to translate spoken language directly, thereby bypassing traditional transcription-based pipelines. Whether this integration improves speech-to-text translation quality over established cascaded architectures, however, remains an open question. We present Hearing to Translate, the first comprehensive test suite rigorously benchmarking 5 state-of-the-art SpeechLLMs against 16 strong direct and cascade systems that couple leading speech foundation models (SFM), with multilingual LLMs. Our analysis spans 16 benchmarks, 13 language pairs, and 9 challenging conditions, including disfluent, noisy, and long-form speech. Across this extensive evaluation, we find that cascaded systems remain the most reliable overall, while current SpeechLLMs only match cascades in selected settings and SFMs lag behind both, highlighting that integrating an LLM, either within the model or in a pipeline, is essential for high-quality speech translation.

