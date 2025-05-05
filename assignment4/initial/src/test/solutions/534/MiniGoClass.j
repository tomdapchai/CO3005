.source MiniGoClass.java
.class public MiniGoClass
.super java.lang.Object
.field static a LTest;

.method public static main([Ljava/lang/String;)V
Label0:
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label2:
	getstatic MiniGoClass/a LTest;
	bipush 20
	putfield Test/x I
	getstatic MiniGoClass/a LTest;
	getfield Test/x I
	invokestatic io/putIntLn(I)V
	getstatic MiniGoClass/a LTest;
	bipush 30
	putfield Test/x I
	getstatic MiniGoClass/a LTest;
	getfield Test/x I
	invokestatic io/putIntLn(I)V
.var 1 is n I from Label2 to Label3
	iconst_0
	istore_1
	bipush 20
	istore_1
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
	new Test
	dup
	invokespecial Test/<init>()V
	putstatic MiniGoClass/a LTest;
Label1:
	return
.limit stack 2
.limit locals 0
.end method
