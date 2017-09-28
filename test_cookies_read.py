import cookielib
import urllib2

#读取本地cookie
cookie = cookielib.MozillaCookieJar()
cookie.load('cookie.txt', ignore_discard=True, ignore_expires=True)
req = urllib2.Request("http://www.baidu.com")
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
response = opener.open(req)
print response.read()
for item in cookie:
    print 'Name = ' + item.name
    print 'Value = ' + item.value
