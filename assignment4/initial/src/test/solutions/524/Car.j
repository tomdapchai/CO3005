.source Car.java
.class public Car
.super java/lang/Object
.field static name Ljava/lang/String;
.field static age I

.method public <init>()V
.var 0 is this LCar; from Label0 to Label1
Label0:
	aload_0
	invokespecial java/lang/Object/<init>()V
Label1:
	return
.limit stack 1
.limit locals 1
.end method

.method public static foo1()V
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
