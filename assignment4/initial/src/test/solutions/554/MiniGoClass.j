.source MiniGoClass.java
.class public MiniGoClass
.super java.lang.Object
.field static final MAX I = 10

.method public static arrsort([I)V
Label0:
.var 0 is arr [I from Label0 to Label1
Label2:
	iconst_0
.var 1 is i I from Label2 to Label3
	istore_1
Label6:
	iload_1
	getstatic MiniGoClass/MAX I
	if_icmpge Label7
	iconst_1
	goto Label8
Label7:
	iconst_0
Label8:
	ifle Label5
Label9:
	iconst_0
.var 2 is j I from Label9 to Label10
	istore_2
Label13:
	iload_2
	iload_1
	if_icmpge Label14
	iconst_1
	goto Label15
Label14:
	iconst_0
Label15:
	ifle Label12
Label16:
	aload_0
	iload_1
	iaload
	aload_0
	iload_2
	iaload
	if_icmpge Label20
	iconst_1
	goto Label21
Label20:
	iconst_0
Label21:
	ifle Label18
Label22:
.var 3 is temp I from Label22 to Label23
	aload_0
	iload_1
	iaload
	istore_3
	aload_0
	iload_1
	aload_0
	iload_2
	iaload
	iastore
	aload_0
	iload_2
	iload_3
	iastore
Label23:
Label18:
Label17:
Label11:
	iload_2
	iconst_1
	iadd
	istore_2
	goto Label13
Label12:
Label10:
Label4:
	iload_1
	iconst_1
	iadd
	istore_1
	goto Label6
Label5:
Label3:
Label1:
	return
.limit stack 12
.limit locals 4
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
	invokestatic MiniGoClass/arrsort([I)V
	iconst_0
.var 2 is i I from Label2 to Label3
	istore_2
Label6:
	iload_2
	getstatic MiniGoClass/MAX I
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
	invokestatic io/putInt(I)V
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
.limit stack 16
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
