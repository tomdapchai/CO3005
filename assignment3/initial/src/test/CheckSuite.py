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
        type Person struct {
            name string
            age int
            year int
            birth int
        }

        func (c Person) Add(x int) int {
            c.value += x;
            return c.value;
        }

        type People struct {
            name string
            age int
            year int
            birth int
        }

        func (c People) Add(x int) int {
            c.value += x;
            return c.value;
        }

        type Peo struct {
            name string
            age int
            year int
            birth int
        }

        func (c Person) Add(x int) int {
            c.value += x;
            return c.value;
        }

        """
        expect = "Redeclared Field: age\n"
        self.assertTrue(TestChecker.test(input,expect,404))
  