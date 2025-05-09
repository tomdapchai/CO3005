.source MiniGoClass.java
.class public MiniGoClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
Label0:
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label2:
	ldc "Testing boolean conditions:"
	invokestatic io/putStringLn(Ljava/lang/String;)V
.var 1 is a Z from Label2 to Label3
	iconst_1
	istore_1
.var 2 is b Z from Label2 to Label3
	iconst_0
	istore_2
	ldc "a && b: "
	invokestatic io/putString(Ljava/lang/String;)V
	iload_1
	ifle Label5
	iload_2
	ifle Label5
	iconst_1
	goto Label4
Label5:
	iconst_0
Label4:
	invokestatic io/putBoolLn(Z)V
	ldc "a || b: "
	invokestatic io/putString(Ljava/lang/String;)V
	iload_1
	ifgt Label7
	iload_2
	ifgt Label7
	iconst_0
	goto Label6
Label7:
	iconst_1
Label6:
	invokestatic io/putBoolLn(Z)V
	ldc "!a: "
	invokestatic io/putString(Ljava/lang/String;)V
	iload_1
	ifgt Label8
	iconst_1
	goto Label9
Label8:
	iconst_0
Label9:
	invokestatic io/putBoolLn(Z)V
	ldc "!b: "
	invokestatic io/putString(Ljava/lang/String;)V
	iload_2
	ifgt Label10
	iconst_1
	goto Label11
Label10:
	iconst_0
Label11:
	invokestatic io/putBoolLn(Z)V
Label3:
Label1:
	return
.limit stack 5
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
