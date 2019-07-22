import requests
from bs4 import BeautifulSoup
from datetime import datetime

test_url = "https://movie.naver.com/movie/bi/mi/pointWriteFormList.nhn?code=136990&type=after&page=1"
resp = requests.get(test_url)
html = BeautifulSoup(resp.content, 'html.parser')
result = html.find('div', {'class':'score_total'}).find('strong').findChildren('em')[1].getText()
total_count = int(result.replace(',', ''))

def get_data(url):
    resp = requests.get(url)
    html = BeautifulSoup(resp.content, 'html.parser')
    score_result = html.find('div', {'class': 'score_result'})
    lis = score_result.findAll('li')
    created_at = datetime.strptime(li.find('dt').findAll('em')[-1].getText(), "%Y.%m.%d %H:%M")

    for li in lis:        
        nickname = li.findAll('a')[0].find('span').getText()
        created_at = datetime.strptime(li.find('dt').findAll('em')[-1].getText(), "%Y.%m.%d %H:%M")
        
        review_text = li.find('p').getText()
        score = li.find('em').getText()
        btn_likes = li.find('div', {'class': 'btn_area'}).findAll('span')
        like = btn_likes[1].getText()
        dislike = btn_likes[3].getText()
        
        watch_movie = li.find('span', {'class':'ico_viewer'})
        
        # 간단하게 프린트만 했습니다.
        print(nickname, review_text, score, like, dislike, created_at, watch_movie and True or False)

for i in range(1, int(total_count / 10) + 1):
    url = test_url + '&page=' + str(i)
    print('url: "' + url + '" is parsing....')
    get_data(url)
