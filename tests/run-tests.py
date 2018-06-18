"""
    Test cases for the text similarity analyzer. We need to make sure 
    we're properly identifying cases.abs
"""

import time
import io
import os
import sys

def SampleLineIsAllCopied():
    """
    Checks the case where the sample line is a complete, copied fragment.
    """
    print("(Error: ENOIMPL, Missing test implementation)", file=sys.stderr)

def SampleLineIsPartialCopy():
    """
    Checks the case where the sample line only contains a fragment of a copied
    piece.
    """
    print("(Error: ENOIMPL, Missing test implementation)", file=sys.stderr)

def RunAll():
    """
    Runs all test methods and checks for proper behavior.
    """
    SampleLineIsAllCopied()
    SampleLineIsPartialCopy()

if (__name__ == "__main__"):
    RunAll()