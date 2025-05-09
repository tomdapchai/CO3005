.source MiniGoClass.java
.class public MiniGoClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
Label0:
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label2:
.var 1 is a I from Label2 to Label3
	iconst_5
	istore_1
.var 2 is b F from Label2 to Label3
	ldc 2.5
	fstore_2
.var 3 is c F from Label2 to Label3
	iload_1
	i2f
	fload_2
	fmul
	iload_1
	iconst_2
	idiv
	i2f
	fadd
	fstore_3
	fload_3
	invokestatic io/putFloatLn(F)V
.var 4 is d F from Label2 to Label3
	iload_1
	i2f
	fload_2
	fmul
	iconst_3
	i2f
	fsub
	fstore 4
	fload 4
	invokestatic io/putFloatLn(F)V
Label3:
Label1:
	return
.limit stack 5
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
