#!/usr/bin/env python
#coding=utf8
'''
    @author: 段家公子
    @date: 2015-7-16
    @desc: python2.7.8; realtime monitor 12306 train tickets
'''

import urllib2
import cookielib 


def get_page(url):
    cj = cookielib.CookieJar()
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
    urllib2.install_opener(opener)
    headers = {
            'User_Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.134 Safari/537.36',
            'referer': 'http://www.12306.cn/',
            'connection': 'keep-alive',
            'Host': 'kyfw.12306.cn',
            'Referer': 'https://kyfw.12306.cn/otn/leftTicket/init'
            }
    req = urllib2.Request(url, headers = headers)
    html = urllib2.urlopen(req).read()
    
    f = open('./index.html', 'w')
    f.write(html)

    print len(html)
    return html


def get_url():
    print 'choose your dept_id and dest_id code: BJP(北京);SHH(上海);WXH(无锡);DLT(大连);'
    dept_id = raw_input('input your dept_id:\t')
    dest_id = raw_input('\ninput your dest_id:\t')
    dept_date = raw_input('\ninput your dept_date 格式2016-02-01:\t')
    pur_code = raw_input('\ninput your purpose code: ADULT or 0X00  (student)\t') 
    url = 'https://kyfw.12306.cn/otn/leftTicket/query?leftTicketDTO.train_date='+dept_date+'&leftTicketDTO.from_station='+dept_id+'&leftTicketDTO.to_station='+dest_id+'&purpose_codes='+pur_code
    print url
    return url


if __name__ == '__main__':
    url = get_url()
    html = get_page(url)
