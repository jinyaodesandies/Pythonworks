# -*- coding:UTF-8 -*-
import requests

if __name__ == '__main__':
    target = 'https://www.baidu.com/s?wd=%E8%BF%99%E4%BA%9B%E7%BB%86%E8%8A%82%E4%BD%93%E7%8E%B0%E9%87%91%E7%A0%96%E5%9B%BD%E5%AE%B6%E7%9A%84%E6%B7%B1%E5%8E%9A%E6%83%85%E8%B0%8A&sa=fyb_n_homepage&rsv_dl=fyb_n_homepage&from=super&cl=3&tn=baidutop10&fr=top1000&rsv_idx=2&hisfilter=1/'
    req = requests.get(url=target)
    print(req.text)
