.source Test1.java
.class public Test1
.super java/lang/Object
.field y LTest2;

.method public <init>(LTest2;)V
.var 0 is this LTest1; from Label0 to Label1
.var 1 is y LTest2; from Label0 to Label1
Label0:
	aload_0
	invokespecial java/lang/Object/<init>()V
	aload_0
	aload_1
	putfield Test1/y LTest2;
Label1:
	return
.limit stack 2
.limit locals 2
.end method

.method public <init>()V
.var 0 is this LTest1; from Label0 to Label1
Label0:
	aload_0
	invokespecial java/lang/Object/<init>()V
Label1:
	return
.limit stack 1
.limit locals 1
.end method
