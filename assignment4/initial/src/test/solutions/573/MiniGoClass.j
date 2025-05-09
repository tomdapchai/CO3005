.source MiniGoClass.java
.class public MiniGoClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
Label0:
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label2:
	ldc "Nested functions:"
	invokestatic io/putStringLn(Ljava/lang/String;)V
	iconst_5
	invokestatic MiniGoClass/outer(I)I
	invokestatic io/putIntLn(I)V
Label3:
Label1:
	return
.limit stack 2
.limit locals 1
.end method

.method public static outer(I)I
Label0:
.var 0 is x I from Label0 to Label1
Label2:
	ldc "  Outer: "
	invokestatic io/putString(Ljava/lang/String;)V
	iload_0
	invokestatic io/putIntLn(I)V
	iload_0
	iconst_2
	imul
	invokestatic MiniGoClass/inner(I)I
	ireturn
Label3:
Label1:
.limit stack 3
.limit locals 1
.end method

.method public static inner(I)I
Label0:
.var 0 is y I from Label0 to Label1
Label2:
	ldc "    Inner: "
	invokestatic io/putString(Ljava/lang/String;)V
	iload_0
	invokestatic io/putIntLn(I)V
	iload_0
	iconst_2
	imul
	ireturn
Label3:
Label1:
.limit stack 3
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
