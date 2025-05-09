.source MiniGoClass.java
.class public MiniGoClass
.super java.lang.Object

.method public static printShapeInfo(LShape;)V
Label0:
.var 0 is s LShape; from Label0 to Label1
Label2:
	aload_0
	invokeinterface Shape/area()F 1
	invokestatic io/putFloatLn(F)V
	aload_0
	invokeinterface Shape/perimeter()F 1
	invokestatic io/putFloatLn(F)V
Label3:
Label1:
	return
.limit stack 1
.limit locals 1
.end method

.method public static main([Ljava/lang/String;)V
Label0:
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label2:
.var 1 is r LShape; from Label2 to Label3
	new Rectangle
	dup
	ldc 5.0
	ldc 3.0
	invokespecial Rectangle/<init>(FF)V
	astore_1
.var 2 is c LShape; from Label2 to Label3
	new Circle
	dup
	ldc 2.0
	invokespecial Circle/<init>(F)V
	astore_2
	ldc "Rectangle:"
	invokestatic io/putStringLn(Ljava/lang/String;)V
	aload_1
	invokestatic MiniGoClass/printShapeInfo(LShape;)V
	ldc "Circle:"
	invokestatic io/putStringLn(Ljava/lang/String;)V
	aload_2
	invokestatic MiniGoClass/printShapeInfo(LShape;)V
Label3:
Label1:
	return
.limit stack 4
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
