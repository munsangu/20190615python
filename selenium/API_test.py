import os, sys, urllib.request

# naver개발자 센터에서 발급받은 client_id,client_secret
client_id = "o92_FDZJFJ9JZw5O1jEo"
client_secret = "h0tSuRPcol"

encText = urllib.parse.quote("제주도")
url = "https://openapi.naver.com/v1/search/blog?query=" + encText # json 결과
# url = "https://openapi.naver.com/v1/search/blog.xml?query=" + encText # xml 결과

request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)
response = urllib.request.urlopen(request)
rescode = response.getcode()
if(rescode==200):
    response_body = response.read()
    print(response_body.decode('utf-8'))
else:
    print("Error Code:" + rescode)
