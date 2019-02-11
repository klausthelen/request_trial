import requests
import json

print("-------Requests-------")

google = requests.get("http://google.com")

print("-------Google Response-------")
print(google)

outfile = open("googlehtml.html", "w")
outfile.write(str(google.text.encode('utf-8')))

httpbinurl = "http://httpbin.org"

print("Post HttpBin")
httpbinpost = requests.post(httpbinurl + "/post")
print(httpbinpost)

print("Put HttpBin")
httpbinput = requests.put(httpbinurl + "/put")
print(httpbinput)

print("Delete HttpBin")
httpbindelete = requests.delete(httpbinurl + "/delete")
print(httpbindelete)

print("Head HttpBin")
httpbinhead = requests.head(httpbinurl + "/get")
print(httpbinhead)

print("Options HttpBin")
httpbinoptions = requests.options(httpbinurl + "/get")
print(httpbinoptions)

print("Get HttpBin URL")
payloadget = {'key1': 'value1', 'key2': 'value2'}
httpbinget = requests.get(httpbinurl + "/get", params=payloadget)
print(httpbinget.url)
print("Get HttpBin Response")
print(json.dumps(httpbinget.json(), indent=4))
print(httpbinget.content)