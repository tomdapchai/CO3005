.source MiniGoClass.java
.class public MiniGoClass
.super java.lang.Object

.method public static isPrime(I)Z
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
	iconst_0
	ireturn
Label9:
Label4:
.var 1 is i I from Label2 to Label3
	iconst_2
	istore_1
Label12:
	iload_1
	iload_1
	imul
	iload_0
	if_icmpgt Label13
	iconst_1
	goto Label14
Label13:
	iconst_0
Label14:
	ifle Label11
Label15:
	iload_0
	iload_1
	irem
	iconst_0
	if_icmpne Label19
	iconst_1
	goto Label20
Label19:
	iconst_0
Label20:
	ifle Label17
Label21:
	iconst_0
	ireturn
Label22:
Label17:
Label16:
Label10:
	iload_1
	iconst_1
	iadd
	istore_1
	goto Label12
Label11:
	iconst_1
	ireturn
Label3:
Label1:
.limit stack 12
.limit locals 2
.end method

.method public static main([Ljava/lang/String;)V
Label0:
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label2:
.var 1 is n I from Label2 to Label3
	bipush 29
	istore_1
	iload_1
	invokestatic MiniGoClass/isPrime(I)Z
	ifle Label4
Label6:
	ldc "Prime number"
	invokestatic io/putStringLn(Ljava/lang/String;)V
Label7:
	goto Label5
Label4:
Label8:
	ldc "Not a prime number"
	invokestatic io/putStringLn(Ljava/lang/String;)V
Label9:
Label5:
Label3:
Label1:
	return
.limit stack 2
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
Label1:
	return
.limit stack 0
.limit locals 0
.end method
