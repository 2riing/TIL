import imp
import requests
# 요청을 보내는 requests
from bs4 import BeautifulSoup

url = 'https://finance.naver.com/sise/'

# 문서 받아오기 
# 요청을 보내서, 문서를 한 장 받는다.(필수조건 : url)

response = requests.get(url)
doc = response.text

# 구조 파악 pasing

data = BeautifulSoup(doc, 'html.parser')
# 문서를 해석할 수 있는게 필요해? 'html.parser'
# 필요한 데이터 뽑아오기

result = data.select_one('#KOSPI_now')

# 데이터 출력
print(result.text)


# URL 요청을 보내고, 문서를 달라는 프고르매 => client (프로그램 : 브라우저, request)
# URL 요청이 오면, 문서를 한장 주는 프로그램 => server

# 요청 Request => URL
# 응답 Response => 문서 1장


