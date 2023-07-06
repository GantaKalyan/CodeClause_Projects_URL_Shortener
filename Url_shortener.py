import pyshorteners

def shorten_url(url):
    # Create an instance of the Shortener class
    shortener = pyshorteners.Shortener()

    try:
        # Shorten the URL
        shortened_url = shortener.tinyurl.short(url)
        return shortened_url
    except pyshorteners.exceptions.ShorteningErrorException:
        print("Error: Failed to shorten the URL.")

    return None

# Example usage
original_url = input("Enter the URL: ")

short_url = shorten_url(original_url)

if short_url:
    print(f"Original URL: {original_url}")
    print(f"Shortened URL: {short_url}")