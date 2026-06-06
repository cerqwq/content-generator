"""
Content Generator - AI内容生成器
支持文章、视频脚本、社交媒体内容生成
"""

import json
import os
from typing import Dict, List, Any
from datetime import datetime

try:
    from openai import OpenAI
    OPENAI_AVAILABLE = True
except ImportError:
    OPENAI_AVAILABLE = False


class ContentGenerator:
    """
    AI内容生成器
    支持：文章、脚本、社交媒体、广告文案
    """

    def __init__(self, model: str = "mimo-v2.5-pro", api_key: str = None, base_url: str = None):
        self.model = model
        if OPENAI_AVAILABLE:
            self.client = OpenAI(
                api_key=api_key or os.environ.get('OPENAI_API_KEY', ''),
                base_url=base_url or os.environ.get('OPENAI_BASE_URL', 'https://api.xiaomimimo.com/v1')
            )
        else:
            self.client = None

    def generate_article(self, topic: str, style: str = "professional", length: str = "1000字") -> str:
        """生成文章"""
        if not self.client:
            return "LLM客户端未配置"

        prompt = f"""请写一篇关于"{topic}"的文章。

要求：
- 风格：{style}
- 字数：{length}
- 结构清晰
- 包含引言、正文、结论
- 使用Markdown格式"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=3000
        )

        return response.choices[0].message.content

    def generate_video_script(self, topic: str, duration: str = "5分钟", style: str = "教育") -> str:
        """生成视频脚本"""
        if not self.client:
            return "LLM客户端未配置"

        prompt = f"""请为以下主题生成视频脚本：

主题：{topic}
时长：{duration}
风格：{style}

要求：
1. 包含开场、内容、结尾
2. 标注画面和字幕
3. 语言口语化
4. 包含互动引导"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=3000
        )

        return response.choices[0].message.content

    def generate_social_media(self, topic: str, platform: str = "微博", count: int = 5) -> List[str]:
        """生成社交媒体内容"""
        if not self.client:
            return ["LLM客户端未配置"]

        prompt = f"""请为"{topic}"生成{count}条{platform}内容：

要求：
1. 符合{platform}特点
2. 包含话题标签
3. 吸引用户互动
4. 内容多样化

请返回JSON数组格式：["内容1", "内容2", ...]"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=2000
        )

        try:
            content = response.choices[0].message.content
            import re
            json_match = re.search(r'\[.*\]', content, re.DOTALL)
            if json_match:
                return json.loads(json_match.group())
        except:
            pass

        return [response.choices[0].message.content]

    def generate_ad_copy(self, product: str, target: str, style: str = "吸引眼球") -> Dict:
        """生成广告文案"""
        if not self.client:
            return {"error": "LLM客户端未配置"}

        prompt = f"""请为以下产品生成广告文案：

产品：{product}
目标人群：{target}
风格：{style}

请返回JSON格式：
{{
    "headline": "标题",
    "subheadline": "副标题",
    "body": "正文",
    "cta": "行动号召",
    "hashtags": ["标签1", "标签2"]
}}"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=1000
        )

        try:
            content = response.choices[0].message.content
            import re
            json_match = re.search(r'\{.*\}', content, re.DOTALL)
            if json_match:
                return json.loads(json_match.group())
        except:
            pass

        return {"copy": response.choices[0].message.content}

    def generate_email_template(self, purpose: str, tone: str = "professional") -> str:
        """生成邮件模板"""
        if not self.client:
            return "LLM客户端未配置"

        prompt = f"""请生成一封{purpose}的邮件模板：

语气：{tone}

要求：
1. 专业且友好
2. 结构清晰
3. 包含占位符[xxx]
4. 可直接使用"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=1000
        )

        return response.choices[0].message.content

    def rewrite_content(self, content: str, style: str = "professional") -> str:
        """改写内容"""
        if not self.client:
            return "LLM客户端未配置"

        prompt = f"""请将以下内容改写为{style}风格：

原文：
{content}

要求：
1. 保持原意
2. 改善表达
3. 符合目标风格"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=2000
        )

        return response.choices[0].message.content

    def translate_content(self, content: str, target_lang: str = "English") -> str:
        """翻译内容"""
        if not self.client:
            return "LLM客户端未配置"

        prompt = f"""请将以下内容翻译成{target_lang}：

{content}

要求：
1. 保持原意
2. 语言自然流畅
3. 符合目标语言习惯"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=2000
        )

        return response.choices[0].message.content


def create_generator(**kwargs) -> ContentGenerator:
    """创建内容生成器"""
    return ContentGenerator(**kwargs)


if __name__ == "__main__":
    generator = create_generator()

    print("Content Generator")
    print()

    # 测试
    article = generator.generate_article("人工智能发展趋势", "专业", "500字")
    print(article[:300] + "...")
