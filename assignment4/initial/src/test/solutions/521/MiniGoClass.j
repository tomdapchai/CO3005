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
.var 2 is arr [I from Label2 to Label3
	iconst_4
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
	astore_2
.var 3 is x I from Label2 to Label3
	bipush 10
	istore_3
	iload_3
	invokestatic io/putIntLn(I)V
Label3:
Label1:
	return
.limit stack 16
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
