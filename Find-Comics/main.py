import os
import requests
from bs4 import BeautifulSoup


def findComic(*targets, ):
    url = 'https://tw.manhuagui.com/'
    upd = 'update/'

    # find today's update
    r = requests.get(url + upd)
    bs = BeautifulSoup(r.text, 'html.parser')
    first_latest_list = bs.find_all('div', class_='latest-list')[0]
    result = {}
    ul = first_latest_list.find_all('a', {'class': 'cover'})

    # get name and comic local link
    # O(m) time complexity
    for t in ul:
        title = t.get('title')
        ref = t.get('href')
        result[title] = url + ref
        pass

    cmd = "open -na 'Google Chrome' --args --incognito "

    # traverse all targest
    # O(n) time complexity
    for tar in targets:
        if result.get(tar):
            cmd += "{} ".format(result.get(tar))
            print(tar)
            pass

    print('opeining.......... ')
    os.system(cmd)


if __name__ == '__main__':
    findComic('新信長公記', 'ONE PIECE航海王', '哥布林殺手', 'BEASTARS', '百鍊成神', '七龍珠超')
    pass

