import requests

url = "https://background-removal.p.rapidapi.com/remove"

payload = { "image_url": "https://objectcut.com/assets/img/raven.jpg" }
headers = {
	"content-type": "application/x-www-form-urlencoded",
	"X-RapidAPI-Key": "fab2f70f8bmsh10b9fa3f3ad6b90p1ea06cjsn8ec2c58fdced",
	"X-RapidAPI-Host": "background-removal.p.rapidapi.com"
}

response = requests.post(url, data=payload, headers=headers)
print(response.status_code)

print(response.json()['response']['image_url'])