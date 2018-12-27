import requests
from bs4 import BeautifulSoup

if __name__ == '__main__':
    id = 74454
    url = 'http://www.biqukan.net/book/%d/' % id
    headers = {'User-Agent':'Mozilla/5.0 (Linux; Android 4.1.1; Nexus 7 Build/JRO03D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166  Safari/535.19'}
    r = requests.get(url=url, headers=headers)
    r.encoding = 'gbk'
    chapters = BeautifulSoup(r.text).find_all('div', id='list-chapterAll', class_='panel-default')
    download_soup = BeautifulSoup(str(chapters))
    for child in download_soup.dl.children:
        if child != '\n':
            if child.a != None:
                print(child.a.string)
