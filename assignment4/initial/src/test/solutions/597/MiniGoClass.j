.source MiniGoClass.java
.class public MiniGoClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
Label0:
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label2:
.var 1 is c LCalculator; from Label2 to Label3
	new Calculator
	dup
	ldc "MyCalc"
	iconst_0
	invokespecial Calculator/<init>(Ljava/lang/String;I)V
	astore_1
.var 2 is a LAdder; from Label2 to Label3
	aload_1
	astore_2
	aload_2
	bipush 10
	bipush 20
	invokeinterface Adder/add(II)I 3
	invokestatic io/putIntLn(I)V
	aload_1
	getfield Calculator/name Ljava/lang/String;
	invokestatic io/putStringLn(Ljava/lang/String;)V
Label3:
Label1:
	return
.limit stack 5
.limit locals 3
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
