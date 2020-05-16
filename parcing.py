import requests
from bs4 import BeautifulSoup
import csv

url = 'http://www.kobis.or.kr/kobis/business/mast/thea/findTheaterInfoList.do'
r = requests.post(url)

soup = BeautifulSoup(r.text,'html.parser')
table = soup.find('table')
rows = table.find('tbody').find_all('tr')

initial_index = 0   # 로우 파싱을 위해 인덱스 선언

result = list() # 리스트 형식으로 데이터 타입만 선언

for i in range(len(rows)):  # 한 로우 마다
    col=rows[initial_index].find_all('td')  # 인덱스의 로우스에서 모든 단어 찾기
    for item in col:    # 한 칼럼 마다
        result.append(item.get_text())  # 리절트 배열에다가 텍스트 담기
    initial_index += 1     # 인덱스 1 증가로 로우 바꾸기

print(result)   # 리절트 배열 출력

'''
col=rows[0] ~ 부터 for item in col 이거 나오는 끝까지 
어떤 사이트에 표의 첫번째 행을 가져오는 코드인데 이거를 첫번째 행이아니라 
10번째 행까지 가져오는 코드로 어떻게 만들죠?
'''