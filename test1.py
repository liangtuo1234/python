#!/usr/bin/env python
# -*- coding:utf-8 -*-
import urllib
import json
import sys
import socket
import urllib.request
import urllib.parse

#imp.reload(sys)
#sys.setdefaultencoding('utf8')

ddmsg="你好，我是慎"
mobile="15986845591"

# 获取钉钉消息
def extractionMessage():
    #拼接需要发送的消息
    return "##### <font color=red> @15986845591钉钉message </font>"

#发送钉钉消息
def sendDingDingMessage(url,data):
    req = urllib.request.Request(url)
    req.add_header("Content-Type", "application/json; charset=utf-8")
    opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor())
    response = opener.open(req, json.dumps(data).encode(encoding='utf-8'))# 源码是 response = opener.open(req, json.dumps(data))，由于执行会报POST data should be bytes, an iterable of bytes, or a file object. It cannot be of type str 的错误
    return response.read()

    #主函数
def main():
    posturl = "https://oapi.dingtalk.com/robot/send?access_token=b17eb64223cf39738a404acd375e88ce21d1a6d2c97e448a5f809d7761b94fe2"
    data = {"msgtype": "markdown", "markdown": {"text": extractionMessage(),"title":"Jenkins"},"at": {"atMobiles":["15986845591"],"isAtAll": "false"}}
    sendDingDingMessage(posturl, data)

main()


# -------------------------------------------------------------------------------------------------------
# 参考python2的如下代码
'''

    #!/usr/bin/python
    #coding=utf-8
    import urllib
    import urllib2
    import json
    import sys
    import socket

    reload(sys)
    sys.setdefaultencoding('utf8')

    # 获取钉钉消息
    def extractionMessage() :
        #拼接需要发送的消息
        return "##### <font color=orange> 钉钉message </font>"

    #发送钉钉消息
    def sendDingDingMessage(url, data):
        req = urllib2.Request(url)
        req.add_header("Content-Type", "application/json; charset=utf-8")
        opener = urllib2.build_opener(urllib2.HTTPCookieProcessor())
        response = opener.open(req, json.dumps(data))
        return response.read()

    #主函数
    def main():
        posturl = "https://oapi.dingtalk.com/robot/send?access_token=????????????????????????????"
        data = {"msgtype": "markdown", "markdown": {"text": extractionMessage(),"title":"Jenkins","isAtAll": "false"}}
        sendDingDingMessage(posturl, data)

    main()

'''

