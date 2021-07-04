"""
Classify a given URL, classify into various categories
Uses WhoisXML API for prediction.

To generate own API key, signup at
https://website-categorization.whoisxmlapi.com/api

then replace the API_KEY variable below.

07/04/2021 : 
    100 free API requests per month
"""

from typing import List, Tuple
import urllib.request
import urllib.error
import json


URL_CLASSIFIER_API_BASE: str = (
    "https://website-categorization.whoisxmlapi.com/api/v2"
)

# This value must be modified by user
# For implementing CLI, this value is exported to be ENV-VAR
URL_CLASSIFIER_API_KEY: str = None


def get_prediction_for_url(domain_to_categorize: str) -> List[Tuple]:
    """
    Classifies a given webpage to various categories
    Requests the API at
    "https://website-categorization.whoisxmlapi.com/api/v2"
    to classify the url

    URL_CLASSIFIER_API_KEY must contain API key
    URL_CLASSIFIER_API_BASE must contain the base url of API

    Args:
        domain_to_categorize (string): url of the domain to categorize
    Returns:
        (list of tuples) : list; elements are list containing
        tuple (category of webpage, prediction confidence)
    """
    # api request
    # reuturns JSON
    api_request = (
        f"{URL_CLASSIFIER_API_BASE}"
        f"?domainName={domain_to_categorize}"
        f"&apiKey={URL_CLASSIFIER_API_KEY}"
        "&outputFormat=JSON"
    )

    try:
        api_response: str = urllib.request.urlopen(api_request).read().decode("utf8")
        response_dict: dict = json.loads(api_response)

        # Final preictions in 'categories' key of api_response dict
        # 'categories' is single element list of dictionries
        preictions: dict = response_dict["categories"][0]

        # final results
        # name, confidence - name of keys from api call
        clf_results: list = [
            (ele["name"], ele["confidence"]) for ele in preictions.values()
        ]

        return clf_results

    except urllib.error.HTTPError:
        print(
            f"Check your classifier API key and/or API base "
            f"API-KEY {URL_CLASSIFIER_API_KEY} "
            f"API-BASE {URL_CLASSIFIER_API_BASE} "
        )
