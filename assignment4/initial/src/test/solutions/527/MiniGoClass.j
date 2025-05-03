.source MiniGoClass.java
.class public MiniGoClass
.super java.lang.Object

.method public static foo(ILjava/lang/String;F)LPerson;
Label0:
.var 0 is a I from Label0 to Label1
.var 1 is n Ljava/lang/String; from Label0 to Label1
.var 2 is h F from Label0 to Label1
Label2:
.var 3 is k LPerson; from Label2 to Label3
	new Person
	dup
	aload_1
	iload_0
	fload_2
	invokespecial Person/<init>(Ljava/lang/String;IF)V
	astore_3
	aload_3
	areturn
Label3:
Label1:
.limit stack 5
.limit locals 4
.end method

.method public static main([Ljava/lang/String;)V
Label0:
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label2:
.var 1 is x LPerson; from Label2 to Label3
	bipush 30
	ldc "John"
	ldc 177.3
	invokestatic MiniGoClass/foo(ILjava/lang/String;F)LPerson;
	astore_1
	aload_1
	getfield Person/age I
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
Label1:
	return
.limit stack 0
.limit locals 0
.end method
