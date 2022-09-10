import urllib.parse


def link(url: str, width: int, height: int) -> bytes:
    """
    Get capture link for screenshot of a URL and save to file.

    Args:
        url: Website URL
        width: Image width
        height: Image height
        f: File to save to

    Returns:
        bytes
    """
    return f"https://api.screenshotmachine.com?key=2108fd&url={urllib.parse.quote_plus(url)}&device=desktop&dimension={width}x{height}&format=jpg&delay=5000"
