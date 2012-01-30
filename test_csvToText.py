'''
Test the csvToText module.
'''
import unittest
import os
import shutil
import csvToText


class Test(unittest.TestCase):


    def setUp(self):
        self.path = "/Users/rob/Documents/workspace/csvToText/testdir"
        os.mkdir(self.path)
        self.csv_file_name = "testFile.csv"
        self.text_file_name = "testFile.txt"
        self.text = ["here", "now", "dog", "cat", "when", "choose"]
        self.csv_line = ",".join(self.text)
        self.text_line = " ".join(self.text)
        self.num_lines = 20
        
        f = open(os.path.join(self.path, self.csv_file_name), "w")
        for i in range(self.num_lines):
            f.write(self.csv_line)
            f.write("\n")
        f.close()
        
    def test_csvToText(self):
        expected = []
        for i in range(self.num_lines):
            expected.append(self.text_line + "\n") 
        csv_path = os.path.join(self.path, self.csv_file_name)
        text_path = os.path.join(self.path, self.text_file_name)
        args = ["csvToText.py", csv_path, text_path]
        csvToText.main(args)
        
        if not os.path.exists(text_path):
            raise IOError('"%s" does not exist' % (text_path,))
            
        f = open(text_path, "r")
        self.observed = f.readlines()
        f.close()
        self.assertEqual(self.observed, expected)

    def tearDown(self):
        try:
            shutil.rmtree(self.path, ignore_errors=True)
        except IOError:
            pass    

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()