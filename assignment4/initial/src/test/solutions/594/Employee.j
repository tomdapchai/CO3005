.source Employee.java
.class public Employee
.super java/lang/Object
.field name Ljava/lang/String;
.field id I

.method public <init>(Ljava/lang/String;I)V
.var 0 is this LEmployee; from Label0 to Label1
.var 1 is name Ljava/lang/String; from Label0 to Label1
.var 2 is id I from Label0 to Label1
Label0:
	aload_0
	invokespecial java/lang/Object/<init>()V
	aload_0
	aload_1
	putfield Employee/name Ljava/lang/String;
	aload_0
	iload_2
	putfield Employee/id I
Label1:
	return
.limit stack 2
.limit locals 3
.end method

.method public <init>()V
.var 0 is this LEmployee; from Label0 to Label1
Label0:
	aload_0
	invokespecial java/lang/Object/<init>()V
Label1:
	return
.limit stack 1
.limit locals 1
.end method
