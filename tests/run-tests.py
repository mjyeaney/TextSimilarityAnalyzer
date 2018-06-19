"""
    Test cases for the text similarity analyzer. We need to make sure 
    we're properly identifying cases.abs
"""

import time
import io
import os
import sys
import unittest

sys.path.append("../")

import scrubInputFile

class TestSimilarityMethods(unittest.TestCase):

    def test_SampleLineIsAllCopied(self):
        """
        Checks the case where the sample line is a complete, copied fragment.
        """
        self.fail("No implementation!!!")

    def test_SampleLineIsPartialCopy(self):
        """
        Checks the case where the sample line only contains a fragment of a copied
        piece.
        """
        self.fail("No implementation!!!")

if (__name__ == "__main__"):
    unittest.main()