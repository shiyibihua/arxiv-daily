# arXiv Daily 中文要点汇总

自动抓取 arXiv 论文，使用 LLM 生成中文摘要，发布到 GitHub Pages。

## ✨ 特性

- 📥 **自动抓取** - 每日抓取指定分类的 arXiv 论文
- 🎯 **兴趣筛选** - 根据关键词过滤感兴趣的论文
- 🤖 **多 API 支持** - Gemini / OpenAI / DeepSeek，自动故障转移
- 📝 **中文摘要** - 一句话要点、核心内容、方法详解、应用场景
- 🔗 **代码链接** - 自动提取 GitHub / HuggingFace / 项目主页
- 🌐 **静态网站** - 生成 GitHub Pages 站点，按分类和日期组织
- 📊 **兴趣分组** - 页面按兴趣领域分组显示，快速定位

## 🚀 快速开始

### 1. 安装依赖

```bash
pip install -r requirements.txt
```

### 2. 配置 API Key

支持多个 API，按优先级自动选择（Gemini → OpenAI → DeepSeek）：

```bash
# 主 API：Gemini（速度快，推荐）
export GEMINI_API_KEY="你的密钥"
export GEMINI_BASE_URL="https://api.openai-proxy.org/v1"  # 如使用代理
export GEMINI_MODEL="gemini-2.0-flash"

# 备用 API：OpenAI
export OPENAI_API_KEY="你的密钥"
export OPENAI_BASE_URL="https://api.openai-proxy.org/v1"  # 如使用代理

# 备用 API：DeepSeek（中文效果好）
export DEEPSEEK_API_KEY="你的密钥"
```

> 💡 只需设置你有的 API Key，程序会自动选择可用的 API。主 API 失败时自动切换备用。

### 3. 抓取并分析论文

```bash
python main.py
```

**可选参数**：
```bash
python main.py --thumbnails          # 抓取论文预览图
python main.py --concurrency 16      # 提高并发数
python main.py --max-results 500     # 限制论文数
python main.py --no-filter           # 不使用兴趣筛选
python main.py --skip-ai             # 跳过 AI 分析
```

### 4. 生成网站

```bash
python build_page.py
```

### 5. 查看结果

打开 `docs/index.html` 或部署到 GitHub Pages。

## ⚙️ GitHub Actions 自动化

### 配置 Secrets

进入仓库 **Settings → Secrets and variables → Actions → New repository secret**：

| Secret 名称 | 说明 | 默认值 |
|------------|------|--------|
| `GEMINI_API_KEY` | Gemini API 密钥 | - （推荐设置） |
| `GEMINI_BASE_URL` | Gemini API 地址 | `https://generativelanguage.googleapis.com/v1beta/openai/` |
| `GEMINI_MODEL` | Gemini 模型名 | `gemini-2.0-flash` |
| `OPENAI_API_KEY` | OpenAI API 密钥 | - （推荐设置） |
| `OPENAI_BASE_URL` | OpenAI API 地址 | `https://api.openai.com/v1` |
| `OPENAI_MODEL` | OpenAI 模型名 | `gpt-4o-mini` |
| `DEEPSEEK_API_KEY` | DeepSeek API 密钥 | - （可选） |
| `DEEPSEEK_BASE_URL` | DeepSeek API 地址 | `https://api.deepseek.com` |
| `DEEPSEEK_MODEL` | DeepSeek 模型名 | `deepseek-chat` |

> 💡 **建议配置**：至少设置两个 API Key（如 Gemini + OpenAI），确保故障转移可用。
> 
> 💡 **使用代理**：如果使用 API 代理服务，设置对应的 `*_BASE_URL`。

<details>
<summary>📋 可选模型列表</summary>

#### Gemini 模型
| 模型名 | 说明 | 推荐场景 |
|--------|------|----------|
| `gemini-2.0-flash` | 最新快速模型 ⭐ | **默认推荐**，速度快 |
| `gemini-2.0-flash-lite` | 超轻量版 | 成本敏感场景 |
| `gemini-1.5-pro` | 高性能版 | 复杂任务 |
| `gemini-1.5-flash` | 平衡版 | 通用场景 |
| `gemini-1.5-flash-8b` | 轻量版 | 简单任务 |

#### OpenAI 模型
| 模型名 | 说明 | 推荐场景 |
|--------|------|----------|
| `gpt-4o-mini` | 性价比最高 ⭐ | **默认推荐** |
| `gpt-4o` | 最强性能 | 复杂分析 |
| `gpt-4-turbo` | 高性能 | 长文本 |
| `gpt-3.5-turbo` | 经济实惠 | 简单任务 |
| `o1-mini` | 推理增强 | 深度分析 |
| `o1-preview` | 推理增强 | 研究场景 |

#### DeepSeek 模型
| 模型名 | 说明 | 推荐场景 |
|--------|------|----------|
| `deepseek-chat` | 通用对话 ⭐ | **默认推荐**，中文好 |
| `deepseek-coder` | 代码专用 | 代码分析 |
| `deepseek-reasoner` | 推理增强 | 深度分析 |

#### Claude 模型（需配置 Anthropic 代理）
| 模型名 | 说明 | 推荐场景 |
|--------|------|----------|
| `claude-sonnet-4-20250514` | 最新平衡版 | 通用场景 |
| `claude-3-5-sonnet-20241022` | 高性价比 | 日常使用 |
| `claude-3-opus-20240229` | 最强性能 | 复杂分析 |
| `claude-3-haiku-20240307` | 快速响应 | 简单任务 |

</details>

### 配置 GitHub Pages

1. 进入 **Settings → Pages**
2. **Source**: Deploy from a branch
3. **Branch**: `main`，**Folder**: `/docs`
4. 点击 **Save**

### 触发方式

- **自动触发**：每天 UTC 19:00（北京时间凌晨 3:00）
- **手动触发**：Actions → Daily arXiv fetch & build → Run workflow

### 自定义调度时间

编辑 `.github/workflows/daily.yml`：

```yaml
schedule:
  - cron: "0 19 * * *"  # UTC 时间
```

## 📁 项目结构

```
├── main.py              # 主程序：抓取 + AI 分析
├── build_page.py        # 生成静态网站
├── tags.json            # arXiv 分类配置
├── interests.json       # 兴趣关键词配置
├── utils/
│   ├── analyser.py      # LLM API 调用（多 API + 故障转移）
│   ├── scrapy.py        # arXiv 抓取 + 兴趣筛选
│   └── prompts/         # LLM 提示词模板
├── data/                # 数据目录
│   └── YYYY-MM-DD/
│       ├── arxiv.json       # 原始论文数据
│       └── ai_summary.json  # AI 分析结果
├── docs/                # 生成的网站
│   ├── index.md
│   ├── cs-CV/
│   ├── cs-RO/
│   └── ...
└── .github/workflows/
    └── daily.yml        # GitHub Actions 配置
```

## 🔧 自定义配置

### 修改 arXiv 分类

编辑 `tags.json`：

```json
{
  "tags": ["cs.CV", "cs.RO", "cs.AI", "cs.LG"]
}
```

### 修改兴趣关键词

编辑 `interests.json`：

```json
{
  "interests": [
    {
      "name": "强化学习",
      "keywords": ["reinforcement learning", "RL", "PPO", "SAC"],
      "enabled": true
    }
  ]
}
```

### 修改 LLM 提示词

编辑 `utils/prompts/system.txt` 和 `utils/prompts/user.txt`。

## 📊 输出数据格式

### AI 分析结果 (`ai_summary.json`)

```json
{
  "headline_zh": "一句话中文要点",
  "summary_zh": "中文摘要",
  "intro_zh": ["核心要点1", "核心要点2", "核心要点3"],
  "method_zh": "方法详解",
  "application_zh": "应用场景",
  "highlight_zh": "实验亮点",
  "tags_zh": ["关键词1", "关键词2"],
  "_used_api": "gemini"  // 使用的 API
}
```

## 🔄 API 故障转移机制

程序会自动：
1. 按优先级选择可用 API（Gemini → OpenAI → DeepSeek）
2. 主 API 调用失败时，自动切换到备用 API
3. 每篇论文独立重试，最大化成功率
4. 运行结束显示各 API 使用统计

```
[INFO] 主 API: Gemini (gemini-2.0-flash)
[INFO] 备用 API: OpenAI, DeepSeek
LLM (Gemini): 100%|████████| 180/180 [03:22<00:00]

[统计] 成功: 178, 失败: 2
[统计] API 使用分布: gemini: 175, openai: 3
```

## 📝 License

GPL-3.0. See `LICENSE`.
