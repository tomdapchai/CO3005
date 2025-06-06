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
        var a int = 10
        var y int = 15

        func main() {
            var a int = 5;
            var b int = 10;
            var c int = 15;
            var d int = 20;
            putInt((a + b + c + d % a) * a / y);
        };"""
        expect = "10"
        self.assertTrue(TestCodeGen.test(input,expect,509))

    def test_4(self):
        input = """
        var a int = 10
        var y float = 15.5

        func main() {
            var a int = 5;
            var b int = 10;
            var c int = 15;
            var d int = 20;
            putFloat((a + b + c + d % a) * a + y);
        };"""
        expect = "165.5"
        self.assertTrue(TestCodeGen.test(input,expect,510))

    def test_5(self):
        input = """
        var a int = 10
        var y float = 15.5

        func main() {
            var a = 5 * 2 - 10 + 5;
            var b = 10;
            var c = 15;
            var d int = 20;
            putFloat((a + b + c + d % a) * a - y);
        };
        
        """
        expect = "134.5"
        self.assertTrue(TestCodeGen.test(input,expect,511))
    
    def test_6(self):
        input = """
        var a = 5 + 0
        var y = 15.5

        func main() {
            var b = 10;
            var c = 15;
            var d int = 20;
            putFloat((a + b + c + d % a) * a - y);
        };
        
        """
        expect = "134.5"
        self.assertTrue(TestCodeGen.test(input,expect,512))

    def test_7(self):
        input = """
        const a = 20 * 10
        var y = 15.5 * 2

        func main() {
            putFloat(a + y)
        };
        
        """
        expect = "231.0"
        self.assertTrue(TestCodeGen.test(input,expect,513))

    def test_8(self):
        input = """
        const a = 20 * 10
        var y = 15.5

        func main() {
            const x = 10 * 2 + 3
            var a = 20
            putFloatLn(a + y)
            a := a + 10
            putInt(x * a)

        };
        
        """
        expect = "35.5\n690"
        self.assertTrue(TestCodeGen.test(input,expect,514))

    def test_9(self):
        input = """
        const a = 20 * 10
        var y = 15.5

        func main() {
            const x = 10 * 2 + 3
            var a = 20
            putFloatLn(a + y)
            a := a + 10
            putIntLn(x * a)
            y += 10
            putFloat(y)

        };
        
        """
        expect = "35.5\n690\n25.5"
        self.assertTrue(TestCodeGen.test(input,expect,515))

    def test_10(self):
        input = """
        const a = 20 * 10
        var y = 15.5

        

        func main() {
            const x = 10 * 2 + 3
            var a = 20
            putFloatLn(a + y)
            a := a + 10
            putIntLn(x * a)
            y += 10
            putFloatLn(y)
            putInt(a + foo())

        };
        
        func foo() int {
            return 1 + 2;
        }
        """
        expect = "35.5\n690\n25.5\n33"
        self.assertTrue(TestCodeGen.test(input,expect,516))


    def test_11(self):
        input = """
        const a = 20 * 10
        var y = 15.5

        func main() {
            if (y >= 16) {
                putInt(a + foo())
            } else {
                putInt(a + foo() + 1)
            }
        };
        
        func foo() int {
            return 1 + 2;
        }
        """
        expect = "204"
        self.assertTrue(TestCodeGen.test(input,expect,517))

    def test_12(self):
        input = """
        const a = 20 * 10
        var y = 15.5

        func main() {
            if (y >= 16) {
                putInt(a + foo())
            } else {
                if (a + 10 >= 211) {
                    putIntLn(234)
                } else {
                    var x = 5;
                    for x < 10 {
                        putIntLn(567)
                        x += 1;
                    }
                }
                putInt(a + foo() + 1)
            }
            for i := 0; i < 10; i += 1 {
                putInt(i)
            }
        };
        
        func foo() int {
            return 1 + 2;
        }
        """
        expect = "567\n567\n567\n567\n567\n2040123456789"
        self.assertTrue(TestCodeGen.test(input,expect,518))

    def test_13(self):
        input = """
        const a = 20 * 10
        var y = 15.5
        var x = "Hello World"
        func main() {
            putStringLn(x)
            putString("Welcome 2025")
        };
        """
        expect = "Hello World\nWelcome 2025"
        self.assertTrue(TestCodeGen.test(input,expect,519))

    def test_14(self):
        input = """
        const a = 20 * 10
        var y = 15.5

        func main() {
            if (y >= 16) {
                putInt(a + foo())
            } else {
                if (a + 10 >= 211) {
                    putIntLn(234)
                } else {
                    var x = 5;
                    for x < 10 {
                        putIntLn(567)
                        x += 1;
                    }
                }
                putInt(a + foo() + 1)
            }
            for i := 0; i < 10; i += 1 {
                if (i <= 4) {
                    if (foo() > 2 && i < 3) {
                        continue;
                    }
                }
                putInt(i)
                if (i == 8) {
                    break;
                }

            }
        };
        
        func foo() int {
            return 1 + 2;
        }
        """
        expect = "567\n567\n567\n567\n567\n204345678"
        self.assertTrue(TestCodeGen.test(input,expect,520))

    def test_15(self):
        input = """
        const a = 5;
        func main() {
            var b = 3;
            var a [4]int = [4]int{5, 2, 3, 4}
            var arr [5]int = [5]int{10, 20, 30, 40, 50}
            a[1] := 20
            var x = 10;
            putIntLn(a[0] + arr[0] * 2 + a[1])
        }
        """
        expect = "45\n"
        self.assertTrue(TestCodeGen.test(input,expect,521))

    def test_16(self):
        input = """
        const a = 5;
        func main() {
            var b = 3;
            var a [4]int = [4]int{5, 2, 3, 4}
            var arr [3][4]int = [3][4]int{{1, 2, 3}, {1, 2, 3, 4}, {10, 20}}
            
            var x = 10;
            putIntLn(a[0] + arr[2][1] * 2)
            putIntLn(arr[0][3])
            arr[0][3] := 10
            putIntLn(arr[0][3])
        }
        """
        expect = "45\n0\n10\n"
        self.assertTrue(TestCodeGen.test(input,expect,522))
    
    def test_17(self):
        input = """
        const a = 5;
        func main() {

            var b = foo()[0] + 1
            putIntLn(b)
        }

        // somehow this test works so well idk lololol

        func foo() [3]int {
        
            return [3]int{1, 2, 3}
        }
        """
        expect = "2\n"
        self.assertTrue(TestCodeGen.test(input,expect,523))

    def test_18(self):
        input = """
        const a = 5;
        var b = 5;

        func (p Person) foo() {
            var x = 10;
        }

        type Person struct {
            name string;
            age int;
        }

        func main() {
            var x Person = Person{name: "John", age: 30}
            var y Person = Person{name: "Doe", age: 25}
            putIntLn(x.age)
            putStringLn(x.name)
            putIntLn(y.age)
            putStringLn(y.name)
            putIntLn(x.age)
            putStringLn(x.name)
        }

        
        """
        expect = "30\nJohn\n25\nDoe\n30\nJohn\n"
        self.assertTrue(TestCodeGen.test(input,expect,524))
    
    def test_19(self):
        input = """
        type Person struct {
            name string;
            age int;
        }

        func main() {
            var x Person = Person{name: "John", age: 30}
            x.age := 35 * 2
            var y Person = Person{name: "Jane", age: 25}
            y.name += " Doe"
            putIntLn(x.age)
            putStringLn(y.name)
        }

        
        """
        expect = "70\nJane Doe\n"
        self.assertTrue(TestCodeGen.test(input,expect,525))
    
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
    
    def test_21(self):
        input = """
        type Person struct {
            name string;
            age int;
            height float;
        }

        func foo(a int, n string, h float) Person {
            var k Person = Person{name: n, age: a, height: h}
            return k
        } 

        func main() {
            var x Person = foo(30, "John", 177.3)
            putIntLn(x.age)
        }

        
        """
        expect = "30\n"
        self.assertTrue(TestCodeGen.test(input,expect,527))

    def test_22(self):
        input = """
        type Person struct {
            name string;
            age int;
            height float;
        }

        func (p Person) foo(a, b int) int {
            var x = 10;

            var c int = x + p.age + a * b
            var d Person = Person{name: "Doe", age: 25, height: 180.5}
            var p int = 20 + d.age // try to shadowing
            return c + p
        }

        func (p Person) bar() {
            putStringLn(p.name)
            putIntLn(p.age)
            putFloatLn(p.height)
        }

        func main() {
            var x Person = Person{name: "John", age: 30, height: 177.3}
            putIntLn(x.foo(2, 5))
            x.bar()
        }

        
        """
        expect = "95\nJohn\n30\n177.3\n"
        self.assertTrue(TestCodeGen.test(input,expect,528))

    def test_23(self):
        input = """
        type Person struct {
            name string;
            age int;
            height float;
        }

        func (p Person) foo(a, b int) Person {
            
            var d Person = Person{name: "Doe", age: 25, height: 180.5}
            d.name += " " + p.name
            return d
        }

        func (p Person) bar() {
            putStringLn(p.name)
            putIntLn(p.age)
            putFloatLn(p.height)
        }
        func main() {
            var x Person = Person{name: "John", age: 30, height: 177.3}
            x.foo(2, 5).bar()
        }

        
        """
        expect = "Doe John\n25\n180.5\n"
        self.assertTrue(TestCodeGen.test(input,expect,529))

    def test_24(self):
        input = """
        

        type Person struct {
            name string;
            age int;
            height float;
            car Car
        }

        type Car struct {
            name string;
            year int;
        }

        func init(name string, age int, height float, car Car) Person {
            return Person{name: name, age: age, height: height, car: car}
        }

        func (c Car) init(name string, year int) Car {
            return Car{name: name, year: year}
        }

        func (c Car) print() {
            putStringLn(c.name)
            putIntLn(c.year)
        }

        func (p Person) bar() {
            putStringLn(p.name)
            putIntLn(p.age)
            putFloatLn(p.height)
            p.car.print()
        }

        func main() {
            var car Car = Car{name: "Toyota", year: 2020}
            var x Person = init("John", 30, 177.3, car)
            x.bar()
        }

        
        """
        expect = "John\n30\n177.3\nToyota\n2020\n"
        self.assertTrue(TestCodeGen.test(input,expect,530))

    def test_25(self):
        input = """

        type Person struct {
            name string;
            age int;
            height float;
        }

        type IPerson interface {
            init(name string, age int, height float) Person;
            bar();
        }

        func (p Person) init(name string, age int, height float) Person {
            return Person{name: name, age: age, height: height}
        }

        func (p Person) bar() {
            putStringLn(p.name)
            putIntLn(p.age)
            putFloatLn(p.height)
        }

        func main() {
            var x Person
            x := Person{name: "John", age: 30, height: 177.3}
            var y IPerson
            y := x
            putStringLn(x.name)
            y.bar()
        }

        
        """
        expect = "John\nJohn\n30\n177.3\n"
        self.assertTrue(TestCodeGen.test(input,expect,531))

    def test_26(self):
        input = """
        type Test2 struct {
            z int
        }
        type Test1 struct {
            y Test2
        }
        type Test struct {
            x Test1
        }

        func main() {
            var a Test = Test{x: Test1{y: Test2{z: 10}}}
            var m = 2
            var n = 10
            putIntLn(a.x.y.z)
            a.x.y.z := n * m
            putIntLn(a.x.y.z)
        }
        """
        expect = "10\n20\n"
        self.assertTrue(TestCodeGen.test(input,expect,532))

    def test_27(self):
        input = """
        type Test struct {
            x int
        }

        var a Test = Test{x: 10}

        func main() {
            putIntLn(a.x)
            
        }
        """
        expect = "10\n"
        self.assertTrue(TestCodeGen.test(input,expect,533))
    
    def test_28(self):
        input = """
        type Test struct {
            x int
        }

        var a Test;

        func main() {
            a.x := 20
            putIntLn(a.x)
            a.x := 30
            putIntLn(a.x)
            var n int
            n := 20
            putIntLn(n)
            
        }
        """
        expect = "20\n30\n20\n"
        self.assertTrue(TestCodeGen.test(input,expect,534))

    def test_29(self):
        input = """
        type Person struct {
            name string;
            age int;
            height float;
        }

        type IPerson interface {
            init(name string, age int, height float) Person;
            bar();
        }

        func (p Person) init(name string, age int, height float) Person {
            return Person{name: name, age: age, height: height}
        }

        func (p Person) bar() {
            putStringLn(p.name)
            putIntLn(p.age)
            putFloatLn(p.height)
        }

        var a IPerson = Person{name: "John", age: 30, height: 177.3}

        func main() {
            a.bar()
            
        }
        """
        expect = "John\n30\n177.3\n"
        self.assertTrue(TestCodeGen.test(input,expect,535))

    def test_30(self):
        input = """
        type Person struct {
            name string;
            age int;
            height float;
        }

        type IPerson interface {
            init(name string, age int, height float) Person;
            bar();
        }

        func (p Person) init(name string, age int, height float) Person {
            return Person{name: name, age: age, height: height}
        }

        func (p Person) bar() {
            putStringLn(p.name)
            putIntLn(p.age)
            putFloatLn(p.height)
        }

        var a IPerson 

        func main() {
            a := Person{name: "John", age: 30, height: 177.3}
            a.bar()
            
        }
        """
        expect = "John\n30\n177.3\n"
        self.assertTrue(TestCodeGen.test(input,expect,536))
    
    def test_31(self):
        input = """

        var a = [3]int{1, 2, 3}

        func main() {
            putIntLn(a[0])
            a[1] += 10
            putIntLn(a[1])
        }
        """
        expect = "1\n12\n"
        self.assertTrue(TestCodeGen.test(input,expect,537))
    
    def test_32(self):
        input = """
        var a = [3][4]int{{1, 2}, {4, 5, 6, 7}, {10, 8, 9}}

        func main() {
            putIntLn(a[0][0])
            a[0][1] += 10
            putIntLn(a[0][1])
            a[2][1] -= 20
            putIntLn(a[2][1])
        }
        """
        expect = "1\n12\n-12\n"
        self.assertTrue(TestCodeGen.test(input,expect,538))
    
    def test_33(self):
        input = """

        func main() {
            var a [3][4]int
            a := [3][4]int{{1, 2}, {4, 5, 6, 7}, {10, 8, 9}}
            putIntLn(a[0][0])
        }
        """
        expect = "1\n"
        self.assertTrue(TestCodeGen.test(input,expect,539))

    def test_34(self):
        input = """
        var a [3][4]int

        func main() {
            a := [3][4]int{{1, 2}, {4, 5, 6, 7}, {10, 8, 9}}
            putIntLn(a[0][0])
            a[0][1] += 10
            putIntLn(a[0][1])
            a[2][1] -= 20
            putIntLn(a[2][1])
        }
        """
        expect = "1\n12\n-12\n"
        self.assertTrue(TestCodeGen.test(input,expect,540))

    def test_35(self):
        input = """
        var a = [3][4]int{{1, 2}, {4, 5, 6, 7}, {10, 8, 9}}

        func main() { 
            putIntLn(a[0][0])
            a[0][1] += 10
            putIntLn(a[0][1])
            a[2][1] -= 20
            putIntLn(a[2][1])
        }
        """
        expect = "1\n12\n-12\n"
        self.assertTrue(TestCodeGen.test(input,expect,541))
    
    def test_36(self):
        input = """

        func main() { 
            var a float = 1 + 2
            putFloatLn(a)
        }
        """
        expect = "3.0\n"
        self.assertTrue(TestCodeGen.test(input,expect,542))

    def test_37(self):
        input = """
        var arr = [5]int{0,1,2,3,4}

        func main() { 
            arr2 := arr
            arr2[3] := 300000
            putIntLn(arr[3])
            putIntLn(arr2[3])
        }
        """
        expect = "300000\n300000\n"
        self.assertTrue(TestCodeGen.test(input,expect,543))

    def test_38(self):
        input = """
        type Person struct {
            name string;
            age int;
            height float;
        }

        type IPerson interface {
            init(name string, age int, height float) Person;
            bar();
        }

        func (p Person) init(name string, age int, height float) Person {
            return Person{name: name, age: age, height: height}
        }

        func (p Person) bar() {
            putStringLn(p.name)
            putIntLn(p.age)
            putFloatLn(p.height)
        }

        func foo(p Person, a int) {
            p.name := "Hello"
        }

        func main() { 
            var p Person = Person{name: "John", age: 30, height: 177.3}
            
            foo(p, 10)
            putStringLn(p.name)
        }
        """
        expect = "Hello\n"
        self.assertTrue(TestCodeGen.test(input,expect,544))
    
    def test_39(self):
        input = """
        var x float

        func main() { 
            
            x := 10 + 3
            putFloatLn(x)
        }
        """
        expect = "13.0\n"
        self.assertTrue(TestCodeGen.test(input,expect,545))
    
    def test_40(self):
        input = """
        var x float

        func main() { 
        var a int = 3
        var b int = 5
            var n = [3]float{1, 2, 3}
            x := 10 + 3
            putFloatLn(n[0] + n[1] + n[2])
        }
        """
        expect = "6.0\n"
        self.assertTrue(TestCodeGen.test(input,expect,546))
    
    def test_41(self):
        input = """
        var x float

        func main() { 
        var a int = 3
        var b int = 5
            var n = [3][4]float{{1.2, 2.3, 3}, {4.5, 5.6, 6.55, 7.8}, {10.2, 8, 9}}
            putFloatLn(n[0][2] + n[1][0])
        }
        """
        expect = "7.5\n"
        self.assertTrue(TestCodeGen.test(input,expect,547))
    
    def test_42(self):
        input = """
        var x float

        func main() { 
            var n = [2][3][4]float{{{1.2, 2.3, 3}, {4.5, 5.6, 6.55, 7.8}, {10.2, 9, 9}}, {{1.2, 2.3, 3}, {4.5, 5.6, 6.55, 7.8}, {10.2, 8.0, 9}}}
            putFloatLn(n[0][2][2] + n[1][0][0])
        }
        """
        expect = "10.2\n"
        self.assertTrue(TestCodeGen.test(input,expect,548))

    def test_43(self):
        input = """
        type Person struct {
            name string
            age int
            car Car
        }

        type Car struct {
            year int
            brand string
        }

        func (c Car) print() {
            putStringLn(c.brand)
            putIntLn(c.year)
        }

        func main() { 
            var a Person = Person{name: "John", car: Car{year: 2020, brand: "Toyota"}}
            a.age := 30
            putStringLn(a.name)
            putIntLn(a.age)
            a.car.print()

        }
        """
        expect = "John\n30\nToyota\n2020\n"
        self.assertTrue(TestCodeGen.test(input,expect,549))

    def test_44(self):
        input = """
        

        type Person struct {
            name string
            age int
            car Car
        }

        type Car struct {
            year int
            brand string
        }

        func (c Car) print() {
            putStringLn(c.brand)
            putIntLn(c.year)
        }
        var arr [3]Person 

        func main() { 
        
        arr := [3]Person{Person{name: "Doe", car: Car{year: 2021, brand: "Honda"}, age: 25}, Person{name: "Jane", car: Car{year: 2022, brand: "Ford"}, age: 28}, Person{name: "Smith", car: Car{year: 2023, brand: "BMW"}, age: 35}}
            arr[0].car.print()

        }
        """
        expect = "Honda\n2021\n"
        self.assertTrue(TestCodeGen.test(input,expect,550))

    def test_45(self):
        input = """
        

        func main() { 
        
        var a = 3
        var arr [a]int = [a]int{1, 2, 3}
        var x = 2
        arr[x + a - 3] := 6
        putIntLn(arr[2])

        }
        """
        expect = "6\n"
        self.assertTrue(TestCodeGen.test(input,expect,551))

    def test_46(self):
        input = """
        const size = 3

        func main() { 
        
        var a = 3
        var arr [a]int = foo(1)
        var x = 2
        arr[x + a - 3] := 6
        putIntLn(arr[2])
        putIntLn(arr[0])

        }

        func foo(a int) [size]int {
            return [size]int{a, a, a}
        }
        """
        expect = "6\n1\n"
        self.assertTrue(TestCodeGen.test(input,expect,552))

    def test_47(self):
        input = """
        const size = 3

        func main() { 
        
        var a = "b"
        putBoolLn(foo(a))

        }

        func foo(a string) boolean {
            return a > "a"
        } 
        """
        expect = "true\n"
        self.assertTrue(TestCodeGen.test(input,expect,553))

    def test_48(self):
        input = """
        const MAX = 10
        func arrsort (arr [MAX]int){
            for i := 0; i<MAX; i+=1{
                for j:=0; j < i; j+=1{
                    if (arr[i] < arr[j]){
                        var temp = arr[i]
                        arr[i] := arr[j]
                        arr[j] := temp
                    }
                }
            }
        }
        func main(){
            var arr[MAX]int = [MAX]int{4,2,3,7,8,9,12,14,15,11}
            arrsort(arr)
            for i := 0; i<MAX; i+=1{
                putInt(arr[i])
            }
        }
        """
        expect = "23478911121415"
        self.assertTrue(TestCodeGen.test(input, expect, 554))
    
    def test_49(self):
        input = """
        func binSearch(arr [10]int, x int, n int) int {
            l := 0;
            h := n - 1
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

        func main() {
            var arr [10]int = [10]int{1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
            var x int = 5;
            var result int = binSearch(arr, x, 10);
            putIntLn(result);
        }
        """
        expect = "4\n"
        self.assertTrue(TestCodeGen.test(input, expect, 555))

    def test_50(self):
        input = """
        func quickSort(arr [10]int, low int, high int) {
            if (low < high) {
                // Partition the array and get the pivot index
                pivotIndex := partition(arr, low, high)
                
                // Recursively sort elements before and after the pivot
                quickSort(arr, low, pivotIndex - 1)
                quickSort(arr, pivotIndex + 1, high)
            }
        }

        func partition(arr [10]int, low int, high int) int {
            pivot := arr[high]
            i := low - 1  // Index of smaller element
            
            for j := low; j < high; j += 1 {
                // If current element is smaller than or equal to pivot
                if (arr[j] <= pivot) {
                    i += 1
                    // Swap arr[i] and arr[j]
                    temp := arr[i]
                    arr[i] := arr[j]
                    arr[j] := temp
                }
            }
            
            // Swap arr[i+1] and arr[high] (put pivot in correct position)
            temp := arr[i+1]
            arr[i+1] := arr[high]
            arr[high] := temp
            
            return i + 1
        }

        func main() {
            var arr [10]int = [10]int{4, 2, 3, 7, 8, 9, 12, 14, 15, 11};
            quickSort(arr, 0, 9);
            for i := 0; i < 10; i += 1 {
                putIntLn(arr[i]);
            }
        }
        """
        expect = "2\n3\n4\n7\n8\n9\n11\n12\n14\n15\n"
        self.assertTrue(TestCodeGen.test(input, expect, 556))

    def test_51(self):
        input = """
        type HashTable struct {
            size int;
            table [10]int;
        }

        func (h HashTable) hash(key int) int {
            return key % h.size;
        }

        func main() {
            var h HashTable = HashTable{size: 10, table: [10]int{0, 0, 0, 0, 0, 0, 0, 0, 0, 0}};
            var key int = 5;
            var index int = h.hash(key);
            h.table[index] := key;
            
            for i := 0; i < h.size; i += 1 {
                putIntLn(h.table[i]);
            }
        }

        """
        expect = "0\n0\n0\n0\n0\n5\n0\n0\n0\n0\n"
        self.assertTrue(TestCodeGen.test(input, expect, 557))
    
    def test_52(self):
        input = """
        
        func gcd(a int, b int) int {
            for b != 0 {
                temp := b;
                b := a % b;
                a := temp;
            }
            return a;
        }

        func main() {
            var a int = 56;
            var b int = 98;
            var result int = gcd(a, b);
            putIntLn(result);
        }
        """
        expect = "14\n"
        self.assertTrue(TestCodeGen.test(input, expect, 558))

    def test_53(self):
        input = """
        func isPrime(n int) boolean {
                if (n <= 1) {
                    return false;
                }
                for var i = 2; i * i <= n; i += 1 {
                    if (n % i == 0) {
                        return false;
                    }
                }
                return true;
            }

        func main() {
            var n int = 29;
            if (isPrime(n)) {
                putStringLn("Prime number")
            } else {
                putStringLn("Not a prime number")
            }
        }
        """
        expect = "Prime number\n"
        self.assertTrue(TestCodeGen.test(input, expect, 559))

    def test_54(self):
        input = """
            func calculateFactorial(n int) int {
                if (n <= 1) { return 1; }
                result := 1;
                for i := 2; i <= n; i += 1 {
                    result *= i;
                }
                return result;
            }

        func main() {
            var n int = 5;
            var factorial int = calculateFactorial(n);
            putIntLn(factorial);
        }
        """
        expect = "120\n"
        self.assertTrue(TestCodeGen.test(input, expect, 560))

    def test_55(self):
        input = """
            func bubbleSort(arr [7]int, n int) {
                swapped := true;
                for swapped {
                    swapped := false;
                    for i := 1; i < n; i += 1 {
                        if (arr[i-1] > arr[i]) {
                            temp := arr[i-1];
                            arr[i-1] := arr[i];
                            arr[i] := temp;
                            swapped := true;
                        }
                    }
                }
            }
            
            func main() {
                var arr [7]int = [7]int{64, 34, 25, 12, 22, 11, 90};
                var n int = 7;
                bubbleSort(arr, n);
                for i := 0; i < n; i += 1 {
                    putIntLn(arr[i]);
                }
            }
        """
        expect = "11\n12\n22\n25\n34\n64\n90\n"
        self.assertTrue(TestCodeGen.test(input, expect, 561))

    def test_56(self):
        input = """
        // full call stmt
        func power(base float, exponent int) float {
                if (exponent == 0) { return 1.0; }
                if (exponent < 0) {
                    base := 1.0 / base;
                    exponent := -exponent;
                }
                result := 1.0;
                for i := 0; i < exponent; i += 1 {
                    result *= base;
                }
                return result;
            }
            func main() {
                var base float = 2.5;
                var exponent int = 3;
                var result float = power(base, exponent);
                putFloatLn(result);
            }
        """
        expect = "15.625\n"
        self.assertTrue(TestCodeGen.test(input, expect, 562))

    # Short-circuit test
    def test_57(self):
        input = """
        func work() boolean {
            putStringLn("Short-circuit evaluation works!")
            return true
        }

        func notwork() boolean {
            putStringLn("Short-circuit evaluation doesn't work!")
            return false
        }

        func main() {
            var a int = 5
            var b int = 10
            if (work() || notwork()) {
                a := 2
            }
        }
        """
        expect = "Short-circuit evaluation works!\n"
        self.assertTrue(TestCodeGen.test(input, expect, 563))

    
    def test_58(self):
        input = """
        func work() boolean {
            putStringLn("Short-circuit evaluation works!")
            return true
        }

        func notwork() boolean {
            putStringLn("Short-circuit evaluation doesn't work!")
            return false
        }

        func main() {
            var a int = 5
            var b int = 10
            if (notwork() && work()) {
                a := 2
            }
        }
        """
        expect = "Short-circuit evaluation doesn't work!\n"
        self.assertTrue(TestCodeGen.test(input, expect, 564))

    # Built-in function tests
    def test_59(self):
        input = """
        func main() {
            putInt(123);
            putFloat(45.67);
            putString("Hello");
            putBool(true);
        }
        """
        expect = "12345.67Hellotrue"
        self.assertTrue(TestCodeGen.test(input, expect, 565))
    
    def test_60(self):
        input = """
        func main() {
            putIntLn(123);
            putFloatLn(45.67);
            putStringLn("Hello");
            putBoolLn(true);
            putLn();
        }
        """
        expect = "123\n45.67\nHello\ntrue\n\n"
        self.assertTrue(TestCodeGen.test(input, expect, 566))
    
    def test_61(self):
        input = """
        func main() {
            putIntLn(123 + 456);
            putFloatLn(45.67 * 2.0);
        }
        """
        expect = "579\n91.34\n"
        self.assertTrue(TestCodeGen.test(input, expect, 567))
    
    def test_62(self):
        input = """
        func main() {
            putString("Hello" + " " + "World");
            putLn();
            putBool(10 > 5 && 7 < 9);
        }
        """
        expect = "Hello World\ntrue"
        self.assertTrue(TestCodeGen.test(input, expect, 568))
    
    def test_63(self):
        input = """
        func calculate() int {
            putStringLn("Calculating...");
            return 42;
        }
        
        func main() {
            putIntLn(calculate());
            putString("Result: ");
            putInt(calculate() * 2);
        }
        """
        expect = "Calculating...\n42\nResult: Calculating...\n84"
        self.assertTrue(TestCodeGen.test(input, expect, 569))
    
    def test_64(self):
        input = """
        func main() {
            var a int = 10;
            var b float = 20.5;
            var c string = "Test";
            var d boolean = false;
            
            putInt(a);
            putLn();
            putFloat(b);
            putLn();
            putString(c);
            putLn();
            putBool(d);
        }
        """
        expect = "10\n20.5\nTest\nfalse"
        self.assertTrue(TestCodeGen.test(input, expect, 570))
    
    def test_65(self):
        input = """
        func main() {
            putIntLn(sum(10, 20, 30));
            putFloatLn(average(10.5, 20.5, 30.5));
        }
        
        func sum(a int, b int, c int) int {
            return a + b + c;
        }
        
        func average(a float, b float, c float) float {
            return (a + b + c) / 3.0;
        }
        """
        expect = "60\n20.5\n"
        self.assertTrue(TestCodeGen.test(input, expect, 571))
    
    def test_66(self):
        input = """
        func main() {
            var arr [5]int = [5]int{10, 20, 30, 40, 50};
            
            for i := 0; i < 5; i += 1 {
                putInt(arr[i]);
                if (i < 4) {
                    putString(", ");
                }
            }
            putLn();
            
            var total int = 0;
            for i := 0; i < 5; i += 1 {
                total += arr[i];
            }
            putString("Total: ");
            putInt(total);
        }
        """
        expect = "10, 20, 30, 40, 50\nTotal: 150"
        self.assertTrue(TestCodeGen.test(input, expect, 572))
    
    def test_67(self):
        input = """
        func main() {
            putStringLn("Nested functions:");
            
            putIntLn(outer(5));
        }
        
        func outer(x int) int {
            putString("  Outer: ");
            putIntLn(x);
            return inner(x * 2);
        }
        
        func inner(y int) int {
            putString("    Inner: ");
            putIntLn(y);
            return y * 2;
        }
        """
        expect = "Nested functions:\n  Outer: 5\n    Inner: 10\n20\n"
        self.assertTrue(TestCodeGen.test(input, expect, 573))
    
    def test_68(self):
        input = """
        func main() {
            putStringLn("Testing boolean conditions:");
            
            var a boolean = true;
            var b boolean = false;
            
            putString("a && b: ");
            putBoolLn(a && b);
            
            putString("a || b: ");
            putBoolLn(a || b);
            
            putString("!a: ");
            putBoolLn(!a);
            
            putString("!b: ");
            putBoolLn(!b);
        }
        """
        expect = "Testing boolean conditions:\na && b: false\na || b: true\n!a: false\n!b: true\n"
        self.assertTrue(TestCodeGen.test(input, expect, 574))

    def test_69(self):
        input = """
            var childSize = 2
            type Person struct {
                age int
                name string
                child [2]Children
            }

            type Children struct {
                age int
                name string
            }

            func (p Person) getChild() {
                putStringLn(p.name)
                putIntLn(p.age)
                for i := 0; i < childSize; i += 1 {
                    putStringLn(p.child[i].name)
                    putIntLn(p.child[i].age)
                }
            }

            func main() {
                var c [2]Children = [2]Children{Children{name: "Hugo", age: 5}, Children{name: "Jerry", age: 3}}
                var a Person = Person{name: "Tom", age: 21, child: c}
                a.getChild()
            }

        """
        expect = "Tom\n21\nHugo\n5\nJerry\n3\n"
        self.assertTrue(TestCodeGen.test(input, expect, 575))
    
    def test_70(self):
        input = """
            var childSize = 2
            type Person struct {
                age int
                name string
                child [2]Children
            }

            type Children struct {
                age int
                name string
            }

            func (p Person) getChild() {
                putStringLn(p.name)
                putIntLn(p.age)
                for i := 0; i < childSize; i += 1 {
                    putStringLn(p.child[i].name)
                    putIntLn(p.child[i].age)
                }
                p.child[0].name := "Changed"
                p.child[0].age := 10
                for i := 0; i < childSize; i += 1 {
                    putStringLn(p.child[i].name)
                    putIntLn(p.child[i].age)
                }
            }

            func main() {
                var c [2]Children = [2]Children{Children{name: "Hugo", age: 5}, Children{name: "Jerry", age: 3}}
                var a Person = Person{name: "Tom", age: 21, child: c}
                a.getChild()
            }

        """
        expect = "Tom\n21\nHugo\n5\nJerry\n3\nChanged\n10\nJerry\n3\n"
        self.assertTrue(TestCodeGen.test(input, expect, 576))

    def test_71(self):
        input = """
        func main(){
            foo(10)
        }
        func foo(n int){
            for var i = 1; i < n; i += 1 {
                putInt(i)
            }
            for i := 1; i < n; i += 1 {
                putInt(i)
            }
        }
        """
        expect = "123456789123456789"
        self.assertTrue(TestCodeGen.test(input, expect, 577))

    def test_72(self):
        input = """
        var arr[5]int = [5]int{1,2,3,4,5}
        func main(){
            for i := 0; i < 5; i += 1 {
                if (arr[i] % 2 == 0) {
                    putInt(arr[i])
                }
            }
            for var i = 0; i < 5; i += 1 {
                if (arr[i] % 2 != 0) {
                    putInt(arr[i])
                }
            }
        }
        """
        expect = "24135"
        self.assertTrue(TestCodeGen.test(input, expect, 578))

    def test_73(self):
        input = """
        const childSize = 2
            type Person struct {
                age int
                name string
                child [2]Children
            }

            type Children struct {
                age int
                name string
            }

            func (p Person) getChild() {
                putStringLn(p.name)
                putIntLn(p.age)
                for i := 0; i < childSize; i += 1 {
                    p.child[i].getChild()
                }
                p.child[0].name := "Changed"
                p.child[0].age := 10
                for i := 0; i < childSize; i += 1 {
                    putStringLn(p.child[i].name)
                    putIntLn(p.child[i].age)
                }
            }

            func (children Children) getChild() {
                putStringLn(children.name)
                putIntLn(children.age)
            }

            func main() {
                var c [2]Children = [2]Children{Children{name: "Hugo", age: 5}, Children{name: "Jerry", age: 3}}
                var a Person = Person{name: "Tom", age: 21, child: c}
                a.getChild()
            }

        """
        expect = "Tom\n21\nHugo\n5\nJerry\n3\nChanged\n10\nJerry\n3\n"
        self.assertTrue(TestCodeGen.test(input, expect, 579))

    def test_74(self):
        input = """
        func fibonacci(n int) int {
            if (n <= 1) {
                return n;
            }
            return fibonacci(n-1) + fibonacci(n-2);
        }

        func main() {
            putIntLn(fibonacci(10));
        }
        """
        expect = "55\n"
        self.assertTrue(TestCodeGen.test(input, expect, 580))
    
    def test_75(self):
        input = """
        func main() {
            var arr [5]int = [5]int{10, 20, 30, 40, 50};
            var index int = 2;
            putIntLn(arr[index + 1]);
            putIntLn(arr[index * 2 - 2]);
        }
        """
        expect = "40\n30\n"
        self.assertTrue(TestCodeGen.test(input, expect, 581))
    
    def test_76(self):
        input = """
        type Calculator struct {
            value int;
        }
        
        func (c Calculator) add(x int) Calculator {
            c.value += x;
            return c;
        }
        
        func (c Calculator) multiply(x int) Calculator {
            c.value *= x;
            return c;
        }
        
        func (c Calculator) getValue() int {
            return c.value;
        }
        
        func main() {
            var calc Calculator = Calculator{value: 5};
            putIntLn(calc.add(10).multiply(2).getValue());
        }
        """
        expect = "30\n"
        self.assertTrue(TestCodeGen.test(input, expect, 582))
    
    def test_77(self):
        input = """
        type Car struct {
            brand string;
            model string;
            year int;
            features [2]string;
        }
        
        func main() {
            var myCar Car = Car{brand: "Toyota", model: "Camry", year: 2023, features: [2]string{"GPS", "Bluetooth"}};
            
            putStringLn(myCar.brand);
            putStringLn(myCar.model);
            putIntLn(myCar.year);
            putStringLn(myCar.features[0] + ", " + myCar.features[1]);
        }
        """
        expect = "Toyota\nCamry\n2023\nGPS, Bluetooth\n"
        self.assertTrue(TestCodeGen.test(input, expect, 583))
    
    def test_78(self):
        input = """
        func factorial(n int) int {
            if (n <= 1) {
                return 1;
            }
            return n * factorial(n-1);
        }
        
        func main() {
            putIntLn(factorial(5));
        }
        """
        expect = "120\n"
        self.assertTrue(TestCodeGen.test(input, expect, 584))
    
    def test_79(self):
        input = """
        func main() {
            var i int = 0;
            var j int = 0;
            
            for i < 3 {
                for j < 3 {
                    putInt(i * 3 + j + 1);
                    putString(" ");
                    j += 1;
                    if (j == 2) {
                        break;
                    }
                }
                putStringLn("");
                j := 0;
                i += 1;
                if (i == 2) {
                    break;
                }
            }
        }
        """
        expect = "1 2 \n4 5 \n"
        self.assertTrue(TestCodeGen.test(input, expect, 585))
    
    def test_80(self):
        input = """
        func main() {
            var a boolean = true;
            var b boolean = false;
            var c boolean = true;
            
            putBoolLn(a && b || c);
            putBoolLn(!a || b && c);
            putBoolLn((a || b) && (b || c));
        }
        """
        expect = "true\nfalse\ntrue\n"
        self.assertTrue(TestCodeGen.test(input, expect, 586))
    
    def test_81(self):
        input = """
        func main() {
            var str1 string = "Hello";
            var str2 string = "World";
            var str3 string = str1 + " " + str2;
            
            putStringLn(str3);
            putBoolLn(str1 > str2);
            putBoolLn("abc" == "abc");
        }
        """
        expect = "Hello World\nfalse\ntrue\n"
        self.assertTrue(TestCodeGen.test(input, expect, 587))
    
    def test_82(self):
        input = """
        func main() {
            var matrix [3][3]int = [3][3]int{{1, 2, 3}, {4, 5, 6}, {7, 8, 9}}
            
            // Calculate sum of diagonals
            var mainDiag int = 0;
            var antiDiag int = 0;
            
            for i := 0; i < 3; i += 1 {
                mainDiag += matrix[i][i];
                antiDiag += matrix[i][2-i];
            }
            
            putStringLn("Main diagonal sum:");
            putIntLn(mainDiag);
            putStringLn("Anti-diagonal sum:");
            putIntLn(antiDiag);
        }
        """
        expect = "Main diagonal sum:\n15\nAnti-diagonal sum:\n15\n"
        self.assertTrue(TestCodeGen.test(input, expect, 588))
    
    def test_83(self):
        input = """
        type Shape interface {
            area() float;
            perimeter() float;
        }
        
        type Rectangle struct {
            width float;
            height float;
        }
        
        type Circle struct {
            radius float;
        }
        
        func (r Rectangle) area() float {
            return r.width * r.height;
        }
        
        func (r Rectangle) perimeter() float {
            return 2 * (r.width + r.height);
        }
        
        func (c Circle) area() float {
            return 3.14 * c.radius * c.radius;
        }
        
        func (c Circle) perimeter() float {
            return 2 * 3.14 * c.radius;
        }
        
        func printShapeInfo(s Shape) {
            putFloatLn(s.area());
            putFloatLn(s.perimeter());
        }
        
        func main() {
            var r Shape = Rectangle{width: 5.0, height: 3.0};
            var c Shape = Circle{radius: 2.0};
            
            putStringLn("Rectangle:");
            printShapeInfo(r);
            
            putStringLn("Circle:");
            printShapeInfo(c);
        }
        """
        expect = "Rectangle:\n15.0\n16.0\nCircle:\n12.56\n12.56\n"
        self.assertTrue(TestCodeGen.test(input, expect, 589))
    
    def test_84(self):
        input = """
        func main() {
            var arr [3]int = [3]int{10, 20, 30};
            
            // Use array literal in an expression
            var sum int = arr[0] + arr[1] + arr[2] + [3]int{1, 2, 3}[0] + [3]int{4, 5, 6}[1];
            
            putIntLn(sum);
        }
        """
        expect = "66\n"
        self.assertTrue(TestCodeGen.test(input, expect, 590))
    
    def test_85(self):
        input = """
        func main() {
            var a int = 5;
            var b float = 2.5;
            var c float = a * b + a / 2;
            
            putFloatLn(c);
            
            var d float = a * b - 3;
            putFloatLn(d);
        }
        """
        expect = "14.5\n9.5\n"
        self.assertTrue(TestCodeGen.test(input, expect, 591))
    
    def test_86(self):
        input = """
        
        func main() {
            putStringLn("Name: " + "Alice")
            putStringLn("Encoded age: " + "300")
        }
        """
        expect = "Name: Alice\nEncoded age: 300\n"
        self.assertTrue(TestCodeGen.test(input, expect, 592))
    
    def test_87(self):
        input = """
        type Outr struct {
            name string
            innr Innr
        }

        type Innr struct{
            name string
            age int
        }

        func main() {
            var obj Outr = Outr{name: "Hello", innr: Innr{name: "Bro", age: 21}}
            putStringLn(obj.name)
            
            putStringLn(obj.innr.name)
        }

        """
        expect = "Hello\nBro\n"
        self.assertTrue(TestCodeGen.test(input, expect, 593))
    
    def test_88(self):
        input = """
        type Employee struct {
            name string;
            id int;
        }
        
        func main() {
            var employees [3]Employee = [3]Employee{Employee{name: "Alice", id: 101},Employee{name: "Bob", id: 102},Employee{name: "Charlie", id: 103}};
            
            for i := 0; i < 3; i += 1 {
                putStringLn("Employee " + employees[i].name + " has ID: ");
                putIntLn(employees[i].id);
            }
        }
        """
        expect = "Employee Alice has ID: \n101\nEmployee Bob has ID: \n102\nEmployee Charlie has ID: \n103\n"
        self.assertTrue(TestCodeGen.test(input, expect, 594))
    
    def test_89(self):
        input = """
        func main() {
            
                var x int = 10;
                putIntLn(x)
                    x := 20;
                        x := 30;
                        putIntLn(x);
                    putIntLn(x)
                putIntLn(x);
            
        }
        """
        expect = "10\n30\n30\n30\n"
        self.assertTrue(TestCodeGen.test(input, expect, 595))
    
    def test_90(self):
        input = """
        func main() {
            var a int = 5;
            var b int = 10;
            var c int = 15;
            
            c /= 3
            b *= c
            a += b
            
            putIntLn(a);
            putIntLn(b);
            putIntLn(c);
        }
        """
        expect = "55\n50\n5\n"
        self.assertTrue(TestCodeGen.test(input, expect, 596))
    
    def test_91(self):
        input = """
        type Adder interface {
            add(a int, b int) int;
        }
        
        type Calculator struct {
            name string;
            age int
        }
        
        func (c Calculator) add(a, b int) int {
            return a + b;
        }
        
        func main() {
            var c Calculator = Calculator{name: "MyCalc"};
            var a Adder = c;
            
            putIntLn(a.add(10, 20));
            putStringLn(c.name);
        }
        """
        expect = "30\nMyCalc\n"
        self.assertTrue(TestCodeGen.test(input, expect, 597))
    
    def test_92(self):
        input = """
        func selectionSort(arr [10]int) [10]int {
            for i := 0; i < 10 - 1; i += 1 {
                minIdx := i;
                for j := i + 1; j < 10; j += 1 {
                    if (arr[j] < arr[minIdx]) {
                        minIdx := j;
                    }
                }
                
                if (minIdx != i) {
                    temp := arr[i];
                    arr[i] := arr[minIdx];
                    arr[minIdx] := temp;
                }
            }
            return arr;
        }
        
        func main() {
            var numbers [10]int = [10]int{9, 3, 5, 1, 8, 2, 4, 7, 6, 0};
            var sorted [10]int = selectionSort(numbers);
            
            for i := 0; i < 10; i += 1 {
                putInt(sorted[i]);
                putString(" ");
            }
        }
        """
        expect = "0 1 2 3 4 5 6 7 8 9 "
        self.assertTrue(TestCodeGen.test(input, expect, 598))
    
    def test_93(self):
        input = """
        func isPalindrome(str string) boolean {
            var len int = length(str);
            for i := 0; i < len / 2; i += 1 {
                if (charAt(str, i) != charAt(str, len - i - 1)) {
                    return false;
                }
            }
            return true;
        }
        
        func length(str string) int {
            return 5; // Assuming "radar" or "hello" has 5 chars
        }
        
        func charAt(str string, idx int) string {
            if (str == "radar") {
                var chars = [5]string{"r", "a", "d", "a", "r"};
                return chars[idx];
            } else {
                var chars = [5]string{"h", "e", "l", "l", "o"};
                return chars[idx];
            }
            return ""
        }
        
        func main() {
            putStringLn("Is 'radar' a palindrome?");
            putBoolLn(isPalindrome("radar"));
            
            putStringLn("Is 'hello' a palindrome?");
            putBoolLn(isPalindrome("hello"));
        }
        """
        expect = "Is 'radar' a palindrome?\ntrue\nIs 'hello' a palindrome?\nfalse\n"
        self.assertTrue(TestCodeGen.test(input, expect, 599))
    
    def test_94(self):
        input = """
        type Queue struct {
            items [5]int;
            front int;
            rear int;
        }
        
        func (q Queue) initialize() Queue {
            q.front := 0;
            q.rear := -1;
            q.items := [5]int{0, 0, 0, 0, 0}
            return q;
        }
        
        func (q Queue) enqueue(item int) Queue {
            if (q.rear < 4) {
                q.rear += 1;
                q.items[q.rear] := item;
            }
            return q;
        }
        
        func (q Queue) dequeue() int {
            if (q.front <= q.rear) {
                item := q.items[q.front];
                q.front += 1;
                return item;
            }
            return -1;
        }
        
        func (q Queue) display() {
            for i := q.front; i <= q.rear; i += 1 {
                putIntLn(q.items[i]);
            }
        }
        
        func main() {
            var queue Queue;
            queue := queue.initialize();
            
            queue := queue.enqueue(10);
            queue := queue.enqueue(20);
            queue := queue.enqueue(30);
            
            putStringLn("Queue items:");
            queue.display();
            
            putStringLn("Dequeued item:");
            putIntLn(queue.dequeue());
            
            putStringLn("Queue after dequeue:");
            queue.display();
        }
        """
        expect = "Queue items:\n10\n20\n30\nDequeued item:\n10\nQueue after dequeue:\n20\n30\n"
        self.assertTrue(TestCodeGen.test(input, expect, 600))

    def test_95(self):
        input = """
type Speaker interface { speak(); }

type Human struct { name int; }

func (h Human) speak() { putIntLn(h.name); }

func main() {
    var people [3]Speaker;
    var a = 1
    var b = 2

    people[0] := Human {name: 1};
    people[b - a] := Human {name: 2};
    people[2] := Human {name: 3};

    people[0].speak(); // Output: 1
    people[1].speak(); // Output: 2
    people[2].speak(); // Output: 3
}
        """
        expect = "1\n2\n3\n"
        self.assertTrue(TestCodeGen.test(input, expect, 601))

    def test_96(self):
        input = """
        func main() {
        
            var a [2][2]float = [2][2]float{{1.2, 2.3}, {2.5, 3.6}}
            a[0][1] := 5.6
            putFloatLn(a[0][1])
        }
        
        """
        expect = "5.6\n"
        self.assertTrue(TestCodeGen.test(input, expect, 602))




