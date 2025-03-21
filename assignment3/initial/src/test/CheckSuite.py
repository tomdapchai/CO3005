import unittest
from TestUtils import TestChecker
from AST import *

class CheckSuite(unittest.TestCase):
    def test_redeclared(self):
        input = """var a int; var b int; var a int; """
        expect = "Redeclared Variable: a\n"
        self.assertTrue(TestChecker.test(input,expect,400))

    def test_type_mismatch(self):
        input = """var a int = 1.2;"""
        expect = "Type Mismatch: VarDecl(a,IntType,FloatLiteral(1.2))\n"
        self.assertTrue(TestChecker.test(input,expect,401))

    def test_undeclared_identifier(self):
        input = Program([VarDecl("a",IntType(),Id("b"))])
        expect = "Undeclared Identifier: b\n"
        self.assertTrue(TestChecker.test(input,expect,402))

    def test_function(self):
        input = """
        func foo(a int, b int, a, c int) int {return 1;}
        
        """
        expect = "Redeclared Parameter: a\n"
        self.assertTrue(TestChecker.test(input,expect,403))

    def test(self):
        input = """
        func foo(a int, b int, c int) int {
            if (a == b) {
                var e int;
                e := 1;
            } else if (x == c) {
                var x float;
                x := 1;
            } else {
                var x float;
                if (x == 1) {
                   var a = 1.2;
                }
            }
        }
        """
        expect = "Redeclared Variable: e\n"
        self.assertTrue(TestChecker.test(input,expect,404))
  