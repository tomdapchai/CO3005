import unittest
from TestUtils import TestChecker
from AST import *

class CheckSuite(unittest.TestCase):
    # def test_redeclared(self):
    #     input = """var a int; var b int; var a int; """
    #     expect = "Redeclared Variable: a\n"
    #     self.assertTrue(TestChecker.test(input,expect,400))

    # def test_type_mismatch(self):
    #     input = """var a int = 1.2;"""
    #     expect = "Type Mismatch: VarDecl(a,IntType,FloatLiteral(1.2))\n"
    #     self.assertTrue(TestChecker.test(input,expect,401))

    # def test_undeclared_identifier(self):
    #     input = Program([VarDecl("a",IntType(),Id("b"))])
    #     expect = "Undeclared Identifier: b\n"
    #     self.assertTrue(TestChecker.test(input,expect,402))

    # def test_function(self):
    #     input = """
    #     func foo(a int, b int, a, c int) int {return 1;}
        
    #     """
    #     expect = "Redeclared Parameter: a\n"
    #     self.assertTrue(TestChecker.test(input,expect,403))

    # def test1(self):
    #     input = """
    #     func foo(a int, b int, c int) int {
    #         if (a == b) {
    #             var e int;
    #             e := 1;
    #         } else if (x == c) {
    #             var x float;
    #             x := 1;
    #         } else {
    #             var x float;
    #             if (x == 1) {
    #                var a = 1.2;
    #             }
    #         }
    #     }
    #     """
    #     expect = "Redeclared Variable: e\n"
    #     self.assertTrue(TestChecker.test(input,expect,404))

    # def test2(self):
    #     input = """
    #     func foo(a int, b int, c int) int {
    #         var x float;
    #     }
        
    #     var x int;
    #     const y = 1;
    #     var z = 1.2;
        

    #     type Person struct {
    #         name string;
    #         age int;
    #     }

    #     type Car interface {
    #         Add(a int, b int) int;
    #         Sub(a int, b int) int;
    #     }

    #     type Door interface {
    #         Add(a int, b int) int;
    #         Sub(a int, b int) int;
    #     }

    #     func (p Person) getAge() int {
    #         var x int;
            
    #     }

    #     func Person(a int) int {
    #         var x int;
    #     }

    #     """
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input,expect,405))

    def test3(self):
        input = """

        type Person struct {
            name string;
            age int;
        }

        const x = -1;
        var y int = x;

        func foo(a int, b float, c int) int {
            a := x;

            if (c < b) {

                return;
            }
        
        }

        func foo1() {
            foo(x, 1.2, 5, 6);
        }



        """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,406))
  