.source MiniGoClass.java
.class public MiniGoClass
.super java.lang.Object

.method public static foo()LPerson;
Label0:
Label2:
.var 0 is k LPerson; from Label2 to Label3
	new Person
	dup
	ldc "Doe"
	bipush 25
	ldc 180.5
	invokespecial Person/<init>(Ljava/lang/String;IF)V
	astore_0
	aload_0
	areturn
Label3:
Label1:
.limit stack 5
.limit locals 1
.end method

.method public static main([Ljava/lang/String;)V
Label0:
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label2:
.var 1 is x LPerson; from Label2 to Label3
	new Person
	dup
	ldc "John"
	bipush 30
	ldc 177.3
	invokespecial Person/<init>(Ljava/lang/String;IF)V
	astore_1
	aload_1
	getfield Person/age I
	invokestatic io/putIntLn(I)V
	aload_1
	getfield Person/height F
	invokestatic io/putFloatLn(F)V
	aload_1
	getfield Person/name Ljava/lang/String;
	invokestatic io/putStringLn(Ljava/lang/String;)V
.var 2 is y I from Label2 to Label3
	invokestatic MiniGoClass/foo()LPerson;
	getfield Person/age I
	istore_2
	iload_2
	invokestatic io/putIntLn(I)V
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
