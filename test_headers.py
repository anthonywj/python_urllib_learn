import urllib
import urllib2

enable_proxy = True
#设置代理
proxy_handler = urllib2.ProxyHandler({"http": 'http://119.23.161.182:3128'})
null_proxy_handler = urllib2.ProxyHandler({})
if enable_proxy:
    opener = urllib2.build_opener(proxy_handler)
else:
    opener = urllib2.build_opener(null_proxy_handler)
urllib2.install_opener(opener)
#设置头部
url = 'http://passport.csdn.net/account/login?from=http://my.csdn.net/my/mycsdn'
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
#对付反盗链
referer = 'http://www.jianshu.com/p/q81RER'
values = {'username': 'anthony', 'password': '123456'}
headers = {'User-Agent': user_agent, 'Referer': referer}
data = urllib.urlencode(values)
request = urllib2.Request(url, data, headers)
response = urllib2.urlopen(request)
page = response.read()
print page
