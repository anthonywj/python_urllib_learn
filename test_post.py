import urllib
import urllib2

values = {}
values['username'] = "anthony@gmail.com"
values['password'] = "123456"
#编码values字典，格式化
data = urllib.urlencode(values)
print data
url = "http://passport.csdn.net/account/login?from=http://my.csdn.net/my/mycsdn"
#构建post请求
request = urllib2.Request(url, data)
print request
response = urllib2.urlopen(request)
print response.read()