/*
    Sample used to locate and isolate text from one file that may be in another using 2
    Map/Reduce stages.

    Tested on Node v10.3.0 / NPM 6.1.0 / Windows 10 x64
*/

const fs = require("fs"),
    moment = require("moment");

const REFERENCE_TXT_PATH = ".\\input_files\\sample_reference.txt",
    INPUT_TXT_PATH = ".\\input_files\\sample_input.txt",
    OUTPUT_TXT_PATH = ".\\output_files\\scrubbed_output.txt";

// Main file breaker - this takes a given file and breaks it into arbitrary 
// fragments, returning and array of fragments. For simplicity, this is breaking on 
// newline characters to start with. May have to be altered to work with puncuation 
// and/or special characters as needed.
let ReadAndMapFile = (path, callback) => {
    fs.readFile(path, (err, data) => {
        if (err) {
            callback(err);
            return;
        }

        let splitLines = [];
        data.toString().split("\r\n").map((item) => {
            let trimmedLine = item.trim();
            if (trimmedLine.length > 0){
                splitLines.push(trimmedLine);
            }
        });

        console.log(`Read ${splitLines.length} lines of text from ${path}`);

        callback(null, splitLines);
    });
};

// Overall strategy - essentially, read in the policy document and make a 
// joined, single character string out of it with unified casing. Then read 
// the input doc, break it into fragments, and attempt to locate each fragment 
// within the policy block.

// This is using the default implementation of .find(), and worst case should exhibit
// O(nm) runtime perf (if the fragment is NOT found). Could be optimized to use 
// Knuth-Morris-Pratt[1] to get better performance on larger policy documents as-needed.

// [1]: https://en.wikipedia.org/wiki/Knuth%E2%80%93Morris%E2%80%93Pratt_algorithm
(() => {
    let start = new Date(),
        end = new Date();

    ReadAndMapFile(REFERENCE_TXT_PATH, (err, referenceData) => {
        if (err) {
            console.log(`ERROR: ${err}`);
            return;
        }

        // Build index string of this reference file (REDUCE phase)
        let policyText = referenceData.join(" ").toLowerCase();

        ReadAndMapFile(INPUT_TXT_PATH, (err, inputData) => {
            if (err) {
                console.log(`ERROR: ${err}`);
                return;
            }

            let scrubbedInputData = [];

            inputData.map((inputItem, index) => {
                if (policyText.indexOf(inputItem.toLowerCase()) > -1){
                    console.log(`Found match at (${index}): "${inputItem}"`);
                } else {
                    scrubbedInputData.push(inputItem);
                }
            });

            // Reduce the input data and dump out the stream
            fs.writeFileSync(OUTPUT_TXT_PATH, scrubbedInputData.join("\r\n"));

            end = new Date();
            console.log(`Total execution time: ${(end-start)}ms`)
        });
    });
})();