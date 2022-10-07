import sys
import os
sys.path.append(sys.path[0] + "/...")
sys.path.append(os.getcwd())

from unittest import TestLoader, TestSuite, TextTestRunner
from Test.Scripts.test_HomePage import PHPT_HomePage
from Test.Scripts.test_LoginPage import PHPT_Login
from Test.Scripts.test_ManageHotelsPage import PHPT_Hotel

import testtools as testtools

if __name__ == "__main__":

    test_loader = TestLoader()
    test_suite = TestSuite((
        test_loader.loadTestsFromTestCase(PHPT_HomePage),
        test_loader.loadTestsFromTestCase(PHPT_Login),
        test_loader.loadTestsFromTestCase(PHPT_Hotel)
    ))

    test_runner = TextTestRunner(verbosity=2)
    test_runner.run(test_suite)

    parallel_suite = testtools.ConcurrentStreamTestSuite(lambda: ((case, None) for case in test_suite))
    parallel_suite.run(testtools.StreamResult())
