import requests


def retry_request(url, total=4, status_forcelist=[429, 500, 502, 503, 504], **kwargs):
    # Make number of requests required
    for _ in range(total):
        try:
            response = requests.get(url, **kwargs)
            if response.status_code in status_forcelist:
                # Retry request
                continue
            return response
        except requests.exceptions.ConnectionError:
            pass
    return None