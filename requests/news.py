import json

import requests

a = requests.get('http://195.38.164.25:81/news/')
# print(a.text)
text = json.loads(a.text)

# print(text['news'])
text2 = json.loads(text['news'])
print(text2)