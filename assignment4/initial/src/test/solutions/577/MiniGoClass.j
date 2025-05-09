.source MiniGoClass.java
.class public MiniGoClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
Label0:
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label2:
	bipush 10
	invokestatic MiniGoClass/foo(I)V
Label3:
Label1:
	return
.limit stack 2
.limit locals 1
.end method

.method public static foo(I)V
Label0:
.var 0 is n I from Label0 to Label1
Label2:
.var 1 is i I from Label2 to Label3
	iconst_1
	istore_1
Label6:
	iload_1
	iload_0
	if_icmpge Label7
	iconst_1
	goto Label8
Label7:
	iconst_0
Label8:
	ifle Label5
Label9:
	iload_1
	invokestatic io/putInt(I)V
Label10:
Label4:
	iload_1
	iconst_1
	iadd
	istore_1
	goto Label6
Label5:
	iconst_1
.var 2 is i I from Label2 to Label3
	istore_2
Label13:
	iload_2
	iload_0
	if_icmpge Label14
	iconst_1
	goto Label15
Label14:
	iconst_0
Label15:
	ifle Label12
Label16:
	iload_2
	invokestatic io/putInt(I)V
Label17:
Label11:
	iload_2
	iconst_1
	iadd
	istore_2
	goto Label13
Label12:
Label3:
Label1:
	return
.limit stack 10
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
