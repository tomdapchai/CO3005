.source MiniGoClass.java
.class public MiniGoClass
.super java.lang.Object

.method public static bubbleSort([II)V
Label0:
.var 0 is arr [I from Label0 to Label1
.var 1 is n I from Label0 to Label1
Label2:
	iconst_1
.var 2 is swapped Z from Label2 to Label3
	istore_2
Label4:
	iload_2
	ifle Label5
Label6:
	iconst_0
	istore_2
	iconst_1
.var 3 is i I from Label6 to Label7
	istore_3
Label10:
	iload_3
	iload_1
	if_icmpge Label11
	iconst_1
	goto Label12
Label11:
	iconst_0
Label12:
	ifle Label9
Label13:
	aload_0
	iload_3
	iconst_1
	isub
	iaload
	aload_0
	iload_3
	iaload
	if_icmple Label17
	iconst_1
	goto Label18
Label17:
	iconst_0
Label18:
	ifle Label15
Label19:
	aload_0
	iload_3
	iconst_1
	isub
	iaload
.var 4 is temp I from Label19 to Label20
	istore 4
	aload_0
	iload_3
	iconst_1
	isub
	aload_0
	iload_3
	iaload
	iastore
	aload_0
	iload_3
	iload 4
	iastore
	iconst_1
	istore_2
Label20:
Label15:
Label14:
Label8:
	iload_3
	iconst_1
	iadd
	istore_3
	goto Label10
Label9:
Label7:
	goto Label4
Label5:
Label3:
Label1:
	return
.limit stack 12
.limit locals 5
.end method

.method public static main([Ljava/lang/String;)V
Label0:
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label2:
.var 1 is arr [I from Label2 to Label3
	bipush 7
	newarray int
	dup
	iconst_0
	bipush 64
	iastore
	dup
	iconst_1
	bipush 34
	iastore
	dup
	iconst_2
	bipush 25
	iastore
	dup
	iconst_3
	bipush 12
	iastore
	dup
	iconst_4
	bipush 22
	iastore
	dup
	iconst_5
	bipush 11
	iastore
	dup
	bipush 6
	bipush 90
	iastore
	astore_1
.var 2 is n I from Label2 to Label3
	bipush 7
	istore_2
	aload_1
	iload_2
	invokestatic MiniGoClass/bubbleSort([II)V
	iconst_0
.var 3 is i I from Label2 to Label3
	istore_3
Label6:
	iload_3
	iload_2
	if_icmpge Label7
	iconst_1
	goto Label8
Label7:
	iconst_0
Label8:
	ifle Label5
Label9:
	aload_1
	iload_3
	iaload
	invokestatic io/putIntLn(I)V
Label10:
Label4:
	iload_3
	iconst_1
	iadd
	istore_3
	goto Label6
Label5:
Label3:
Label1:
	return
.limit stack 15
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
