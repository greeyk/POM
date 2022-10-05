import sys
import os
sys.path.append(sys.path[0] + "/...")
sys.path.append(os.getcwd())

from unittest import TestLoader, TestSuite, TextTestRunner
from Test.Scripts.test_HomePage import Google_HomePage
from Test.Scripts.test_LoginPage import Google_Search

import testtools as testtools

if __name__ == "__main__":

    test_loader = TestLoader()
    test_suite = TestSuite((
        test_loader.loadTestsFromTestCase(Google_HomePage),
        test_loader.loadTestsFromTestCase(Google_Search)
    ))

    test_runner = TextTestRunner(verbosity=2)
    test_runner.run(test_suite)

    parallel_suite = testtools.ConcurrentStreamTestSuite(lambda: ((case, None) for case in test_suite))
    parallel_suite.run(testtools.StreamResult())

