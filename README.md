# Hello Project

一个展示 AI 辅助编码与 Git 作者身份追踪的演示项目。

## 项目结构

| 文件 | 说明 | 行数 |
|------|------|------|
| [`main.py`](main.py) | 打印多条问候语 | 4 |
| [`hello.py`](hello.py) | 打印「你好，Ricky」 | 1 |
| [`system_info.py`](system_info.py) | 收集系统信息（OS、Python、CPU、内存、磁盘、网络）| 139 |
| [`ai_code_analyzer.py`](ai_code_analyzer.py) | 分析 Git 提交历史中的 AI / 人类代码占比 | 212 |

## 快速上手

```bash
# 打印问候语
python main.py

# 打印个性化问候
python hello.py

# 查看系统信息
python system_info.py

# 分析项目中的 AI 代码占比
python ai_code_analyzer.py
```

## AI 归属分析

本项目使用 **git-ai**（[git-ai-project/git-ai](https://github.com/git-ai-project/git-ai)）追踪每条代码行的作者身份。

```bash
# 查看各提交的 AI / 人类占比
git-ai log

# 查看最近提交的详细归因
git-ai stats HEAD

# 查看 AI 使用统计（Session / Token / 模型）
git-ai usage
```

项目代码约 **98.6%** 由 AI 生成（Codex / Trae），接受率 100%。

## 许可证

MIT
