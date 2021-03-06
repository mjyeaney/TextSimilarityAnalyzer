"""
    Sample used to locate and isolate text from one file that may be in another using 2
    Map/Reduce stages.

    Tested on Python 3.6.4, Windows 10 x64
"""
import os
import time
import io
import logging

FILE_ENCODING = "utf-8"

logging.basicConfig(level=logging.DEBUG)

def readAndMapFile(path):
    """
    Main file breaker - this takes a given file and breaks it into arbitrary 
    fragments, returning and array of fragments. For simplicity, this is breaking on 
    newline characters to start with. May have to be altered to work with puncuation 
    and/or special characters as needed.
    """

    splitLines = []
    
    def mapper(line):
        strippedLine = line.strip()
        if (len(strippedLine) > 0):
            splitLines.append(strippedLine)
    
    with open(path, "r", encoding=FILE_ENCODING) as f:
        content = f.read()
        items = content.split("\n")

        for i in items:
            logging.info("n-gram length = {}".format(len(i)))
            mapper(i)
        
    logging.info("Read {} lines of text from {}".format(len(splitLines), path))
    return splitLines

def scrubFile(inputFilePath, referenceFilePath, outputFilePath):
    """
    Overall strategy - essentially, read in the policy document and make a 
    joined, single character string o ut of it with unified casing. Then read 
    the input doc, break it into fragments, and attempt to locate each fragment 
    within the policy block.

    This is using the default implementation of .find(), and worst case should exhibit
    O(nm) runtime perf (if the fragment is NOT found). Could be optimized to use 
    Knuth-Morris-Pratt[1] to get better performance on larger policy documents as-needed.

    [1]: https://en.wikipedia.org/wiki/Knuth%E2%80%93Morris%E2%80%93Pratt_algorithm
    """

    policyText = " ".join(readAndMapFile(referenceFilePath)).lower()
    inputText = readAndMapFile(inputFilePath)
    scrubbedData = []
    mapperPos = 0

    def mapper(line, index):
        if (policyText.find(line.lower()) > -1):
            logging.info("Found match at {}: {}".format(index, line))
        else:
            scrubbedData.append(line)
    
    for line in inputText:
        mapper(line, mapperPos)
        mapperPos = mapperPos + 1
    
    with open(outputFilePath, "w", encoding=FILE_ENCODING) as scrubbedFile:
        scrubbedFile.write("\n".join(scrubbedData))

def main():
    baselineDocPath = os.path.join(".", "input_files", "sample_reference.txt")
    inputDocPath = os.path.join(".", "input_files", "sample_input.txt")
    resultsDocPath = os.path.join(".", "output_files", "scrubbed_output.txt")

    start = time.time()
    scrubFile(inputDocPath, baselineDocPath, resultsDocPath)
    end = time.time()

    logging.info("Total execution time: {}ms".format((end - start) * 1000))

# Bootstrap the main method
if (__name__ == "__main__"):
    main()
