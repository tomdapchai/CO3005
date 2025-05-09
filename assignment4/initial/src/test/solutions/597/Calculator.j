.source Calculator.java
.class public Calculator
.super java/lang/Object
.implements Adder
.field name Ljava/lang/String;
.field age I

.method public <init>(Ljava/lang/String;I)V
.var 0 is this LCalculator; from Label0 to Label1
.var 1 is name Ljava/lang/String; from Label0 to Label1
.var 2 is age I from Label0 to Label1
Label0:
	aload_0
	invokespecial java/lang/Object/<init>()V
	aload_0
	aload_1
	putfield Calculator/name Ljava/lang/String;
	aload_0
	iload_2
	putfield Calculator/age I
Label1:
	return
.limit stack 2
.limit locals 3
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

.method public add(II)I
.var 0 is this LCalculator; from Label0 to Label1
Label0:
.var 1 is a I from Label0 to Label1
.var 2 is b I from Label0 to Label1
Label2:
	iload_1
	iload_2
	iadd
	ireturn
Label3:
Label1:
.limit stack 2
.limit locals 3
.end method
