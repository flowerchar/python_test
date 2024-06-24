import requests
import jsonpath

def test_jsonpath():
    url = 'https://httpbin.ceshiren.com/post'
    req_body = {"teacher": [{"name": "lwl", "age": 18}, {"name": "lwl2", "age": 19}]}
    r = requests.post(url, json=req_body)
    res = jsonpath.jsonpath(r.json(), '$..Content-Type')
    print(res)