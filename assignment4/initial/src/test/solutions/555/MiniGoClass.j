.source MiniGoClass.java
.class public MiniGoClass
.super java.lang.Object

.method public static binSearch([III)I
Label0:
.var 0 is arr [I from Label0 to Label1
.var 1 is x I from Label0 to Label1
.var 2 is n I from Label0 to Label1
Label2:
	iconst_0
.var 3 is l I from Label2 to Label3
	istore_3
	iload_2
	iconst_1
	isub
.var 4 is h I from Label2 to Label3
	istore 4
Label4:
	iload_3
	iload 4
	if_icmpgt Label6
	iconst_1
	goto Label7
Label6:
	iconst_0
Label7:
	ifle Label5
Label8:
	iload_3
	iload 4
	iload_3
	isub
	iconst_2
	idiv
	iadd
.var 5 is m I from Label8 to Label9
	istore 5
	aload_0
	iload 5
	iaload
	iload_1
	if_icmpne Label12
	iconst_1
	goto Label13
Label12:
	iconst_0
Label13:
	ifle Label10
Label14:
	iload 5
	ireturn
Label15:
Label10:
	aload_0
	iload 5
	iaload
	iload_1
	if_icmpge Label18
	iconst_1
	goto Label19
Label18:
	iconst_0
Label19:
	ifle Label16
Label20:
	iload 5
	iconst_1
	iadd
	istore_3
Label21:
	goto Label17
Label16:
Label22:
	iload 5
	iconst_1
	isub
	istore 4
Label23:
Label17:
Label9:
	goto Label4
Label5:
	iconst_1
	ineg
	ireturn
Label3:
Label1:
.limit stack 13
.limit locals 6
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
	dup
	iconst_3
	iconst_4
	iastore
	dup
	iconst_4
	iconst_5
	iastore
	dup
	iconst_5
	bipush 6
	iastore
	dup
	bipush 6
	bipush 7
	iastore
	dup
	bipush 7
	bipush 8
	iastore
	dup
	bipush 8
	bipush 9
	iastore
	dup
	bipush 9
	bipush 10
	iastore
	astore_1
.var 2 is x I from Label2 to Label3
	iconst_5
	istore_2
.var 3 is result I from Label2 to Label3
	aload_1
	iload_2
	bipush 10
	invokestatic MiniGoClass/binSearch([III)I
	istore_3
	iload_3
	invokestatic io/putIntLn(I)V
Label3:
Label1:
	return
.limit stack 16
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
