import requests
import json
# NOT DONE YET!!!!!
class Url_manager:
    def __init__(self, request, **kwargs):
        self.request = request
        self.id = kwargs.get('id', None)
        self.query = kwargs.get('query', None)
    def details(self):
        url = self.app_details.get(self.request)
        if url is None:
            return Exception('No such url in details')
        else:
            return url + str(self.id)
    def media(self):
        url = self.media.get(self.request)
        if url is None:
            return Exception('No such url in media')
        else:
            return url + str(self.id)
    def chooser(self):
        url_1 = self.app_details.get(self.request)
        url_2 = self.media.get(self.request)
        if url_1 is not None:
            return url_1 + str(self.id)
        elif url_2 is not None:
            return url_2 + str(self.id)
        elif self.request == 'search':
            return self.SEARCH_URL
        else:
            return Exception('No such url in details or media or search')
    app_details = {
        'platforms': "https://steam-api7.p.rapidapi.com/appDetails/platforms/",
        'supported_languages': "https://steam-api7.p.rapidapi.com/appDetails/supportedLanguages/",
        'detailed_description': "https://steam-api7.p.rapidapi.com/appDetails/detailedDescription/",
        'achievements': "https://steam-api7.p.rapidapi.com/appDetails/achievements/",
        'about': "https://steam-api7.p.rapidapi.com/appDetails/aboutApp/",
        'short_description': "https://steam-api7.p.rapidapi.com/appDetails/shortDescription/",
        'genres': "https://steam-api7.p.rapidapi.com/appDetails/genres/",
        'categories': "https://steam-api7.p.rapidapi.com/appDetails/categories/",
        'publishers': "https://steam-api7.p.rapidapi.com/appDetails/publishers/",
        'developers': "https://steam-api7.p.rapidapi.com/appDetails/developers/",
        'requirements': "https://steam-api7.p.rapidapi.com/appDetails/requirements/"
    }
    media = {
        'videos_url': "https://steam-api7.p.rapidapi.com/media/videos/",
        'capsule_image': "https://steam-api7.p.rapidapi.com/media/capsuleImage/",
        'screenshots': "https://steam-api7.p.rapidapi.com/media/screenshots/",
        'cover_image': "https://steam-api7.p.rapidapi.com/media/coverImage/"
    }
    
    SEARCH_URL = "https://steam-api7.p.rapidapi.com/search"
    
class Base:
    def __init__(self, request, **kwargs):
        self.manager = Url_manager(request, id == kwargs.get('id'))
        self.url = self.manager.chooser()
    def base(self, url):
        headers = {
            "x-rapidapi-key": "ad761c6685msh23982c33ec09642p1e22b5jsn8e6e7a7adec0",
            "x-rapidapi-host": "steam-api7.p.rapidapi.com"
        }

        response = requests.get(url, headers=headers)
        data = json.loads(response.text)
        return data

class Search:
    def __init__(self, query):
        self.query = query
        self.manager = Url_manager('search')
        self.url = self.manager.chooser()
    def fetch_search_results(self):
        querystring = {"query":self.query,"limit":10}

        headers = {
            "x-rapidapi-key": "ad761c6685msh23982c33ec09642p1e22b5jsn8e6e7a7adec0",
            "x-rapidapi-host": "steam-api7.p.rapidapi.com"
        }

        response = requests.get(self.url, headers=headers, params=querystring)
        data = json.loads(response.text)
        if len(data) == 0:
            return None
        else:
            results = data["results"]
            responses = []
            for result in results:
                responses.append(result["name"])
            return responses
            
class MediaQuery(Base):
    def __init__(self, request, **kwargs):
        self.manager = Url_manager(request, id = kwargs.get('id'))
        self.url = self.manager.chooser()
        self.kwargs = kwargs
        self.data = kwargs.get('data')
        self.response = requests.get(self.url)
        self.data = super().base(self.url)
    def fetch_video_url(self):
        videos = self.data['videos']
        if videos.length == 0:
            return None
        elif videos.length == 1:
            return videos['mp4']
        else:
            for video in videos:
                return video['mp4']
    def fetch_capsule_url(self):
        capsule = self.data['capsuleImage']
        return capsule
    def fetch_screenshots_url(self):
        screenshots = self.data['screenshots']
        if screenshots.length == 0:
            return None
        else:
            for screenshot in screenshots:
                return screenshot
    def fetch_cover_url(self):
        return self.response.text
        
    media = {
        'videos_url': "https://steam-api7.p.rapidapi.com/media/videos/{id}",
        'capsule_image': "https://steam-api7.p.rapidapi.com/media/capsuleImage/{id}",
        'screenshots': "https://steam-api7.p.rapidapi.com/media/screenshots/{id}",
        'cover_image': "https://steam-api7.p.rapidapi.com/media/coverImage/{id}"
    }
    

url = Url_manager('capsule_image', id = 1)
print(url.chooser())
        


media = MediaQuery('capsule_image')
print(media.fetch_capsule_url())