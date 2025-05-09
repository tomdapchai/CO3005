.source MiniGoClass.java
.class public MiniGoClass
.super java.lang.Object
.field static final size I = 3

.method public static main([Ljava/lang/String;)V
Label0:
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label2:
.var 1 is a I from Label2 to Label3
	iconst_3
	istore_1
.var 2 is arr [I from Label2 to Label3
	iconst_1
	invokestatic MiniGoClass/foo(I)[I
	astore_2
.var 3 is x I from Label2 to Label3
	iconst_2
	istore_3
	aload_2
	iload_3
	iload_1
	iadd
	iconst_3
	isub
	bipush 6
	iastore
	aload_2
	iconst_2
	iaload
	invokestatic io/putIntLn(I)V
	aload_2
	iconst_0
	iaload
	invokestatic io/putIntLn(I)V
Label3:
Label1:
	return
.limit stack 9
.limit locals 4
.end method

.method public static foo(I)[I
Label0:
.var 0 is a I from Label0 to Label1
Label2:
	iconst_3
	newarray int
	dup
	iconst_0
	iload_0
	iastore
	dup
	iconst_1
	iload_0
	iastore
	dup
	iconst_2
	iload_0
	iastore
	areturn
Label3:
Label1:
.limit stack 4
.limit locals 1
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
