import json
import unittest
import requests
from HaoHai.Excel_test import Excel_meter
from HaoHai.Meyhod_test import meyhod_api
from HaoHai.Meyhod_test import Method_encion
import xlrd
"""
搜索商品下单支付

"""
class Test_Place(unittest.TestCase):

    #获取token来拼接headers
    def Token(self):
        excel = Excel_meter.Excel()
        token = excel.excel_token()
        return token

    #搜素商品
    def test_asearch1(self):
        try:
            method=Method_encion.Method_tion()
            headers=method.header()
            token=self.Token()
            excel=method.Excel1()
            url=excel.excel_mode(1,1)
            Data=excel.excel_mode(1,4)
            data=eval(Data)
            data['user_token']=token
            meyod=meyhod_api.ApiRequest()
            re=meyod.post_method(url,data,headers)
            goo_id=re['data']['list'][0]['goods_id']
            self.assertEqual(re['code'],200,msg=re)
            return goo_id
        except Exception as e:
            print(e)
            raise

    #商品详情
    def test_bcommodity2(self):
        try:
            method = Method_encion.Method_tion()
            headers = method.header()
            excel = method.Excel1()
            url = excel.excel_mode(2, 1)
            data = excel.excel_mode(2, 4)
            good_os = self.test_asearch1()
            token=self.Token()
            Data = eval(data)
            Data['goods_id'] =good_os
            Data['user_token'] =token
            datas = json.dumps(Data)
            data_as=eval(datas)
            meyud=meyhod_api.ApiRequest()
            re_commodity=meyud.post_method(url,data_as,headers)
            sku=re_commodity['data']['sku'][0]['sku_id']
            self.assertEqual(re_commodity['code'],200,msg=re_commodity)
            return sku
        except Exception as e:
            print(e)
            raise

    #立即购买
    def test_cpurchase(self):
        try:
            method = Method_encion.Method_tion()
            headers = method.header()
            token = self.Token()
            excel = method.Excel1()
            url = excel.excel_mode(3, 1)
            good_os = self.test_asearch1()
            sku=self.test_bcommodity2()
            Data = excel.excel_mode(3, 4)
            data = eval(Data)
            data['user_token'] = token
            data['goods_id'] = good_os
            data['sku_id'] = sku
            datas = json.dumps(data)
            datass = eval(datas)
            meyud = meyhod_api.ApiRequest()
            re_cpurchase = meyud.post_method(url, datass, headers)
            self.assertEqual(re_cpurchase['code'], 200, msg=re_cpurchase)
            return
        except Exception as e:
            print(e)
            raise

    #余额支付
    def test_payment(self):
        try:
            method = Method_encion.Method_tion()
            headers = method.header()
            # token = method.Token()
            excel = method.Excel1()
            url = excel.excel_mode(4, 1)
            good_os = self.test_asearch1()
            # sku = self.test_bcommodity2()
            token=self.Token()
            Data = excel.excel_mode(4, 4)
            data = eval(Data)
            data['user_token'] = token
            data['goods_id'] = good_os
            # data['sku_id'] = sku
            datas = json.dumps(data)
            datass = eval(datas)
            meyud = meyhod_api.ApiRequest()
            re_payment = meyud.post_method(url, datass, headers)
            self.assertEqual(re_payment['code'],200,msg=re_payment)
            return
        except Exception as e:
            print(e)
            raise



if __name__ == '__main__':
    unittest.main()