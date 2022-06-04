import requests

location = "omr"
current_time = 12

url = "https://speed-api.herokuapp.com/api/service"
data = {
            "location": f"{location}",
            "time": f"{current_time}"
        }

response = requests.post(url, data=data)

print(response.json())
