import requests
from src.config import TOTAL_RETRY_REQUEST,FORCELIST


def retry_request(url, total=TOTAL_RETRY_REQUEST, status_forcelist=(429, 500, 502, 503, 504), **kwargs):
    # Make number of requests required
    for _ in range(0, int(total)):
        try:
            response = requests.get(url, **kwargs)
            if response.status_code in status_forcelist:
                # Retry request
                continue
            return response
        except requests.exceptions.ConnectionError:
            pass
    return None
