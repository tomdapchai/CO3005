.source MiniGoClass.java
.class public MiniGoClass
.super java.lang.Object
.field static a I = 10
.field static y I = 15

.method public static main([Ljava/lang/String;)V
Label0:
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label2:
.var 1 is a I from Label2 to Label3
	iconst_5
	istore_1
.var 2 is b I from Label2 to Label3
	bipush 10
	istore_2
.var 3 is c I from Label2 to Label3
	bipush 15
	istore_3
.var 4 is d I from Label2 to Label3
	bipush 20
	istore 4
	iload_1
	iload_2
	iadd
	iload_3
	iadd
	iload 4
	iload_1
	irem
	iadd
	iload_1
	imul
	getstatic MiniGoClass/y I
	idiv
	invokestatic io/putInt(I)V
Label3:
Label1:
	return
.limit stack 11
.limit locals 5
.end method

.method public <init>()V
.var 0 is this LMiniGoClass; from Label0 to Label1
Label0:
	aload_0
	invokespecial java/lang/Object/<init>()V
Label1:
	return
.limit stack 1
.limit locals 1
.end method

.method public static <clinit>()V
Label0:
Label1:
	return
.limit stack 0
.limit locals 0
.end method
