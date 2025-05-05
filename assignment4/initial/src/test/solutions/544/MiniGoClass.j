.source MiniGoClass.java
.class public MiniGoClass
.super java.lang.Object

.method public static foo(LPerson;I)V
Label0:
.var 0 is p LPerson; from Label0 to Label1
.var 1 is a I from Label0 to Label1
Label2:
	aload_0
	ldc "Hello"
	putfield Person/name Ljava/lang/String;
Label3:
Label1:
	return
.limit stack 2
.limit locals 2
.end method

.method public static main([Ljava/lang/String;)V
Label0:
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label2:
.var 1 is p LPerson; from Label2 to Label3
	new Person
	dup
	ldc "John"
	bipush 30
	ldc 177.3
	invokespecial Person/<init>(Ljava/lang/String;IF)V
	astore_1
	aload_1
	bipush 10
	invokestatic MiniGoClass/foo(LPerson;I)V
	aload_1
	getfield Person/name Ljava/lang/String;
	invokestatic io/putStringLn(Ljava/lang/String;)V
Label3:
Label1:
	return
.limit stack 6
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
