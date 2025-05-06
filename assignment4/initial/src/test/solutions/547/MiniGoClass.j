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
.var 3 is n [[F from Label2 to Label3
	iconst_3
	iconst_4
	multianewarray [[F 2
	dup
	iconst_0
	aaload
	iconst_0
	ldc 1.2
	fastore
	dup
	iconst_0
	aaload
	iconst_1
	ldc 2.3
	fastore
	dup
	iconst_0
	aaload
	iconst_2
	iconst_3
	i2f
	fastore
	dup
	iconst_1
	aaload
	iconst_0
	ldc 4.5
	fastore
	dup
	iconst_1
	aaload
	iconst_1
	ldc 5.6
	fastore
	dup
	iconst_1
	aaload
	iconst_2
	ldc 6.55
	fastore
	dup
	iconst_1
	aaload
	iconst_3
	ldc 7.8
	fastore
	dup
	iconst_2
	aaload
	iconst_0
	ldc 10.2
	fastore
	dup
	iconst_2
	aaload
	iconst_1
	bipush 8
	i2f
	fastore
	dup
	iconst_2
	aaload
	iconst_2
	bipush 9
	i2f
	fastore
	astore_3
	aload_3
	iconst_0
	aaload
	iconst_2
	faload
	aload_3
	iconst_1
	aaload
	iconst_0
	faload
	fadd
	invokestatic io/putFloatLn(F)V
Label3:
Label1:
	return
.limit stack 25
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
