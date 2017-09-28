import urllib2
import cookielib

# 保存cookie到变量
cookie = cookielib.CookieJar()
handler = urllib2.HTTPCookieProcessor(cookie)
opener = urllib2.build_opener(handler)
response = opener.open('http://www.baidu.com')
for item in cookie:
    print 'Name = ' + item.name
    print 'Value = ' + item.value
