import requests

image = requests.get('http://cdn.akamai.steamstatic.com/steam/apps/2035420/movie_max.mp4?t=1447364873')
print(image.text)
print(image.content)
print(image.status_code)