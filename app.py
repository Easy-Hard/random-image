from flask import Flask, Response
import requests

app = Flask(__name__)

# Unsplash access key
ACCESS_KEY = "1fEp5I42R5u4R-B0mjp0Ie8Ln7GavdyZW-_sNgwzyH0"

@app.route('/')
def random_image():
    # Request a random landscape photo metadata from Unsplash API
    api_url = (
        f"https://api.unsplash.com/photos/random"
        f"?query=landscape&orientation=landscape&client_id={ACCESS_KEY}"
    )
    api_response = requests.get(api_url)
    if api_response.status_code != 200:
        return (f"Error fetching metadata: {api_response.status_code}", 500)

    data = api_response.json()
    image_url = data.get('urls', {}).get('full')
    if not image_url:
        return ("Error: No image URL found in API response", 500)

    # Fetch the actual image bytes
    image_response = requests.get(image_url)
    if image_response.status_code != 200:
        return (f"Error fetching image: {image_response.status_code}", 500)

    # Return image content directly
    content_type = image_response.headers.get('Content-Type', 'image/jpeg')
    return Response(image_response.content, content_type=content_type)

if __name__ == '__main__':
    # Use port 81 for Render compatibility
    app.run(host='0.0.0.0', port=81)