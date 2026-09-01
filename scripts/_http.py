"""Shared HTTP session with retry-on-connection-reset for the Apify
scripts (reddit_scan.py, ig_outliers.py, tiktok_outliers.py).

Found in production: a mid-poll connection reset (proxy tunnel drop,
not an Apify error) previously caused the whole run to be reported as
failed even though the Apify run itself kept going and often
succeeded anyway. Retrying the request on a fresh connection is the
right fix, not aborting a run that's probably fine.
"""
import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

RETRY_TOTAL = 4
BACKOFF_FACTOR = 2  # 2s, 4s, 8s, 16s between retries


def make_session():
    session = requests.Session()
    retry = Retry(
        total=RETRY_TOTAL,
        backoff_factor=BACKOFF_FACTOR,
        status_forcelist=(429, 500, 502, 503, 504),
        allowed_methods=("GET", "POST"),
        raise_on_status=False,
    )
    adapter = HTTPAdapter(max_retries=retry)
    session.mount("https://", adapter)
    session.mount("http://", adapter)
    return session
