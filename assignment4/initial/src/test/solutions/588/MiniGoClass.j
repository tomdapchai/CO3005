.source MiniGoClass.java
.class public MiniGoClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
Label0:
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label2:
.var 1 is matrix [[I from Label2 to Label3
	iconst_3
	iconst_3
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
	iconst_0
	aaload
	iconst_2
	iconst_3
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
	iconst_2
	aaload
	iconst_0
	bipush 7
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
	astore_1
.var 2 is mainDiag I from Label2 to Label3
	iconst_0
	istore_2
.var 3 is antiDiag I from Label2 to Label3
	iconst_0
	istore_3
	iconst_0
.var 4 is i I from Label2 to Label3
	istore 4
Label6:
	iload 4
	iconst_3
	if_icmpge Label7
	iconst_1
	goto Label8
Label7:
	iconst_0
Label8:
	ifle Label5
Label9:
	iload_2
	aload_1
	iload 4
	aaload
	iload 4
	iaload
	iadd
	istore_2
	iload_3
	aload_1
	iload 4
	aaload
	iconst_2
	iload 4
	isub
	iaload
	iadd
	istore_3
Label10:
Label4:
	iload 4
	iconst_1
	iadd
	istore 4
	goto Label6
Label5:
	ldc "Main diagonal sum:"
	invokestatic io/putStringLn(Ljava/lang/String;)V
	iload_2
	invokestatic io/putIntLn(I)V
	ldc "Anti-diagonal sum:"
	invokestatic io/putStringLn(Ljava/lang/String;)V
	iload_3
	invokestatic io/putIntLn(I)V
Label3:
Label1:
	return
.limit stack 32
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
