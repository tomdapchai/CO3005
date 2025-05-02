.source MiniGoClass.java
.class public MiniGoClass
.super java.lang.Object
.field static final a I = 200
.field static y F = 15.5

.method public static main([Ljava/lang/String;)V
Label0:
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label2:
.var 1 is x I from Label2 to Label3
	bipush 10
	iconst_2
	imul
	iconst_3
	iadd
	istore_1
.var 2 is a I from Label2 to Label3
	bipush 20
	istore_2
	iload_2
	i2f
	getstatic MiniGoClass/y F
	fadd
	invokestatic io/putFloatLn(F)V
	iload_2
	bipush 10
	iadd
	istore_2
	iload_1
	iload_2
	imul
	invokestatic io/putIntLn(I)V
	getstatic MiniGoClass/y F
	bipush 10
	i2f
	fadd
	putstatic MiniGoClass/y F
	getstatic MiniGoClass/y F
	invokestatic io/putFloat(F)V
Label3:
Label1:
	return
.limit stack 11
.limit locals 3
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
