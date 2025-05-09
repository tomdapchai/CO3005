.source MiniGoClass.java
.class public MiniGoClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
Label0:
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label2:
.var 1 is arr [I from Label2 to Label3
	iconst_5
	newarray int
	dup
	iconst_0
	bipush 10
	iastore
	dup
	iconst_1
	bipush 20
	iastore
	dup
	iconst_2
	bipush 30
	iastore
	dup
	iconst_3
	bipush 40
	iastore
	dup
	iconst_4
	bipush 50
	iastore
	astore_1
	iconst_0
.var 2 is i I from Label2 to Label3
	istore_2
Label6:
	iload_2
	iconst_5
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
	iload_2
	iconst_4
	if_icmpge Label13
	iconst_1
	goto Label14
Label13:
	iconst_0
Label14:
	ifle Label11
Label15:
	ldc ", "
	invokestatic io/putString(Ljava/lang/String;)V
Label16:
Label11:
Label10:
Label4:
	iload_2
	iconst_1
	iadd
	istore_2
	goto Label6
Label5:
	invokestatic io/putLn()V
.var 3 is total I from Label2 to Label3
	iconst_0
	istore_3
	iconst_0
.var 4 is i I from Label2 to Label3
	istore 4
Label19:
	iload 4
	iconst_5
	if_icmpge Label20
	iconst_1
	goto Label21
Label20:
	iconst_0
Label21:
	ifle Label18
Label22:
	iload_3
	aload_1
	iload 4
	iaload
	iadd
	istore_3
Label23:
Label17:
	iload 4
	iconst_1
	iadd
	istore 4
	goto Label19
Label18:
	ldc "Total: "
	invokestatic io/putString(Ljava/lang/String;)V
	iload_3
	invokestatic io/putInt(I)V
Label3:
Label1:
	return
.limit stack 22
.limit locals 5
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
