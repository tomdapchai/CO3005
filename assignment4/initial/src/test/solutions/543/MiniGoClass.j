.source MiniGoClass.java
.class public MiniGoClass
.super java.lang.Object
.field static arr [I

.method public static main([Ljava/lang/String;)V
Label0:
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label2:
	getstatic MiniGoClass/arr [I
.var 1 is arr2 [I from Label2 to Label3
	astore_1
	aload_1
	iconst_3
	ldc 300000
	iastore
	getstatic MiniGoClass/arr [I
	iconst_3
	iaload
	invokestatic io/putIntLn(I)V
	aload_1
	iconst_3
	iaload
	invokestatic io/putIntLn(I)V
Label3:
Label1:
	return
.limit stack 6
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
	iconst_5
	newarray int
	dup
	iconst_0
	iconst_0
	iastore
	dup
	iconst_1
	iconst_1
	iastore
	dup
	iconst_2
	iconst_2
	iastore
	dup
	iconst_3
	iconst_3
	iastore
	dup
	iconst_4
	iconst_4
	iastore
	putstatic MiniGoClass/arr [I
Label1:
	return
.limit stack 10
.limit locals 0
.end method
