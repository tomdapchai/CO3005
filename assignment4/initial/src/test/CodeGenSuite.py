import unittest
from TestUtils import TestCodeGen
from AST import *


class CheckCodeGenSuite(unittest.TestCase):
    # def test_int_literal(self):
    #     input = """func main() {putInt(5);};"""
    #     expect = "5"
    #     self.assertTrue(TestCodeGen.test(input,expect,501))
    # def test_local_var(self):
    #     input = """func main() {var a int = 20;  putInt(a);};"""
    #     expect = "20"
    #     self.assertTrue(TestCodeGen.test(input,expect,502))
    # def test_gllobal_var(self):
    #     input = """var a int = 10; func main() { putInt(a);};"""
    #     expect = "10"
    #     self.assertTrue(TestCodeGen.test(input,expect,503))
    # def test_int_ast(self):
    #     input = Program([FuncDecl("main",[],VoidType(),Block([FuncCall("putInt", [IntLiteral(25)])]))])
    #     expect = "25"
    #     self.assertTrue(TestCodeGen.test(input,expect,504))
    # def test_local_var_ast(self):
    #     input = Program([FuncDecl("main",[],VoidType(),Block([VarDecl("a",IntType(),IntLiteral(500)),FuncCall("putInt", [Id("a")])]))])
    #     expect = "500"
    #     self.assertTrue(TestCodeGen.test(input,expect,505))
    # def test_global_var_ast(self):  
    #     input = Program([VarDecl("a",IntType(),IntLiteral(5000)),FuncDecl("main",[],VoidType(),Block([FuncCall("putInt", [Id("a")])]))])
    #     expect = "5000"
    #     self.assertTrue(TestCodeGen.test(input,expect,506))
    
    # def test_1(self):
    #     input = """
    #     func main() {
    #         var a int = 5;
    #         var b int = 10;
    #         putInt(a + b);
    #     };"""
    #     expect = "15"
    #     self.assertTrue(TestCodeGen.test(input,expect,507))

    # def test_2(self):
    #     input = """
    #     func main() {
    #         var a int = 5;
    #         var b int = 10;
    #         var c int = 15;
    #         putInt(a + b + c);
    #     };"""
    #     expect = "30"
    #     self.assertTrue(TestCodeGen.test(input,expect,508))

    # def test_3(self):
    #     input = """
    #     var a int = 10
    #     var y int = 15

    #     func main() {
    #         var a int = 5;
    #         var b int = 10;
    #         var c int = 15;
    #         var d int = 20;
    #         putInt((a + b + c + d % a) * a / y);
    #     };"""
    #     expect = "10"
    #     self.assertTrue(TestCodeGen.test(input,expect,509))

    # def test_4(self):
    #     input = """
    #     var a int = 10
    #     var y float = 15.5

    #     func main() {
    #         var a int = 5;
    #         var b int = 10;
    #         var c int = 15;
    #         var d int = 20;
    #         putFloat((a + b + c + d % a) * a + y);
    #     };"""
    #     expect = "165.5"
    #     self.assertTrue(TestCodeGen.test(input,expect,510))

    # def test_5(self):
    #     input = """
    #     var a int = 10
    #     var y float = 15.5

    #     func main() {
    #         var a = 5 * 2 - 10 + 5;
    #         var b = 10;
    #         var c = 15;
    #         var d int = 20;
    #         putFloat((a + b + c + d % a) * a - y);
    #     };
        
    #     """
    #     expect = "134.5"
    #     self.assertTrue(TestCodeGen.test(input,expect,511))
    
    # def test_6(self):
    #     input = """
    #     var a = 5 + 0
    #     var y = 15.5

    #     func main() {
    #         var b = 10;
    #         var c = 15;
    #         var d int = 20;
    #         putFloat((a + b + c + d % a) * a - y);
    #     };
        
    #     """
    #     expect = "134.5"
    #     self.assertTrue(TestCodeGen.test(input,expect,512))

    # def test_7(self):
    #     input = """
    #     const a = 20 * 10
    #     var y = 15.5 * 2

    #     func main() {
    #         putFloat(a + y)
    #     };
        
    #     """
    #     expect = "231.0"
    #     self.assertTrue(TestCodeGen.test(input,expect,513))

    # def test_8(self):
    #     input = """
    #     const a = 20 * 10
    #     var y = 15.5

    #     func main() {
    #         const x = 10 * 2 + 3
    #         var a = 20
    #         putFloatLn(a + y)
    #         a := a + 10
    #         putInt(x * a)

    #     };
        
    #     """
    #     expect = "35.5\n690"
    #     self.assertTrue(TestCodeGen.test(input,expect,514))

    # def test_9(self):
    #     input = """
    #     const a = 20 * 10
    #     var y = 15.5

    #     func main() {
    #         const x = 10 * 2 + 3
    #         var a = 20
    #         putFloatLn(a + y)
    #         a := a + 10
    #         putIntLn(x * a)
    #         y += 10
    #         putFloat(y)

    #     };
        
    #     """
    #     expect = "35.5\n690\n25.5"
    #     self.assertTrue(TestCodeGen.test(input,expect,515))

    # def test_10(self):
    #     input = """
    #     const a = 20 * 10
    #     var y = 15.5

        

    #     func main() {
    #         const x = 10 * 2 + 3
    #         var a = 20
    #         putFloatLn(a + y)
    #         a := a + 10
    #         putIntLn(x * a)
    #         y += 10
    #         putFloatLn(y)
    #         putInt(a + foo())

    #     };
        
    #     func foo() int {
    #         return 1 + 2;
    #     }
    #     """
    #     expect = "35.5\n690\n25.5\n33"
    #     self.assertTrue(TestCodeGen.test(input,expect,516))


    # def test_11(self):
    #     input = """
    #     const a = 20 * 10
    #     var y = 15.5

    #     func main() {
    #         if (y >= 16) {
    #             putInt(a + foo())
    #         } else {
    #             putInt(a + foo() + 1)
    #         }
    #     };
        
    #     func foo() int {
    #         return 1 + 2;
    #     }
    #     """
    #     expect = "204"
    #     self.assertTrue(TestCodeGen.test(input,expect,517))

    # def test_12(self):
    #     input = """
    #     const a = 20 * 10
    #     var y = 15.5

    #     func main() {
    #         if (y >= 16) {
    #             putInt(a + foo())
    #         } else {
    #             if (a + 10 >= 211) {
    #                 putIntLn(234)
    #             } else {
    #                 var x = 5;
    #                 for x < 10 {
    #                     putIntLn(567)
    #                     x += 1;
    #                 }
    #             }
    #             putInt(a + foo() + 1)
    #         }
    #         for i := 0; i < 10; i += 1 {
    #             putInt(i)
    #         }
    #     };
        
    #     func foo() int {
    #         return 1 + 2;
    #     }
    #     """
    #     expect = "567\n567\n567\n567\n567\n2040123456789"
    #     self.assertTrue(TestCodeGen.test(input,expect,518))

    # def test_13(self):
    #     input = """
    #     const a = 20 * 10
    #     var y = 15.5
    #     var x = "Hello World"
    #     func main() {
    #         putStringLn(x)
    #         putString("Welcome 2025")
    #     };
    #     """
    #     expect = "Hello World\nWelcome 2025"
    #     self.assertTrue(TestCodeGen.test(input,expect,519))

    # def test_14(self):
    #     input = """
    #     const a = 20 * 10
    #     var y = 15.5

    #     func main() {
    #         if (y >= 16) {
    #             putInt(a + foo())
    #         } else {
    #             if (a + 10 >= 211) {
    #                 putIntLn(234)
    #             } else {
    #                 var x = 5;
    #                 for x < 10 {
    #                     putIntLn(567)
    #                     x += 1;
    #                 }
    #             }
    #             putInt(a + foo() + 1)
    #         }
    #         for i := 0; i < 10; i += 1 {
    #             if (i <= 4) {
    #                 if (foo() > 2 && i < 3) {
    #                     continue;
    #                 }
    #             }
    #             putInt(i)
    #             if (i == 8) {
    #                 break;
    #             }

    #         }
    #     };
        
    #     func foo() int {
    #         return 1 + 2;
    #     }
    #     """
    #     expect = "567\n567\n567\n567\n567\n204345678"
    #     self.assertTrue(TestCodeGen.test(input,expect,520))

    # def test_15(self):
    #     input = """
    #     const a = 5;
    #     func main() {
    #         var b = 3;
    #         var a [4]int = [4]int{5, 2, 3, 4}
    #         var arr [5]int = [5]int{10, 20, 30, 40, 50}
    #         a[1] := 20
    #         var x = 10;
    #         putIntLn(a[0] + arr[0] * 2 + a[1])
    #     }
    #     """
    #     expect = "45\n"
    #     self.assertTrue(TestCodeGen.test(input,expect,521))

    # def test_16(self):
    #     input = """
    #     const a = 5;
    #     func main() {
    #         var b = 3;
    #         var a [4]int = [4]int{5, 2, 3, 4}
    #         var arr [3][4]int = [3][4]int{{1, 2, 3}, {1, 2, 3, 4}, {10, 20}}
            
    #         var x = 10;
    #         putIntLn(a[0] + arr[2][1] * 2)
    #         putIntLn(arr[0][3])
    #         arr[0][3] := 10
    #         putIntLn(arr[0][3])
    #     }
    #     """
    #     expect = "45\n0\n10\n"
    #     self.assertTrue(TestCodeGen.test(input,expect,522))
    
    # def test_17(self):
    #     input = """
    #     const a = 5;
    #     func main() {

    #         var b = foo()[0] + 1
    #         putIntLn(b)
    #     }

    #     // somehow this test works so well idk lololol

    #     func foo() [3]int {
        
    #         return [3]int{1, 2, 3}
    #     }
    #     """
    #     expect = "2\n"
    #     self.assertTrue(TestCodeGen.test(input,expect,523))

    # def test_18(self):
    #     input = """
    #     const a = 5;
    #     var b = 5;

    #     func (p Person) foo() {
    #         var x = 10;
    #     }

    #     type Person struct {
    #         name string;
    #         age int;
    #     }

    #     func main() {
    #         var x Person = Person{name: "John", age: 30}
    #         var y Person = Person{name: "Doe", age: 25}
    #         putIntLn(x.age)
    #         putStringLn(x.name)
    #         putIntLn(y.age)
    #         putStringLn(y.name)
    #         putIntLn(x.age)
    #         putStringLn(x.name)
    #     }

        
    #     """
    #     expect = "30\nJohn\n25\nDoe\n30\nJohn\n"
    #     self.assertTrue(TestCodeGen.test(input,expect,524))
    
    # def test_19(self):
    #     input = """
    #     type Person struct {
    #         name string;
    #         age int;
    #     }

    #     func main() {
    #         var x Person = Person{name: "John", age: 30}
    #         x.age := 35 * 2
    #         var y Person = Person{name: "Jane", age: 25}
    #         y.name += " Doe"
    #         putIntLn(x.age)
    #         putStringLn(y.name)
    #     }

        
    #     """
    #     expect = "70\nJane Doe\n"
    #     self.assertTrue(TestCodeGen.test(input,expect,525))
    
    def test_20(self):
        input = """
        type Person struct {
            name string;
            age int;
            height float;
        }

        func foo() Person {
            var k Person = Person{name: "Doe", age: 25, height: 180.5}
            return k
        } 

        func main() {
            var x Person = Person{age: 30, height: 177.3, name: "John"}
            putIntLn(x.age)
            putFloatLn(x.height)
            putStringLn(x.name)
            var y int = foo().age
            putIntLn(y)
        }

        
        """
        expect = "30\n177.3\nJohn\n25\n"
        self.assertTrue(TestCodeGen.test(input,expect,526))

    