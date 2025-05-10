.source MiniGoClass.java
.class public MiniGoClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
Label0:
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label2:
.var 1 is a [[F from Label2 to Label3
	iconst_2
	iconst_2
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
	iconst_1
	aaload
	iconst_0
	ldc 2.5
	fastore
	dup
	iconst_1
	aaload
	iconst_1
	ldc 3.6
	fastore
	astore_1
	aload_1
	iconst_0
	aaload
	iconst_1
	ldc 5.6
	fastore
	aload_1
	iconst_0
	aaload
	iconst_1
	faload
	invokestatic io/putFloatLn(F)V
Label3:
Label1:
	return
.limit stack 13
.limit locals 2
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
