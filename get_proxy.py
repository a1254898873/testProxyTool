import requests
import re

url = "https://www.tyhttp.com/free/page1/"

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36 Edg/86.0.622.69'
}

if __name__ == '__main__':
    res = requests.get("https://www.tyhttp.com/free/page1/", headers=headers)
    res.encoding = "utf-8"
    html_doc = res.text

    pattern = re.compile(
        ' <div class="tr ip_tr">.*?<div class="td td-4">(.*?)</div>.*?<div class="td td-2">(.*?)</div>.*?<div class="td td-2">.*?</div>.*?<div class="td td-2">.*?</div>.*?<div class="td td-2">.*?</div>.*?<div class="td td-2">.*?</div>.*?<div class="td td-4">.*?</div>.*?<div class="td td-2">.*?</div>.*?</div>',
        re.S)

    items = re.findall(pattern, html_doc)
    res = ""

    for item in items:
        str = '{a}:{b}'.format(a=item[0], b=item[1])
        res = res + str + '\n'

    with open("proxy.txt", "w") as f:
        f.write(res)
