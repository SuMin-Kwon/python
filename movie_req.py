import requests 
import json

url = 'http://kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.json?key=f5eef3421c602c6cb7ea224104795888&targetDt=20210524'
res = requests.get(url)
text = res.text
#print(text)

d = json.loads(text) 

for b in d['boxOfficeResult']['dailyBoxOfficeList']:
    print(b['rank'], b['movieNm'])