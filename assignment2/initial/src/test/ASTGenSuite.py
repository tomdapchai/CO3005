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
#         var a float = 2.47e-2;
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
#                     VarDecl("a",FloatType(),FloatLiteral("2.47e-2")),
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
    def test_327(self):
        input = """var arr [3]int = [3]int{1, 2, 3}; 
            func foo() {
    arr2[1].putName("abc")
}

           """
        expect = str(
            Program([VarDecl("arr",None,ArrayLiteral([IntLiteral(3)],IntType(),[IntLiteral(1),IntLiteral(2),IntLiteral(3)])),FuncDecl("Add",[],VoidType(),Block([ForEach(Id("index"),Id("value"),Id("arr"),Block([Assign(Id("x"),BinaryOp("+",Id("x"),Id("value")))]))]))])
        )
        # print(expect)
        self.assertTrue(TestAST.checkASTGen(input,expect,327))
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
#     def test_351(self):
#         input = """
#         func binSearch(arr [100]int, x int) int {
#             l := 0;
#             h := arr.length() - 1;
#             for l <= h {
#                 m := l + (h - l) / 2;
#                 if (arr[m] == x) {
#                     return m;
#                 }
#                 if (arr[m] < x) {
#                     l := m + 1;
#                 } else {
#                     h := m - 1;
#                 }
#             }
#             return -1;
#         }
#         """
#         expect = str(
#             Program([FuncDecl("binSearch",[ParamDecl("arr",ArrayType([IntLiteral(100)],IntType())),ParamDecl("x",IntType())],IntType(),Block([Assign(Id("l"),IntLiteral(0)),Assign(Id("h"),BinaryOp("-",MethCall(Id("arr"),"length",[]),IntLiteral(1))),ForBasic(BinaryOp("<=",Id("l"),Id("h")),Block([Assign(Id("m"),BinaryOp("+",Id("l"),BinaryOp("/",BinaryOp("-",Id("h"),Id("l")),IntLiteral(2)))),If(BinaryOp("==",ArrayCell(Id("arr"),[Id("m")]),Id("x")),Block([Return(Id("m"))]),None),If(BinaryOp("<",ArrayCell(Id("arr"),[Id("m")]),Id("x")),Block([Assign(Id("l"),BinaryOp("+",Id("m"),IntLiteral(1)))]),Block([Assign(Id("h"),BinaryOp("-",Id("m"),IntLiteral(1)))]))])),Return(UnaryOp("-",IntLiteral(1)))]))])
#         )
#         self.assertTrue(TestAST.checkASTGen(input, expect, 351))
#     def test_352(self):
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
#         self.assertTrue(TestAST.checkASTGen(input, expect, 352))
#     def test_353(self):
#         input = """var a = 10 % 3 * Person{Id: test}.Id[3].d(2, 3)[4].d.e.f();"""
#         expect = str(
#             Program([VarDecl("a",None,BinaryOp("*",BinaryOp("%",IntLiteral(10),IntLiteral(3)),MethCall(FieldAccess(FieldAccess(ArrayCell(MethCall(ArrayCell(FieldAccess(StructLiteral("Person",[("Id",Id("test"))]),"Id"),[IntLiteral(3)]),"d",[IntLiteral(2),IntLiteral(3)]),[IntLiteral(4)]),"d"),"e"),"f",[])))])
#         )
#         self.assertTrue(TestAST.checkASTGen(input, expect, 353))
#     def test_354(self):
#         input = """
#         const TEST = 10;
#         var arr [5]int;
#         var a2 [TEST]string;
        
#         func main() {
#             arr := [TEST]int{1, 2, 3}
#             arr[a+b-c*(11%11+1||(d&&(!c)))] /= 23;
#         }
        
#         """
#         expect = str(
#             Program([ConstDecl("TEST",None,IntLiteral(10)),VarDecl("arr",ArrayType([IntLiteral(5)],IntType()),None),VarDecl("a2",ArrayType([Id("TEST")],StringType()),None),FuncDecl("main",[],VoidType(),Block([Assign(Id("arr"),ArrayLiteral([Id("TEST")],IntType(),[IntLiteral(1),IntLiteral(2),IntLiteral(3)])),Assign(ArrayCell(Id("arr"),[BinaryOp("-",BinaryOp("+",Id("a"),Id("b")),BinaryOp("*",Id("c"),BinaryOp("||",BinaryOp("+",BinaryOp("%",IntLiteral(11),IntLiteral(11)),IntLiteral(1)),BinaryOp("&&",Id("d"),UnaryOp("!",Id("c"))))))]),BinaryOp("/",ArrayCell(Id("arr"),[BinaryOp("-",BinaryOp("+",Id("a"),Id("b")),BinaryOp("*",Id("c"),BinaryOp("||",BinaryOp("+",BinaryOp("%",IntLiteral(11),IntLiteral(11)),IntLiteral(1)),BinaryOp("&&",Id("d"),UnaryOp("!",Id("c"))))))]),IntLiteral(23)))]))])
#         )
#         self.assertTrue(TestAST.checkASTGen(input, expect, 354))
#     def test_355(self):
#         input = """
#         type Person struct {
#             name string;
#             age int;
#         }

#         func (c Person) SayHello() {
#                 fmt.Println("Hello, my name is " + c.name);
#             }

#         var p Person = Person{name: "Alice", age: 25};
#         func tmp() {
#         if (p.age > 18) {
#             for i := 0; i < p.age; i += 1 {
#                 // Some action
#                 counter := counter + 1;
#             }
#         }
#         }
        
#         """
#         expect = str(
#             Program([StructType("Person",[("name",StringType()),("age",IntType())],[]),MethodDecl("c",Id("Person"),FuncDecl("SayHello",[],VoidType(),Block([MethCall(Id("fmt"),"Println",[BinaryOp("+",StringLiteral("\"Hello, my name is \""),FieldAccess(Id("c"),"name"))])]))),VarDecl("p",Id("Person"),StructLiteral("Person",[("name",StringLiteral("\"Alice\"")),("age",IntLiteral(25))])),FuncDecl("tmp",[],VoidType(),Block([If(BinaryOp(">",FieldAccess(Id("p"),"age"),IntLiteral(18)),Block([ForStep(Assign(Id("i"),IntLiteral(0)),BinaryOp("<",Id("i"),FieldAccess(Id("p"),"age")),Assign(Id("i"),BinaryOp("+",Id("i"),IntLiteral(1))),Block([Assign(Id("counter"),BinaryOp("+",Id("counter"),IntLiteral(1)))]))]),None)]))])
#         )
#         self.assertTrue(TestAST.checkASTGen(input, expect, 355))
#     def test_356(self):
#         input = """
#         type Point struct {
#             x int;
#             y int;
#         }

#         var p Point = Point{x: 5, y: 10};
#         func tmp() {
#             for i := 0; i < p.x; i += 1 {
#             p.y := p.y + 1;
#             const a = [1]int{{1, 0x1}, ID{}, 1.2, "s", true, false, nil} + nil                    
#         }
        
#         }
        
#         """
#         expect = str(
#             Program([StructType("Point",[("x",IntType()),("y",IntType())],[]),VarDecl("p",Id("Point"),StructLiteral("Point",[("x",IntLiteral(5)),("y",IntLiteral(10))])),FuncDecl("tmp",[],VoidType(),Block([ForStep(Assign(Id("i"),IntLiteral(0)),BinaryOp("<",Id("i"),FieldAccess(Id("p"),"x")),Assign(Id("i"),BinaryOp("+",Id("i"),IntLiteral(1))),Block([Assign(FieldAccess(Id("p"),"y"),BinaryOp("+",FieldAccess(Id("p"),"y"),IntLiteral(1))),ConstDecl("a",None,BinaryOp("+",ArrayLiteral([IntLiteral(1)],IntType(),[[IntLiteral(1),IntLiteral("0x1")],StructLiteral("ID",[]),FloatLiteral(1.2),StringLiteral("\"s\""),BooleanLiteral(True),BooleanLiteral(False),NilLiteral()]),NilLiteral()))]))]))])
#         )
#         self.assertTrue(TestAST.checkASTGen(input, expect, 356))
#     def test_357(self):
#         input = """
#             const a = !-!-!-1 + Person{Id: name}.c[3].d().a[2];
#         """
#         expect = str(
#             Program([ConstDecl("a",None,BinaryOp("+",UnaryOp("!",UnaryOp("-",UnaryOp("!",UnaryOp("-",UnaryOp("!",UnaryOp("-",IntLiteral(1))))))),ArrayCell(FieldAccess(MethCall(ArrayCell(FieldAccess(StructLiteral("Person",[("Id",Id("name"))]),"c"),[IntLiteral(3)]),"d",[]),"a"),[IntLiteral(2)])))])
#         )
#         self.assertTrue(TestAST.checkASTGen(input, expect, 357))
#     def test_358(self):
#         input = """
#             type Rectangle struct {
#                 length float;
#                 width float;
#                 color string;
#             }
#         """
#         expect = str(
#             Program([StructType("Rectangle",[("length",FloatType()),("width",FloatType()),("color",StringType())],[])])
#         )
#         self.assertTrue(TestAST.checkASTGen(input, expect, 358))
#     def test_359(self):
#         input = """
#             func main() {
#                 for i := 0; i < 10; i += 1 {
#                     if (i % 2 == 0) {
#                         putIntLn(i);
#                     }
#                 }
#             }
#         """
#         expect = str(
#             Program([FuncDecl("main",[],VoidType(),Block([ForStep(Assign(Id("i"),IntLiteral(0)),BinaryOp("<",Id("i"),IntLiteral(10)),Assign(Id("i"),BinaryOp("+",Id("i"),IntLiteral(1))),Block([If(BinaryOp("==",BinaryOp("%",Id("i"),IntLiteral(2)),IntLiteral(0)),Block([FuncCall("putIntLn",[Id("i")])]),None)]))]))])
#         )
#         self.assertTrue(TestAST.checkASTGen(input, expect, 359))
#     def test_360(self):
#         input = """
#             var colors = [3]string{"red", "green", "blue"};
#             const MAX_SIZE = 100;
#             var grid = [MAX_SIZE][MAX_SIZE]int{1,2,3};
#         """
#         expect = str(
#             Program([VarDecl("colors",None,ArrayLiteral([IntLiteral(3)],StringType(),[StringLiteral("\"red\""),StringLiteral("\"green\""),StringLiteral("\"blue\"")])),ConstDecl("MAX_SIZE",None,IntLiteral(100)),VarDecl("grid",None,ArrayLiteral([Id("MAX_SIZE"),Id("MAX_SIZE")],IntType(),[IntLiteral(1),IntLiteral(2),IntLiteral(3)]))])
#         )
#         self.assertTrue(TestAST.checkASTGen(input, expect, 360))
#     def test_361(self):
#         input = """
#             func fibonacci(n int) int {
#                 if (n <= 1) {
#                     return n;
#                 }
#                 return fibonacci(n - 1) + fibonacci(n - 2);
#             }
#         """
#         expect = str(
#             Program([FuncDecl("fibonacci",[ParamDecl("n",IntType())],IntType(),Block([If(BinaryOp("<=",Id("n"),IntLiteral(1)),Block([Return(Id("n"))]),None),Return(BinaryOp("+",FuncCall("fibonacci",[BinaryOp("-",Id("n"),IntLiteral(1))]),FuncCall("fibonacci",[BinaryOp("-",Id("n"),IntLiteral(2))])))]))])
#         )
#         self.assertTrue(TestAST.checkASTGen(input, expect, 361))
#     def test_362(self):
#         input = """
#             type Stack interface {
#                 push(value int);
#                 pop() int;
#                 isEmpty() boolean;
#                 size() int
#             }
#         """
#         expect = str(
#             Program([InterfaceType("Stack",[Prototype("push",[IntType()],VoidType()),Prototype("pop",[],IntType()),Prototype("isEmpty",[],BoolType()),Prototype("size",[],IntType())])])
#         )
#         self.assertTrue(TestAST.checkASTGen(input, expect, 362))
#     def test_363(self):
#         input = """
#             func processArray(arr [10]int) {
#                 for i := 0; i < 10; i += 1 {
#                     arr[i] := arr[i] * 2;
#                 }
#             }
#         """
#         expect =  str(
#             Program([FuncDecl("processArray",[ParamDecl("arr",ArrayType([IntLiteral(10)],IntType()))],VoidType(),Block([ForStep(Assign(Id("i"),IntLiteral(0)),BinaryOp("<",Id("i"),IntLiteral(10)),Assign(Id("i"),BinaryOp("+",Id("i"),IntLiteral(1))),Block([Assign(ArrayCell(Id("arr"),[Id("i")]),BinaryOp("*",ArrayCell(Id("arr"),[Id("i")]),IntLiteral(2)))]))]))])
#         )
#         self.assertTrue(TestAST.checkASTGen(input, expect, 363))
#     def test_364(self):
#         input = """
#             type Complex struct {
#                 real float;
#                 imag float;
#             }

#             func (c Complex) magnitude() float {
#                 return c.real * c.real + c.imag * c.imag;
#             }
#         """
#         expect = str(
#             Program([StructType("Complex",[("real",FloatType()),("imag",FloatType())],[]),MethodDecl("c",Id("Complex"),FuncDecl("magnitude",[],FloatType(),Block([Return(BinaryOp("+",BinaryOp("*",FieldAccess(Id("c"),"real"),FieldAccess(Id("c"),"real")),BinaryOp("*",FieldAccess(Id("c"),"imag"),FieldAccess(Id("c"),"imag"))))])))])
#         )
#         self.assertTrue(TestAST.checkASTGen(input, expect, 364))
#     def test_365(self):
#         input = """
#             var matrix3D = [2][3][4]float{{{1.1, 1.2, 1.3, 1.4}, {2.1, 2.2, 2.3, 2.4}, {3.1, 3.2, 3.3, 3.4}},{{4.1, 4.2, 4.3, 4.4}, {5.1, 5.2, 5.3, 5.4}, {6.1, 6.2, 6.3, 6.4}}}
#             };
#         """
#         expect =  str(
#             Program([VarDecl("matrix3D",None,ArrayLiteral([IntLiteral(2),IntLiteral(3),IntLiteral(4)],FloatType(),[[[FloatLiteral(1.1),FloatLiteral(1.2),FloatLiteral(1.3),FloatLiteral(1.4)],[FloatLiteral(2.1),FloatLiteral(2.2),FloatLiteral(2.3),FloatLiteral(2.4)],[FloatLiteral(3.1),FloatLiteral(3.2),FloatLiteral(3.3),FloatLiteral(3.4)]],[[FloatLiteral(4.1),FloatLiteral(4.2),FloatLiteral(4.3),FloatLiteral(4.4)],[FloatLiteral(5.1),FloatLiteral(5.2),FloatLiteral(5.3),FloatLiteral(5.4)],[FloatLiteral(6.1),FloatLiteral(6.2),FloatLiteral(6.3),FloatLiteral(6.4)]]]))])
#         )
#         self.assertTrue(TestAST.checkASTGen(input, expect, 365))
#     def test_366(self):
#         input = """
#             type Tree struct {
#                 value int;
#                 left Tree;
#                 right Tree;
#             }

#             func (t Tree) insert(val int) {
#                 if (val < t.value) {
#                     t.left.insert(val);
#                 } else {
#                     t.right.insert(val);
#                 }
#             }
#         """
#         expect =  str(
#             Program([StructType("Tree",[("value",IntType()),("left",Id("Tree")),("right",Id("Tree"))],[]),MethodDecl("t",Id("Tree"),FuncDecl("insert",[ParamDecl("val",IntType())],VoidType(),Block([If(BinaryOp("<",Id("val"),FieldAccess(Id("t"),"value")),Block([MethCall(FieldAccess(Id("t"),"left"),"insert",[Id("val")])]),Block([MethCall(FieldAccess(Id("t"),"right"),"insert",[Id("val")])]))])))])
#         )
#         self.assertTrue(TestAST.checkASTGen(input, expect, 366))
#     def test_367(self):
#         input = """
#             func quickSort(arr [100]int, low int, high int) {
#                 if (low < high) {
#                     pivot := arr[high];
#                     i := low - 1;
                    
#                     for j := low; j < high; j += 1 {
#                         if (arr[j] < pivot) {
#                             i += 1;
#                             temp := arr[i];
#                             arr[i] := arr[j];
#                             arr[j] := temp;
#                         }
#                     }
#                 }
#             }
#         """
#         expect =  str(
#             Program([FuncDecl("quickSort",[ParamDecl("arr",ArrayType([IntLiteral(100)],IntType())),ParamDecl("low",IntType()),ParamDecl("high",IntType())],VoidType(),Block([If(BinaryOp("<",Id("low"),Id("high")),Block([Assign(Id("pivot"),ArrayCell(Id("arr"),[Id("high")])),Assign(Id("i"),BinaryOp("-",Id("low"),IntLiteral(1))),ForStep(Assign(Id("j"),Id("low")),BinaryOp("<",Id("j"),Id("high")),Assign(Id("j"),BinaryOp("+",Id("j"),IntLiteral(1))),Block([If(BinaryOp("<",ArrayCell(Id("arr"),[Id("j")]),Id("pivot")),Block([Assign(Id("i"),BinaryOp("+",Id("i"),IntLiteral(1))),Assign(Id("temp"),ArrayCell(Id("arr"),[Id("i")])),Assign(ArrayCell(Id("arr"),[Id("i")]),ArrayCell(Id("arr"),[Id("j")])),Assign(ArrayCell(Id("arr"),[Id("j")]),Id("temp"))]),None)]))]),None)]))])
#         )
#         self.assertTrue(TestAST.checkASTGen(input, expect, 367))
#     def test_368(self):
#         input = """
#             type Queue interface {
#                 enqueue(value int);
#                 dequeue() int;
#                 peek() int;
#                 isEmpty() boolean;
#                 isFull() boolean
#             }
#         """
#         expect =  str(
#             Program([InterfaceType("Queue",[Prototype("enqueue",[IntType()],VoidType()),Prototype("dequeue",[],IntType()),Prototype("peek",[],IntType()),Prototype("isEmpty",[],BoolType()),Prototype("isFull",[],BoolType())])])
#         )
#         self.assertTrue(TestAST.checkASTGen(input, expect, 368))
#     def test_369(self):
#         input = """
#             func calculateStats(numbers [100]float) float {
#                 var sum float = 0.0;
#                 var count int = 0;
                
#                 for i := 0; i < 100; i += 1 {
#                     if (numbers[i] > 0.0) {
#                         sum += numbers[i];
#                         count += 1;
#                     }
#                 }
                
#                 return sum / toFloat(count);
#             }
#         """
#         expect =  str(
#             Program([FuncDecl("calculateStats",[ParamDecl("numbers",ArrayType([IntLiteral(100)],FloatType()))],FloatType(),Block([VarDecl("sum",FloatType(),FloatLiteral(0.0)),VarDecl("count",IntType(),IntLiteral(0)),ForStep(Assign(Id("i"),IntLiteral(0)),BinaryOp("<",Id("i"),IntLiteral(100)),Assign(Id("i"),BinaryOp("+",Id("i"),IntLiteral(1))),Block([If(BinaryOp(">",ArrayCell(Id("numbers"),[Id("i")]),FloatLiteral(0.0)),Block([Assign(Id("sum"),BinaryOp("+",Id("sum"),ArrayCell(Id("numbers"),[Id("i")]))),Assign(Id("count"),BinaryOp("+",Id("count"),IntLiteral(1)))]),None)])),Return(BinaryOp("/",Id("sum"),FuncCall("toFloat",[Id("count")])))]))])
#         )
#         self.assertTrue(TestAST.checkASTGen(input, expect, 369))

#     def test_370(self):
#         input = """
#             type HashTable struct {
#                 size int;
#                 table [1000]int;
#             }

#             func (h HashTable) hash(key int) int {
#                 return key % h.size;
#             }
#         """
#         expect =  str(
#             Program([StructType("HashTable",[("size",IntType()),("table",ArrayType([IntLiteral(1000)],IntType()))],[]),MethodDecl("h",Id("HashTable"),FuncDecl("hash",[ParamDecl("key",IntType())],IntType(),Block([Return(BinaryOp("%",Id("key"),FieldAccess(Id("h"),"size")))])))])
#         )
#         self.assertTrue(TestAST.checkASTGen(input, expect, 370))
#     def test_371(self):
#         input = """
#             func gcd(a int, b int) int {
#                 for b != 0 {
#                     temp := b;
#                     b := a % b;
#                     a := temp;
#                 }
#                 return a;
#             }
#         """
#         expect =  str(
#             Program([FuncDecl("gcd",[ParamDecl("a",IntType()),ParamDecl("b",IntType())],IntType(),Block([ForBasic(BinaryOp("!=",Id("b"),IntLiteral(0)),Block([Assign(Id("temp"),Id("b")),Assign(Id("b"),BinaryOp("%",Id("a"),Id("b"))),Assign(Id("a"),Id("temp"))])),Return(Id("a"))]))])
#         )
#         self.assertTrue(TestAST.checkASTGen(input, expect, 371))
#     def test_372(self):
#         input = """
#             func isPrime(n int) boolean {
#                 if (n <= 1) {
#                     return false;
#                 }
#                 for var i = 2; i * i <= n; i += 1 {
#                     if (n % i == 0) {
#                         return false;
#                     }
#                 }
#                 return true;
#             }
#         """
#         expect =  str(
#             Program([FuncDecl("isPrime",[ParamDecl("n",IntType())],BoolType(),Block([If(BinaryOp("<=",Id("n"),IntLiteral(1)),Block([Return(BooleanLiteral(False))]),None),ForStep(Assign(Id("i"),IntLiteral(2)),BinaryOp("<=",BinaryOp("*",Id("i"),Id("i")),Id("n")),Assign(Id("i"),BinaryOp("+",Id("i"),IntLiteral(1))),Block([If(BinaryOp("==",BinaryOp("%",Id("n"),Id("i")),IntLiteral(0)),Block([Return(BooleanLiteral(False))]),None)])),Return(BooleanLiteral(True))]))])
#         )
#         self.assertTrue(TestAST.checkASTGen(input, expect, 372))
#     def test_373(self):
#         input = """
#             type BinaryTreeNode struct {
#                 data int;
#                 left BinaryTreeNode;
#                 right BinaryTreeNode;
#                 parent BinaryTreeNode;
#             }

#             func (node BinaryTreeNode) findMin() BinaryTreeNode {
#                 current := node;
#                 for current.left != nil {
#                     current := current.left;
#                 }
#                 return current;
#             }
#         """
#         expect =  str(
#             Program([StructType("BinaryTreeNode",[("data",IntType()),("left",Id("BinaryTreeNode")),("right",Id("BinaryTreeNode")),("parent",Id("BinaryTreeNode"))],[]),MethodDecl("node",Id("BinaryTreeNode"),FuncDecl("findMin",[],Id("BinaryTreeNode"),Block([Assign(Id("current"),Id("node")),ForBasic(BinaryOp("!=",FieldAccess(Id("current"),"left"),NilLiteral()),Block([Assign(Id("current"),FieldAccess(Id("current"),"left"))])),Return(Id("current"))])))])
#         )
#         self.assertTrue(TestAST.checkASTGen(input, expect, 373))
#     def test_374(self):
#         input = """
#             func mergeSort(arr [100]int, left int, right int) {
#                 if (left < right) {
#                     mid := (left + right) / 2;
#                     mergeSort(arr, left, mid);
#                     mergeSort(arr, mid + 1, right);
#                 }
#             }
#         """
#         expect =  str(
#             Program([FuncDecl("mergeSort",[ParamDecl("arr",ArrayType([IntLiteral(100)],IntType())),ParamDecl("left",IntType()),ParamDecl("right",IntType())],VoidType(),Block([If(BinaryOp("<",Id("left"),Id("right")),Block([Assign(Id("mid"),BinaryOp("/",BinaryOp("+",Id("left"),Id("right")),IntLiteral(2))),FuncCall("mergeSort",[Id("arr"),Id("left"),Id("mid")]),FuncCall("mergeSort",[Id("arr"),BinaryOp("+",Id("mid"),IntLiteral(1)),Id("right")])]),None)]))])
#         )
#         self.assertTrue(TestAST.checkASTGen(input, expect, 374))
#     def test_375(self):
#         input = """
#             func (ht HashTable) resize() {
#                 oldTable := ht.table;
#                 ht.size *= 2;
#                 ht.table := [2000]int{1, 2, 3};
                
#                 for i := 0; i < ht.size / 2; i += 1 {
#                     if (oldTable[i] != 0) {
#                         ht.insert(oldTable[i]);
#                     }
#                 }
#             }
#         """
#         expect =  str(
#             Program([MethodDecl("ht",Id("HashTable"),FuncDecl("resize",[],VoidType(),Block([Assign(Id("oldTable"),FieldAccess(Id("ht"),"table")),Assign(FieldAccess(Id("ht"),"size"),BinaryOp("*",FieldAccess(Id("ht"),"size"),IntLiteral(2))),Assign(FieldAccess(Id("ht"),"table"),ArrayLiteral([IntLiteral(2000)],IntType(),[IntLiteral(1),IntLiteral(2),IntLiteral(3)])),ForStep(Assign(Id("i"),IntLiteral(0)),BinaryOp("<",Id("i"),BinaryOp("/",FieldAccess(Id("ht"),"size"),IntLiteral(2))),Assign(Id("i"),BinaryOp("+",Id("i"),IntLiteral(1))),Block([If(BinaryOp("!=",ArrayCell(Id("oldTable"),[Id("i")]),IntLiteral(0)),Block([MethCall(Id("ht"),"insert",[ArrayCell(Id("oldTable"),[Id("i")])])]),None)]))])))])
#         )
#         self.assertTrue(TestAST.checkASTGen(input, expect, 375))
#     def test_376(self):
#         input = """
#             type Stack struct {
#                 elements [100]int;
#                 top int;
#             }

#             func (s Stack) push(element int) boolean {
#                 if (s.top >= 100) { return false; }
#                 s.elements[s.top] := element;
#                 s.top += 1;
#                 return true;
#             }
#         """
#         expect =  str(
#             Program([StructType("Stack",[("elements",ArrayType([IntLiteral(100)],IntType())),("top",IntType())],[]),MethodDecl("s",Id("Stack"),FuncDecl("push",[ParamDecl("element",IntType())],BoolType(),Block([If(BinaryOp(">=",FieldAccess(Id("s"),"top"),IntLiteral(100)),Block([Return(BooleanLiteral(False))]),None),Assign(ArrayCell(FieldAccess(Id("s"),"elements"),[FieldAccess(Id("s"),"top")]),Id("element")),Assign(FieldAccess(Id("s"),"top"),BinaryOp("+",FieldAccess(Id("s"),"top"),IntLiteral(1))),Return(BooleanLiteral(True))])))])
#         )
#         self.assertTrue(TestAST.checkASTGen(input, expect, 376))
#     def test_377(self):
#         input = """
#             func calculateFactorial(n int) int {
#                 if (n <= 1) { return 1; }
#                 result := 1;
#                 for i := 2; i <= n; i += 1 {
#                     result *= i;
#                 }
#                 return result;
#             }
#         """
#         expect = str(
#             Program([FuncDecl("calculateFactorial",[ParamDecl("n",IntType())],IntType(),Block([If(BinaryOp("<=",Id("n"),IntLiteral(1)),Block([Return(IntLiteral(1))]),None),Assign(Id("result"),IntLiteral(1)),ForStep(Assign(Id("i"),IntLiteral(2)),BinaryOp("<=",Id("i"),Id("n")),Assign(Id("i"),BinaryOp("+",Id("i"),IntLiteral(1))),Block([Assign(Id("result"),BinaryOp("*",Id("result"),Id("i")))])),Return(Id("result"))]))])
#         )
#         self.assertTrue(TestAST.checkASTGen(input, expect, 377))
#     def test_378(self):
#         input = """
#             type CircularQueue struct {
#                 items [100]int;
#                 head int;
#                 tail int;
#                 size int;
#             }

#             func (cq CircularQueue) isFull() boolean {
#                 return cq.size == 100;
#             }
#         """
#         expect =  str(
#             Program([StructType("CircularQueue",[("items",ArrayType([IntLiteral(100)],IntType())),("head",IntType()),("tail",IntType()),("size",IntType())],[]),MethodDecl("cq",Id("CircularQueue"),FuncDecl("isFull",[],BoolType(),Block([Return(BinaryOp("==",FieldAccess(Id("cq"),"size"),IntLiteral(100)))])))])
#         )
#         self.assertTrue(TestAST.checkASTGen(input, expect, 378))
#     def test_379(self):
#         input = """
#             func findLongestCommonPrefix(str1 string, str2 string) string {
#                 minLen := len(str1);
#                 if (len(str2) < minLen) {
#                     minLen := len(str2);
#                 }
                
#                 for i := 0; i < minLen; i += 1 {
#                     if (str1[i] != str2[i]) {
#                         return str1[0];
#                     }
#                 }
#                 return str1[minLen];
#             }
#         """
#         expect =  str(
#             Program([FuncDecl("findLongestCommonPrefix",[ParamDecl("str1",StringType()),ParamDecl("str2",StringType())],StringType(),Block([Assign(Id("minLen"),FuncCall("len",[Id("str1")])),If(BinaryOp("<",FuncCall("len",[Id("str2")]),Id("minLen")),Block([Assign(Id("minLen"),FuncCall("len",[Id("str2")]))]),None),ForStep(Assign(Id("i"),IntLiteral(0)),BinaryOp("<",Id("i"),Id("minLen")),Assign(Id("i"),BinaryOp("+",Id("i"),IntLiteral(1))),Block([If(BinaryOp("!=",ArrayCell(Id("str1"),[Id("i")]),ArrayCell(Id("str2"),[Id("i")])),Block([Return(ArrayCell(Id("str1"),[IntLiteral(0)]))]),None)])),Return(ArrayCell(Id("str1"),[Id("minLen")]))]))])
#         )
#         self.assertTrue(TestAST.checkASTGen(input, expect, 379))
#     def test_380(self):
#         input = """
#             type RGB struct {
#                 red int;
#                 green int;
#                 blue int;
#             }

#             func (color RGB) toGrayscale() int {
#                 return (color.red + color.green + color.blue) / 3;
#             }
#         """
#         expect =  str(
#             Program([StructType("RGB",[("red",IntType()),("green",IntType()),("blue",IntType())],[]),MethodDecl("color",Id("RGB"),FuncDecl("toGrayscale",[],IntType(),Block([Return(BinaryOp("/",BinaryOp("+",BinaryOp("+",FieldAccess(Id("color"),"red"),FieldAccess(Id("color"),"green")),FieldAccess(Id("color"),"blue")),IntLiteral(3)))])))])
#         )
#         self.assertTrue(TestAST.checkASTGen(input, expect, 380))
#     def test_381(self):
#         input = """
#             func isPalindrome(str string) boolean {
#                 length := len(str);
#                 for i := 0; i < length / 2; i += 1 {
#                     if (str[i] != str[length - 1 - i]) {
#                         return false;
#                     }
#                 }
#                 return true;
#             }
#         """
#         expect =  str(
#             Program([FuncDecl("isPalindrome",[ParamDecl("str",StringType())],BoolType(),Block([Assign(Id("length"),FuncCall("len",[Id("str")])),ForStep(Assign(Id("i"),IntLiteral(0)),BinaryOp("<",Id("i"),BinaryOp("/",Id("length"),IntLiteral(2))),Assign(Id("i"),BinaryOp("+",Id("i"),IntLiteral(1))),Block([If(BinaryOp("!=",ArrayCell(Id("str"),[Id("i")]),ArrayCell(Id("str"),[BinaryOp("-",BinaryOp("-",Id("length"),IntLiteral(1)),Id("i"))])),Block([Return(BooleanLiteral(False))]),None)])),Return(BooleanLiteral(True))]))])
#         )
#         self.assertTrue(TestAST.checkASTGen(input, expect, 381))
#     def test_382(self):
#         input = """
#             type Matrix3D struct {
#                 data [10][10][10]float;
#                 rows int;
#                 cols int;
#                 depth int;
#             }

#             func (m Matrix3D) initialize(value float) {
#                 for i := 0; i < m.rows; i += 1 {
#                     for j := 0; j < m.cols; j += 1 {
#                         for k := 0; k < m.depth; k += 1 {
#                             m.data[i][j][k] := value;
#                         }
#                     }
#                 }
#             }
#         """
#         expect =  str(
#             Program([StructType("Matrix3D",[("data",ArrayType([IntLiteral(10),IntLiteral(10),IntLiteral(10)],FloatType())),("rows",IntType()),("cols",IntType()),("depth",IntType())],[]),MethodDecl("m",Id("Matrix3D"),FuncDecl("initialize",[ParamDecl("value",FloatType())],VoidType(),Block([ForStep(Assign(Id("i"),IntLiteral(0)),BinaryOp("<",Id("i"),FieldAccess(Id("m"),"rows")),Assign(Id("i"),BinaryOp("+",Id("i"),IntLiteral(1))),Block([ForStep(Assign(Id("j"),IntLiteral(0)),BinaryOp("<",Id("j"),FieldAccess(Id("m"),"cols")),Assign(Id("j"),BinaryOp("+",Id("j"),IntLiteral(1))),Block([ForStep(Assign(Id("k"),IntLiteral(0)),BinaryOp("<",Id("k"),FieldAccess(Id("m"),"depth")),Assign(Id("k"),BinaryOp("+",Id("k"),IntLiteral(1))),Block([Assign(ArrayCell(FieldAccess(Id("m"),"data"),[Id("i"),Id("j"),Id("k")]),Id("value"))]))]))]))])))])
#         )
#         self.assertTrue(TestAST.checkASTGen(input, expect, 382))
#     def test_383(self):
#         input = """
#             func generateFibonacci(n int) [100]int {
#                 var result [100]int;
#                 if (n <= 0) { return result; }
#                 result[0] := 0;
#                 if (n == 1) { return result; }
#                 result[1] := 1;
#                 for i := 2; i < n; i += 1 {
#                     result[i] := result[i-1] + result[i-2];
#                 }
#                 return result;
#             }
#         """
#         expect =  str(
#             Program([FuncDecl("generateFibonacci",[ParamDecl("n",IntType())],ArrayType([IntLiteral(100)],IntType()),Block([VarDecl("result",ArrayType([IntLiteral(100)],IntType()),None),If(BinaryOp("<=",Id("n"),IntLiteral(0)),Block([Return(Id("result"))]),None),Assign(ArrayCell(Id("result"),[IntLiteral(0)]),IntLiteral(0)),If(BinaryOp("==",Id("n"),IntLiteral(1)),Block([Return(Id("result"))]),None),Assign(ArrayCell(Id("result"),[IntLiteral(1)]),IntLiteral(1)),ForStep(Assign(Id("i"),IntLiteral(2)),BinaryOp("<",Id("i"),Id("n")),Assign(Id("i"),BinaryOp("+",Id("i"),IntLiteral(1))),Block([Assign(ArrayCell(Id("result"),[Id("i")]),BinaryOp("+",ArrayCell(Id("result"),[BinaryOp("-",Id("i"),IntLiteral(1))]),ArrayCell(Id("result"),[BinaryOp("-",Id("i"),IntLiteral(2))])))])),Return(Id("result"))]))])
#         )
#         self.assertTrue(TestAST.checkASTGen(input, expect, 383))
#     def test_384(self):
#         input = """
#             type AVLNode struct {
#                 key int;
#                 height int;
#                 left AVLNode;
#                 right AVLNode;
#             }

#             func (node AVLNode) getHeight() int {
#                 if (node == nil) {
#                     return -1;
#                 }
#                 return node.height;
#             }
#         """
#         expect =  str(
#             Program([StructType("AVLNode",[("key",IntType()),("height",IntType()),("left",Id("AVLNode")),("right",Id("AVLNode"))],[]),MethodDecl("node",Id("AVLNode"),FuncDecl("getHeight",[],IntType(),Block([If(BinaryOp("==",Id("node"),NilLiteral()),Block([Return(UnaryOp("-",IntLiteral(1)))]),None),Return(FieldAccess(Id("node"),"height"))])))])
#         )
#         self.assertTrue(TestAST.checkASTGen(input, expect, 384))
#     def test_385(self):
#         input = """
#             func bubbleSort(arr [100]int) {
#                 n := 100;
#                 swapped := true;
#                 for swapped {
#                     swapped := false;
#                     for i := 1; i < n; i += 1 {
#                         if (arr[i-1] > arr[i]) {
#                             temp := arr[i-1];
#                             arr[i-1] := arr[i];
#                             arr[i] := temp;
#                             swapped := true;
#                         }
#                     }
#                 }
#             }
#         """
#         expect =  str(
#             Program([FuncDecl("bubbleSort",[ParamDecl("arr",ArrayType([IntLiteral(100)],IntType()))],VoidType(),Block([Assign(Id("n"),IntLiteral(100)),Assign(Id("swapped"),BooleanLiteral(True)),ForBasic(Id("swapped"),Block([Assign(Id("swapped"),BooleanLiteral(False)),ForStep(Assign(Id("i"),IntLiteral(1)),BinaryOp("<",Id("i"),Id("n")),Assign(Id("i"),BinaryOp("+",Id("i"),IntLiteral(1))),Block([If(BinaryOp(">",ArrayCell(Id("arr"),[BinaryOp("-",Id("i"),IntLiteral(1))]),ArrayCell(Id("arr"),[Id("i")])),Block([Assign(Id("temp"),ArrayCell(Id("arr"),[BinaryOp("-",Id("i"),IntLiteral(1))])),Assign(ArrayCell(Id("arr"),[BinaryOp("-",Id("i"),IntLiteral(1))]),ArrayCell(Id("arr"),[Id("i")])),Assign(ArrayCell(Id("arr"),[Id("i")]),Id("temp")),Assign(Id("swapped"),BooleanLiteral(True))]),None)]))]))]))])
#         )
#         self.assertTrue(TestAST.checkASTGen(input, expect, 385))
#     def test_386(self):
#         input = """
#             type PriorityQueue interface {
#                 insert(element int, priority int);
#                 deleteMin() int;
#                 decreaseKey(element int, newPriority int);
#                 isEmpty() boolean;
#                 size() int
#             }
#         """
#         expect =  str(
#             Program([InterfaceType("PriorityQueue",[Prototype("insert",[IntType(),IntType()],VoidType()),Prototype("deleteMin",[],IntType()),Prototype("decreaseKey",[IntType(),IntType()],VoidType()),Prototype("isEmpty",[],BoolType()),Prototype("size",[],IntType())])])
#         )
#         self.assertTrue(TestAST.checkASTGen(input, expect, 386))
#     def test_387(self):
#         input = """
#         // full call stmt
#         func power(base float, exponent int) float {
#                 if (exponent == 0) { return 1.0; }
#                 if (exponent < 0) {
#                     base := 1.0 / base;
#                     exponent := -exponent;
#                 }
#                 result := 1.0;
#                 for i := 0; i < exponent; i += 1 {
#                     result *= base;
#                 }
#                 return result;
#             }
#         """
#         expect =  str(
#             Program([FuncDecl("power",[ParamDecl("base",FloatType()),ParamDecl("exponent",IntType())],FloatType(),Block([If(BinaryOp("==",Id("exponent"),IntLiteral(0)),Block([Return(FloatLiteral(1.0))]),None),If(BinaryOp("<",Id("exponent"),IntLiteral(0)),Block([Assign(Id("base"),BinaryOp("/",FloatLiteral(1.0),Id("base"))),Assign(Id("exponent"),UnaryOp("-",Id("exponent")))]),None),Assign(Id("result"),FloatLiteral(1.0)),ForStep(Assign(Id("i"),IntLiteral(0)),BinaryOp("<",Id("i"),Id("exponent")),Assign(Id("i"),BinaryOp("+",Id("i"),IntLiteral(1))),Block([Assign(Id("result"),BinaryOp("*",Id("result"),Id("base")))])),Return(Id("result"))]))])
#         )
#         self.assertTrue(TestAST.checkASTGen(input, expect, 387))
#     def test_388(self):
#         input = """
#         /* Comment */
#             type Fraction struct {
#                 numerator int;
#                 denominator int;
#             }

#             func (f Fraction) simplify() Fraction {
#                 gcd := calculateGCD(f.numerator, f.denominator);
#                 return Fraction(f.numerator / gcd, f.denominator / gcd);
#             }
#         """
#         expect = str(
#             Program([StructType("Fraction",[("numerator",IntType()),("denominator",IntType())],[]),MethodDecl("f",Id("Fraction"),FuncDecl("simplify",[],Id("Fraction"),Block([Assign(Id("gcd"),FuncCall("calculateGCD",[FieldAccess(Id("f"),"numerator"),FieldAccess(Id("f"),"denominator")])),Return(FuncCall("Fraction",[BinaryOp("/",FieldAccess(Id("f"),"numerator"),Id("gcd")),BinaryOp("/",FieldAccess(Id("f"),"denominator"),Id("gcd"))]))])))])
#         )
#         self.assertTrue(TestAST.checkASTGen(input, expect, 388))
#     def test_389(self):
#         input = """
#             func findMaxSubarraySum(arr [100]int) int {
#                 maxSoFar := arr[0];
#                 currMax := arr[0];
                
#                 for i := 1; i < 100; i += 1 {
#                     currMax := max(arr[i], currMax + arr[i]);
#                     maxSoFar := max(maxSoFar, currMax);
#                 }
#                 return maxSoFar;
#             }
#         """
#         expect =  str(
#             Program([FuncDecl("findMaxSubarraySum",[ParamDecl("arr",ArrayType([IntLiteral(100)],IntType()))],IntType(),Block([Assign(Id("maxSoFar"),ArrayCell(Id("arr"),[IntLiteral(0)])),Assign(Id("currMax"),ArrayCell(Id("arr"),[IntLiteral(0)])),ForStep(Assign(Id("i"),IntLiteral(1)),BinaryOp("<",Id("i"),IntLiteral(100)),Assign(Id("i"),BinaryOp("+",Id("i"),IntLiteral(1))),Block([Assign(Id("currMax"),FuncCall("max",[ArrayCell(Id("arr"),[Id("i")]),BinaryOp("+",Id("currMax"),ArrayCell(Id("arr"),[Id("i")]))])),Assign(Id("maxSoFar"),FuncCall("max",[Id("maxSoFar"),Id("currMax")]))])),Return(Id("maxSoFar"))]))])
#         )
#         self.assertTrue(TestAST.checkASTGen(input, expect, 389))
#     def test_390(self):
#         input = """
#             type Vector3D struct {
#                 x float;
#                 y float;
#                 z float;
#             }

#             func (v Vector3D) crossProduct(other Vector3D) Vector3D {
#                 return Vector3D(v.y * other.z - v.z * other.y, v.z * other.x - v.x * other.z, v.x * other.y - v.y * other.x);
#             }
#         """
#         expect =  str(
#             Program([StructType("Vector3D",[("x",FloatType()),("y",FloatType()),("z",FloatType())],[]),MethodDecl("v",Id("Vector3D"),FuncDecl("crossProduct",[ParamDecl("other",Id("Vector3D"))],Id("Vector3D"),Block([Return(FuncCall("Vector3D",[BinaryOp("-",BinaryOp("*",FieldAccess(Id("v"),"y"),FieldAccess(Id("other"),"z")),BinaryOp("*",FieldAccess(Id("v"),"z"),FieldAccess(Id("other"),"y"))),BinaryOp("-",BinaryOp("*",FieldAccess(Id("v"),"z"),FieldAccess(Id("other"),"x")),BinaryOp("*",FieldAccess(Id("v"),"x"),FieldAccess(Id("other"),"z"))),BinaryOp("-",BinaryOp("*",FieldAccess(Id("v"),"x"),FieldAccess(Id("other"),"y")),BinaryOp("*",FieldAccess(Id("v"),"y"),FieldAccess(Id("other"),"x")))]))])))])
#         )
#         self.assertTrue(TestAST.checkASTGen(input, expect, 390))
#     def test_391(self):
#         input = """
#             func countSort(arr [100]int) [100]int {
#                 var count [100]int;
#                 var output [100]int;
                
#                 for i := 0; i < 100; i += 1 {
#                     count[arr[i]] += 1;
#                 }
                
#                 for i := 1; i < 100; i += 1 {
#                     count[i] += count[i-1];
#                 }
                
#                 return output;
#             }
#         """
#         expect =  str(
#             Program([FuncDecl("countSort",[ParamDecl("arr",ArrayType([IntLiteral(100)],IntType()))],ArrayType([IntLiteral(100)],IntType()),Block([VarDecl("count",ArrayType([IntLiteral(100)],IntType()),None),VarDecl("output",ArrayType([IntLiteral(100)],IntType()),None),ForStep(Assign(Id("i"),IntLiteral(0)),BinaryOp("<",Id("i"),IntLiteral(100)),Assign(Id("i"),BinaryOp("+",Id("i"),IntLiteral(1))),Block([Assign(ArrayCell(Id("count"),[ArrayCell(Id("arr"),[Id("i")])]),BinaryOp("+",ArrayCell(Id("count"),[ArrayCell(Id("arr"),[Id("i")])]),IntLiteral(1)))])),ForStep(Assign(Id("i"),IntLiteral(1)),BinaryOp("<",Id("i"),IntLiteral(100)),Assign(Id("i"),BinaryOp("+",Id("i"),IntLiteral(1))),Block([Assign(ArrayCell(Id("count"),[Id("i")]),BinaryOp("+",ArrayCell(Id("count"),[Id("i")]),ArrayCell(Id("count"),[BinaryOp("-",Id("i"),IntLiteral(1))])))])),Return(Id("output"))]))])
#         )
#         self.assertTrue(TestAST.checkASTGen(input, expect, 391))
#     def test_392(self):
#         input = """
#             type WeightedGraph interface {
#                 addEdge(from int, to int, weight float);
#                 removeEdge(from int, to int);
#                 getWeight(from int, to int) float;
#                 isAdjacent(from int, to int) boolean;
#                 getNeighbors(vertex int) [100]int
#             }
#         """
#         expect = str(
#             Program([InterfaceType("WeightedGraph",[Prototype("addEdge",[IntType(),IntType(),FloatType()],VoidType()),Prototype("removeEdge",[IntType(),IntType()],VoidType()),Prototype("getWeight",[IntType(),IntType()],FloatType()),Prototype("isAdjacent",[IntType(),IntType()],BoolType()),Prototype("getNeighbors",[IntType()],ArrayType([IntLiteral(100)],IntType()))])])
#         )
#         self.assertTrue(TestAST.checkASTGen(input, expect, 392))
#     def test_393(self):
#         input = """
#             type Trie struct {
#                 isEndOfWord boolean;
#                 children [26]Trie;
#             }

#             func (t Trie) insert(word string) {
#                 current := t;
#                 for i := 0; i < len(word); i += 1 {
#                     index := word[i] - "a";
#                     if (current.children[index] == nil) {
#                         current.children[index] := Trie{isEndOfWord: false};
#                     }
#                     current := current.children[index];
#                 }
#                 current.isEndOfWord := true;
#             }
#         """
#         expect = str(
#             Program([StructType("Trie",[("isEndOfWord",BoolType()),("children",ArrayType([IntLiteral(26)],Id("Trie")))],[]),MethodDecl("t",Id("Trie"),FuncDecl("insert",[ParamDecl("word",StringType())],VoidType(),Block([Assign(Id("current"),Id("t")),ForStep(Assign(Id("i"),IntLiteral(0)),BinaryOp("<",Id("i"),FuncCall("len",[Id("word")])),Assign(Id("i"),BinaryOp("+",Id("i"),IntLiteral(1))),Block([Assign(Id("index"),BinaryOp("-",ArrayCell(Id("word"),[Id("i")]),StringLiteral("\"a\""))),If(BinaryOp("==",ArrayCell(FieldAccess(Id("current"),"children"),[Id("index")]),NilLiteral()),Block([Assign(ArrayCell(FieldAccess(Id("current"),"children"),[Id("index")]),StructLiteral("Trie",[("isEndOfWord",BooleanLiteral(False))]))]),None),Assign(Id("current"),ArrayCell(FieldAccess(Id("current"),"children"),[Id("index")]))])),Assign(FieldAccess(Id("current"),"isEndOfWord"),BooleanLiteral(True))])))])
#         )
#         self.assertTrue(TestAST.checkASTGen(input, expect, 393))
#     def test_394(self):
#         input = """
#             type BTree struct {
#                 keys [100]int;
#                 children [101]BTree;
#                 count int;
#                 isLeaf boolean;
#             }

#             func (b BTree) splitChild(i int, child BTree) {
#                 newNode := BTree{isLeaf: child.isLeaf};
#                 newNode.count := b.count / 2;
                
#                 for j := 0; j < newNode.count; j += 1 {
#                     newNode.keys[j] := child.keys[j + b.count];
#                 }
                
#                 if (!child.isLeaf) {
#                     for j := 0; j < newNode.count + 1; j += 1 {
#                         newNode.children[j] := child.children[j + b.count];
#                     }
#                 }
                
#                 child.count := b.count / 2;
#                 b.children[i + 1] := newNode;
#             }
#         """
#         expect =  str(
#             Program([StructType("BTree",[("keys",ArrayType([IntLiteral(100)],IntType())),("children",ArrayType([IntLiteral(101)],Id("BTree"))),("count",IntType()),("isLeaf",BoolType())],[]),MethodDecl("b",Id("BTree"),FuncDecl("splitChild",[ParamDecl("i",IntType()),ParamDecl("child",Id("BTree"))],VoidType(),Block([Assign(Id("newNode"),StructLiteral("BTree",[("isLeaf",FieldAccess(Id("child"),"isLeaf"))])),Assign(FieldAccess(Id("newNode"),"count"),BinaryOp("/",FieldAccess(Id("b"),"count"),IntLiteral(2))),ForStep(Assign(Id("j"),IntLiteral(0)),BinaryOp("<",Id("j"),FieldAccess(Id("newNode"),"count")),Assign(Id("j"),BinaryOp("+",Id("j"),IntLiteral(1))),Block([Assign(ArrayCell(FieldAccess(Id("newNode"),"keys"),[Id("j")]),ArrayCell(FieldAccess(Id("child"),"keys"),[BinaryOp("+",Id("j"),FieldAccess(Id("b"),"count"))]))])),If(UnaryOp("!",FieldAccess(Id("child"),"isLeaf")),Block([ForStep(Assign(Id("j"),IntLiteral(0)),BinaryOp("<",Id("j"),BinaryOp("+",FieldAccess(Id("newNode"),"count"),IntLiteral(1))),Assign(Id("j"),BinaryOp("+",Id("j"),IntLiteral(1))),Block([Assign(ArrayCell(FieldAccess(Id("newNode"),"children"),[Id("j")]),ArrayCell(FieldAccess(Id("child"),"children"),[BinaryOp("+",Id("j"),FieldAccess(Id("b"),"count"))]))]))]),None),Assign(FieldAccess(Id("child"),"count"),BinaryOp("/",FieldAccess(Id("b"),"count"),IntLiteral(2))),Assign(ArrayCell(FieldAccess(Id("b"),"children"),[BinaryOp("+",Id("i"),IntLiteral(1))]),Id("newNode"))])))])
#         )
#         self.assertTrue(TestAST.checkASTGen(input, expect, 394))
#     def test_395(self):
#         input = """
#             type RedBlackNode struct {
#                 key int;
#                 color boolean;
#                 left RedBlackNode;
#                 right RedBlackNode;
#                 parent RedBlackNode;
#             }

#             func (tree RedBlackNode) rotateLeft(node RedBlackNode) {
#                 rightChild := node.right;
#                 node.right := rightChild.left;
                
#                 if (rightChild.left != nil) {
#                     rightChild.left.parent := node;
#                 }
                
#                 rightChild.parent := node.parent;
                
#                 if (node.parent == nil) {
#                     tree := rightChild;
#                 } else if (node == node.parent.left) {
#                     node.parent.left := rightChild;
#                 } else {
#                     node.parent.right := rightChild;
#                 }
                
#                 rightChild.left := node;
#                 node.parent := rightChild;
#             }
#         """
#         expect =  str(
#             Program([StructType("RedBlackNode",[("key",IntType()),("color",BoolType()),("left",Id("RedBlackNode")),("right",Id("RedBlackNode")),("parent",Id("RedBlackNode"))],[]),MethodDecl("tree",Id("RedBlackNode"),FuncDecl("rotateLeft",[ParamDecl("node",Id("RedBlackNode"))],VoidType(),Block([Assign(Id("rightChild"),FieldAccess(Id("node"),"right")),Assign(FieldAccess(Id("node"),"right"),FieldAccess(Id("rightChild"),"left")),If(BinaryOp("!=",FieldAccess(Id("rightChild"),"left"),NilLiteral()),Block([Assign(FieldAccess(FieldAccess(Id("rightChild"),"left"),"parent"),Id("node"))]),None),Assign(FieldAccess(Id("rightChild"),"parent"),FieldAccess(Id("node"),"parent")),If(BinaryOp("==",FieldAccess(Id("node"),"parent"),NilLiteral()),Block([Assign(Id("tree"),Id("rightChild"))]),If(BinaryOp("==",Id("node"),FieldAccess(FieldAccess(Id("node"),"parent"),"left")),Block([Assign(FieldAccess(FieldAccess(Id("node"),"parent"),"left"),Id("rightChild"))]),Block([Assign(FieldAccess(FieldAccess(Id("node"),"parent"),"right"),Id("rightChild"))]))),Assign(FieldAccess(Id("rightChild"),"left"),Id("node")),Assign(FieldAccess(Id("node"),"parent"),Id("rightChild"))])))])
#         )
#         self.assertTrue(TestAST.checkASTGen(input, expect, 395))
#     def test_396(self):
#         input = """
#             type Graph struct {
#                 vertices int;
#                 adjMatrix [100][100]float;
#             }

#             func (g Graph) floydWarshall() [100][100]float {
#                 var dist [100][100]float;
                
#                 for i := 0; i < g.vertices; i += 1 {
#                     for j := 0; j < g.vertices; j += 1 {
#                         dist[i][j] := g.adjMatrix[i][j];
#                     }
#                 }
                
#                 for k := 0; k < g.vertices; k += 1 {
#                     for i := 0; i < g.vertices; i += 1 {
#                         for j := 0; j < g.vertices; j += 1 {
#                             if (dist[i][k] + dist[k][j] < dist[i][j]) {
#                                 dist[i][j] := dist[i][k] + dist[k][j];
#                             }
#                         }
#                     }
#                 }
#                 return dist;
#             }
#         """
#         expect =  str(
#             Program([StructType("Graph",[("vertices",IntType()),("adjMatrix",ArrayType([IntLiteral(100),IntLiteral(100)],FloatType()))],[]),MethodDecl("g",Id("Graph"),FuncDecl("floydWarshall",[],ArrayType([IntLiteral(100),IntLiteral(100)],FloatType()),Block([VarDecl("dist",ArrayType([IntLiteral(100),IntLiteral(100)],FloatType()),None),ForStep(Assign(Id("i"),IntLiteral(0)),BinaryOp("<",Id("i"),FieldAccess(Id("g"),"vertices")),Assign(Id("i"),BinaryOp("+",Id("i"),IntLiteral(1))),Block([ForStep(Assign(Id("j"),IntLiteral(0)),BinaryOp("<",Id("j"),FieldAccess(Id("g"),"vertices")),Assign(Id("j"),BinaryOp("+",Id("j"),IntLiteral(1))),Block([Assign(ArrayCell(Id("dist"),[Id("i"),Id("j")]),ArrayCell(FieldAccess(Id("g"),"adjMatrix"),[Id("i"),Id("j")]))]))])),ForStep(Assign(Id("k"),IntLiteral(0)),BinaryOp("<",Id("k"),FieldAccess(Id("g"),"vertices")),Assign(Id("k"),BinaryOp("+",Id("k"),IntLiteral(1))),Block([ForStep(Assign(Id("i"),IntLiteral(0)),BinaryOp("<",Id("i"),FieldAccess(Id("g"),"vertices")),Assign(Id("i"),BinaryOp("+",Id("i"),IntLiteral(1))),Block([ForStep(Assign(Id("j"),IntLiteral(0)),BinaryOp("<",Id("j"),FieldAccess(Id("g"),"vertices")),Assign(Id("j"),BinaryOp("+",Id("j"),IntLiteral(1))),Block([If(BinaryOp("<",BinaryOp("+",ArrayCell(Id("dist"),[Id("i"),Id("k")]),ArrayCell(Id("dist"),[Id("k"),Id("j")])),ArrayCell(Id("dist"),[Id("i"),Id("j")])),Block([Assign(ArrayCell(Id("dist"),[Id("i"),Id("j")]),BinaryOp("+",ArrayCell(Id("dist"),[Id("i"),Id("k")]),ArrayCell(Id("dist"),[Id("k"),Id("j")])))]),None)]))]))])),Return(Id("dist"))])))])
#         )
#         self.assertTrue(TestAST.checkASTGen(input, expect, 396))
#     def test_397(self):
#         input = """
#             type Heap struct {
#                 data [100]int;
#                 size int;
#             }

#             func (h Heap) heapifyDown(index int) {
#                 smallest := index;
#                 left := 2 * index + 1;
#                 right := 2 * index + 2;

#                 if (left < h.size && h.data[left] < h.data[smallest]) {
#                     smallest := left;
#                 }

#                 if (right < h.size && h.data[right] < h.data[smallest]) {
#                     smallest := right;
#                 }

#                 if (smallest != index) {
#                     temp := h.data[index];
#                     h.data[index] := h.data[smallest];
#                     h.data[smallest] := temp;
#                     h.heapifyDown(smallest);
#                 }
#             }
#         """
#         expect = str(
#             Program([StructType("Heap",[("data",ArrayType([IntLiteral(100)],IntType())),("size",IntType())],[]),MethodDecl("h",Id("Heap"),FuncDecl("heapifyDown",[ParamDecl("index",IntType())],VoidType(),Block([Assign(Id("smallest"),Id("index")),Assign(Id("left"),BinaryOp("+",BinaryOp("*",IntLiteral(2),Id("index")),IntLiteral(1))),Assign(Id("right"),BinaryOp("+",BinaryOp("*",IntLiteral(2),Id("index")),IntLiteral(2))),If(BinaryOp("&&",BinaryOp("<",Id("left"),FieldAccess(Id("h"),"size")),BinaryOp("<",ArrayCell(FieldAccess(Id("h"),"data"),[Id("left")]),ArrayCell(FieldAccess(Id("h"),"data"),[Id("smallest")]))),Block([Assign(Id("smallest"),Id("left"))]),None),If(BinaryOp("&&",BinaryOp("<",Id("right"),FieldAccess(Id("h"),"size")),BinaryOp("<",ArrayCell(FieldAccess(Id("h"),"data"),[Id("right")]),ArrayCell(FieldAccess(Id("h"),"data"),[Id("smallest")]))),Block([Assign(Id("smallest"),Id("right"))]),None),If(BinaryOp("!=",Id("smallest"),Id("index")),Block([Assign(Id("temp"),ArrayCell(FieldAccess(Id("h"),"data"),[Id("index")])),Assign(ArrayCell(FieldAccess(Id("h"),"data"),[Id("index")]),ArrayCell(FieldAccess(Id("h"),"data"),[Id("smallest")])),Assign(ArrayCell(FieldAccess(Id("h"),"data"),[Id("smallest")]),Id("temp")),MethCall(Id("h"),"heapifyDown",[Id("smallest")])]),None)])))])
#         )
#         self.assertTrue(TestAST.checkASTGen(input, expect, 397))
#     def test_398(self):
#         input = """
#             type DynamicArray struct {
#                 elements [100]int;
#                 size int;
#                 capacity int;
#             }

#             func (da DynamicArray) resize() {
#                 newCapacity := da.capacity * 2;
#                 var newElements [100]int;
                
#                 for i := 0; i < da.size; i += 1 {
#                     newElements[i] := da.elements[i];
#                 }
                
#                 da.elements := newElements;
#                 da.capacity := newCapacity;
#             }

#             func (da DynamicArray) add(element int) {
#                 if (da.size == da.capacity) {
#                     da.resize();
#                 }
#                 da.elements[da.size] := element;
#                 da.size += 1;
#             }
#         """
#         expect = str(
#             Program([StructType("DynamicArray",[("elements",ArrayType([IntLiteral(100)],IntType())),("size",IntType()),("capacity",IntType())],[]),MethodDecl("da",Id("DynamicArray"),FuncDecl("resize",[],VoidType(),Block([Assign(Id("newCapacity"),BinaryOp("*",FieldAccess(Id("da"),"capacity"),IntLiteral(2))),VarDecl("newElements",ArrayType([IntLiteral(100)],IntType()),None),ForStep(Assign(Id("i"),IntLiteral(0)),BinaryOp("<",Id("i"),FieldAccess(Id("da"),"size")),Assign(Id("i"),BinaryOp("+",Id("i"),IntLiteral(1))),Block([Assign(ArrayCell(Id("newElements"),[Id("i")]),ArrayCell(FieldAccess(Id("da"),"elements"),[Id("i")]))])),Assign(FieldAccess(Id("da"),"elements"),Id("newElements")),Assign(FieldAccess(Id("da"),"capacity"),Id("newCapacity"))]))),MethodDecl("da",Id("DynamicArray"),FuncDecl("add",[ParamDecl("element",IntType())],VoidType(),Block([If(BinaryOp("==",FieldAccess(Id("da"),"size"),FieldAccess(Id("da"),"capacity")),Block([MethCall(Id("da"),"resize",[])]),None),Assign(ArrayCell(FieldAccess(Id("da"),"elements"),[FieldAccess(Id("da"),"size")]),Id("element")),Assign(FieldAccess(Id("da"),"size"),BinaryOp("+",FieldAccess(Id("da"),"size"),IntLiteral(1)))])))])
#         )
#         self.assertTrue(TestAST.checkASTGen(input, expect, 398))
#     def test_399(self):
#         input = """
#             type SegmentTree struct {
#                 tree [400]int;
#                 lazy [400]int;
#             }

#             func (st SegmentTree) updateRange(node int, start int, end int, l int, r int, val int) {
#                 if (st.lazy[node] != 0) {
#                     st.tree[node] += (end - start + 1) * st.lazy[node];
#                     if (start != end) {
#                         st.lazy[node * 2] += st.lazy[node];
#                         st.lazy[node * 2 + 1] += st.lazy[node];
#                     }
#                     st.lazy[node] := 0;
#                 }

#                 if (start > end || start > r || end < l) {
#                     return;
#                 }

#                 if (start >= l && end <= r) {
#                     st.tree[node] += (end - start + 1) * val;
#                     if (start != end) {
#                         st.lazy[node * 2] += val;
#                         st.lazy[node * 2 + 1] += val;
#                     }
#                     return;
#                 }

#                 mid := (start + end) / 2;
#                 st.updateRange(node * 2, start, mid, l, r, val);
#                 st.updateRange(node * 2 + 1, mid + 1, end, l, r, val);
#                 st.tree[node] := st.tree[node * 2] + st.tree[node * 2 + 1];
#             }
#         """
#         expect =  str(
#             Program([StructType("SegmentTree",[("tree",ArrayType([IntLiteral(400)],IntType())),("lazy",ArrayType([IntLiteral(400)],IntType()))],[]),MethodDecl("st",Id("SegmentTree"),FuncDecl("updateRange",[ParamDecl("node",IntType()),ParamDecl("start",IntType()),ParamDecl("end",IntType()),ParamDecl("l",IntType()),ParamDecl("r",IntType()),ParamDecl("val",IntType())],VoidType(),Block([If(BinaryOp("!=",ArrayCell(FieldAccess(Id("st"),"lazy"),[Id("node")]),IntLiteral(0)),Block([Assign(ArrayCell(FieldAccess(Id("st"),"tree"),[Id("node")]),BinaryOp("+",ArrayCell(FieldAccess(Id("st"),"tree"),[Id("node")]),BinaryOp("*",BinaryOp("+",BinaryOp("-",Id("end"),Id("start")),IntLiteral(1)),ArrayCell(FieldAccess(Id("st"),"lazy"),[Id("node")])))),If(BinaryOp("!=",Id("start"),Id("end")),Block([Assign(ArrayCell(FieldAccess(Id("st"),"lazy"),[BinaryOp("*",Id("node"),IntLiteral(2))]),BinaryOp("+",ArrayCell(FieldAccess(Id("st"),"lazy"),[BinaryOp("*",Id("node"),IntLiteral(2))]),ArrayCell(FieldAccess(Id("st"),"lazy"),[Id("node")]))),Assign(ArrayCell(FieldAccess(Id("st"),"lazy"),[BinaryOp("+",BinaryOp("*",Id("node"),IntLiteral(2)),IntLiteral(1))]),BinaryOp("+",ArrayCell(FieldAccess(Id("st"),"lazy"),[BinaryOp("+",BinaryOp("*",Id("node"),IntLiteral(2)),IntLiteral(1))]),ArrayCell(FieldAccess(Id("st"),"lazy"),[Id("node")])))]),None),Assign(ArrayCell(FieldAccess(Id("st"),"lazy"),[Id("node")]),IntLiteral(0))]),None),If(BinaryOp("||",BinaryOp("||",BinaryOp(">",Id("start"),Id("end")),BinaryOp(">",Id("start"),Id("r"))),BinaryOp("<",Id("end"),Id("l"))),Block([Return(None)]),None),If(BinaryOp("&&",BinaryOp(">=",Id("start"),Id("l")),BinaryOp("<=",Id("end"),Id("r"))),Block([Assign(ArrayCell(FieldAccess(Id("st"),"tree"),[Id("node")]),BinaryOp("+",ArrayCell(FieldAccess(Id("st"),"tree"),[Id("node")]),BinaryOp("*",BinaryOp("+",BinaryOp("-",Id("end"),Id("start")),IntLiteral(1)),Id("val")))),If(BinaryOp("!=",Id("start"),Id("end")),Block([Assign(ArrayCell(FieldAccess(Id("st"),"lazy"),[BinaryOp("*",Id("node"),IntLiteral(2))]),BinaryOp("+",ArrayCell(FieldAccess(Id("st"),"lazy"),[BinaryOp("*",Id("node"),IntLiteral(2))]),Id("val"))),Assign(ArrayCell(FieldAccess(Id("st"),"lazy"),[BinaryOp("+",BinaryOp("*",Id("node"),IntLiteral(2)),IntLiteral(1))]),BinaryOp("+",ArrayCell(FieldAccess(Id("st"),"lazy"),[BinaryOp("+",BinaryOp("*",Id("node"),IntLiteral(2)),IntLiteral(1))]),Id("val")))]),None),Return(None)]),None),Assign(Id("mid"),BinaryOp("/",BinaryOp("+",Id("start"),Id("end")),IntLiteral(2))),MethCall(Id("st"),"updateRange",[BinaryOp("*",Id("node"),IntLiteral(2)),Id("start"),Id("mid"),Id("l"),Id("r"),Id("val")]),MethCall(Id("st"),"updateRange",[BinaryOp("+",BinaryOp("*",Id("node"),IntLiteral(2)),IntLiteral(1)),BinaryOp("+",Id("mid"),IntLiteral(1)),Id("end"),Id("l"),Id("r"),Id("val")]),Assign(ArrayCell(FieldAccess(Id("st"),"tree"),[Id("node")]),BinaryOp("+",ArrayCell(FieldAccess(Id("st"),"tree"),[BinaryOp("*",Id("node"),IntLiteral(2))]),ArrayCell(FieldAccess(Id("st"),"tree"),[BinaryOp("+",BinaryOp("*",Id("node"),IntLiteral(2)),IntLiteral(1))])))])))])
#         )
#         self.assertTrue(TestAST.checkASTGen(input, expect, 399))
        