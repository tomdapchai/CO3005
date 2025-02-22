import unittest
from TestUtils import TestAST
from AST import *

class ASTGenSuite(unittest.TestCase):
    def test_simple_program(self):
        """Simple program: int main() {} """
        input = """func main() {
        var a int = a.c().b(1,2)[4];
        b()[1]
        }
        """
        expect = str(Program([FuncDecl("main",[],VoidType(),Block([VarDecl("x",IntType(),None)]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,300))

    def test_more_complex_program(self):
        """More complex program"""
        input = """var x int ;"""
        expect = str(Program([VarDecl("x",IntType(),None)]))
        self.assertTrue(TestAST.checkASTGen(input,expect,301))
    
    def test_call_without_parameter(self):
        """More complex program"""
        input = """type Person struct {
            name string;
            age int;
        }
        """
        expect = str(Program([StructType("Person",[("name",StringType()),("age",IntType())],[])]))
        self.assertTrue(TestAST.checkASTGen(input,expect,302))
   