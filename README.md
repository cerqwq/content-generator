# ✍️ Content Generator

AI内容生成器，支持文章、视频脚本、社交媒体内容生成。

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10+-blue?logo=python" />
  <img src="https://img.shields.io/badge/OpenAI-API-green?logo=openai" />
  <img src="https://img.shields.io/badge/License-MIT-yellow" />
</p>

## ✨ 特性

- 📝 文章生成
- 🎬 视频脚本生成
- 📱 社交媒体内容
- 📢 广告文案
- 📧 邮件模板
- 🔄 内容改写
- 🌐 内容翻译

## 🚀 快速开始

```bash
pip install openai

python generator.py
```

## 📖 使用

```python
from content_generator import create_generator

generator = create_generator()

# 生成文章
article = generator.generate_article("AI发展趋势", "专业", "1000字")

# 生成视频脚本
script = generator.generate_video_script("Python教程", "10分钟", "教育")

# 生成社交媒体
posts = generator.generate_social_media("产品发布", "微博", 5)

# 生成广告文案
ad = generator.generate_ad_copy("智能手表", "年轻人", "时尚")

# 改写内容
rewritten = generator.rewrite_content(original_text, "casual")

# 翻译
translated = generator.translate_content(text, "English")
```

## 📁 项目结构

```
content-generator/
├── generator.py   # 内容生成器核心
└── README.md
```

## 📄 许可证

MIT License
