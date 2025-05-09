.source MiniGoClass.java
.class public MiniGoClass
.super java.lang.Object
.field static arr [I

.method public static main([Ljava/lang/String;)V
Label0:
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label2:
	iconst_0
.var 1 is i I from Label2 to Label3
	istore_1
Label6:
	iload_1
	iconst_5
	if_icmpge Label7
	iconst_1
	goto Label8
Label7:
	iconst_0
Label8:
	ifle Label5
Label9:
	getstatic MiniGoClass/arr [I
	iload_1
	iaload
	iconst_2
	irem
	iconst_0
	if_icmpne Label13
	iconst_1
	goto Label14
Label13:
	iconst_0
Label14:
	ifle Label11
Label15:
	getstatic MiniGoClass/arr [I
	iload_1
	iaload
	invokestatic io/putInt(I)V
Label16:
Label11:
Label10:
Label4:
	iload_1
	iconst_1
	iadd
	istore_1
	goto Label6
Label5:
.var 2 is i I from Label2 to Label3
	iconst_0
	istore_2
Label19:
	iload_2
	iconst_5
	if_icmpge Label20
	iconst_1
	goto Label21
Label20:
	iconst_0
Label21:
	ifle Label18
Label22:
	getstatic MiniGoClass/arr [I
	iload_2
	iaload
	iconst_2
	irem
	iconst_0
	if_icmpeq Label26
	iconst_1
	goto Label27
Label26:
	iconst_0
Label27:
	ifle Label24
Label28:
	getstatic MiniGoClass/arr [I
	iload_2
	iaload
	invokestatic io/putInt(I)V
Label29:
Label24:
Label23:
Label17:
	iload_2
	iconst_1
	iadd
	istore_2
	goto Label19
Label18:
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
	iconst_5
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
	putstatic MiniGoClass/arr [I
Label1:
	return
.limit stack 10
.limit locals 0
.end method
