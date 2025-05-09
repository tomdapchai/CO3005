.source Children.java
.class public Children
.super java/lang/Object
.field age I
.field name Ljava/lang/String;

.method public <init>(ILjava/lang/String;)V
.var 0 is this LChildren; from Label0 to Label1
.var 1 is age I from Label0 to Label1
.var 2 is name Ljava/lang/String; from Label0 to Label1
Label0:
	aload_0
	invokespecial java/lang/Object/<init>()V
	aload_0
	iload_1
	putfield Children/age I
	aload_0
	aload_2
	putfield Children/name Ljava/lang/String;
Label1:
	return
.limit stack 2
.limit locals 3
.end method

.method public <init>()V
.var 0 is this LChildren; from Label0 to Label1
Label0:
	aload_0
	invokespecial java/lang/Object/<init>()V
Label1:
	return
.limit stack 1
.limit locals 1
.end method

.method public getChild()V
.var 0 is this LChildren; from Label0 to Label1
Label0:
Label2:
	aload_0
	getfield Children/name Ljava/lang/String;
	invokestatic io/putStringLn(Ljava/lang/String;)V
	aload_0
	getfield Children/age I
	invokestatic io/putIntLn(I)V
Label3:
Label1:
	return
.limit stack 1
.limit locals 1
.end method
