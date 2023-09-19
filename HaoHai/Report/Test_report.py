from BeautifulReport import BeautifulReport as bt
from HaoHai.case_test import Place_test
import unittest

"""

报告输入层

"""

unittes=unittest.TestSuite()
unittes.addTest(unittest.makeSuite(Place_test.Test_Place))
rung=bt(unittes)
rung.report(filename="Test_report.py", description="新媒体小程序接口测试")