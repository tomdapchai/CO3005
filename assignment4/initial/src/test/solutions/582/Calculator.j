.source Calculator.java
.class public Calculator
.super java/lang/Object
.field value I

.method public <init>(I)V
.var 0 is this LCalculator; from Label0 to Label1
.var 1 is value I from Label0 to Label1
Label0:
	aload_0
	invokespecial java/lang/Object/<init>()V
	aload_0
	iload_1
	putfield Calculator/value I
Label1:
	return
.limit stack 2
.limit locals 2
.end method

.method public <init>()V
.var 0 is this LCalculator; from Label0 to Label1
Label0:
	aload_0
	invokespecial java/lang/Object/<init>()V
Label1:
	return
.limit stack 1
.limit locals 1
.end method

.method public add(I)LCalculator;
.var 0 is this LCalculator; from Label0 to Label1
Label0:
.var 1 is x I from Label0 to Label1
Label2:
	aload_0
	aload_0
	getfield Calculator/value I
	iload_1
	iadd
	putfield Calculator/value I
	aload_0
	areturn
Label3:
Label1:
.limit stack 3
.limit locals 2
.end method

.method public multiply(I)LCalculator;
.var 0 is this LCalculator; from Label0 to Label1
Label0:
.var 1 is x I from Label0 to Label1
Label2:
	aload_0
	aload_0
	getfield Calculator/value I
	iload_1
	imul
	putfield Calculator/value I
	aload_0
	areturn
Label3:
Label1:
.limit stack 3
.limit locals 2
.end method

.method public getValue()I
.var 0 is this LCalculator; from Label0 to Label1
Label0:
Label2:
	aload_0
	getfield Calculator/value I
	ireturn
Label3:
Label1:
.limit stack 1
.limit locals 1
.end method
