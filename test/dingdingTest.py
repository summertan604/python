import requests
import json


class SendMsg:
    def msg(self, send_text):
        json_text = {
            "msgtype": "text",
            "at": {
                "atMobiles": [
                    "11111"
                ],
                "isAtAll": False
            },
            "text": {
                "content": send_text
            }
        }
        token = "aa8a9fd15dcc9e71ac7585951ef49c5b4da330b73cedd96cefe1c036e7934ddd"
        headers = {'Content-Type': 'application/json;charset=utf-8'}
        api_url = "https://oapi.dingtalk.com/robot/send?access_token=%s" % token
        print(requests.post(api_url, json.dumps(json_text), headers=headers).content)


if __name__ == '__main__':
    send_text = "王胜是猪"
    SendMsg.msg(send_text)