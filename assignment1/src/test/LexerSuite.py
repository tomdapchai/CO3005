import unittest
from TestUtils import TestLexer

class LexerSuite(unittest.TestCase):
      
    def test_lower_identifier(self):
        """test identifiers"""
        self.assertTrue(TestLexer.checkLexeme("abc","abc,<EOF>",101))
    
    def test_wrong_token(self):
        self.assertTrue(TestLexer.checkLexeme("ab?sVN","ab,ErrorToken ?",102))
        
    def test_keyword_var(self):
        """test keyword var"""
        self.assertTrue(TestLexer.checkLexeme("var abc int ;","var,abc,int,;,<EOF>",103))

    def test_keyword_func(self):
        """test keyword func"""
        self.assertTrue(TestLexer.checkLexeme("""func abc ( ) ""","""func,abc,(,),<EOF>""",104))

    def test_keyword_break(self):
        """test keyword break"""
        self.assertTrue(TestLexer.checkLexeme("""break; continue;""", """break,;,continue,;,<EOF>""", 105))

    def test_keyword_const(self):
        """test keyword const"""
        self.assertTrue(TestLexer.checkLexeme("""const abc boolean x = nil;""", """const,abc,boolean,x,=,nil,;,<EOF>""", 106))

    def test_keyword_else(self):
        """test keyword if/else"""
        self.assertTrue(TestLexer.checkLexeme("""if If else Else""", """if,If,else,Else,<EOF>""", 107))

    def test_keyword_for(self):
        """test keyword for"""
        self.assertTrue(TestLexer.checkLexeme("""for i,v := range arr{}""", """for,i,,,v,:=,range,arr,{,},<EOF>""", 108))

    def test_keyword_interface(self):
        """test keyword interface"""
        self.assertTrue(TestLexer.checkLexeme("""type functions interface {}""", """type,functions,interface,{,},<EOF>""", 109))

    def test_keyword_return(self):
        """test keyword return"""
        self.assertTrue(TestLexer.checkLexeme("""return x+y+z;;;;""", """return,x,+,y,+,z,;,;,;,;,<EOF>""", 110))

    def test_keyword_struct(self):
        self.assertTrue(TestLexer.checkLexeme("""struct type float person, {}""", """struct,type,float,person,,,{,},<EOF>""", 111))

    def test_comment(self):
        self.assertTrue(TestLexer.checkLexeme("""/* This part is skipped as comment */ var // Next comment""", """var,<EOF>""", 112))

    def test_bin_lit(self):
        self.assertTrue(TestLexer.checkLexeme("""0b01111-012.432e-15""","""0b01111,-,012.432e-15,<EOF>""",113))

    def test_float_lit(self):
        self.assertTrue(TestLexer.checkLexeme("""-012.432e-15""","""-,012.432e-15,<EOF>""",114))

    def test_oct_lit(self):
        self.assertTrue(TestLexer.checkLexeme("""0o1234567 - 0O7654321 + 0O8""","""0o1234567,-,0O7654321,+,0,O8,<EOF>""",115))

    def test_hex_lit(self):
        self.assertTrue(TestLexer.checkLexeme("""0xaff-12=0Xbff""","""0xaff,-,12,=,0Xbff,<EOF>""",116))

    def test_117(self):    
        self.assertTrue(TestLexer.checkLexeme("12ab_sVN","12,ab_sVN,<EOF>",117))    

    def test_118(self):    
        self.assertTrue(TestLexer.checkLexeme("/*/**/*/","<EOF>",118)) 

    def test_119(self):    
        self.assertTrue(TestLexer.checkLexeme("000000","0,0,0,0,0,0,<EOF>",119)) 

    def test_120(self):    
        self.assertTrue(TestLexer.checkLexeme("00b0000","0,0b0000,<EOF>",120)) 

    def test_121(self):    
        self.assertTrue(TestLexer.checkLexeme("0b2.0e10","0,b2,.,0,e10,<EOF>",121)) 

    def test_122(self):    
        self.assertTrue(TestLexer.checkLexeme(".0e10",".,0,e10,<EOF>",122)) 

    def test_123(self):    
        self.assertTrue(TestLexer.checkLexeme("\"abc\\n\\t\"","\"abc\\n\\t\",<EOF>",123)) 

    def test_124(self):    
        self.assertTrue(TestLexer.checkLexeme("\"\\**\\n\"","Illegal escape in string: \"\\**\\n\"",124)) 

    def test_125(self):    
        self.assertTrue(TestLexer.checkLexeme("a:=b=+=c-=d--*=","a,:=,b,=,+=,c,-=,d,-,-,*=,<EOF>",125)) 

    def test_126(self):    
        self.assertTrue(TestLexer.checkLexeme("===/=\"==\"%=","==,=,/=,\"==\",%=,<EOF>",126))

    def test_127(self):    
        self.assertTrue(TestLexer.checkLexeme("597E+71","597,E,+,71,<EOF>",127))

    def test_128(self):    
        self.assertTrue(TestLexer.checkLexeme("6.E-33","6.E-33,<EOF>",128))

    def test_129(self):    
        self.assertTrue(TestLexer.checkLexeme("Aaj#^HdR","Aaj,ErrorToken #",129))

    def test_130(self):    
        self.assertTrue(TestLexer.checkLexeme("## F]R","ErrorToken #",130))

    def test_131(self):    
        self.assertTrue(TestLexer.checkLexeme("\"\\i'\"_)1'\"\"","Illegal escape in string: \"\\i'\"",131))

    def test_132(self):    
        self.assertTrue(TestLexer.checkLexeme("+-=[]{}|","+,-=,[,],{,},ErrorToken |",132))

    def test_133(self):    
        self.assertTrue(TestLexer.checkLexeme("func#main!(){fmt.Println(\"Hello\"}","func,ErrorToken #",133))

    def test_134(self):    
        self.assertTrue(TestLexer.checkLexeme("for;;i+=-1{break}","for,;,;,i,+=,-,1,{,break,},<EOF>",134))

    def test_135(self):    
        self.assertTrue(TestLexer.checkLexeme("\"A\" != B == !!true","\"A\",!=,B,==,!,!,true,<EOF>",135))

    def test_136(self):    
        self.assertTrue(TestLexer.checkLexeme("nil?? undefined:: 123.e+10","nil,ErrorToken ?",136))

    def test_137(self):    
        self.assertTrue(TestLexer.checkLexeme("struct{X int Y float64}{\"X\":42,\"Y\":3.14}","struct,{,X,int,Y,float64,},{,\"X\",:,42,,,\"Y\",:,3.14,},<EOF>",137))

    def test_138(self):    
        self.assertTrue(TestLexer.checkLexeme("map[int]string{1:\"One\", \"Two\":2}","map,[,int,],string,{,1,:,\"One\",,,\"Two\",:,2,},<EOF>",138))

    def test_139(self):    
        self.assertTrue(TestLexer.checkLexeme(":= *&^%$#@!()",":=,*,ErrorToken &",139))

    def test_140(self):    
        self.assertTrue(TestLexer.checkLexeme("\"\\\"Escape\\\\Sequence\\\\Test\\\"\"","\"\\\"Escape\\\\Sequence\\\\Test\\\"\",<EOF>",140))

    def test_141(self):    
        self.assertTrue(TestLexer.checkLexeme("0_123 123_","0,_123,123,_,<EOF>",141))

    def test_142(self):    
        self.assertTrue(TestLexer.checkLexeme("import \"fmt\" fmt.Println(\"Hello\"","import,\"fmt\",fmt,.,Println,(,\"Hello\",<EOF>",142))

    def test_143(self):    
        self.assertTrue(TestLexer.checkLexeme("a <*b && c<<=2","a,<,*,b,&&,c,<,<=,2,<EOF>",143))

    def test_144(self):    
        self.assertTrue(TestLexer.checkLexeme("// Nested /* comment */","<EOF>",144))

    def test_145(self):    
        self.assertTrue(TestLexer.checkLexeme(":=***===!==&&||",":=,*,*,*=,==,!=,=,&&,||,<EOF>",145))

    def test_146(self):    
        self.assertTrue(TestLexer.checkLexeme("00x123GHIJK","0,0x123,GHIJK,<EOF>",146))

    def test_147(self):    
        self.assertTrue(TestLexer.checkLexeme("var x = 1.2.3.4","var,x,=,1.2,.,3.4,<EOF>",147))

    def test_148(self):    
        self.assertTrue(TestLexer.checkLexeme("1_2_3_4_","1,_2_3_4_,<EOF>",148))

    def test_149(self):    
        self.assertTrue(TestLexer.checkLexeme("123abc def!","123,abc,def,!,<EOF>",149))

    def test_150(self):    
        self.assertTrue(TestLexer.checkLexeme("a := 3---2","a,:=,3,-,-,-,2,<EOF>",150))

    def test_151(self):    
        self.assertTrue(TestLexer.checkLexeme("for i:=0, i<10, i++ {}","for,i,:=,0,,,i,<,10,,,i,+,+,{,},<EOF>",151))
    
    def test_152(self):    
        self.assertTrue(TestLexer.checkLexeme("a := map[int]string{1: \"one\", 2: \"two\",,}","a,:=,map,[,int,],string,{,1,:,\"one\",,,2,:,\"two\",,,,,},<EOF>",152))

    def test_153(self):    
        self.assertTrue(TestLexer.checkLexeme("range 1..10 {}","range,1.,.,10,{,},<EOF>",153))

    def test_154(self):    
        self.assertTrue(TestLexer.checkLexeme("1.2.3e+4.5","1.2,.,3,e,+,4.5,<EOF>",154))

    def test_155(self):    
        self.assertTrue(TestLexer.checkLexeme("fmt.Printf(\"%d\", 42, 24)","fmt,.,Printf,(,\"%d\",,,42,,,24,),<EOF>",155))
    
    def test_156(self):    
        self.assertTrue(TestLexer.checkLexeme("1234.E++10","1234.,E,+,+,10,<EOF>",156))

    def test_157(self):    
        self.assertTrue(TestLexer.checkLexeme("a := make(chan<-int, -1)","a,:=,make,(,chan,<,-,int,,,-,1,),<EOF>",157))

    def test_158(self):    
        self.assertTrue(TestLexer.checkLexeme("x = **2","x,=,*,*,2,<EOF>",158))

    def test_159(self):    
        self.assertTrue(TestLexer.checkLexeme("breakcontinuereturn","breakcontinuereturn,<EOF>",159))

    def test_160(self):    
        self.assertTrue(TestLexer.checkLexeme("foo = bar && || !baz","foo,=,bar,&&,||,!,baz,<EOF>",160))

    def test_newline_1(self):
        """test newline"""
        self.assertTrue(TestLexer.checkLexeme(
"""type Person struct {
    name string
    age int
}

var x int = 10;""",
"""type,Person,struct,{,name,string,;,age,int,;,},;,var,x,int,=,10,;,<EOF>""",
        161)) 

    def test_newline_2(self):
        """test newline"""
        self.assertTrue(TestLexer.checkLexeme(
"""
const x = 12
var y float
""",
"""const,x,=,12,;,var,y,float,;,<EOF>""",
        162)) 

    def test_newline_3(self):
        """test newline"""
        self.assertTrue(TestLexer.checkLexeme(
"""
func main() int {
    var x string = ""
}
""",
"""func,main,(,),int,{,var,x,string,=,"",;,},;,<EOF>""",
        163)) 

    def test_newline_4(self):
        """test newline"""
        self.assertTrue(TestLexer.checkLexeme(
"""func id() {}
""",
"""func,id,(,),{,},;,<EOF>""",
        164)) 

    def test_newline_5(self):
        """test newline"""
        self.assertTrue(TestLexer.checkLexeme(
"""var 12int=intx = ""
""",
"""var,12,int,=,intx,=,"",;,<EOF>""",
        165)) 

    def test_newline_6(self):
        """test newline"""
        self.assertTrue(TestLexer.checkLexeme(
"""type Calculator interface {
    Subtract(a, b float, c int) float
    SayHello(name string)
}""",
"""type,Calculator,interface,{,Subtract,(,a,,,b,float,,,c,int,),float,;,SayHello,(,name,string,),;,},<EOF>""",
        166)) 

    def test_newline_7(self):
        """test newline"""
        self.assertTrue(TestLexer.checkLexeme(
"""if (b == 2) {fmt.Println(b)
	
} else if (x == 1) {
	fmt.Println(x)
}""",
"""if,(,b,==,2,),{,fmt,.,Println,(,b,),;,},else,if,(,x,==,1,),{,fmt,.,Println,(,x,),;,},<EOF>""",
        167)) 

    def test_newline_8(self):
        """test newline"""
        self.assertTrue(TestLexer.checkLexeme(
"""
arr := [3]int{10, 20, 30}
for _, value := range arr {
 // value: 10, 20, 30
}
""",
"""arr,:=,[,3,],int,{,10,,,20,,,30,},;,for,_,,,value,:=,range,arr,{,},;,<EOF>""",
        168)) 

    def test_newline_9(self):
        """test newline"""
        self.assertTrue(TestLexer.checkLexeme(
"""
for index, value := range arr 
{}
""",
"""for,index,,,value,:=,range,arr,;,{,},;,<EOF>""",
        169)) 

    def test_newline_10(self):
        """test newline"""
        self.assertTrue(TestLexer.checkLexeme(
"""
person.name := "John"
person.age := 30
""",
"""person,.,name,:=,"John",;,person,.,age,:=,30,;,<EOF>""",
        170)) 

    def test_error_token_1(self):
        """test error token"""
        self.assertTrue(TestLexer.checkLexeme(
"""abcd1!as""",
"""abcd1,!,as,<EOF>""",
        171))

    def test_error_token_2(self):
        """test error token"""
        self.assertTrue(TestLexer.checkLexeme(
"""mm@hcmut.edu.vn""",
"""mm,ErrorToken @""",
        172)) 

    def test_error_token_3(self):
        """test error token"""
        self.assertTrue(TestLexer.checkLexeme(
"""x = "This is string with illegal char #" ## """,
"""x,=,"This is string with illegal char #",ErrorToken #""",
        173)) 

    def test_error_token_4(self):
        """test error token"""
        self.assertTrue(TestLexer.checkLexeme(
"""$$x$$""",
"""ErrorToken $""",
        174)) 

    def test_error_token_5(self):
        """test error token"""
        self.assertTrue(TestLexer.checkLexeme(
"""7^3""",
"""7,ErrorToken ^""",
        175)) 

    def test_error_token_6(self):
        """test error token"""
        self.assertTrue(TestLexer.checkLexeme(
"""int *p=x&&&x""",
"""int,*,p,=,x,&&,ErrorToken &""",
        176)) 

    def test_error_token_7(self):
        """test error token"""
        self.assertTrue(TestLexer.checkLexeme(
"""|||\\""",
"""||,ErrorToken |""",
        177)) 

    def test_error_token_8(self):
        """test error token"""
        self.assertTrue(TestLexer.checkLexeme(
"""x = x'""",
"""x,=,x,ErrorToken '""",
        178)) 

    def test_error_token_9(self):
        """test error token"""
        self.assertTrue(TestLexer.checkLexeme(
"""\\""",
"""ErrorToken \\""",
        179)) 

    def test_error_token_10(self):
        """test error token"""
        self.assertTrue(TestLexer.checkLexeme(
"""t = 1?true:false""",
"""t,=,1,ErrorToken ?""",
        180)) 

#     def test_illegal_escape_1(self):
#         """test illegal escape"""
#         self.assertTrue(TestLexer.checkLexeme(
# """\"\\t\\y\"""",
# """Illegal escape in string: \"\\t\\y\"""",
#         181))

#     def test_illegal_escape_2(self):
#         """test illegal escape"""
#         self.assertTrue(TestLexer.checkLexeme(
# """\"\\t'\"_)1\"\\im\"""",
# """\"\\t'\",_,),1,Illegal escape in string: \"\\im\"""",
#         182)) 

#     def test_illegal_escape_3(self):
#         """test illegal escape"""
#         self.assertTrue(TestLexer.checkLexeme(
# """\"@@\\f\"""",
# """Illegal escape in string: \"@@\\f\"""",
#         183)) 

#     def test_illegal_escape_4(self):
#         """test illegal escape"""
#         self.assertTrue(TestLexer.checkLexeme(
# """\"\\n\\t\" ++ \"@@\\f\"""",
# """\"\\n\\t\",+,+,Illegal escape in string: \"@@\\f\"""",
#         184)) 

#     def test_illegal_escape_5(self):
#         """test illegal escape"""
#         self.assertTrue(TestLexer.checkLexeme(
# """\"\\u\\t\\u\"""",
# """Illegal escape in string: \"\\u\\t\\u\"""",
#         185)) 

#     def test_illegal_escape_6(self):
#         """test illegal escape"""
#         self.assertTrue(TestLexer.checkLexeme(
# """\"\\tt\\n\\"t\\u\\u\"""",
# """Illegal escape in string: \"\\tt\\n\\"t\\u\\u\"""",
#         186)) 

#     def test_illegal_escape_7(self):
#         """test illegal escape"""
#         self.assertTrue(TestLexer.checkLexeme(
# """\"\\v\"""",
# """Illegal escape in string: \"\\v\"""",
#         187)) 

#     def test_illegal_escape_8(self):
#         """test illegal escape"""
#         self.assertTrue(TestLexer.checkLexeme(
# """\"\\",\\t\\,\"""",
# """Illegal escape in string: \"\\",\\t\\,\"""",
#         188)) 

#     def test_illegal_escape_9(self):
#         """test illegal escape"""
#         self.assertTrue(TestLexer.checkLexeme(
# """\"\\u\\u\\u\\u\"""",
# """Illegal escape in string: \"\\u\\u\\u\\u\"""",
#         189)) 

#     def test_illegal_escape_10(self):
#         """test illegal escape"""
#         self.assertTrue(TestLexer.checkLexeme(
# """1\"\\1\"""",
# """1,Illegal escape in string: \"\\1\"""",
#         190)) 

#     def test_unclosed_string_1(self):
#         """test unclose string"""
#         self.assertTrue(TestLexer.checkLexeme(
# """var x = "this is test\\nstring
# func abc ()""",
# """var,x,=,Unclosed string: "this is test\\nstring""",
#         191)) 

#     def test_unclosed_string_2(self):
#         """test unclose string"""
#         self.assertTrue(TestLexer.checkLexeme(
# """"t""",
# """Unclosed string: "t""",
#         192)) 

#     def test_unclosed_string_3(self):
#         """test unclose string"""
#         self.assertTrue(TestLexer.checkLexeme(
# """func test() {
# var x = "" "string without end
# }""",
#             """func,test,(,),{,var,x,=,"",Unclosed string: "string without end""",
#         193))

#     def test_unclosed_string_4(self):
#         """test unclose string"""
#         self.assertTrue(TestLexer.checkLexeme(
# """ "" " """,
# """"",Unclosed string: " """,
#         194))

#     def test_unclosed_string_5(self):
#         """test unclose string"""
#         self.assertTrue(TestLexer.checkLexeme(
# """test"Hello World""",
# """test,Unclosed string: "Hello World""",
#         195))

#     def test_unclosed_string_6(self):
#         """test unclose string"""
#         self.assertTrue(TestLexer.checkLexeme(
# """a"\\"" test""",
# """a,"\\"",test,<EOF>""",
#         196))

#     def test_unclosed_string_7(self):
#         """test unclose string"""
#         self.assertTrue(TestLexer.checkLexeme(
# """var text = "str
# ing\"""",
# """var,text,=,Unclosed string: "str""",
#         197))

#     def test_unclosed_string_8(self):
#         """test unclose string"""
#         self.assertTrue(TestLexer.checkLexeme(
# """var msg = "hello\\n
# var name = "world";""",
#             """var,msg,=,Unclosed string: "hello\\n""",
#         198))

#     def test_unclosed_string_9(self):
#         """test unclose string"""
#         self.assertTrue(TestLexer.checkLexeme(
# """"
# 1'"M7";""",
#             """Unclosed string: \"""",
#         199))

#     def test_unclosed_string_10(self):
#         """test unclose string"""
#         self.assertTrue(TestLexer.checkLexeme(
# """"test with \\t\\"\\n\\\\""",
# """Unclosed string: "test with \\t\\"\\n\\\\""",
#         200))
