.source MiniGoClass.java
.class public MiniGoClass
.super java.lang.Object
.field static x F

.method public static main([Ljava/lang/String;)V
Label0:
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label2:
.var 1 is a I from Label2 to Label3
	iconst_3
	istore_1
.var 2 is b I from Label2 to Label3
	iconst_5
	istore_2
.var 3 is n [F from Label2 to Label3
	iconst_3
	newarray float
	dup
	iconst_0
	iconst_1
	i2f
	fastore
	dup
	iconst_1
	iconst_2
	i2f
	fastore
	dup
	iconst_2
	iconst_3
	i2f
	fastore
	astore_3
	bipush 10
	iconst_3
	iadd
	i2f
	putstatic MiniGoClass/x F
	aload_3
	iconst_0
	faload
	aload_3
	iconst_1
	faload
	fadd
	aload_3
	iconst_2
	faload
	fadd
	invokestatic io/putFloatLn(F)V
Label3:
Label1:
	return
.limit stack 14
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
Label1:
	return
.limit stack 0
.limit locals 0
.end method
