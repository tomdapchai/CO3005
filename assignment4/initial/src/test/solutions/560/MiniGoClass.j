.source MiniGoClass.java
.class public MiniGoClass
.super java.lang.Object

.method public static calculateFactorial(I)I
Label0:
.var 0 is n I from Label0 to Label1
Label2:
	iload_0
	iconst_1
	if_icmpgt Label6
	iconst_1
	goto Label7
Label6:
	iconst_0
Label7:
	ifle Label4
Label8:
	iconst_1
	ireturn
Label9:
Label4:
	iconst_1
.var 1 is result I from Label2 to Label3
	istore_1
	iconst_2
.var 2 is i I from Label2 to Label3
	istore_2
Label12:
	iload_2
	iload_0
	if_icmpgt Label13
	iconst_1
	goto Label14
Label13:
	iconst_0
Label14:
	ifle Label11
Label15:
	iload_1
	iload_2
	imul
	istore_1
Label16:
Label10:
	iload_2
	iconst_1
	iadd
	istore_2
	goto Label12
Label11:
	iload_1
	ireturn
Label3:
Label1:
.limit stack 11
.limit locals 3
.end method

.method public static main([Ljava/lang/String;)V
Label0:
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label2:
.var 1 is n I from Label2 to Label3
	iconst_5
	istore_1
.var 2 is factorial I from Label2 to Label3
	iload_1
	invokestatic MiniGoClass/calculateFactorial(I)I
	istore_2
	iload_2
	invokestatic io/putIntLn(I)V
Label3:
Label1:
	return
.limit stack 2
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
