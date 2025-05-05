.source MiniGoClass.java
.class public MiniGoClass
.super java.lang.Object
.field static a [I

.method public static main([Ljava/lang/String;)V
Label0:
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label2:
	getstatic MiniGoClass/a [I
	iconst_0
	iaload
	invokestatic io/putIntLn(I)V
	getstatic MiniGoClass/a [I
	iconst_1
	getstatic MiniGoClass/a [I
	iconst_1
	iaload
	bipush 10
	iadd
	iastore
	getstatic MiniGoClass/a [I
	iconst_1
	iaload
	invokestatic io/putIntLn(I)V
Label3:
Label1:
	return
.limit stack 7
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
	putstatic MiniGoClass/a [I
Label1:
	return
.limit stack 8
.limit locals 0
.end method
