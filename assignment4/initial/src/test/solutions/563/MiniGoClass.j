.source MiniGoClass.java
.class public MiniGoClass
.super java.lang.Object

.method public static work()Z
Label0:
Label2:
	ldc "Short-circuit evaluation works!"
	invokestatic io/putStringLn(Ljava/lang/String;)V
	iconst_1
	ireturn
Label3:
Label1:
.limit stack 1
.limit locals 0
.end method

.method public static notwork()Z
Label0:
Label2:
	ldc "Short-circuit evaluation doesn't work!"
	invokestatic io/putStringLn(Ljava/lang/String;)V
	iconst_0
	ireturn
Label3:
Label1:
.limit stack 1
.limit locals 0
.end method

.method public static main([Ljava/lang/String;)V
Label0:
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label2:
.var 1 is a I from Label2 to Label3
	iconst_5
	istore_1
.var 2 is b I from Label2 to Label3
	bipush 10
	istore_2
	invokestatic MiniGoClass/work()Z
	ifgt Label7
	invokestatic MiniGoClass/notwork()Z
	ifgt Label7
	iconst_0
	goto Label6
Label7:
	iconst_1
Label6:
	ifle Label4
Label8:
	iconst_2
	istore_1
Label9:
Label4:
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
