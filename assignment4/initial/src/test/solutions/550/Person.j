.source Person.java
.class public Person
.super java/lang/Object
.field name Ljava/lang/String;
.field age I
.field car LCar;

.method public <init>(Ljava/lang/String;ILCar;)V
.var 0 is this LPerson; from Label0 to Label1
.var 1 is name Ljava/lang/String; from Label0 to Label1
.var 2 is age I from Label0 to Label1
.var 3 is car LCar; from Label0 to Label1
Label0:
	aload_0
	invokespecial java/lang/Object/<init>()V
	aload_0
	aload_1
	putfield Person/name Ljava/lang/String;
	aload_0
	iload_2
	putfield Person/age I
	aload_0
	aload_3
	putfield Person/car LCar;
Label1:
	return
.limit stack 2
.limit locals 4
.end method

.method public <init>()V
.var 0 is this LPerson; from Label0 to Label1
Label0:
	aload_0
	invokespecial java/lang/Object/<init>()V
Label1:
	return
.limit stack 1
.limit locals 1
.end method
