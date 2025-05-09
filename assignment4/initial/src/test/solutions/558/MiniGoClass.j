.source MiniGoClass.java
.class public MiniGoClass
.super java.lang.Object

.method public static gcd(II)I
Label0:
.var 0 is a I from Label0 to Label1
.var 1 is b I from Label0 to Label1
Label2:
Label4:
	iload_1
	iconst_0
	if_icmpeq Label6
	iconst_1
	goto Label7
Label6:
	iconst_0
Label7:
	ifle Label5
Label8:
	iload_1
.var 2 is temp I from Label8 to Label9
	istore_2
	iload_0
	iload_1
	irem
	istore_1
	iload_2
	istore_0
Label9:
	goto Label4
Label5:
	iload_0
	ireturn
Label3:
Label1:
.limit stack 5
.limit locals 3
.end method

.method public static main([Ljava/lang/String;)V
Label0:
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label2:
.var 1 is a I from Label2 to Label3
	bipush 56
	istore_1
.var 2 is b I from Label2 to Label3
	bipush 98
	istore_2
.var 3 is result I from Label2 to Label3
	iload_1
	iload_2
	invokestatic MiniGoClass/gcd(II)I
	istore_3
	iload_3
	invokestatic io/putIntLn(I)V
Label3:
Label1:
	return
.limit stack 4
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
