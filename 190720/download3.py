import urllib.request
import urllib.parse

# https://search.naver.com/search.naver?sm=top_hty&fbm=1&ie=utf8&query=%EC%B4%88%EC%BD%9C%EB%A6%BF
api = 'https://search.naver.com/search.naver'
values={
    'where':'news',
    'sm':'tab_jum',
    'ie':'utf8',
    'query':'장마'
}

params=urllib.parse.urlencode(values)
url=api + '?' + params
data=urllib.request.urlopen(url).read()
text=data.decode('utf-8')
print(text)