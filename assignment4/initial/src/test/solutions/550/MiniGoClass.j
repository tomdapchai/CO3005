.source MiniGoClass.java
.class public MiniGoClass
.super java.lang.Object
.field static arr [LPerson;

.method public static main([Ljava/lang/String;)V
Label0:
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label2:
	iconst_3
	anewarray Person
	dup
	iconst_0
	new Person
	dup
	ldc "Doe"
	bipush 25
	new Car
	dup
	sipush 2021
	ldc "Honda"
	invokespecial Car/<init>(ILjava/lang/String;)V
	invokespecial Person/<init>(Ljava/lang/String;ILCar;)V
	aastore
	dup
	iconst_1
	new Person
	dup
	ldc "Jane"
	bipush 28
	new Car
	dup
	sipush 2022
	ldc "Ford"
	invokespecial Car/<init>(ILjava/lang/String;)V
	invokespecial Person/<init>(Ljava/lang/String;ILCar;)V
	aastore
	dup
	iconst_2
	new Person
	dup
	ldc "Smith"
	bipush 35
	new Car
	dup
	sipush 2023
	ldc "BMW"
	invokespecial Car/<init>(ILjava/lang/String;)V
	invokespecial Person/<init>(Ljava/lang/String;ILCar;)V
	aastore
	putstatic MiniGoClass/arr [LPerson;
	getstatic MiniGoClass/arr [LPerson;
	iconst_0
	aaload
	getfield Person/car LCar;
	invokevirtual Car/print()V
Label3:
Label1:
	return
.limit stack 18
.limit locals 1
.end method

.method public <init>()V
.var 0 is this LMiniGoClass; from Label0 to Label1
Label0:
	aload_0
	invokespecial java/lang/Object/<init>()V
Label1:
	return
.limit stack 1
.limit locals 1
.end method

.method public static <clinit>()V
Label0:
Label1:
	return
.limit stack 0
.limit locals 0
.end method
