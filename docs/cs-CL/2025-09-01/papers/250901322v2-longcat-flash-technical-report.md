---
layout: default
title: LongCat-Flash Technical Report
---

# LongCat-Flash Technical Report

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.01322" class="toolbar-btn" target="_blank">📄 arXiv: 2509.01322v2</a>
  <a href="https://arxiv.org/pdf/2509.01322.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.01322v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.01322v2', 'LongCat-Flash Technical Report')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Meituan LongCat Team, Bayan, Bei Li, Bingye Lei, Bo Wang, Bolin Rong, Chao Wang, Chao Zhang, Chen Gao, Chen Zhang, Cheng Sun, Chengcheng Han, Chenguang Xi, Chi Zhang, Chong Peng, Chuan Qin, Chuyu Zhang, Cong Chen, Congkui Wang, Dan Ma, Daoru Pan, Defei Bu, Dengchang Zhao, Deyang Kong, Dishan Liu, Feiye Huo, Fengcun Li, Fubao Zhang, Gan Dong, Gang Liu, Gang Xu, Ge Li, Guoqiang Tan, Guoyuan Lin, Haihang Jing, Haomin Fu, Haonan Yan, Haoxing Wen, Haozhe Zhao, Hong Liu, Hongmei Shi, Hongyan Hao, Hongyin Tang, Huantian Lv, Hui Su, Jiacheng Li, Jiahao Liu, Jiahuan Li, Jiajun Yang, Jiaming Wang, Jian Yang, Jianchao Tan, Jiaqi Sun, Jiaqi Zhang, Jiawei Fu, Jiawei Yang, Jiaxi Hu, Jiayu Qin, Jingang Wang, Jiyuan He, Jun Kuang, Junhui Mei, Kai Liang, Ke He, Kefeng Zhang, Keheng Wang, Keqing He, Liang Gao, Liang Shi, Lianhui Ma, Lin Qiu, Lingbin Kong, Lingtong Si, Linkun Lyu, Linsen Guo, Liqi Yang, Lizhi Yan, Mai Xia, Man Gao, Manyuan Zhang, Meng Zhou, Mengxia Shen, Mingxiang Tuo, Mingyang Zhu, Peiguang Li, Peng Pei, Peng Zhao, Pengcheng Jia, Pingwei Sun, Qi Gu, Qianyun Li, Qingyuan Li, Qiong Huang, Qiyuan Duan, Ran Meng, Rongxiang Weng, Ruichen Shao, Rumei Li, Shizhe Wu, Shuai Liang, Shuo Wang, Suogui Dang, Tao Fang, Tao Li, Tefeng Chen, Tianhao Bai, Tianhao Zhou, Tingwen Xie, Wei He, Wei Huang, Wei Liu, Wei Shi, Wei Wang, Wei Wu, Weikang Zhao, Wen Zan, Wenjie Shi, Xi Nan, Xi Su, Xiang Li, Xiang Mei, Xiangyang Ji, Xiangyu Xi, Xiangzhou Huang, Xianpeng Li, Xiao Fu, Xiao Liu, Xiao Wei, Xiaodong Cai, Xiaolong Chen, Xiaoqing Liu, Xiaotong Li, Xiaowei Shi, Xiaoyu Li, Xili Wang, Xin Chen, Xing Hu, Xingyu Miao, Xinyan He, Xuemiao Zhang, Xueyuan Hao, Xuezhi Cao, Xunliang Cai, Xurui Yang, Yan Feng, Yang Bai, Yang Chen, Yang Yang, Yaqi Huo, Yerui Sun, Yifan Lu, Yifan Zhang, Yipeng Zang, Yitao Zhai, Yiyang Li, Yongjing Yin, Yongkang Lv, Yongwei Zhou, Yu Yang, Yuchen Xie, Yueqing Sun, Yuewen Zheng, Yuhuai Wei, Yulei Qian, Yunfan Liang, Yunfang Tai, Yunke Zhao, Zeyang Yu, Zhao Zhang, Zhaohua Yang, Zhenchao Zhang, Zhikang Xia, Zhiye Zou, Zhizhao Zeng, Zhongda Su, Zhuofan Chen, Zijian Zhang, Ziwen Wang, Zixu Jiang, Zizhe Zhao, Zongyu Wang, Zunhai Su

**分类**: cs.CL, cs.AI, cs.DC, cs.LG

**发布日期**: 2025-09-01 (更新: 2025-09-19)

**🔗 代码/项目**: [HUGGINGFACE](https://huggingface.co/meituan-longcat)

---

## 💡 一句话要点

**LongCat-Flash：一个具有高效计算和高级Agent能力的5600亿参数MoE语言模型**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `混合专家模型` `MoE` `语言模型` `Agent能力` `计算效率` `零计算专家` `捷径连接` `大模型训练`

## 📋 核心要点

1. 现有大模型在计算效率和Agent能力上存在瓶颈，难以兼顾资源消耗和智能水平。
2. LongCat-Flash通过零计算专家和捷径连接MoE，实现动态计算预算分配和计算通信重叠，提升效率。
3. 实验表明，LongCat-Flash在Agent任务中表现出色，并以较低成本实现了高吞吐量的推理。

## 📝 摘要（中文）

本文介绍了LongCat-Flash，一个拥有5600亿参数的混合专家(MoE)语言模型，旨在实现计算效率和高级Agent能力。为了满足可扩展效率的需求，LongCat-Flash采用了两种新颖的设计：(a)零计算专家，它能够动态分配计算预算，并根据上下文需求激活186亿到313亿（平均270亿）参数，从而优化资源使用。(b)捷径连接的MoE，它扩大了计算-通信重叠窗口，与同等规模的模型相比，在推理效率和吞吐量方面表现出显著的提升。我们为大型模型开发了一个全面的缩放框架，该框架结合了超参数迁移、模型增长初始化、多管齐下的稳定性套件和确定性计算，以实现稳定和可重复的训练。值得注意的是，通过可扩展的架构设计和基础设施努力之间的协同作用，我们在30天内完成了超过20万亿token的模型训练，同时以每百万输出token 0.70美元的成本实现了每秒超过100个token (TPS)的推理速度。为了将LongCat-Flash培养成具有Agent智能的模型，我们对优化的混合数据进行了大规模预训练，然后对推理、代码和指令进行了有针对性的中期和后期训练，并进一步利用了合成数据和工具使用任务进行增强。全面的评估表明，作为一个非思考的基础模型，LongCat-Flash在其他领先模型中提供了极具竞争力的性能，并在Agent任务中具有卓越的优势。LongCat-Flash的模型检查点已开源，以促进社区研究。

## 🔬 方法详解

**问题定义**：现有的大型语言模型在计算效率和Agent能力之间存在权衡。传统的稠密模型计算量大，而稀疏模型（如MoE）虽然可以提高效率，但通信开销可能成为瓶颈。此外，如何有效地训练和扩展MoE模型，并使其具备更强的Agent能力，也是一个挑战。

**核心思路**：LongCat-Flash的核心思路是通过创新的MoE架构设计，在保证模型容量的同时，最大限度地提高计算效率和通信效率。具体来说，通过“零计算专家”实现动态的计算预算分配，只激活必要的专家，减少不必要的计算。“捷径连接MoE”则通过扩大计算-通信重叠窗口，降低通信开销，提高整体吞吐量。

**技术框架**：LongCat-Flash的整体框架基于MoE架构，包含以下主要模块：(1)输入层：接收输入文本。(2)MoE层：包含多个专家网络，每个专家网络处理不同类型的输入。(3)路由网络：根据输入文本的特征，动态地选择激活哪些专家网络。(4)输出层：生成最终的输出文本。此外，LongCat-Flash还采用了大规模预训练、中期训练和后期训练等多个阶段，以提升模型的性能和Agent能力。

**关键创新**：LongCat-Flash的关键创新在于以下两点：(1)零计算专家：允许模型根据输入动态地调整计算量，只激活必要的专家，从而节省计算资源。(2)捷径连接MoE：通过捷径连接，扩大计算-通信重叠窗口，降低通信开销，提高整体吞吐量。这与传统的MoE模型中专家之间的通信方式不同，传统MoE模型通常需要等待所有专家的计算完成后才能进行通信。

**关键设计**：在模型设计方面，LongCat-Flash采用了以下关键设计：(1)模型规模：5600亿参数。(2)激活专家数量：平均每个token激活270亿参数。(3)训练数据：超过20万亿token。(4)训练时间：30天。(5)推理成本：每百万输出token 0.70美元。(6)训练策略：结合超参数迁移、模型增长初始化、稳定性套件和确定性计算。

## 📊 实验亮点

LongCat-Flash在超过20万亿token的数据上进行了训练，并在30天内完成了训练。在推理方面，该模型实现了每秒超过100个token的吞吐量，并且每百万输出token的成本仅为0.70美元。此外，LongCat-Flash在Agent任务中表现出卓越的性能，与其他领先模型相比具有竞争力。

## 🎯 应用场景

LongCat-Flash具有广泛的应用前景，包括智能助手、代码生成、文本摘要、机器翻译等。其高效的计算能力和强大的Agent能力使其能够胜任复杂的任务，例如自动化报告生成、智能客服、以及各种需要推理和决策的场景。该模型开源，将促进社区研究，并推动AI技术在各行业的应用。

## 📄 摘要（原文）

> We introduce LongCat-Flash, a 560-billion-parameter Mixture-of-Experts (MoE) language model designed for both computational efficiency and advanced agentic capabilities. Stemming from the need for scalable efficiency, LongCat-Flash adopts two novel designs: (a) Zero-computation Experts, which enables dynamic computational budget allocation and activates 18.6B-31.3B (27B on average) per token depending on contextual demands, optimizing resource usage. (b) Shortcut-connected MoE, which enlarges the computation-communication overlap window, demonstrating notable gains in inference efficiency and throughput compared to models of a comparable scale. We develop a comprehensive scaling framework for large models that combines hyperparameter transfer, model-growth initialization, a multi-pronged stability suite, and deterministic computation to achieve stable and reproducible training. Notably, leveraging the synergy among scalable architectural design and infrastructure efforts, we complete model training on more than 20 trillion tokens within 30 days, while achieving over 100 tokens per second (TPS) for inference at a cost of \$0.70 per million output tokens. To cultivate LongCat-Flash towards agentic intelligence, we conduct a large-scale pre-training on optimized mixtures, followed by targeted mid- and post-training on reasoning, code, and instructions, with further augmentation from synthetic data and tool use tasks. Comprehensive evaluations demonstrate that, as a non-thinking foundation model, LongCat-Flash delivers highly competitive performance among other leading models, with exceptional strengths in agentic tasks. The model checkpoint of LongCat-Flash is open-sourced to foster community research.
>   LongCat Chat: https://longcat.ai
>   Hugging Face: https://huggingface.co/meituan-longcat
>   GitHub: https://github.com/meituan-longcat

