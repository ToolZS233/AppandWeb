import requests


class TestAddress:
    def setup(self):
        self.access_token = self.get_token()

    def get_token(self):
        res = requests.get(
            'https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid=ww540601793b2a3f57&corpsecret=IceeCVjilJWHgF7QN2kunUzKm-RQBbP5W_8gNp66mdA')
        return (res.json()['access_token'])

    def test_get_information(self):
        userid = 'ZhangShuai'
        res = requests.get(
            f'https://qyapi.weixin.qq.com/cgi-bin/user/get?access_token={self.access_token}&userid={userid}')
        print(res.json())

    def test_add_merber(self):
        url = f'https://qyapi.weixin.qq.com/cgi-bin/user/create?access_token={self.access_token}'
        data = {
            "userid": "001",
            "name": "漩涡鸣人",
            "mobile": "13800000000",
            "department": [1]
        }
        res = requests.post(url, json=data)
        print(res.json())

    def test_update(self):
        url = f'https://qyapi.weixin.qq.com/cgi-bin/user/update?access_token={self.access_token}'
        data = {
            "userid": "001",
            "name": "宇智波佐助",
            "mobile": "13800000000",
            "department": [1]
        }
        res = requests.post(url, json=data)
        print(res.json())

    def test_delete(self):
        userid = '001'
        res = requests.get(
            f'https://qyapi.weixin.qq.com/cgi-bin/user/delete?access_token={self.access_token}&userid={userid}')
        print(res.json())
