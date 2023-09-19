from HaoHai.Excel_test import Excel_meter
from HaoHai.Meyhod_test import meyhod_api
import requests
import unittest
"""

搜索商品加购下单

"""
class Test_Search(unittest.TestCase):
    #调用Execel的方法获取token
    def Token1(self):
        excel=Excel_meter.Excel()
        token=excel.excel_token()
        #用返回的token来拼接请求头
        headers={"Content-type":"application/json","user_token":token}
        # return headers
        print(token)

    #调用获取excel的行和列
    # def Excel1(self):
    #     excel1=Excel_meter.Excel()
    #     return excel1

    #搜索上商品
    # def test_search(self):
    #     header=self.Token1()
    #     excel=self.Excel1()
    #     url=excel.excel_mode(1,1)
    #     data=excel.excel_mode(1,4)
    #     Data=json.load(data)
    #     method=meyhod_api.ApiRequest()
    #     re=method.post_method(url,Data,header)
    #     print(re)


if __name__ == '__main__':
    unittest.main()
