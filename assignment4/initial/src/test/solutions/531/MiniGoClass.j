.source MiniGoClass.java
.class public MiniGoClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
Label0:
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label2:
.var 1 is x LPerson; from Label2 to Label3
	new Person
	dup
	invokespecial Person/<init>()V
	astore_1
	new Person
	dup
	ldc "John"
	bipush 30
	ldc 177.3
	invokespecial Person/<init>(Ljava/lang/String;IF)V
	astore_1
.var 2 is y LIPerson; from Label2 to Label3
	aload_1
	astore_2
	aload_1
	getfield Person/name Ljava/lang/String;
	invokestatic io/putStringLn(Ljava/lang/String;)V
	aload_2
	invokeinterface IPerson/bar()V 1
Label3:
Label1:
	return
.limit stack 6
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
