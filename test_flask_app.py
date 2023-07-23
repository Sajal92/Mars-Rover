import requests
res = requests.post('http://localhost:5005', json={"mytext":"lalala"})
if res.ok:
    print(res.json())

## run in debug mode docker run -it image_name

## can send files, json, str from postman as post request