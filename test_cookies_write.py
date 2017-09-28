import cookielib
import urllib2

# 保存cookie到本地文件
filename = 'cookie.txt'
cookie = cookielib.MozillaCookieJar(filename)
handler = urllib2.HTTPCookieProcessor(cookie)
opener = urllib2.build_opener(handler)
response = opener.open("http://www.baidu.com")
cookie.save(ignore_discard=True, ignore_expires=True)
for item in cookie:
    print 'Name = ' + item.name
    print 'Value = ' + item.value
