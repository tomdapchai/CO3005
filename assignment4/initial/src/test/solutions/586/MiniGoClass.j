.source MiniGoClass.java
.class public MiniGoClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
Label0:
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label2:
.var 1 is a Z from Label2 to Label3
	iconst_1
	istore_1
.var 2 is b Z from Label2 to Label3
	iconst_0
	istore_2
.var 3 is c Z from Label2 to Label3
	iconst_1
	istore_3
	iload_1
	ifle Label5
	iload_2
	ifle Label5
	iconst_1
	goto Label4
Label5:
	iconst_0
Label4:
	ifgt Label7
	iload_3
	ifgt Label7
	iconst_0
	goto Label6
Label7:
	iconst_1
Label6:
	invokestatic io/putBoolLn(Z)V
	iload_1
	ifgt Label8
	iconst_1
	goto Label9
Label8:
	iconst_0
Label9:
	ifgt Label13
	iload_2
	ifle Label11
	iload_3
	ifle Label11
	iconst_1
	goto Label10
Label11:
	iconst_0
Label10:
	ifgt Label13
	iconst_0
	goto Label12
Label13:
	iconst_1
Label12:
	invokestatic io/putBoolLn(Z)V
	iload_1
	ifgt Label15
	iload_2
	ifgt Label15
	iconst_0
	goto Label14
Label15:
	iconst_1
Label14:
	ifle Label19
	iload_2
	ifgt Label17
	iload_3
	ifgt Label17
	iconst_0
	goto Label16
Label17:
	iconst_1
Label16:
	ifle Label19
	iconst_1
	goto Label18
Label19:
	iconst_0
Label18:
	invokestatic io/putBoolLn(Z)V
Label3:
Label1:
	return
.limit stack 9
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
