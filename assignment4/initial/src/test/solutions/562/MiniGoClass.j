.source MiniGoClass.java
.class public MiniGoClass
.super java.lang.Object

.method public static power(FI)F
Label0:
.var 0 is base F from Label0 to Label1
.var 1 is exponent I from Label0 to Label1
Label2:
	iload_1
	iconst_0
	if_icmpne Label6
	iconst_1
	goto Label7
Label6:
	iconst_0
Label7:
	ifle Label4
Label8:
	ldc 1.0
	freturn
Label9:
Label4:
	iload_1
	iconst_0
	if_icmpge Label12
	iconst_1
	goto Label13
Label12:
	iconst_0
Label13:
	ifle Label10
Label14:
	ldc 1.0
	fload_0
	fdiv
	fstore_0
	iload_1
	ineg
	istore_1
Label15:
Label10:
	ldc 1.0
.var 2 is result F from Label2 to Label3
	fstore_2
	iconst_0
.var 3 is i I from Label2 to Label3
	istore_3
Label18:
	iload_3
	iload_1
	if_icmpge Label19
	iconst_1
	goto Label20
Label19:
	iconst_0
Label20:
	ifle Label17
Label21:
	fload_2
	fload_0
	fmul
	fstore_2
Label22:
Label16:
	iload_3
	iconst_1
	iadd
	istore_3
	goto Label18
Label17:
	fload_2
	freturn
Label3:
Label1:
.limit stack 12
.limit locals 4
.end method

.method public static main([Ljava/lang/String;)V
Label0:
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label2:
.var 1 is base F from Label2 to Label3
	ldc 2.5
	fstore_1
.var 2 is exponent I from Label2 to Label3
	iconst_3
	istore_2
.var 3 is result F from Label2 to Label3
	fload_1
	iload_2
	invokestatic MiniGoClass/power(FI)F
	fstore_3
	fload_3
	invokestatic io/putFloatLn(F)V
Label3:
Label1:
	return
.limit stack 3
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
