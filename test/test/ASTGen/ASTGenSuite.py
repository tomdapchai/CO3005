"""
 * Initial code for Assignment 1, 2
 * Programming Language Principles
 * Author: Võ Tiến
 * Link FB : https://www.facebook.com/Shiba.Vo.Tien
 * Link Group : https://www.facebook.com/groups/khmt.ktmt.cse.bku
 * Date: 07.01.2025
"""
import unittest
from TestUtils import TestAST
from AST import *
import inspect

##! continue update
class ASTGenSuite(unittest.TestCase):
    def test_026(self):
        input = """
            func foo(){
                a[2].b.c[2] := 1;
            } 
"""
        expect = Program([
            FunctionDecl(Id("foo"), VoidType(), None,[],[
                AssignStmt(ArrayCell(FieldAccess(FieldAccess(ArrayCell(Id("a"),IntLiteral(2)),Id("b")),Id("c")),IntLiteral(2)),":=",IntLiteral(1))])
        ])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

