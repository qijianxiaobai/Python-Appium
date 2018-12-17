
from Base.BaseRunner import ParametrizedTestCase
import os
import sys
from PageObject.Home.FirstOpenPage import FirstOpenPage
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


class HomeTest(ParametrizedTestCase):
    def testFirstOpen(self):
        group = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../Yamls/团购/Test_GroupPurchase.yaml"),
               "device": self.devicesName, "caseName": sys._getframe().f_code.co_name}

        group_page = FirstOpenPage(group)
        group_page.operate()
        group_page.checkPoint()


        sweep = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../Yamls/扫码购/Test_SweepPurchasing.yaml"),
               "device": self.devicesName, "caseName": sys._getframe().f_code.co_name}

        sweep_page = FirstOpenPage(sweep)
        sweep_page.operate()
        sweep_page.checkPoint()

    @classmethod
    def setUpClass(cls):
        super(HomeTest, cls).setUpClass()

    @classmethod
    def tearDownClass(cls):
        super(HomeTest, cls).tearDownClass()
