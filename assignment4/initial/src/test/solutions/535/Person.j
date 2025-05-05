.source Person.java
.class public Person
.super java/lang/Object
.implements IPerson
.field name Ljava/lang/String;
.field age I
.field height F

.method public <init>(Ljava/lang/String;IF)V
.var 0 is this LPerson; from Label0 to Label1
.var 1 is name Ljava/lang/String; from Label0 to Label1
.var 2 is age I from Label0 to Label1
.var 3 is height F from Label0 to Label1
Label0:
	aload_0
	invokespecial java/lang/Object/<init>()V
	aload_0
	aload_1
	putfield Person/name Ljava/lang/String;
	aload_0
	iload_2
	putfield Person/age I
	aload_0
	fload_3
	putfield Person/height F
Label1:
	return
.limit stack 2
.limit locals 4
.end method

.method public <init>()V
.var 0 is this LPerson; from Label0 to Label1
Label0:
	aload_0
	invokespecial java/lang/Object/<init>()V
Label1:
	return
.limit stack 1
.limit locals 1
.end method

.method public init(Ljava/lang/String;IF)LPerson;
.var 0 is this LPerson; from Label0 to Label1
Label0:
.var 1 is name Ljava/lang/String; from Label0 to Label1
.var 2 is age I from Label0 to Label1
.var 3 is height F from Label0 to Label1
Label2:
	new Person
	dup
	aload_1
	iload_2
	fload_3
	invokespecial Person/<init>(Ljava/lang/String;IF)V
	areturn
Label3:
Label1:
.limit stack 5
.limit locals 4
.end method

.method public bar()V
.var 0 is this LPerson; from Label0 to Label1
Label0:
Label2:
	aload_0
	getfield Person/name Ljava/lang/String;
	invokestatic io/putStringLn(Ljava/lang/String;)V
	aload_0
	getfield Person/age I
	invokestatic io/putIntLn(I)V
	aload_0
	getfield Person/height F
	invokestatic io/putFloatLn(F)V
Label3:
Label1:
	return
.limit stack 1
.limit locals 1
.end method
