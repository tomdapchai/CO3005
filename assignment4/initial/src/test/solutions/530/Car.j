.source Car.java
.class public Car
.super java/lang/Object
.field name Ljava/lang/String;
.field year I

.method public <init>(Ljava/lang/String;I)V
.var 0 is this LCar; from Label0 to Label1
.var 1 is name Ljava/lang/String; from Label0 to Label1
.var 2 is year I from Label0 to Label1
Label0:
	aload_0
	invokespecial java/lang/Object/<init>()V
	aload_0
	aload_1
	putfield Car/name Ljava/lang/String;
	aload_0
	iload_2
	putfield Car/year I
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

.method public init(Ljava/lang/String;I)LCar;
.var 0 is this LCar; from Label0 to Label1
Label0:
.var 1 is name Ljava/lang/String; from Label0 to Label1
.var 2 is year I from Label0 to Label1
Label2:
	new Car
	dup
	aload_1
	iload_2
	invokespecial Car/<init>(Ljava/lang/String;I)V
	areturn
Label3:
Label1:
.limit stack 4
.limit locals 3
.end method

.method public print()V
.var 0 is this LCar; from Label0 to Label1
Label0:
Label2:
	aload_0
	getfield Car/name Ljava/lang/String;
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
