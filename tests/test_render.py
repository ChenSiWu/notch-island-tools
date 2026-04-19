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


if __name__ == "__main__":
    unittest.main()
