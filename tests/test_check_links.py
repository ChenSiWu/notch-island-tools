import unittest

from scripts.check_links import is_link_failure


class CheckLinksTest(unittest.TestCase):
    def test_allowed_http_status_does_not_fail_link_check(self):
        status = {"status": 451, "allowed_statuses": [451], "final_url": "https://example.com"}

        self.assertFalse(is_link_failure(status))

    def test_unallowed_http_status_fails_link_check(self):
        status = {"status": 451, "allowed_statuses": [403], "final_url": "https://example.com"}

        self.assertTrue(is_link_failure(status))


if __name__ == "__main__":
    unittest.main()
