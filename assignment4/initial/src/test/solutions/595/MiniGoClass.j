.source MiniGoClass.java
.class public MiniGoClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
Label0:
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label2:
.var 1 is x I from Label2 to Label3
	bipush 10
	istore_1
	iload_1
	invokestatic io/putIntLn(I)V
	bipush 20
	istore_1
	bipush 30
	istore_1
	iload_1
	invokestatic io/putIntLn(I)V
	iload_1
	invokestatic io/putIntLn(I)V
	iload_1
	invokestatic io/putIntLn(I)V
Label3:
Label1:
	return
.limit stack 4
.limit locals 2
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
