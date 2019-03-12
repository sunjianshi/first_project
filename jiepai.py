import json
import requests
from log_decorator import loggerInFile
from urllib.parse import urlencode
from requests.exceptions import RequestException

@loggerInFile('./pachonglog.log')
def get_page_index(offset, keyword):
    date = {
        'aid': 24,
        'offset': offset,
        'format': 'json',
        'keyword': keyword,
        'autoload': 'true',
        'count': 20,
        'cur_tab': 1,
        'from': 'search_tab',
        'pd': 'synthesis',
    }
    url = 'https://www.toutiao.com/api/search/content/?' + urlencode(date)
    print(url)
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        print('请求出错')
        return None

@loggerInFile('./pachonglog.log')
def parse_page_html(html):
    date = json.loads(html)
    print(date)
    if date and 'data' in date.keys():
        print('1')
        for item in date.get('data'):
            yield item.get('article_url')

@loggerInFile('./pachonglog.log')
def get_parse_detail(url):
    print(url)
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        print('请求出错')
        return None

@loggerInFile('./pachonglog.log')
def main():
    html = get_page_index(0, '街拍')
    # print(html)
    for url in parse_page_html(html):
        if url:
            html = get_parse_detail(url)
            print(html)
            return

if __name__ == '__main__':
    main()