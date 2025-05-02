.source Person.java
.class public Person
.super java/lang/Object
.field name Ljava/lang/String;
.field age I

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

.method public static foo()V
Label0:
Label2:
.var 0 is x I from Label2 to Label3
	bipush 10
	istore_0
Label3:
Label1:
	return
.limit stack 2
.limit locals 1
.end method
