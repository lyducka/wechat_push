import json
import requests
import configparser
import datetime

# read config.ini
config = configparser.ConfigParser()
config.read('config.ini')

corp_id = config['Wechat']['corp_id']
corp_secret = config['Wechat']['corp_secret']
agent_id = config['Wechat']['agent_id']
get_URL = 'https://www.zhaodaka.cn'

# initial date to current date, format: 2023年01月01日
send_date = datetime.datetime.now()
send_date_formatted = send_date.strftime('%Y年%m月%d日')
send_date_plus_5 = send_date + datetime.timedelta(days=5)
send_date_plus_5_formatted = send_date_plus_5.strftime('%Y年%m月%d日')

def get_access_token(corp_id, corp_secret):
    resp = requests.get(f'https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={corp_id}&corpsecret={corp_secret}')
    js = json.loads(resp.text)
    print(js)
    if js["errcode"] == 0:
        access_token = js["access_token"]
        expires_in = js["expires_in"]
        return access_token, expires_in

def wechat_push_text(agent_id, access_token, message):
    data = {
        "touser": "Li",
        "msgtype": 'text',
        "agentid": agent_id,
        "text": {
            "content": message
        },
        "safe": 0,
        "enable_id_trans": 0,
        "enable_duplicate_check": 0,
        "duplicate_check_interval": 1800
    }
    resp = requests.post(f'https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token={access_token}', json=data)
    js = json.loads(resp.text)
    print(js)
    if js["errcode"] == 0:
        return js
    
def wechat_push_card(agent_id, access_token, message):
    data={
        "touser": "Li",
        "msgtype": "textcard",
        "agentid": agent_id,
        "textcard": message,
        "safe": 0,
        "enable_id_trans": 0,
        "enable_duplicate_check": 0,
        "duplicate_check_interval": 1800
    }
    resp = requests.post(f'https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token={access_token}', json=data)
    js = json.loads(resp.text)
    print(js)
    if js["errcode"] == 0:
        return js