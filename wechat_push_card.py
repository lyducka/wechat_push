from wechat_push import *

access_token, expires_in = get_access_token(corp_id, corp_secret)
wechat_push_card(agent_id=agent_id, access_token=access_token, message={
            "title": "领奖通知",
            "description": f"<div class=\"gray\"> {send_date_formatted} </div> <div class=\"normal\">恭喜你抽中iPhone 7一台，领奖码：xxxx</div><div class=\"highlight\">请于{send_date_plus_5_formatted}前联系行政同事领取</div>",
            "url": get_URL,
            "btntxt": "更多"
        },)