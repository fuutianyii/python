# 习讯云每日签到和周报

## 1. 脚本介绍

本脚本用于习讯云每日签到、周报提交，使用python3环境，使用了requests和rsa第三方库，脚本设置好参数后，运行后会自动按照配置在习讯云签到并通过pushplus微信公众号推送消息到微信内，用户可以查看是否签到成功或其他内容。

文件结构：

```shell
习讯云自动签到脚本
 ├── config.json  // 配置文件
 ├── README.md  // 说明文件
 └── 习讯云每日签到.py  // 脚本
```

## 2. 注意事项

第一次签到最好手动签到因为需要设定第一次签到地点，之后的每日可以使用本脚本自动签到，使用定时任务运行该脚本即可。

`pushToken`的获取方式：关注公众号：pushplus->点击启用推送功能->回复 激活消息->点击右下角`功能`选项->个人中心->个人资料->开发设置->token

PushPlus官网: [http://www.pushplus.plus](http://www.pushplus.plus)

获取经纬度网址：[坐标，经纬度定位查询，坐标拾取](https://www.qvdv.net/tools/qvdv-coordinate.html)

## 3. config.json配置详情

```json
{
    "schoolId":"1622", // 学校ID
    "mail_provider": "fuutianyii@qq.com",//发送方邮箱账号
    "mail_provider_password": "密码",//发送方邮箱密码
    "mail_type": "qq",//邮箱类型
    "userList":[
        {
            "username":"账号",
            "password":"密码",
            "mail":"fuutianyii@qq.com",
            "lifeMode":["#","#","#","#","#","#","#"], //周一到周日的签到配置
            "pushToken":"pushplus的token",  // 看上面的获取方式
            "#": { //签到配置
                "remark":9, //看下面的表
                "address":"江苏省苏州市姑苏区三香路1055号", // 详细地址的例子
                "address_name":"苏州大学附属第二医院", // 地址名称的例子
                "city":"苏州市",
                "province":"江苏省",
                "longitude":"120.590744", // 经度 保留小数点后6位
                "latitude":"31.301617", // 纬度 保留小数点后6位
                "comment":"这是签到内容" //提交内容
            },
            "weeklyReport":5, // 周报提交日期 5为周六 6为周日，如果不需要周报提交的话 删掉 weeklyReport 参数
            "weeklyReportMessage":[ // 每一栏需要填的内容
                "有序复习中", // 实习工作具体情况及实习任务完成情况
                "有序复习中", // 主要收获及工作成绩
                "无" // 工作中的问题及需要老师的指导帮助
            ]
        },
        //.... 多个用户添加字典即可
    ]
}
```

### 3.1. remark表

| 代码  | 意义   |
| --- | ---- |
| 0   | 上班   |
| 1   | 因公外出 |
| 2   | 假期   |
| 3   | 请假   |
| 4   | 轮岗   |
| 5   | 回校   |
| 6   | 外宿   |
| 7   | 在家   |
| 8   | 下班   |
| 9   | 学习   |
| 10  | 毕业设计 |
| 11  | 院区轮转 |

### 3.2. lifeMode说明

lifeMode是一个列表，有7个元素，从左到右是从周一到周日需要签到的配置，下面是一个周一到周五上班，周六和周日在家休息的签到配置

```json
{
    "schoolId":"1622",
    "userList":[
        {
            "username":"账号",
            "password":"密码",
            "lifeMode":["#","#","#","#","#","*","*"], //周一到周日的签到配置
            "pushToken":"pushplus的token",
            "#": { //周一到周五需要的配置
                "remark":0, // 0上班
                "address":"公司地址",
                "address_name":"公司地址",
                // ....
            },
            "*": { //周六和周日需要的配置
                "remark":2, // 2假期
                "address":"家庭地址",
                "address_name":"家庭地址",
                // ....
            }
        }
    ]
}
```

### 3.3. 周报提交介绍

在 `config.json` 中的 `weeklyReport` 和 `weeklyReportMessage`中设置。

#### 3.3.1. weeklyReport

`weeklyReport` 定义了周报提交时间

注意：**如果不需要脚本帮你提交周报请必须删除本参数**，如果可以也请删除 `weeklyReportMessage` 参数

取值含义：

|取值|含义|
|-|-|
|5|周六|
|6|周日|

#### 3.3.2. weeklyReportMessage

`weeklyReportMessage` 是一个列表，规定了周报需提交的内容

```json
"weeklyReportMessage":[ // 每一栏需要填的内容
    "有序复习中", // 实习工作具体情况及实习任务完成情况
    "有序复习中", // 主要收获及工作成绩
    "无" // 工作中的问题及需要老师的指导帮助
]
```