import unittest
from TestUtils import TestAST
from AST import *

class ASTGenSuite(unittest.TestCase):
    def test_simple_program(self):
        """Simple program: int main() {} """
        input = """
                type A interface {
                    Add(x,y int, z float);
                    test(a [2]Bike);
                }
                """
        expect = str(Program([InterfaceType("A",[Prototype("Add",[IntType(),IntType(),FloatType()],VoidType()),Prototype("test",[ArrayType([IntLiteral(2)],Id("Bike"))],VoidType())])]))
        print(expect)
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
   