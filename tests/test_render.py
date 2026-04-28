import tempfile
import unittest
from pathlib import Path

from scripts.render_docs import render_private, render_public


class RenderDocsTest(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        data = self.root / "data"
        data.mkdir()
        (data / "tools.json").write_text(
            """
{
  "general": [
    {
      "name": "Atoll",
      "rank": 1,
      "status": "推荐，开源",
      "github_stars": "1.7k+",
      "metadata": "Release v2.1.0",
      "links": [{"label": "GitHub", "url": "https://example.com/atoll"}],
      "summary": "通用主力",
      "features": {"音乐/媒体": "Apple Music、Spotify"}
    }
  ],
  "ai_coding": [],
  "archived": []
}
""",
            encoding="utf-8",
        )
        (data / "local-notes.json").write_text(
            """
{
  "installed_packages": [
    {"tool": "Atoll", "file": "Atoll.2.1.0.dmg", "role": "通用主力"}
  ],
  "verification": [
    {"scenario": "QQ 音乐实时识别", "official": "有媒体能力", "local": "待测"}
  ]
}
""",
            encoding="utf-8",
        )
        (data / "generated-metadata.json").write_text(
            """
{
  "updated_at": "2026-04-28T00:00:00+00:00",
  "tools": {
    "Atoll": {
      "group": "general",
      "github": {
        "stars": 1762,
        "latest_release": {
          "tag": "v9.9.9",
          "published_at": "2026-04-28T00:00:00Z",
          "url": "https://example.com/atoll/release"
        }
      }
    },
    "LookieLoo": {
      "group": "general",
      "app_store": {
        "version": "2.3.4",
        "release_date": "2026-04-27",
        "track_url": "https://example.com/lookieloo"
      }
    },
    "Alcove": {
      "group": "general",
      "homebrew": {
        "version": "1.7.2"
      }
    }
  }
}
""",
            encoding="utf-8",
        )

    def tearDown(self):
        self.tmp.cleanup()

    def test_public_document_does_not_include_private_installed_packages(self):
        output = render_public(self.root)

        self.assertIn("Atoll", output)
        self.assertNotIn("Atoll.2.1.0.dmg", output)
        self.assertNotIn("本地已有安装包", output)

    def test_private_document_includes_local_notes(self):
        output = render_private(self.root)

        self.assertIn("Atoll.2.1.0.dmg", output)
        self.assertIn("QQ 音乐实时识别", output)
        self.assertIn("本地已有安装包", output)

    def test_public_document_prefers_generated_github_release_metadata(self):
        output = render_public(self.root)

        self.assertIn("v9.9.9", output)
        self.assertNotIn("Release v2.1.0", output)

    def test_public_document_prefers_generated_store_and_homebrew_versions(self):
        tools = self.root / "data" / "tools.json"
        tools.write_text(
            """
{
  "general": [
    {
      "name": "LookieLoo",
      "rank": 1,
      "status": "可试，闭源商业",
      "metadata": "官网和 App Store 可用",
      "links": [{"label": "App Store", "url": "https://example.com/lookieloo"}],
      "summary": "音乐工具",
      "features": {"音乐/媒体": "歌词"}
    },
    {
      "name": "Alcove",
      "rank": 2,
      "status": "推荐，闭源商业",
      "metadata": "官网下载可用",
      "links": [{"label": "官网", "url": "https://example.com/alcove"}],
      "summary": "动画工具",
      "features": {"系统状态/HUD": "HUD"}
    },
    {
      "name": "MacNotch",
      "rank": 3,
      "status": "可试，闭源商业",
      "metadata": "Setapp 页面可用",
      "links": [{"label": "Setapp", "url": "https://example.com/macnotch"}],
      "summary": "Setapp 工具",
      "features": {"系统状态/HUD": "HUD"}
    }
  ],
  "ai_coding": [],
  "archived": []
}
""",
            encoding="utf-8",
        )

        output = render_public(self.root)

        self.assertIn("2.3.4", output)
        self.assertIn("1.7.2", output)

    def test_public_document_prefers_generated_setapp_version(self):
        tools = self.root / "data" / "tools.json"
        tools.write_text(
            """
{
  "general": [
    {
      "name": "MacNotch",
      "rank": 1,
      "status": "可试，闭源商业",
      "metadata": "Setapp 页面可用",
      "links": [{"label": "Setapp", "url": "https://example.com/macnotch"}],
      "summary": "Setapp 工具",
      "features": {"系统状态/HUD": "HUD"}
    }
  ],
  "ai_coding": [],
  "archived": []
}
""",
            encoding="utf-8",
        )
        (self.root / "data" / "generated-metadata.json").write_text(
            """
{
  "updated_at": "2026-04-28T00:00:00+00:00",
  "tools": {
    "MacNotch": {
      "group": "general",
      "setapp": {
        "version": "1.8.7.4"
      }
    }
  }
}
""",
            encoding="utf-8",
        )

        output = render_public(self.root)
        self.assertIn("1.8.7.4", output)


if __name__ == "__main__":
    unittest.main()
