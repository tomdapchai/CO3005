.source MiniGoClass.java
.class public MiniGoClass
.super java.lang.Object
.field static final a I = 200
.field static y F = 15.5

.method public static main([Ljava/lang/String;)V
Label0:
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label2:
	getstatic MiniGoClass/y F
	bipush 16
	i2f
	fcmpl
	iflt Label6
	iconst_1
	goto Label7
Label6:
	iconst_0
Label7:
	ifle Label4
Label8:
	getstatic MiniGoClass/a I
	invokestatic MiniGoClass/foo()I
	iadd
	invokestatic io/putInt(I)V
Label9:
	goto Label5
Label4:
Label10:
	getstatic MiniGoClass/a I
	bipush 10
	iadd
	sipush 211
	if_icmplt Label14
	iconst_1
	goto Label15
Label14:
	iconst_0
Label15:
	ifle Label12
Label16:
	sipush 234
	invokestatic io/putIntLn(I)V
Label17:
	goto Label13
Label12:
Label18:
.var 1 is x I from Label18 to Label19
	iconst_5
	istore_1
Label20:
	iload_1
	bipush 10
	if_icmpge Label22
	iconst_1
	goto Label23
Label22:
	iconst_0
Label23:
	ifle Label21
Label24:
	sipush 567
	invokestatic io/putIntLn(I)V
	iload_1
	iconst_1
	iadd
	istore_1
Label25:
	goto Label20
Label21:
Label19:
Label13:
	getstatic MiniGoClass/a I
	invokestatic MiniGoClass/foo()I
	iadd
	iconst_1
	iadd
	invokestatic io/putInt(I)V
Label11:
Label5:
	iconst_0
.var 1 is i I from Label2 to Label3
	istore_1
Label28:
	iload_1
	bipush 10
	if_icmpge Label29
	iconst_1
	goto Label30
Label29:
	iconst_0
Label30:
	ifle Label27
Label31:
	iload_1
	iconst_4
	if_icmpgt Label35
	iconst_1
	goto Label36
Label35:
	iconst_0
Label36:
	ifle Label33
Label37:
	invokestatic MiniGoClass/foo()I
	iconst_2
	if_icmple Label41
	iconst_1
	goto Label42
Label41:
	iconst_0
Label42:
	ifle Label46
	iload_1
	iconst_3
	if_icmpge Label43
	iconst_1
	goto Label44
Label43:
	iconst_0
Label44:
	ifle Label46
	iconst_1
	goto Label45
Label46:
	iconst_0
Label45:
	ifle Label39
Label47:
	goto Label26
Label48:
Label39:
Label38:
Label33:
	iload_1
	invokestatic io/putInt(I)V
	iload_1
	bipush 8
	if_icmpne Label51
	iconst_1
	goto Label52
Label51:
	iconst_0
Label52:
	ifle Label49
Label53:
	goto Label27
Label54:
Label49:
Label32:
Label26:
	iload_1
	iconst_1
	iadd
	istore_1
	goto Label28
Label27:
Label3:
Label1:
	return
.limit stack 35
.limit locals 2
.end method

.method public static foo()I
Label0:
Label2:
	iconst_1
	iconst_2
	iadd
	ireturn
Label3:
Label1:
.limit stack 4
.limit locals 0
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
