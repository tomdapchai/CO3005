.source MiniGoClass.java
.class public MiniGoClass
.super java.lang.Object
.field static final size I = 3

.method public static main([Ljava/lang/String;)V
Label0:
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label2:
.var 1 is a Ljava/lang/String; from Label2 to Label3
	ldc "b"
	astore_1
	aload_1
	invokestatic MiniGoClass/foo(Ljava/lang/String;)Z
	invokestatic io/putBoolLn(Z)V
Label3:
Label1:
	return
.limit stack 1
.limit locals 2
.end method

.method public static foo(Ljava/lang/String;)Z
Label0:
.var 0 is a Ljava/lang/String; from Label0 to Label1
Label2:
	aload_0
	ldc "a"
	invokevirtual java/lang/String/compareTo(Ljava/lang/String;)I
	ifle Label4
	iconst_1
	goto Label5
Label4:
	iconst_0
Label5:
	ireturn
Label3:
Label1:
.limit stack 4
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
