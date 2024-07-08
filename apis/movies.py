import requests
import json

def advanced_search(**kwargs):
    start_year = kwargs.get('start_year')
    end_year = kwargs.get('end_year')
    min_imdb = kwargs.get('min_imdb')
    max_imdb = kwargs.get('max_imdb')
    genre = kwargs.get('genre')
    language = kwargs.get('language')
    type_film = kwargs.get('type')
    sort = kwargs.get('sort')
    
    url = "https://ott-details.p.rapidapi.com/advancedsearch"

    querystring = {"start_year":start_year,"end_year":end_year,"min_imdb":min_imdb,"max_imdb":max_imdb,"genre":genre,"language":language,"type":type_film,"sort":sort,"page":"1"}

    headers = {
        "x-rapidapi-key": "ad761c6685msh23982c33ec09642p1e22b5jsn8e6e7a7adec0",
        "x-rapidapi-host": "ott-details.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)

    data = json.loads(response.text)
    results = data['results']

    for result in results:
        print(result['title'])
        
    genres = result['genre']
    imdb_id = result['imdbid']
    image_url = result['imageurl']
    rating = result['imdbrating']
    type_movie = result['type']
    description = result['synopsis']
    title = result['title']
    release_year = result['released']
    print(results)
    
