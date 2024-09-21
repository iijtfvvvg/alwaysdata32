import time
import requests

# 定义登录信息
login_url = "https://admin.alwaysdata.com/login/"
user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 Edg/119.0.0.0"

# 定义多个用户的登录信息
users = {
    "user1": {
        "username": "ybinmopop@gmail.com",
        "password": "tttgfgS47/780"
    },
    "user2": {
        "username": "hjinmioui@gmail.com",
        "password": "ttgfsS7/80@"
    },
    "user3": {
        "username": "bujnioio@gmail.com",
        "password": "tgvgdF47/850/Y"
    },
    "user4": {
        "username": "hyuhjbnny@gmail.com",
        "password": "uuuT/780/@"
    },
    "user5": {
        "username": "dddtyghbhgh@gmail.com",
        "password": "tgvDxcvG/25"
    },
    "user6": {
        "username": "gyhyhyhgh@gmail.com",
        "password": "yyytgD,tyy47/2"
    },
     "user7": {
        "username": "hiokmjkui@gmail.com",
        "password": "yyyhhD47/253"
    },
    "user8": {
        "username": "nyuiopopit@gmail.com",
        "password": "tguuuytG/253"
    },
    "user9": {
        "username": "bijnnjuiu@gmail.com",
        "password": "yyyhhhghF78/253"
    },
    "user10": {
        "username": "hhijnjjjuiu@gmail.com",
        "password": "yyyG587/8582"
    },
    "user11": {
        "username": "bbbiopopop@gmail.com",
        "password": "tttYhz/780/2"
    },
    "user12": {
        "username": "hijnuyuy@gmail.com",
        "password": "yyyhhhD47/850/U"
    },
    "user13": {
        "username": "jjjiuiuyuty@gmail.com",
        "password": "yyyH255/78I"
    },
    "user14": {
        "username": "hgbyuuyu@gmail.com",
        "password": "tttyyyG47/807/@"
    },
    "user15": {
        "username": "ftyghhhbht@gmail.com",
        "password": "tgvgtgC*/7Yu"
    },
    "user16": {
        "username": "binkopopi@gmail.com",
        "password": "tgvS/47/@Y"
    },
        "user17": {
        "username": "buyuuuyu@gmail.com",
        "password": "yyyhhhD*/T"
    },
    "user18": {
        "username": "vbyuuhhy@gmail.com",
        "password": "tgvF47/58@"
    },
    # 可以继续添加更多用户
}

# 遍历每个用户并尝试登录
for user, user_info in users.items():
    username = user_info["username"]
    password = user_info["password"]

    # 创建一个session对象
    session = requests.Session()

    # 设置User-Agent
    session.headers.update({'User-Agent': user_agent})

    # 获取登录页面
    response = session.get(login_url)

    # 获取CSRF token
    csrf_token = response.cookies['csrftoken']

    # 定义登录数据
    login_data = {
        'csrfmiddlewaretoken': csrf_token,
        'login': username,
        'password': password,
    }

    # 提交登录请求
    response = session.post(login_url, data=login_data, headers={'Referer': login_url})

    # 访问https://admin.alwaysdata.com/log
    response = session.get('https://admin.alwaysdata.com/log/', allow_redirects=False)

    # 检查响应状态
    if response.status_code == 200:
        print(f"用户 {user} 登录成功")
    elif response.status_code in [301, 302]:
        print(f"用户 {user} 登录失败，状态码：{response.status_code}")
    else:
        print(f"用户 {user} 未知状态，状态码：{response.status_code}")
    # 等待30秒
    time.sleep(20)
