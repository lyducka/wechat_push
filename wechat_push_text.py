from wechat_push import wechat_push_text, get_access_token, corp_id, corp_secret, agent_id

access_token, expires_in = get_access_token(corp_id, corp_secret)
wechat_push_text(agent_id=agent_id, access_token=access_token, message='wechat notify\ntest')