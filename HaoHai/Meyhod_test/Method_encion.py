import json
from HaoHai.Excel_test import Excel_meter
from HaoHai.Meyhod_test import meyhod_api
import xlrd
"""

公用方法封装

"""
class Method_tion():
    # 获取token来拼接headers
    def Token(self):
        excel = Excel_meter.Excel()
        token = excel.excel_token()
        # return token
        print(token)

    # 获取接口用例的数据
    def Excel1(self):
        excel01 = Excel_meter.Excel()
        return excel01

    # 获取请求头信息
    def header(self):
        headers = {"Content-type": "application/json"}
        return headers

    #遍历excel表中的参数
    # def tser_data(self):
    #     excel=xlrd.open_workbook(r'D:\zhaoyang\py\API_test.xls')
    #     excel_name=excel.sheet_by_index(0)
    #     for call in excel_name.col(4):
    #         return call.value

    #便利excel中的URL
    # def test_url(self):
    #     excel = xlrd.open_workbook(r'D:\zhaoyang\py\API_test.xls')
    #     excel_name = excel.sheet_by_index(0)
    #     for cell in excel_name.col(1):
    #         return cell.value
if __name__ == '__main__':
    method=Method_tion()
    method.Token()
    method.Excel1()
    method.header()
    # method.test_url()
    # method.tser_data()