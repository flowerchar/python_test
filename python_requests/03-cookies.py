import requests

def test_demo():
    url = 'https://httpbin.testing-studio.com/cookies'
    header = {
        'Cookie': 'lwl=school'
    }
    cookie = {
        'lwl': 'school',
        'session': '123456'
    }
    # 1. 通过header传递cookie 2. 通过cookies传递cookie
    r = requests.get(url, cookies=cookie, verify=False)
    print(r.request.headers)