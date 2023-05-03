# Artist-Microservice

CS 361 Random Artist Microservice

## Requesting Data

Request

```
export MUSIC_MAX_API_KEY= <insert API key here>
python random_artist.py
http://localhost:4000/random_artist
```

## Receiving Data

Navigate to `http://localhost:4000/random_artist` and you should get the response.

- Since this API has not been deployed, there is no external URL.
  To use this on flask you would do something like:

```
def get_artist()
  url = 'http://localhost:4000/random_artist' #url here to be replaced by external URL once deployed
  response = urllib.request.urlopen(url)
  data = response.read()
  return json.loads(data) # this can be modified to respond specific attributes
```

## Sample response below:

```
{
  "message": {
    "body": {
      "artist": {
        "artist_alias_list": [
          {
            "artist_alias": "\u30a8\u30c9\u30ac\u30fc\u30a6\u30a3\u30f3\u30bf\u30fc"
          },
          {
            "artist_alias": "Winter"
          },
          {
            "artist_alias": " Edgar"
          },
          {
            "artist_alias": "Edgar Holland Winter"
          }
        ],
        "artist_comment": "",
        "artist_country": "US",
        "artist_credits": {
          "artist_list": []
        },
        "artist_id": 135,
        "artist_name": "Edgar Winter",
        "artist_name_translation_list": [],
        "artist_rating": 22,
        "artist_twitter_url": "",
        "begin_date": "1946-12-28",
        "begin_date_year": "1946",
        "end_date": "0000-00-00",
        "end_date_year": "",
        "restricted": 0,
        "updated_time": "2013-11-05T11:24:50Z"
      }
    },
    "header": {
      "execute_time": 0.11635804176331,
      "status_code": 200
    }
  }
}
```
