.source Person.java
.class public Person
.super java/lang/Object
.field name Ljava/lang/String;
.field age I

.method public <init>(Ljava/lang/String;I)V
.var 0 is this LPerson; from Label0 to Label1
.var 1 is name Ljava/lang/String; from Label0 to Label1
.var 2 is age I from Label0 to Label1
Label0:
	aload_0
	invokespecial java/lang/Object/<init>()V
	aload_0
	aload_1
	putfield Person/name Ljava/lang/String;
	aload_0
	iload_2
	putfield Person/age I
Label1:
	return
.limit stack 2
.limit locals 3
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

.method public foo()V
.var 0 is this LPerson; from Label0 to Label1
Label0:
Label2:
.var 1 is x I from Label2 to Label3
	bipush 10
	istore_1
Label3:
Label1:
	return
.limit stack 2
.limit locals 2
.end method
