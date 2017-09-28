import urllib
import urllib2

values = {}
values["username"] = "anthoy@gmail.com"
values["passwd"] = "123456"
#编码values字典，格式化
data = urllib.urlencode(values)
print data
#构建get访问地址
geturl = "http://www.baidu.com"+"?"+data
print geturl
request = urllib2.Request(geturl)
respose = urllib2.urlopen(request)
