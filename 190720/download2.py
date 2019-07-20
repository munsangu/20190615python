import urllib.request

url = "https://news.naver.com/main/read.nhn?mode=LSD&mid=shm&sid1=105&oid=421&aid=0004104096"

mem = urllib.request.urlopen(url).read()
print(mem)
# print(mem.decode('utf-8'))