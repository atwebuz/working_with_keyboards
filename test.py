# Requires "requests" to be installed (see python-requests.org)
import requests

response = requests.post(
    'https://api.remove.bg/v1.0/removebg',
    data={
        'image_url': 'https://www.remove.bg/example.jpg',
        'size': 'auto'
    },
    headers={'X-Api-Key': 'NNpTPcvAi49WoMZNfMXGF3Ds'},
)
if response.status_code == requests.codes.ok:
    with open('no-bg.png', 'wb') as out:
        out.write(response.content)
        print(response.json)
else:
    print("Error:", response.status_code, response.text)

