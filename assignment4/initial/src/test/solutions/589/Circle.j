.source Circle.java
.class public Circle
.super java/lang/Object
.implements Shape
.field radius F

.method public <init>(F)V
.var 0 is this LCircle; from Label0 to Label1
.var 1 is radius F from Label0 to Label1
Label0:
	aload_0
	invokespecial java/lang/Object/<init>()V
	aload_0
	fload_1
	putfield Circle/radius F
Label1:
	return
.limit stack 2
.limit locals 2
.end method

.method public <init>()V
.var 0 is this LCircle; from Label0 to Label1
Label0:
	aload_0
	invokespecial java/lang/Object/<init>()V
Label1:
	return
.limit stack 1
.limit locals 1
.end method

.method public area()F
.var 0 is this LCircle; from Label0 to Label1
Label0:
Label2:
	ldc 3.14
	aload_0
	getfield Circle/radius F
	fmul
	aload_0
	getfield Circle/radius F
	fmul
	freturn
Label3:
Label1:
.limit stack 2
.limit locals 1
.end method

.method public perimeter()F
.var 0 is this LCircle; from Label0 to Label1
Label0:
Label2:
	iconst_2
	i2f
	ldc 3.14
	fmul
	aload_0
	getfield Circle/radius F
	fmul
	freturn
Label3:
Label1:
.limit stack 3
.limit locals 1
.end method
