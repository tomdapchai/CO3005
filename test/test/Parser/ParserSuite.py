"""
 * Initial code for Assignment 1, 2
 * Programming Language Principles
 * Author: Võ Tiến
 * Link FB : https://www.facebook.com/Shiba.Vo.Tien
 * Link Group : https://www.facebook.com/groups/khmt.ktmt.cse.bku
 * Date: 20.01.2025
"""

import unittest
from TestUtils import TestParser
import inspect

class ParserSuite(unittest.TestCase):
    def test_001(self):
        """Literal"""
        self.assertTrue(TestParser.test("""
                                    func Add() {
                                        


                                        a := 1;


                                        var b = 2; var c = 3;

                                        func Add(x, y int) int {
                                            return x + y;
                                        }
                                    };""","successful", inspect.stack()[0].function))