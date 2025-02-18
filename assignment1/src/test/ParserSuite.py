import unittest
from TestUtils import TestParser

class ParserSuite(unittest.TestCase):
    def test_simple_program(self):
        """Simple program: void main() {} """
        input = """var Tam = 1 && 2 && c + 3 / 2 - -1;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,201))

    def test_more_complex_program(self):
        """More complex program"""
        input = """func foo () {
        }"""
        expect = "Error on line 2 col 9: }"
        self.assertTrue(TestParser.checkParser(input,expect,202))
    
    def test_wrong_miss_close(self):
        """Miss ) void main( {}"""
        input = """func foo({};"""
        expect = "Error on line 1 col 10: {"
        self.assertTrue(TestParser.checkParser(input,expect,203))

    def test_wrong_variable(self):
        input = """var float;"""
        expect = "Error on line 1 col 5: float"
        self.assertTrue(TestParser.checkParser(input,expect,204))

    def test_wrong_index(self):
        input = """var a ;"""
        expect = "Error on line 1 col 7: ;"
        self.assertTrue(TestParser.checkParser(input,expect,205))
    def test_const_decl(self):
        input = """const k = -b - !-!c - ---[2]int{2, 3, 4};  """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,206))
    def test_block_stmt(self):
        input = """
                                        break;
                                    func Add() {
                                    }"""
        expect = "Error on line 2 col 41: break"
        self.assertTrue(TestParser.checkParser(input,expect,207))
    def test_method_decl(self):
        input = """func (c c) Add(x, c int) {
            var a int;
        }
         
            """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,208))
    def test_expr(self):
        input = """var x Person = a[]"""
        expect = "Error on line 1 col 18: ]"
        self.assertTrue(TestParser.checkParser(input,expect,209))
    def test_interface_declaration_success(self):
        input = """
        type Calculator interface {
            Add(x, y int) int;
            Subtract(a int, b, c int) string
            SayHello(name string)
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 210))
    def test_interface_missing_brace(self):
        input = """
        type Calculator interface {
            Add(x, y int) int;
            Subtract(a, b float, c int) float;
            Reset()
            SayHello(name string);
        """
        expect = "Error on line 7 col 9: <EOF>"
        self.assertTrue(TestParser.checkParser(input, expect, 211))
    def test_interface_missing_method_semicolon(self):
        input = """
        type Calculator interface {
            Add(x, y int) int Subtract(a, b float, c int) float;
            Reset();
        }
        """
        expect = "Error on line 3 col 31: Subtract"
        self.assertTrue(TestParser.checkParser(input, expect, 212))
    def test_interface_empty(self):
        input = """
        type Empty interface {
        }
        """
        expect = "Error on line 3 col 9: }"
        self.assertTrue(TestParser.checkParser(input, expect, 213))
    def test_interface_method_with_no_parameters(self):
        input = """
        type Test interface {
            DoSomething()
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 214))
    def test_interface_invalid_method_syntax(self):
        input = """
        type Invalid interface {
            Compute int (x, y);
        }
        """
        expect = "Error on line 3 col 21: int"
        self.assertTrue(TestParser.checkParser(input, expect, 215))
    def test_interface_wrong_keyword(self):
        input = """
        struct Calculator interface {
            Add(x, y int) int;
        }
        """
        expect = "Error on line 2 col 9: struct"
        self.assertTrue(TestParser.checkParser(input, expect, 216))
    def test_struct(self):
        input = """
        type Person struct {
            name string;
            age int;
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 217))
    def test_struct_with_method_inside_wrong(self):
        input = """
        type Person struct {
            name string;
            age int;
            func SayHello() {
            }
        }
        """
        expect = "Error on line 5 col 13: func"
        self.assertTrue(TestParser.checkParser(input, expect, 218))
    def test_struct_with_method_inside(self):
        input = """
        type Person struct {
            name string;
            age int;
        }
        func (p Person) SayHello() {
            var a int;
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 219))
    def test_interface_without_interface_keyword(self):
        input = """
        type Wrong {
            Add(x, y int) int;
        }
        """
        expect = "Error on line 2 col 20: {"
        self.assertTrue(TestParser.checkParser(input, expect, 220))

    def test_var_decl_221(self):
        input = """var x int = 10;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 221))

    def test_var_decl_222(self):
        input = """var y = "Hello";"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 222))

    def test_var_decl_223(self):
        input = """var z string;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 223))

    def test_var_decl_224(self):
        input = """    
            const k = ID {a : 2}.c[2] + 2[2] + false.foo() + (1).foo();                         
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 224))

    def test_var_decl_225(self):
        input = """var c, d int;"""
        expect = "Error on line 1 col 6: ,"
        self.assertTrue(TestParser.checkParser(input, expect, 225))

    def test_var_decl_multiple(self):
        input = """var e string = "Test"; var f = 123;"""  # Multiple declarations
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 226))

    def test_var_decl_227(self):
        input = """var int;"""  # Invalid variable name
        expect = "Error on line 1 col 5: int"  # Example error message
        self.assertTrue(TestParser.checkParser(input, expect, 227))

    # Constant Declarations
    def test_const_decl_228(self):
        input = """const round = 3.1423242345e-10;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 228))

    def test_const_decl_229(self):
        input = """const Greeting = "Hello, MiniGo!";"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 229))

    def test_const_decl_230(self):
        input = """const MaxSize = 100 + 50;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 230))

    def test_const_decl_231(self):
        input = """const x int = 5.a + b[1].c;"""
        expect = "Error on line 1 col 9: int"
        self.assertTrue(TestParser.checkParser(input, expect, 231))

    def test_const_decl_232(self):
        input = """const x = 5.a + b[1].c.d()[3];"""
        expect = "Error on line 1 col 13: a"
        self.assertTrue(TestParser.checkParser(input, expect, 232))

    def test_const_decl_233(self):
        input = """const z;""" # Missing initialization
        expect = "Error on line 1 col 8: ;" # Example error message
        self.assertTrue(TestParser.checkParser(input, expect, 233))

    # Expressions
    def test_expression_234(self):
        input = """var result int = 10 + 5 * 2;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 234))

    def test_expression_235(self):
        input = """var flag bool = !true && false * !-!-1 + a(1, 2)[3].c[2].a.d(1)[3][4];"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 235))

    def test_expression_236(self):
        input = """func main() {
        1 + 1 += 2;
        }"""
        expect = "Error on line 2 col 9: 1"
        self.assertTrue(TestParser.checkParser(input, expect, 236))

    def test_expression_237(self):
        input = """var a = 10 % 3 * a().abn.Person{Id: test}.Id[3].d(2, 3);"""
        expect = "Error on line 1 col 32: {"
        self.assertTrue(TestParser.checkParser(input, expect, 237))

    def test_expression_238(self):
        input = """var a = 10 % 3 * Person{Id: test}.Id[3].d(2, 3)[4].d.e.f();"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 238))

    def test_expression_239(self):
        input = """
        func main() {
        c += 2
        }
"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 239))

    def test_expression_240(self):
        input = """var d int = func(1, 2, 3).d[4];""" # Parentheses
        expect = "Error on line 1 col 13: func"
        self.assertTrue(TestParser.checkParser(input, expect, 240))

    def test_array(self):
        input = """var a = b[1];"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 241))
    
    def test_array_242(self):
        input = """
        func main() {
        a[1] := b[1][2];
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 242))
    
    def test_array_243(self):
        input = """var a = [1][2][3]int{1,{2,3,4},{Person{Id: name}, 3, {a, b}}};"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 243))

    def test_array_literal_244(self):
        input = """var arr2 = [2]float{"a", "b"};"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 244))

    def test_array_literal_245(self):
        input = """var arr3 := [3]int{1, 2};""" # Fewer elements than array size
        expect = "Error on line 1 col 10: :="
        self.assertTrue(TestParser.checkParser(input, expect, 245))
    
    def test_array_literal_wrong_index(self):
        input = """var arr4 = [true]int{1, 2, 3}[1];"""
        expect = "Error on line 1 col 13: true"
        self.assertTrue(TestParser.checkParser(input, expect, 246))
    
    def test_array_literal_wrong_literal(self):
        input = """var arr5 = [5]int{1 + 1, 2, 3, 4, 5};"""
        expect = "Error on line 1 col 21: +"
        self.assertTrue(TestParser.checkParser(input, expect, 247))

    def test_array_literal_wrong_literal2(self):
        input = """var arr5 = [5]int{1, 2, {}, 3, 4, 5};"""
        expect = "Error on line 1 col 26: }"
        self.assertTrue(TestParser.checkParser(input, expect, 248))
    
    def test_array_literal_wrong_literal3(self):
        input = """var arr5 = [5]int{2, {1, 2, 3, {a + b}} 3, 4, 5};"""
        expect = "Error on line 1 col 35: +"
        self.assertTrue(TestParser.checkParser(input, expect, 249))
    
    def test_array_literal_wrong_literal4(self):
        input = """func add() {
        a[1].b() -= [5]int{1, 2, 3, 4, 5};
        }"""
        expect = "Error on line 2 col 18: -="
        self.assertTrue(TestParser.checkParser(input, expect, 250))
    
    # Struct Literals
    def test_struct_literal_251(self):
        input = """
    func main() {
    p := Person{name: "Alice", age: 30};
    }
"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 251))

    def test_struct_literal_252(self):
        input = """
func main() {
q := Person{};
}
"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 252))

    def test_struct_literal_253(self):
        input = """var r = Point{x: 10, y: 20, z: 30};""" # Assuming Point struct
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 253))

    def test_struct_literal_254(self):
        input = """var s = Person{name: "Bob"};""" # Partial initialization
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 254))
    
    def test_struct_literal_255(self):
        input = """var t Person = Person{name: "Bob"; age: 30, address: "Hanoi"};"""
        expect = "Error on line 1 col 34: ;"
        self.assertTrue(TestParser.checkParser(input, expect, 255))
    
     # Function Calls
    def test_function_call_256(self):
        input = """func Add() {add(3, 4)
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 256))

    def test_function_call_257(self):
        input = """func Add() {
        reset()
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 257))

    def test_function_call_258(self):
        input = """func Add() {print("Hello");}
        """ # Assuming print function exists
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 258))

    def test_function_call_259(self):
        input = """var result = add(5, 7);""" 
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 259))

    def test_function_call_260(self):
        input = """var result = add(5 + 5, 7 * (1 + -!2), Person{ID: name});"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 260))

    def test_function_call_261(self):
        input = """var result = add(5, 7, 9"""
        expect = "Error on line 1 col 25: <EOF>"
        self.assertTrue(TestParser.checkParser(input, expect, 261))

    def test_function_call_262(self):
        input = """var result = a.add(5, 7, b(), c.a(1,2,3), a[1].c(2));"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 262))

    def test_function_call_263(self):
        input = """var result = add.(5, 7, 9);"""
        expect = "Error on line 1 col 18: ("
        self.assertTrue(TestParser.checkParser(input, expect, 263))

     # Mixed/Complex Cases
    def test_complex_264(self):
        input = """
        const MAX_VALUE = 100;
        var counter int = 0;

        func increment() int {
            counter += 1;
            return counter;
        }

        var result int = increment() + MAX_VALUE;
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 264))

    def test_complex_265(self):
        input = """
        type Point struct {
            x int;
            y int;
        }

        func main() {
            var p Point = Point{x: 5, y: 10};
        p.x += 5;

        var area int = p.x * p.y;
        }
        
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 265))

    def test_complex_266(self):
        input = """
        
            type Calculator interface {
            Add(x int) int;
        }

        type MyCalc struct {
            value int;
        }

        func (c MyCalc) Add(x int) int {
            c.value += x;
            return c.value;

        var calc Calculator = MyCalc{value: 0};
        calc.Add(5);
        }
        
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 266))

    def test_complex_267(self):
       input = """
       var arr = [3]int{1, 2, 3};
       var sum int = arr[0] + arr[1] + arr[2];
       """
       expect = "successful"
       self.assertTrue(TestParser.checkParser(input, expect, 267))

    def test_complex_268(self):
        input = """
        type Person struct {
            name string;
            age int;
        }

        func main() {
        var people [2]Person;
        people[0] := Person{name: "Alice", age: 30};
        people[1] := Person{name: "Bob", age: 25};

        var aliceAge int = people[0].age;
        }
        
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 268))


    def test_complex_269(self):
        input = """
        func multiply(x int, y int) int {
            return x * y;
        }

        const FACTOR = 2;
        var result int = multiply(5, 10) * FACTOR;
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 269))

    def test_complex_270(self):
        input = """
        type Rectangle struct {
            width int;
            height int;
        }

        func (r Rectangle) area() int {
            return r.width * r.height;
        }

        var rect Rectangle = Rectangle{width: 10, height: 5};
        var rectArea int = rect.area();
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 270))

    def test_complex_271(self):
        input = """
        type Circle struct {
            radius float;
        }

        func (c Circle) circumference() float {
            const PI = 3.14159;
            return 2 * PI * c.radius;
        }

        var myCircle Circle = Circle{radius: 7.0};
        var c float = myCircle.circumference();
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 271))

    def test_complex_272(self):
        input = """
        
            type Point struct {
            x int;
            y int;
        }
        
        func (p Point) move(dx int, dy int) {
            p.x := p.x + dx;
            p.y := p.y + dy;
        }

        func Add() {
        var myPoint Point = Point{x: 2, y: 3};
        myPoint.move(5, -2);
        }
        
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 272))

    def test_complex_273(self):
        input = """
        type Person struct {
            name string;
            age int;
        }

        func (p Person) greet() string {
            return "Hello, my name is " + p.name + " and I am " + toString(p.age) + " years old.";
        }

        var someone Person = Person{name: "Charlie", age: 42};
        var greeting string = someone.greet();
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 273))

    def test_complex_274(self):
        input = """
        type Rectangle struct {
            width int;
            height int;
        }

        func (r Rectangle) scale(factor int) {
            r.width := r.width * factor;
            r.height := r.height * factor;
        }

        var rect Rectangle = Rectangle{width: 4, height: 6};
        rect.scale(2);
        """
        expect = "Error on line 13 col 9: rect"
        self.assertTrue(TestParser.checkParser(input, expect, 274))

    def test_complex_275(self):
        input = """
        type Car struct {
            make string;
            model string;
            year int;
        }

        func (c Car) description() string {
            return string(c.year) + " " + c.make + " " + c.model;
        }

        var myCar Car = Car{make: "Toyota", model: "Camry", year: 2023};
        var carDesc string = myCar.description();
        """
        expect = "Error on line 9 col 20: string"
        self.assertTrue(TestParser.checkParser(input, expect, 275))
    
    # If Statements (10 tests)
    def test_if_276(self):
        input = """func Add() {
            if (x > 10) { 
        x -= 5; 
        }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 276))

    def test_if_else_277(self):
        input = """func Add() {if (y == 0) { 
        y := 1 
        } else { 
            y *= 2 
        }
        };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 277))

    def test_if_elseif_else_278(self):
        input = """func Add() {
        if (z < 0) { z := -z; } else if (z > 0) { 
        z += 1 
        } else { 
        z := 0 
        }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 278))

    def test_nested_if_279(self):
        input = """func Add() {
        if (a > 5) { 
            if (a < 10) { a := a * 2; }
          };
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 279))

    def test_if_with_complex_condition_280(self):
        input = """func Add() {
            if (b > 0 && b < 10 || b == 15) { b := b / 2; };
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 280))

    def test_if_no_braces_281(self):  # Should be an error
        input = """func Add() {
            if (c > 0) c = c + 1;
        }"""
        expect = "Error on line 2 col 24: c"  # Example error
        self.assertTrue(TestParser.checkParser(input, expect, 281))

    def test_if_wrong_condition_282(self):
        input = """func Add() {
        if (d) { d := 0; }
        }""" 
        expect = "Error on line 3 col 10: <EOF>"  # Example error
        self.assertTrue(TestParser.checkParser(input, expect, 282))

    def test_if_empty_block_283(self):
        input = """func Add() {if (e == 1) {} else {}};"""
        expect = "Error on line 1 col 26: }"
        self.assertTrue(TestParser.checkParser(input, expect, 283))

    def test_if_with_array_access_284(self):
        input = """
        func Add() {
        if (arr[0] > 0) { 
        arr[0] := arr[0] * 2; 
        }
        else {
            arr[0] := 0;
        }
        }
"""
        expect = "Error on line 6 col 9: else"
        self.assertTrue(TestParser.checkParser(input, expect, 284))

    def test_if_with_struct_access_285(self):
        input = """
        func Add() {
            if (person.age > 18) {
          person.isAdult := true; 
          };
        }
"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 285))

    # For Statements (10 tests)
    def test_for_basic_286(self):
        input = """
            func Add() {
            for i < 10 { 
        }
}
        """
        expect = "Error on line 4 col 9: }"
        self.assertTrue(TestParser.checkParser(input, expect, 286))

    def test_for_init_cond_update_287(self):
        input = """
    func Add() {
    for i := 0; i < 10; i += 1 {  
        var x int = i * 2;
        }
    }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 287))

    def test_for_range_288(self):
        input = """var arr = [3]int{1, 2, 3}; 
        func Add() {
        for index, value := range arr { 
         x := x + value;
           }
        }
           """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 288))

    def test_for_range_no_index_289(self):
        input = """var arr = [3]int{1, 2, 3}; 
        func Add() {
        for _, value := range arr { 
            x += value;
           };
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 289))

    def test_for_break_290(self):
        input = """func Add() {for i := 0; i < 10; i += 1 { if (i == 5) { break; }; };};"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 290))

    def test_for_continue_291(self):
        input = """
                                    func Add() {
                                        for var i [2]int = 0; foo().a.b(); i[3] := 1 {
                                            return; 
                                        }
                                    };"""
        expect = "Error on line 3 col 77: ["
        self.assertTrue(TestParser.checkParser(input, expect, 291))

    def test_for_nested_292(self):
        input = """
                                    func Add() {
                                        for var i [2]int = 0; foo().a.b();  {
                                            return; 
                                        }
                                    };"""
        expect = "Error on line 3 col 77: {"
        self.assertTrue(TestParser.checkParser(input, expect, 292))

    def test_for_empty_body_293(self):
        input = """
        func Add() {
            for index, value := range arr[2] {
            for i := 0; i < 10; i += 1 {
                x := 2;
            }
                                        };
        }
"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 293))

    def test_for_missing_semicolon_294(self):  # Should be an error
        input = """
        func Add() {
            for i := 0 i < 10 i+=1 {}
        }
        """
        expect = "Error on line 3 col 24: i"  # Example error
        self.assertTrue(TestParser.checkParser(input, expect, 294))

    def test_for_range_wrong_type_295(self): # Should be an error
        input = """
        func Add() {
            for i, v := range 10 {}
        }
""" # Not an array
        expect = "Error on line 3 col 35: }" # Example error
        self.assertTrue(TestParser.checkParser(input, expect, 295))


    # Mixed/Complex Cases (5 tests)
    def test_mixed_296(self):
        input = """
        var x int = 0;
        func tmp() {
        if (x < 10) {
            for i := 0; i < 5; i += 1 {
                x := x + 1;
            }
        }
        }
        
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 296))

    def test_mixed_297(self):
        input = """
        var arr = [3]int{1, 2, 3};
        func tmp() {
            for _, value := range arr {
            if (value > 1) {
                value := value * 2;
            }
        }
        }
        
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 297))

    def test_mixed_298(self):
        input = """
        type Person struct {
            name string;
            age int;
        }

        func (c Person) SayHello() {
                fmt.Println("Hello, my name is " + c.name);
            }

        var p Person = Person{name: "Alice", age: 25};
        func tmp() {
        if (p.age > 18) {
            for i := 0; i < p.age; i += 1 {
                // Some action
                counter := counter + 1;
            }
        }
        }
        
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 298))

    def test_mixed_299(self):
        input = """
                                    func Add() {
                                        1 + 1 += 2;       
                                    }"""
        expect = "Error on line 3 col 41: 1"
        self.assertTrue(TestParser.checkParser(input, expect, 299))

    def test_mixed_300(self):
        input = """
        type Point struct {
            x int;
            y int;
        }

        var p Point = Point{x: 5, y: 10};
        func tmp() {
            for i := 0; i < p.x; i += 1 {
            p.y := p.y + 1;
            const a = [1]int{{1, 0x1}, ID{}, 1.2, "s", true, false, nil} + nil                    
        }
        
        }
        
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 300))

    def test_301(self): 
        input = """
        const TEST = 10;
        var arr [5]int;
        var a2 [TEST]string;
        
        func main() {
            arr := [TEST]int{1, 2, 3}
            arr[a+b-c*(11%11+0o111||(d&&(!c)))] /= 23;
        }
        
        """
        expect = """successful"""
        self.assertTrue(TestParser.checkParser(input,expect,301))
    
    