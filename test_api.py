import requests

def test_web_connection():
    # Using Google because we know it's not blocked on your network
    url = "https://www.google.com"
    
    try:
        print(f"Testing connection to: {url}")
        response = requests.get(url, timeout=5)
        
        if response.status_code == 200:
            print("\n--- Success! ---")
            print(f"Status Code: {response.status_code} (OK)")
            # Instead of .json(), we use .text to see the first 100 characters of the page
            print(f"Webpage Snippet: {response.text[:100]}...")
            print("\nYour Python environment and 'requests' library are 100% ready.")
        else:
            print(f"Connected, but server returned error code: {response.status_code}")
            
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    test_web_connection()


