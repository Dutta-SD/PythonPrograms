import unittest

from url_classify import (
    get_prediction_for_url,
    URL_CLASSIFIER_API_BASE,
    URL_CLASSIFIER_API_KEY,
)


class TestURLClassifier(unittest.TestCase):
    """
    Test cases for url classifier
    """

    # fixtures
    example_url = "bbc.com"
    expected_api_base = "https://website-categorization.whoisxmlapi.com/api/v2"

    def test_api_key(self):
        """
        API Key test
        """
        self.assertIsNotNone(URL_CLASSIFIER_API_KEY, msg="Invalid API key")

    def test_api_base_url(self):
        """
        API base okay or not
        """
        self.assertEqual(
            self.expected_api_base, URL_CLASSIFIER_API_BASE, msg="API base unequal"
        )

    def test_prediction_format(self):
        """
        Check format of return
        'bbc.com' - returns two values.
        Needs internet connection"""

        preds = get_prediction_for_url(self.example_url)
        self.assertEqual(len(preds), 2, msg="Bad return length")
        self.assertEqual(
            type(preds[0]), tuple, msg="Expected tuple. Got something else"
        )


if __name__ == "__main__":
    unittest.main()
