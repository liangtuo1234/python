#!/usr/bin/python
#coding=utf-8

import urllib
import json
import sys
import re
import urllib.request

headers = {'Content-Type': 'application/json'}

test_data = {
    'msgtype':"text",
    "text":{
        'content':"%s" % sys.argv[0]
    },
    "at":{
        "atMobiles":[
            "********"
        ],
        "isAtAll":False
    }
}

requrl = "https://oapi.dingtalk.com/robot/send?access_token=b17eb64223cf39738a404acd375e88ce21d1a***********"
req = urllib.request.Request(url = requrl,headers = headers,data = json.dumps(test_data).encode(encoding='utf-8'))
response = urllib.request.urlopen(req)
