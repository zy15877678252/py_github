import requests
import json


class ApiRequest(object):
    """
    请求方法
    """

    # 请求方法get
    def get_method(self, url,data=None, headers=None):

        # if header is not None:
        #     res = requests.get(url, params=data, headers=header)
        # else:
        res = requests.get(url=url,data=json.dumps(data),headers=headers)
        return res.json()

    # 请求方法post
    def post_method(self, url, data=None, headers=None):
        # global res
        # if header is not None:
        res = requests.post(url=url,json=data, headers=headers)
        # else:
        #     res = requests.post(url, json=data)
        # if str(res) == "<Response [200]>":
        return res.json()
        # else:
        #     return res.text

        # def test_add():
        #     aaqqw=Excel_add.Excel()
        #     gdfga=aaqqw.excel1(1,4)
        #     print(gdfga)
# if __name__ == '__main__':
#     api=ApiRequest()
#     api.get_method()
#     api.post_method()