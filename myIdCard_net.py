# coding=utf-8

import urllib2
import json

value = raw_input("please enter you ID card: ")

url = 'http://apis.baidu.com/apistore/idservice/id?id={}'.format(value)

req = urllib2.Request(url)
req.add_header("apikey", "331167c2bf7ced1b1328998920c293c6")

resp = urllib2.urlopen(req)
content = resp.read()
content = content.decode("utf-8")
result = json.loads(content)
result = result["retData"]

if result:
    result = result["address"]
    print 'The address is: ',result
