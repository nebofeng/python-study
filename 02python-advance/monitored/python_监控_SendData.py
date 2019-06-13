import urllib
import urllib2
test_data = {'data':'while'}
test_data_urlencode = urllib.urlencode(test_data)
requrl = "http://127.0.0.1:8000/cgi-bin/updata.py"
req = urllib2.Request(url = requrl,data =test_data_urlencode)
print req
res_data = urllib2.urlopen(req)
res = res_data.read()
print res
