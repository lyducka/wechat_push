
**企业微信推送 python版**：

- 参考该库内容和教程。https://github.com/shenbo/qiye-wechat-push

### 1. 企业微信注册

- 1.1 注册企业

用电脑打开企业微信官网，https://work.weixin.qq.com/， 注册一个企业

- 1.2 获取企业ID

`我的企业` --> 最下边可以看到企业ID: `corpid`

- 1.3 获取应用ID

`管理企业` --> `应用管理` --> `创建应用` 

创建完成后可得到应用ID `agentid` 

- 1.4 获取Secret

还在应用页面， 获取 Secret， 需要在企业微信客户端里接收。

这样就得到了 `secret` 

### 2. 发送文本消息 python

<!-- more -->

- 2.1 官方API：

用到了两个API

> - 获取 access_token ： https://work.weixin.qq.com/api/doc/90000/90135/91039
> - 发送应用消息 ： https://work.weixin.qq.com/api/doc/90000/90135/90236

- 2.2 用户ID：

企业微信管理员登录后可以查看用户ID，明文显示在用户列表