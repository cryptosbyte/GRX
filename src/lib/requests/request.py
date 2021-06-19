import requests, json

headers_file = open("src/lib/requests/headers.json", "r")
headers = json.load(headers_file)

def get_all_gists() -> object:

    """Returns all gists."""

    res = requests.get("https://api.github.com/gists", headers)
    res = res.json()

    return res

def get(url: str) -> str:

    """Basic GET function using request package without importing it in another file."""

    res = requests.get(url, headers)

    return res.text

def _headers() -> object:

    """Returns headers required for request. | UNUSED"""

    return headers

headers_file.close()