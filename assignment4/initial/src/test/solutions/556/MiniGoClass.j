.source MiniGoClass.java
.class public MiniGoClass
.super java.lang.Object

.method public static quickSort([III)V
Label0:
.var 0 is arr [I from Label0 to Label1
.var 1 is low I from Label0 to Label1
.var 2 is high I from Label0 to Label1
Label2:
	iload_1
	iload_2
	if_icmpge Label6
	iconst_1
	goto Label7
Label6:
	iconst_0
Label7:
	ifle Label4
Label8:
	aload_0
	iload_1
	iload_2
	invokestatic MiniGoClass/partition([III)I
.var 3 is pivotIndex I from Label8 to Label9
	istore_3
	aload_0
	iload_1
	iload_3
	iconst_1
	isub
	invokestatic MiniGoClass/quickSort([III)V
	aload_0
	iload_3
	iconst_1
	iadd
	iload_2
	invokestatic MiniGoClass/quickSort([III)V
Label9:
Label4:
Label3:
Label1:
	return
.limit stack 7
.limit locals 4
.end method

.method public static partition([III)I
Label0:
.var 0 is arr [I from Label0 to Label1
.var 1 is low I from Label0 to Label1
.var 2 is high I from Label0 to Label1
Label2:
	aload_0
	iload_2
	iaload
.var 3 is pivot I from Label2 to Label3
	istore_3
	iload_1
	iconst_1
	isub
.var 4 is i I from Label2 to Label3
	istore 4
	iload_1
.var 5 is j I from Label2 to Label3
	istore 5
Label6:
	iload 5
	iload_2
	if_icmpge Label7
	iconst_1
	goto Label8
Label7:
	iconst_0
Label8:
	ifle Label5
Label9:
	aload_0
	iload 5
	iaload
	iload_3
	if_icmpgt Label13
	iconst_1
	goto Label14
Label13:
	iconst_0
Label14:
	ifle Label11
Label15:
	iload 4
	iconst_1
	iadd
	istore 4
	aload_0
	iload 4
	iaload
.var 6 is temp I from Label15 to Label16
	istore 6
	aload_0
	iload 4
	aload_0
	iload 5
	iaload
	iastore
	aload_0
	iload 5
	iload 6
	iastore
Label16:
Label11:
Label10:
Label4:
	iload 5
	iconst_1
	iadd
	istore 5
	goto Label6
Label5:
	aload_0
	iload 4
	iconst_1
	iadd
	iaload
.var 6 is temp I from Label2 to Label3
	istore 6
	aload_0
	iload 4
	iconst_1
	iadd
	aload_0
	iload_2
	iaload
	iastore
	aload_0
	iload_2
	iload 6
	iastore
	iload 4
	iconst_1
	iadd
	ireturn
Label3:
Label1:
.limit stack 13
.limit locals 7
.end method

.method public static main([Ljava/lang/String;)V
Label0:
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label2:
.var 1 is arr [I from Label2 to Label3
	bipush 10
	newarray int
	dup
	iconst_0
	iconst_4
	iastore
	dup
	iconst_1
	iconst_2
	iastore
	dup
	iconst_2
	iconst_3
	iastore
	dup
	iconst_3
	bipush 7
	iastore
	dup
	iconst_4
	bipush 8
	iastore
	dup
	iconst_5
	bipush 9
	iastore
	dup
	bipush 6
	bipush 12
	iastore
	dup
	bipush 7
	bipush 14
	iastore
	dup
	bipush 8
	bipush 15
	iastore
	dup
	bipush 9
	bipush 11
	iastore
	astore_1
	aload_1
	iconst_0
	bipush 9
	invokestatic MiniGoClass/quickSort([III)V
	iconst_0
.var 2 is i I from Label2 to Label3
	istore_2
Label6:
	iload_2
	bipush 10
	if_icmpge Label7
	iconst_1
	goto Label8
Label7:
	iconst_0
Label8:
	ifle Label5
Label9:
	aload_1
	iload_2
	iaload
	invokestatic io/putIntLn(I)V
Label10:
Label4:
	iload_2
	iconst_1
	iadd
	istore_2
	goto Label6
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
