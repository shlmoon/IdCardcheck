# coding=utf-8

import urllib2

url = 'http://apis.baidu.com/apistore/idservice/id?id=421127199105141930'

req = urllib2.Request(url)
req.add_header("apikey", "331167c2bf7ced1b1328998920c293c6")

resp = urllib2.urlopen(req)
content = resp.read()

content = content.decode("utf-8")

print isinstance(content, unicode)

result = eval(content)

result = result["retData"]

if result:
    result = result["address"]
    print isinstance(result, unicode)
    result = result.decode("unicode_escape")
    print result
