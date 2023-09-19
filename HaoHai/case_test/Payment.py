import requests
import json
import unittest
from HaoHai.Meyhod_test import Method_encion
from HaoHai.Meyhod_test import meyhod_api
from HaoHai.case_test import DEmo1
"""

下单支付

"""

class Text_paymert(unittest.TestCase):
    #搜索商品
    # def test_case01(self):
    #     try:
    #         globe=Method_encion.Method_tion()
    #         host=meyhod_api.ApiRequest()
    #         token=globe.Token()
    #         headers=globe.header()
    #         excel=globe.Excel1()
    #         url=excel.excel_mode(0,1)
    #         datas=excel.excel_mode(0,4)
    #         data=eval(datas)
    #         re=host.post_method(url,data,headers)
    #         goo_id = re['data']['list'][0]['goods_id']
    #         self.assertEqual(re['code'],200,msg=re)
    #         return goo_id
    #     except Exception as e:
    #         print(e)
    #         raise

    def test_case002(selfself):
        datas=DEmo1.xunhuan()
        data=datas.tser_er()
        Data=eval(data)
        url=datas.test_url()
        headers={"Content-type": "application/json"}
        host=meyhod_api.ApiRequest()
        re=host.post_method(url,Data,headers)
        print(re)

if __name__ == '__main__':
    unittest.main()