import unittest
from TestUtils import TestChecker
from AST import *


# format test
""" 
    test_4xx
    400-410: Redeclared built-in functions
    411-430: Redeclared
    431-450: Undeclared
    451-470: TypeMismatch
    471-499: Mixed
"""
class CheckSuite(unittest.TestCase):
    # def test_400(self):
    #     input = """
    #     func getInt() int {
    #         return 10;
    #     }
    #     """
    #     expect = "Redeclared Function: getInt\n"
    #     self.assertTrue(TestChecker.test(input,expect,400))
        
    # def test_401(self):
    #     input = """
    #     func putInt(x float) {
    #         x := 1
    #     }
    #     """
    #     expect = "Redeclared Function: putInt\n"
    #     self.assertTrue(TestChecker.test(input,expect,401))
    
    # def test_402(self):
    #     input = """
    #     func putIntLn(x, y int) {
    #         x := y + 1; 
    #     }
    #     """
    #     expect = "Redeclared Function: putIntLn\n"
    #     self.assertTrue(TestChecker.test(input,expect,402))
        
    # def test_403(self):
    #     input = """
    #     func getFloat() int {
    #         return 1;
    #     }
    #     """
    #     expect = "Redeclared Function: getFloat\n"
    #     self.assertTrue(TestChecker.test(input,expect,403))
        
    # def test_404(self):
    #     input = """
    #     func putFloat(a float, b float) {
    #         putLn();
    #     }
    #     """
    #     expect = "Redeclared Function: putFloat\n"
    #     self.assertTrue(TestChecker.test(input,expect,404))
        
    # def test_405(self):
    #     input = """
    #     const putFloatLn = 1;
    #     func putFloatLn() string {
    #         return "hello";
    #     }
    #     """
    #     expect = "Redeclared Constant: putFloatLn\n"
    #     self.assertTrue(TestChecker.test(input,expect,405))
        
    # def test_406(self):
    #     input = """
    #     var getBool = 1;
    #     func getBool() string {
    #         return "true";
    #     }
    #     """
    #     expect = "Redeclared Variable: getBool\n"
    #     self.assertTrue(TestChecker.test(input,expect,406))
        
    # def test_407(self):
    #     input = """
    #     type putBool struct {
    #         a int;
    #     }

    #     func putBool(b boolean, extra string) {
    #         var putBool = 1;
    #         return;
    #     }
        
        
    #     """
    #     expect = "Redeclared Type: putBool\n"
    #     self.assertTrue(TestChecker.test(input,expect,407))
        
    # def test_408(self):
    #     input = """
    #     type putIntLn interface {
    #         Add(a int) int;
    #     }
    #     func putBoolLn() int {
    #         return 0;
    #     }
    #     """
    #     expect = "Redeclared Type: putIntLn\n"
    #     self.assertTrue(TestChecker.test(input,expect,408))
        
    # def test_409(self):
    #     input = """
    #     func getString() {
    #         return;
    #     }
    #     """
    #     expect = "Redeclared Function: getString\n"
    #     self.assertTrue(TestChecker.test(input,expect,409))
        
    # def test_410(self):
    #     input = """
    #     func putLn(message string) {
    #         return;
    #     }
    #     """
    #     expect = "Redeclared Function: putLn\n"
    #     self.assertTrue(TestChecker.test(input,expect,410))
        
    # def test_411(self):
    #     input = """
    #     var x int = 5;
    #     var x float;
    #     """
    #     expect = "Redeclared Variable: x\n"
    #     self.assertTrue(TestChecker.test(input,expect,411))
        
    # def test_412(self):
    #     input = """
    #     var x = getInt() + 5;
    #     const x = 10;
    #     """
    #     expect = "Redeclared Constant: x\n"
    #     self.assertTrue(TestChecker.test(input,expect,412))
        
    # def test_413(self):
    #     input = """
    #     func foo(a, b int, a string) {
    #         return;
    #     }
    #     """
    #     expect = "Redeclared Parameter: a\n"
    #     self.assertTrue(TestChecker.test(input,expect,413))
        
    # def test_414(self):
    #     input = """
    #     type Person struct {
    #         name string;
    #         age int;
    #     }
    #     type Person struct {
    #         name int;
    #     }
    #     """
    #     expect = "Redeclared Type: Person\n"
    #     self.assertTrue(TestChecker.test(input,expect,414))
        
    # def test_415(self):
    #     input = """
    #     func foo(a int, b int) int {
    #         return a + b;
    #     }
    #     func foo(x float, y float) float {
    #         return x + y;
    #     }
    #     """
    #     expect = "Redeclared Function: foo\n"
    #     self.assertTrue(TestChecker.test(input,expect,415))
        
    # def test_416(self):
    #     input = """
        
        
    #     func (c Car) crash() {
    #         return;
    #     }
        
    #     func (c Car) crash() int {
    #         return 0;
    #     }

    #     type Car struct {
    #         brand string;
    #     }
    #     """
    #     expect = "Redeclared Method: crash\n"
    #     self.assertTrue(TestChecker.test(input,expect,416))
        
    # def test_417(self):
    #     input = """
    #     type People interface {
    #         getHeight();
    #         getHeight(height int);
    #     }
    #     """
    #     expect = "Redeclared Prototype: getHeight\n"
    #     self.assertTrue(TestChecker.test(input,expect,417))
        
    # def test_418(self):
    #     input = """
    #     type Person struct {
    #         height int;
    #         name string;
    #         height float
    #     }
    #     """
    #     expect = "Redeclared Field: height\n"
    #     self.assertTrue(TestChecker.test(input,expect,418))
        
    # def test_419(self):
    #     input = """
    #     var x int = 1;

    #     func foo() {
    #         var x int;
    #         const x = 10;
    #     }
    #     """
    #     expect = "Redeclared Constant: x\n" 
    #     self.assertTrue(TestChecker.test(input,expect,419))
        
    # def test_420(self):
    #     input = """
    #     func main() {
    #         var x int;
    #         x := 10;
    #         var x [x][2]int;
    #     }
    #     """
    #     expect = "Redeclared Variable: x\n" 
    #     self.assertTrue(TestChecker.test(input,expect,420))
        
    # def test_421(self):
    #     input = """
    #     func foo(x int) int {
    #         return x + x * 1
    #     }
        
    #     func main() {
    #         var x int;
    #         x := foo(x);
    #     }
        
    #     func foo(x float) {
    #         return;
    #     }
    #     """
    #     expect = "Redeclared Function: foo\n"
    #     self.assertTrue(TestChecker.test(input,expect,421))
        
    # def test_422(self):
    #     input = """
    #     type Pair struct {
    #         first int;
    #         second int;
    #     }
    #     func main(){
    #         var x Pair = Pair{first: 4, second: 5};
    #         x := Pair{first: 1, second: 2};
    #         var y = x.swap()
    #     }
    #     func (p Pair) swap() Pair {
    #         return Pair{first: p.second, second: p.first};
    #     }
        
    #     func swap(a, b int) {
    #         var tmp = a
    #         a := b
    #         b := tmp
    #     }
        
    #     func (p Pair) swap() Pair {
    #         return 2;
    #     }
    #     """
    #     expect = "Redeclared Method: swap\n"
    #     self.assertTrue(TestChecker.test(input,expect,422))
        
    # def test_423(self):
    #     input = """
    #     type Pair struct {
    #         first int;
    #         second int;
    #     }
    #     const x = 10
    #     func (p Pair) getInt() int {
    #         return p.first + x;
    #     }
    #     func (p Pair) foo() int {
    #         return p.second;
    #     }

    #     func (p Pair) foo(a int) int {
    #         return a * 2;
    #     }
        
    #     """
    #     expect = "Redeclared Method: foo\n"
    #     self.assertTrue(TestChecker.test(input,expect,423))
        
    # def test_424(self):
    #     input = """
    #     const n = 5;

    #     func test() {
    #         s := Subject{name: "Math", scores: [5]float{1.0}, scores: [5]int{1, 2}};
    #     }
    #     func (s Subject) putFloat() float {
    #         return s.scores[0];
    #     }
        
    #     type Subject struct {
    #         name string;
    #         scores [n]float;
    #         scores [n]int;
    #     }
    #     """
    #     expect = "Redeclared Field: scores\n" 
    #     self.assertTrue(TestChecker.test(input,expect,424))
    # def test_425(self):
    #     input = """
    #     type Person struct {
    #         name string;
    #         age int;
    #     }
    #     func (p Person) getName() string {
    #         return p.name;
    #     }
    #     func (s Student) getName() string {
    #         return s.name;
    #     }
    #     type Student struct {
    #         name string;
    #         age int;
    #     }
    #     func (t Teacher) getName() string {
    #         return t.person.getName();
    #     }
    #     func (p Person) getAge() string {
    #         return p.name;
    #     }

    #     type Teacher struct {
    #         person Person;
    #         students [5]Student;
    #     }
    #     func (p Person) getAge() string {
    #         return p.name;
    #     }
    #     """
    #     expect = "Redeclared Method: getAge\n" 
    #     self.assertTrue(TestChecker.test(input,expect,425))
        
    # def test_426(self):
    #     input = """
    #     func test(x, y int, z float) {
    #         var x int;
    #         t := 1;
    #         const t = 2;
    #     }
    #     """
    #     expect = "Redeclared Constant: t\n"
    #     self.assertTrue(TestChecker.test(input,expect,426))
        
    # def test_427(self):
    #     input = """
    #     func (a Person) name() {
    #         return
    #     } 
    #     type Person struct {
    #         name string
    #     }

    #     """
    #     expect = "Redeclared Field: name\n" 
    #     self.assertTrue(TestChecker.test(input,expect,427))
        
    # def test_428(self):
    #     input = """
    #     func foo(x,y,z int, t float) int {
    #         var t float = 1.0;
    #         k := 1;
    #         return k;
    #     }
    #     func main(){
    #         t := foo(1,2,3,4.0);
    #         putInt(t);
    #     }
    #     var k = 1;
    #     var k = 2;
    #     """
    #     expect = "Redeclared Variable: k\n" 
    #     self.assertTrue(TestChecker.test(input,expect,428))
        
    # def test_429(self):
    #     input = """
    #     type A struct {
    #         x int;
    #     }
    #     func main(){
    #         var a A;
    #         putInt(a.test());
    #     }
    #     func (a A) test() int {
    #         return a.x;
    #     }
        
    #     var test = 1;

    #     func test() {
    #         var x int;
    #     }    

    #     const test = 21.0
        
    #     func foo(){
    #         putInt(test);
    #     }
        
        
    #     """
    #     expect = "Redeclared Function: test\n" 
    #     self.assertTrue(TestChecker.test(input,expect,429))
        
    # def test_430(self):
    #     input = """
    #     func (a A) test() int {
    #         return a.test1();
    #     }
    #     func (a A) test1() int {
    #         return a.x;
    #     }
    #     type A struct {
    #         x int;
    #     }
    #     func main(){
    #         var a A;
    #         putInt(a.test());
    #     }
    #     """
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input,expect,430))
    # def test_431(self):
    #     input = """
    #     func main(){
    #         x += 1;
    #     }
    #     """
    #     expect = "Undeclared Identifier: x\n"
    #     self.assertTrue(TestChecker.test(input,expect,431))
    # def test_432(self):
    #     input = """
    #     var b boolean;
    #     var c int;
    #     var a int = c * d;
    #     """
    #     expect = "Undeclared Identifier: d\n"
    #     self.assertTrue(TestChecker.test(input,expect,432))
    # def test_433(self):
    #     input = """
    #     var a = 2 + 5 * 3;
    #     func foo(){
    #         k := a + b;
    #         var e = h + 1;
    #     }
    #     """
    #     expect = "Undeclared Identifier: b\n"
    #     self.assertTrue(TestChecker.test(input,expect,433))
    # def test_434(self):
    #     input = """
    #     var a[1]int = [1]int{1};
    #     var b [5]float;
    #     func foo(){
    #         b := [5]int{1,2,3,4,5};
    #         var c = a[0];
    #         putInt(c);
    #         var d = e + 1;
    #     }
    #     """
    #     expect = "Undeclared Identifier: e\n"
    #     self.assertTrue(TestChecker.test(input,expect,434))
    # def test_435(self):
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
    #     self.assertTrue(TestChecker.test(input,expect,435))
    # def test_436(self):
    #     input = """
    #     var a[1]int = [1]int{1};
    #     var b [5]float;
    #     func foo(){
    #         a[0] := 2;
    #         putInt(a[0]);
    #         b[0] := c;
    #     }
    #     var c int = 2;
    #     """
    #     expect = "Undeclared Identifier: c\n"
    #     self.assertTrue(TestChecker.test(input,expect,436))
    # def test_437(self):
    #     input = """
    #     func foo(a, b int, c float) {
    #         var a int;
    #         var b float;
    #         var c float;
    #         putInt(a);
    #         putFloat(c);
    #         c := d + 1;
    #     }
    #     const d = 1;
    #     """
    #     expect = "Undeclared Identifier: d\n"
    #     self.assertTrue(TestChecker.test(input,expect,437))
    # def test_438(self):
    #     input = """
    #     func foo() {
    #         foo1();
    #         foo2();
    #     }
    #     func foo1() {
    #         return;
    #     }
    #     func foo2() {
    #         return;
    #     }
    #     func main() {
    #         foo();
    #         putInt(1);
    #         foo3(1,2);
    #     }
    #     """
    #     expect = "Undeclared Function: foo3\n"
    #     self.assertTrue(TestChecker.test(input,expect,438))
    # def test_439(self):
    #     input = """
    #     func add(a int, b int) int {
    #         return a + b;
    #     }
    #     func foo(){
    #         var c int;
    #         c := add(1,2);
    #         var d int;
    #         d := add(c,3);
    #     } 
    #     func mul(a int, b int) int {
    #         return a * b;
    #     }
        
    #     func modulo(a int, b int) int {
    #         foo();
    #         return add1(1,2) % mul(3,4);
    #     }
    #     """
    #     expect = "Undeclared Function: add1\n"
    #     self.assertTrue(TestChecker.test(input,expect,439))
    # def test_440(self):
    #     input = """
    #     func (p Person) getName() string {
    #         return p.name;
    #     }
    #     type Person struct {
    #         name string;
    #         age int;
    #     }
    #     var p Person;
    #     func main(){
    #         p.print();
    #     }
    #     """
    #     expect = "Undeclared Method: print\n"
    #     self.assertTrue(TestChecker.test(input,expect,440))
    # def test_441(self):
    #     input = """
    #     func (a A) test() int {
    #         return a.test1();
    #     }
    #     type A struct {
    #         x int;
    #     }
    #     func (a A) test1() int {
    #         return a.test2();
    #     }
    #     """
    #     expect = "Undeclared Method: test2\n"
    #     self.assertTrue(TestChecker.test(input,expect,441))
    # def test_442(self):
    #     input = """
    #     type A interface{
    #         test1() int;
    #     }
    #     type B struct {
    #         x int;
    #     }
    #     func (b B) test1() int {
    #         return b.x;
    #     }
    #     func (b B) test2() int {
    #         return b.x;
    #     }
    #     func main(){
    #         var a A;
    #         a := B{x: 1};
    #         putInt(a.test2());
    #     }
    #     """
    #     expect = "Undeclared Method: test2\n"
    #     self.assertTrue(TestChecker.test(input,expect,442))
    # def test_443(self):
    #     input = """
    #     type A struct {
    #         x int;
    #         other B;
    #     }
    #     func (a A) test() int {
    #         return a.x;
    #     }
    #     func (a A) test1() int {
    #         return a.other.test();
    #     }
    #     type B struct {
    #         x int;
    #     }
    #     func (b B) test1() int {
    #         return b.x;
    #     }
    #     """
    #     expect = "Undeclared Method: test\n"
    #     self.assertTrue(TestChecker.test(input,expect,443))
    # def test_444(self):
    #     input = """
    #     type A struct {
    #         x int;
    #         other B;
    #     }
    #     func (a A) test() int {
    #         return a.x;
    #     }
    #     type B struct {
    #         x int;
    #         other A;
    #     }
    #     func (b B) test() int {
    #         return b.x + b.other.test1();
    #     }
    #     """
    #     expect = "Undeclared Method: test1\n"
    #     self.assertTrue(TestChecker.test(input,expect,444))
    # def test_445(self):
    #     input = """
    #     type A interface {
    #         test1() int;
    #         foo(a int) int;
    #         foo1(b int) int;
    #     }
    #     func foo() B {
    #         return B{x: 1};
    #     }
    #     type B struct {
    #         x int;
    #     }
    #     func (b B) test1() int {
    #         return b.x;
    #     }
    #     func (b B) foo(a int) int {
    #         return b.x + a;
    #     }
    #     func (b B) foo1(a int) int {
    #         return a;
    #     }
    #     func main(){
    #         var a A;
    #         a := foo();
    #         putInt(a.foo1(2));
    #         putInt(a.foo2(3));
    #     }
    #     """
    #     expect = "Undeclared Method: foo2\n"
    #     self.assertTrue(TestChecker.test(input,expect,445))
    # def test_446(self):
    #     input = """
    #     type Truck struct{
    #         brand string;
    #         year int;
    #     }
    #     type Vehicle interface {
    #         drive() int;
    #     }
    #     func main(){
    #         var t Vehicle;
    #         t := Truck{brand: "Ford", year: 2020};
    #         putInt(t.drive());
    #     }
    #     func (v Truck) drive() int {
    #         return v.speed;
    #     }
    #     """
    #     expect = "Undeclared Field: speed\n"
    #     self.assertTrue(TestChecker.test(input,expect,446))
    # def test_447(self):
    #     input = """
    #     type C struct {
    #         a int;
    #         b float;
    #     }
    #     func (c C) test() int {
    #         return c.a + c.b + c.d;
    #     }
    #     type D interface {
    #         test() int;
    #     }
    #     """
    #     expect = "Undeclared Field: d\n"
    #     self.assertTrue(TestChecker.test(input,expect,447))
    # def test_448(self):
    #     input = """
    #     func main(){
    #         var a A;
    #         a := A{x: 1, z:2};
    #         putInt(a.test());
    #     }
    #     func (a A) test() int {
    #         return a.test1();
    #     }
    #     type A struct {
    #         x int;
    #     }
    #     """
    #     expect = "Undeclared Field: z\n"
    #     self.assertTrue(TestChecker.test(input,expect,448))
    # def test_449(self):
    #     input = """
    #     func foo(a,b,c int) A{
    #         return A{a:a, b:b, c:c, d:d}
    #     }
    #     type A struct{
    #         a int;
    #         b int;
    #         c int;
    #     }
    #     """
    #     expect = "Undeclared Field: d\n"
    #     self.assertTrue(TestChecker.test(input, expect, 449))
    # def test_450(self):
    #     input = Program(
    #         [StructType("B",
    #                     [("x",IntType())],[MethodDecl("a",Id("B"),FuncDecl("test",[],IntType(),Block([Return(FieldAccess(Id("a"),"z"))])))]),])
    #     expect = "Undeclared Field: z\n"
    #     self.assertTrue(TestChecker.test(input, expect, 450))
    # def test_451(self):
    #     input = """
    #     const a = 1;
    #     var b float = 1.0;
    #     var c int = a;
    #     var d = c > b;
    #     """
    #     expect = "Type Mismatch: BinaryOp(Id(c),>,Id(b))\n"
    #     self.assertTrue(TestChecker.test(input,expect,451))
    # def test_452(self):
    #     input = """
    #     var a string = "hello";
    #     var b string = "world";
    #     var c = a > b;
    #     var d = a + b;
    #     var e = c % d;
    #     """
    #     expect = "Type Mismatch: BinaryOp(Id(c),%,Id(d))\n"
    #     self.assertTrue(TestChecker.test(input,expect,452))
    # def test_453(self):
    #     input = """
    #     var a int = 1;
    #     var b float = 2.0;
    #     var c = a + b;
    #     var d = a > c;
    #     """
    #     expect = "Type Mismatch: BinaryOp(Id(a),>,Id(c))\n"
    #     self.assertTrue(TestChecker.test(input,expect,453))
    # def test_454(self):
    #     input = """
    #     var a float = 1.0;
    #     var b float = 2.0;
    #     var c = a % b;
    #     """
    #     expect = "Type Mismatch: BinaryOp(Id(a),%,Id(b))\n"
    #     self.assertTrue(TestChecker.test(input,expect,454))
    # def test_455(self):
    #     input = """
    #     var a = true || false;
    #     var b = a && true;
    #     var c = a && b;
    #     var d = !a;
    #     var e = a + c;
    #     """
    #     expect = "Type Mismatch: BinaryOp(Id(a),+,Id(c))\n"
    #     self.assertTrue(TestChecker.test(input,expect,455))
    # def test_456(self):
    #     input = """
    #     var arr [5]int;
    #     func foo(){
    #         arr := [5]int{1,2.0,3};
    #     }
    #     """
    #     expect = "Type Mismatch: ArrayLiteral([IntLiteral(5)],IntType,[IntLiteral(1),FloatLiteral(2.0),IntLiteral(3)])\n"
    #     self.assertTrue(TestChecker.test(input,expect,456))
    # def test_457(self):
    #     input = """
    #     var a int = 1.0;
    #     var b float = 2.0;
    #     var c int;
    #     """
    #     expect = "Type Mismatch: VarDecl(a,IntType,FloatLiteral(1.0))\n"
    #     self.assertTrue(TestChecker.test(input,expect,457))
    # def test_458(self):
    #     input = """
    #     func foo(x, y int) {
    #         a := x + y;
    #         b := a > y;
    #         c := a || b;
    #     }
    #     """
    #     expect = "Type Mismatch: BinaryOp(Id(a),||,Id(b))\n"
    #     self.assertTrue(TestChecker.test(input,expect,458))
    # def test_459(self):
    #     input = """
    #     const a = 2;
    #     const b = 3;
    #     const c = a + b;
    #     var d [a][c]int;
    #     func foo(){
    #         d := [2][5]int{{1,2,3},{4,5,6}};
    #     }
    #     func main(){
    #         foo();
    #         putInt(d[0][0]);
    #         putInt(d[1][1]);
    #         putFloat(d[1][0]);
    #     }
    #     """
    #     expect = "Type Mismatch: FuncCall(putFloat,[ArrayCell(Id(d),[IntLiteral(1),IntLiteral(0)])])\n"
    #     self.assertTrue(TestChecker.test(input,expect,459))
    # def test_460(self):
    #     input = """
    #     type A struct {
    #         x int;
    #         y float;
    #         other B;
    #     }
    #     func (a A) test(x int, y float) {
    #         var b B;
    #         b := A{x: 1, y: 2.0};
    #         putInt(b.x);
    #     }
    #     func main(){
    #         var b B;
    #         b := A{x: 1, y: 2.0};
    #     }
    #     type B interface {
    #         test(x int, y float);
    #     }
    #     """
    #     expect = "Type Mismatch: FieldAccess(Id(b),x)\n"
    #     self.assertTrue(TestChecker.test(input,expect,460))
    # def test_461(self):
    #     input = """
    #     type A struct {
    #         x int; 
    #         y float;
    #     }
    #     func (a A) foo(){
    #         putInt(a.x);
    #     }
    #     func (a A) bar() int{
    #         return a.x + 1;
    #     }
    #     func main(){
    #         var a A;
    #         a := A{x: 1, y: 2.0};
    #         a.foo();
    #         a.bar();
    #     }
    #     """
    #     expect = "Type Mismatch: MethodCall(Id(a),bar,[])\n"
    #     self.assertTrue(TestChecker.test(input,expect,461))
    # def test_462(self):
    #     input = """
    #     func complexFunc(a int, b float, c Person) {
    #         var z Person;
    #         var v = z.test();

    #         const y = 1.2
    #         putFloat(y);
    #     }
    #     type Person struct {
    #         name string;
    #         age int;
    #     }
    #     func (p Person) test() int {
    #         return p.age;
    #     }
    #     func main(){
    #         complexFunc(1, 2.0, Person{name: "John", age: 30});
    #         var p Person;
    #         p := Person{name: "Alice", age: 25};
    #         p.test();
    #     }
    #     """
    #     expect = "Type Mismatch: MethodCall(Id(p),test,[])\n"
    #     self.assertTrue(TestChecker.test(input,expect,462))
    # def test_463(self):
    #     input = """
    #     func foo(a int) int{
    #         return 0x1FA24;
    #     }
    #     func bar(b int) int{
    #         return 0b1111;
    #     }
    #     func main(){
    #         putInt(foo(bar(foo(bar(foo(bar(bar(2.0))))))));
    #     }
    #     """
    #     expect = "Type Mismatch: FuncCall(bar,[FloatLiteral(2.0)])\n"
    #     self.assertTrue(TestChecker.test(input,expect,463))
    # def test_464(self):
    #     input = """
    #     func foo(a int, b int) int{
    #         return;
    #     }
    #     """
    #     expect = "Type Mismatch: Return()\n"
    #     self.assertTrue(TestChecker.test(input,expect,464))
    # def test_465(self):
    #     input = """
    #     func main(){
    #         var a int;
            
    #         for a < "hi there" {
    #             putInt(a);
    #             a += 1;
    #         }
    #     }
    #     """
    #     expect = "Type Mismatch: BinaryOp(Id(a),<,StringLiteral(\"hi there\"))\n"
    #     self.assertTrue(TestChecker.test(input,expect,465))
    # def test_466(self):
    #     input = """
    #     func main(){
    #         var a int;
    #         var b float;
    #         for a <= b {
    #             putInt(a);
    #             a += 1;
    #         }
    #     }
    #     """
    #     expect = "Type Mismatch: BinaryOp(Id(a),<=,Id(b))\n"
    #     self.assertTrue(TestChecker.test(input,expect,466))
    # def test_467(self):
    #     input = """
    #     func testLoop(k int){
    #         for i := 0; i < k; i+=1 {
    #             putInt(i);
    #             for var j = 1.0; j < k; j += 1 {
    #                 putInt(j);
    #             }
    #         }
    #     }
    #     """
    #     expect = "Type Mismatch: BinaryOp(Id(j),<,Id(k))\n"
    #     self.assertTrue(TestChecker.test(input,expect,467))
    # def test_468(self):
    #     input = """
    #     var n int = 2;
    #     var i = 2
    #     func foo(a int, b int, c [n]int) [n]int {
    #         var x1 = 1 + 2 * 3
    #         var x2 int = 5 * 6;
    #         var x3 [x2]int;
    #         x3 := [30]int{1,2,3,4};
    #         var x4 [30]int = x3;
    #         var x5 [n]int;
    #         var x6 [2]int = x5
    #         const x7 = [x2]int{1,2,3,4};
    #         var x8 [i]int = foo(1, 2, x2)
    #         return c;
    #     }
    #     """
    #     expect = "Type Mismatch: FuncCall(foo,[IntLiteral(1),IntLiteral(2),Id(x2)])\n"
    #     self.assertTrue(TestChecker.test(input,expect,468))
    # def test_469(self):
    #     input = """
    #     const a = logicEval(true, false);
    #     const b = logicEval(true, true);
    #     const c = 2;
    #     func foo(){
    #         if (a) {
    #             putString("True");
    #             if (a && b){
    #                 putString("True");
    #             } else {
    #                 putString("False");
    #             }
    #         } else if (c){
    #             putString("False");
    #         }  else {
    #             putString("True");
    #         }  
    #     }
    #     func logicEval(a boolean, b boolean) boolean {
    #         return a || b && a || b && !a || !b;
    #     }
    #     """
    #     expect = "Type Mismatch: If(Id(c),Block([FuncCall(putString,[StringLiteral(\"False\")])]),Block([FuncCall(putString,[StringLiteral(\"True\")])]))\n"
    #     self.assertTrue(TestChecker.test(input,expect,469))
    # def test_470(self):
    #     input = """
    #     const a = 2
    #     const b = 3
    #     const c = a + b
        
    #     func foo(a int, b int) {
    #         if (a > b) {
    #             putInt(a)
    #         } else if (b < c){
    #             putInt(b)
    #         } else {
    #             putInt(c)
    #         }
    #     }
    #     func main(){
    #         var c boolean = true;
    #         foo(1, 2);
    #         putFloat(c * a - b);
    #     }
    #     """
    #     expect = "Type Mismatch: BinaryOp(Id(c),*,Id(a))\n"
    #     self.assertTrue(TestChecker.test(input,expect,470))
    # def test_471(self):
    #     input = """
    #     var n int = 2;
    #     var i = 2
    #     func foo(a int, b int, c [n]int) int {
    #         var x1 = 1 + 2 * 3
    #         return a;
    #     }

    #     func foo1(a, b int) Person {
    #         a := foo(a, b, [2]int{1, 2})

    #         return a;
    #     }
    #     """
    #     expect = "Undeclared Identifier: Person\n"
    #     self.assertTrue(TestChecker.test(input,expect,471))
    # def test_472(self):
    #     input = """
    #     func foo() {
    #         a := 1;
    #         b := 2;
    #         c := a + b;
    #         putInt(c);
    #     }
    #     func main() {
    #         var a = foo();
    #     }
    #     """
    #     expect = "Type Mismatch: VarDecl(a,FuncCall(foo,[]))\n"
    #     self.assertTrue(TestChecker.test(input,expect,472))
    # def test_473(self):
    #     input = """
    #     func foo(){
    #         a := foo();
    #         var b int = 1;
    #         putInt(b);
    #     }
    #     """
    #     expect = "Type Mismatch: Assign(Id(a),FuncCall(foo,[]))\n"
    #     self.assertTrue(TestChecker.test(input, expect, 473))
    # def test_474(self):
    #     input = """
    #     func (a A) c() int {
    #         return a.b();
    #     }
    #     var a int;
    #     type A struct {
    #         c int;
    #     }
    #     func (a A) b() int {
    #         return a.c;
    #     }
    #     func (a A) d() int {
    #         return a.b();
    #     }
        
    #     """
    #     expect = "Redeclared Field: c\n"
    #     self.assertTrue(TestChecker.test(input, expect, 474))
    # def test_475(self):
    #     input = """
    #     const n = 4;
    #     var i string;
    #     func main(){
    #         for i := 0; i < n * 2; i += 1{
    #             if (i % 2 == 0){
    #                 putInt(i);
    #             }
    #         }
            
    #         i := "hi there";
    #         i += 1;
    #     }
    #     """
    #     expect = "Type Mismatch: BinaryOp(Id(i),+,IntLiteral(1))\n"
    #     self.assertTrue(TestChecker.test(input, expect, 475))
    # def test_476(self):
    #     input = """
    #     type A struct {
    #         x int;
    #         y float;
    #     }
    #     func (a A) test() int {
    #         return a.x;
    #     }
    #     func main(){
    #         const a = A{x: 1, y:2.0, y:1.0};
    #         putInt(a.test());
    #     }
    #     """
    #     expect = "Redeclared Field: y\n"
    #     self.assertTrue(TestChecker.test(input, expect, 476))
    # def test_477(self):
    #     input = """
    #     func main(){
    #         var index string = "hi there";
    #         var value int;
    #         for index, value := range [4]int{1,2,3} {
    #             putInt(value);
    #         }
    #     }
    #     """
    #     expect = "Type Mismatch: ForEach(Id(index),Id(value),ArrayLiteral([IntLiteral(4)],IntType,[IntLiteral(1),IntLiteral(2),IntLiteral(3)]),Block([FuncCall(putInt,[Id(value)])]))\n"
    #     self.assertTrue(TestChecker.test(input, expect, 477))
    # def test_478(self):
    #     input = """
    #     func main(){
    #         var index int = 0;
    #         var value int;
    #         for _, value := range [5]int{1,2,3,4,5} {
    #             putInt(value);
    #             putInt(index);
    #             index += value;
    #         }
    #         for index, value := range [5]int{1,2,3,4,5} {
    #             putInt(value);
    #             putString(index);
    #         }
    #     }
    #     """
    #     expect = "Type Mismatch: FuncCall(putString,[Id(index)])\n"
    #     self.assertTrue(TestChecker.test(input, expect, 478))
    # def test_479(self):
    #     input = """
    #     const a = 1;
    #     const b = 2;
    #     var c = a + b;
    #     func main(){
    #         foo();
    #         arr := [c]int{1,2,3};
    #         putInt(arr[3]);
    #         putString(arr[1]);
    #     }
    #     func foo(){
    #         c +=1;
    #     }
    #     """
    #     expect = "Type Mismatch: FuncCall(putString,[ArrayCell(Id(arr),[IntLiteral(1)])])\n"
    #     self.assertTrue(TestChecker.test(input, expect, 479))
    # def test_480(self):
    #     input = """
    #     var a int;
    #     var b int;
    #     var c = 10;
    #     func main(){
    #         for a, b := range c{
    #             putInt(a);
    #         }
    #     }
    #     """
    #     expect = "Type Mismatch: ForEach(Id(a),Id(b),Id(c),Block([FuncCall(putInt,[Id(a)])]))\n"
    #     self.assertTrue(TestChecker.test(input, expect, 480))
    # def test_481(self):
    #     input = """
    #     var a float = 3.0;
    #     func main(){
    #         a += 2;
    #         arr := [a]int{1,2,3};
    #     }
    #     """
    #     expect = "Type Mismatch: ArrayLiteral([Id(a)],IntType,[IntLiteral(1),IntLiteral(2),IntLiteral(3)])\n"
    #     self.assertTrue(TestChecker.test(input, expect, 481))
    # def test_482(self):
    #     input = """
    #     var a int = 1;
    #     var b int = 2;
    #     var c int = 3;
    #     func main(){
    #         a += 0b01;
    #         b += 0x01; 
    #         c += 0o02;
    #         arr := [a][b][c]int{{{1,2,3,4,5},{2,3,4,5,6},{4,5,6,7,8}},{{1,2,3,4,5},{2,3,4,5,6},{4,5,6,7,8}}};
    #         putFloat(arr[0][0][0]);
    #     }
    #     """
    #     expect = "Type Mismatch: FuncCall(putFloat,[ArrayCell(Id(arr),[IntLiteral(0),IntLiteral(0),IntLiteral(0)])])\n"
    #     self.assertTrue(TestChecker.test(input, expect, 482))
    # def test_483(self):
    #     input = """
    #     type A struct {
    #         x int;
    #         y int;
    #         z B;
    #     }
        
    #     type B interface {
    #         test() int;
    #     }
    #     func (a A) foo() {
    #         var z B;
    #         a.z := A{x: 1, y: 2, z: z};
    #         putString(a.z.test());
    #     }
    #     func (a A) test() int {
    #         return a.x + a.y;
    #     }
    #     """
    #     expect = "Type Mismatch: FuncCall(putString,[MethodCall(FieldAccess(Id(a),z),test,[])])\n"
    #     self.assertTrue(TestChecker.test(input, expect, 483))
    # def test_484(self):
    #     input = """
    #     type A interface{
    #         test() int;
    #     }
    #     type B struct {
    #         x int;
    #         y int;
    #         z A;
    #     }
    #     func (b B) test() int {
    #         var c B;
    #         var d A;
    #         b.z := B{x: 1, y: 2, z: d};
    #         return b.x + b.z.x;
    #     }
    #     """
    #     expect = "Type Mismatch: FieldAccess(FieldAccess(Id(b),z),x)\n"
    #     self.assertTrue(TestChecker.test(input, expect, 484))
    # def test_485(self):
    #     input = """
    #     func foo(){
    #         a := 1;
    #         b := 2;
    #         c := a + b;
    #         putInt(c);
    #     }
    #     func main(){
    #         d := foo();
    #     }
    #     """
    #     expect = "Type Mismatch: Assign(Id(d),FuncCall(foo,[]))\n"
    #     self.assertTrue(TestChecker.test(input, expect, 485))
    # def test_486(self):
    #     input = """
    #     func main(){
    #         var i int = 2;
    #         var j int = 3;
    #         var z = i + j;
    #         var arr[i][j][z]int;
            
    #         arr := [2][3][5]int{{{1}, {2,7}, {2}, {4, 5, 6, 7}}, {{1},{2,3},{4,5,6}}};
    #         putInt(arr[0][0][0]);
    #     }
    #     """
    #     expect = "Type Mismatch: ArrayLiteral([IntLiteral(2),IntLiteral(3),IntLiteral(5)],IntType,[[[IntLiteral(1)],[IntLiteral(2),IntLiteral(7)],[IntLiteral(2)],[IntLiteral(4),IntLiteral(5),IntLiteral(6),IntLiteral(7)]],[[IntLiteral(1)],[IntLiteral(2),IntLiteral(3)],[IntLiteral(4),IntLiteral(5),IntLiteral(6)]]])\n"
    #     self.assertTrue(TestChecker.test(input, expect, 486))
    # def test_487(self):
    #     input = """
    #     type A struct{
    #         x int;
    #         y float;
    #     }
    #     func (a A) foo(a int) float{
    #         return a.y;
    #     }
    #     """
    #     expect = "Type Mismatch: FieldAccess(Id(a),y)\n"
    #     self.assertTrue(TestChecker.test(input, expect, 487))
    # def test_488(self):
    #     input = """
    #     type Person struct {
    #         name string;
    #         age int;
    #     }
    #     func main(){
    #         var p Person;
    #         p := Person{age: 25, name: "Tom"};
    #         putFloat(p.age);
    #     }
    #     """
    #     expect = "Type Mismatch: FuncCall(putFloat,[FieldAccess(Id(p),age)])\n"
    #     self.assertTrue(TestChecker.test(input, expect, 488))
    def test_489(self):
        input = """
        func main(){

            for a := 0; a < 5; b := 1 {
                var b = a * 2
                putFloat(b);
            }
        }
        """
        expect = "Type Mismatch: FuncCall(putFloat,[Id(b)])\n"
        self.assertTrue(TestChecker.test(input, expect, 489))
    def test_490(self):
        input = """
        func foo(a, b, c int, c float, d string) {
            var a int;
            var b float;
            putInt(a);
            putFloat(b);
        }
        """
        expect = "Redeclared Parameter: c\n"
        self.assertTrue(TestChecker.test(input, expect, 490))
    def test_491(self):
        input = """
        func foo(){
            a := A{x: 1, y: 2};
        }
        type A struct {
            x int;
            y int;
            x int;
        }
        """
        expect = "Redeclared Field: x\n"
        self.assertTrue(TestChecker.test(input, expect, 491))
    def test_492(self):
        input = """
        func foo(a int, b float, c string, e B, d A){
            putInt(a);
            putFloat(b);
        }
        type B interface {
            test() int;
        }
        type A struct {
            x int;
            y float;
        }
        func (a A) test() int {
            return a.x;
        }
        func main(){
            foo(1, 2.0, "hello", A{x:1, y:2.0}, A{x:1, y:2.0});
        }
        """
        expect = "Type Mismatch: FuncCall(foo,[IntLiteral(1),FloatLiteral(2.0),StringLiteral(\"hello\"),StructLiteral(A,[(x,IntLiteral(1)),(y,FloatLiteral(2.0))]),StructLiteral(A,[(x,IntLiteral(1)),(y,FloatLiteral(2.0))])])\n"
        self.assertTrue(TestChecker.test(input, expect, 492))
    def test_493(self):
        input = """
        func foo(a int, b float, c string){
            putInt(a);
        }
        func main(){
            foo(foo(7, 24.0, "hi there"), 24.0, "hi there");
        }
        """
        expect = "Type Mismatch: FuncCall(foo,[FuncCall(foo,[IntLiteral(7),FloatLiteral(24.0),StringLiteral(\"hi there\")]),FloatLiteral(24.0),StringLiteral(\"hi there\")])\n"
        self.assertTrue(TestChecker.test(input, expect, 493))
    def test_494(self):
        input = """
        func foo(){
            a := 1;
            putInt(a);
        }
        func main(){
            var b int;
            b := foo() + 2
        }
        """
        expect = "Type Mismatch: BinaryOp(FuncCall(foo,[]),+,IntLiteral(2))\n"
        self.assertTrue(TestChecker.test(input, expect, 494))
    def test_495(self):
        input = """
        type A struct {
            x int;
            y float;
        }
        func (a A) test() int {
            return a.z;
        }
        """
        expect = "Undeclared Field: z\n"
        self.assertTrue(TestChecker.test(input, expect, 495))
    def test_496(self):
        input = """
        func foo(a int, b float, c string){
            var a float;
            var b int;
            var c string;
            putInt(a);
        }
        """
        expect = "Type Mismatch: FuncCall(putInt,[Id(a)])\n"
        self.assertTrue(TestChecker.test(input, expect, 496))
    def test_497(self):
        input = """
        func foo(a A, b B) {
            var a int;
            var b float;
            var c string;
            putInt(a);
        }
        type A struct {
            x int;
            y float;
        }
        type B interface {
            test() int;
        }
        func (a A) test() int {
            return a.x;
        }
        func main(){
            var c B;
            foo(A{x:1, y:2.0, z:1}, c);
        }
        """
        expect = "Undeclared Field: z\n"
        self.assertTrue(TestChecker.test(input, expect, 497))
    def test_498(self):
        input = """
        func main(){
            var a[2][3]int;
            a[0][0] := 1.0;
        }
        """
        expect = "Type Mismatch: Assign(ArrayCell(Id(a),[IntLiteral(0),IntLiteral(0)]),FloatLiteral(1.0))\n"
        self.assertTrue(TestChecker.test(input, expect, 498))
    def test_499(self):
        input = """
        func foo(a int, b float, c string){
            var a int;
            var b float;
            var c string;
            putInt(a);
        }
        func main(){
            foo(1, 2.0, "hello");
        }
        func foo() int{
            return 1;
        }
        """
        expect = "Redeclared Function: foo\n"
        self.assertTrue(TestChecker.test(input, expect, 499))
    def test_500(self):
        input = """
        func foo(){
            var getInt int;
            getInt := 1;
            putInt(getInt);
        }
        func main(){
            var a int;
            a := foo();
        }
        """
        expect = "Type Mismatch: Assign(Id(a),FuncCall(foo,[]))\n"
        self.assertTrue(TestChecker.test(input, expect, 500))
#     def test_501(self):
#         input = """
#         func foo(a int){
#             foo(1);
#             var foo int;
#             foo(2);
#         }
#         """
#         expect = "Undeclared Function: foo\n"
#         self.assertTrue(TestChecker.test(input, expect, 501))
#     def test_502(self):
#         input = """
#         type A struct {
#             getInt int;
#             getFloat float;
#         }
#         """
#         expect = ""
#         self.assertTrue(TestChecker.test(input, expect, 502))
#     def test_503(self):
#         input = """
#         func foo(){
#             var a int;
#             var b float;
#             var c string;
#             putInt(a);
#         }
#         func main(){
#             var x = foo()
#         }
#         """
#         expect = "Type Mismatch: VarDecl(x,FuncCall(foo,[]))\n"
#         self.assertTrue(TestChecker.test(input, expect, 503))
#     def test_504(self):
#         input = """
#         type Address struct {
#             street string
#             city string
#             country string
#         }
#         func (p Person) location() Address {
#             var a int
#             return Address{street: "123 Main St", city: "New York", country: "USA"}
#         }
#         type Person struct {
#             name string
#         }
#         var huy Person;
#         var add = huy.location().location;
#         """
#         expect = "Undeclared Field: location\n"
#         self.assertTrue(TestChecker.test(input,expect,504))
#     def test_505(self):
#         input = """
#         type Person struct {
#             name string
#         }
#         type Person interface {
#             age()
#         }
#         """
#         expect = "Redeclared Type: Person\n"
#         self.assertTrue(TestChecker.test(input,expect,505))
#     def test_506(self):
#         input = """
#         type Address struct {
#             street string
#             city string
#             country string
#         }
#         type Person struct {
#             name string
#             address Address
#         }
#         var huy Person;
#         var loc = huy.address.location();
#         """
#         expect = "Undeclared Method: location\n"
#         self.assertTrue(TestChecker.test(input,expect,506))
#     def test_507(self):
#         input = """
#         func (a Person) name() {
#             return
#         } 
#         type Person struct {
#             name string
#         }
               
#         """
#         expect = "Redeclared Field: name\n"
#         self.assertTrue(TestChecker.test(input,expect,507))       
#     def test_508(self):
#         input = """

#         type Person struct {
#             name string
#         }

#         func main() {

#             var Person int = 1;

#             var n string = Person.name;
#         }
#         """
#         expect = "Type Mismatch: FieldAccess(Id(Person),name)\n"
#         self.assertTrue(TestChecker.test(input,expect,508))
#     def test_509(self):
#         input = """
#         func (b A) foo() {
#             return
#         }
#         type A struct {
#             name string
#         }
#         func (a A) foo() {
#             return
#         }
#         """
#         expect = "Redeclared Method: foo\n"
#         self.assertTrue(TestChecker.test(input,expect,509))  
#     def test_510(self):
#         input = """
#         var a[5]int;
#         var b[5]int;
#         func main(){
#             b:= [5]int{1,2,3,4,5};
#             a := b;
#         }
#         """
#         expect = ""
#         self.assertTrue(TestChecker.test(input,expect,510))
        
#     def test_511(self):
#         input = Program(
#             [StructType("A",
#                         [("y",IntType())],[MethodDecl("a",Id("A"),FuncDecl("test",[],IntType(),Block([Return(FieldAccess(Id("a"),"y"))]))), MethodDecl("a",Id("A"),FuncDecl("y",[],IntType(),Block([Return(FieldAccess(Id("a"),"y"))])))]),])
#         expect = "Redeclared Method: y\n"
#         self.assertTrue(TestChecker.test(input, expect, 511))
    
#     def test_512(self):
#         input = """
#         func foo(){
#             return;
#         }
#         func main(){
#             a := foo();
#         }
#         """
#         expect = "Type Mismatch: Assign(Id(a),FuncCall(foo,[]))\n"
#         self.assertTrue(TestChecker.test(input, expect, 512))
#     def test_513(self):
#         input = """
#         type Community struct {
#             commu [3]Person
#         }
#         type Person struct {
#             name string
#         }
        
#         func main() {
#             var obj Community
#             var result = obj.commu[3].age
#         }
#         """
#         expect = "Undeclared Field: age\n"
#         self.assertTrue(TestChecker.test(input,expect,513))
#     def test_514(self):
#         input = """
#         type Person struct {
#             name string
#         }
#         var a Person;
#         var b = c.name;
#         """
#         expect = "Undeclared Identifier: c\n"
#         self.assertTrue(TestChecker.test(input,expect,514))
#     def test_515(self):
#         input = """
#             func main() int {
#                 return -main();
#             }
#             """
#         expect = """"""
#         self.assertTrue(TestChecker.test(input, expect, 515))

#     def test_516(self):
#         input = """
#         const a = 2
#         const b = 3
#         var arr[2][2]int;
#         func main(){
#             arr[0] := [3]int{1,2,3}
#         }
        
#         """
#         expect = "Type Mismatch: Assign(ArrayCell(Id(arr),[IntLiteral(0)]),ArrayLiteral([IntLiteral(3)],IntType,[IntLiteral(1),IntLiteral(2),IntLiteral(3)]))\n"
#         self.assertTrue(TestChecker.test(input, expect, 516))
        
#     def test_517(self):
#         input = """
#         var a [2][2]int;
#         func main(){
#             a[0] := 1;
#         }
#         """
#         expect = "Type Mismatch: Assign(ArrayCell(Id(a),[IntLiteral(0)]),IntLiteral(1))\n"
#         self.assertTrue(TestChecker.test(input, expect, 517))
#     def test_518(self):
#         input = """
#         var a[2][2]int;
#         var b[2] int = a[0];
#         """
#         expect = ""
#         self.assertTrue(TestChecker.test(input, expect, 518))
#     def test_519(self):
#         input = """
#         func main(){
#             var value_ int;
#             for index, value_ := range [5]int{1,2,3,4,5} {
#                 putInt(value_);
#             }
#         }
#         """
#         expect = "Undeclared Identifier: index\n"
#         self.assertTrue(TestChecker.test(input, expect, 519))
#     def test_520(self):
#         input = """
#         func main(){
#             var index int;
#             for _, value := range [5]int{1,2,3,4,5} {
#                 putInt(value);
#             }
#         }
#         """
#         expect = "Undeclared Identifier: value\n"
#         self.assertTrue(TestChecker.test(input, expect, 520))
#     def test_521(self):
#         input = """
#         func main(){
#             a := "string" + 1 + 2 - 3
#         }
#         """
#         expect = "Type Mismatch: BinaryOp(StringLiteral(\"string\"),+,IntLiteral(1))\n"
#         self.assertTrue(TestChecker.test(input, expect, 521))
#     def test_522(self):
#         input = """
#         func main(){
#             var index int
#             var value int
#             for index, value := range arr {
#                 putInt(value);
#             }
            
#         }
#         """
#         expect = "Undeclared Identifier: arr\n"
#         self.assertTrue(TestChecker.test(input, expect, 522))
#     def test_523(self):
#         input = """ 
#     const a = 2
#     const b = 2
#     func foo () [a]int {
#         var arr[2][2]int;
#         arr[0] := [2]int{1,2};
#         return arr[0];
#     }
#     """
#         expect = ""
#         self.assertTrue(TestChecker.test(input, expect, 523))
#     def test_524(self):
#         input = """
#         type Person struct {
#             name string
#             age int
#         }
#         func main(){
#             arr := [5]Person{Person{name: "Alice", age: 25},Person{name: "Bob", age: 30},Person{name: "Charlie", age: 35},Person{name: "David", age: 40},Person{name: "Eve", age: 45}}
#         }
#         """
#         expect = ""
#         self.assertTrue(TestChecker.test(input, expect, 524))
#     def test_525(self):
#         input = """
#         type A interface {
#             test()
#         }
#         func main(){
#             var b A
#             var c A
#             var arr[2]A = [2]A{b,c}
#         }
#         """
#         expect = ""
#         self.assertTrue(TestChecker.test(input, expect, 525))
#     def test_526(self):
#         input = """
#         type Person struct {
#             name string;
#             age int
#         }
#         const a = 5
#         func foo() [5]Person{
#             arr := [5]Person{Person{name: "Alice", age: 25},Person{name: "Bob", age: 30},Person{name: "Charlie", age: 35},Person{name: "David", age: 40},Person{name: "Eve", age: 45}}
#             return arr
#         }
#         """
#         expect = ""
#         self.assertTrue(TestChecker.test(input, expect, 526))
#     def test_527(self):
#         input = """
        
#         var a float = 1;
#         """
#         expect = ""
#         self.assertTrue(TestChecker.test(input, expect, 527))
#     def test_528(self):
#         input = """
#     var a [3][4] int;
#     var b [4] int = a;
# """
#         expect = """Type Mismatch: VarDecl(b,ArrayType(IntType,[IntLiteral(4)]),Id(a))\n"""
#         self.assertTrue(TestChecker.test(input, expect, 528))
#     def test_529(self):
#         input = """
#         var a int = 1;
#         var b float = 2.0;
#         var c int = a + b;
#         var d = a - b;
        
#         """
#         expect = """Type Mismatch: VarDecl(c,IntType,BinaryOp(Id(a),+,Id(b)))\n"""
#         self.assertTrue(TestChecker.test(input, expect, 529))
#     def test_530(self):
#         input = """
#         type A struct{
#             x int
#         }
#         func (a A) test() int {
#             return a.x;
#         }
#         func main(){
#             var a int;
#             var b A = A{x: 1};
#             var c = a + !b.test();
#         }
#         """
#         expect = "Type Mismatch: UnaryOp(!,MethodCall(Id(b),test,[]))\n"
#         self.assertTrue(TestChecker.test(input, expect, 530))
#     def test_531(self):
#         input = """
#         type A struct{
#             x int
#         }
#         type B struct{
#             y int
#         }
#         func foo(a A, b B) A{
#             return b;
#         }
#         """
#         expect = "Type Mismatch: Return(Id(b))\n"
#         self.assertTrue(TestChecker.test(input, expect, 531))
#     def test_532(self):
#         input = """
#         type A struct {
#             x int
#         }
#         type B interface {
#             test() int
#         }
#         func (a A) test() int {
#             return a.x;
#         }
#         func foo(a A, b B) B{
#             return a;
#         }
#         """
#         expect = "Type Mismatch: Return(Id(a))\n"
#         self.assertTrue(TestChecker.test(input, expect, 532))
#     def test_533(self):
#         input = """
#         type A interface {
#             test() int
#         }
#         type B interface {
#             test() int
#         }
#         func foo() A{
#             var a A
#             var b B
#             return b;
#         }
#         """
#         expect = "Type Mismatch: Return(Id(b))\n"
#         self.assertTrue(TestChecker.test(input, expect, 533))
#     def test_534(self):
#         input = """
#         type A struct {
#             x int;
#         }
#         type B interface {
#             test() int;
#         }
#         func (a A) test() int {
#             return a.x;
#         }
#         func foo() {
#             var a B = A{x: 1};
#         }
#         """
#         expect =""
#         self.assertTrue(TestChecker.test(input, expect, 534))
    # def test_535(self):
    #     input = """
    #     func foo(a int, b float, c string){
    #         var a int;
    #         var b float;
    #         var c string;
    #         putInt(a);
    #     }
    #     func main(){
    #         foo(foo(1, 2.0, "hello"), 2.0, "hello");
    #     }
    #     """
    #     expect = "Type Mismatch: FuncCall(foo,[FuncCall(foo,[IntLiteral(1),FloatLiteral(2.0),StringLiteral(\"hello\")]),FloatLiteral(2.0),StringLiteral(\"hello\")])\n"
    #     self.assertTrue(TestChecker.test(input, expect, 535))
                        
    
        
