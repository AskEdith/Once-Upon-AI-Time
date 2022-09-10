import requests
import urllib.parse


def capture(url: str, width: int, height: int) -> bytes:
    """
    Capture screenshot of a URL and save to file.

    Args:
        url: Website URL
        width: Image width
        height: Image height
        f: File to save to

    Returns:
        bytes
    """
    print("RANNNN")
    response = requests.get(f"https://api.screenshotmachine.com?key=2108fd&url={urllib.parse.quote_plus(url)}&device=desktop&dimension={width}x{height}&format=jpg&cacheLimit=0&delay=3000")
    
    return response.content
