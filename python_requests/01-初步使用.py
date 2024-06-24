import requests
# from requests_xml import XMLSession
def test_req_get():
    url = 'https://httpbin.ceshiren.com/get'
    r = requests.get(url)
    print(r.json())

def test_req_post():
    url = 'https://httpbin.ceshiren.com/post'
    r = requests.post(url)
    print(r.text)
    print()
    print(r.json())

def test_req_put():
    url = 'https://httpbin.ceshiren.com/put'
    r = requests.put(url)
    print(r.json())

def test_req_delete():
    url = 'https://httpbin.ceshiren.com/delete'
    r = requests.delete(url)
    print(r.json())