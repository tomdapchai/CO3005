.source MiniGoClass.java
.class public MiniGoClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
Label0:
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label2:
.var 1 is i I from Label2 to Label3
	iconst_0
	istore_1
.var 2 is j I from Label2 to Label3
	iconst_0
	istore_2
Label4:
	iload_1
	iconst_3
	if_icmpge Label6
	iconst_1
	goto Label7
Label6:
	iconst_0
Label7:
	ifle Label5
Label8:
Label10:
	iload_2
	iconst_3
	if_icmpge Label12
	iconst_1
	goto Label13
Label12:
	iconst_0
Label13:
	ifle Label11
Label14:
	iload_1
	iconst_3
	imul
	iload_2
	iadd
	iconst_1
	iadd
	invokestatic io/putInt(I)V
	ldc " "
	invokestatic io/putString(Ljava/lang/String;)V
	iload_2
	iconst_1
	iadd
	istore_2
	iload_2
	iconst_2
	if_icmpne Label18
	iconst_1
	goto Label19
Label18:
	iconst_0
Label19:
	ifle Label16
Label20:
	goto Label11
Label21:
Label16:
Label15:
	goto Label10
Label11:
	ldc ""
	invokestatic io/putStringLn(Ljava/lang/String;)V
	iconst_0
	istore_2
	iload_1
	iconst_1
	iadd
	istore_1
	iload_1
	iconst_2
	if_icmpne Label24
	iconst_1
	goto Label25
Label24:
	iconst_0
Label25:
	ifle Label22
Label26:
	goto Label5
Label27:
Label22:
Label9:
	goto Label4
Label5:
Label3:
Label1:
	return
.limit stack 20
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
