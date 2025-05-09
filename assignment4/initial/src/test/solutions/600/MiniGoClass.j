.source MiniGoClass.java
.class public MiniGoClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
Label0:
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label2:
.var 1 is queue LQueue; from Label2 to Label3
	new Queue
	dup
	invokespecial Queue/<init>()V
	astore_1
	aload_1
	invokevirtual Queue/initialize()LQueue;
	astore_1
	aload_1
	bipush 10
	invokevirtual Queue/enqueue(I)LQueue;
	astore_1
	aload_1
	bipush 20
	invokevirtual Queue/enqueue(I)LQueue;
	astore_1
	aload_1
	bipush 30
	invokevirtual Queue/enqueue(I)LQueue;
	astore_1
	ldc "Queue items:"
	invokestatic io/putStringLn(Ljava/lang/String;)V
	aload_1
	invokevirtual Queue/display()V
	ldc "Dequeued item:"
	invokestatic io/putStringLn(Ljava/lang/String;)V
	aload_1
	invokevirtual Queue/dequeue()I
	invokestatic io/putIntLn(I)V
	ldc "Queue after dequeue:"
	invokestatic io/putStringLn(Ljava/lang/String;)V
	aload_1
	invokevirtual Queue/display()V
Label3:
Label1:
	return
.limit stack 5
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
