.source Car.java
.class public Car
.super java/lang/Object
.field brand Ljava/lang/String;
.field model Ljava/lang/String;
.field year I
.field features [Ljava/lang/String;

.method public <init>(Ljava/lang/String;Ljava/lang/String;I[Ljava/lang/String;)V
.var 0 is this LCar; from Label0 to Label1
.var 1 is brand Ljava/lang/String; from Label0 to Label1
.var 2 is model Ljava/lang/String; from Label0 to Label1
.var 3 is year I from Label0 to Label1
.var 4 is features [Ljava/lang/String; from Label0 to Label1
Label0:
	aload_0
	invokespecial java/lang/Object/<init>()V
	aload_0
	aload_1
	putfield Car/brand Ljava/lang/String;
	aload_0
	aload_2
	putfield Car/model Ljava/lang/String;
	aload_0
	iload_3
	putfield Car/year I
	aload_0
	aload 4
	putfield Car/features [Ljava/lang/String;
Label1:
	return
.limit stack 2
.limit locals 5
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
