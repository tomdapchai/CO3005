.source MiniGoClass.java
.class public MiniGoClass
.super java.lang.Object

.method public static selectionSort([I)[I
Label0:
.var 0 is arr [I from Label0 to Label1
Label2:
	iconst_0
.var 1 is i I from Label2 to Label3
	istore_1
Label6:
	iload_1
	bipush 10
	iconst_1
	isub
	if_icmpge Label7
	iconst_1
	goto Label8
Label7:
	iconst_0
Label8:
	ifle Label5
Label9:
	iload_1
.var 2 is minIdx I from Label9 to Label10
	istore_2
	iload_1
	iconst_1
	iadd
.var 3 is j I from Label9 to Label10
	istore_3
Label13:
	iload_3
	bipush 10
	if_icmpge Label14
	iconst_1
	goto Label15
Label14:
	iconst_0
Label15:
	ifle Label12
Label16:
	aload_0
	iload_3
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
	iload_3
	istore_2
Label23:
Label18:
Label17:
Label11:
	iload_3
	iconst_1
	iadd
	istore_3
	goto Label13
Label12:
	iload_2
	iload_1
	if_icmpeq Label26
	iconst_1
	goto Label27
Label26:
	iconst_0
Label27:
	ifle Label24
Label28:
	aload_0
	iload_1
	iaload
.var 4 is temp I from Label28 to Label29
	istore 4
	aload_0
	iload_1
	aload_0
	iload_2
	iaload
	iastore
	aload_0
	iload_2
	iload 4
	iastore
Label29:
Label24:
Label10:
Label4:
	iload_1
	iconst_1
	iadd
	istore_1
	goto Label6
Label5:
	aload_0
	areturn
Label3:
Label1:
.limit stack 17
.limit locals 5
.end method

.method public static main([Ljava/lang/String;)V
Label0:
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label2:
.var 1 is numbers [I from Label2 to Label3
	bipush 10
	newarray int
	dup
	iconst_0
	bipush 9
	iastore
	dup
	iconst_1
	iconst_3
	iastore
	dup
	iconst_2
	iconst_5
	iastore
	dup
	iconst_3
	iconst_1
	iastore
	dup
	iconst_4
	bipush 8
	iastore
	dup
	iconst_5
	iconst_2
	iastore
	dup
	bipush 6
	iconst_4
	iastore
	dup
	bipush 7
	bipush 7
	iastore
	dup
	bipush 8
	bipush 6
	iastore
	dup
	bipush 9
	iconst_0
	iastore
	astore_1
.var 2 is sorted [I from Label2 to Label3
	aload_1
	invokestatic MiniGoClass/selectionSort([I)[I
	astore_2
	iconst_0
.var 3 is i I from Label2 to Label3
	istore_3
Label6:
	iload_3
	bipush 10
	if_icmpge Label7
	iconst_1
	goto Label8
Label7:
	iconst_0
Label8:
	ifle Label5
Label9:
	aload_2
	iload_3
	iaload
	invokestatic io/putInt(I)V
	ldc " "
	invokestatic io/putString(Ljava/lang/String;)V
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
.limit stack 18
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
