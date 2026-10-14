from urllib.parse import urlparse

def check_url(url):
    indicators = []

    parsed = urlparse(url)
    hostname = parsed.hostname or ""

    if parsed.scheme != "https":
        indicators.append("URL does not use HTTPS")

    if "@" in url:
        indicators.append("Contains an @ symbol")

    if len(url) > 100:
        indicators.append("URL is unusually long")

    if hostname and hostname.replace(".", "").isdigit():
        indicators.append("Host may be an IP address")

    suspicious_words = [
        "login", "verify", "password",
        "account", "update", "secure"
    ]

    if any(word in url.lower() for word in suspicious_words):
        indicators.append("Contains a sensitive keyword")

    print("\nURL:", url)

    if indicators:
        print("Warning: Suspicious indicators found:")
        for item in indicators:
            print("-", item)
    else:
        print("No listed indicators found.")

    print("Note: This is a basic educational checker.")
    print("It cannot confirm whether a URL is safe.")

url = input("Enter a URL to examine: ").strip()
check_url(url)
