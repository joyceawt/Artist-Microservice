import random
from flask import Flask
import urllib.request
import json
import os
app = Flask(__name__)


@app.get('/random_artist')
def get_random_artist():
    random_id = random.randint(0, 1000)
    url = "https://api.musixmatch.com/ws/1.1/artist.get?apikey={}&artist_id={}".format(
        os.environ.get("MUSIX_MATCH_API_KEY"), random_id)
    response = urllib.request.urlopen(url)
    data = response.read()
    return json.loads(data)


# Listener
if __name__ == "__main__":
    app.run(port=4000, debug=True)
