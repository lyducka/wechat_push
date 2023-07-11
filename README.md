
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

> - 获取 access_token ： https://developer.work.weixin.qq.com/document/path/91039
> - 发送应用消息 ： https://developer.work.weixin.qq.com/document/path/90236

- 文本消息参数说明

| 参数                     | 是否必须 | 说明                                                         |
| ------------------------ | -------- | ------------------------------------------------------------ |
| touser                   | 否       | 指定接收消息的成员，成员ID列表（多个接收者用‘\|’分隔，最多支持1000个）。 特殊情况：指定为"@all"，则向该企业应用的全部成员发送 |
| toparty                  | 否       | 指定接收消息的部门，部门ID列表，多个接收者用‘\|’分隔，最多支持100个。 当touser为"@all"时忽略本参数 |
| totag                    | 否       | 指定接收消息的标签，标签ID列表，多个接收者用‘\|’分隔，最多支持100个。 当touser为"@all"时忽略本参数 |
| msgtype                  | 是       | 消息类型，此时固定为：text                                   |
| agentid                  | 是       | 企业应用的id，整型。企业内部开发，可在应用的设置页面查看；第三方服务商，可通过接口 [获取企业授权信息](https://developer.work.weixin.qq.com/document/path/90236#10975/获取企业授权信息) 获取该参数值 |
| content                  | 是       | 消息内容，最长不超过2048个字节，超过将截断**（支持id转译）** |
| safe                     | 否       | 表示是否是保密消息，0表示可对外分享，1表示不能分享且内容显示水印，默认为0 |
| enable_id_trans          | 否       | 表示是否开启id转译，0表示否，1表示是，默认0。仅第三方应用需要用到，企业自建应用可以忽略。 |
| enable_duplicate_check   | 否       | 表示是否开启重复消息检查，0表示否，1表示是，默认0            |
| duplicate_check_interval | 否       | 表示是否重复消息检查的时间间隔，默认1800s，最大不超过4小时   |

> <font color=red>touser、toparty、totag</font>不能同时为空，后面不再强调。

- 2.2 用户ID：

企业微信管理员登录后可以查看用户ID，明文显示在用户列表