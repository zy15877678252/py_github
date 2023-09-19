import requests
import xlrd

class xunhuan():
    def tser_er(self):
        excel=xlrd.open_workbook(r'D:\zhaoyang\py\API_test.xls')
        excel_name=excel.sheet_by_index(0)
        for call in excel_name.col(4):
            return call.value
    def test_url(self):
        excel = xlrd.open_workbook(r'D:\zhaoyang\py\API_test.xls')
        excel_name = excel.sheet_by_index(0)
        for cell in excel_name.col(1):
            return cell.value
    def test_h(self):
        excel = xlrd.open_workbook(r'D:\zhaoyang\py\API_test.xls')
        excel_name = excel.sheet_by_index(0)
        for cell in excel_name.col(1):
            return cell.value


if __name__ == '__main__':
    xx=xunhuan()
    xx.tser_er()