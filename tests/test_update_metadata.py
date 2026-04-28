import unittest

from scripts.update_metadata import stable_final_url, website_version_metadata


class UpdateMetadataTest(unittest.TestCase):
    def test_website_version_metadata_extracts_configured_pattern(self):
        html = '<a href="/download/Notchpad-0.9.1.dmg">Download</a>'

        result = website_version_metadata(
            {
                "url": "https://example.com/notchpad",
                "pattern": r"Notchpad-([0-9.]+)\.dmg",
                "label": "官网版本",
            },
            fetcher=lambda url: html,
        )

        self.assertEqual(result["version"], "0.9.1")
        self.assertEqual(result["label"], "官网版本")
        self.assertEqual(result["source_url"], "https://example.com/notchpad")

    def test_stable_final_url_keeps_github_release_asset_urls_deterministic(self):
        original_url = "https://github.com/sk-ruban/notchi/releases/download/v1.0.5/Notchi-1.0.5.dmg"
        signed_url = "https://release-assets.githubusercontent.com/github-production-release-asset/1/file?sig=temporary"

        self.assertEqual(stable_final_url(original_url, signed_url), original_url)


if __name__ == "__main__":
    unittest.main()
