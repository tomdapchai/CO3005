.source MiniGoClass.java
.class public MiniGoClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
Label0:
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label2:
.var 1 is calc LCalculator; from Label2 to Label3
	new Calculator
	dup
	iconst_5
	invokespecial Calculator/<init>(I)V
	astore_1
	aload_1
	bipush 10
	invokevirtual Calculator/add(I)LCalculator;
	iconst_2
	invokevirtual Calculator/multiply(I)LCalculator;
	invokevirtual Calculator/getValue()I
	invokestatic io/putIntLn(I)V
Label3:
Label1:
	return
.limit stack 5
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
