import pytumblr
from google_images_download import google_images_download




                     


def get_client():
    CONSUMER_KEY = 'OOJii0xL1lndypB7OXNALRUOjoh9L4UB9ODnctfIMML9tnBAjj'
    CONSUMER_SECRET = 'jqUWbdwv3RZCq1hOlREXMPzU4k6jWX8WJbM2CK3jltexlv59Kj'
    OAUTH_TOKEN = 'nY8bKKlm6zRhxfF4UxiXq4dECvOklyqmaFIh1IqH6Fb7ENvO7U'
    OAUTH_TOKEN_SECRET = 'k2hoNV78KjEsDuTbeMUWKzV2rXulAU86eUt1K32cgjMfWVC4BP'

    client = pytumblr.TumblrRestClient(
        CONSUMER_KEY,
        CONSUMER_SECRET,
        OAUTH_TOKEN,
        OAUTH_TOKEN_SECRET
    )

    return client


response = google_images_download.googleimagesdownload()
arguments = {"keywords": "anorexia tumblr", "limit": 200, "print_urls": True, "chromedriver": "chromedriver"}
paths = response.download(arguments)
print(paths)





client = get_client()
