#coding:utf-8
#http demo (get, post, cookie)
#http://www.cnblogs.com/TankXiao/p/3081312.html

import urllib
import urllib2
import cookielib

def get_demo():
    request = urllib2.Request('http://www.baidu.com/')
    request.add_header('content-TYPE', 'application/x-www-form-urlencoded')
    response = urllib2.urlopen(request)
    print(response.getcode())
    print(response.geturl())
    print(response.read())
    
def post_demo():
    request = urllib2.Request('http://passport.cnblogs.com/login.aspx')
    request.add_header('content-TYPE', 'application/x-www-form-urlencoded')
    data = {'tbUserName':'test_username', 'tbPassword':'test_password'}
    response = urllib2.urlopen(request, urllib.urlencode(data))
    print(response.getcode())
    print(response.geturl())
    print(response.read())
    
def cook_demo():
    cj = cookielib.CookieJar()
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
    request = urllib2.Request('https://dynamic.12306.cn/otsweb')
    request.add_header('content-TYPE', 'application/x-www-form-urlencoded')
    data = {'tbUserName':'test_username', 'tbPassword':'test_password'}
    response = urllib2.urlopen(request, urllib.urlencode(data)) #opener.open(request, urllib.urlencode(data))
    print(response.getcode())
    print(response.geturl())
    print(response.read())
    

if __name__ == '__main__':
    get_demo()
    print('\n')
    post_demo()
    print('\n')
    cook_demo()