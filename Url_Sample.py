import urllib.request
import json

url = "https://speed-api.herokuapp.com/service/"
location = "navin"

request = url+location

response = urllib.request.urlopen(request).read()

speed = json.loads(response)

print(f"The Response from the server is : { response }.")
print(f"The Recmonded speed is : { speed }.")
