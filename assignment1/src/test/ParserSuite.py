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

    def test_302(self):
        input = """
            const a = !-!-!-1 + Person{Id: name}.c[3].d().a[2];
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 302))

    def test_303(self):
        input = """
            type Rectangle struct {
                length float;
                width float;
                color string;
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 303))

    def test_304(self):
        input = """
            var matrix = [3][3]int{
                {1, 2, 3},
                {4, 5, 6},
                {7, 8, 9}
            };
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 304))

    def test_305(self):
        input = """
            func (rect Rectangle) area() float {
                return rect.length * rect.width;
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 305))

    def test_306(self):
        input = """
            type Shape interface {
                getArea() float;
                getPerimeter() float;
                scale(factor float)
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 306))

    def test_307(self):
        input = """
            func main() {
                for i := 0; i < 10; i += 1 {
                    if (i % 2 == 0) {
                        putIntLn(i);
                    }
                }
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 307))

    def test_308(self):
        input = """
            var colors = [3]string{"red", "green", "blue"};
            const MAX_SIZE = 100;
            var grid = [MAX_SIZE][MAX_SIZE]int;
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 308))

    def test_309(self):
        input = """
            type Person struct {
                name string;
                age int;
                address string;
                contacts [5]string;
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 309))

    def test_310(self):
        input = """
            func fibonacci(n int) int {
                if (n <= 1) {
                    return n;
                }
                return fibonacci(n - 1) + fibonacci(n - 2);
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 310))

    def test_311(self):
        input = """
            type Stack interface {
                push(value int);
                pop() int;
                isEmpty() boolean;
                size() int
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 311))

    def test_312(self):
        input = """
            func processArray(arr [10]int) {
                for i := 0; i < 10; i += 1 {
                    arr[i] := arr[i] * 2;
                }
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 312))

    def test_313(self):
        input = """
            const PI = 3.14159;
            const E = 2.71828;
            const GOLDEN_RATIO = 1.61803;
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 313))

    def test_314(self):
        input = """
            type Complex struct {
                real float;
                imag float;
            }

            func (c Complex) magnitude() float {
                return c.real * c.real + c.imag * c.imag;
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 314))

    def test_315(self):
        input = """
            func main() {
                for _, value := range numbers {
                    if (value < 0) {
                        continue;
                    }
                    putIntLn(value);
                }
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 315))

    def test_316(self):
        input = """
            var matrix3D = [2][3][4]float{{{1.1, 1.2, 1.3, 1.4}, {2.1, 2.2, 2.3, 2.4}, {3.1, 3.2, 3.3, 3.4}},{{4.1, 4.2, 4.3, 4.4}, {5.1, 5.2, 5.3, 5.4}, {6.1, 6.2, 6.3, 6.4}}
            };
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 316))

    def test_317(self):
        input = """
            type Tree struct {
                value int;
                left Tree;
                right Tree;
            }

            func (t Tree) insert(val int) {
                if (val < t.value) {
                    t.left.insert(val);
                } else {
                    t.right.insert(val);
                }
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 317))

    def test_318(self):
        input = """
            func quickSort(arr [100]int, low int, high int) {
                if (low < high) {
                    pivot := arr[high];
                    i := low - 1;
                    
                    for j := low; j < high; j += 1 {
                        if (arr[j] < pivot) {
                            i += 1;
                            temp := arr[i];
                            arr[i] := arr[j];
                            arr[j] := temp;
                        }
                    }
                }
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 318))

    def test_319(self):
        input = """
            type Queue interface {
                enqueue(value int);
                dequeue() int;
                peek() int;
                isEmpty() boolean;
                isFull() boolean
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 319))

    def test_320(self):
        input = """
            func calculateStats(numbers [100]float) float {
                var sum float = 0.0;
                var count int = 0;
                
                for i := 0; i < 100; i += 1 {
                    if (numbers[i] > 0.0) {
                        sum += numbers[i];
                        count += 1;
                    }
                }
                
                return sum / float(count);
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 320))

    def test_321(self):
        input = """
            type HashTable struct {
                size int;
                table [1000]int;
            }

            func (h HashTable) hash(key int) int {
                return key % h.size;
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 321))

    def test_322(self):
        input = """
            func gcd(a int, b int) int {
                for b != 0 {
                    temp := b;
                    b := a % b;
                    a := temp;
                }
                return a;
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 322))

    def test_323(self):
        input = """
            type Matrix struct {
                rows int;
                cols int;
                data [100][100]float;
            }

            func (m Matrix) multiply(other Matrix) Matrix {
                var result Matrix;
                return result;
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 323))

    def test_324(self):
        input = """
            func isPrime(n int) boolean {
                if (n <= 1) {
                    return false;
                }
                for i := 2; i * i <= n; i += 1 {
                    if (n % i == 0) {
                        return false;
                    }
                }
                return true;
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 324))

    def test_325(self):
        input = """
            type Graph interface {
                addVertex(v int);
                addEdge(from int, to int);
                removeVertex(v int);
                removeEdge(from int, to int);
                getNeighbors(v int) [100]int
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 325))

    def test_326(self):
        input = """
            type BinaryTreeNode struct {
                data int;
                left BinaryTreeNode;
                right BinaryTreeNode;
                parent BinaryTreeNode;
            }

            func (node BinaryTreeNode) findMin() BinaryTreeNode {
                current := node;
                for current.left != nil {
                    current := current.left;
                }
                return current;
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 326))

    def test_327(self):
        input = """
            func mergeSort(arr [100]int, left int, right int) {
                if (left < right) {
                    mid := (left + right) / 2;
                    mergeSort(arr, left, mid);
                    mergeSort(arr, mid + 1, right);
                }
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 327))

    def test_328(self):
        input = """
            type Set interface {
                add(element int);
                remove(element int);
                contains(element int) boolean;
                size() int;
                isEmpty() boolean;
                clear()
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 328))

    def test_329(self):
        input = """
            func (ht HashTable) resize() {
                oldTable := ht.table;
                ht.size *= 2;
                ht.table := [2000]int{};
                
                for i := 0; i < ht.size / 2; i += 1 {
                    if (oldTable[i] != 0) {
                        ht.insert(oldTable[i]);
                    }
                }
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 329))

    def test_330(self):
        input = """
            type ComplexNumber struct {
                real float;
                imag float;
            }

            func (c ComplexNumber) add(other ComplexNumber) ComplexNumber {
                return ComplexNumber{
                    real: c.real + other.real,
                    imag: c.imag + other.imag
                };
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 330))

    def test_331(self):
        input = """
            func binarySearch(arr [100]int, target int) int {
                left := 0;
                right := 99;
                
                for left <= right {
                    mid := (left + right) / 2;
                    if (arr[mid] == target) { return mid; }
                    if (arr[mid] < target) { left := mid + 1; }
                    else { right := mid - 1; }
                }
                return -1;
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 331))

    def test_332(self):
        input = """
            type Stack struct {
                elements [100]int;
                top int;
            }

            func (s Stack) push(element int) boolean {
                if (s.top >= 100) { return false; }
                s.elements[s.top] := element;
                s.top += 1;
                return true;
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 332))

    def test_333(self):
        input = """
            func calculateFactorial(n int) int {
                if (n <= 1) { return 1; }
                result := 1;
                for i := 2; i <= n; i += 1 {
                    result *= i;
                }
                return result;
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 333))

    def test_334(self):
        input = """
            type CircularQueue struct {
                items [100]int;
                head int;
                tail int;
                size int;
            }

            func (cq CircularQueue) isFull() boolean {
                return cq.size == 100;
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 334))

    def test_335(self):
        input = """
            func findLongestCommonPrefix(str1 string, str2 string) string {
                minLen := len(str1);
                if (len(str2) < minLen) {
                    minLen := len(str2);
                }
                
                for i := 0; i < minLen; i += 1 {
                    if (str1[i] != str2[i]) {
                        return str1[0:i];
                    }
                }
                return str1[0:minLen];
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 335))

    def test_336(self):
        input = """
            type RGB struct {
                red int;
                green int;
                blue int;
            }

            func (color RGB) toGrayscale() int {
                return (color.red + color.green + color.blue) / 3;
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 336))

    def test_337(self):
        input = """
            func isPalindrome(str string) boolean {
                length := len(str);
                for i := 0; i < length / 2; i += 1 {
                    if (str[i] != str[length - 1 - i]) {
                        return false;
                    }
                }
                return true;
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 337))

    def test_338(self):
        input = """
            type Matrix3D struct {
                data [10][10][10]float;
                rows int;
                cols int;
                depth int;
            }

            func (m Matrix3D) initialize(value float) {
                for i := 0; i < m.rows; i += 1 {
                    for j := 0; j < m.cols; j += 1 {
                        for k := 0; k < m.depth; k += 1 {
                            m.data[i][j][k] := value;
                        }
                    }
                }
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 338))

    def test_339(self):
        input = """
            func generateFibonacci(n int) [100]int {
                var result [100]int;
                if (n <= 0) { return result; }
                result[0] := 0;
                if (n == 1) { return result; }
                result[1] := 1;
                for i := 2; i < n; i += 1 {
                    result[i] := result[i-1] + result[i-2];
                }
                return result;
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 339))

    def test_340(self):
        input = """
            type AVLNode struct {
                key int;
                height int;
                left AVLNode;
                right AVLNode;
            }

            func (node AVLNode) getHeight() int {
                if (node == nil) {
                    return -1;
                }
                return node.height;
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 340))

    def test_341(self):
        input = """
            func bubbleSort(arr [100]int) {
                n := 100;
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
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 341))

    def test_342(self):
        input = """
            type PriorityQueue interface {
                insert(element int, priority int);
                deleteMin() int;
                decreaseKey(element int, newPriority int);
                isEmpty() boolean;
                size() int
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 342))

    def test_343(self):
        input = """
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
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 343))

    def test_344(self):
        input = """
            type Fraction struct {
                numerator int;
                denominator int;
            }

            func (f Fraction) simplify() Fraction {
                gcd := calculateGCD(f.numerator, f.denominator);
                return Fraction{
                    numerator: f.numerator / gcd,
                    denominator: f.denominator / gcd
                };
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 344))

    def test_345(self):
        input = """
            func findMaxSubarraySum(arr [100]int) int {
                maxSoFar := arr[0];
                currMax := arr[0];
                
                for i := 1; i < 100; i += 1 {
                    currMax := max(arr[i], currMax + arr[i]);
                    maxSoFar := max(maxSoFar, currMax);
                }
                return maxSoFar;
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 345))

    def test_346(self):
        input = """
            type Vector3D struct {
                x float;
                y float;
                z float;
            }

            func (v Vector3D) crossProduct(other Vector3D) Vector3D {
                return Vector3D{
                    x: v.y * other.z - v.z * other.y,
                    y: v.z * other.x - v.x * other.z,
                    z: v.x * other.y - v.y * other.x
                };
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 346))

    def test_347(self):
        input = """
            func countSort(arr [100]int) [100]int {
                var count [100]int;
                var output [100]int;
                
                for i := 0; i < 100; i += 1 {
                    count[arr[i]] += 1;
                }
                
                for i := 1; i < 100; i += 1 {
                    count[i] += count[i-1];
                }
                
                return output;
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 347))

    def test_348(self):
        input = """
            type WeightedGraph interface {
                addEdge(from int, to int, weight float);
                removeEdge(from int, to int);
                getWeight(from int, to int) float;
                isAdjacent(from int, to int) boolean;
                getNeighbors(vertex int) [100]int
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 348))

    def test_349(self):
        input = """
            func evaluatePostfix(expression string) float {
                var stack [100]float;
                top := -1;
                
                for i := 0; i < len(expression); i += 1 {
                    if (isDigit(expression[i])) {
                        top += 1;
                        stack[top] := float(expression[i] - "0");
                    }
                }
                return stack[top];
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 349))

    def test_350(self):
        input = """
            type Trie struct {
                isEndOfWord boolean;
                children [26]Trie;
            }

            func (t Trie) insert(word string) {
                current := t;
                for i := 0; i < len(word); i += 1 {
                    index := word[i] - "a";
                    if (current.children[index] == nil) {
                        current.children[index] := Trie{isEndOfWord: false};
                    }
                    current := current.children[index];
                }
                current.isEndOfWord := true;
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 350))

    def test_351(self):
        input = """
            type BTree struct {
                keys [100]int;
                children [101]BTree;
                count int;
                isLeaf boolean;
            }

            func (b BTree) splitChild(i int, child BTree) {
                newNode := BTree{isLeaf: child.isLeaf};
                newNode.count := b.count / 2;
                
                for j := 0; j < newNode.count; j += 1 {
                    newNode.keys[j] := child.keys[j + b.count];
                }
                
                if (!child.isLeaf) {
                    for j := 0; j < newNode.count + 1; j += 1 {
                        newNode.children[j] := child.children[j + b.count];
                    }
                }
                
                child.count := b.count / 2;
                b.children[i + 1] := newNode;
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 351))

    def test_352(self):
        input = """
            type RedBlackNode struct {
                key int;
                color boolean;
                left RedBlackNode;
                right RedBlackNode;
                parent RedBlackNode;
            }

            func (tree RedBlackNode) rotateLeft(node RedBlackNode) {
                rightChild := node.right;
                node.right := rightChild.left;
                
                if (rightChild.left != nil) {
                    rightChild.left.parent := node;
                }
                
                rightChild.parent := node.parent;
                
                if (node.parent == nil) {
                    tree := rightChild;
                } else if (node == node.parent.left) {
                    node.parent.left := rightChild;
                } else {
                    node.parent.right := rightChild;
                }
                
                rightChild.left := node;
                node.parent := rightChild;
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 352))

    def test_353(self):
        input = """
            type Graph struct {
                vertices int;
                adjMatrix [100][100]float;
            }

            func (g Graph) floydWarshall() [100][100]float {
                var dist [100][100]float;
                
                for i := 0; i < g.vertices; i += 1 {
                    for j := 0; j < g.vertices; j += 1 {
                        dist[i][j] := g.adjMatrix[i][j];
                    }
                }
                
                for k := 0; k < g.vertices; k += 1 {
                    for i := 0; i < g.vertices; i += 1 {
                        for j := 0; j < g.vertices; j += 1 {
                            if (dist[i][k] + dist[k][j] < dist[i][j]) {
                                dist[i][j] := dist[i][k] + dist[k][j];
                            }
                        }
                    }
                }
                return dist;
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 353))

    def test_354(self):
        input = """
            type Heap struct {
                data [100]int;
                size int;
            }

            func (h Heap) heapifyDown(index int) {
                smallest := index;
                left := 2 * index + 1;
                right := 2 * index + 2;

                if (left < h.size && h.data[left] < h.data[smallest]) {
                    smallest := left;
                }

                if (right < h.size && h.data[right] < h.data[smallest]) {
                    smallest := right;
                }

                if (smallest != index) {
                    temp := h.data[index];
                    h.data[index] := h.data[smallest];
                    h.data[smallest] := temp;
                    h.heapifyDown(smallest);
                }
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 354))

    def test_355(self):
        input = """
            type DynamicArray struct {
                elements [100]int;
                size int;
                capacity int;
            }

            func (da DynamicArray) resize() {
                newCapacity := da.capacity * 2;
                var newElements [100]int;
                
                for i := 0; i < da.size; i += 1 {
                    newElements[i] := da.elements[i];
                }
                
                da.elements := newElements;
                da.capacity := newCapacity;
            }

            func (da DynamicArray) add(element int) {
                if (da.size == da.capacity) {
                    da.resize();
                }
                da.elements[da.size] := element;
                da.size += 1;
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 355))

    def test_356(self):
        input = """
            type SegmentTree struct {
                tree [400]int;
                lazy [400]int;
            }

            func (st SegmentTree) updateRange(node int, start int, end int, l int, r int, val int) {
                if (st.lazy[node] != 0) {
                    st.tree[node] += (end - start + 1) * st.lazy[node];
                    if (start != end) {
                        st.lazy[node * 2] += st.lazy[node];
                        st.lazy[node * 2 + 1] += st.lazy[node];
                    }
                    st.lazy[node] := 0;
                }

                if (start > end || start > r || end < l) {
                    return;
                }

                if (start >= l && end <= r) {
                    st.tree[node] += (end - start + 1) * val;
                    if (start != end) {
                        st.lazy[node * 2] += val;
                        st.lazy[node * 2 + 1] += val;
                    }
                    return;
                }

                mid := (start + end) / 2;
                st.updateRange(node * 2, start, mid, l, r, val);
                st.updateRange(node * 2 + 1, mid + 1, end, l, r, val);
                st.tree[node] := st.tree[node * 2] + st.tree[node * 2 + 1];
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 356))

    def test_357(self):
        input = """
            type SkipList struct {
                head SkipNode;
                level int;
            }

            type SkipNode struct {
                key int;
                forward [10]SkipNode;
            }

            func (sl SkipList) insert(key int) {
                var update [10]SkipNode;
                current := sl.head;

                for i := sl.level - 1; i >= 0; i -= 1 {
                    for current.forward[i] != nil && current.forward[i].key < key {
                        current := current.forward[i];
                    }
                    update[i] := current;
                }

                level := sl.randomLevel();
                if (level > sl.level) {
                    for i := sl.level; i < level; i += 1 {
                        update[i] := sl.head;
                    }
                    sl.level := level;
                }

                newNode := SkipNode{key: key};
                for i := 0; i < level; i += 1 {
                    newNode.forward[i] := update[i].forward[i];
                    update[i].forward[i] := newNode;
                }
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 357))

    def test_358(self):
        input = """
            type SuffixArray struct {
                text string;
                suffixes [100]int;
                length int;
            }

            func (sa SuffixArray) buildSuffixArray() {
                for i := 0; i < sa.length; i += 1 {
                    sa.suffixes[i] := i;
                }

                for i := 0; i < sa.length - 1; i += 1 {
                    for j := 0; j < sa.length - i - 1; j += 1 {
                        if (sa.compare(sa.suffixes[j], sa.suffixes[j + 1]) > 0) {
                            temp := sa.suffixes[j];
                            sa.suffixes[j] := sa.suffixes[j + 1];
                            sa.suffixes[j + 1] := temp;
                        }
                    }
                }
            }

            func (sa SuffixArray) compare(i int, j int) int {
                for i < sa.length && j < sa.length {
                    if (sa.text[i] != sa.text[j]) {
                        return sa.text[i] - sa.text[j];
                    }
                    i += 1;
                    j += 1;
                }
                return sa.length - j;
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 358))

    def test_359(self):
        input = """
            type DisjointSet struct {
                parent [100]int;
                rank [100]int;
                size int;
            }

            func (ds DisjointSet) makeSet(n int) {
                ds.size := n;
                for i := 0; i < n; i += 1 {
                    ds.parent[i] := i;
                    ds.rank[i] := 0;
                }
            }

            func (ds DisjointSet) find(x int) int {
                if (ds.parent[x] != x) {
                    ds.parent[x] := ds.find(ds.parent[x]);
                }
                return ds.parent[x];
            }

            func (ds DisjointSet) union(x int, y int) {
                xRoot := ds.find(x);
                yRoot := ds.find(y);

                if (xRoot == yRoot) {
                    return;
                }

                if (ds.rank[xRoot] < ds.rank[yRoot]) {
                    ds.parent[xRoot] := yRoot;
                } else if (ds.rank[xRoot] > ds.rank[yRoot]) {
                    ds.parent[yRoot] := xRoot;
                } else {
                    ds.parent[yRoot] := xRoot;
                    ds.rank[xRoot] += 1;
                }
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 359))

    def test_360(self):
        input = """
            type Polynomial struct {
                coefficients [100]float;
                degree int;
            }

            func (p Polynomial) evaluate(x float) float {
                result := p.coefficients[0];
                power := x;
                
                for i := 1; i <= p.degree; i += 1 {
                    result += p.coefficients[i] * power;
                    power *= x;
                }
                
                return result;
            }

            func (p Polynomial) derivative() Polynomial {
                if (p.degree == 0) {
                    return Polynomial{coefficients: [100]float{0}, degree: 0};
                }

                var derivCoeff [100]float;
                for i := 1; i <= p.degree; i += 1 {
                    derivCoeff[i-1] := float(i) * p.coefficients[i];
                }

                return Polynomial{
                    coefficients: derivCoeff,
                    degree: p.degree - 1
                };
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 360))

