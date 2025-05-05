.source Test.java
.class public Test
.super java/lang/Object
.field x LTest1;

.method public <init>(LTest1;)V
.var 0 is this LTest; from Label0 to Label1
.var 1 is x LTest1; from Label0 to Label1
Label0:
	aload_0
	invokespecial java/lang/Object/<init>()V
	aload_0
	aload_1
	putfield Test/x LTest1;
Label1:
	return
.limit stack 2
.limit locals 2
.end method

.method public <init>()V
.var 0 is this LTest; from Label0 to Label1
Label0:
	aload_0
	invokespecial java/lang/Object/<init>()V
Label1:
	return
.limit stack 1
.limit locals 1
.end method
