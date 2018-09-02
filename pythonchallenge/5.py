import pickle
import requests
url = 'http://www.pythonchallenge.com/pc/def/banner.p'

payload = requests.get(url)
with open('5', 'w') as file:
    file.write(payload.text)
with open('5', 'rb') as file:
    print(pickle.load(file))