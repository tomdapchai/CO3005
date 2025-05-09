.source Rectangle.java
.class public Rectangle
.super java/lang/Object
.implements Shape
.field width F
.field height F

.method public <init>(FF)V
.var 0 is this LRectangle; from Label0 to Label1
.var 1 is width F from Label0 to Label1
.var 2 is height F from Label0 to Label1
Label0:
	aload_0
	invokespecial java/lang/Object/<init>()V
	aload_0
	fload_1
	putfield Rectangle/width F
	aload_0
	fload_2
	putfield Rectangle/height F
Label1:
	return
.limit stack 2
.limit locals 3
.end method

.method public <init>()V
.var 0 is this LRectangle; from Label0 to Label1
Label0:
	aload_0
	invokespecial java/lang/Object/<init>()V
Label1:
	return
.limit stack 1
.limit locals 1
.end method

.method public area()F
.var 0 is this LRectangle; from Label0 to Label1
Label0:
Label2:
	aload_0
	getfield Rectangle/width F
	aload_0
	getfield Rectangle/height F
	fmul
	freturn
Label3:
Label1:
.limit stack 2
.limit locals 1
.end method

.method public perimeter()F
.var 0 is this LRectangle; from Label0 to Label1
Label0:
Label2:
	iconst_2
	i2f
	aload_0
	getfield Rectangle/width F
	aload_0
	getfield Rectangle/height F
	fadd
	fmul
	freturn
Label3:
Label1:
.limit stack 4
.limit locals 1
.end method
