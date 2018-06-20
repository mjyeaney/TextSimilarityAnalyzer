"""
    Test cases for the text similarity analyzer. We need to make sure 
    we're properly identifying cases.
"""

import time
import io
import os
import sys
import unittest

sys.path.append("./")

import scrubber

class TestSimilarityMethods(unittest.TestCase):

    def test_SampleLineIsAllCopied(self):
        """
        Checks the case where the sample line is a complete, copied fragment.
        """
        REFERENCE_TXT_PATH = os.path.join(".", "input_files", "sample_reference.txt")
        INPUT_TXT_PATH = os.path.join(".", "tests", "case1.txt")
        OUTPUT_TXT_PATH = os.path.join(".", "tests", "case1-out.txt")
        OUTPUT_MASTER_TXT_PATH = os.path.join(".", "tests", "case1-master.txt")

        scrubber.scrubFile(INPUT_TXT_PATH, REFERENCE_TXT_PATH, OUTPUT_TXT_PATH)
        
        with open(OUTPUT_MASTER_TXT_PATH, "r", encoding=scrubber.FILE_ENCODING) as master:
            desired = master.read()
            with open(OUTPUT_TXT_PATH, "r", encoding=scrubber.FILE_ENCODING) as f:
                result = f.read()

                self.assertTrue(desired == result)

    def test_SampleLineIsPartialCopy(self):
        """
        Checks the case where the sample line only contains a fragment of a copied
        piece. Note this isn't expected to work, as we're only looking for exact matches.
        """
        REFERENCE_TXT_PATH = os.path.join(".", "input_files", "sample_reference.txt")
        INPUT_TXT_PATH = os.path.join(".", "tests", "case2.txt")
        OUTPUT_TXT_PATH = os.path.join(".", "tests", "case2-out.txt")
        OUTPUT_MASTER_TXT_PATH = os.path.join(".", "tests", "case1-master.txt")

        scrubber.scrubFile(INPUT_TXT_PATH, REFERENCE_TXT_PATH, OUTPUT_TXT_PATH)
        
        with open(OUTPUT_MASTER_TXT_PATH, "r", encoding=scrubber.FILE_ENCODING) as master:
            desired = master.read()
            with open(OUTPUT_TXT_PATH, "r", encoding=scrubber.FILE_ENCODING) as f:
                result = f.read()

                self.assertFalse(desired == result)

if (__name__ == "__main__"):
    unittest.main()