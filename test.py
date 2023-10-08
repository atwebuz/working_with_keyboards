import requests
from pprint import pprint as print


region='Toshkent'
url = f"https://islomapi.uz/api/present/day?region={region}"

# Making our request
response = requests.get(url)
data = response.json() 

# Your JSON objectx

try:
    # print(data['times']['asr'])
    print(data)
except ResourceWarning:
    print("Bu so'rov mavjud emas")



# https://islomapi.uz/
		