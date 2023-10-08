import requests
import logging

url = "https://background-removal.p.rapidapi.com/remove"

headers = {
	"content-type": "application/x-www-form-urlencoded",
	"X-RapidAPI-Key": "fab2f70f8bmsh10b9fa3f3ad6b90p1ea06cjsn8ec2c58fdced",
	"X-RapidAPI-Host": "background-removal.p.rapidapi.com"
}

async def remove_background(img_url):
    payload = f"image_url={img_url}"
    response = requests.request("POST", url, data=payload, headers=headers)
    if response.status_code == requests.codes.ok:
        logging.info(response.json()['response']['image_url'])
        return response.json()['response']['image_url']
    else:
        return response
