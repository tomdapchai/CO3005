.source MiniGoClass.java
.class public MiniGoClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
Label0:
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label2:
.var 1 is arr [I from Label2 to Label3
	iconst_3
	newarray int
	dup
	iconst_0
	bipush 10
	iastore
	dup
	iconst_1
	bipush 20
	iastore
	dup
	iconst_2
	bipush 30
	iastore
	astore_1
.var 2 is sum I from Label2 to Label3
	aload_1
	iconst_0
	iaload
	aload_1
	iconst_1
	iaload
	iadd
	aload_1
	iconst_2
	iaload
	iadd
	iconst_3
	newarray int
	dup
	iconst_0
	iconst_1
	iastore
	dup
	iconst_1
	iconst_2
	iastore
	dup
	iconst_2
	iconst_3
	iastore
	iconst_0
	iaload
	iadd
	iconst_3
	newarray int
	dup
	iconst_0
	iconst_4
	iastore
	dup
	iconst_1
	iconst_5
	iastore
	dup
	iconst_2
	bipush 6
	iastore
	iconst_1
	iaload
	iadd
	istore_2
	iload_2
	invokestatic io/putIntLn(I)V
Label3:
Label1:
	return
.limit stack 21
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
