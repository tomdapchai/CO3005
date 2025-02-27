import unittest
from TestUtils import TestAST
from AST import *

class ASTGenSuite(unittest.TestCase):
    def test_simple_program_300(self):
        input = """func main() {x := 1+2; };"""
        expect = str(Program([FuncDecl("main",[],VoidType(),Block([Assign(Id("x"),BinaryOp("+",IntLiteral(1),IntLiteral(2)))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,300))

    def test_more_complex_program_301(self):
        input = """var x int ;"""
        expect = str(Program([VarDecl("x",IntType(),None)]))
        self.assertTrue(TestAST.checkASTGen(input,expect,301))
    
    def test_302(self):
        input = """func main () {var b int;}; var x int ;"""
        expect = str(Program([FuncDecl("main",[],VoidType(),Block([VarDecl("b",IntType(), None)])),VarDecl("x",IntType(), None)]))
        self.assertTrue(TestAST.checkASTGen(input,expect,302))
    def test_303(self):
        input = """
        var a[5][6] int;
        var b[5] int;
        """
        expect = str(
              Program([
                VarDecl("a",ArrayType([IntLiteral(5),IntLiteral(6)],IntType()),None),
                VarDecl("b",ArrayType([IntLiteral(5)],IntType()),None)
              ])
        )
        self.assertTrue(TestAST.checkASTGen(input,expect,303))
    def test_304(self):
        input = """
        func main() {
            foo(1+x/y, 2);
        }
        """
        expect = str(
              Program([
                FuncDecl("main",[],VoidType(),Block([FuncCall("foo",[BinaryOp("+",IntLiteral(1),BinaryOp("/",Id("x"),Id("y"))),IntLiteral(2)])]))
              ])
        )
        self.assertTrue(TestAST.checkASTGen(input,expect,304))
    def test_305(self):
        input = """
        const x = 5;
        const y = 6;
        const z = x+y;
        """
        expect = str(
              Program([
                ConstDecl("x",None,IntLiteral(5)),
                ConstDecl("y",None,IntLiteral(6)),
                ConstDecl("z",None,BinaryOp("+",Id("x"),Id("y")))
              ])
        )
        self.assertTrue(TestAST.checkASTGen(input,expect,305))
    def test_306(self):
        input = """
        var a boolean;
        var b boolean = true;
        var c = a && b;
        var e = !a;
        """
        expect = str(
              Program([
                VarDecl("a",BoolType(),None),
                VarDecl("b",BoolType(),BooleanLiteral(True)),
                VarDecl("c",None,BinaryOp("&&",Id("a"),Id("b"))),
                VarDecl("e",None,UnaryOp("!",Id("a")))
              ])
        )
        self.assertTrue(TestAST.checkASTGen(input,expect,306))
    def test_307(self):
        input = """
        var a int;
        var b int = 5;
        var c = a + b;
        var d = a - b;
        var e = a * b;
        var f = a / b;
        var g = a % b;
        """
        expect = str(
              Program([
                VarDecl("a",IntType(),None),
                VarDecl("b",IntType(),IntLiteral(5)),
                VarDecl("c",None,BinaryOp("+",Id("a"),Id("b"))),
                VarDecl("d",None,BinaryOp("-",Id("a"),Id("b"))),
                VarDecl("e",None,BinaryOp("*",Id("a"),Id("b"))),
                VarDecl("f",None,BinaryOp("/",Id("a"),Id("b"))),
                VarDecl("g",None,BinaryOp("%",Id("a"),Id("b")))
              ])
        )
        self.assertTrue(TestAST.checkASTGen(input,expect,307))
    def test_308(self):
        input = """
        var a float;
        var b float = 5.5;
        var c = a + b;
        var d = a > b;
        var e = a < b;
        var f = a >= b;
        var g = a <= b;
        var h = a != b;
        var i = a == b;
        """
        expect = str(
                Program([
                    VarDecl("a",FloatType(),None),
                    VarDecl("b",FloatType(),FloatLiteral(5.5)),
                    VarDecl("c",None,BinaryOp("+",Id("a"),Id("b"))),
                    VarDecl("d",None,BinaryOp(">",Id("a"),Id("b"))),
                    VarDecl("e",None,BinaryOp("<",Id("a"),Id("b"))),
                    VarDecl("f",None,BinaryOp(">=",Id("a"),Id("b"))),
                    VarDecl("g",None,BinaryOp("<=",Id("a"),Id("b"))),
                    VarDecl("h",None,BinaryOp("!=",Id("a"),Id("b"))),
                    VarDecl("i",None,BinaryOp("==",Id("a"),Id("b")))
                ])
        )
        self.assertTrue(TestAST.checkASTGen(input,expect,308))
    def test_309(self):
        input = """
        var a string;
        var b string = "Hello";
        var c = a + b;
        var d = a > b;
        var e = a < b;
        var f = a >= b;
        var g = a <= b;
        var h = a != b;
        var i = a == b;
        """
        expect = str(
                Program([
                    VarDecl("a",StringType(),None),
                    VarDecl("b",StringType(),StringLiteral("\"Hello\"")),
                    VarDecl("c",None,BinaryOp("+",Id("a"),Id("b"))),
                    VarDecl("d",None,BinaryOp(">",Id("a"),Id("b"))),
                    VarDecl("e",None,BinaryOp("<",Id("a"),Id("b"))),
                    VarDecl("f",None,BinaryOp(">=",Id("a"),Id("b"))),
                    VarDecl("g",None,BinaryOp("<=",Id("a"),Id("b"))),
                    VarDecl("h",None,BinaryOp("!=",Id("a"),Id("b"))),
                    VarDecl("i",None,BinaryOp("==",Id("a"),Id("b")))
                ])
        )
        self.assertTrue(TestAST.checkASTGen(input,expect,309))
    def test_310(self):
        input = """
        var a[5]int;
        var b[3][3] int;
        var c[3][3][3] float;
        var d[3][3][3] Person;
        """
        expect = str(
                Program([
                    VarDecl("a",ArrayType([IntLiteral(5)],IntType()),None),
                    VarDecl("b",ArrayType([IntLiteral(3),IntLiteral(3)],IntType()),None),
                    VarDecl("c",ArrayType([IntLiteral(3),IntLiteral(3),IntLiteral(3)],FloatType()),None),
                    VarDecl("d",ArrayType([IntLiteral(3),IntLiteral(3),IntLiteral(3)],Id("Person")),None)
                ])
        )
        self.assertTrue(TestAST.checkASTGen(input,expect,310))
    def test_311(self):
        input = """
        type Person struct {
            name string;
            age int;
        }
        type Student struct {
            person Person;
            grade float;
        }
        func main() {
            p := Person{name: "John", age: 25};
            s := Student{person: p, grade: 8.5};
        }
        """
        expect = str(
                Program([
                    StructType("Person",[("name", StringType()),("age", IntType())], []),
                    StructType("Student",[("person", Id("Person")),("grade", FloatType())], []),
                    FuncDecl("main",[],VoidType(),Block([
                        Assign(Id("p"),StructLiteral("Person",[("name",StringLiteral("\"John\"")),("age",IntLiteral(25))])),
                        Assign(Id("s"),StructLiteral("Student",[("person",Id("p")),("grade",FloatLiteral(8.5))]))
                    ]))
                ])
        )
        self.assertTrue(TestAST.checkASTGen(input,expect,311))
    def test_312(self):
        input = """
        type Person interface {
            getName() string;
            getAge() int;
            getGrade() float
            printInfo()
            setAge(age int) 
        }
        """
        expect = str(
                Program([
                    InterfaceType("Person",[
                        Prototype("getName",[],StringType()),
                        Prototype("getAge",[],IntType()),
                        Prototype("getGrade",[],FloatType()),
                        Prototype("printInfo",[],VoidType()),
                        Prototype("setAge",[IntType()],VoidType())
                    ])
                ])
        )
        self.assertTrue(TestAST.checkASTGen(input,expect,312))
    def test_313(self):
        input = """
        type Person struct {
            name string;
            age int;
        }
        type Student struct {
            person Person;
            grade float;
        }
        type Teacher struct {
            person Person;
            salary float;
        }
        func main() {
            p := Person{name: "John", age: 25};
            s := Student{person: p, grade: 8.5};
            t := Teacher{person: p, salary: 1000.9};
            age := p.age;
            age1 := s.person.age;
            age2 := t.person.age;
            total := s.grade + t.salary;
        }
        """
        expect = str(
                Program([
                    StructType("Person",[("name", StringType()),("age", IntType())], []),
                    StructType("Student",[("person", Id("Person")),("grade", FloatType())], []),
                    StructType("Teacher",[("person", Id("Person")),("salary", FloatType())], []),
                    FuncDecl("main",[],VoidType(),Block([
                        Assign(Id("p"),StructLiteral("Person",[("name",StringLiteral("\"John\"")),("age",IntLiteral(25))])),
                        Assign(Id("s"),StructLiteral("Student",[("person",Id("p")),("grade",FloatLiteral(8.5))])),
                        Assign(Id("t"),StructLiteral("Teacher",[("person",Id("p")),("salary",FloatLiteral(1000.9))])),
                        Assign(Id("age"),FieldAccess(Id("p"),"age")),
                        Assign(Id("age1"),FieldAccess(FieldAccess(Id("s"),"person"),"age")),
                        Assign(Id("age2"),FieldAccess(FieldAccess(Id("t"),"person"),"age")),
                        Assign(Id("total"),BinaryOp("+",FieldAccess(Id("s"),"grade"),FieldAccess(Id("t"),"salary")))
                    ]))
                ])
        )
        # print(expect)
        self.assertTrue(TestAST.checkASTGen(input,expect,313))
    def test_314(self):
        input = """
        var a[5]int;
        var b[3][3] int;
        var c[3][3][3] float;
        var d[3][3][3] Person;
        func main() {
            a := [5]int{1,2,3,4,5};
            b := [3][3]int{{1,2,3},{4,5,6},{7,8,9}};
        }
        """
        expect = str(
                Program([
                    VarDecl("a",ArrayType([IntLiteral(5)],IntType()),None),
                    VarDecl("b",ArrayType([IntLiteral(3),IntLiteral(3)],IntType()),None),
                    VarDecl("c",ArrayType([IntLiteral(3),IntLiteral(3),IntLiteral(3)],FloatType()),None),
                    VarDecl("d",ArrayType([IntLiteral(3),IntLiteral(3),IntLiteral(3)],Id("Person")),None),
                    FuncDecl("main",[],VoidType(),Block([
                        Assign(Id("a"),ArrayLiteral([IntLiteral(5)],IntType(),[IntLiteral(1),IntLiteral(2),IntLiteral(3),IntLiteral(4),IntLiteral(5)])),
                        Assign(Id("b"),ArrayLiteral([IntLiteral(3), IntLiteral(3)], IntType(), [[IntLiteral(1),IntLiteral(2),IntLiteral(3)],[IntLiteral(4),IntLiteral(5),IntLiteral(6)],[IntLiteral(7),IntLiteral(8),IntLiteral(9)]]))
                    ]))
                ])
        )
        self.assertTrue(TestAST.checkASTGen(input,expect,314))
    def test_315(self):
        input = """
        type Person struct {
            name string;
            age int;
        }
        func (p Person) getName() string {
            return p.name;
        }
        func main() {
            p := Person{name: "John", age: 25};
            var a Person;
            a := p;
            var b = a.name;
            var c = a.age;
        }
        """
        expect = str(
                Program([
                    StructType("Person",[("name", StringType()),("age", IntType())], []),
                    MethodDecl("p",Id("Person"), FuncDecl("getName", [],StringType(),Block([Return(FieldAccess(Id("p"),"name"))]))),
                    FuncDecl("main",[],VoidType(),Block([
                        Assign(Id("p"),StructLiteral("Person",[("name",StringLiteral("\"John\"")),("age",IntLiteral(25))])),
                        VarDecl("a",Id("Person"),None),
                        Assign(Id("a"),Id("p")),
                        VarDecl("b",None,FieldAccess(Id("a"),"name")),
                        VarDecl("c",None,FieldAccess(Id("a"),"age"))
                    ]))
                ])
        )
        # print(expect)
        self.assertTrue(TestAST.checkASTGen(input,expect,315))
    def test_316(self):
        input = """
        func foo() {
            putString("Hello");
        }
        func bar(a int, b float) {
            putInt(a);
            putFloat(b);
        }
        func main(){
            foo();
            bar(5, 5.5);
        }
        """
        expect = str(
            Program([
                FuncDecl("foo",[],VoidType(),Block([FuncCall("putString",[StringLiteral("\"Hello\"")])])),
                FuncDecl("bar",[ParamDecl("a", IntType()), ParamDecl("b", FloatType())],VoidType(),Block([FuncCall("putInt",[Id("a")]),FuncCall("putFloat",[Id("b")])])),
                FuncDecl("main",[],VoidType(),Block([FuncCall("foo",[]),FuncCall("bar",[IntLiteral(5),FloatLiteral(5.5)])]))
            ])
        )
        self.assertTrue(TestAST.checkASTGen(input,expect,316))
    def test_317(self):
        input = """
        func foo() int {
            return 5;
        }
        func bar(a int, b float) float {
            return a + b;
        }
        func main() {
            putInt(foo());
            putFloat(bar(5, 5.5));
        }
        """
        expect = str(
            Program(
                [
                    FuncDecl("foo",[],IntType(),Block([Return(IntLiteral(5))])),
                    FuncDecl("bar",[ParamDecl("a", IntType()), ParamDecl("b", FloatType())],FloatType(),Block([Return(BinaryOp("+",Id("a"),Id("b")))])),
                    FuncDecl("main",[],VoidType(),Block([FuncCall("putInt",[FuncCall("foo",[])]),FuncCall("putFloat",[FuncCall("bar",[IntLiteral(5),FloatLiteral(5.5)])])]))
                ]
            )
        )
        self.assertTrue(TestAST.checkASTGen(input,expect,317))
    def test_318(self):
        input = """
        type Person struct {
            name string;
            age int;
            grades [5]Subject;
        }
        func (p Person) printInfo() {
            putString(p.name);
            putInt(p.age);
        }
        func main() {
            p := Person{name: "John", age: 25};
            p.printInfo();
            putString(p.name);
            putInt(p.age);
            putFloat(p.grades[0].score);
        }
        """
        expect = str(
            Program(
                [
                    StructType("Person",[("name", StringType()),("age", IntType()),("grades",ArrayType([IntLiteral(5)],Id("Subject")))], []),
                    MethodDecl("p",Id("Person"), FuncDecl("printInfo", [],VoidType(),Block([FuncCall("putString",[FieldAccess(Id("p"),"name")]),FuncCall("putInt",[FieldAccess(Id("p"),"age")])]))),
                    FuncDecl("main",[],VoidType(),Block([
                        Assign(Id("p"),StructLiteral("Person",[("name",StringLiteral("\"John\"")),("age",IntLiteral(25))])),
                        MethCall(Id("p"),"printInfo",[]),
                        FuncCall("putString",[FieldAccess(Id("p"),"name")]),
                        FuncCall("putInt",[FieldAccess(Id("p"),"age")]),
                        FuncCall("putFloat",[FieldAccess(ArrayCell(FieldAccess(Id("p"),"grades"),[IntLiteral(0)]),"score")])
                    ]))
                ]
            )
        )
        self.assertTrue(TestAST.checkASTGen(input,expect,318))
    def test_319(self):
        input = """
        func foo() {
            if (x > 10) {
                putString("x is greater than 10");
            }
        }
        """
        expect = str(
            Program(
                [
                    FuncDecl("foo",[],VoidType(),Block([If(BinaryOp(">",Id("x"),IntLiteral(10)),Block([FuncCall("putString",[StringLiteral("\"x is greater than 10\"")])]), None)]))
                ]
            )
        )
        self.assertTrue(TestAST.checkASTGen(input,expect,319))
    def test_320(self):
        input = """
        func main() {
            if (a > b){
                putString("a is greater than b");
            } else {
                putString("a is not greater than b");
            }
        }
        """
        expect = str(
            Program(
                [
                    FuncDecl("main",[],VoidType(),
                             Block(
                            [If(BinaryOp(">",Id("a"),Id("b")),
                                Block([FuncCall("putString",[StringLiteral("\"a is greater than b\"")])]),
                                Block([FuncCall("putString",[StringLiteral("\"a is not greater than b\"")])]))]))
                ]
            )
        )
        self.assertTrue(TestAST.checkASTGen(input,expect,320))
    def test_321(self):
        input = """
        func main() {
            if (a > b){
                putString("a is greater than b");
            } else if (a < b) {
                putString("a is less than b");
            } else {
                putString("a is equal to b");
            }
        }
        """
        expect = str(
            Program(
                [
                    FuncDecl("main",[],VoidType(),
                             Block(
                            [If(BinaryOp(">",Id("a"),Id("b")),
                                Block([FuncCall("putString",[StringLiteral("\"a is greater than b\"")])]),
                                If(BinaryOp("<",Id("a"),Id("b")),
                                   Block([FuncCall("putString",[StringLiteral("\"a is less than b\"")])]),
                                   Block([FuncCall("putString",[StringLiteral("\"a is equal to b\"")])])))]))
                ]
            )
        )
        self.assertTrue(TestAST.checkASTGen(input,expect,321))
    def test_322(self):
        input = """
        func main() {
            for i := 0; i < 10; i += 1 {
                putInt(i);
            }
        }
        """
        expect = str(
            Program(
                [
                    FuncDecl("main",[],VoidType(),
                             Block(
                            [ForStep(
                                Assign(Id("i"), IntLiteral(0)),
                                BinaryOp("<",Id("i"),IntLiteral(10)),
                                Assign(Id("i"), BinaryOp("+", Id("i"), IntLiteral(1))),
                                Block([FuncCall("putInt",[Id("i")])]))
                            ]))
                ]
            )
        )
        self.assertTrue(TestAST.checkASTGen(input,expect,322))
    def test_323(self):
        input = """
        func main() {
            for i < 10 {
                putInt(i);
            }
        }
        """
        expect = str(
            Program(
                [   FuncDecl("main",[],VoidType(),
                    Block(
                    [
                    ForBasic(BinaryOp("<",Id("i"),IntLiteral(10)),Block([FuncCall("putInt",[Id("i")])]))
                    ]
                    )
                )]
            ))
        self.assertTrue(TestAST.checkASTGen(input,expect,323))
    def test_324(self):
        input = """
        func main() {
            for idx, val := range arr {
                putInt(idx);
                putInt(val);
            }
            for _, val := range arr {
                putInt(val);
            }
        }
            
        """
        expect = str(
            Program([
                FuncDecl("main",[],VoidType(),Block([
                    ForEach(Id("idx"),Id("val"),Id("arr"),Block([FuncCall("putInt",[Id("idx")]),FuncCall("putInt",[Id("val")])])),
                    ForEach(Id("_"), Id("val"), Id("arr"), Block([FuncCall("putInt",[Id("val")])]))
                ]))
            ])
        )
        self.assertTrue(TestAST.checkASTGen(input,expect,324))
    def test_325(self):
        input = """
        func main () {
            a := 5 + 5;
            b := 5 - 5;
            c := 5 * 5;
            d := 5 / 5;
            e := 5 % 5;
        }
        """
        expect = str(
            Program([
                FuncDecl("main",[],VoidType(),Block([
                    Assign(Id("a"),BinaryOp("+",IntLiteral(5),IntLiteral(5))),
                    Assign(Id("b"),BinaryOp("-",IntLiteral(5),IntLiteral(5))),
                    Assign(Id("c"),BinaryOp("*",IntLiteral(5),IntLiteral(5))),
                    Assign(Id("d"),BinaryOp("/",IntLiteral(5),IntLiteral(5))),
                    Assign(Id("e"),BinaryOp("%",IntLiteral(5),IntLiteral(5)))]))
            ])
        )
        self.assertTrue(TestAST.checkASTGen(input,expect,325))
    def test_326(self):
        input = """
        func main() {
            a := b[1][2][foo()];
            c := b[1][2][foo()] + 5;
            d := b[1][2][foo()] + 5 * 5;
            e := b[1][2][foo()] + 5 * 5 / 5;
            f := b[1][2][foo()] + 5 * 5 / 5 % 5;
        }
        """
        expect = str(
            Program([
                FuncDecl("main",[],VoidType(),Block([
                    Assign(Id("a"),ArrayCell(Id("b"),[IntLiteral(1),IntLiteral(2),FuncCall("foo",[])])),
                    Assign(Id("c"),BinaryOp("+",ArrayCell(Id("b"),[IntLiteral(1),IntLiteral(2),FuncCall("foo",[])]),IntLiteral(5))),
                    Assign(Id("d"),BinaryOp("+",ArrayCell(Id("b"),[IntLiteral(1),IntLiteral(2),FuncCall("foo",[])]),BinaryOp("*",IntLiteral(5),IntLiteral(5)))),
                    Assign(Id("e"),BinaryOp("+",ArrayCell(Id("b"),[IntLiteral(1),IntLiteral(2),FuncCall("foo",[])]),BinaryOp("/",BinaryOp("*",IntLiteral(5),IntLiteral(5)),IntLiteral(5)))),
                    Assign(Id("f"),BinaryOp("+",ArrayCell(Id("b"),[IntLiteral(1),IntLiteral(2),FuncCall("foo",[])]),BinaryOp("%",BinaryOp("/",BinaryOp("*",IntLiteral(5),IntLiteral(5)),IntLiteral(5)),IntLiteral(5))))
                ]))
            ])
        )
        self.assertTrue(TestAST.checkASTGen(input,expect,326))
    def test_327(self):
        input = """
        func main() {
            p.foo(dd, 5, 5.5, "Hello", true, a[1][2], b.c[3].d[4].e[5]);
        }
        """
        expect = str(
            Program([
                FuncDecl("main",[],VoidType(),Block([
                    MethCall(Id("p"),"foo",[Id("dd"),IntLiteral(5),FloatLiteral(5.5),StringLiteral("\"Hello\""),BooleanLiteral(True),ArrayCell(Id("a"),[IntLiteral(1),IntLiteral(2)]),ArrayCell(FieldAccess(ArrayCell(FieldAccess(ArrayCell(FieldAccess(Id("b"),"c"),[IntLiteral(3)]),"d"), [IntLiteral(4)]),"e"),[IntLiteral(5)])])
                ]))
            ])
        )
        # print(expect)
        self.assertTrue(TestAST.checkASTGen(input,expect,327))
    def test_328(self):
        input = """
        func main() {
            foo(foo(1,2), foo(4,5));
            goo(goo(goo(goo(goo(goo(1))))));
        }
        """
        expect = str(
            Program([
                FuncDecl("main",[],VoidType(),Block([
                    FuncCall("foo",[FuncCall("foo",[IntLiteral(1),IntLiteral(2)]),FuncCall("foo",[IntLiteral(4),IntLiteral(5)])]),
                    FuncCall("goo",[FuncCall("goo",[FuncCall("goo",[FuncCall("goo",[FuncCall("goo",[FuncCall("goo",[IntLiteral(1)])])])])])])
                ]))
            ])
        )
        self.assertTrue(TestAST.checkASTGen(input,expect,328))
    def test_329(self):
        input = """
        func main() {
            if (a>b){
                if (b>c){
                    if (c>d){
                        putString("a>b, b>c, c>d");
                    }
                }
            }
        }
        """
        expect = str(
            Program([
                FuncDecl("main",[],VoidType(),Block([
                    If(BinaryOp(">",Id("a"),Id("b")),Block([
                        If(BinaryOp(">",Id("b"),Id("c")),Block([
                            If(BinaryOp(">",Id("c"),Id("d")),Block([
                                FuncCall("putString",[StringLiteral("\"a>b, b>c, c>d\"")])
                            ]), None)
                        ]), None)
                    ]), None)
                ]))
            ])
                
        )
        self.assertTrue(TestAST.checkASTGen(input,expect,329))
    def test_330(self):
        input = """
        func main() {
            a := foo() + 5;
            b := foo() + 5 * 5;
            c := d[1].foo(bar(5, 5.5)) / bar[foo1(5, 5.5)]/5 + 10;
            d := -5 + 5;
        }
        """
        expect = str(
            Program([FuncDecl("main",[],VoidType(),Block([
                Assign(Id("a"),BinaryOp("+",FuncCall("foo",[]),IntLiteral(5))),
                Assign(Id("b"),BinaryOp("+",FuncCall("foo",[]),BinaryOp("*",IntLiteral(5),IntLiteral(5)))),
                Assign(Id("c"),
                       BinaryOp("+", 
                                BinaryOp("/",
                                         BinaryOp("/",
                                                  MethCall(ArrayCell(Id("d"),[IntLiteral(1)]),"foo",[FuncCall("bar",[IntLiteral(5),FloatLiteral(5.5)])]),
                                            ArrayCell(Id("bar"),[FuncCall("foo1",[IntLiteral(5),FloatLiteral(5.5)])])),
                                IntLiteral(5)),
                       IntLiteral(10))),
                Assign(Id("d"),BinaryOp("+",UnaryOp("-",IntLiteral(5)),IntLiteral(5)))
            ]))])
        )
        self.assertTrue(TestAST.checkASTGen(input,expect,330))
    def test_331(self):
        input = """
        func main(){
            for i:=0;i<10;i+=1{
                if (i % 2 == 0){
                    continue;
                }
            }    
        }
        """
        expect = str(
            Program([
                FuncDecl("main",[],VoidType(),Block([
                    ForStep(
                        Assign(Id("i"),IntLiteral(0)),
                        BinaryOp("<",Id("i"),IntLiteral(10)),
                        Assign(Id("i"),BinaryOp("+",Id("i"),IntLiteral(1))),
                        Block([If(
                                   BinaryOp("==",BinaryOp("%",Id("i"),IntLiteral(2)),IntLiteral(0)),
                                   Block([Continue()]),None)]))]))
            ])
        )
        self.assertTrue(TestAST.checkASTGen(input,expect,331))
    def test_332(self):
        input = """
        func main() {
            a := [1][2]int{1,2, Id, 3, Person{name: "John", age: 25}};
        }
        """
        expect = str(
            Program([
                FuncDecl("main",[],VoidType(),Block([
                    Assign(Id("a"),
                           ArrayLiteral([IntLiteral(1),IntLiteral(2)],IntType(),
                                        [IntLiteral(1),IntLiteral(2),Id("Id"),IntLiteral(3),StructLiteral("Person",[("name",StringLiteral("\"John\"")),("age",IntLiteral(25))])]))
                ]))
            ])
        )
        self.assertTrue(TestAST.checkASTGen(input,expect,332))
    def test_333(self):
        input = """
        func main(){
            b.a[1][2][3][4][5] := Person{name: "John", age: 25};
        }
        """
        expect = str(
            Program([
                FuncDecl("main",[],VoidType(),Block([
                    Assign(ArrayCell(FieldAccess(Id("b"), "a"), [IntLiteral(1), IntLiteral(2), IntLiteral(3), IntLiteral(4), IntLiteral(5)]),
                           StructLiteral("Person",[("name",StringLiteral("\"John\"")),("age",IntLiteral(25))])
                    )
                ]))
            ])
        )
        self.assertTrue(TestAST.checkASTGen(input,expect,333))
    def test_334(self):
        input = """
        func main(){
            a := b[1][2][3][4][5];
        }
        """
        expect = str(
            Program([
                FuncDecl("main",[],VoidType(),Block([
                    Assign(Id("a"),ArrayCell(Id("b"),[IntLiteral(1),IntLiteral(2),IntLiteral(3),IntLiteral(4),IntLiteral(5)]))
                ]))
            ])
        )
        self.assertTrue(TestAST.checkASTGen(input,expect,334))
    def test_335(self):
        input = """
        func main(){
        a[5][2][4][foo()].b.c.d.e := [2]Person{1,2,3,4};
        }
        """
        expect = str(
            Program([
                FuncDecl("main",[],VoidType(),Block([
                    Assign(FieldAccess(
                        FieldAccess(
                            FieldAccess(
                                FieldAccess(
                                    ArrayCell(Id("a"),[IntLiteral(5),IntLiteral(2),IntLiteral(4),FuncCall("foo",[])]),
                                    "b"),
                                "c"),
                            "d"),
                        "e"),
                        ArrayLiteral([IntLiteral(2)],Id("Person"),[IntLiteral(1),IntLiteral(2),IntLiteral(3),IntLiteral(4)])
                            )
            ])
                    )]))
        self.assertTrue(TestAST.checkASTGen(input,expect,335))
    def test_336(self):
        input = """
        func main() {
            a.b[1].c := b[2].d[3].e[4].f;
            k[1].l[2].m := n[3].o[4].p[5].q;
        }
        """
        expect = str(
            Program([
                FuncDecl("main",[],VoidType(),Block([
                    Assign(FieldAccess(ArrayCell(FieldAccess(Id("a"),"b"),[IntLiteral(1)]),"c"),FieldAccess(ArrayCell(FieldAccess(ArrayCell(FieldAccess(ArrayCell(Id("b"), [IntLiteral(2)]),"d"),[IntLiteral(3)]),"e"),[IntLiteral(4)]),"f")),
                    Assign(FieldAccess(ArrayCell(FieldAccess(ArrayCell(Id("k"),[IntLiteral(1)]), "l"),[IntLiteral(2)]),"m"),
                           FieldAccess(ArrayCell(FieldAccess(ArrayCell(FieldAccess(ArrayCell(Id("n"), [IntLiteral(3)]),"o"),[IntLiteral(4)]),"p"),[IntLiteral(5)]),"q"))
                ]))
            ])
        )
        self.assertTrue(TestAST.checkASTGen(input,expect,336))
    def test_337(self):
        input = """
        func main(){
            foo("abc", 5, 5.5, true, nil, false, Person{name: "John", age: 25});
        }
        """
        expect = str(
            Program([
                FuncDecl("main",[],VoidType(),Block([
                    FuncCall("foo",[StringLiteral("\"abc\""),IntLiteral(5),FloatLiteral(5.5),BooleanLiteral(True),NilLiteral(),BooleanLiteral(False),StructLiteral("Person",[("name",StringLiteral("\"John\"")),("age",IntLiteral(25))])])
                ]))
            ])
        )
        self.assertTrue(TestAST.checkASTGen(input,expect,337))
    def test_338(self):
        input = """
        func foo(a int, b float, c string, d Person, f[1][2]int) int{
            a := 5;
            c := "Hello";
            d := Person{name: "John", age: 25};
            return b+a;
        }
        """
        expect = str(
            Program([
                FuncDecl("foo",[ParamDecl("a", IntType()), ParamDecl("b", FloatType()), ParamDecl("c", StringType()), ParamDecl("d", Id("Person")), ParamDecl("f", ArrayType([IntLiteral(1),IntLiteral(2)],IntType()))],IntType(),Block([
                    Assign(Id("a"),IntLiteral(5)),
                    Assign(Id("c"),StringLiteral("\"Hello\"")),
                    Assign(Id("d"),StructLiteral("Person",[("name",StringLiteral("\"John\"")),("age",IntLiteral(25))])),
                    Return(BinaryOp("+",Id("b"),Id("a"))
                )]))
                ]))
        self.assertTrue(TestAST.checkASTGen(input,expect,338))
    def test_339(self):
        input = """
        func foo(a int, b float, c string, d Person, f[1][2]int) Person{
            a := 5;
            c := "Hello";
            d := Person{name: "John", age: 25};
            return d;
        }
        """
        expect = str(
            Program([
                FuncDecl("foo",[ParamDecl("a", IntType()), ParamDecl("b", FloatType()), ParamDecl("c", StringType()), ParamDecl("d", Id("Person")), ParamDecl("f", ArrayType([IntLiteral(1),IntLiteral(2)],IntType()))],Id("Person"),Block([
                    Assign(Id("a"),IntLiteral(5)),
                    Assign(Id("c"),StringLiteral("\"Hello\"")),
                    Assign(Id("d"),StructLiteral("Person",[("name",StringLiteral("\"John\"")),("age",IntLiteral(25))])),
                    Return(Id("d")) ])
            )
            ])
        )
        self.assertTrue(TestAST.checkASTGen(input,expect,339))
    def test_340(self):
        input = """
        func printSomething(){
            for i:=0;i<10;i+=1{
                putString("Hello");
                if (i == 9){
                    break;
                }
            }
        }
        """
        expect = str(
            Program([
                FuncDecl("printSomething",[],VoidType(),Block([
                    ForStep(
                        Assign(Id("i"),IntLiteral(0)),
                        BinaryOp("<",Id("i"),IntLiteral(10)),
                        Assign(Id("i"),BinaryOp("+",Id("i"),IntLiteral(1))),
                        Block([
                            FuncCall("putString",[StringLiteral("\"Hello\"")]),
                            If(
                                BinaryOp("==",Id("i"),IntLiteral(9)),
                                Block([Break()]),None)]))]))
            ])
        )
        self.assertTrue(TestAST.checkASTGen(input,expect,340))
    def test_341(self):
        input = """
        func main(){
            for var i = arr[2]; i < 10; i +=  b.foo() {
                putInt(i);
            }
        }
        """
        expect = str(
            Program([
                FuncDecl("main",[],VoidType(),Block([
                    ForStep(
                        VarDecl("i",None,ArrayCell(Id("arr"),[IntLiteral(2)])),
                        BinaryOp("<",Id("i"),IntLiteral(10)),
                        Assign(Id("i"),BinaryOp("+",Id("i"),MethCall(Id("b"),"foo",[]))),
                        Block([FuncCall("putInt",[Id("i")])]))])
                    )
            ])
        )
        self.assertTrue(TestAST.checkASTGen(input,expect,341))
    def test_342(self):
        input = """
        func compare(a int, b int) boolean{
            return a && b || a || b && !a;
        }
        """
        expect = str(
            Program([
                FuncDecl("compare",[ParamDecl("a", IntType()), ParamDecl("b", IntType())],BoolType(),Block([
                    Return(
                        BinaryOp("||",
                            BinaryOp("||",
                                     BinaryOp("&&",Id("a"),Id("b")),
                                     Id("a")),
                            BinaryOp("&&",Id("b"),UnaryOp("!",Id("a")))
                        )
                    )
                ]))
            ])
        )
        
        # print(expect)
        self.assertTrue(TestAST.checkASTGen(input,expect,342))
    def test_343(self):
        input = """
        func boolLLLL() boolean{
            return a || a && a || a || a && !a > b <= c;
        }
        """
        expect = str(
            Program([
                FuncDecl("boolLLLL", [], BoolType(), Block([
                    Return(
                        BinaryOp("||",
                            BinaryOp("||",
                                BinaryOp("||", Id("a"), BinaryOp("&&", Id("a"), Id("a"))),
                                Id("a")
                            ),
                            BinaryOp("&&", Id("a"),
                                BinaryOp("<=",
                                    BinaryOp(">", UnaryOp("!", Id("a")), Id("b")),
                                    Id("c")
                                )
                            )
                        )
                    )
                ]))
            ])
        )
        self.assertTrue(TestAST.checkASTGen(input,expect,343))
    def test_344(self):
        input = """
        func test() boolean{
            return (x + y) * z > 10 && a || b;
        }
        """
        expect = str(
            Program([
                FuncDecl("test", [], BoolType(), Block([
                    Return(
                        BinaryOp("||",
                            BinaryOp("&&",
                                BinaryOp(">",
                                    BinaryOp("*",
                                        BinaryOp("+", Id("x"), Id("y")),
                                        Id("z")
                                    ),
                                    IntLiteral(10)
                                ),
                                Id("a")
                            ),
                            Id("b")
                        )
                    )
                ]))
            ])
        )
        self.assertTrue(TestAST.checkASTGen(input, expect, 344))

    def test_345(self):
        input = """
        func compute() boolean{
            return (x - y) / z <= a && b || !c;
        }
        """
        expect = str(
            Program([
                FuncDecl("compute", [], BoolType(), Block([
                    Return(
                        BinaryOp("||",
                            BinaryOp("&&",
                                BinaryOp("<=",
                                    BinaryOp("/",
                                        BinaryOp("-", Id("x"), Id("y")),
                                        Id("z")
                                    ),
                                    Id("a")
                                ),
                                Id("b")
                            ),
                            UnaryOp("!", Id("c"))
                        )
                    )
                ]))
            ])
        )
        self.assertTrue(TestAST.checkASTGen(input, expect, 345))

    def test_346(self):
        input = """
        func logic() boolean{
            return x * y + z > a || b && c;
        }
        """
        expect = str(
            Program([
                FuncDecl("logic", [], BoolType(), Block([
                    Return(
                        BinaryOp("||",
                            BinaryOp(">",
                                BinaryOp("+",
                                    BinaryOp("*", Id("x"), Id("y")),
                                    Id("z")
                                ),
                                Id("a")
                            ),
                            BinaryOp("&&", Id("b"), Id("c"))
                        )
                    )
                ]))
            ])
        )
        self.assertTrue(TestAST.checkASTGen(input, expect, 346))
    
    def test_347(self):
        input = """
        func mathLogic() boolean{
            return a + b * c - d / e > f && g || h;
        }
        """
        expect = str(
            Program([
                FuncDecl("mathLogic", [], BoolType(), Block([
                    Return(
                        BinaryOp("||",
                            BinaryOp("&&",
                                BinaryOp(">",
                                    BinaryOp("-",
                                        BinaryOp("+", Id("a"), BinaryOp("*", Id("b"), Id("c"))),
                                        BinaryOp("/", Id("d"), Id("e"))
                                    ),
                                    Id("f")
                                ),
                                Id("g")
                            ),
                            Id("h")
                        )
                    )
                ]))
            ])
        )
        self.assertTrue(TestAST.checkASTGen(input, expect, 347))
    def test_348(self):
        input = """
        func main(){
            a += 727432 + 1324324;
            a -= 1234;
            a *= 1234;
            a /= 1234;
            a %= 1234;
        }
        """
        expect = str(
            Program([
                FuncDecl("main", [], VoidType(), Block([
                    Assign(Id("a"), BinaryOp("+", Id("a"), BinaryOp("+", IntLiteral(727432), IntLiteral(1324324)))),
                    Assign(Id("a"), BinaryOp("-", Id("a"), IntLiteral(1234))),
                    Assign(Id("a"), BinaryOp("*", Id("a"), IntLiteral(1234))),
                    Assign(Id("a"), BinaryOp("/", Id("a"), IntLiteral(1234))),
                    Assign(Id("a"), BinaryOp("%", Id("a"), IntLiteral(1234)))
                ]))
            ])
        )
        self.assertTrue(TestAST.checkASTGen(input, expect, 348))
    def test_349(self):
        input = """
        func sumAndCompare(x int, y int) boolean{
            return x + y > 100;
        }
        """
        expect = str(
            Program([
                FuncDecl("sumAndCompare", [ParamDecl("x", IntType()), ParamDecl("y", IntType())], BoolType(), Block([
                    Return(BinaryOp(">", BinaryOp("+", Id("x"), Id("y")), IntLiteral(100)))
                ]))
            ])
        )
        self.assertTrue(TestAST.checkASTGen(input, expect, 349))

    def test_350(self):
        input = """
        func complexFunc(a boolean, b int, c float) float{
            return (b * c) / 1.0;
        }
        """
        expect = str(
            Program([
                FuncDecl("complexFunc", [ParamDecl("a", BoolType()), ParamDecl("b", IntType()), ParamDecl("c", FloatType())], FloatType(), Block([
                    Return(BinaryOp("/", BinaryOp("*", Id("b"), Id("c")), FloatLiteral(1.0)))
                ]))
            ])
        )
        self.assertTrue(TestAST.checkASTGen(input, expect, 350))
    def test_351(self):
        input = """
        func binarySearch(arr [100]int, x int) int {
            low := 0;
            high := len(arr) - 1;
            for low <= high {
                mid := low + (high - low) / 2;
                if (arr[mid] == x) {
                    return mid;
                }
                if (arr[mid] < x) {
                    low := mid + 1;
                } else {
                    high := mid - 1;
                }
            }
            return -1;
        }
        """
        expect = "Program([FuncDecl(binarySearch,[ParDecl(arr,ArrayType(IntType,[IntLiteral(100)])),ParDecl(x,IntType)],IntType,Block([Assign(Id(low),IntLiteral(0)),Assign(Id(high),BinaryOp(FuncCall(len,[Id(arr)]),-,IntLiteral(1))),For(BinaryOp(Id(low),<=,Id(high)),Block([Assign(Id(mid),BinaryOp(Id(low),+,BinaryOp(BinaryOp(Id(high),-,Id(low)),/,IntLiteral(2)))),If(BinaryOp(ArrayCell(Id(arr),[Id(mid)]),==,Id(x)),Block([Return(Id(mid))])),If(BinaryOp(ArrayCell(Id(arr),[Id(mid)]),<,Id(x)),Block([Assign(Id(low),BinaryOp(Id(mid),+,IntLiteral(1)))]),Block([Assign(Id(high),BinaryOp(Id(mid),-,IntLiteral(1)))]))])),Return(UnaryOp(-,IntLiteral(1)))]))])"
        self.assertTrue(TestAST.checkASTGen(input, expect, 351))
    def test_352(self):
        input = """
        func bubbleSort(arr [100]int) {
            n := len(arr);
            for i := 0; i < n - 1; i += 1 {
                for j := 0; j < n - i - 1; j += 1 {
                    if (arr[j] > arr[j+1]) {
                        swap(arr, j, j+1);
                    }
                }
            }
        }
        """
        expect = "Program([FuncDecl(bubbleSort,[ParDecl(arr,ArrayType(IntType,[IntLiteral(100)]))],VoidType,Block([Assign(Id(n),FuncCall(len,[Id(arr)])),For(Assign(Id(i),IntLiteral(0)),BinaryOp(Id(i),<,BinaryOp(Id(n),-,IntLiteral(1))),Assign(Id(i),BinaryOp(Id(i),+,IntLiteral(1))),Block([For(Assign(Id(j),IntLiteral(0)),BinaryOp(Id(j),<,BinaryOp(BinaryOp(Id(n),-,Id(i)),-,IntLiteral(1))),Assign(Id(j),BinaryOp(Id(j),+,IntLiteral(1))),Block([If(BinaryOp(ArrayCell(Id(arr),[Id(j)]),>,ArrayCell(Id(arr),[BinaryOp(Id(j),+,IntLiteral(1))])),Block([FuncCall(swap,[Id(arr),Id(j),BinaryOp(Id(j),+,IntLiteral(1))])]))]))]))]))])"
        self.assertTrue(TestAST.checkASTGen(input, expect, 352))
    def test_353(self):
        input = """
        func insertionSort(arr [100]int) {
            n := len(arr);
            for i := 1; i < n; i += 1 {
                key := arr[i];
                j := i - 1;
                for j >= 0 && arr[j] > key {
                    arr[j+1] := arr[j];
                    j -= 1;
                }
                arr[j+1] := key;
            }
        }
        """
        expect = "Program([FuncDecl(insertionSort,[ParDecl(arr,ArrayType(IntType,[IntLiteral(100)]))],VoidType,Block([Assign(Id(n),FuncCall(len,[Id(arr)])),For(Assign(Id(i),IntLiteral(1)),BinaryOp(Id(i),<,Id(n)),Assign(Id(i),BinaryOp(Id(i),+,IntLiteral(1))),Block([Assign(Id(key),ArrayCell(Id(arr),[Id(i)])),Assign(Id(j),BinaryOp(Id(i),-,IntLiteral(1))),For(BinaryOp(BinaryOp(Id(j),>=,IntLiteral(0)),&&,BinaryOp(ArrayCell(Id(arr),[Id(j)]),>,Id(key))),Block([Assign(ArrayCell(Id(arr),[BinaryOp(Id(j),+,IntLiteral(1))]),ArrayCell(Id(arr),[Id(j)])),Assign(Id(j),BinaryOp(Id(j),-,IntLiteral(1)))])),Assign(ArrayCell(Id(arr),[BinaryOp(Id(j),+,IntLiteral(1))]),Id(key))]))]))])"
        self.assertTrue(TestAST.checkASTGen(input, expect, 353))
    def test_354(self):
        input = """
        func selectionSort(arr [100]int) {
            n := len(arr);
            for i := 0; i < n - 1; i += 1 {
                min_idx := i;
                for j := i + 1; j < n; j += 1 {
                    if (arr[j] < arr[min_idx]) {
                        min_idx := j;
                    }
                }
                swap(arr, i, min_idx);
            }
        }
        """
        expect = "Program([FuncDecl(selectionSort,[ParDecl(arr,ArrayType(IntType,[IntLiteral(100)]))],VoidType,Block([Assign(Id(n),FuncCall(len,[Id(arr)])),For(Assign(Id(i),IntLiteral(0)),BinaryOp(Id(i),<,BinaryOp(Id(n),-,IntLiteral(1))),Assign(Id(i),BinaryOp(Id(i),+,IntLiteral(1))),Block([Assign(Id(min_idx),Id(i)),For(Assign(Id(j),BinaryOp(Id(i),+,IntLiteral(1))),BinaryOp(Id(j),<,Id(n)),Assign(Id(j),BinaryOp(Id(j),+,IntLiteral(1))),Block([If(BinaryOp(ArrayCell(Id(arr),[Id(j)]),<,ArrayCell(Id(arr),[Id(min_idx)])),Block([Assign(Id(min_idx),Id(j))]))])),FuncCall(swap,[Id(arr),Id(i),Id(min_idx)])]))]))])"
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
    def test_360(self):
        input = """
        func main() {
            a := [5]int{1,2,3,4,5};
            b := [3][3]float{1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0};
            c := Person{name: "John", age: 25};
            d := [5]Person{Person{name: "John", age: 25}, Person{name: "John", age: 25}, Person{name: "John", age: 25}, Person{name: "John", age: 25}, Person{name: "John", age: 25}};
        }
        """
        expect = "Program([FuncDecl(main,[],VoidType,Block([Assign(Id(a),ArrayLiteral([IntLiteral(5)],IntType,[IntLiteral(1),IntLiteral(2),IntLiteral(3),IntLiteral(4),IntLiteral(5)])),Assign(Id(b),ArrayLiteral([IntLiteral(3),IntLiteral(3)],FloatType,[FloatLiteral(1.0),FloatLiteral(2.0),FloatLiteral(3.0),FloatLiteral(4.0),FloatLiteral(5.0),FloatLiteral(6.0),FloatLiteral(7.0),FloatLiteral(8.0),FloatLiteral(9.0)])),Assign(Id(c),StructLiteral(Person,[(name,StringLiteral(\"John\")),(age,IntLiteral(25))])),Assign(Id(d),ArrayLiteral([IntLiteral(5)],Id(Person),[StructLiteral(Person,[(name,StringLiteral(\"John\")),(age,IntLiteral(25))]),StructLiteral(Person,[(name,StringLiteral(\"John\")),(age,IntLiteral(25))]),StructLiteral(Person,[(name,StringLiteral(\"John\")),(age,IntLiteral(25))]),StructLiteral(Person,[(name,StringLiteral(\"John\")),(age,IntLiteral(25))]),StructLiteral(Person,[(name,StringLiteral(\"John\")),(age,IntLiteral(25))])]))]))])"
        self.assertTrue(TestAST.checkASTGen(input, expect, 360))
    def test_361(self):
        input = """
        func main() {
            a := 2;
            b := 5
            if (a > b) {
                putString("a is greater than b");
            } else {
                putString("a is not greater than b");
            }
        }
        """
        expect = """Program([FuncDecl(main,[],VoidType,Block([Assign(Id(a),IntLiteral(2)),Assign(Id(b),IntLiteral(5)),If(BinaryOp(Id(a),>,Id(b)),Block([FuncCall(putString,[StringLiteral("a is greater than b")])]),Block([FuncCall(putString,[StringLiteral("a is not greater than b")])]))]))])""" 
        self.assertTrue(TestAST.checkASTGen(input, expect, 361))
    def test_362(self):
        input = """
        func main() {
            a := 2;
            b := 5;
            if (a > b) {
                putString("a is greater than b");
            } else if (a < b) {
                putString("a is less than b");
            } else {
                putString("a is equal to b");
            }
        }
        """
        expect = """
        Program([FuncDecl(main,[],VoidType,Block([Assign(Id(a),IntLiteral(2)),Assign(Id(b),IntLiteral(5)),If(BinaryOp(Id(a),>,Id(b)),Block([FuncCall(putString,[StringLiteral(\"a is greater than b\")])]),If(BinaryOp(Id(a),<,Id(b)),Block([FuncCall(putString,[StringLiteral(\"a is less than b\")])]),Block([FuncCall(putString,[StringLiteral(\"a is equal to b\")])])))]))])
        """
    def test_363(self):
        input = """
        func foo() int{
            a := 5 + 5;
        }
        """
        expect =  """Program([FuncDecl(foo,[],IntType,Block([Assign(Id(a),BinaryOp(IntLiteral(5),+,IntLiteral(5)))]))])"""
        self.assertTrue(TestAST.checkASTGen(input, expect, 363))
    def test_364(self):
        input = """
        func foo() {
            
            return x+y;
        }
        """
        expect = """Program([FuncDecl(foo,[],VoidType,Block([Return(BinaryOp(Id(x),+,Id(y)))]))])""" 
        self.assertTrue(TestAST.checkASTGen(input, expect, 364))
    def test_365(self):
        input = """
        func complexFunc(a int, b float, c string, d boolean, e [5]int, f [3][3]float, g Person) {
            if (a > 10) {
                putInt(a);
            } else {
                putFloat(b);
            }
            if (d) {
                putString(c);
            }
            if (e[0] == 5) {
                putBool(d);
            }
            if (f[0][0] != 5.5) {
                putInt(e[0]);
            }
        }
        """
        expect =  """Program([FuncDecl(complexFunc,[ParDecl(a,IntType),ParDecl(b,FloatType),ParDecl(c,StringType),ParDecl(d,BoolType),ParDecl(e,ArrayType(IntType,[IntLiteral(5)])),ParDecl(f,ArrayType(FloatType,[IntLiteral(3),IntLiteral(3)])),ParDecl(g,Id(Person))],VoidType,Block([If(BinaryOp(Id(a),>,IntLiteral(10)),Block([FuncCall(putInt,[Id(a)])]),Block([FuncCall(putFloat,[Id(b)])])),If(Id(d),Block([FuncCall(putString,[Id(c)])])),If(BinaryOp(ArrayCell(Id(e),[IntLiteral(0)]),==,IntLiteral(5)),Block([FuncCall(putBool,[Id(d)])])),If(BinaryOp(ArrayCell(Id(f),[IntLiteral(0),IntLiteral(0)]),!=,FloatLiteral(5.5)),Block([FuncCall(putInt,[ArrayCell(Id(e),[IntLiteral(0)])])]))]))])"""
        self.assertTrue(TestAST.checkASTGen(input, expect, 365))
    def test_366(self):
        input = """
        func complexFunc(a int, b float, c string, d boolean, e [5]int, f [3][3]float, g Person) {
            for i := 0; i < 10; i += 1 {
                putInt(i);
            }
            for idx, value := range e {
                putInt(idx);
                putInt(value);
            }
        }
        """
        expect =  """Program([FuncDecl(complexFunc,[ParDecl(a,IntType),ParDecl(b,FloatType),ParDecl(c,StringType),ParDecl(d,BoolType),ParDecl(e,ArrayType(IntType,[IntLiteral(5)])),ParDecl(f,ArrayType(FloatType,[IntLiteral(3),IntLiteral(3)])),ParDecl(g,Id(Person))],VoidType,Block([For(Assign(Id(i),IntLiteral(0)),BinaryOp(Id(i),<,IntLiteral(10)),Assign(Id(i),BinaryOp(Id(i),+,IntLiteral(1))),Block([FuncCall(putInt,[Id(i)])])),ForEach(Id(idx),Id(value),Id(e),Block([FuncCall(putInt,[Id(idx)]),FuncCall(putInt,[Id(value)])]))]))])"""
        self.assertTrue(TestAST.checkASTGen(input, expect, 366))
    def test_367(self):
        input = """
        func main() {
                    a[5].bar();
            }
        """
        expect =  """Program([FuncDecl(main,[],VoidType,Block([MethodCall(ArrayCell(Id(a),[IntLiteral(5)]),bar,[])]))])"""
        self.assertTrue(TestAST.checkASTGen(input, expect, 367))
    def test_368(self):
        input = """
        var b int;
        func main() {
            b := [5]int{1,2,3,4,5};
            putInt(b[0]);
        }
        """
        expect =  """Program([VarDecl(b,IntType),FuncDecl(main,[],VoidType,Block([Assign(Id(b),ArrayLiteral([IntLiteral(5)],IntType,[IntLiteral(1),IntLiteral(2),IntLiteral(3),IntLiteral(4),IntLiteral(5)])),FuncCall(putInt,[ArrayCell(Id(b),[IntLiteral(0)])])]))])"""
        self.assertTrue(TestAST.checkASTGen(input, expect, 368))
    def test_369(self):
        input = """
        var x float;
        func main() {
            x := 5.5;
            putFloat(x);
        }
        """
        expect =  """Program([VarDecl(x,FloatType),FuncDecl(main,[],VoidType,Block([Assign(Id(x),FloatLiteral(5.5)),FuncCall(putFloat,[Id(x)])]))])"""
        self.assertTrue(TestAST.checkASTGen(input, expect, 369))

    def test_370(self):
        input = """
        func main() {
            str := "Hello" + " World";
            putString(str);
        }
        """
        expect =  """Program([FuncDecl(main,[],VoidType,Block([Assign(Id(str),BinaryOp(StringLiteral("Hello"),+,StringLiteral(" World"))),FuncCall(putString,[Id(str)])]))])"""
        self.assertTrue(TestAST.checkASTGen(input, expect, 370))
    def test_371(self):
        input = """
        func main() {
            a := 5;
            b := 5;
            c := 5;
            d := 5;
            e := 5;
        }
        """
        expect =  """Program([FuncDecl(main,[],VoidType,Block([Assign(Id(a),IntLiteral(5)),Assign(Id(b),IntLiteral(5)),Assign(Id(c),IntLiteral(5)),Assign(Id(d),IntLiteral(5)),Assign(Id(e),IntLiteral(5))]))])"""
        self.assertTrue(TestAST.checkASTGen(input, expect, 371))
    def test_372(self):
        input = """
        func main() {
            var flag bool = false;
            putBool(flag);
        }
        """
        expect =  """Program([FuncDecl(main,[],VoidType,Block([VarDecl(flag,Id(bool),BooleanLiteral(false)),FuncCall(putBool,[Id(flag)])]))])"""
        self.assertTrue(TestAST.checkASTGen(input, expect, 372))
    def test_373(self):
        input = """
        func main() {
            x := !true;
        }
        """
        expect =  """Program([FuncDecl(main,[],VoidType,Block([Assign(Id(x),UnaryOp(!,BooleanLiteral(true)))]))])"""
        self.assertTrue(TestAST.checkASTGen(input, expect, 373))
    def test_374(self):
        input = """
        func main() {
            x := 5;
            y := 10;
            z := x + y;
        }
        """
        expect =  """Program([FuncDecl(main,[],VoidType,Block([Assign(Id(x),IntLiteral(5)),Assign(Id(y),IntLiteral(10)),Assign(Id(z),BinaryOp(Id(x),+,Id(y)))]))])"""
        self.assertTrue(TestAST.checkASTGen(input, expect, 374))
    def test_375(self):
        input ="""
        func fibo(n int) int {
            if (n == 0) {
                return 0;
            }
            if (n == 1) {
                return 1;
            }
            return fibo(n-1) + fibo(n-2);
        }
        """
        expect =  """Program([FuncDecl(fibo,[ParDecl(n,IntType)],IntType,Block([If(BinaryOp(Id(n),==,IntLiteral(0)),Block([Return(IntLiteral(0))])),If(BinaryOp(Id(n),==,IntLiteral(1)),Block([Return(IntLiteral(1))])),Return(BinaryOp(FuncCall(fibo,[BinaryOp(Id(n),-,IntLiteral(1))]),+,FuncCall(fibo,[BinaryOp(Id(n),-,IntLiteral(2))])))]))])"""
        self.assertTrue(TestAST.checkASTGen(input, expect, 375))
    def test_376(self):
        input = """
        func lcs(X string, Y string, m int, n int) int {
            if (m == 0 || n == 0) {
                return 0;
            }
            if (X[m-1] == Y[n-1]) {
                return 1 + lcs(X, Y, m-1, n-1);
            } else {
                return max(lcs(X, Y, m, n-1), lcs(X, Y, m-1, n));
            }
        }
        """
        expect =  """Program([FuncDecl(lcs,[ParDecl(X,StringType),ParDecl(Y,StringType),ParDecl(m,IntType),ParDecl(n,IntType)],IntType,Block([If(BinaryOp(BinaryOp(Id(m),==,IntLiteral(0)),||,BinaryOp(Id(n),==,IntLiteral(0))),Block([Return(IntLiteral(0))])),If(BinaryOp(ArrayCell(Id(X),[BinaryOp(Id(m),-,IntLiteral(1))]),==,ArrayCell(Id(Y),[BinaryOp(Id(n),-,IntLiteral(1))])),Block([Return(BinaryOp(IntLiteral(1),+,FuncCall(lcs,[Id(X),Id(Y),BinaryOp(Id(m),-,IntLiteral(1)),BinaryOp(Id(n),-,IntLiteral(1))])))]),Block([Return(FuncCall(max,[FuncCall(lcs,[Id(X),Id(Y),Id(m),BinaryOp(Id(n),-,IntLiteral(1))]),FuncCall(lcs,[Id(X),Id(Y),BinaryOp(Id(m),-,IntLiteral(1)),Id(n)])]))]))]))])"""
        self.assertTrue(TestAST.checkASTGen(input, expect, 376))
    def test_377(self):
        input = """
        func main(){
            a := "Hello";
            b := "World";
            c := a + b;
            putString(c);
            z := "ccndshbc \\n \\t"
        }
        """
        expect = str(
            Program(
                [
                    FuncDecl("main", [],VoidType(),  Block([
                        Assign(Id("a"), StringLiteral("\"Hello\"")),
                        Assign(Id("b"), StringLiteral("\"World\"")),
                        Assign(Id("c"), BinaryOp("+", Id("a"), Id("b"))),
                        FuncCall("putString", [Id("c")]),
                        Assign(Id("z"), StringLiteral("\"ccndshbc \\n \\t\""))
                    ]))
                ]
            )
        )
        self.assertTrue(TestAST.checkASTGen(input, expect, 377))
    def test_378(self):
        input = """
        func main(){
            a:= 1.e-2;
            b:= 1.e+2;
            c:= 1.e2;
        }
        """
        expect =  """Program([FuncDecl(main,[],VoidType,Block([Assign(Id(a),FloatLiteral(0.01)),Assign(Id(b),FloatLiteral(100.0)),Assign(Id(c),FloatLiteral(100.0))]))])"""
        self.assertTrue(TestAST.checkASTGen(input, expect, 378))
    def test_379(self):
        input = """
        func main(){
            for true{
                putString("Hello");
            }
        }
        """
        expect =  """Program([FuncDecl(main,[],VoidType,Block([For(BooleanLiteral(true),Block([FuncCall(putString,[StringLiteral("Hello")])]))]))])"""
        self.assertTrue(TestAST.checkASTGen(input, expect, 379))
    def test_380(self):
        input = """
        func main(){
            foo();
            bar();
            something();
            hello();
        }
        """
        expect =  """Program([FuncDecl(main,[],VoidType,Block([FuncCall(foo,[]),FuncCall(bar,[]),FuncCall(something,[]),FuncCall(hello,[])]))])"""
        self.assertTrue(TestAST.checkASTGen(input, expect, 380))
    def test_381(self):
        input = """
        var xyz[5] int;
        func main(){
            xyz[0] := 5;
            putInt(xyz[0]);
        }
        """
        expect =  """Program([VarDecl(xyz,ArrayType(IntType,[IntLiteral(5)])),FuncDecl(main,[],VoidType,Block([Assign(ArrayCell(Id(xyz),[IntLiteral(0)]),IntLiteral(5)),FuncCall(putInt,[ArrayCell(Id(xyz),[IntLiteral(0)])])]))])"""
        self.assertTrue(TestAST.checkASTGen(input, expect, 381))
    def test_382(self):
        input = """
        var fl float;
        func main(){
            fl := 5.5;
            putFloat(fl);
        }
        """
        expect =  """Program([VarDecl(fl,FloatType),FuncDecl(main,[],VoidType,Block([Assign(Id(fl),FloatLiteral(5.5)),FuncCall(putFloat,[Id(fl)])]))])"""
        self.assertTrue(TestAST.checkASTGen(input, expect, 382))
    def test_383(self):
        input = """
        func main (){
            for i:=0;i<10;i+=1{
                if (abc){
                    break;
                } else if(def){
                    if (ghi){
                        continue;
                    }
                }
            }
        }
        """
        expect =  """Program([FuncDecl(main,[],VoidType,Block([For(Assign(Id(i),IntLiteral(0)),BinaryOp(Id(i),<,IntLiteral(10)),Assign(Id(i),BinaryOp(Id(i),+,IntLiteral(1))),Block([If(Id(abc),Block([Break()]),If(Id(def),Block([If(Id(ghi),Block([Continue()]))])))]))]))])"""
        self.assertTrue(TestAST.checkASTGen(input, expect, 383))
    def test_384(self):
        input = """
        func main(){
            for abc*def{
                putString("Hello");
            }
        }
        """
        expect =  """Program([FuncDecl(main,[],VoidType,Block([For(BinaryOp(Id(abc),*,Id(def)),Block([FuncCall(putString,[StringLiteral("Hello")])]))]))])"""
        self.assertTrue(TestAST.checkASTGen(input, expect, 384))
    def test_385(self):
        input = """
        func main(){
            for idx, value := range arr{
                if (idx * value > 10){
                    break;
                } else if(idx * value < 10){
                    continue;
                }
            }
        }
        """
        expect =  """Program([FuncDecl(main,[],VoidType,Block([ForEach(Id(idx),Id(value),Id(arr),Block([If(BinaryOp(BinaryOp(Id(idx),*,Id(value)),>,IntLiteral(10)),Block([Break()]),If(BinaryOp(BinaryOp(Id(idx),*,Id(value)),<,IntLiteral(10)),Block([Continue()])))]))]))])"""
        self.assertTrue(TestAST.checkASTGen(input, expect, 385))
    def test_386(self):
        input = """
        func main(){
            for i:=0;i<10;i+=1{
                for j:=0;j<10;j+=1{
                    putInt(i+j);
                }
            }
        }
        """
        expect =  """Program([FuncDecl(main,[],VoidType,Block([For(Assign(Id(i),IntLiteral(0)),BinaryOp(Id(i),<,IntLiteral(10)),Assign(Id(i),BinaryOp(Id(i),+,IntLiteral(1))),Block([For(Assign(Id(j),IntLiteral(0)),BinaryOp(Id(j),<,IntLiteral(10)),Assign(Id(j),BinaryOp(Id(j),+,IntLiteral(1))),Block([FuncCall(putInt,[BinaryOp(Id(i),+,Id(j))])]))]))]))])"""
        self.assertTrue(TestAST.checkASTGen(input, expect, 386))
    def test_387(self):
        input = """
        // full call stmt
        func main(){
            foo(1,2,3);
            bar(1.0,2.0,3.0);
            hello("Hello","World");
            something(true,false);
            nillfunc(nil)
        }
        """
        expect =  """Program([FuncDecl(main,[],VoidType,Block([FuncCall(foo,[IntLiteral(1),IntLiteral(2),IntLiteral(3)]),FuncCall(bar,[FloatLiteral(1.0),FloatLiteral(2.0),FloatLiteral(3.0)]),FuncCall(hello,[StringLiteral("Hello"),StringLiteral("World")]),FuncCall(something,[BooleanLiteral(true),BooleanLiteral(false)]),FuncCall(nillfunc,[Nil])]))])"""
        self.assertTrue(TestAST.checkASTGen(input, expect, 387))
    def test_388(self):
        input = """
        /* comment*/
        func main(){
            // call method
            a.foo();
            b.bar();
            c.hello();
            d.something();
            e.nillfunc();
        }
        """
        expect = """Program([FuncDecl(main,[],VoidType,Block([MethodCall(Id(a),foo,[]),MethodCall(Id(b),bar,[]),MethodCall(Id(c),hello,[]),MethodCall(Id(d),something,[]),MethodCall(Id(e),nillfunc,[])]))])"""
        self.assertTrue(TestAST.checkASTGen(input, expect, 388))
    def test_389(self):
        input = """
        func main(){
            for true {
                for false{
                    for i < 10{
                        putInt(i);
                    }
                }
            }
        }
        """
        expect =  """Program([FuncDecl(main,[],VoidType,Block([For(BooleanLiteral(true),Block([For(BooleanLiteral(false),Block([For(BinaryOp(Id(i),<,IntLiteral(10)),Block([FuncCall(putInt,[Id(i)])]))]))]))]))])"""
        self.assertTrue(TestAST.checkASTGen(input, expect, 389))
    def test_390(self):
        input = """
        func main(){
            for i:=0;i<10;i+=1{
                for j:=0;j<10;j+=1{
                    for k:=0;k<10;k+=1{
                        putInt(i+j+k);
                    }
                }
            }
        }
        """
        expect =  """Program([FuncDecl(main,[],VoidType,Block([For(Assign(Id(i),IntLiteral(0)),BinaryOp(Id(i),<,IntLiteral(10)),Assign(Id(i),BinaryOp(Id(i),+,IntLiteral(1))),Block([For(Assign(Id(j),IntLiteral(0)),BinaryOp(Id(j),<,IntLiteral(10)),Assign(Id(j),BinaryOp(Id(j),+,IntLiteral(1))),Block([For(Assign(Id(k),IntLiteral(0)),BinaryOp(Id(k),<,IntLiteral(10)),Assign(Id(k),BinaryOp(Id(k),+,IntLiteral(1))),Block([FuncCall(putInt,[BinaryOp(BinaryOp(Id(i),+,Id(j)),+,Id(k))])]))]))]))]))])"""
        self.assertTrue(TestAST.checkASTGen(input, expect, 390))
    def test_391(self):
        input = """
        func main(){
            for var i = 0; i < 10; i += 1{
                for var j = 0; j < 10; j += 1{
                    for var k = 0; k < 10; k += 1{
                        putInt(i+j+k);
                    }
                }
            }
        }
        """
        expect =  """Program([FuncDecl(main,[],VoidType,Block([For(VarDecl(i,IntLiteral(0)),BinaryOp(Id(i),<,IntLiteral(10)),Assign(Id(i),BinaryOp(Id(i),+,IntLiteral(1))),Block([For(VarDecl(j,IntLiteral(0)),BinaryOp(Id(j),<,IntLiteral(10)),Assign(Id(j),BinaryOp(Id(j),+,IntLiteral(1))),Block([For(VarDecl(k,IntLiteral(0)),BinaryOp(Id(k),<,IntLiteral(10)),Assign(Id(k),BinaryOp(Id(k),+,IntLiteral(1))),Block([FuncCall(putInt,[BinaryOp(BinaryOp(Id(i),+,Id(j)),+,Id(k))])]))]))]))]))])"""
        self.assertTrue(TestAST.checkASTGen(input, expect, 391))
    def test_392(self):
        input = """
        func main(){
        for i:=0;i<10;i+=1{
            for j:=0;j<10;j+=1{
                for true{
                    putInt(i+j);
                }
            }
        }
        }
        """
        expect = """Program([FuncDecl(main,[],VoidType,Block([For(Assign(Id(i),IntLiteral(0)),BinaryOp(Id(i),<,IntLiteral(10)),Assign(Id(i),BinaryOp(Id(i),+,IntLiteral(1))),Block([For(Assign(Id(j),IntLiteral(0)),BinaryOp(Id(j),<,IntLiteral(10)),Assign(Id(j),BinaryOp(Id(j),+,IntLiteral(1))),Block([For(BooleanLiteral(true),Block([FuncCall(putInt,[BinaryOp(Id(i),+,Id(j))])]))]))]))]))])"""
        self.assertTrue(TestAST.checkASTGen(input, expect, 392))
    def test_393(self):
        input = """
        func ifStmt(){
            if (true){
                putString("Hello");
                if (foo()){
                    putString("World");
                }
            }
        }
        """
        expect = """Program([FuncDecl(ifStmt,[],VoidType,Block([If(BooleanLiteral(true),Block([FuncCall(putString,[StringLiteral("Hello")]),If(FuncCall(foo,[]),Block([FuncCall(putString,[StringLiteral("World")])]))]))]))])"""
        self.assertTrue(TestAST.checkASTGen(input, expect, 393))
    def test_394(self):
        input = """
        func main(){
            foo("Hello", 1.e432, 1.0e-2, 1.0e+2, 1.0e2);
        }
        """
        expect =  """Program([FuncDecl(main,[],VoidType,Block([FuncCall(foo,[StringLiteral("Hello"),FloatLiteral(inf),FloatLiteral(0.01),FloatLiteral(100.0),FloatLiteral(100.0)])]))])"""
        self.assertTrue(TestAST.checkASTGen(input, expect, 394))
    def test_395(self):
        input = """
        const a = 5;
        const z = a + 5;
        const y = z + 5;
        const x = y + 5;
        """
        expect =  """Program([ConstDecl(a,IntLiteral(5)),ConstDecl(z,BinaryOp(Id(a),+,IntLiteral(5))),ConstDecl(y,BinaryOp(Id(z),+,IntLiteral(5))),ConstDecl(x,BinaryOp(Id(y),+,IntLiteral(5)))])"""
        self.assertTrue(TestAST.checkASTGen(input, expect, 395))
    def test_396(self):
        input = """
        func main (){
            a := !true;
            b := !false;
            c := !a;
            d := !b;
        }
        """
        expect =  """Program([FuncDecl(main,[],VoidType,Block([Assign(Id(a),UnaryOp(!,BooleanLiteral(true))),Assign(Id(b),UnaryOp(!,BooleanLiteral(false))),Assign(Id(c),UnaryOp(!,Id(a))),Assign(Id(d),UnaryOp(!,Id(b)))]))])"""
        self.assertTrue(TestAST.checkASTGen(input, expect, 396))
    def test_397(self):
        input = """
        func smartFunc(){
            if (true){
                putString("Hello");
            } else if (false){
                putString("World");
            } else {
                putString("Goodbye");
            }
        }
        """
        expect = """Program([FuncDecl(smartFunc,[],VoidType,Block([If(BooleanLiteral(true),Block([FuncCall(putString,[StringLiteral("Hello")])]),If(BooleanLiteral(false),Block([FuncCall(putString,[StringLiteral("World")])]),Block([FuncCall(putString,[StringLiteral("Goodbye")])])))]))])"""
        self.assertTrue(TestAST.checkASTGen(input, expect, 397))
    def test_398(self):
        input = """
        func (c Circle) area() float {
            return c.radius * c.radius * 3.14;
        }
        """
        expect =  """Program([MethodDecl(c,Id(Circle),FuncDecl(area,[],FloatType,Block([Return(BinaryOp(BinaryOp(FieldAccess(Id(c),radius),*,FieldAccess(Id(c),radius)),*,FloatLiteral(3.14)))])))])"""
        self.assertTrue(TestAST.checkASTGen(input, expect, 398))
    def test_399(self):
        input = """
        func lastTestcase(){
            if (true){
                if (false){
                    if (true){
                        if (false){
                            putString("Hello");
                        }
                    }
                }
            }
        }
        """
        expect =  """Program([FuncDecl(lastTestcase,[],VoidType,Block([If(BooleanLiteral(true),Block([If(BooleanLiteral(false),Block([If(BooleanLiteral(true),Block([If(BooleanLiteral(false),Block([FuncCall(putString,[StringLiteral("Hello")])]))]))]))]))]))])"""
        self.assertTrue(TestAST.checkASTGen(input, expect, 399))
        