.source Innner.java
.class public Innner
.super java/lang/Object
.field id I
.field value F

.method public <init>(IF)V
.var 0 is this LInnner; from Label0 to Label1
.var 1 is id I from Label0 to Label1
.var 2 is value F from Label0 to Label1
Label0:
	aload_0
	invokespecial java/lang/Object/<init>()V
	aload_0
	iload_1
	putfield Innner/id I
	aload_0
	fload_2
	putfield Innner/value F
Label1:
	return
.limit stack 2
.limit locals 3
.end method

.method public <init>()V
.var 0 is this LInnner; from Label0 to Label1
Label0:
	aload_0
	invokespecial java/lang/Object/<init>()V
Label1:
	return
.limit stack 1
.limit locals 1
.end method
