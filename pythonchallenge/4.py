import requests

base_url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing='
# current_number = 12345
# current_number = 8022
# current_number = 559
current_number = 631


while True:
    resp = requests.get(f'{base_url}{current_number}')
    result = resp.text[-5:]
    print(result)
    current_number = result
