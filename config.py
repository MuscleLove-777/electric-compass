"""電力比較コンパス - ブログ固有設定"""
import os
from pathlib import Path

BASE_DIR = Path(__file__).parent

BLOG_NAME = "電力比較コンパス"
BLOG_DESCRIPTION = "電力自由化後の新電力会社を徹底比較。エネチェンジ・楽天でんき・auでんき等の料金プラン比較、地域別お得な切替先、電気代節約術まで網羅。"
BLOG_URL = "https://musclelove-777.github.io/electric-compass/"
BLOG_LANGUAGE = "ja"
GITHUB_REPO = "MuscleLove-777/electric-compass"

TARGET_CATEGORIES = [
    "新電力会社比較",
    "地域別おすすめ電力プラン",
    "電気料金シミュレーション",
    "電気代節約テクニック",
    "オール電化・エコキュート",
    "太陽光・蓄電池",
    "切替手続き・解約",
    "電力業界ニュース",
]

THEME = {
    "primary": "#0d3b66",
    "accent": "#f4d35e",
    "gradient_start": "#0d3b66",
    "gradient_end": "#ee964b",
}

GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY", "")
GEMINI_MODEL = "gemini-2.5-flash"
GEMINI_FALLBACK_MODEL = "gemini-2.5-flash-lite"

OUTPUT_DIR = BASE_DIR / "output"
ARTICLES_DIR = OUTPUT_DIR / "articles"
SITE_DIR = OUTPUT_DIR / "site"
TOPICS_DIR = OUTPUT_DIR / "topics"

MAX_ARTICLE_LENGTH = 4000
SEO_KEYWORD_DENSITY = 0.02
