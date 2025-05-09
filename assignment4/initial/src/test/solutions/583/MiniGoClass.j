.source MiniGoClass.java
.class public MiniGoClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
Label0:
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label2:
.var 1 is myCar LCar; from Label2 to Label3
	new Car
	dup
	ldc "Toyota"
	ldc "Camry"
	sipush 2023
	iconst_2
	anewarray java/lang/String
	dup
	iconst_0
	ldc "GPS"
	aastore
	dup
	iconst_1
	ldc "Bluetooth"
	aastore
	invokespecial Car/<init>(Ljava/lang/String;Ljava/lang/String;I[Ljava/lang/String;)V
	astore_1
	aload_1
	getfield Car/brand Ljava/lang/String;
	invokestatic io/putStringLn(Ljava/lang/String;)V
	aload_1
	getfield Car/model Ljava/lang/String;
	invokestatic io/putStringLn(Ljava/lang/String;)V
	aload_1
	getfield Car/year I
	invokestatic io/putIntLn(I)V
	aload_1
	getfield Car/features [Ljava/lang/String;
	iconst_0
	aaload
	ldc ", "
	invokevirtual java/lang/String/concat(Ljava/lang/String;)Ljava/lang/String;
	aload_1
	getfield Car/features [Ljava/lang/String;
	iconst_1
	aaload
	invokevirtual java/lang/String/concat(Ljava/lang/String;)Ljava/lang/String;
	invokestatic io/putStringLn(Ljava/lang/String;)V
Label3:
Label1:
	return
.limit stack 11
.limit locals 2
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
