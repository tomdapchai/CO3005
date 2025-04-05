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

    # def test3(self):
    #     input = """
    #     func foo() int { 
    #         var c = Car { name: "abc"}
    #         return foo()
    #     }

    #     func (c Car) getName() string {
    #         return c.name
    #     }
    #     type Car struct {
    #         name string
    #         owner [5][2] int
    #     }
        

    #     """
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input,expect,406))
    # def test4(self):
    #     input = """
    #     var n int = 2;

    #     func foo(a int, b int, c [n]int) [n]int {
    #     var x1 = 1 + 2 * 3
    #         var x2 int = 5 * 6;
    #         var x3 [x2]int;
    #         x3 := [30]int{1,2,3,4};
    #         var x4 [x2]int = x3;
    #         var x5 [2]int;
    #         var x6 [2]int = c
    #         const x7 = [x2]int{1,2,3,4};
    #         return x5;
    #     }
    #     """
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input,expect,407))
    
    # def test5(self):
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
    #     self.assertTrue(TestChecker.test(input,expect,408))

    # def test6(self):
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
    #     self.assertTrue(TestChecker.test(input,expect,409))

    # def test7(self):
    #     input = """
    #     var n int = 2;
    #     var i = 2
    #     func foo(a int, b int, c [n]int) int {
    #         var x1 = 1 + 2 * 3
    #         return a;
    #     }

    #     func foo1(a, b int) Person {
    #         a := foo(a, b, [2]int{1, 2})
    #         const p = Person { name: "abc", age: 1, salary: a}
    #         return p;
    #     }



    #     type Person struct {
    #         name string;
    #         age int;
    #         salary int;
    #     }

    #     func (p Person) foo() string {
    #         return p.name;
    #     }

    #     func (p Person) getInt1() int {
    #         return p.age;
    #     }

    #     func (p Person) getInt2() int {
    #         return p.age;
    #     }
        
    #     """
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input,expect,410))
    
    # def test8(self):
    #     input = """
    #     func foo(a,b,c int) A{
    #         return A{a:a, b:b, c:c, d:d}
    #     }
    #     func main(){
    #         var b A;
    #         b := foo(1,2,3)
    #     }
    #     type A struct{
    #         a int;
    #         b int;
    #         c int;
    #     }
    #     """
    #     expect = "Undeclared Field: d\n"
    #     self.assertTrue(TestChecker.test(input,expect,411))
    # def test_412(self):
    #     input = """
    #     const x = getInt() + 5;
    #     const x = 10;
    #     """
    #     expect = "Redeclared Constant: x\n"
    #     self.assertTrue(TestChecker.test(input,expect,412))
        
    # def test_413(self):
    #     input = """
    #     func test(a int, a float) {
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
    #         id int;
    #     }
    #     """
    #     expect = "Redeclared Type: Person\n"
    #     self.assertTrue(TestChecker.test(input,expect,414))
        
    # def test_415(self):
    #     input = """
    #     func add(a int, b int) int {
    #         return a + b;
    #     }
    #     func add(x float, y float) float {
    #         return x + y;
    #     }
    #     """
    #     expect = "Redeclared Function: add\n"
    #     self.assertTrue(TestChecker.test(input,expect,415))
        
    # def test_416(self):
    #     input = """
    #     type Vehicle struct {
    #         brand string;
    #     }
        
    #     func (v Vehicle) drive() {
    #         return;
    #     }
        
    #     func (v Vehicle) drive() int {
    #         return 0;
    #     }
    #     """
    #     expect = "Redeclared Method: drive\n"
    #     self.assertTrue(TestChecker.test(input,expect,416))
        
    # def test_417(self):
    #     input = """
    #     type Drawable interface {
    #         draw();
    #         draw(color string);
    #     }
    #     """
    #     expect = "Redeclared Prototype: draw\n"
    #     self.assertTrue(TestChecker.test(input,expect,417))
        
    # def test_418(self):
    #     input = """
    #     type Student struct {
    #         name string;
    #         name int;
    #     }
    #     """
    #     expect = "Redeclared Field: name\n"
    #     self.assertTrue(TestChecker.test(input,expect,418))
        
    # def test_419(self):
    #     input = """
    #     func main() {
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
    #         var x [1][2]int;
    #     }
    #     """
    #     expect = "Redeclared Variable: x\n" 
    #     self.assertTrue(TestChecker.test(input,expect,420))
        
    # def test_421(self):
    #     input = """
    #     func calculate(x int) int {
    #         var x int;
    #         x := 1;
    #         return x;
    #     }
        
    #     func main() {
    #         var x int;
    #         x := calculate(x);
    #     }
        
    #     func calculate(x float) {
    #         return;
    #     }
    #     """
    #     expect = "Redeclared Function: calculate\n"
    #     self.assertTrue(TestChecker.test(input,expect,421))
        
    # def test_422(self):
    #     input = """
    #     type Pair struct {
    #         first int;
    #         second int;
    #     }
    #     func main(){
    #         var x Pair;
    #         x := Pair{first: 1, second: 2};
    #         var y Pair;
    #         y := x.swap();
    #     }
    #     func (p Pair) swap() Pair {
    #         return Pair{first: p.second, second: p.first};
    #     }
        
    #     func swap(a int, b int) {
    #         var temp = a;
    #         a := b;
    #         b := temp;
    #     }
        
    #     func (p Pair) swap() Pair {
    #         return Pair{first: p.first, second: p.second};
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
        
    #     func main(){
    #         var x Pair;
    #         x := Pair{first: 1, second: 2};
    #         putInt(x.getInt());
    #     }
    #     var x = 10;
    #     func (p Pair) getInt() int {
    #         return p.first + x;
    #     }
    #     func (p Pair) getInt() int {
    #         return p.second;
    #     }
        
    #     """
    #     expect = "Redeclared Method: getInt\n"
    #     self.assertTrue(TestChecker.test(input,expect,423))
        
    # def test_424(self):
    #     input = """
    #     func test() {
    #         s := Subject{name: "Math", scores: [5]float{1.0, 2.0, 3.0, 4.0, 5.0}, scores: [5]int{1, 2, 3, 4, 5}};
    #         putFloat(s.scores[0]);
    #         s.putFloat();
    #     }
    #     func (s Subject) putFloat() float {
    #         return s.scores[0];
    #     }
    #     type Subject struct {
    #         name string;
    #         scores [5]float;
    #         scores [5]int;
    #     }
    #     func main() {
    #         test();
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
    #     type Teacher struct {
    #         person Person;
    #         students [5]Student;
    #     }
    #     func (p Person) getName() string {
    #         return p.name;
    #     }
    #     """
    #     expect = "Redeclared Method: getName\n" 
    #     self.assertTrue(TestChecker.test(input,expect,425))
        
    # def test_426(self):
    #     input = """
    #     func test(x, y int, z float) {
    #         var x int;
    #         var z float;
    #         t := 1;
    #         const t = 2;
    #     }
    #     """
    #     expect = "Redeclared Constant: t\n"
    #     self.assertTrue(TestChecker.test(input,expect,426))
        
    # def test_427(self):
    #     input = """
    #     func foo(){
    #         x:= 1;
    #         y := 2;
            
            
    #         y := 3;
    #     }
    #     const z = 1;
    #     var z = 2;
    #     """
    #     expect = "Redeclared Variable: z\n" 
    #     self.assertTrue(TestChecker.test(input,expect,427))
        
    # def test_428(self):
    #     input = """
    #     func foo(x,y,z int, t float) int {
    #         var x int;
    #         y := 2;
    #         z := 3;
    #         var t float = 1.0;
    #         k := 1;
    #         return k;
    #     }
    #     func main(){
    #         t := foo(1,2,3,4.0);
    #         putInt(t);
    #     }
    #     const k = 1;
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
        
    #     const test = 1;
    #     func foo(){
    #         putInt(test);
    #     }
        
    #     var test = 2;
    #     """
    #     expect = "Redeclared Variable: test\n" 
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
    #         x := y;
    #         putInt(x);
    #     }
    #     """
    #     expect = "Undeclared Identifier: y\n"
    #     self.assertTrue(TestChecker.test(input,expect,431))
    # def test_432(self):
    #     input = """
    #     var b boolean;
    #     var c int;
    #     var a = c+d;
    #     var d = b + c;
    #     var e = b + 1;
    #     """
    #     expect = "Undeclared Identifier: d\n"
    #     self.assertTrue(TestChecker.test(input,expect,432))
    # def test_433(self):
    #     input = """
    #     var a = 2 + 5 * 3;
    #     var b = a + 1;
    #     var c = a * b;
    #     var d = c - 1;
    #     var e = d / 2;
    #     func foo(){
    #         k := a + b;
    #         putInt(k);
    #         var c = d + e;
    #         putInt(c);
    #         var e = h + 1;
    #     }
    #     """
    #     expect = "Undeclared Identifier: h\n"
    #     self.assertTrue(TestChecker.test(input,expect,433))
    # def test_434(self):
    #     input = """
    #     var a[1]int = [1]int{1};
    #     var b [5]int;
    #     func foo(){
    #         b := [5]int{1,2,3,4,5};
    #         var c = a[0];
    #         putInt(c);
    #         var d = e+1;
    #     }
    #     var e int = 2;
    #     """
    #     expect = "Undeclared Identifier: e\n"
    #     self.assertTrue(TestChecker.test(input,expect,434))
    # def test_435(self):
    #     input = """
    #     const a = 1;
    #     const b = 2;
    #     const c = d + 3;
    #     const d = 4;
    #     """
    #     expect = "Undeclared Identifier: d\n"
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
    #     var a Person;
    #     func main(){
    #         a.printInfo();
    #     }
    #     """
    #     expect = "Undeclared Method: printInfo\n"
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
    #     func main(){
    #         var a A;
    #         putInt(a.test());
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
    #     func (b B) test3() int {
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
    #     func main(){
    #         var a A;
    #         a := A{x: 1, other: B{x: 2}};
    #         putInt(a.test());
    #         putInt(a.test1());
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
    #         return b.x + b.other.test() + b.other.test1();
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
    #     func (b B) foo1(c int) int {
    #         return b.x;
    #     }
    #     func main(){
    #         var a A;
    #         a := foo();
    #         putInt(a.test1());
    #         putInt(a.foo(1));
    #         putInt(a.foo1(2));
    #         putInt(a.foo2(3));
    #     }
    #     """
    #     expect = "Undeclared Method: foo2\n"
    #     self.assertTrue(TestChecker.test(input,expect,445))
    # def test_446(self):
    #     input = """
    #     type Vehicle struct{
    #         brand string;
    #         year int;
    #     }
    #     type Truck interface {
    #         drive() int;
    #     }
    #     func main(){
    #         var t Truck;
    #         t := Vehicle{brand: "Ford", year: 2020};
    #         putInt(t.drive());
    #     }
    #     func (v Vehicle) drive() int {
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
    #     func main(){
    #         var c C;
    #         c := C{a: 1, b: 2.0};
    #         putInt(c.test());
    #         var d D;
    #         d := C{a: 1, b: 2.0};
    #         putInt(d.test());
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
    #         a := A{x: 1, y:2};
    #         putInt(a.test());
    #     }
    #     func (a A) test() int {
    #         return a.test1();
    #     }
    #     func (a A) test1() int {
    #         return a.x;
    #     }
    #     type A struct {
    #         x int;
    #     }
    #     """
    #     expect = "Undeclared Field: y\n"
    #     self.assertTrue(TestChecker.test(input,expect,448))
    # def test_449(self):
    #     input = """
    #     func foo(a,b,c int) A{
    #         return A{a:a, b:b, c:c, d:d}
    #     }
    #     func main(){
    #         var b A;
    #         b := foo(1,2,3)
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
    #         [StructType("A",
    #                     [("x",IntType)],[MethodDecl("a",Id("A"),FuncDecl("test",[],IntType,Block([Return(FieldAccess(Id("a"),"y"))])))]),])
    #     expect = "Undeclared Field: y\n"
    # #     self.assertTrue(TestChecker.test(input, expect, 450))
    # def test_451(self):
    #     input = """
    #     var a int;
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
    #     var e = a + b;
    #     """
    #     expect = "Type Mismatch: BinaryOp(Id(a),+,Id(b))\n"
    #     self.assertTrue(TestChecker.test(input,expect,455))
    # def test_456(self):
    #     input = """
    #     var a [5]int;
    #     func foo(){
    #         a := [5]int{1,2.0,3,4,5};
    #         a := [5]int{1,2,3};
    #     }
    #     """
    #     expect = "Type Mismatch: ArrayLiteral([IntLiteral(5)],IntType,[IntLiteral(1),FloatLiteral(2.0),IntLiteral(3),IntLiteral(4),IntLiteral(5)])\n"
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
    #         c := a && b;
    #     }
    #     """
    #     expect = "Type Mismatch: BinaryOp(Id(a),&&,Id(b))\n"
    #     self.assertTrue(TestChecker.test(input,expect,458))
    # def test_459(self):
    #     input = """
    #     const a = 2;
    #     const b = 3;
    #     const c = a + b;
    #     var d [a][b]int;
    #     func foo(){
    #         d := [a][b]int{{1,2,3},{4,5,6}};
    #     }
    #     func main(){
    #         foo();
    #         putInt(d[0][0]);
    #         putInt(d[1][1]);
    #         putFloat(d[0][1]);
    #     }
    #     """
    #     expect = "Type Mismatch: FuncCall(putFloat,[ArrayCell(Id(d),[IntLiteral(0),IntLiteral(1)])])\n"
    #     self.assertTrue(TestChecker.test(input,expect,459))
    # def test_460(self):
    #     input = """
    #     type A struct {
    #         x int;
    #         y float;
    #         other B;
    #     }
    #     func (a A) test(x int, y float) {
    #         var x int;
    #         var y = x;
    #         var z = y + 1;
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
    #         putFloat(a.y);
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
    #         var x int;
    #         var y float;
    #         var z Person;
    #         var w = x + y;
    #         var v = z.test();
    #         putInt(x);
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
    #         return 0xFF;
    #     }
    #     func bar(b int) int{
    #         return 0b101;
    #     }
    #     func main(){
    #         putInt(foo(bar(foo(bar(foo(bar(foo(2.0))))))));
    #     }
    #     """
    #     expect = "Type Mismatch: FuncCall(foo,[FloatLiteral(2.0)])\n"
    #     self.assertTrue(TestChecker.test(input,expect,463))
    # def test_464(self):
    #     input = """
    #     func main(){
    #         a := foo(1,2);
    #         b := a + 1;
    #         c := a > b;
    #     }
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
            
    #         for a < "hello" {
    #             putInt(a);
    #             a += 1;
    #         }
    #     }
    #     """
    #     expect = "Type Mismatch: BinaryOp(Id(a),<,StringLiteral(\"hello\"))\n"
    #     self.assertTrue(TestChecker.test(input,expect,465))
    # def test_466(self):
    #     input = """
    #     func main(){
    #         var a int;
    #         var b float;
    #         for a < b {
    #             putInt(a);
    #             a += 1;
    #         }
    #     }
    #     """
    #     expect = "Type Mismatch: BinaryOp(Id(a),<,Id(b))\n"
    #     self.assertTrue(TestChecker.test(input,expect,466))
    # def test_467(self):
    #     input = """
    #     func testLoop(k int){
    #         for i := 0; i < k; i+=1 {
    #             putInt(i);
    #         }
    #         for var j = 1.0; j < k; j+=1 {
    #             putInt(j);
    #         }
    #     }
    #     """
    #     expect = "Type Mismatch: BinaryOp(Id(j),<,Id(k))\n"
    #     self.assertTrue(TestChecker.test(input,expect,467))
    # def test_468(self):
    #     input = """
    #     func main(){
    #         for _, value := range [5]float{1.0,2.0,3.0,4.0,5.0} {
    #             putInt(value);
    #         }
    #         var value string;
    #         var index int;
    #         arr := [5]int{1,2,3,4,5};
    #         for index, value := range arr {
    #             putInt(index);
    #             putString(value);
    #         }
    #     }
    #     """
    #     expect = "Type Mismatch: FuncCall(putInt,[Id(value)])\n"
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
        
    #     func main(){
    #         const c = true;
    #         foo();
    #     }
    #     """
    #     expect = "Type Mismatch: If(Id(c),Block([FuncCall(putString,[StringLiteral(\"False\")])]),Block([FuncCall(putString,[StringLiteral(\"True\")])]))\n"
    #     self.assertTrue(TestChecker.test(input,expect,469))
    # def test_470(self):
    #     input = """
    #     const a = 2
    #     const b = 3
    #     const c = a + b
    #     var d [a][b]float = [2][3]int{{1,2,3},{4,5,6}}

    #     func foo(a int, b int) int {
    #         if (a > b) {
    #         var k int;
    #             putInt(a)
    #             if (a > b) {
    #                 return k;
    #             }
    #         } else if (b < c){
    #             putInt(b)
    #         } else {
    #             putInt(c)
    #         }
    #     }
    #     func main(){
    #         var c boolean = true;
    #         var x = foo(1, 2);
    #         putFloat(c);
    #     }
    #     """
    #     expect = "Type Mismatch: FuncCall(putFloat,[Id(c)])\n"
    #     self.assertTrue(TestChecker.test(input,expect,470))
    
    # def test_471(self):
    #     input = """
    #     const a = 2
    #     const b = 3
    #     const c = a + b
    #     var d [a][b]float = [2][3]int{{1,2,3},{4,5,6}}

        

    #     const n = 12;

    #     var x = Person{name: "Tam", inventory: [12]int{1,2,3,4,5,6,7,8,9,10,11,12}}

    #     type Person struct {
    #         name string;
    #         inventory [n]int;
    #     }

        

    #     func foo(a int, b int) int {
    #         if (a > b) {
    #         var k int;
    #             putInt(a)
    #             if (a > b) {
    #                 return k;
    #             }
    #         } else if (b < c){
    #             putInt(b)
    #         } else {
    #             putInt(c)
    #         }
    #     }
    #     func main(){
    #         var c boolean = true;
    #         var x = foo(1, 2);
    #         putFloat(c);
    #     }
    #     """
    #     expect = "Type Mismatch: FuncCall(putFloat,[Id(c)])\n"
    #     self.assertTrue(TestChecker.test(input,expect,471))
    
    def test_472(self):
        input = """
        const a = 2
        const b = 3
        const c = a + b
        var d [a][b]float = [2][3]int{{1,2,3},{4,5,6}}

        const n = 12;

        var x = Person{name: "Tam", inventory: [12]int{1,2,3,4,5,6,7,8,9,10,11,12}}


        func (p Person) foo() {
            var n = 1;
        }

        func a() {
            n += 3;
        }



        type Person struct {
            name string;
            inventory [n]int;
        }

        func main() int{
            a();
            return 0;
        }
        
        """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,472))