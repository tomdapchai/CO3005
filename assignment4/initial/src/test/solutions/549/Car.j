.source Car.java
.class public Car
.super java/lang/Object
.field year I
.field brand Ljava/lang/String;

.method public <init>(ILjava/lang/String;)V
.var 0 is this LCar; from Label0 to Label1
.var 1 is year I from Label0 to Label1
.var 2 is brand Ljava/lang/String; from Label0 to Label1
Label0:
	aload_0
	invokespecial java/lang/Object/<init>()V
	aload_0
	iload_1
	putfield Car/year I
	aload_0
	aload_2
	putfield Car/brand Ljava/lang/String;
Label1:
	return
.limit stack 2
.limit locals 3
.end method

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

.method public print()V
.var 0 is this LCar; from Label0 to Label1
Label0:
Label2:
	aload_0
	getfield Car/brand Ljava/lang/String;
	invokestatic io/putStringLn(Ljava/lang/String;)V
	aload_0
	getfield Car/year I
	invokestatic io/putIntLn(I)V
Label3:
Label1:
	return
.limit stack 1
.limit locals 1
.end method
