import requests
import re
import json
import time
from requests.exceptions import RequestException
from multiprocessing import Pool


def get_one_page(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        return None

def pare_one_page(html):
    pattern = re.compile('<dd>.*?board-index.*?>(\d+)</i>.*?data-src="(.*?)".*?name"><a.*?>(.*?)</a>.*?star">(.*?)'
                         '</p>.*?releasetime">(.*?)</p>.*?integer">(.*?)</i>.*?fraction">(\d+)</i>.*?</dd>', re.S)

    items = re.findall(pattern, html)
    for item in items:
        yield {
            'index': item[0],
            'image': item[1],
            'title': item[2],
            'actor': item[3].strip()[3:],
            'time' : item[4].strip()[5:],
            'score': item[5] + item[6]
        }
    return items

def write_to_file(item):
    with open('result.txt', 'a', encoding='utf-8') as f:
        f.write(json.dumps(item, ensure_ascii=False) + '\n')
        f.close()

def main(offsete):
    url = 'https://maoyan.com/board/4?offset=' + str(offsete)
    html = get_one_page(url)
    # print(html)
    for item in pare_one_page(html):
        print(item)
        write_to_file(item)
if __name__ == '__main__':
    start_time = time.time()
    for i in range(10):
        main(i*10)

