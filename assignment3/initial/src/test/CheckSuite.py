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
    #             if (x == 1.0) {
    #                var a = 1.2;
    #             }
    #         }
    #     }
    #     """
    #     expect = "Undeclared Identifier: x\n"
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
        func foo() int { 
            var c = Car { name: "abc"}
            return foo()
        }

        func (c Car) getName() string {
            return c.name
        }
        type Car struct {
            name string
            owner [5][2] Student
            
        }
        type Vehicle interface {
            getName() string
        }
        func (c Car) getOwner() [5][2] Student {
            return c.owner
        }
        type Person interface {
            getName() string
            getAge() [3]int
        }
        func (p Student) getName() string {
            return p.name
        }
        type Student struct {
            name string
            age [3] float
        }

        func (p Student) getAge() [3]float {
            return p.age
        }

        func (s Student) getStudent() Student {

            var a Student = Student { name: "abc", age: [3]float{1.0, 2.0, 3.0}}
            return a.getStudent()
        }

        func foo1(a int,b int) Car {
            var c Vehicle;
            c := Car { name: "abc"}

            for i := 0; i > 10; i += 1 {
                var a int;
                a := 1;
            }

            if (a >= 1) {
                var a int;
                a := 1;
            }
            var a = foo();
            return c;
        }
        
        var arr [3]int;

        func foo2(a int) int{
            var n int;
            
            arr := [3]int{10, 20, 30}
            for index, value := range arr {
                n := n + value
                value := 1 % 2
            }

            for _, value := range arr {
                n := n + value
                continue
                break;
            }
            return 2;
        }

        
        var n int = 1;
        var o = foo1(1, 2);
        var p boolean = true && !(1 > 2);
        var m boolean = !(1 > 2);
        var a Vehicle = Car { name: "abc"} 
        var b Person = a.getOwner()[1][n]
        var c string = a.getOwner()[1][2].getName()
        
        func foo3(a [2]int) int{
            var n int;
            
            arr := [3]int{10, 20, 30}
            var arr1 [3]int;
            
            for index, value := range arr {
                n := n + value
                value := 1 % 2
            }

            for _, value := range arr {
                n := n + value
                continue
                break;
            }
            return 2;
        }

        var arr2 [n]Car;

        func foo5(a int) {
            var a int
        }

        func (c Car) putName(s string) {
            var a int
        }
        
        func foo4(a int) int{
            var n int;
            arr2[1].putName("abc");
            return n;
        }

        type I1 interface {
            getName() int
        }
        
        var x1 = 1 + 2 + 3 * 4 + (5 + 6) % 7 - -1;

        var x2 = 5 * 6;

        var x3 = x1 + 3;

        const x4 = x3 * x2;

        var x5 [30]int = [x2]int{1,2,3,4};



        """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,406))
  