import string
import random

# Simulated in-memory database
url_mapping = {}

# Characters for short code (62 possible characters)
characters = string.ascii_letters + string.digits

def generate_short_code(length=6):
    return ''.join(random.choice(characters) for _ in range(length))

def shorten_url(long_url):
    short_code = generate_short_code()
    url_mapping[short_code] = long_url
    return f"http://short.url/{short_code}"

def expand_url(short_url):
    short_code = short_url.split("/")[-1]
    return url_mapping.get(short_code, "URL not found!")

# Example usage:
long_url = input("Enter the long URL: ")
short_url = shorten_url(long_url)
print("Shortened URL:", short_url)

# Test expanding
expanded_url = expand_url(short_url)
print("Expanded URL:", expanded_url)
