.source MiniGoClass.java
.class public MiniGoClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
Label0:
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label2:
	bipush 10
	bipush 20
	bipush 30
	invokestatic MiniGoClass/sum(III)I
	invokestatic io/putIntLn(I)V
	ldc 10.5
	ldc 20.5
	ldc 30.5
	invokestatic MiniGoClass/average(FFF)F
	invokestatic io/putFloatLn(F)V
Label3:
Label1:
	return
.limit stack 6
.limit locals 1
.end method

.method public static sum(III)I
Label0:
.var 0 is a I from Label0 to Label1
.var 1 is b I from Label0 to Label1
.var 2 is c I from Label0 to Label1
Label2:
	iload_0
	iload_1
	iadd
	iload_2
	iadd
	ireturn
Label3:
Label1:
.limit stack 2
.limit locals 3
.end method

.method public static average(FFF)F
Label0:
.var 0 is a F from Label0 to Label1
.var 1 is b F from Label0 to Label1
.var 2 is c F from Label0 to Label1
Label2:
	fload_0
	fload_1
	fadd
	fload_2
	fadd
	ldc 3.0
	fdiv
	freturn
Label3:
Label1:
.limit stack 2
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
