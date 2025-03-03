import unittest
from TestUtils import TestAST
from AST import *

class ASTGenSuite(unittest.TestCase):
#     def test_simple_program_300(self):
#         input = """func main() {
#         x := 2 * 4; 
#         };"""
#         expect = str(Program([FuncDecl("main",[],VoidType(),Block([Assign(Id("x"),BinaryOp("*",IntLiteral(2),IntLiteral(4)))]))]))
#         self.assertTrue(TestAST.checkASTGen(input,expect,300))

#     def test_more_complex_program_301(self):
#         input = """var a float ;"""
#         expect = str(Program([VarDecl("a",FloatType(),None)]))
#         self.assertTrue(TestAST.checkASTGen(input,expect,301))
    
#     def test_302(self):
#         input = """func main () {
#         var a int;
#         }; 
#         var b int 
        
#         """
#         expect = str(Program([FuncDecl("main",[],VoidType(),Block([VarDecl("a",IntType(), None)])),VarDecl("b",IntType(), None)]))
#         self.assertTrue(TestAST.checkASTGen(input,expect,302))
#     def test_303(self):
#         input = """
#         var a[1][2] float;
#         var a[2] int;
#         """
#         expect = str(
#               Program([
#                 VarDecl("a",ArrayType([IntLiteral(1),IntLiteral(2)],FloatType()),None),
#                 VarDecl("a",ArrayType([IntLiteral(2)],IntType()),None)
#               ])
#         )
#         self.assertTrue(TestAST.checkASTGen(input,expect,303))
        
#     def test_304(self):
#         input = """
#         func main() {
#             foo(1 + a * b, 3);
#         }
#         """
#         expect = str(
#               Program([
#                 FuncDecl("main",[],VoidType(),Block([FuncCall("foo",[BinaryOp("+",IntLiteral(1),BinaryOp("*",Id("a"),Id("b"))),IntLiteral(3)])]))
#               ])
#         )
#         self.assertTrue(TestAST.checkASTGen(input,expect,304))
#     def test_305(self):
#         input = """
#         const x = 5;
#         const y = 6;
#         var Tam = 1 && 2 && c + 3 / 2 - -1;
#         """
#         expect = str(
#               Program([ConstDecl("x",None,IntLiteral(5)),ConstDecl("y",None,IntLiteral(6)),VarDecl("Tam",None,BinaryOp("&&",BinaryOp("&&",IntLiteral(1),IntLiteral(2)),BinaryOp("-",BinaryOp("+",Id("c"),BinaryOp("/",IntLiteral(3),IntLiteral(2))),UnaryOp("-",IntLiteral(1)))))])
#         )
#         self.assertTrue(TestAST.checkASTGen(input,expect,305))
#     def test_306(self):
#         input = """
#         var c boolean;
#         var d boolean = false;
#         var a = x && y;
#         var d = !a;
#         """
#         expect = str(
#               Program([
#                 VarDecl("c",BoolType(),None),
#                 VarDecl("d",BoolType(),BooleanLiteral(False)),
#                 VarDecl("a",None,BinaryOp("&&",Id("x"),Id("y"))),
#                 VarDecl("d",None,UnaryOp("!",Id("a")))
#               ])
#         )
#         self.assertTrue(TestAST.checkASTGen(input,expect,306))
#     def test_307(self):
#         input = """
#         const k = -b - !-!c - ---[2]int{2, 3, 4};  
#         """
#         expect = str(
#               Program([ConstDecl("k",None,BinaryOp("-",BinaryOp("-",UnaryOp("-",Id("b")),UnaryOp("!",UnaryOp("-",UnaryOp("!",Id("c"))))),UnaryOp("-",UnaryOp("-",UnaryOp("-",ArrayLiteral([IntLiteral(2)],IntType(),[IntLiteral(2),IntLiteral(3),IntLiteral(4)]))))))])
#         )
#         self.assertTrue(TestAST.checkASTGen(input,expect,307))
#     def test_308(self):
#         input = """
#         var a float;
#         var a float = 2.47;
#         var a = a + b;
#         var a = a > b;
#         var a = a < b;
#         var a = a >= b;
#         var a = a <= b;
#         var a = a != b;
#         var a = a == b;
#         """
#         expect = str(
#                 Program([
#                     VarDecl("a",FloatType(),None),
#                     VarDecl("a",FloatType(),FloatLiteral(2.47)),
#                     VarDecl("a",None,BinaryOp("+",Id("a"),Id("b"))),
#                     VarDecl("a",None,BinaryOp(">",Id("a"),Id("b"))),
#                     VarDecl("a",None,BinaryOp("<",Id("a"),Id("b"))),
#                     VarDecl("a",None,BinaryOp(">=",Id("a"),Id("b"))),
#                     VarDecl("a",None,BinaryOp("<=",Id("a"),Id("b"))),
#                     VarDecl("a",None,BinaryOp("!=",Id("a"),Id("b"))),
#                     VarDecl("a",None,BinaryOp("==",Id("a"),Id("b")))
#                 ])
#         )
#         self.assertTrue(TestAST.checkASTGen(input,expect,308))
#     def test_309(self):
#         input = """
#         var a string;
#         var b string = "Hello";
#         """
#         expect = str(
#                 Program([
#                     VarDecl("a",StringType(),None),
#                     VarDecl("b",StringType(),StringLiteral("\"Hello\"")),
#                 ])
#         )
#         self.assertTrue(TestAST.checkASTGen(input,expect,309))
#     def test_310(self):
#         input = """
#         var a[1][2][3] Person;
#         """
#         expect = str(
#                 Program([
#                     VarDecl("a",ArrayType([IntLiteral(1),IntLiteral(2),IntLiteral(3)],Id("Person")),None)
#                 ])
#         )
#         self.assertTrue(TestAST.checkASTGen(input,expect,310))
#     def test_311(self):
#         input = """
#         type Calculator interface {
#             Add(x, y int) int;
#             Subtract(a int, b, c int) string
#             SayHello(name string)
#         }
#         """
#         expect = str(
#                 Program([InterfaceType("Calculator",[Prototype("Add",[IntType(),IntType()],IntType()),Prototype("Subtract",[IntType(),IntType(),IntType()],StringType()),Prototype("SayHello",[StringType()],VoidType())])])
#         )
#         self.assertTrue(TestAST.checkASTGen(input,expect,311))
#     def test_312(self):
#         input = """
#         type Calculator interface {
#             Add(x, y int) int;
#             Reset();
#         }
#         """
#         expect = str(
#                 Program([InterfaceType("Calculator",[Prototype("Add",[IntType(),IntType()],IntType()),Prototype("Reset",[],VoidType())])])
#         )
#         self.assertTrue(TestAST.checkASTGen(input,expect,312))
#     def test_313(self):
#         input = """
#         type Person struct {
#             name string;
#             age int;
#         }
#         func main() {
#             p := Person{name: "Tam", age: 24};
#             s := Student{person: p, grade: 1.5};
#             t := Teacher{person: p, salary: 24.7};
#             total := s.grade + t.salary;
#         }
#         """
#         expect = str(
#                 Program([StructType("Person",[("name",StringType()),("age",IntType())],[]),FuncDecl("main",[],VoidType(),Block([Assign(Id("p"),StructLiteral("Person",[("name",StringLiteral("\"Tam\"")),("age",IntLiteral(24))])),Assign(Id("s"),StructLiteral("Student",[("person",Id("p")),("grade",FloatLiteral(1.5))])),Assign(Id("t"),StructLiteral("Teacher",[("person",Id("p")),("salary",FloatLiteral(24.7))])),Assign(Id("total"),BinaryOp("+",FieldAccess(Id("s"),"grade"),FieldAccess(Id("t"),"salary")))]))])
#         )
#         # print(expect)
#         self.assertTrue(TestAST.checkASTGen(input,expect,313))
#     def test_314(self):
#         input = """
#         const k = ID {a : 2}.c[2] + 2[2] + a.foo() + (1).foo(); 
#         """
#         expect = str(
#                 Program([ConstDecl("k",None,BinaryOp("+",BinaryOp("+",BinaryOp("+",ArrayCell(FieldAccess(StructLiteral("ID",[("a",IntLiteral(2))]),"c"),[IntLiteral(2)]),ArrayCell(IntLiteral(2),[IntLiteral(2)])),MethCall(Id("a"),"foo",[])),MethCall(IntLiteral(1),"foo",[])))])
#         )
#         self.assertTrue(TestAST.checkASTGen(input,expect,314))
#     def test_315(self):
#         input = """var flag bool = !true && false * !-!-1 + a(1, 2)[3].c[2].a.d(1)[3][4];"""
#         expect = str(
#                 Program([VarDecl("flag",Id("bool"),BinaryOp("&&",UnaryOp("!",BooleanLiteral(True)),BinaryOp("+",BinaryOp("*",BooleanLiteral(False),UnaryOp("!",UnaryOp("-",UnaryOp("!",UnaryOp("-",IntLiteral(1)))))),ArrayCell(MethCall(FieldAccess(ArrayCell(FieldAccess(ArrayCell(FuncCall("a",[IntLiteral(1),IntLiteral(2)]),[IntLiteral(3)]),"c"),[IntLiteral(2)]),"a"),"d",[IntLiteral(1)]),[IntLiteral(3),IntLiteral(4)]))))])
#         )
#         # print(expect)
#         self.assertTrue(TestAST.checkASTGen(input,expect,315))
#     def test_316(self):
#         input = """
#         func main() {
#         c += 2
#         }
#         """
#         expect = str(
#             Program([FuncDecl("main",[],VoidType(),Block([Assign(Id("c"),BinaryOp("+",Id("c"),IntLiteral(2)))]))])
#         )
#         self.assertTrue(TestAST.checkASTGen(input,expect,316))
#     def test_317(self):
#         input = """
#         var a = b[1];
#         """
#         expect = str(
#             Program([VarDecl("a",None,ArrayCell(Id("b"),[IntLiteral(1)]))])
#         )
#         self.assertTrue(TestAST.checkASTGen(input,expect,317))
#     def test_318(self):
#         input = """
#         func main() {
#         a[1] := b[1][2];
#         }
#         """
#         expect = str(
#             Program([FuncDecl("main",[],VoidType(),Block([Assign(ArrayCell(Id("a"),[IntLiteral(1)]),ArrayCell(Id("b"),[IntLiteral(1),IntLiteral(2)]))]))])
#         )
#         self.assertTrue(TestAST.checkASTGen(input,expect,318))
#     def test_319(self):
#         input = """var a = [1][2][3]int{1,{2,3,4},{Person{Id: name}, 3, {a, b}}};"""
#         expect = str(
#             Program([VarDecl("a",None,ArrayLiteral([IntLiteral(1),IntLiteral(2),IntLiteral(3)],IntType(),[IntLiteral(1),[IntLiteral(2),IntLiteral(3),IntLiteral(4)],[StructLiteral("Person",[("Id",Id("name"))]),IntLiteral(3),[Id("a"),Id("b")]]]))])
#         )
#         self.assertTrue(TestAST.checkASTGen(input,expect,319))
#     def test_320(self):
#         input = """var arr2 = [2]float{"a", "b"};"""
#         expect = str(
#             Program([VarDecl("arr2",None,ArrayLiteral([IntLiteral(2)],FloatType(),[StringLiteral("\"a\""),StringLiteral("\"b\"")]))])
#         )
#         self.assertTrue(TestAST.checkASTGen(input,expect,320))
#     def test_321(self):
#         input = """func Add() {
#         if (z < 0) { z := -z; } else if (z > 0) { 
#         z += 1 
#         } else { 
#         z := 0 
#         }
#         }
#         """
#         expect = str(
#             Program([FuncDecl("Add",[],VoidType(),Block([If(BinaryOp("<",Id("z"),IntLiteral(0)),Block([Assign(Id("z"),UnaryOp("-",Id("z")))]),If(BinaryOp(">",Id("z"),IntLiteral(0)),Block([Assign(Id("z"),BinaryOp("+",Id("z"),IntLiteral(1)))]),Block([Assign(Id("z"),IntLiteral(0))])))]))])
#         )
#         self.assertTrue(TestAST.checkASTGen(input,expect,321))
#     def test_322(self):
#         input = """func Add() {
#         if (a > 5) { 
#             if (a < 10) { a := a * 2; }
#           };
#         }
#         """
#         expect = str(
#             Program([FuncDecl("Add",[],VoidType(),Block([If(BinaryOp(">",Id("a"),IntLiteral(5)),Block([If(BinaryOp("<",Id("a"),IntLiteral(10)),Block([Assign(Id("a"),BinaryOp("*",Id("a"),IntLiteral(2)))]),None)]),None)]))])
#         )
#         self.assertTrue(TestAST.checkASTGen(input,expect,322))
#     def test_323(self):
#         input = """func Add() {
#             if (b > 0 && b < 10 || b == 15) { b := b / 2; };
#         }
#         """
#         expect = str(
#             Program([FuncDecl("Add",[],VoidType(),Block([If(BinaryOp("||",BinaryOp("&&",BinaryOp(">",Id("b"),IntLiteral(0)),BinaryOp("<",Id("b"),IntLiteral(10))),BinaryOp("==",Id("b"),IntLiteral(15))),Block([Assign(Id("b"),BinaryOp("/",Id("b"),IntLiteral(2)))]),None)]))]))
#         self.assertTrue(TestAST.checkASTGen(input,expect,323))
#     def test_324(self):
#         input = """
#         func Add() {
#         if (arr[0] > 0) { 
#         arr[0] := arr[0] * 2; 
#         } else {
#             arr[0] := 0;
#         }
#         }
# """
#         expect = str(
#             Program([FuncDecl("Add",[],VoidType(),Block([If(BinaryOp(">",ArrayCell(Id("arr"),[IntLiteral(0)]),IntLiteral(0)),Block([Assign(ArrayCell(Id("arr"),[IntLiteral(0)]),BinaryOp("*",ArrayCell(Id("arr"),[IntLiteral(0)]),IntLiteral(2)))]),Block([Assign(ArrayCell(Id("arr"),[IntLiteral(0)]),IntLiteral(0))]))]))])
#         )
#         self.assertTrue(TestAST.checkASTGen(input,expect,324))
#     def test_325(self):
#         input = """
#         func Add() {
#             if (person.age > 18) {
#           person.isAdult := true; 
#           };
#         }
# """
#         expect = str(
#             Program([FuncDecl("Add",[],VoidType(),Block([If(BinaryOp(">",FieldAccess(Id("person"),"age"),IntLiteral(18)),Block([Assign(FieldAccess(Id("person"),"isAdult"),BooleanLiteral(True))]),None)]))])
#         )
#         self.assertTrue(TestAST.checkASTGen(input,expect,325))
#     def test_326(self):
#         input = """
#     func Add() {
#     for i := 0; i < 10; i += 1 {  
#         var x int = i * 2;
#         }
#     }
#         """
#         expect = str(
#             Program([FuncDecl("Add",[],VoidType(),Block([ForStep(Assign(Id("i"),IntLiteral(0)),BinaryOp("<",Id("i"),IntLiteral(10)),Assign(Id("i"),BinaryOp("+",Id("i"),IntLiteral(1))),Block([VarDecl("x",IntType(),BinaryOp("*",Id("i"),IntLiteral(2)))]))]))])
#         )
#         self.assertTrue(TestAST.checkASTGen(input,expect,326))
#     def test_327(self):
#         input = """var arr = [3]int{1, 2, 3}; 
#         func Add() {
#         for index, value := range arr { 
#          x := x + value;
#            }
#         }
#            """
#         expect = str(
#             Program([VarDecl("arr",None,ArrayLiteral([IntLiteral(3)],IntType(),[IntLiteral(1),IntLiteral(2),IntLiteral(3)])),FuncDecl("Add",[],VoidType(),Block([ForEach(Id("index"),Id("value"),Id("arr"),Block([Assign(Id("x"),BinaryOp("+",Id("x"),Id("value")))]))]))])
#         )
#         # print(expect)
#         self.assertTrue(TestAST.checkASTGen(input,expect,327))
#     def test_328(self):
#         input = """var arr = [3]int{1, 2, 3}; 
#         func Add() {
#         for _, value := range arr { 
#             x += value;
#            };
#         }
#         """
#         expect = str(
#             Program([VarDecl("arr",None,ArrayLiteral([IntLiteral(3)],IntType(),[IntLiteral(1),IntLiteral(2),IntLiteral(3)])),FuncDecl("Add",[],VoidType(),Block([ForEach(Id("_"),Id("value"),Id("arr"),Block([Assign(Id("x"),BinaryOp("+",Id("x"),Id("value")))]))]))])
#         )
#         self.assertTrue(TestAST.checkASTGen(input,expect,328))
#     def test_329(self):
#         input = """func Add() {for i := 0; i < 10; i += 1 { if (i == 5) { break; }; };};"""
#         expect = str(
#             Program([FuncDecl("Add",[],VoidType(),Block([ForStep(Assign(Id("i"),IntLiteral(0)),BinaryOp("<",Id("i"),IntLiteral(10)),Assign(Id("i"),BinaryOp("+",Id("i"),IntLiteral(1))),Block([If(BinaryOp("==",Id("i"),IntLiteral(5)),Block([Break()]),None)]))]))])
                
#         )
#         self.assertTrue(TestAST.checkASTGen(input,expect,329))
#     def test_330(self):
#         input = """
#                                     func Add() {
#                                         for var i [2]int = 0; foo().a.b(); i := 1 {
#                                             return; 
#                                         }
#                                     };"""
#         expect = str(
#             Program([FuncDecl("Add",[],VoidType(),Block([ForStep(VarDecl("i",ArrayType([IntLiteral(2)],IntType()),IntLiteral(0)),MethCall(FieldAccess(FuncCall("foo",[]),"a"),"b",[]),Assign(Id("i"),IntLiteral(1)),Block([Return(None)]))]))])
#         )
#         self.assertTrue(TestAST.checkASTGen(input,expect,330))
#     def test_331(self):
#         input = """var result = add(5 + 5, 7 * (1 + -!2), Person{ID: name});"""
#         expect = str(
#             Program([VarDecl("result",None,FuncCall("add",[BinaryOp("+",IntLiteral(5),IntLiteral(5)),BinaryOp("*",IntLiteral(7),BinaryOp("+",IntLiteral(1),UnaryOp("-",UnaryOp("!",IntLiteral(2))))),StructLiteral("Person",[("ID",Id("name"))])]))])
#         )
#         self.assertTrue(TestAST.checkASTGen(input,expect,331))
#     def test_332(self):
#         input = """
#         func main() {
#             a := [1][2]int{1,2, Id, 3, Person{name: "John", age: 25}};
#         }
#         """
#         expect = str(
#             Program([
#                 FuncDecl("main",[],VoidType(),Block([
#                     Assign(Id("a"),
#                            ArrayLiteral([IntLiteral(1),IntLiteral(2)],IntType(),
#                                         [IntLiteral(1),IntLiteral(2),Id("Id"),IntLiteral(3),StructLiteral("Person",[("name",StringLiteral("\"John\"")),("age",IntLiteral(25))])]))
#                 ]))
#             ])
#         )
#         self.assertTrue(TestAST.checkASTGen(input,expect,332))
#     def test_333(self):
#         input = """var result = a.add(5, 7, b(), c.a(1,2,3), a[1].c(2));"""
#         expect = str(
#             Program([VarDecl("result",None,MethCall(Id("a"),"add",[IntLiteral(5),IntLiteral(7),FuncCall("b",[]),MethCall(Id("c"),"a",[IntLiteral(1),IntLiteral(2),IntLiteral(3)]),MethCall(ArrayCell(Id("a"),[IntLiteral(1)]),"c",[IntLiteral(2)])]))])
#         )
#         self.assertTrue(TestAST.checkASTGen(input,expect,333))
#     def test_334(self):
#         input = """
#         const MAX_VALUE = 100;
#         var counter int = 0;

#         func increment() int {
#             counter += 1;
#             return counter;
#         }

#         var result int = increment() + MAX_VALUE;
#         """
#         expect = str(
#             Program([ConstDecl("MAX_VALUE",None,IntLiteral(100)),VarDecl("counter",IntType(),IntLiteral(0)),FuncDecl("increment",[],IntType(),Block([Assign(Id("counter"),BinaryOp("+",Id("counter"),IntLiteral(1))),Return(Id("counter"))])),VarDecl("result",IntType(),BinaryOp("+",FuncCall("increment",[]),Id("MAX_VALUE")))])
#         )
#         self.assertTrue(TestAST.checkASTGen(input,expect,334))
#     def test_335(self):
#         input = """
#         type Point struct {
#             x int;
#             y int;
#         }

#         func main() {
#             var p Point = Point{x: 5, y: 10};
#         p.x += 5;

#         var area int = p.x * p.y;
#         }
        
#         """
#         expect = str(
#             Program([StructType("Point",[("x",IntType()),("y",IntType())],[]),FuncDecl("main",[],VoidType(),Block([VarDecl("p",Id("Point"),StructLiteral("Point",[("x",IntLiteral(5)),("y",IntLiteral(10))])),Assign(FieldAccess(Id("p"),"x"),BinaryOp("+",FieldAccess(Id("p"),"x"),IntLiteral(5))),VarDecl("area",IntType(),BinaryOp("*",FieldAccess(Id("p"),"x"),FieldAccess(Id("p"),"y")))]))]))
#         self.assertTrue(TestAST.checkASTGen(input,expect,335))
#     def test_336(self):
#         input = """
        
#             type Calculator interface {
#             Add(x int) int;
#         }

#         type MyCalc struct {
#             value int;
#         }

#         func (c MyCalc) Add(x int) int {
#             c.value += x;
#             return c.value;

#         var calc Calculator = MyCalc{value: 0};
#         calc.Add(5);
#         }
        
#         """
#         expect = str(
#             Program([InterfaceType("Calculator",[Prototype("Add",[IntType()],IntType())]),StructType("MyCalc",[("value",IntType())],[]),MethodDecl("c",Id("MyCalc"),FuncDecl("Add",[ParamDecl("x",IntType())],IntType(),Block([Assign(FieldAccess(Id("c"),"value"),BinaryOp("+",FieldAccess(Id("c"),"value"),Id("x"))),Return(FieldAccess(Id("c"),"value")),VarDecl("calc",Id("Calculator"),StructLiteral("MyCalc",[("value",IntLiteral(0))])),MethCall(Id("calc"),"Add",[IntLiteral(5)])])))])
#         )
#         self.assertTrue(TestAST.checkASTGen(input,expect,336))
#     def test_337(self):
#         input = """
#        var arr = [3]int{1, 2, 3};
#        var sum int = arr[0] + arr[1] + arr[2];
#        """
#         expect = str(
#             Program([VarDecl("arr",None,ArrayLiteral([IntLiteral(3)],IntType(),[IntLiteral(1),IntLiteral(2),IntLiteral(3)])),VarDecl("sum",IntType(),BinaryOp("+",BinaryOp("+",ArrayCell(Id("arr"),[IntLiteral(0)]),ArrayCell(Id("arr"),[IntLiteral(1)])),ArrayCell(Id("arr"),[IntLiteral(2)])))])
#         )
#         self.assertTrue(TestAST.checkASTGen(input,expect,337))
#     def test_338(self):
#         input = """
#         type Person struct {
#             name string;
#             age int;
#         }

#         func main() {
#         var people [2]Person;
#         people[0] := Person{name: "Alice", age: 30};
#         people[1] := Person{name: "Bob", age: 25};

#         var aliceAge int = people[0].age;
#         }
        
#         """
#         expect = str(
#             Program([StructType("Person",[("name",StringType()),("age",IntType())],[]),FuncDecl("main",[],VoidType(),Block([VarDecl("people",ArrayType([IntLiteral(2)],Id("Person")),None),Assign(ArrayCell(Id("people"),[IntLiteral(0)]),StructLiteral("Person",[("name",StringLiteral("\"Alice\"")),("age",IntLiteral(30))])),Assign(ArrayCell(Id("people"),[IntLiteral(1)]),StructLiteral("Person",[("name",StringLiteral("\"Bob\"")),("age",IntLiteral(25))])),VarDecl("aliceAge",IntType(),FieldAccess(ArrayCell(Id("people"),[IntLiteral(0)]),"age"))]))]))
#         self.assertTrue(TestAST.checkASTGen(input,expect,338))
#     def test_339(self):
#         input = """
#         func multiply(x int, y int) int {
#             return x * y;
#         }

#         const FACTOR = 2;
#         var result int = multiply(5, 10) * FACTOR;
#         """
#         expect = str(
#             Program([FuncDecl("multiply",[ParamDecl("x",IntType()),ParamDecl("y",IntType())],IntType(),Block([Return(BinaryOp("*",Id("x"),Id("y")))])),ConstDecl("FACTOR",None,IntLiteral(2)),VarDecl("result",IntType(),BinaryOp("*",FuncCall("multiply",[IntLiteral(5),IntLiteral(10)]),Id("FACTOR")))])
#         )
#         self.assertTrue(TestAST.checkASTGen(input,expect,339))
#     def test_340(self):
#         input = """
#         type Rectangle struct {
#             width int;
#             height int;
#         }

#         func (r Rectangle) area() int {
#             return r.width * r.height;
#         }

#         var rect Rectangle = Rectangle{width: 10, height: 5};
#         var rectArea int = rect.area();
#         """
#         expect = str(
#             Program([StructType("Rectangle",[("width",IntType()),("height",IntType())],[]),MethodDecl("r",Id("Rectangle"),FuncDecl("area",[],IntType(),Block([Return(BinaryOp("*",FieldAccess(Id("r"),"width"),FieldAccess(Id("r"),"height")))]))),VarDecl("rect",Id("Rectangle"),StructLiteral("Rectangle",[("width",IntLiteral(10)),("height",IntLiteral(5))])),VarDecl("rectArea",IntType(),MethCall(Id("rect"),"area",[]))])
#         )
#         self.assertTrue(TestAST.checkASTGen(input,expect,340))
#     def test_341(self):
#         input = """
#         type Circle struct {
#             radius float;
#         }

#         func (c Circle) circumference() float {
#             const PI = 3.14159;
#             return 2 * PI * c.radius;
#         }

#         var myCircle Circle = Circle{radius: 7.0};
#         var c float = myCircle.circumference();
#         """
#         expect = str(
#             Program([StructType("Circle",[("radius",FloatType())],[]),MethodDecl("c",Id("Circle"),FuncDecl("circumference",[],FloatType(),Block([ConstDecl("PI",None,FloatLiteral(3.14159)),Return(BinaryOp("*",BinaryOp("*",IntLiteral(2),Id("PI")),FieldAccess(Id("c"),"radius")))]))),VarDecl("myCircle",Id("Circle"),StructLiteral("Circle",[("radius",FloatLiteral(7.0))])),VarDecl("c",FloatType(),MethCall(Id("myCircle"),"circumference",[]))])
#         )
#         self.assertTrue(TestAST.checkASTGen(input,expect,341))
#     def test_342(self):
#         input = """
        
#             type Point struct {
#             x int;
#             y int;
#         }
        
#         func (p Point) move(dx int, dy int) {
#             p.x := p.x + dx;
#             p.y := p.y + dy;
#         }

#         func Add() {
#         var myPoint Point = Point{x: 2, y: 3};
#         myPoint.move(5, -2);
#         }
        
#         """
#         expect = str(
#             Program([StructType("Point",[("x",IntType()),("y",IntType())],[]),MethodDecl("p",Id("Point"),FuncDecl("move",[ParamDecl("dx",IntType()),ParamDecl("dy",IntType())],VoidType(),Block([Assign(FieldAccess(Id("p"),"x"),BinaryOp("+",FieldAccess(Id("p"),"x"),Id("dx"))),Assign(FieldAccess(Id("p"),"y"),BinaryOp("+",FieldAccess(Id("p"),"y"),Id("dy")))]))),FuncDecl("Add",[],VoidType(),Block([VarDecl("myPoint",Id("Point"),StructLiteral("Point",[("x",IntLiteral(2)),("y",IntLiteral(3))])),MethCall(Id("myPoint"),"move",[IntLiteral(5),UnaryOp("-",IntLiteral(2))])]))])
#         )
        
#         # print(expect)
#         self.assertTrue(TestAST.checkASTGen(input,expect,342))
#     def test_343(self):
#         input = """
#         type Person struct {
#             name string;
#             age int;
#         }

#         func (p Person) greet() string {
#             return "Hello, my name is " + p.name + " and I am " + toString(p.age) + " years old.";
#         }

#         var someone Person = Person{name: "Charlie", age: 42};
#         var greeting string = someone.greet();
#         """
#         expect = str(
#             Program([StructType("Person",[("name",StringType()),("age",IntType())],[]),MethodDecl("p",Id("Person"),FuncDecl("greet",[],StringType(),Block([Return(BinaryOp("+",BinaryOp("+",BinaryOp("+",BinaryOp("+",StringLiteral("\"Hello, my name is \""),FieldAccess(Id("p"),"name")),StringLiteral("\" and I am \"")),FuncCall("toString",[FieldAccess(Id("p"),"age")])),StringLiteral("\" years old.\"")))]))),VarDecl("someone",Id("Person"),StructLiteral("Person",[("name",StringLiteral("\"Charlie\"")),("age",IntLiteral(42))])),VarDecl("greeting",StringType(),MethCall(Id("someone"),"greet",[]))])
#         )
#         self.assertTrue(TestAST.checkASTGen(input,expect,343))
#     def test_344(self):
#         input = """
#         type Rectangle struct {
#             width int;
#             height int;
#         }

#         func (r Rectangle) scale(factor int) {
#             r.width := r.width * factor;
#             r.height := r.height * factor;
#         }

#         var rect Rectangle = Rectangle{width: 4, height: 6};
#         """
#         expect = str(
#             Program([StructType("Rectangle",[("width",IntType()),("height",IntType())],[]),MethodDecl("r",Id("Rectangle"),FuncDecl("scale",[ParamDecl("factor",IntType())],VoidType(),Block([Assign(FieldAccess(Id("r"),"width"),BinaryOp("*",FieldAccess(Id("r"),"width"),Id("factor"))),Assign(FieldAccess(Id("r"),"height"),BinaryOp("*",FieldAccess(Id("r"),"height"),Id("factor")))]))),VarDecl("rect",Id("Rectangle"),StructLiteral("Rectangle",[("width",IntLiteral(4)),("height",IntLiteral(6))]))])
#         )
#         self.assertTrue(TestAST.checkASTGen(input, expect, 344))

#     def test_345(self):
#         input = """
#         type Car struct {
#             make string;
#             model string;
#             year int;
#         }

#         func (c Car) description() string {
#             return stri(c.year) + " " + c.make + " " + c.model;
#         }

#         var myCar Car = Car{make: "Toyota", model: "Camry", year: 2023};
#         var carDesc string = myCar.description();
#         """
#         expect = str(
#             Program([StructType("Car",[("make",StringType()),("model",StringType()),("year",IntType())],[]),MethodDecl("c",Id("Car"),FuncDecl("description",[],StringType(),Block([Return(BinaryOp("+",BinaryOp("+",BinaryOp("+",BinaryOp("+",FuncCall("stri",[FieldAccess(Id("c"),"year")]),StringLiteral("\" \"")),FieldAccess(Id("c"),"make")),StringLiteral("\" \"")),FieldAccess(Id("c"),"model")))]))),VarDecl("myCar",Id("Car"),StructLiteral("Car",[("make",StringLiteral("\"Toyota\"")),("model",StringLiteral("\"Camry\"")),("year",IntLiteral(2023))])),VarDecl("carDesc",StringType(),MethCall(Id("myCar"),"description",[]))])
#         )
#         self.assertTrue(TestAST.checkASTGen(input, expect, 345))

#     def test_346(self):
#         input = """func Add() {
#             if (x > 10) { 
#         x -= 5; 
#         }
#         }
#         """
#         expect = str(
#             Program([FuncDecl("Add",[],VoidType(),Block([If(BinaryOp(">",Id("x"),IntLiteral(10)),Block([Assign(Id("x"),BinaryOp("-",Id("x"),IntLiteral(5)))]),None)]))])
#         )
#         self.assertTrue(TestAST.checkASTGen(input, expect, 346))
    
#     def test_347(self):
#         input = """func Add() {if (y == 0) { 
#         y := 1 
#         } else { 
#             y *= 2 
#         }
#         };"""
#         expect = str(
#             Program([FuncDecl("Add",[],VoidType(),Block([If(BinaryOp("==",Id("y"),IntLiteral(0)),Block([Assign(Id("y"),IntLiteral(1))]),Block([Assign(Id("y"),BinaryOp("*",Id("y"),IntLiteral(2)))]))]))])
#         )
#         self.assertTrue(TestAST.checkASTGen(input, expect, 347))
#     def test_348(self):
#         input = """func Add() {
#         if (a > 5) { 
#             if (a < 10) { a := a * 2; }
#           };
#         }
#         """
#         expect = str(
#             Program([FuncDecl("Add",[],VoidType(),Block([If(BinaryOp(">",Id("a"),IntLiteral(5)),Block([If(BinaryOp("<",Id("a"),IntLiteral(10)),Block([Assign(Id("a"),BinaryOp("*",Id("a"),IntLiteral(2)))]),None)]),None)]))])
#         )
#         self.assertTrue(TestAST.checkASTGen(input, expect, 348))
#     def test_349(self):
#         input = """func Add(x, y int, b float) {
#             if (b > 0 && b < 10 || b == 15) { b := b / 2; };
#         }
#         """
#         expect = str(
#             Program([FuncDecl("Add",[ParamDecl("x",IntType()),ParamDecl("y",IntType()),ParamDecl("b",FloatType())],VoidType(),Block([If(BinaryOp("||",BinaryOp("&&",BinaryOp(">",Id("b"),IntLiteral(0)),BinaryOp("<",Id("b"),IntLiteral(10))),BinaryOp("==",Id("b"),IntLiteral(15))),Block([Assign(Id("b"),BinaryOp("/",Id("b"),IntLiteral(2)))]),None)]))])
#         )
#         self.assertTrue(TestAST.checkASTGen(input, expect, 349))

#     def test_350(self):
#         input = """
#         func Add() {
#         if (arr[0] > 0) { 
#         arr[0] := arr[0] * 2; 
#         } else {
#             arr[0] := 0;
#         }
#         }
# """
#         expect = str(
#             Program([FuncDecl("Add",[],VoidType(),Block([If(BinaryOp(">",ArrayCell(Id("arr"),[IntLiteral(0)]),IntLiteral(0)),Block([Assign(ArrayCell(Id("arr"),[IntLiteral(0)]),BinaryOp("*",ArrayCell(Id("arr"),[IntLiteral(0)]),IntLiteral(2)))]),Block([Assign(ArrayCell(Id("arr"),[IntLiteral(0)]),IntLiteral(0))]))]))])
#         )
#         self.assertTrue(TestAST.checkASTGen(input, expect, 350))
    def test_351(self):
        input = """
        func binSearch(arr [100]int, x int) int {
            l := 0;
            h := arr.length() - 1;
            for l <= h {
                m := l + (h - l) / 2;
                if (arr[m] == x) {
                    return m;
                }
                if (arr[m] < x) {
                    l := m + 1;
                } else {
                    h := m - 1;
                }
            }
            return -1;
        }
        """
        expect = str(
            Program([FuncDecl("binSearch",[ParamDecl("arr",ArrayType([IntLiteral(100)],IntType())),ParamDecl("x",IntType())],IntType(),Block([Assign(Id("l"),IntLiteral(0)),Assign(Id("h"),BinaryOp("-",MethCall(Id("arr"),"length",[]),IntLiteral(1))),ForBasic(BinaryOp("<=",Id("l"),Id("h")),Block([Assign(Id("m"),BinaryOp("+",Id("l"),BinaryOp("/",BinaryOp("-",Id("h"),Id("l")),IntLiteral(2)))),If(BinaryOp("==",ArrayCell(Id("arr"),[Id("m")]),Id("x")),Block([Return(Id("m"))]),None),If(BinaryOp("<",ArrayCell(Id("arr"),[Id("m")]),Id("x")),Block([Assign(Id("l"),BinaryOp("+",Id("m"),IntLiteral(1)))]),Block([Assign(Id("h"),BinaryOp("-",Id("m"),IntLiteral(1)))]))])),Return(UnaryOp("-",IntLiteral(1)))]))])
        )
        self.assertTrue(TestAST.checkASTGen(input, expect, 351))
    def test_352(self):
        input = """
        func Add() {
            if (person.age > 18) {
          person.isAdult := true; 
          };
        }
"""
        expect = str(
            Program([FuncDecl("Add",[],VoidType(),Block([If(BinaryOp(">",FieldAccess(Id("person"),"age"),IntLiteral(18)),Block([Assign(FieldAccess(Id("person"),"isAdult"),BooleanLiteral(True))]),None)]))])
        )
        self.assertTrue(TestAST.checkASTGen(input, expect, 352))
    def test_353(self):
        input = """var a = 10 % 3 * Person{Id: test}.Id[3].d(2, 3)[4].d.e.f();"""
        expect = str(
            Program([VarDecl("a",None,BinaryOp("*",BinaryOp("%",IntLiteral(10),IntLiteral(3)),MethCall(FieldAccess(FieldAccess(ArrayCell(MethCall(ArrayCell(FieldAccess(StructLiteral("Person",[("Id",Id("test"))]),"Id"),[IntLiteral(3)]),"d",[IntLiteral(2),IntLiteral(3)]),[IntLiteral(4)]),"d"),"e"),"f",[])))])
        )
        self.assertTrue(TestAST.checkASTGen(input, expect, 353))
    def test_354(self):
        input = """
        const TEST = 10;
        var arr [5]int;
        var a2 [TEST]string;
        
        func main() {
            arr := [TEST]int{1, 2, 3}
            arr[a+b-c*(11%11+1||(d&&(!c)))] /= 23;
        }
        
        """
        expect = str(
            Program([ConstDecl("TEST",None,IntLiteral(10)),VarDecl("arr",ArrayType([IntLiteral(5)],IntType()),None),VarDecl("a2",ArrayType([Id("TEST")],StringType()),None),FuncDecl("main",[],VoidType(),Block([Assign(Id("arr"),ArrayLiteral([Id("TEST")],IntType(),[IntLiteral(1),IntLiteral(2),IntLiteral(3)])),Assign(ArrayCell(Id("arr"),[BinaryOp("-",BinaryOp("+",Id("a"),Id("b")),BinaryOp("*",Id("c"),BinaryOp("||",BinaryOp("+",BinaryOp("%",IntLiteral(11),IntLiteral(11)),IntLiteral(1)),BinaryOp("&&",Id("d"),Id("c")))))]),BinaryOp("/",ArrayCell(Id("arr"),[BinaryOp("-",BinaryOp("+",Id("a"),Id("b")),BinaryOp("*",Id("c"),BinaryOp("||",BinaryOp("+",BinaryOp("%",IntLiteral(11),IntLiteral(11)),IntLiteral(1)),BinaryOp("&&",Id("d"),Id("c")))))]),IntLiteral(23)))]))])
        )
        self.assertTrue(TestAST.checkASTGen(input, expect, 354))
    def test_355(self):
        input = """
        func mergeSort(arr [100]int) {
            n := len(arr);
            if (n < 2) {
                return;
            }
            mid := n / 2;
            left := [mid]int{1,2,3};
            remain := n - mid;
            right := [remain]int{1,2,3};
            for i := 0; i < mid; i += 1 {
                left[i] := arr[i];
            }
            for i := mid; i < n; i += 1 {
                right[i - mid] := arr[i];
            }
            mergeSort(left);
            mergeSort(right);
            merge(arr, left, right);
        }
        """
        expect = "Program([FuncDecl(mergeSort,[ParDecl(arr,ArrayType(IntType,[IntLiteral(100)]))],VoidType,Block([Assign(Id(n),FuncCall(len,[Id(arr)])),If(BinaryOp(Id(n),<,IntLiteral(2)),Block([Return()])),Assign(Id(mid),BinaryOp(Id(n),/,IntLiteral(2))),Assign(Id(left),ArrayLiteral([Id(mid)],IntType,[IntLiteral(1),IntLiteral(2),IntLiteral(3)])),Assign(Id(remain),BinaryOp(Id(n),-,Id(mid))),Assign(Id(right),ArrayLiteral([Id(remain)],IntType,[IntLiteral(1),IntLiteral(2),IntLiteral(3)])),For(Assign(Id(i),IntLiteral(0)),BinaryOp(Id(i),<,Id(mid)),Assign(Id(i),BinaryOp(Id(i),+,IntLiteral(1))),Block([Assign(ArrayCell(Id(left),[Id(i)]),ArrayCell(Id(arr),[Id(i)]))])),For(Assign(Id(i),Id(mid)),BinaryOp(Id(i),<,Id(n)),Assign(Id(i),BinaryOp(Id(i),+,IntLiteral(1))),Block([Assign(ArrayCell(Id(right),[BinaryOp(Id(i),-,Id(mid))]),ArrayCell(Id(arr),[Id(i)]))])),FuncCall(mergeSort,[Id(left)]),FuncCall(mergeSort,[Id(right)]),FuncCall(merge,[Id(arr),Id(left),Id(right)])]))])"
        self.assertTrue(TestAST.checkASTGen(input, expect, 355))
    def test_356(self):
        input = """
        func quickSort(arr [100]int, low int, high int) {
            if (low < high) {
                pi := partition(arr, low, high);
                quickSort(arr, low, pi - 1);
                quickSort(arr, pi + 1, high);
            }
        }
        func partition(arr [100]int, low int, high int) int {
            pivot := arr[high];
            i := low - 1;
            for j := low; j < high; j += 1 {
                if (arr[j] < pivot) {
                    i += 1;
                    swap(arr, i, j);
                }
            }
            swap(arr, i + 1, high);
            return i + 1;
        }
        """
        expect = "Program([FuncDecl(quickSort,[ParDecl(arr,ArrayType(IntType,[IntLiteral(100)])),ParDecl(low,IntType),ParDecl(high,IntType)],VoidType,Block([If(BinaryOp(Id(low),<,Id(high)),Block([Assign(Id(pi),FuncCall(partition,[Id(arr),Id(low),Id(high)])),FuncCall(quickSort,[Id(arr),Id(low),BinaryOp(Id(pi),-,IntLiteral(1))]),FuncCall(quickSort,[Id(arr),BinaryOp(Id(pi),+,IntLiteral(1)),Id(high)])]))])),FuncDecl(partition,[ParDecl(arr,ArrayType(IntType,[IntLiteral(100)])),ParDecl(low,IntType),ParDecl(high,IntType)],IntType,Block([Assign(Id(pivot),ArrayCell(Id(arr),[Id(high)])),Assign(Id(i),BinaryOp(Id(low),-,IntLiteral(1))),For(Assign(Id(j),Id(low)),BinaryOp(Id(j),<,Id(high)),Assign(Id(j),BinaryOp(Id(j),+,IntLiteral(1))),Block([If(BinaryOp(ArrayCell(Id(arr),[Id(j)]),<,Id(pivot)),Block([Assign(Id(i),BinaryOp(Id(i),+,IntLiteral(1))),FuncCall(swap,[Id(arr),Id(i),Id(j)])]))])),FuncCall(swap,[Id(arr),BinaryOp(Id(i),+,IntLiteral(1)),Id(high)]),Return(BinaryOp(Id(i),+,IntLiteral(1)))]))])"
        self.assertTrue(TestAST.checkASTGen(input, expect, 356))
    def test_357(self):
        input = """
        func complexFunc(a int, b float, c string, d boolean, e [5]int, f [3][3]float, g Person) {
            putInt(a);
            putFloat(b);
            putString(c);
            putBool(d);
            putInt(e[0]);
            putFloat(f[0][0]);
            putString(g.name);
            putInt(g.age);
        }
        """
        expect = "Program([FuncDecl(complexFunc,[ParDecl(a,IntType),ParDecl(b,FloatType),ParDecl(c,StringType),ParDecl(d,BoolType),ParDecl(e,ArrayType(IntType,[IntLiteral(5)])),ParDecl(f,ArrayType(FloatType,[IntLiteral(3),IntLiteral(3)])),ParDecl(g,Id(Person))],VoidType,Block([FuncCall(putInt,[Id(a)]),FuncCall(putFloat,[Id(b)]),FuncCall(putString,[Id(c)]),FuncCall(putBool,[Id(d)]),FuncCall(putInt,[ArrayCell(Id(e),[IntLiteral(0)])]),FuncCall(putFloat,[ArrayCell(Id(f),[IntLiteral(0),IntLiteral(0)])]),FuncCall(putString,[FieldAccess(Id(g),name)]),FuncCall(putInt,[FieldAccess(Id(g),age)])]))])"
        self.assertTrue(TestAST.checkASTGen(input, expect, 357))
    def test_358(self):
        input = """
        func (p Person) complexMethod(a int, b float, c string, d boolean, e [5]int, f [3][3]float, g Person) {
            putInt(a);
            putFloat(b);
            putString(c);
            putBool(d);
            putInt(e[0]);
            putFloat(f[0][0]);
            putString(g.name);
            putInt(g.age);
        }
        """
        expect = "Program([MethodDecl(p,Id(Person),FuncDecl(complexMethod,[ParDecl(a,IntType),ParDecl(b,FloatType),ParDecl(c,StringType),ParDecl(d,BoolType),ParDecl(e,ArrayType(IntType,[IntLiteral(5)])),ParDecl(f,ArrayType(FloatType,[IntLiteral(3),IntLiteral(3)])),ParDecl(g,Id(Person))],VoidType,Block([FuncCall(putInt,[Id(a)]),FuncCall(putFloat,[Id(b)]),FuncCall(putString,[Id(c)]),FuncCall(putBool,[Id(d)]),FuncCall(putInt,[ArrayCell(Id(e),[IntLiteral(0)])]),FuncCall(putFloat,[ArrayCell(Id(f),[IntLiteral(0),IntLiteral(0)])]),FuncCall(putString,[FieldAccess(Id(g),name)]),FuncCall(putInt,[FieldAccess(Id(g),age)])])))])"
        self.assertTrue(TestAST.checkASTGen(input, expect, 358))
    def test_359(self):
        input = """
        func main() {
            a := [5]int{1,2,3,4,5};
            b := [3][3]float{1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0};
            c := Person{name: "John", age: 25};
        }
        """
        expect = "Program([FuncDecl(main,[],VoidType,Block([Assign(Id(a),ArrayLiteral([IntLiteral(5)],IntType,[IntLiteral(1),IntLiteral(2),IntLiteral(3),IntLiteral(4),IntLiteral(5)])),Assign(Id(b),ArrayLiteral([IntLiteral(3),IntLiteral(3)],FloatType,[FloatLiteral(1.0),FloatLiteral(2.0),FloatLiteral(3.0),FloatLiteral(4.0),FloatLiteral(5.0),FloatLiteral(6.0),FloatLiteral(7.0),FloatLiteral(8.0),FloatLiteral(9.0)])),Assign(Id(c),StructLiteral(Person,[(name,StringLiteral(\"John\")),(age,IntLiteral(25))]))]))])"
        self.assertTrue(TestAST.checkASTGen(input, expect, 359))
    # def test_360(self):
    #     input = """
    #     func main() {
    #         a := [5]int{1,2,3,4,5};
    #         b := [3][3]float{1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0};
    #         c := Person{name: "John", age: 25};
    #         d := [5]Person{Person{name: "John", age: 25}, Person{name: "John", age: 25}, Person{name: "John", age: 25}, Person{name: "John", age: 25}, Person{name: "John", age: 25}};
    #     }
    #     """
    #     expect = "Program([FuncDecl(main,[],VoidType,Block([Assign(Id(a),ArrayLiteral([IntLiteral(5)],IntType,[IntLiteral(1),IntLiteral(2),IntLiteral(3),IntLiteral(4),IntLiteral(5)])),Assign(Id(b),ArrayLiteral([IntLiteral(3),IntLiteral(3)],FloatType,[FloatLiteral(1.0),FloatLiteral(2.0),FloatLiteral(3.0),FloatLiteral(4.0),FloatLiteral(5.0),FloatLiteral(6.0),FloatLiteral(7.0),FloatLiteral(8.0),FloatLiteral(9.0)])),Assign(Id(c),StructLiteral(Person,[(name,StringLiteral(\"John\")),(age,IntLiteral(25))])),Assign(Id(d),ArrayLiteral([IntLiteral(5)],Id(Person),[StructLiteral(Person,[(name,StringLiteral(\"John\")),(age,IntLiteral(25))]),StructLiteral(Person,[(name,StringLiteral(\"John\")),(age,IntLiteral(25))]),StructLiteral(Person,[(name,StringLiteral(\"John\")),(age,IntLiteral(25))]),StructLiteral(Person,[(name,StringLiteral(\"John\")),(age,IntLiteral(25))]),StructLiteral(Person,[(name,StringLiteral(\"John\")),(age,IntLiteral(25))])]))]))])"
    #     self.assertTrue(TestAST.checkASTGen(input, expect, 360))
    # def test_361(self):
    #     input = """
    #     func main() {
    #         a := 2;
    #         b := 5
    #         if (a > b) {
    #             putString("a is greater than b");
    #         } else {
    #             putString("a is not greater than b");
    #         }
    #     }
    #     """
    #     expect = """Program([FuncDecl(main,[],VoidType,Block([Assign(Id(a),IntLiteral(2)),Assign(Id(b),IntLiteral(5)),If(BinaryOp(Id(a),>,Id(b)),Block([FuncCall(putString,[StringLiteral("a is greater than b")])]),Block([FuncCall(putString,[StringLiteral("a is not greater than b")])]))]))])""" 
    #     self.assertTrue(TestAST.checkASTGen(input, expect, 361))
    # def test_362(self):
    #     input = """
    #     func main() {
    #         a := 2;
    #         b := 5;
    #         if (a > b) {
    #             putString("a is greater than b");
    #         } else if (a < b) {
    #             putString("a is less than b");
    #         } else {
    #             putString("a is equal to b");
    #         }
    #     }
    #     """
    #     expect = """
    #     Program([FuncDecl(main,[],VoidType,Block([Assign(Id(a),IntLiteral(2)),Assign(Id(b),IntLiteral(5)),If(BinaryOp(Id(a),>,Id(b)),Block([FuncCall(putString,[StringLiteral(\"a is greater than b\")])]),If(BinaryOp(Id(a),<,Id(b)),Block([FuncCall(putString,[StringLiteral(\"a is less than b\")])]),Block([FuncCall(putString,[StringLiteral(\"a is equal to b\")])])))]))])
    #     """
    # def test_363(self):
    #     input = """
    #     func foo() int{
    #         a := 5 + 5;
    #     }
    #     """
    #     expect =  """Program([FuncDecl(foo,[],IntType,Block([Assign(Id(a),BinaryOp(IntLiteral(5),+,IntLiteral(5)))]))])"""
    #     self.assertTrue(TestAST.checkASTGen(input, expect, 363))
    # def test_364(self):
    #     input = """
    #     func foo() {
            
    #         return x+y;
    #     }
    #     """
    #     expect = """Program([FuncDecl(foo,[],VoidType,Block([Return(BinaryOp(Id(x),+,Id(y)))]))])""" 
    #     self.assertTrue(TestAST.checkASTGen(input, expect, 364))
    # def test_365(self):
    #     input = """
    #     func complexFunc(a int, b float, c string, d boolean, e [5]int, f [3][3]float, g Person) {
    #         if (a > 10) {
    #             putInt(a);
    #         } else {
    #             putFloat(b);
    #         }
    #         if (d) {
    #             putString(c);
    #         }
    #         if (e[0] == 5) {
    #             putBool(d);
    #         }
    #         if (f[0][0] != 5.5) {
    #             putInt(e[0]);
    #         }
    #     }
    #     """
    #     expect =  """Program([FuncDecl(complexFunc,[ParDecl(a,IntType),ParDecl(b,FloatType),ParDecl(c,StringType),ParDecl(d,BoolType),ParDecl(e,ArrayType(IntType,[IntLiteral(5)])),ParDecl(f,ArrayType(FloatType,[IntLiteral(3),IntLiteral(3)])),ParDecl(g,Id(Person))],VoidType,Block([If(BinaryOp(Id(a),>,IntLiteral(10)),Block([FuncCall(putInt,[Id(a)])]),Block([FuncCall(putFloat,[Id(b)])])),If(Id(d),Block([FuncCall(putString,[Id(c)])])),If(BinaryOp(ArrayCell(Id(e),[IntLiteral(0)]),==,IntLiteral(5)),Block([FuncCall(putBool,[Id(d)])])),If(BinaryOp(ArrayCell(Id(f),[IntLiteral(0),IntLiteral(0)]),!=,FloatLiteral(5.5)),Block([FuncCall(putInt,[ArrayCell(Id(e),[IntLiteral(0)])])]))]))])"""
    #     self.assertTrue(TestAST.checkASTGen(input, expect, 365))
    # def test_366(self):
    #     input = """
    #     func complexFunc(a int, b float, c string, d boolean, e [5]int, f [3][3]float, g Person) {
    #         for i := 0; i < 10; i += 1 {
    #             putInt(i);
    #         }
    #         for idx, value := range e {
    #             putInt(idx);
    #             putInt(value);
    #         }
    #     }
    #     """
    #     expect =  """Program([FuncDecl(complexFunc,[ParDecl(a,IntType),ParDecl(b,FloatType),ParDecl(c,StringType),ParDecl(d,BoolType),ParDecl(e,ArrayType(IntType,[IntLiteral(5)])),ParDecl(f,ArrayType(FloatType,[IntLiteral(3),IntLiteral(3)])),ParDecl(g,Id(Person))],VoidType,Block([For(Assign(Id(i),IntLiteral(0)),BinaryOp(Id(i),<,IntLiteral(10)),Assign(Id(i),BinaryOp(Id(i),+,IntLiteral(1))),Block([FuncCall(putInt,[Id(i)])])),ForEach(Id(idx),Id(value),Id(e),Block([FuncCall(putInt,[Id(idx)]),FuncCall(putInt,[Id(value)])]))]))])"""
    #     self.assertTrue(TestAST.checkASTGen(input, expect, 366))
    # def test_367(self):
    #     input = """
    #     func main() {
    #                 a[5].bar();
    #         }
    #     """
    #     expect =  """Program([FuncDecl(main,[],VoidType,Block([MethodCall(ArrayCell(Id(a),[IntLiteral(5)]),bar,[])]))])"""
    #     self.assertTrue(TestAST.checkASTGen(input, expect, 367))
    # def test_368(self):
    #     input = """
    #     var b int;
    #     func main() {
    #         b := [5]int{1,2,3,4,5};
    #         putInt(b[0]);
    #     }
    #     """
    #     expect =  """Program([VarDecl(b,IntType),FuncDecl(main,[],VoidType,Block([Assign(Id(b),ArrayLiteral([IntLiteral(5)],IntType,[IntLiteral(1),IntLiteral(2),IntLiteral(3),IntLiteral(4),IntLiteral(5)])),FuncCall(putInt,[ArrayCell(Id(b),[IntLiteral(0)])])]))])"""
    #     self.assertTrue(TestAST.checkASTGen(input, expect, 368))
    # def test_369(self):
    #     input = """
    #     var x float;
    #     func main() {
    #         x := 5.5;
    #         putFloat(x);
    #     }
    #     """
    #     expect =  """Program([VarDecl(x,FloatType),FuncDecl(main,[],VoidType,Block([Assign(Id(x),FloatLiteral(5.5)),FuncCall(putFloat,[Id(x)])]))])"""
    #     self.assertTrue(TestAST.checkASTGen(input, expect, 369))

    # def test_370(self):
    #     input = """
    #     func main() {
    #         str := "Hello" + " World";
    #         putString(str);
    #     }
    #     """
    #     expect =  """Program([FuncDecl(main,[],VoidType,Block([Assign(Id(str),BinaryOp(StringLiteral("Hello"),+,StringLiteral(" World"))),FuncCall(putString,[Id(str)])]))])"""
    #     self.assertTrue(TestAST.checkASTGen(input, expect, 370))
    # def test_371(self):
    #     input = """
    #     func main() {
    #         a := 5;
    #         b := 5;
    #         c := 5;
    #         d := 5;
    #         e := 5;
    #     }
    #     """
    #     expect =  """Program([FuncDecl(main,[],VoidType,Block([Assign(Id(a),IntLiteral(5)),Assign(Id(b),IntLiteral(5)),Assign(Id(c),IntLiteral(5)),Assign(Id(d),IntLiteral(5)),Assign(Id(e),IntLiteral(5))]))])"""
    #     self.assertTrue(TestAST.checkASTGen(input, expect, 371))
    # def test_372(self):
    #     input = """
    #     func main() {
    #         var flag bool = false;
    #         putBool(flag);
    #     }
    #     """
    #     expect =  """Program([FuncDecl(main,[],VoidType,Block([VarDecl(flag,Id(bool),BooleanLiteral(false)),FuncCall(putBool,[Id(flag)])]))])"""
    #     self.assertTrue(TestAST.checkASTGen(input, expect, 372))
    # def test_373(self):
    #     input = """
    #     func main() {
    #         x := !true;
    #     }
    #     """
    #     expect =  """Program([FuncDecl(main,[],VoidType,Block([Assign(Id(x),UnaryOp(!,BooleanLiteral(true)))]))])"""
    #     self.assertTrue(TestAST.checkASTGen(input, expect, 373))
    # def test_374(self):
    #     input = """
    #     func main() {
    #         x := 5;
    #         y := 10;
    #         z := x + y;
    #     }
    #     """
    #     expect =  """Program([FuncDecl(main,[],VoidType,Block([Assign(Id(x),IntLiteral(5)),Assign(Id(y),IntLiteral(10)),Assign(Id(z),BinaryOp(Id(x),+,Id(y)))]))])"""
    #     self.assertTrue(TestAST.checkASTGen(input, expect, 374))
    # def test_375(self):
    #     input ="""
    #     func fibo(n int) int {
    #         if (n == 0) {
    #             return 0;
    #         }
    #         if (n == 1) {
    #             return 1;
    #         }
    #         return fibo(n-1) + fibo(n-2);
    #     }
    #     """
    #     expect =  """Program([FuncDecl(fibo,[ParDecl(n,IntType)],IntType,Block([If(BinaryOp(Id(n),==,IntLiteral(0)),Block([Return(IntLiteral(0))])),If(BinaryOp(Id(n),==,IntLiteral(1)),Block([Return(IntLiteral(1))])),Return(BinaryOp(FuncCall(fibo,[BinaryOp(Id(n),-,IntLiteral(1))]),+,FuncCall(fibo,[BinaryOp(Id(n),-,IntLiteral(2))])))]))])"""
    #     self.assertTrue(TestAST.checkASTGen(input, expect, 375))
    # def test_376(self):
    #     input = """
    #     func lcs(X string, Y string, m int, n int) int {
    #         if (m == 0 || n == 0) {
    #             return 0;
    #         }
    #         if (X[m-1] == Y[n-1]) {
    #             return 1 + lcs(X, Y, m-1, n-1);
    #         } else {
    #             return max(lcs(X, Y, m, n-1), lcs(X, Y, m-1, n));
    #         }
    #     }
    #     """
    #     expect =  """Program([FuncDecl(lcs,[ParDecl(X,StringType),ParDecl(Y,StringType),ParDecl(m,IntType),ParDecl(n,IntType)],IntType,Block([If(BinaryOp(BinaryOp(Id(m),==,IntLiteral(0)),||,BinaryOp(Id(n),==,IntLiteral(0))),Block([Return(IntLiteral(0))])),If(BinaryOp(ArrayCell(Id(X),[BinaryOp(Id(m),-,IntLiteral(1))]),==,ArrayCell(Id(Y),[BinaryOp(Id(n),-,IntLiteral(1))])),Block([Return(BinaryOp(IntLiteral(1),+,FuncCall(lcs,[Id(X),Id(Y),BinaryOp(Id(m),-,IntLiteral(1)),BinaryOp(Id(n),-,IntLiteral(1))])))]),Block([Return(FuncCall(max,[FuncCall(lcs,[Id(X),Id(Y),Id(m),BinaryOp(Id(n),-,IntLiteral(1))]),FuncCall(lcs,[Id(X),Id(Y),BinaryOp(Id(m),-,IntLiteral(1)),Id(n)])]))]))]))])"""
    #     self.assertTrue(TestAST.checkASTGen(input, expect, 376))
    # def test_377(self):
    #     input = """
    #     func main(){
    #         a := "Hello";
    #         b := "World";
    #         c := a + b;
    #         putString(c);
    #         z := "ccndshbc \\n \\t"
    #     }
    #     """
    #     expect = str(
    #         Program(
    #             [
    #                 FuncDecl("main", [],VoidType(),  Block([
    #                     Assign(Id("a"), StringLiteral("\"Hello\"")),
    #                     Assign(Id("b"), StringLiteral("\"World\"")),
    #                     Assign(Id("c"), BinaryOp("+", Id("a"), Id("b"))),
    #                     FuncCall("putString", [Id("c")]),
    #                     Assign(Id("z"), StringLiteral("\"ccndshbc \\n \\t\""))
    #                 ]))
    #             ]
    #         )
    #     )
    #     self.assertTrue(TestAST.checkASTGen(input, expect, 377))
    # def test_378(self):
    #     input = """
    #     func main(){
    #         a:= 1.e-2;
    #         b:= 1.e+2;
    #         c:= 1.e2;
    #     }
    #     """
    #     expect =  """Program([FuncDecl(main,[],VoidType,Block([Assign(Id(a),FloatLiteral(0.01)),Assign(Id(b),FloatLiteral(100.0)),Assign(Id(c),FloatLiteral(100.0))]))])"""
    #     self.assertTrue(TestAST.checkASTGen(input, expect, 378))
    # def test_379(self):
    #     input = """
    #     func main(){
    #         for true{
    #             putString("Hello");
    #         }
    #     }
    #     """
    #     expect =  """Program([FuncDecl(main,[],VoidType,Block([For(BooleanLiteral(true),Block([FuncCall(putString,[StringLiteral("Hello")])]))]))])"""
    #     self.assertTrue(TestAST.checkASTGen(input, expect, 379))
    # def test_380(self):
    #     input = """
    #     func main(){
    #         foo();
    #         bar();
    #         something();
    #         hello();
    #     }
    #     """
    #     expect =  """Program([FuncDecl(main,[],VoidType,Block([FuncCall(foo,[]),FuncCall(bar,[]),FuncCall(something,[]),FuncCall(hello,[])]))])"""
    #     self.assertTrue(TestAST.checkASTGen(input, expect, 380))
    # def test_381(self):
    #     input = """
    #     var xyz[5] int;
    #     func main(){
    #         xyz[0] := 5;
    #         putInt(xyz[0]);
    #     }
    #     """
    #     expect =  """Program([VarDecl(xyz,ArrayType(IntType,[IntLiteral(5)])),FuncDecl(main,[],VoidType,Block([Assign(ArrayCell(Id(xyz),[IntLiteral(0)]),IntLiteral(5)),FuncCall(putInt,[ArrayCell(Id(xyz),[IntLiteral(0)])])]))])"""
    #     self.assertTrue(TestAST.checkASTGen(input, expect, 381))
    # def test_382(self):
    #     input = """
    #     var fl float;
    #     func main(){
    #         fl := 5.5;
    #         putFloat(fl);
    #     }
    #     """
    #     expect =  """Program([VarDecl(fl,FloatType),FuncDecl(main,[],VoidType,Block([Assign(Id(fl),FloatLiteral(5.5)),FuncCall(putFloat,[Id(fl)])]))])"""
    #     self.assertTrue(TestAST.checkASTGen(input, expect, 382))
    # def test_383(self):
    #     input = """
    #     func main (){
    #         for i:=0;i<10;i+=1{
    #             if (abc){
    #                 break;
    #             } else if(def){
    #                 if (ghi){
    #                     continue;
    #                 }
    #             }
    #         }
    #     }
    #     """
    #     expect =  """Program([FuncDecl(main,[],VoidType,Block([For(Assign(Id(i),IntLiteral(0)),BinaryOp(Id(i),<,IntLiteral(10)),Assign(Id(i),BinaryOp(Id(i),+,IntLiteral(1))),Block([If(Id(abc),Block([Break()]),If(Id(def),Block([If(Id(ghi),Block([Continue()]))])))]))]))])"""
    #     self.assertTrue(TestAST.checkASTGen(input, expect, 383))
    # def test_384(self):
    #     input = """
    #     func main(){
    #         for abc*def{
    #             putString("Hello");
    #         }
    #     }
    #     """
    #     expect =  """Program([FuncDecl(main,[],VoidType,Block([For(BinaryOp(Id(abc),*,Id(def)),Block([FuncCall(putString,[StringLiteral("Hello")])]))]))])"""
    #     self.assertTrue(TestAST.checkASTGen(input, expect, 384))
    # def test_385(self):
    #     input = """
    #     func main(){
    #         for idx, value := range arr{
    #             if (idx * value > 10){
    #                 break;
    #             } else if(idx * value < 10){
    #                 continue;
    #             }
    #         }
    #     }
    #     """
    #     expect =  """Program([FuncDecl(main,[],VoidType,Block([ForEach(Id(idx),Id(value),Id(arr),Block([If(BinaryOp(BinaryOp(Id(idx),*,Id(value)),>,IntLiteral(10)),Block([Break()]),If(BinaryOp(BinaryOp(Id(idx),*,Id(value)),<,IntLiteral(10)),Block([Continue()])))]))]))])"""
    #     self.assertTrue(TestAST.checkASTGen(input, expect, 385))
    # def test_386(self):
    #     input = """
    #     func main(){
    #         for i:=0;i<10;i+=1{
    #             for j:=0;j<10;j+=1{
    #                 putInt(i+j);
    #             }
    #         }
    #     }
    #     """
    #     expect =  """Program([FuncDecl(main,[],VoidType,Block([For(Assign(Id(i),IntLiteral(0)),BinaryOp(Id(i),<,IntLiteral(10)),Assign(Id(i),BinaryOp(Id(i),+,IntLiteral(1))),Block([For(Assign(Id(j),IntLiteral(0)),BinaryOp(Id(j),<,IntLiteral(10)),Assign(Id(j),BinaryOp(Id(j),+,IntLiteral(1))),Block([FuncCall(putInt,[BinaryOp(Id(i),+,Id(j))])]))]))]))])"""
    #     self.assertTrue(TestAST.checkASTGen(input, expect, 386))
    # def test_387(self):
    #     input = """
    #     // full call stmt
    #     func main(){
    #         foo(1,2,3);
    #         bar(1.0,2.0,3.0);
    #         hello("Hello","World");
    #         something(true,false);
    #         nillfunc(nil)
    #     }
    #     """
    #     expect =  """Program([FuncDecl(main,[],VoidType,Block([FuncCall(foo,[IntLiteral(1),IntLiteral(2),IntLiteral(3)]),FuncCall(bar,[FloatLiteral(1.0),FloatLiteral(2.0),FloatLiteral(3.0)]),FuncCall(hello,[StringLiteral("Hello"),StringLiteral("World")]),FuncCall(something,[BooleanLiteral(true),BooleanLiteral(false)]),FuncCall(nillfunc,[Nil])]))])"""
    #     self.assertTrue(TestAST.checkASTGen(input, expect, 387))
    # def test_388(self):
    #     input = """
    #     /* comment*/
    #     func main(){
    #         // call method
    #         a.foo();
    #         b.bar();
    #         c.hello();
    #         d.something();
    #         e.nillfunc();
    #     }
    #     """
    #     expect = """Program([FuncDecl(main,[],VoidType,Block([MethodCall(Id(a),foo,[]),MethodCall(Id(b),bar,[]),MethodCall(Id(c),hello,[]),MethodCall(Id(d),something,[]),MethodCall(Id(e),nillfunc,[])]))])"""
    #     self.assertTrue(TestAST.checkASTGen(input, expect, 388))
    # def test_389(self):
    #     input = """
    #     func main(){
    #         for true {
    #             for false{
    #                 for i < 10{
    #                     putInt(i);
    #                 }
    #             }
    #         }
    #     }
    #     """
    #     expect =  """Program([FuncDecl(main,[],VoidType,Block([For(BooleanLiteral(true),Block([For(BooleanLiteral(false),Block([For(BinaryOp(Id(i),<,IntLiteral(10)),Block([FuncCall(putInt,[Id(i)])]))]))]))]))])"""
    #     self.assertTrue(TestAST.checkASTGen(input, expect, 389))
    # def test_390(self):
    #     input = """
    #     func main(){
    #         for i:=0;i<10;i+=1{
    #             for j:=0;j<10;j+=1{
    #                 for k:=0;k<10;k+=1{
    #                     putInt(i+j+k);
    #                 }
    #             }
    #         }
    #     }
    #     """
    #     expect =  """Program([FuncDecl(main,[],VoidType,Block([For(Assign(Id(i),IntLiteral(0)),BinaryOp(Id(i),<,IntLiteral(10)),Assign(Id(i),BinaryOp(Id(i),+,IntLiteral(1))),Block([For(Assign(Id(j),IntLiteral(0)),BinaryOp(Id(j),<,IntLiteral(10)),Assign(Id(j),BinaryOp(Id(j),+,IntLiteral(1))),Block([For(Assign(Id(k),IntLiteral(0)),BinaryOp(Id(k),<,IntLiteral(10)),Assign(Id(k),BinaryOp(Id(k),+,IntLiteral(1))),Block([FuncCall(putInt,[BinaryOp(BinaryOp(Id(i),+,Id(j)),+,Id(k))])]))]))]))]))])"""
    #     self.assertTrue(TestAST.checkASTGen(input, expect, 390))
    # def test_391(self):
    #     input = """
    #     func main(){
    #         for var i = 0; i < 10; i += 1{
    #             for var j = 0; j < 10; j += 1{
    #                 for var k = 0; k < 10; k += 1{
    #                     putInt(i+j+k);
    #                 }
    #             }
    #         }
    #     }
    #     """
    #     expect =  """Program([FuncDecl(main,[],VoidType,Block([For(VarDecl(i,IntLiteral(0)),BinaryOp(Id(i),<,IntLiteral(10)),Assign(Id(i),BinaryOp(Id(i),+,IntLiteral(1))),Block([For(VarDecl(j,IntLiteral(0)),BinaryOp(Id(j),<,IntLiteral(10)),Assign(Id(j),BinaryOp(Id(j),+,IntLiteral(1))),Block([For(VarDecl(k,IntLiteral(0)),BinaryOp(Id(k),<,IntLiteral(10)),Assign(Id(k),BinaryOp(Id(k),+,IntLiteral(1))),Block([FuncCall(putInt,[BinaryOp(BinaryOp(Id(i),+,Id(j)),+,Id(k))])]))]))]))]))])"""
    #     self.assertTrue(TestAST.checkASTGen(input, expect, 391))
    # def test_392(self):
    #     input = """
    #     func main(){
    #     for i:=0;i<10;i+=1{
    #         for j:=0;j<10;j+=1{
    #             for true{
    #                 putInt(i+j);
    #             }
    #         }
    #     }
    #     }
    #     """
    #     expect = """Program([FuncDecl(main,[],VoidType,Block([For(Assign(Id(i),IntLiteral(0)),BinaryOp(Id(i),<,IntLiteral(10)),Assign(Id(i),BinaryOp(Id(i),+,IntLiteral(1))),Block([For(Assign(Id(j),IntLiteral(0)),BinaryOp(Id(j),<,IntLiteral(10)),Assign(Id(j),BinaryOp(Id(j),+,IntLiteral(1))),Block([For(BooleanLiteral(true),Block([FuncCall(putInt,[BinaryOp(Id(i),+,Id(j))])]))]))]))]))])"""
    #     self.assertTrue(TestAST.checkASTGen(input, expect, 392))
    # def test_393(self):
    #     input = """
    #     func ifStmt(){
    #         if (true){
    #             putString("Hello");
    #             if (foo()){
    #                 putString("World");
    #             }
    #         }
    #     }
    #     """
    #     expect = """Program([FuncDecl(ifStmt,[],VoidType,Block([If(BooleanLiteral(true),Block([FuncCall(putString,[StringLiteral("Hello")]),If(FuncCall(foo,[]),Block([FuncCall(putString,[StringLiteral("World")])]))]))]))])"""
    #     self.assertTrue(TestAST.checkASTGen(input, expect, 393))
    # def test_394(self):
    #     input = """
    #     func main(){
    #         foo("Hello", 1.e432, 1.0e-2, 1.0e+2, 1.0e2);
    #     }
    #     """
    #     expect =  """Program([FuncDecl(main,[],VoidType,Block([FuncCall(foo,[StringLiteral("Hello"),FloatLiteral(inf),FloatLiteral(0.01),FloatLiteral(100.0),FloatLiteral(100.0)])]))])"""
    #     self.assertTrue(TestAST.checkASTGen(input, expect, 394))
    # def test_395(self):
    #     input = """
    #     const a = 5;
    #     const z = a + 5;
    #     const y = z + 5;
    #     const x = y + 5;
    #     """
    #     expect =  """Program([ConstDecl(a,IntLiteral(5)),ConstDecl(z,BinaryOp(Id(a),+,IntLiteral(5))),ConstDecl(y,BinaryOp(Id(z),+,IntLiteral(5))),ConstDecl(x,BinaryOp(Id(y),+,IntLiteral(5)))])"""
    #     self.assertTrue(TestAST.checkASTGen(input, expect, 395))
    # def test_396(self):
    #     input = """
    #     func main (){
    #         a := !true;
    #         b := !false;
    #         c := !a;
    #         d := !b;
    #     }
    #     """
    #     expect =  """Program([FuncDecl(main,[],VoidType,Block([Assign(Id(a),UnaryOp(!,BooleanLiteral(true))),Assign(Id(b),UnaryOp(!,BooleanLiteral(false))),Assign(Id(c),UnaryOp(!,Id(a))),Assign(Id(d),UnaryOp(!,Id(b)))]))])"""
    #     self.assertTrue(TestAST.checkASTGen(input, expect, 396))
    # def test_397(self):
    #     input = """
    #     func smartFunc(){
    #         if (true){
    #             putString("Hello");
    #         } else if (false){
    #             putString("World");
    #         } else {
    #             putString("Goodbye");
    #         }
    #     }
    #     """
    #     expect = """Program([FuncDecl(smartFunc,[],VoidType,Block([If(BooleanLiteral(true),Block([FuncCall(putString,[StringLiteral("Hello")])]),If(BooleanLiteral(false),Block([FuncCall(putString,[StringLiteral("World")])]),Block([FuncCall(putString,[StringLiteral("Goodbye")])])))]))])"""
    #     self.assertTrue(TestAST.checkASTGen(input, expect, 397))
    # def test_398(self):
    #     input = """
    #     func (c Circle) area() float {
    #         return c.radius * c.radius * 3.14;
    #     }
    #     """
    #     expect =  """Program([MethodDecl(c,Id(Circle),FuncDecl(area,[],FloatType,Block([Return(BinaryOp(BinaryOp(FieldAccess(Id(c),radius),*,FieldAccess(Id(c),radius)),*,FloatLiteral(3.14)))])))])"""
    #     self.assertTrue(TestAST.checkASTGen(input, expect, 398))
    # def test_399(self):
    #     input = """
    #     func lastTestcase(){
    #         if (true){
    #             if (false){
    #                 if (true){
    #                     if (false){
    #                         putString("Hello");
    #                     }
    #                 }
    #             }
    #         }
    #     }
    #     """
    #     expect =  """Program([FuncDecl(lastTestcase,[],VoidType,Block([If(BooleanLiteral(true),Block([If(BooleanLiteral(false),Block([If(BooleanLiteral(true),Block([If(BooleanLiteral(false),Block([FuncCall(putString,[StringLiteral("Hello")])]))]))]))]))]))])"""
    #     self.assertTrue(TestAST.checkASTGen(input, expect, 399))
        