.source MiniGoClass.java
.class public MiniGoClass
.super java.lang.Object
.field static final a I = 5

.method public static main([Ljava/lang/String;)V
Label0:
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label2:
.var 1 is b I from Label2 to Label3
	iconst_3
	istore_1
.var 2 is a [I from Label2 to Label3
	iconst_4
	newarray int
	dup
	iconst_0
	iconst_5
	iastore
	dup
	iconst_1
	iconst_2
	iastore
	dup
	iconst_2
	iconst_3
	iastore
	dup
	iconst_3
	iconst_4
	iastore
	astore_2
.var 3 is arr [I from Label2 to Label3
	iconst_5
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
	dup
	iconst_3
	bipush 40
	iastore
	dup
	iconst_4
	bipush 50
	iastore
	astore_3
	aload_2
	iconst_1
	bipush 20
	iastore
.var 4 is x I from Label2 to Label3
	bipush 10
	istore 4
	aload_2
	iconst_0
	iaload
	aload_3
	iconst_0
	iaload
	iconst_2
	imul
	iadd
	aload_2
	iconst_1
	iaload
	iadd
	invokestatic io/putIntLn(I)V
Label3:
Label1:
	return
.limit stack 22
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
