import xlrd
import unittest
import xlwt
"""
   读取Excel
"""
class Excel():
    #读取excel中的某一单元格
    def excel_mode(self, line, column):
        excel=xlrd.open_workbook(r'D:\zhaoyang\py\API_test.xls')
        excel_noel=excel.sheet_by_index(0)
        colase=excel_noel.cell_value(line,column)
        # colases=eval(colase)
        return colase

    def excel_token(self):
        excel = xlrd.open_workbook(r'D:\zhaoyang\py\API_test.xls')
        excel_noel = excel.sheet_by_index(0)
        token = excel_noel.cell_value(1,5)
        return token

if __name__ == '__main__':
    re=Excel()
    re.excel_mode(1,4)
    re.excel_token()