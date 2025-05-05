.source MiniGoClass.java
.class public MiniGoClass
.super java.lang.Object
.field static a [[I

.method public static main([Ljava/lang/String;)V
Label0:
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label2:
	getstatic MiniGoClass/a [[I
	iconst_0
	aaload
	iconst_0
	iaload
	invokestatic io/putIntLn(I)V
	getstatic MiniGoClass/a [[I
	iconst_0
	aaload
	iconst_1
	getstatic MiniGoClass/a [[I
	iconst_0
	aaload
	iconst_1
	iaload
	bipush 10
	iadd
	iastore
	getstatic MiniGoClass/a [[I
	iconst_0
	aaload
	iconst_1
	iaload
	invokestatic io/putIntLn(I)V
	getstatic MiniGoClass/a [[I
	iconst_2
	aaload
	iconst_1
	getstatic MiniGoClass/a [[I
	iconst_2
	aaload
	iconst_1
	iaload
	bipush 20
	isub
	iastore
	getstatic MiniGoClass/a [[I
	iconst_2
	aaload
	iconst_1
	iaload
	invokestatic io/putIntLn(I)V
Label3:
Label1:
	return
.limit stack 18
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
	iconst_4
	multianewarray [[I 2
	dup
	iconst_0
	aaload
	iconst_0
	iconst_1
	iastore
	dup
	iconst_0
	aaload
	iconst_1
	iconst_2
	iastore
	dup
	iconst_1
	aaload
	iconst_0
	iconst_4
	iastore
	dup
	iconst_1
	aaload
	iconst_1
	iconst_5
	iastore
	dup
	iconst_1
	aaload
	iconst_2
	bipush 6
	iastore
	dup
	iconst_1
	aaload
	iconst_3
	bipush 7
	iastore
	dup
	iconst_2
	aaload
	iconst_0
	bipush 10
	iastore
	dup
	iconst_2
	aaload
	iconst_1
	bipush 8
	iastore
	dup
	iconst_2
	aaload
	iconst_2
	bipush 9
	iastore
	putstatic MiniGoClass/a [[I
Label1:
	return
.limit stack 25
.limit locals 0
.end method
