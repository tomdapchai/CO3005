.source MiniGoClass.java
.class public MiniGoClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
Label0:
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label2:
	ldc "Hello"
	ldc " "
	invokevirtual java/lang/String/concat(Ljava/lang/String;)Ljava/lang/String;
	ldc "World"
	invokevirtual java/lang/String/concat(Ljava/lang/String;)Ljava/lang/String;
	invokestatic io/putString(Ljava/lang/String;)V
	invokestatic io/putLn()V
	bipush 10
	iconst_5
	if_icmple Label4
	iconst_1
	goto Label5
Label4:
	iconst_0
Label5:
	ifle Label9
	bipush 7
	bipush 9
	if_icmpge Label6
	iconst_1
	goto Label7
Label6:
	iconst_0
Label7:
	ifle Label9
	iconst_1
	goto Label8
Label9:
	iconst_0
Label8:
	invokestatic io/putBool(Z)V
Label3:
Label1:
	return
.limit stack 10
.limit locals 1
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
