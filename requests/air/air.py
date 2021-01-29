# import requests
#
# url = "http://api.airvisual.com/v2/countries?key=865ae09e-5336-4d96-8f9b-fb76cffbc0b3"
#
# payload = {}
# files = {}
# headers= {}
#
# response = requests.request("GET", url, headers=headers, data = payload, files = files)
#
# print(response.text.encode('utf8'))
# #
# import requests
#
# url = "http://api.airvisual.com/v2/states?country=Kyrgyzstan&key=865ae09e-5336-4d96-8f9b-fb76cffbc0b3"
#
# payload = {}
# files = {}
# headers= {}
#
# response = requests.request("GET", url, headers=headers, data = payload, files = files)
#
# print(response.text.encode('utf8'))
#
# import requests
#
# url = "http://api.airvisual.com/v2/cities?state=Bishkek&country=Kyrgyzstan&key=865ae09e-5336-4d96-8f9b-fb76cffbc0b3"
#
# payload = {}
# files = {}
# headers= {}
#
# response = requests.request("GET", url, headers=headers, data = payload, files = files)
#
# print(response.text.encode('utf8'))

#
# import requests
#
# url = "http://api.airvisual.com/v2/city?city=Bishkek&state=Bishkek&country=Kyrgyzstan&key=865ae09e-5336-4d96-8f9b-fb76cffbc0b3"
#
# payload = {}
# headers= {}
#
# response = requests.request("GET", url, headers=headers, data = payload)
#
# print(response.text.encode('utf8'))


# import requests
#
# url = "http://api.airvisual.com/v2/stations?city=Bishkek&state=Bishkek&country=Kyrgyzstan&key=865ae09e-5336-4d96-8f9b-fb76cffbc0b3"
#
# payload = {}
# files = {}
# headers= {}
#
# response = requests.request("GET", url, headers=headers, data = payload, files = files)
#
# print(response.text.encode('utf8'))

import requests

url = "http://api.airvisual.com/v2/station?station=IES12&city=Bishkek&state=Bishkek&country=Kyrgyzstan&key=865ae09e-5336-4d96-8f9b-fb76cffbc0b3"

payload = {}
headers= {}

response = requests.request("GET", url, headers=headers, data = payload)