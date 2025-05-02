.source MiniGoClass.java
.class public MiniGoClass
.super java.lang.Object
.field static a I
.field static y F = 15.5

.method public static main([Ljava/lang/String;)V
Label0:
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label2:
.var 1 is b I from Label2 to Label3
	bipush 10
	istore_1
.var 2 is c I from Label2 to Label3
	bipush 15
	istore_2
.var 3 is d I from Label2 to Label3
	bipush 20
	istore_3
	getstatic MiniGoClass/a I
	iload_1
	iadd
	iload_2
	iadd
	iload_3
	getstatic MiniGoClass/a I
	irem
	iadd
	getstatic MiniGoClass/a I
	imul
	i2f
	getstatic MiniGoClass/y F
	fsub
	invokestatic io/putFloat(F)V
Label3:
Label1:
	return
.limit stack 9
.limit locals 4
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
	iconst_5
	iconst_0
	iadd
	putstatic MiniGoClass/a I
Label1:
	return
.limit stack 4
.limit locals 0
.end method
