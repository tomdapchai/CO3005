import unittest
from TestUtils import TestParser

class ParserSuite(unittest.TestCase):
    def test_simple_program(self):
        """Simple program: void main() {} """
        input = """const Votien = 1 || 2 && c + 3 / 2 - -1;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,201))

    def test_more_complex_program(self):
        """More complex program"""
        input = """func foo () {
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,202))
    
    def test_wrong_miss_close(self):
        """Miss ) void main( {}"""
        input = """func main({};"""
        expect = "Error on line 1 col 11: {"
        self.assertTrue(TestParser.checkParser(input,expect,203))

    def test_wrong_variable(self):
        input = """var int;"""
        expect = "Error on line 1 col 5: int"
        self.assertTrue(TestParser.checkParser(input,expect,204))

    def test_wrong_index(self):
        input = """var i ;"""
        expect = "Error on line 1 col 7: ;"
        self.assertTrue(TestParser.checkParser(input,expect,205))
    def test_30(self):
        input = """const k = -a + -!-!c - ---[2]int{2};  """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,206))
    def test_31(self):
        input = """
                                        break;
                                    func Add() {
                                    }"""
        expect = "Error on line 2 col 41: break"
        self.assertTrue(TestParser.checkParser(input,expect,207))
    def test_32(self):
        input = """func (c c) Add(x int, c int) {
        }
         
            """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,208))
    
    