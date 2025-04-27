import unittest
from TestUtils import TestCodeGen
from AST import *


class CheckCodeGenSuite(unittest.TestCase):
    def test_int_literal(self):
        input = """func main() {putInt(5);};"""
        expect = "5"
        self.assertTrue(TestCodeGen.test(input,expect,501))
    def test_local_var(self):
        input = """func main() {var a int = 20;  putInt(a);};"""
        expect = "20"
        self.assertTrue(TestCodeGen.test(input,expect,502))
    def test_gllobal_var(self):
        input = """var a int = 10; func main() { putInt(a);};"""
        expect = "10"
        self.assertTrue(TestCodeGen.test(input,expect,503))
    def test_int_ast(self):
        input = Program([FuncDecl("main",[],VoidType(),Block([FuncCall("putInt", [IntLiteral(25)])]))])
        expect = "25"
        self.assertTrue(TestCodeGen.test(input,expect,504))
    def test_local_var_ast(self):
        input = Program([FuncDecl("main",[],VoidType(),Block([VarDecl("a",IntType(),IntLiteral(500)),FuncCall("putInt", [Id("a")])]))])
        expect = "500"
        self.assertTrue(TestCodeGen.test(input,expect,505))
    def test_global_var_ast(self):  
        input = Program([VarDecl("a",IntType(),IntLiteral(5000)),FuncDecl("main",[],VoidType(),Block([FuncCall("putInt", [Id("a")])]))])
        expect = "5000"
        self.assertTrue(TestCodeGen.test(input,expect,506))
    
    def test_1(self):
        input = """
        func main() {
            var a int = 5;
            var b int = 10;
            putInt(a + b);
        };"""
        expect = "15"
        self.assertTrue(TestCodeGen.test(input,expect,507))

    def test_2(self):
        input = """
        func main() {
            var a int = 5;
            var b int = 10;
            var c int = 15;
            putInt(a + b + c);
        };"""
        expect = "30"
        self.assertTrue(TestCodeGen.test(input,expect,508))

    def test_3(self):
        input = """
        func main() {
            var a int = 5;
            var b int = 10;
            var c int = 15;
            var d int = 20;
            putInt(a + b + c + d % a);
        };"""
        expect = "30"
        self.assertTrue(TestCodeGen.test(input,expect,509))
    