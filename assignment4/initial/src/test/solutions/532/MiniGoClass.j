.source MiniGoClass.java
.class public MiniGoClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
Label0:
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label2:
.var 1 is a LTest; from Label2 to Label3
	new Test
	dup
	new Test1
	dup
	new Test2
	dup
	bipush 10
	invokespecial Test2/<init>(I)V
	invokespecial Test1/<init>(LTest2;)V
	invokespecial Test/<init>(LTest1;)V
	astore_1
	aload_1
	getfield Test/x LTest1;
	getfield Test1/y LTest2;
	getfield Test2/z I
	invokestatic io/putIntLn(I)V
	aload_1
	getfield Test/x LTest1;
	getfield Test1/y LTest2;
	bipush 20
	putfield Test2/z I
	aload_1
	getfield Test/x LTest1;
	getfield Test1/y LTest2;
	getfield Test2/z I
	invokestatic io/putIntLn(I)V
Label3:
Label1:
	return
.limit stack 8
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
