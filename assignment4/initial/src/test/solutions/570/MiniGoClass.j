.source MiniGoClass.java
.class public MiniGoClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
Label0:
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label2:
.var 1 is a I from Label2 to Label3
	bipush 10
	istore_1
.var 2 is b F from Label2 to Label3
	ldc 20.5
	fstore_2
.var 3 is c Ljava/lang/String; from Label2 to Label3
	ldc "Test"
	astore_3
.var 4 is d Z from Label2 to Label3
	iconst_0
	istore 4
	iload_1
	invokestatic io/putInt(I)V
	invokestatic io/putLn()V
	fload_2
	invokestatic io/putFloat(F)V
	invokestatic io/putLn()V
	aload_3
	invokestatic io/putString(Ljava/lang/String;)V
	invokestatic io/putLn()V
	iload 4
	invokestatic io/putBool(Z)V
Label3:
Label1:
	return
.limit stack 2
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
