from flask import Flask, redirect
import requests

app = Flask(__name__)

ACCESS_KEY = "1fEp5I42R5u4R-B0mjp0Ie8Ln7GavdyZW-_sNgwzyH0"

@app.route("/")
def home():
    url = f"https://api.unsplash.com/photos/random?query=landscape&orientation=landscape&client_id={ACCESS_KEY}"
    response = requests.get(url)
    if response.status_code == 200:
        image_url = response.json()["urls"]["full"]
        return redirect(image_url)
    return f"Error: {response.status_code}"

if __name__ == "__main__":
    app.run()