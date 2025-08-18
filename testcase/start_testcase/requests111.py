import requests

req = requests.Session()
# 三种传参模式,形参名分别为json、data、params，其实都是json格式
# 三种传参，json使用post，传请求体；params适用get，传查询参数；data就是直接传字符串，且没有设置context-type
# json_data={
#     "title": "foo",
#     "body": "bar",
#     "userId": 1
# }

json_data = {
    "username": "gxy",
    "password": "gxy040720"
}
# r=requests.get("https://jsonplaceholder.typicode.com/posts")   #requests.get方法

# r = requests.post(url="https://dict.youdao.com/keyword/key", data=data)

# r = requests.get('http://localhost:8080/index')

# r = requests.post('http://localhost:8080/account/login', json=json_data)
# print(r.json())

# 返回状态码418,要给请求加上headers信息,教程里加的是User-Agent
# headers = {
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 Edg/122.0.0.0"
# }

res = req.post(url='http://127.0.0.1:8080/account/login', json=json_data) #url和请求方式要注意，别输错了
print(res.headers)
print(res.status_code)
print("Session Cookies:", req.cookies.get_dict())
print(res.json())

res2 = req.get(url="http://127.0.0.1:8080/index")
print(res2.status_code)
print(res2.text)
