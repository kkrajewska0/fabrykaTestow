import requests

# r = requests.get('https://google.com')
# print(r)

parameters = {'key1':'value', 'key2':'value2'}
r = requests.get('https://google.com', params=parameters)

print(r.url)
print(r.text)
print(r.encoding)