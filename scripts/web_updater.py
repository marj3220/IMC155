import requests

url = 'http://url.com'
query = {'field': value}
res = requests.post(url, data=query)
print(res.text)